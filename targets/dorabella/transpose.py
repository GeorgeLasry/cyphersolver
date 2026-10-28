"""Transposition-then-substitution and space-symbol tests.

For each reordering of the 87 symbols (line reversals, boustrophedon, column reads of the
three lines, decimations, rail fences) solve the result as a substitution on en-modern
order 4, with and without word spaces in the model. Print each with its score; compare
against solve.py's controls (about -1.7 no spaces) and nulls (about -2.2)."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
from solve import anneal, text_of

HERE = os.path.dirname(os.path.abspath(__file__))
lines = [l.split() for l in open(os.path.join(HERE, 'ct.txt')).read().strip().splitlines()]
syms = sorted({t for l in lines for t in l})
L = [[syms.index(t) for t in l] for l in lines]
flat = sum(L, [])
n = len(flat)


def columns(rows):
    out = []
    for i in range(max(map(len, rows))):
        out += [r[i] for r in rows if i < len(r)]
    return out


def rail(seq, k):
    rows = [[] for _ in range(k)]
    period = 2 * (k - 1)
    for i, x in enumerate(seq):
        p = i % period
        rows[p if p < k else period - p].append(x)
    return sum(rows, [])


def unrail(seq, k):
    period = 2 * (k - 1)
    pat = [(i % period) if (i % period) < k else period - (i % period) for i in range(len(seq))]
    order = sorted(range(len(seq)), key=lambda i: (pat[i], i))
    out = [None] * len(seq)
    for j, i in enumerate(order):
        out[i] = seq[j]
    return out


T = {'identity': flat, 'reverse': flat[::-1],
     'boustrophedon': L[0] + L[1][::-1] + L[2],
     'lines-reversed-each': L[0][::-1] + L[1][::-1] + L[2][::-1],
     'line-order-321': L[2] + L[1] + L[0],
     'columns': columns(L), 'columns-rev': columns(L)[::-1]}
for k in range(2, 12):
    for start in range(k):
        T[f'decimate{k}+{start}'] = [flat[(start + i * k) % n] for i in range(n)] if np.gcd(k, n) == 1 else None
for k in range(2, 6):
    T[f'rail{k}'] = rail(flat, k)
    T[f'unrail{k}'] = unrail(flat, k)
for w in range(2, 30):        # columnar read with width w, in written order
    T[f'colw{w}'] = [flat[c + r * w] for c in range(w) for r in range((n - c + w - 1) // w)]

for j in range(6):            # shuffles: the score a meaningless reordering reaches
    T[f'null{j}'] = list(np.random.default_rng(j).permutation(flat))

INJ = "--injective" in sys.argv
spaces = "--spaces" in sys.argv
m = lm.load('en-modern', order=4, spaces=spaces)
out = []
for name, seq in T.items():
    if seq is None:
        continue
    ct = np.array(seq)
    sc, key = anneal(ct, len(syms), m, restarts=8, iters=15000, injective=INJ)
    out.append((sc / n, name, text_of(m, key, ct)))
    print(f'{sc / n:.3f} {name:22s} {text_of(m, key, ct)}', flush=True)
print('--- best')
for r in sorted(out, reverse=True)[:10]:
    print(f'{r[0]:.3f} {r[1]:22s} {r[2]}')
