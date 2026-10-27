"""f. 307 runs: test key A as read off f. 279r, then a capped homophonic anneal with no word breaks (de-1500s, no spaces).

python targets/grumbach1564/solve307.py [restarts]
"""
import math, random, re, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lang import lm

ALPHA = 'abcdefghiklmnopqrstuwz'
CAP = {c: 2 for c in ALPHA}; CAP.update(e=3, n=3)
# key A (f. 279r) cipher shape -> plain, using the shape labels of f307_runs.txt
KEY_A = dict(g='s', o='u', u='r', m='i', y='e', d='w', b='l', z='h', q='a', E='b', f='t', a='f', X='k', x='d', w='z', P='o', L='n')


def runs(path):
    out = []
    for line in Path(path).read_text(encoding='utf8').splitlines():
        if not line.startswith(('R', 'V')):
            continue
        body = re.sub(r'\[[^\]]*\]', ' ', line.split(None, 1)[1])
        out += [r for r in body.split() if r]
    return out


def anneal(seqs, model, restarts=10, steps=40000, seed=1):
    signs = sorted({c for s in seqs for c in s})
    rnd = random.Random(seed)
    def text(m): return ' '.join(''.join(m[c] for c in s) for s in seqs)
    def sc(m): return sum(model.score(''.join(m[c] for c in s)) for s in seqs)
    best = (-1e9, None)
    for r in range(restarts):
        cnt = Counter(); m = {}
        for s in signs:
            m[s] = rnd.choice([c for c in ALPHA if cnt[c] < CAP[c]]); cnt[m[s]] += 1
        cur = sc(m)
        for i in range(steps):
            T = max(0.05, 4.0 * (1 - i / steps))
            a = rnd.choice(signs)
            if rnd.random() < 0.5:
                b = rnd.choice(signs)
                if m[a] == m[b]: continue
                m[a], m[b] = m[b], m[a]; new = sc(m)
                if new >= cur or rnd.random() < math.exp((new - cur) / T): cur = new
                else: m[a], m[b] = m[b], m[a]
            else:
                c = rnd.choice(ALPHA); old = m[a]
                if c == old or cnt[c] >= CAP[c]: continue
                m[a] = c; cnt[old] -= 1; cnt[c] += 1; new = sc(m)
                if new >= cur or rnd.random() < math.exp((new - cur) / T): cur = new
                else: m[a] = old; cnt[old] += 1; cnt[c] -= 1
        n = sum(map(len, seqs))
        print(f'restart {r}: {cur/n:.3f} {text(m)[:120]}', flush=True)
        if cur > best[0]: best = (cur, dict(m))
    return best, text(best[1])


if __name__ == '__main__':
    seqs = runs(Path(__file__).with_name('f307_runs.txt'))
    n = sum(map(len, seqs))
    print(len(seqs), 'runs', n, 'signs', Counter(''.join(seqs)).most_common())
    model = lm.load('de-1500s', spaces=False)
    ka = ' '.join(''.join(KEY_A.get(c, '?') for c in s) for s in seqs)
    print('KEY A:', round(sum(model.score(w.replace('?', 'x')) for w in ka.split()) / n, 3), ka)
    (s, m), t = anneal(seqs, model, int(sys.argv[1]) if len(sys.argv) > 1 else 10)
    print('BEST', round(s / n, 3)); print(' '.join(f'{k}={v}' for k, v in sorted(m.items()))); print(t)
