"""Second-layer systems from the 1896 Pall Mall "Secrets in Cipher" series (research_pallmall/systems.md).

A. Roe-shaped grid + additive key. The sign is a fixed grid position: orientation = Roe group
   (abc def ghi klm nop qrs tuw xyz; no j, v), arc count = place in the group. Group order round the
   dial: 8 starts x 2 directions; arc order 1-2-3 or 3-2-1. On top, a periodic additive key over the
   24-letter alphabet (Vigenère / the series' "pass-word" shift, periods 1-12; shifts per column chosen by
   chi-square against English letter frequencies) or a running "dial" shift k_i = a*i + b.
B. Nihilist-style key on both coordinates, unknown grid: token (o, c) -> (o - ko_i mod 8, c - kc_i mod 3),
   periodic, p = 1-8; shifts chosen to maximise IoC, then strict simple substitution, against shuffles.

python targets/dorabella/pallmall.py [A|B] [nulls]
"""
import os, sys, random, itertools
from collections import Counter
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = [o + c for o in 'ABCDEFGH' for c in '123']
ROE = 'abcdefghiklmnopqrstuwxyz'
# English letter frequencies on the Roe alphabet (j folded into i, v into u)
EN = dict(zip('abcdefghijklmnopqrstuvwxyz', [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, .15, .77, 4.0, 2.4,
                                             6.7, 7.5, 1.9, .1, 6.0, 6.3, 9.1, 2.8, .98, 2.4, .15, 2.0, .07]))
F = np.array([EN[c] + (EN['j'] if c == 'i' else 0) + (EN['v'] if c == 'u' else 0) for c in ROE])
F = F / F.sum()
m = lm.load('en-modern', order=4, spaces=False)
ct_all = [TOK.index(t) for t in open(os.path.join(HERE, 'ct.txt')).read().split()]


def grid_letters(ct, start, step, arcrev):
    """Grid position (0..23 in ROE order) of every token under one group order."""
    out = []
    for t in ct:
        o, c = t // 3, t % 3
        g = ((o - start) * step) % 8
        out.append(g * 3 + (2 - c if arcrev else c))
    return np.array(out)


def best_shift(col):
    best = None
    for s in range(24):
        obs = np.bincount((col - s) % 24, minlength=24)
        chi = ((obs - F * len(col)) ** 2 / (F * len(col))).sum()
        if best is None or chi < best[0]:
            best = (chi, s)
    return best[1]


def score(x):
    s = ''.join(ROE[i] for i in x)
    return m.per_char(s), s


def run_A(ct, tag):
    res = []
    for start, step, arcrev in itertools.product(range(8), (1, -1), (False, True)):
        g = grid_letters(ct, start, step, arcrev)
        for p in range(1, 13):
            key = [best_shift(g[j::p]) for j in range(p)]
            x = np.array([(v - key[i % p]) % 24 for i, v in enumerate(g)])
            sc, s = score(x)
            res.append((sc, f'vig p={p} key={"".join(ROE[k] for k in key)} grid=({start},{step},{int(arcrev)})', s))
        for a in range(1, 24):                     # running dial: k_i = a*i + b, b by chi-square
            g2 = np.array([(v - a * i) % 24 for i, v in enumerate(g)])
            b = best_shift(g2)
            x = (g2 - b) % 24
            sc, s = score(x)
            res.append((sc, f'dial a={a} b={b} grid=({start},{step},{int(arcrev)})', s))
    res.sort(reverse=True)
    print(f'{tag}: {len(res)} keyed readings; best {res[0][0]:.3f}', flush=True)
    for r in res[:4]:
        print(f'   {r[0]:.3f} {r[1]:40s} {r[2]}', flush=True)
    return res[0][0]


def ioc(x):
    c = Counter(x); n = len(x)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def run_B(ct, tag, rng):
    from solve import anneal, text_of
    ct = np.array(ct)
    out = []
    for p in range(1, 9):
        def apply(keys):
            return [((t // 3 - keys[i % p][0]) % 8) * 3 + (t % 3 - keys[i % p][1]) % 3 for i, t in enumerate(ct)]
        best = None
        for r in range(15):                        # coordinate ascent over (ko, kc) per column; column 0 fixed
            keys = [(0, 0)] + [(rng.randrange(8), rng.randrange(3)) for _ in range(p - 1)]
            cur = ioc(apply(keys)); improved = True
            while improved:
                improved = False
                for j in range(1, p):
                    for ko in range(8):
                        for kc in range(3):
                            k2 = keys.copy(); k2[j] = (ko, kc)
                            s = ioc(apply(k2))
                            if s > cur + 1e-12:
                                keys, cur, improved = k2, s, True
            if best is None or cur > best[0]:
                best = (cur, keys)
        x = apply(best[1])
        syms = sorted(set(x)); y = np.array([syms.index(t) for t in x])
        sc, key = anneal(y, len(syms), m, restarts=10, injective=True)
        out.append((sc / len(y), p, best[0], text_of(m, key, y)))
    out.sort(reverse=True)
    print(f'{tag}: best {out[0][0]:.3f} p={out[0][1]} ioc={out[0][2]:.4f} {out[0][3]}', flush=True)
    return out[0][0]


mode = sys.argv[1] if len(sys.argv) > 1 else 'A'
N = int(sys.argv[2]) if len(sys.argv) > 2 else 6
rng = random.Random(0)
if mode == 'A':
    run_A(ct_all, 'DORABELLA')
    # control: English through a Roe grid and a random 5-letter Vigenère key, same length
    corpus = lm.norm(open(os.path.join(HERE, '..', '..', 'lang', 'corpora', 'en-gutenberg.txt'), encoding='utf-8').read()[:2_000_000], 'early', False)
    for j in range(3):
        p0 = rng.randrange(len(corpus) - 200)
        pt = [ROE.index(c) for c in corpus[p0:p0 + 200] if c in ROE][:87]
        k = [rng.randrange(24) for _ in range(5)]
        g = [(v + k[i % 5]) % 24 for i, v in enumerate(pt)]
        start, step, arcrev = rng.randrange(8), rng.choice((1, -1)), rng.random() < .5
        toks = []
        for v in g:                                # invert grid_letters for this group order
            gg, c = divmod(v, 3)
            o = (gg * step + start) % 8
            toks.append(o * 3 + (2 - c if arcrev else c))
        run_A(toks, f'control{j} (key {"".join(ROE[x] for x in k)}, grid ({start},{step},{int(arcrev)}))')
    for j in range(N):
        run_A(list(np.random.default_rng(j).permutation(ct_all)), f'null{j}')
else:
    run_B(ct_all, 'DORABELLA', rng)
    for j in range(N):
        run_B(list(np.random.default_rng(j).permutation(ct_all)), f'null{j}', rng)
