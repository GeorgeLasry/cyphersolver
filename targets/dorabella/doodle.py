"""Motor signature test: do consecutive signs turn gradually, as a hand doodling squiggles would?

Statistics on consecutive pairs: mean circular orientation step |do| (0-4), share of steps of 0 or
+-1 (45 deg), share of steps of exactly +1 or -1 (a sweep), same-arc-count share, and the longest run
of one-way +-1 sweeps. Compared with 5,000 shuffles of Dorabella (same symbols, order destroyed) and
with English enciphered (a) under random keys and (b) under Elgar's own ordered table (letters in order
round the dial), 87 letters each.

python targets/dorabella/doodle.py
"""
import os, sys, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = [o + c for o in 'ABCDEFGH' for c in '123']
ct = np.array([TOK.index(t) for t in open(os.path.join(HERE, 'ct.txt')).read().split()])


def stats(x):
    o, c = x // 3, x % 3
    d = (o[1:] - o[:-1]) % 8
    step = np.minimum(d, 8 - d)
    sweep, best, cur, last = (d == 1) | (d == 7), 0, 0, 0
    for k in d:
        if k in (1, 7) and (cur == 0 or k == last):
            cur += 1
        else:
            cur = 1 if k in (1, 7) else 0
        last = k
        best = max(best, cur)
    return np.array([step.mean(), (step <= 1).mean(), ((d == 1) | (d == 7)).mean(), (c[1:] == c[:-1]).mean(), best])


names = ['mean |step|', 'step<=1', 'step=+-1', 'same arcs', 'longest sweep']
D = stats(ct)
rng = np.random.default_rng(0)
S = np.array([stats(rng.permutation(ct)) for _ in range(5000)])
r = random.Random(1)
corpus = lm.norm(corpora.text(['en-gutenberg'])[:3_000_000], 'early', False)
AL = 'abcdefghiklmnopqrstuwxyz'
E_rand, E_elgar = [], []
for _ in range(2000):
    p = r.randrange(len(corpus) - 200)
    pt = [AL.index(ch) for ch in corpus[p:p + 200] if ch in AL][:87]
    key = r.sample(range(24), 24)
    E_rand.append(stats(np.array([key[v] for v in pt])))
    E_elgar.append(stats(np.array(pt)))                    # letter index = 3*orientation + arcs
E_rand, E_elgar = np.array(E_rand), np.array(E_elgar)
print(f'{"statistic":14s} {"Dorabella":>9s} {"shuffle mean":>12s} {"P(shuffle>=D)":>13s} {"P(shuffle<=D)":>13s} {"Eng rand key":>12s} {"Eng Elgar key":>13s}')
for i, nme in enumerate(names):
    print(f'{nme:14s} {D[i]:9.3f} {S[:, i].mean():12.3f} {(S[:, i] >= D[i]).mean():13.4f} {(S[:, i] <= D[i]).mean():13.4f}'
          f' {E_rand[:, i].mean():12.3f} {E_elgar[:, i].mean():13.3f}')
