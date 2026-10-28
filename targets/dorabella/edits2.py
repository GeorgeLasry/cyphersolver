"""Misread-tolerant substitution, alternating search (edits.py's joint anneal was underpowered).

Each restart: anneal the key on the current reading; then greedily apply the orientation slips
(neighbouring orientation, same arcs) that raise the score by more than LAMBDA, up to K; re-anneal
the key from where it is; three rounds. Controls are English in Dorabella's tokens with K slips;
nulls are shuffles of Dorabella with the same budget.

python targets/dorabella/edits2.py [K] [LAMBDA] [restarts] [controls]
"""
import os, sys, random, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = [o + c for o in 'ABCDEFGH' for c in '123']
K = int(sys.argv[1]) if len(sys.argv) > 1 else 6
LAMBDA = float(sys.argv[2]) if len(sys.argv) > 2 else 4.0
R = int(sys.argv[3]) if len(sys.argv) > 3 else 12
NC = int(sys.argv[4]) if len(sys.argv) > 4 else 6
m = lm.load('en-modern', order=4, spaces=False)
A = m.A


def nb(t, d):
    return ((t // 3 + d) % 8) * 3 + t % 3


def anneal_key(c, key, rng, iters, T0):
    cur = m.score_idx(key[c])
    for i in range(iters):
        T = T0 * (1 - i / iters) + 0.05
        k2 = key.copy()
        s = rng.randrange(24)
        if rng.random() < 0.3:
            free = [a for a in range(A) if a not in set(k2.tolist())]
            k2[s] = rng.choice(free)
        else:
            t = rng.randrange(24)
            k2[s], k2[t] = k2[t], k2[s]
        sc = m.score_idx(k2[c])
        if sc >= cur or rng.random() < math.exp((sc - cur) / T):
            key, cur = k2, sc
    return key, cur


def greedy_edits(ct, c, key, off):
    while np.count_nonzero(off) < K:
        base = m.score_idx(key[c])
        best = (LAMBDA, None)
        for p in range(len(ct)):
            if off[p]:
                continue
            for d in (-1, 1):
                c2 = c.copy(); c2[p] = nb(ct[p], d)
                g = m.score_idx(key[c2]) - base
                if g > best[0]:
                    best = (g, (p, d))
        if best[1] is None:
            break
        p, d = best[1]
        off[p] = d; c[p] = nb(ct[p], d)
    return c, off


def solve(ct, seed):
    rng = random.Random(seed)
    best = (-1e18,)
    for r in range(R):
        key = np.array(rng.sample(range(A), 24))
        off = np.zeros(len(ct), dtype=np.int64)
        c = ct.copy()
        key, sc = anneal_key(c, key, rng, 20000, 3.0)
        for rnd in range(3):
            c, off = greedy_edits(ct, c, key, off)
            key, sc = anneal_key(c, key, rng, 8000, 0.8)
        tot = sc - LAMBDA * np.count_nonzero(off)
        if tot > best[0]:
            best = (tot, key.copy(), c.copy(), off.copy())
    return best


def show(tag, res, truth=None):
    tot, key, c, off = res
    txt = ''.join(m.alpha[i] for i in key[c])
    extra = f' acc={np.mean(key[c] == truth):.2f}' if truth is not None else ''
    print(f'{tag:10s} {tot / len(c):.3f} edits={np.count_nonzero(off)}{extra} {txt}', flush=True)


ct = np.array([TOK.index(t) for t in open(os.path.join(HERE, 'ct.txt')).read().split()])
n = len(ct)
print(f'K={K} lambda={LAMBDA} restarts={R}', flush=True)
res = solve(ct, 0)
show('DORABELLA', res)
print('  edited:', [(int(p), TOK[ct[p]], TOK[res[2][p]]) for p in np.nonzero(res[3])[0]], flush=True)
rng = random.Random(7)
corpus = lm.norm(corpora.text(lm.registry()[0]['en-modern']['sources'])[:3_000_000], 'modern', False)
for j in range(NC):
    p = rng.randrange(len(corpus) - n)
    pt = m.encode(corpus[p:p + n])
    tok_of = dict(zip(sorted(set(pt.tolist())), rng.sample(range(24), 24)))
    cx = np.array([tok_of[l] for l in pt])
    for q in rng.sample(range(n), K):
        cx[q] = nb(cx[q], rng.choice((-1, 1)))
    show(f'control{j}', solve(cx, 10 + j), truth=pt)
for j in range(NC):
    show(f'null{j}', solve(np.random.default_rng(j).permutation(ct), 100 + j))
