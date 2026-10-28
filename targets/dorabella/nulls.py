"""Null-symbol hypotheses: drop one class of signs as filler and solve the rest.

Classes dropped in turn: each orientation (8), each arc count (3), and each of the 6 rarest symbols
together (the singletons A1 A2 C3 D2 G3 + H2). The remainder is solved as a strict substitution on
en-modern order 4 and compared with shuffles of Dorabella under the same drop, and with English
controls of the same remaining length.

python targets/dorabella/nulls.py [nulls]
"""
import os, sys, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora
from solve import anneal, text_of

HERE = os.path.dirname(os.path.abspath(__file__))
toks = open(os.path.join(HERE, 'ct.txt')).read().split()
m = lm.load('en-modern', order=4, spaces=False)
NN = int(sys.argv[1]) if len(sys.argv) > 1 else 5
drops = {f'orient {o}': (lambda t, o=o: t[0] == o) for o in 'ABCDEFGH'}
drops.update({f'arcs {c}': (lambda t, c=c: t[1] == c) for c in '123'})
drops['rare six'] = lambda t: t in {'A1', 'A2', 'C3', 'D2', 'G3', 'H2'}
corpus = lm.norm(corpora.text(['en-gutenberg'])[:2_000_000], 'modern', False)
rng = random.Random(4)


def solve_seq(seq, seed):
    syms = sorted(set(seq))
    ct = np.array([syms.index(t) for t in seq])
    sc, key = anneal(ct, len(syms), m, restarts=12, iters=15000, seed=seed, injective=True)
    return sc / len(ct), text_of(m, key, ct)


print(f'{"dropped":12s} {"n":>3s} {"Dorabella":>9s} {"nulls":>15s} {"controls":>15s}')
for name, f in drops.items():
    keep = [t for t in toks if not f(t)]
    n = len(keep)
    d, txt = solve_seq(keep, 0)
    nl = []
    for j in range(NN):
        sh = list(np.random.default_rng(j).permutation(toks))
        nl.append(solve_seq([t for t in sh if not f(t)], 100 + j)[0])
    cl = []
    for j in range(3):
        p = rng.randrange(len(corpus) - n)
        cl.append(solve_seq(list(corpus[p:p + n]), 200 + j)[0])
    print(f'{name:12s} {n:3d} {d:9.3f} {min(nl):7.3f}..{max(nl):6.3f} {min(cl):7.3f}..{max(cl):6.3f}  {txt}', flush=True)
