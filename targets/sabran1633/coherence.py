"""Word cover of George Lasry's reading: share of the deciphered text (letters plus the firm word codes) that falls
in French words of 3+ letters (fr-henri4 vocabulary, words seen 5+ times, DP maximum cover, early-modern spelling
normalised by lang.lm.norm). Name codes break the runs. Same vocabulary as measure.py, the 21 Oct 2026 check of
the earlier contributed reading. Baluze 155 (Lasry's 2022 decipherment, read in full) shows the measure's ceiling.
  python coherence.py"""
import collections, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm
import decode

corp = open(os.path.join(HERE, '..', '..', 'lang', 'corpora', 'fr-henri4.txt'), encoding='utf-8').read()
cnt = collections.Counter(lm.norm(corp, 'early').split())
VOC = {w for w, n in cnt.items() if n >= 5 and len(w) >= 3}


def covered(s):
    best = [0] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        b = best[i - 1]
        for L in range(3, min(16, i) + 1):
            if s[i - L:i] in VOC:
                b = max(b, best[i - L] + L)
        best[i] = b
    return best[-1]


def runs(rows, sub=None):
    out, cur = [], ''
    for img, s, v, c in rows:
        if c == 'letter':
            cur += sub[s] if sub else v
        elif c == 'code' and not v.startswith('['):
            cur += v.lower()
        elif cur:
            out.append(cur)
            cur = ''
    if cur:
        out.append(cur)
    return out


def score(rs):
    rs = [lm.norm(r, 'early').replace(' ', '') for r in rs]
    return sum(covered(r) for r in rs), sum(len(r) for r in rs)


if __name__ == '__main__':
    rows = list(decode.tokens())
    a, b = score(runs(rows))
    print(f'reading: {a}/{b} = {a/b:.3f}')
    per = collections.defaultdict(list)
    for r in rows:
        per[decode.source(r[0])].append(r)
    for k, v in per.items():
        x, y = score(runs(v))
        print(f'  {k}: {x}/{y} = {x/y:.3f}')
    signs = sorted({s for _, s, _, c in rows if c == 'letter'})
    vals = {s: v for _, s, v, c in rows if c == 'letter'}
    rng, res = random.Random(1), []
    for _ in range(20):
        vv = [vals[s] for s in signs]
        rng.shuffle(vv)
        x, y = score(runs(rows, dict(zip(signs, vv))))
        res.append(x / y)
    res.sort()
    print(f'shuffled letter keys (n=20): median {res[10]:.3f}, max {res[-1]:.3f}')
