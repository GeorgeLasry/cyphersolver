"""Align a Deboli cipher despatch (ZbPop 17) with the clear despatch of the same day (ZbPop 419).

The cipher is a one-part syllabary: groups are numbered in alphabetical order of their values, in more than one
ordered run (a long run from 1 up, then a second run of whole words and syllables above about 1700). Each group stands
for 0-6 letters of the clear text. A banded DP finds the cheapest segmentation of the clear text, scoring each
(group, piece) pair by whether the piece sorts between the values of the nearest known groups below and above it in
the same run. Pairs seen often and consistently become anchors for the next pass.

usage: python align.py c001_1789-01-06 p002_1789-01-06 [--boundary 1700] [--iters 6] [--out key_pass.tsv]
"""
import argparse, collections, json, math, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
TR = str.maketrans({'ł': 'l', 'Ł': 'l'})

SEED = {  # hand alignments on the 6 Jan 1789 pair (NOTES.md)
    '1559': 'w', '1560': 'wa', '1262': 'ru', '780': 'n', '461': 'ka', '466': 'ko', '692': 'mi',
    '623': 'lo', '2150': 'cya', '895': 'nie', '961': 'on', '1900': 'aby', '1926': 'ale',
}


def norm(t):
    t = t.translate(TR).lower()
    t = unicodedata.normalize('NFD', t)
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]', '', t)


def read_cipher(path):
    toks = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or ':' not in line:
            continue
        loc, body = line.split(':', 1)
        body = re.sub(r'\[clear:\s*([^\]]*)\]', lambda m: ' =' + norm(m.group(1)) + ' ', body)
        body = re.sub(r'\[[^\]]*\]', ' ', body)
        for t in body.split():
            unsure = '?' in t
            t = t.replace('?', '')
            base, _, mark = t.partition('^')
            toks.append((base, loc.strip(), unsure))
            if mark.isdigit():  # a group written above another: inserted after it
                toks.append((mark, loc.strip(), unsure))
    return toks


def read_clear(path):
    t = ' '.join(l for l in open(path, encoding='utf-8') if not l.startswith('#'))
    return norm(re.sub(r'\[struck:[^\]]*\]', ' ', t))


def num(v):
    m = re.match(r'\d+', v)
    return int(m.group()) if m else -1


class Order:
    def __init__(self, anchors, boundary):
        self.a = anchors
        self.b = boundary
        self.runs = [sorted((num(v), s) for v, s in anchors.items() if s and (num(v) >= boundary) == hi) for hi in (False, True)]

    def bounds(self, v):
        n = num(v)
        run = self.runs[n >= self.b]
        lo, hi = '', '{'
        for k, s in run:
            if k < n:
                lo = s
            elif k > n:
                hi = s
                break
        return lo, hi


LEN_COST = {0: 7.0, 1: 1.2, 2: 0.6, 3: 0.9, 4: 1.6, 5: 2.6, 6: 3.4, 7: 4.0, 8: 4.6, 9: 5.2, 10: 5.8}


def cost(v, s, order):
    if v.startswith('='):
        return 0.0 if s == v[1:] else 9.0
    if v in order.a:
        return 0.0 if order.a[v] == s else 9.0
    c = LEN_COST[len(s)]
    if s:
        lo, hi = order.bounds(v)
        if not (lo <= s <= hi or (lo <= s and hi.startswith(s))):
            c += 4.0
    return c


def align(toks, text, order, band=260, skip=6.0, maxlen=10, beam=35.0):
    n, m = len(toks), len(text)
    band = max(band, int(0.15 * m))
    INF = 1e18
    ratio = m / max(n, 1)
    D = [dict() for _ in range(n + 1)]
    D[0][0] = (0.0, None)
    for i in range(n):
        v = toks[i][0]
        centre = int((i + 1) * ratio)
        for j, (c0, _) in D[i].items():
            for L in range(0, maxlen + 1):
                jj = j + L
                if jj > m or abs(jj - centre) > band:
                    continue
                c = c0 + cost(v, text[j:jj], order)
                if c < D[i + 1].get(jj, (INF,))[0]:
                    D[i + 1][jj] = (c, (j, 0))
        # beam: drop states far behind the best one
        if D[i + 1]:
            best = min(c for c, _ in D[i + 1].values())
            D[i + 1] = {j: x for j, x in D[i + 1].items() if x[0] <= best + beam}
        # skipped plaintext letters (cipher omits them)
        for jj in sorted(D[i + 1]):
            c, bp = D[i + 1][jj]
            for k in (1, 2):
                if jj + k <= m:
                    c2 = c + skip * k
                    if c2 < D[i + 1].get(jj + k, (INF,))[0]:
                        D[i + 1][jj + k] = (c2, (jj, 1))
    end = min(D[n], key=lambda j: D[n][j][0] + skip * (m - j))
    total = D[n][end][0] + skip * (m - end)
    out, i, j = [], n, end
    while i > 0:
        c, (pj, kind) = D[i][j]
        if kind == 1:
            j = pj
            continue
        out.append((toks[i - 1], text[pj:j]))
        i, j = i - 1, pj
    return total, out[::-1], m - end


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pairs', nargs='+', help='cipher/clear stems, alternating')
    ap.add_argument('--boundary', type=int, default=1700)
    ap.add_argument('--iters', type=int, default=6)
    ap.add_argument('--out', default='key_pass.tsv')
    ap.add_argument('--seed', default='seed.tsv')
    a = ap.parse_args()
    pairs = [(read_cipher(os.path.join(HERE, 'transcription', a.pairs[k] + '.txt')),
              read_clear(os.path.join(HERE, 'clear', a.pairs[k + 1] + '.txt'))) for k in range(0, len(a.pairs), 2)]
    anchors = dict(SEED)
    if a.seed:
        for line in open(os.path.join(HERE, a.seed), encoding='utf-8'):
            p = line.rstrip('\n').split('\t')
            if len(p) >= 2 and p[0] and not p[0].startswith('#') and p[1] != '?':
                SEED[p[0]] = p[1]
    anchors.update(SEED)
    for it in range(a.iters):
        order = Order(anchors, a.boundary)
        seen = collections.defaultdict(collections.Counter)
        tot = 0
        for toks, text in pairs:
            c, out, left = align(toks, text, order)
            tot += c
            for (v, loc, unsure), s in out:
                seen[v][s] += 1
        new = dict(SEED)
        for v, cnt in seen.items():
            s, k = cnt.most_common(1)[0]
            if s and k >= 2 and k / sum(cnt.values()) >= 0.6:
                new[v] = s
            elif cnt[''] >= 5 and cnt[''] / sum(cnt.values()) >= 0.2 and max((y for x, y in cnt.items() if x), default=0) <= 3:
                new[v] = ''  # null: aligned to nothing more often than to any value
        # drop anchors that break the order inside their run
        for hi in (False, True):
            run = sorted((num(v), v, s) for v, s in new.items() if (num(v) >= a.boundary) == hi and v not in SEED and s)
            for idx, (n, v, s) in enumerate(run):
                prev = [x for x in run[:idx]][-2:]
                nxt = run[idx + 1:idx + 3]
                bad = sum(1 for _, _, p in prev if p > s) + sum(1 for _, _, q in nxt if q < s and not s.startswith(q))
                if bad >= 3:
                    new.pop(v, None)
        print(f'pass {it}: cost {tot:.0f}, anchors {len(anchors)} -> {len(new)}', file=sys.stderr)
        if new == anchors:
            break
        anchors = new
    order = Order(anchors, a.boundary)
    with open(os.path.join(HERE, a.out), 'w', encoding='utf-8') as f:
        f.write('# group\tvalue\tcount\talternatives\n')
        for v in sorted(seen, key=lambda v: (num(v), v)):
            cnt = seen[v]
            s, k = cnt.most_common(1)[0]
            f.write(f'{v}\t{s}\t{k}/{sum(cnt.values())}\t{" ".join(f"{x or "-"}:{y}" for x, y in cnt.most_common()[1:])}\n')
    for idx, (toks, text) in enumerate(pairs):
        c, out, left = align(toks, text, order)
        with open(os.path.join(HERE, f'align_{a.pairs[2 * idx]}.txt'), 'w', encoding='utf-8') as f:
            line, buf = None, []
            for (v, loc, unsure), s in out:
                if loc != line:
                    if buf:
                        f.write(f'{line}: ' + ' '.join(buf) + '\n')
                    line, buf = loc, []
                buf.append(f'{v}={s or "-"}')
            f.write(f'{line}: ' + ' '.join(buf) + '\n')
            f.write(f'# unaligned clear letters at end: {left}\n')


if __name__ == '__main__':
    main()
