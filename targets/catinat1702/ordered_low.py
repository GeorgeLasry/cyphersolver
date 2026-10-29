"""Test of the 'ordered low numbers' hypothesis (Tomokiyo 2016): numbers 1-99 are single letters assigned
in alphabetical blocks (as in his Item 4, the 1690/1693 code).  Anneal the 25 block boundaries to maximise a
French letter-bigram score over the runs of consecutive low numbers, and compare with
  (a) the same search on the numbers after a random relabelling (null),
  (b) a control: French text enciphered by an ordered block scheme, cut into runs of the same lengths.
"""
import os, sys, json, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import numpy as np
from lang import lm

LOW = 99
m2 = lm.load('fr-grand-siecle', order=2, spaces=False)
m1 = lm.load('fr-grand-siecle', order=1, spaces=False)
A = m2.A
BG = m2.lp.reshape(A, A)            # log P(next | prev)
UG = m1.lp.ravel()                  # log P(c)
ALPHA = m2.alpha

toks = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tokens.json')))

def runs_of(seq, hi=LOW):
    out, cur = [], []
    for t in seq:
        if t <= hi:
            cur.append(t)
        else:
            if cur: out.append(cur); cur = []
    if cur: out.append(cur)
    return out

def score(runs, letter_of):
    s = 0.0
    for r in runs:
        prev = None
        for v in r:
            c = letter_of[v]
            s += UG[c] if prev is None else BG[prev, c]
            prev = c
    return s

def mapping(bounds):
    """bounds: sorted list of 25 cut points in 1..LOW+1; letter i covers [bounds[i-1], bounds[i])"""
    letter_of = np.zeros(LOW + 2, dtype=np.int64)
    edges = [1] + list(bounds) + [LOW + 1]
    for i in range(A):
        letter_of[edges[i]:edges[i + 1]] = i
    return letter_of

def anneal(runs, iters=40000, seed=0, relabel=None):
    rnd = random.Random(seed)
    if relabel is not None:
        runs = [[relabel[v] for v in r] for r in runs]
    cuts = sorted(rnd.sample(range(2, LOW + 1), A - 1))
    cur = score(runs, mapping(cuts)); best = (cur, list(cuts))
    T0 = 6.0
    for it in range(iters):
        T = T0 * (1 - it / iters) + 0.05
        k = rnd.randrange(A - 1)
        new = list(cuts)
        new[k] = min(LOW + 1, max(1, new[k] + rnd.choice((-3, -2, -1, 1, 2, 3))))
        new.sort()
        sc = score(runs, mapping(new))
        if sc >= cur or rnd.random() < math.exp((sc - cur) / T):
            cuts, cur = new, sc
            if cur > best[0]: best = (cur, list(cuts))
    return best

def run(runs, restarts=6, relabel=None):
    return max((anneal(runs, seed=s, relabel=relabel) for s in range(restarts)), key=lambda b: b[0])

def per_tok(runs, sc):
    n = sum(len(r) for r in runs)
    return sc / n

def decode(runs, cuts):
    lo = mapping(cuts)
    return [''.join(ALPHA[lo[v]] for v in r) for r in runs]

if __name__ == '__main__':
    runs = runs_of(toks)
    n = sum(len(r) for r in runs)
    print('low tokens', n, 'runs', len(runs), 'run lengths', sorted({len(r) for r in runs}))
    real = run(runs)
    print('REAL  per-token %.3f' % per_tok(runs, real[0]))
    print(decode(runs, real[1])[:30])
    nulls = []
    for k in range(6):
        perm = list(range(1, LOW + 1)); random.Random(100 + k).shuffle(perm)
        rl = {v: perm[v - 1] for v in range(1, LOW + 1)}
        b = run(runs, restarts=3, relabel=rl)
        nulls.append(per_tok(runs, b[0]))
    print('NULL  per-token', ['%.3f' % x for x in nulls])
    # control: French text, ordered block scheme (block size ~ letter frequency), runs of the real lengths
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'lang', 'corpora', 'fr-gutenberg.txt')
    raw = open(root, encoding='utf8', errors='ignore').read()[3000000:3400000]
    txt = ''.join(c for c in lm.norm(raw, 'modern', spaces=False))
    cnt = np.bincount(m2.encode(txt), minlength=A).astype(float); fr = cnt / cnt.sum()
    sizes = np.maximum(1, np.round(fr * LOW)).astype(int)
    while sizes.sum() > LOW: sizes[sizes.argmax()] -= 1
    while sizes.sum() < LOW: sizes[sizes.argmax()] += 1
    cuts_true = list(np.cumsum(sizes)[:-1] + 1)
    rnd = random.Random(7); L = [len(r) for r in runs]
    for trial in range(3):
        pos = rnd.randrange(0, len(txt) - 2000); sim = []
        for l in L:
            seg = m2.encode(txt[pos:pos + l]); pos += l + rnd.randrange(1, 4)
            lo_true = mapping(cuts_true)
            sim.append([int(rnd.choice([v for v in range(1, LOW + 1) if lo_true[v] == c])) for c in seg])
        got = run(sim)
        plain = [''.join(ALPHA[mapping(cuts_true)[v]] for v in r) for r in sim]
        dec = decode(sim, got[1])
        acc = np.mean([a == b for p, d in zip(plain, dec) for a, b in zip(p, d)])
        perm = list(range(1, LOW + 1)); random.Random(200 + trial).shuffle(perm)
        nb = run(sim, restarts=3, relabel={v: perm[v - 1] for v in range(1, LOW + 1)})
        print('CONTROL %d: per-token %.3f, null %.3f, letter accuracy %.2f' % (trial, per_tok(sim, got[0]), per_tok(sim, nb[0]), acc))
