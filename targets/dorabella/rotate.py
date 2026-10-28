"""Orientation-rotation polyalphabetics: the orientation of token i is turned back by a key
that repeats with period p (a Vigenère on the dial), or advances linearly (o - a*i - b).
Arc counts are untouched. For each hypothesis the shifts that maximise the index of
coincidence are chosen (exhaustive for p <= 3, coordinate ascent above), the de-rotated text
is solved as a strict substitution, and the same procedure runs on shuffles (nulls), since
maximising IoC over free shifts overfits.

python targets/dorabella/rotate.py [nulls]
"""
import os, sys, random, itertools
from collections import Counter
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
from solve import anneal, text_of

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = [o + c for o in 'ABCDEFGH' for c in '123']
m = lm.load('en-modern', order=4, spaces=False)


def ioc(x):
    c = Counter(x.tolist()); n = len(x)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def derot(ct, shifts):
    p = len(shifts)
    return np.array([((t // 3 - shifts[i % p]) % 8) * 3 + t % 3 for i, t in enumerate(ct)])


def best_shifts(ct, p, rng):
    if p <= 3:
        cands = [(0,) + s for s in itertools.product(range(8), repeat=p - 1)]
        return max(cands, key=lambda s: ioc(derot(ct, s)))
    best = None
    for r in range(20):
        s = [0] + [rng.randrange(8) for _ in range(p - 1)]
        cur = ioc(derot(ct, s))
        improved = True
        while improved:
            improved = False
            for j in range(1, p):
                for v in range(8):
                    s2 = s.copy(); s2[j] = v
                    sc = ioc(derot(ct, s2))
                    if sc > cur + 1e-12:
                        s, cur, improved = s2, sc, True
        if best is None or cur > best[0]:
            best = (cur, tuple(s))
    return best[1]


def linear(ct, a):
    return np.array([((t // 3 - a * i) % 8) * 3 + t % 3 for i, t in enumerate(ct)])


def run(ct, tag, seed):
    rng = random.Random(seed)
    rows = []
    for p in range(1, 9):
        s = best_shifts(ct, p, rng)
        x = derot(ct, s)
        rows.append((f'period{p} {s}', x))
    for a in range(1, 8):
        rows.append((f'linear a={a}', linear(ct, a)))
    out = []
    for name, x in rows:
        syms = sorted(set(x.tolist()))
        y = np.array([syms.index(t) for t in x])
        sc, key = anneal(y, len(syms), m, restarts=10, injective=True)
        out.append((sc / len(y), name, ioc(x), len(syms), text_of(m, key, y)))
    for r in out:
        print(f'{tag:9s} {r[0]:.3f} ioc={r[2]:.4f} syms={r[3]:2d} {r[1]:28s} {r[4]}', flush=True)
    return max(out)


ct = np.array([TOK.index(t) for t in open(os.path.join(HERE, 'ct.txt')).read().split()])
best = run(ct, 'DORA', 0)
print('BEST DORA', best[:2], flush=True)
for j in range(int(sys.argv[1]) if len(sys.argv) > 1 else 3):
    b = run(np.random.default_rng(j).permutation(ct), f'null{j}', 100 + j)
    print(f'BEST null{j}', b[:2], flush=True)
