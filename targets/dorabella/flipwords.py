"""Flips as word breaks: split Dorabella at every 180-degree orientation step (and at line ends),
insert spaces, and solve as a strict substitution against en-modern order 4 with spaces. Nulls: the
same word-break pattern over shuffled signs. Controls: English with its own spaces, same length.

python targets/dorabella/flipwords.py
"""
import os, sys, random, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = [o + c for o in 'ABCDEFGH' for c in '123']
lines = [l.split() for l in open(os.path.join(HERE, 'ct.txt')).read().strip().splitlines()]
m = lm.load('en-modern', order=4, spaces=True)
SP = m.index[' ']
LET = [i for i in range(m.A) if i != SP]


def breaks(lines):
    seq, br = [], []
    for l in lines:
        o = [TOK.index(t) // 3 for t in l]
        for i, t in enumerate(l):
            if i and (o[i] - o[i - 1]) % 8 == 4:
                br.append(len(seq))
            seq.append(t)
        br.append(len(seq))
    return seq, sorted(set(br) - {len(seq)})


def solve(seq, br, seed, R=20, iters=20000):
    syms = sorted(set(seq)); ct = np.array([syms.index(t) for t in seq])
    rng = random.Random(seed); best = (-1e18, None)
    def text(key):
        out = []
        for i, c in enumerate(ct):
            if i in brs:
                out.append(SP)
            out.append(key[c])
        return np.array(out)
    brs = set(br)
    for r in range(R):
        key = np.array(rng.sample(LET, len(syms))); cur = m.score_idx(text(key))
        for i in range(iters):
            T = 3.0 * (1 - i / iters) + 0.05
            k2 = key.copy(); s = rng.randrange(len(syms))
            if rng.random() < 0.3:
                free = [a for a in LET if a not in set(k2.tolist())]; k2[s] = rng.choice(free)
            else:
                t = rng.randrange(len(syms)); k2[s], k2[t] = k2[t], k2[s]
            sc = m.score_idx(text(k2))
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
        if cur > best[0]:
            best = (cur, key)
    x = text(best[1])
    return best[0] / len(x), ''.join(m.alpha[i] for i in x)


seq, br = breaks(lines)
sc, txt = solve(seq, br, 0)
print(f'DORABELLA {sc:.3f} {txt}', flush=True)
for j in range(5):
    sh = list(np.random.default_rng(j).permutation(seq))
    print(f'  null {solve(sh, br, 100 + j)[0]:.3f}', flush=True)
corpus = lm.norm(corpora.text(['en-gutenberg'])[:2_000_000], 'modern', True)
rng = random.Random(3)
for j in range(4):
    p = rng.randrange(len(corpus) - 200); w = corpus[p:p + 200].split()[1:]
    s, b = [], []
    for word in w:
        if len(s) + len(word) > 87:
            break
        if s:
            b.append(len(s))
        s += list(word)
    sc2, t2 = solve(s, b, 10 + j)
    print(f'  control {sc2:.3f} {t2[:60]} | truth {" ".join(w)[:60]}', flush=True)
