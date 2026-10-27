"""Give values to the groups the pairs never showed, from the alphabetical order of the code and a Polish LM.

The code is one-part: a group's value sorts between the values of the nearest known groups below and above it in the
same run. For every unknown group, each candidate value inside that bracket (syllables and words seen in the corpus,
plus null) is tried at all its occurrences in the letters given, and the candidate whose windows score best under the
pl-1790 model (no spaces, with a per-letter allowance so long and short values compete fairly) is kept. Several sweeps,
most frequent groups first.

usage: python fill.py c107_1789-12-22 c108_1789-12-25 c109_1789-12-29 [--key key_pass.tsv] [--out key_fill.tsv]
control: python fill.py c106_1789-12-18 --key key_loo.tsv --exclude p105_1789-12-18 --truth p105_1789-12-18
"""
import argparse, collections, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
from align import read_cipher, read_clear, num  # noqa: E402
from lang import lm  # noqa: E402

BONUS = 2.1  # per-letter allowance, about the model's mean cost per letter


def load_key(path):
    key = {}
    for line in open(path, encoding='utf-8'):
        if line.startswith('#'):
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) >= 2 and p[0]:
            key[p[0]] = p[1]
    return key


def model(exclude):
    if not exclude:
        return lm.load('pl-1790', spaces=False)
    # control: the same corpus without the held-out clear despatch, built in memory
    src = open(os.path.join(ROOT, 'lang', 'corpora', 'pl-1790.txt'), encoding='utf-8').read()
    held = ''.join(l for l in open(os.path.join(HERE, 'clear', exclude + '.txt'), encoding='utf-8') if not l.startswith('#'))
    held = re.sub(r'\[struck:[^\]]*\]|\[\?\]', ' ', held)
    src = src.replace(held, ' ')
    text = lm.norm(src, 'modern', False)
    return lm.DenseLM.build(text, 5, lm.alphabet('modern', False))


def candidates(m_text, maxlen=8, top=40000):
    c = collections.Counter()
    for w in re.findall(r'[a-z]+', m_text):
        for i in range(len(w)):
            for L in range(1, maxlen + 1):
                if i + L <= len(w):
                    c[w[i:i + L]] += 1
    return [s for s, _ in c.most_common(top)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('stems', nargs='+')
    ap.add_argument('--key', default='key_pass.tsv')
    ap.add_argument('--out', default='key_fill.tsv')
    ap.add_argument('--boundary', type=int, default=1860)
    ap.add_argument('--exclude', default='')
    ap.add_argument('--truth', default='')
    ap.add_argument('--sweeps', type=int, default=3)
    ap.add_argument('--minocc', type=int, default=1)
    ap.add_argument('--bonus', type=float, default=BONUS)
    ap.add_argument('--maxlen', type=int, default=8)
    a = ap.parse_args()
    key = load_key(os.path.join(HERE, a.key))
    m = model(a.exclude)
    corpus = open(os.path.join(ROOT, 'lang', 'corpora', 'pl-1790.txt'), encoding='utf-8').read()
    if a.exclude:
        held = ''.join(l for l in open(os.path.join(HERE, 'clear', a.exclude + '.txt'), encoding='utf-8') if not l.startswith('#'))
        corpus = corpus.replace(re.sub(r'\[struck:[^\]]*\]|\[\?\]', ' ', held), ' ')
    vocab = candidates(lm.norm(corpus[:3_000_000], 'modern', True), a.maxlen) + sorted(set(v for v in key.values() if v))
    vocab = sorted(set(vocab))

    letters = []
    for st in a.stems:
        toks = [v for v, _, _ in read_cipher(os.path.join(HERE, 'transcription', st + '.txt'))]
        toks = [t if t in key or t.startswith('=') else (re.sub(r'[a-z]+$', '', t) if re.sub(r'[a-z]+$', '', t) in key else t) for t in toks]
        letters.append(toks)
    known = {k: v for k, v in key.items()}
    occ = collections.defaultdict(list)
    for li, toks in enumerate(letters):
        for i, t in enumerate(toks):
            if t not in known and not t.startswith('='):
                occ[t].append((li, i))
    runs = {hi: sorted((num(k), v) for k, v in known.items() if v and (num(k) >= a.boundary) == hi) for hi in (False, True)}

    def bracket(t):
        n, run = num(t), runs[num(t) >= a.boundary]
        lo = max((x for x in run if x[0] < n), default=(0, ''))[1]
        hi = min((x for x in run if x[0] > n), default=(0, '{'))[1]
        return lo, hi

    import bisect
    guess = {}
    for t in occ:
        lo, hi = bracket(t)
        guess[t] = lo  # start from the lower neighbour's value

    def val(t):
        if t.startswith('='):
            return t[1:]
        return known.get(t, guess.get(t, ''))

    def window(li, i, t, s, w=5):
        toks = letters[li]
        left = ''.join(val(x) for x in toks[max(0, i - w):i])[-10:]
        right = ''.join(val(x) for x in toks[i + 1:i + 1 + w])[:10]
        return left, right

    def score(t, s):
        tot = 0.0
        for li, i in occ[t]:
            left, right = window(li, i, t, s)
            tot += m.score(left + s + right) - m.score(left + right) + a.bonus * len(s)
        return tot

    order = sorted(occ, key=lambda t: -len(occ[t]))
    for sw in range(a.sweeps):
        changed = 0
        for t in order:
            if len(occ[t]) < a.minocc:
                continue
            lo, hi = bracket(t)
            i0, i1 = bisect.bisect_left(vocab, lo), bisect.bisect_right(vocab, hi)
            cands = [''] + vocab[i0:i1]
            best = max(cands, key=lambda s: score(t, s))
            if best != guess.get(t):
                guess[t] = best
                changed += 1
        print(f'sweep {sw}: {changed} changed, {len(order)} unknown groups', file=sys.stderr)
        if not changed:
            break

    with open(os.path.join(HERE, a.out), 'w', encoding='utf-8') as f:
        f.write('# group\tvalue\tsource\toccurrences\tbracket\n')
        for t in sorted(set(list(known) + list(guess)), key=lambda x: (num(x), x)):
            if t in known:
                f.write(f'{t}\t{known[t]}\tpairs\t\t\n')
            else:
                lo, hi = bracket(t)
                f.write(f'{t}\t{guess[t]}\tfill\t{len(occ[t])}\t{lo}~{hi}\n')
    for st, toks in zip(a.stems, letters):
        with open(os.path.join(HERE, f'fill_{st}.txt'), 'w', encoding='utf-8') as f:
            f.write(' '.join((val(t) if (t in known or t.startswith('=')) else '[' + val(t) + ']') or '-' for t in toks) + '\n')
    if a.truth:
        truth = read_clear(os.path.join(HERE, 'clear', a.truth + '.txt'))
        import difflib
        for st, toks in zip(a.stems, letters):
            hidden = [t for t in toks if t not in known and not t.startswith('=')]
            got = ''.join(val(t) for t in toks)
            sm = difflib.SequenceMatcher(None, got, truth, autojunk=False)
            print(f'{st}: {len(hidden)}/{len(toks)} tokens filled; letters matching the clear text: '
                  f'{sum(b.size for b in sm.get_matching_blocks())}/{len(truth)} ({sm.ratio():.3f} ratio)')


if __name__ == '__main__':
    main()
