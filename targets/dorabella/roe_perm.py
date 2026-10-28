"""Roe grid with ANY group order round the dial, plus a keyword (Vigenère) or running dial shift.

pallmall.py tried only the 16 cyclic group orders. Here: orientation o -> Roe group pi(o), pi any
permutation of 8; arc count -> place in the group, ascending or descending. Under an additive key over
the 24-letter Roe alphabet, rotating pi only adds a multiple of 3 to every key letter, so pi(0) = 0 is
fixed: 5,040 orders x 2 arc orders. Keys: periodic p = 1-12, or k_i = a*i + b (a = 1-23).
Stage 1: each column's shift by chi-square on English frequencies, then n-gram score. Stage 2: the top
TOP candidates get their key refined by coordinate ascent on the n-gram score.

python targets/dorabella/roe_perm.py [nulls] [controls]
"""
import os, sys, random, itertools
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = [o + c for o in 'ABCDEFGH' for c in '123']
ROE = 'abcdefghiklmnopqrstuwxyz'
EN = dict(zip('abcdefghijklmnopqrstuvwxyz', [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, .15, .77, 4.0, 2.4,
                                             6.7, 7.5, 1.9, .1, 6.0, 6.3, 9.1, 2.8, .98, 2.4, .15, 2.0, .07]))
F = np.array([EN[c] + (EN['j'] if c == 'i' else 0) + (EN['v'] if c == 'u' else 0) for c in ROE])
F = F / F.sum()
TOP = 300
m = lm.load('en-modern', order=4, spaces=False)
R2M = np.array([m.index[c] for c in ROE])              # Roe index -> model index
ROLL = (np.arange(24)[None, :] + np.arange(24)[:, None]) % 24   # ROLL[s, x] = x + s


def lmscore(x):
    return m.score_idx(R2M[x]) / len(x)


def chi_shift(col):
    c = np.bincount(col, minlength=24)[ROLL]          # c[s, x] = count of (x + s): plaintext x under shift s
    e = F * len(col)
    return int(np.argmin(((c - e) ** 2 / e).sum(1)))


def keyed(g, kind, par):
    """Return (plaintext indices, key) for one key family on grid letters g."""
    n = len(g)
    if kind == 'vig':
        p = par
        key = [chi_shift(g[j::p]) for j in range(p)]
        return (g - np.array([key[i % p] for i in range(n)])) % 24, key
    a = par
    g2 = (g - a * np.arange(n)) % 24
    b = chi_shift(g2)
    return (g2 - b) % 24, [b]


def refine(g, kind, par, key):
    """Coordinate ascent of the key on the n-gram score."""
    n = len(g)
    def dec(key):
        if kind == 'vig':
            return (g - np.array([key[i % par] for i in range(n)])) % 24
        return (g - par * np.arange(n) - key[0]) % 24
    best = lmscore(dec(key)); improved = True
    while improved:
        improved = False
        for j in range(len(key)):
            for s in range(24):
                k2 = list(key); k2[j] = s
                sc = lmscore(dec(k2))
                if sc > best + 1e-9:
                    key, best, improved = k2, sc, True
    return best, dec(key), key


def search(ct, tag):
    o, c = ct // 3, ct % 3
    cand = []
    for rest in itertools.permutations(range(1, 8)):
        pi = np.array((0,) + rest)
        for arcrev in (0, 1):
            g = pi[o] * 3 + (2 - c if arcrev else c)
            for kind, pars in (('vig', range(1, 13)), ('dial', range(1, 24))):
                for par in pars:
                    x, key = keyed(g, kind, par)
                    cand.append((lmscore(x), tuple(pi), arcrev, kind, par, key))
    cand.sort(key=lambda r: -r[0])
    out = []
    for sc, pi, arcrev, kind, par, key in cand[:TOP]:
        g = np.array(pi)[o] * 3 + (2 - c if arcrev else c)
        s2, x, k2 = refine(g, kind, par, key)
        out.append((s2, pi, arcrev, kind, par, k2, ''.join(ROE[i] for i in x)))
    out.sort(key=lambda r: -r[0])
    print(f'{tag}: {len(cand)} readings; stage-1 best {cand[0][0]:.3f}; refined best {out[0][0]:.3f}', flush=True)
    for r in out[:3]:
        print(f'   {r[0]:.3f} {r[3]} {r[4]} key={"".join(ROE[k] for k in r[5])} pi={r[1]} arcrev={r[2]} {r[6]}', flush=True)
    return out[0]


ct = np.array([TOK.index(t) for t in open(os.path.join(HERE, 'ct.txt')).read().split()])
NN = int(sys.argv[1]) if len(sys.argv) > 1 else 4
NC = int(sys.argv[2]) if len(sys.argv) > 2 else 3
rng = random.Random(3)
if NC:
    corpus = lm.norm(open(os.path.join(HERE, '..', '..', 'lang', 'corpora', 'en-gutenberg.txt'),
                          encoding='utf-8').read()[:2_000_000], 'early', False)
for j in range(NC):                                    # English, random non-cyclic order, random key
    p0 = rng.randrange(len(corpus) - 200)
    pt = np.array([ROE.index(ch) for ch in corpus[p0:p0 + 200] if ch in ROE][:87])
    pi = [0] + rng.sample(range(1, 8), 7); arcrev = rng.random() < .5
    kind = rng.choice(('vig', 'dial'))
    if kind == 'vig':
        p = rng.randrange(3, 9); k = [rng.randrange(24) for _ in range(p)]
        g = (pt + np.array([k[i % p] for i in range(87)])) % 24; desc = f'vig p={p} key={"".join(ROE[x] for x in k)}'
    else:
        a, b = rng.randrange(1, 24), rng.randrange(24)
        g = (pt + a * np.arange(87) + b) % 24; desc = f'dial a={a} b={b}'
    inv = {v: i for i, v in enumerate(pi)}
    toks = np.array([inv[v // 3] * 3 + (2 - v % 3 if arcrev else v % 3) for v in g])
    r = search(toks, f'control{j} ({desc}, pi={tuple(pi)}, arcrev={int(arcrev)})')
    print(f'   truth: {"".join(ROE[i] for i in pt)}  acc={np.mean(np.array([ROE.index(ch) for ch in r[6]]) == pt):.2f}', flush=True)
search(ct, 'DORABELLA')
for j in range(NN):
    search(np.random.default_rng(j).permutation(ct), f'null{j}')
