"""Error-tolerant substitution: the key and up to K misread symbols are searched together.

A misreading is modelled as the neighbouring orientation (A<->B ... H<->A) with the same arc
count, the confusion a slanted semicircle invites. Key domain = all 24 tokens, injective onto
26 letters. Each edit costs LAMBDA nats. Run on Dorabella, on shuffles of it (nulls, same budget),
and on English controls written in Dorabella's tokens with K orientation slips added.

python targets/dorabella/edits.py [K] [LAMBDA] [restarts]
"""
import os, sys, random, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = [o + c for o in 'ABCDEFGH' for c in '123']        # index = 3*orient + (arcs-1)
K = int(sys.argv[1]) if len(sys.argv) > 1 else 6
LAMBDA = float(sys.argv[2]) if len(sys.argv) > 2 else 4.0
R = int(sys.argv[3]) if len(sys.argv) > 3 else 12
m = lm.load('en-modern', order=4, spaces=False)
A = m.A


def neighbour(t, d):
    return ((t // 3 + d) % 8) * 3 + t % 3


def solve(ct, seed, iters=40000):
    rng = random.Random(seed)
    n = len(ct)
    best = (-1e18, None, None)
    for r in range(R):
        key = np.array(rng.sample(range(A), 24))
        off = np.zeros(n, dtype=np.int64)              # -1, 0, +1 orientation slip per position
        def cur_ct(off):
            return np.array([neighbour(t, d) if d else t for t, d in zip(ct, off)])
        c = cur_ct(off)
        cur = m.score_idx(key[c]) - LAMBDA * np.count_nonzero(off)
        for i in range(iters):
            T = 3.0 * (1 - i / iters) + 0.05
            k2, o2 = key, off
            u = rng.random()
            if u < 0.25:
                o2 = off.copy()
                p = rng.randrange(n)
                o2[p] = 0 if off[p] else rng.choice((-1, 1))
                if np.count_nonzero(o2) > K:
                    continue
            elif u < 0.45:
                k2 = key.copy()
                free = [a for a in range(A) if a not in set(k2.tolist())]
                k2[rng.randrange(24)] = rng.choice(free)
            else:
                k2 = key.copy()
                s, t = rng.randrange(24), rng.randrange(24)
                k2[s], k2[t] = k2[t], k2[s]
            c2 = cur_ct(o2) if o2 is not off else c
            sc = m.score_idx(k2[c2]) - LAMBDA * np.count_nonzero(o2)
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, off, c, cur = k2, o2, c2, sc
        if cur > best[0]:
            best = (cur, key.copy(), off.copy())
    return best


def show(tag, ct, res, truth=None):
    sc, key, off = res
    c = np.array([neighbour(t, d) if d else t for t, d in zip(ct, off)])
    txt = ''.join(m.alpha[i] for i in key[c])
    extra = f' acc={np.mean(key[c] == truth):.2f}' if truth is not None else ''
    print(f'{tag:10s} {sc / len(ct):.3f} edits={np.count_nonzero(off)}{extra} {txt}', flush=True)
    return txt, off


ct = np.array([TOK.index(t) for t in open(os.path.join(HERE, 'ct.txt')).read().split()])
n = len(ct)
print(f'K={K} lambda={LAMBDA} restarts={R}')
txt, off = show('DORABELLA', ct, solve(ct, 0))
print('  edited positions:', [(int(p), TOK[ct[p]], TOK[neighbour(ct[p], off[p])]) for p in np.nonzero(off)[0]])
rng = random.Random(7)
corpus = lm.norm(corpora.text(lm.registry()[0]['en-modern']['sources'])[:3_000_000], 'modern', False)
for j in range(6):
    p = rng.randrange(len(corpus) - n)
    pt = m.encode(corpus[p:p + n])
    tok_of = dict(zip(sorted(set(pt.tolist())), rng.sample(range(24), 24)))
    cx = np.array([tok_of[l] for l in pt])
    for q in rng.sample(range(n), K):
        cx[q] = neighbour(cx[q], rng.choice((-1, 1)))
    show(f'control{j}', cx, solve(cx, 10 + j), truth=pt)
for j in range(6):
    show(f'null{j}', np.random.default_rng(j).permutation(ct), solve(np.random.default_rng(j).permutation(ct), 100 + j))
