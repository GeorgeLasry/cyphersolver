"""Axis hypothesis: the meaningful sign is axis (orientation mod 4) x arcs = 12 values, and the direction
along the axis is not part of the letter (Dorabella has 27 opposite-orientation steps where shuffles give
12.6 and English under any layout at most ~25). Twelve signs for ~24 letters = a polyphonic cipher: each
sign stands for ~2 letters. The letter -> sign grouping is annealed; each grouping is scored by the best
(Viterbi) letter path under en-modern order 3 (no spaces, i/j u/v merged). Controls: English through a
random 12-sign grouping; nulls: shuffles of Dorabella.

python targets/dorabella/axis.py [restarts] [controls] [nulls] [--direction]
--direction: use the direction (orientation // 4) x arcs = 6 signs instead, as a check of the other half.
"""
import os, sys, random, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = [o + c for o in 'ABCDEFGH' for c in '123']
args = [a for a in sys.argv[1:] if not a.startswith('--')]
R = int(args[0]) if args else 6
NC = int(args[1]) if len(args) > 1 else 3
NN = int(args[2]) if len(args) > 2 else 3
m = lm.load('en-modern', order=3, spaces=False)
AL = 'abcdefghiklmnopqrstuwxyz'
LI = np.array([m.index[c] for c in AL])               # Roe letter -> model index
A = m.A
LP = m.lp.reshape(A, A, A)                            # log P(c | a, b)


def viterbi(seq, groups):
    """Best letter path given sign -> candidate letters; returns log-prob and path."""
    cands = [LI[groups[s]] for s in seq]
    # state: (previous letter, current letter); start with uniform over first two
    prev = {(a, b): 0.0 for a in cands[0] for b in cands[1]}
    for t in range(2, len(seq)):
        cur = {}
        for c in cands[t]:
            for (a, b), v in prev.items():
                s = v + LP[a, b, c]
                if s > cur.get((b, c), -1e18):
                    cur[(b, c)] = s
        prev = cur
    return max(prev.values())


def score(seq, assign, nsig):
    groups = [np.array([i for i in range(24) if assign[i] == s]) for s in range(nsig)]
    if any(len(groups[s]) == 0 for s in set(seq)):     # a sign in use with no letter
        return -1e18, groups
    return viterbi(seq, groups), groups


def decode(seq, groups):
    cands = [LI[groups[s]] for s in seq]
    prev = {(a, b): (0.0, [a, b]) for a in cands[0] for b in cands[1]}
    for t in range(2, len(seq)):
        cur = {}
        for c in cands[t]:
            for (a, b), (v, p) in prev.items():
                s = v + LP[a, b, c]
                if s > cur.get((b, c), (-1e18,))[0]:
                    cur[(b, c)] = (s, p + [c])
        prev = cur
    v, p = max(prev.values(), key=lambda x: x[0])
    return ''.join(m.alpha[i] for i in p)


def solve(seq, nsig, seed, iters=6000):
    rng = random.Random(seed)
    best = (-1e18, None)
    for r in range(R):
        assign = [i % nsig for i in range(24)]; rng.shuffle(assign)
        cur, _ = score(seq, assign, nsig)
        for i in range(iters):
            T = 2.0 * (1 - i / iters) + 0.05
            a2 = list(assign)
            if rng.random() < 0.5:
                x, y = rng.sample(range(24), 2); a2[x], a2[y] = a2[y], a2[x]
            else:
                a2[rng.randrange(24)] = rng.randrange(nsig)
            sc, _ = score(seq, a2, nsig)
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                assign, cur = a2, sc
        if cur > best[0]:
            best = (cur, list(assign))
    _, groups = score(seq, best[1], nsig)
    return best[0] / len(seq), decode(seq, groups), best[1]


direction = '--direction' in sys.argv
toks = [TOK.index(t) for t in open(os.path.join(HERE, 'ct.txt')).read().split()]
sig = (lambda t: (t // 3 // 4) * 3 + t % 3) if direction else (lambda t: (t // 3 % 4) * 3 + t % 3)
NS = 6 if direction else 12
seq = [sig(t) for t in toks]
n = len(seq)
print(f'{"direction" if direction else "axis"} x arcs = {NS} signs; Dorabella uses {len(set(seq))}', flush=True)
sc, txt, _ = solve(seq, NS, 0)
print(f'DORABELLA {sc:.3f} {txt}', flush=True)
rng = random.Random(9)
corpus = lm.norm(corpora.text(['en-gutenberg'])[:2_000_000], 'early', False)
for j in range(NC):
    p = rng.randrange(len(corpus) - 200)
    pt = [AL.index(ch) for ch in corpus[p:p + 200] if ch in AL][:n]
    grp = [i % NS for i in range(24)]; rng.shuffle(grp)
    s2, t2, _ = solve([grp[v] for v in pt], NS, 10 + j)
    truth = ''.join(AL[v] for v in pt)
    print(f'  control {s2:.3f} acc={np.mean([a == b for a, b in zip(t2, truth)]):.2f} {t2}', flush=True)
for j in range(NN):
    sh = list(np.random.default_rng(j).permutation(seq))
    s3, t3, _ = solve(sh, NS, 100 + j)
    print(f'  null {s3:.3f} {t3}', flush=True)
