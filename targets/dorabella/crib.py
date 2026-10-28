"""Crib placement under strict simple substitution.

For each crib and each offset whose letter pattern is isomorphic to the ciphertext there
(same symbol <-> same letter), fix those letters and anneal the rest of the key on en-modern
order 4. The best per-crib score on Dorabella is compared with the best per-crib score on
shuffled Dorabella, which has the same number of chances to fit by accident.

python targets/dorabella/crib.py [nulls]
"""
import os, sys, random, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
CRIBS = ['dorabella', 'dora', 'penny', 'dorapenny', 'missdora', 'missp', 'wolverhampton', 'alice',
         'elgar', 'edward', 'edu', 'forli', 'malvern', 'thanks', 'thankyou', 'dearest', 'dear',
         'ladyalice', 'mrselgar', 'schuster', 'thevicarage', 'vicarage', 'thursday', 'friday', 'saturday',
         'sunday', 'monday', 'tuesday', 'wednesday', 'july', 'yours', 'yourssincerely', 'kind', 'remember',
         'gramophone', 'bicycle', 'cycle', 'music', 'caractacus', 'stephen', 'enigma', 'variation',
         'whatever', 'please', 'come', 'tomorrow', 'letter', 'hearts', 'love', 'kiss']
m = lm.load('en-modern', order=4, spaces=False)
A = m.A


def fits(ct, crib, p):
    s2l, l2s = {}, {}
    for t, ch in zip(ct[p:p + len(crib)], crib):
        if s2l.setdefault(t, ch) != ch or l2s.setdefault(ch, t) != t:
            return None
    return s2l


def anneal_fixed(ct, fixed, rng, restarts=4, iters=8000):
    syms = sorted(set(ct.tolist()))
    free = [s for s in syms if s not in fixed]
    used = {m.index[c] for c in fixed.values()}
    pool = [a for a in range(A) if a not in used]
    best = -1e18
    for r in range(restarts):
        key = np.zeros(max(syms) + 1, dtype=np.int64)
        for s, c in fixed.items():
            key[s] = m.index[c]
        assign = rng.sample(pool, len(free))
        for s, a in zip(free, assign):
            key[s] = a
        cur = m.score_idx(key[ct])
        for i in range(iters):
            T = 2.0 * (1 - i / iters) + 0.05
            k2 = key.copy()
            s = rng.choice(free)
            if rng.random() < 0.5:
                t = rng.choice(free)
                k2[s], k2[t] = k2[t], k2[s]
            else:
                inuse = set(k2[free].tolist()) | used
                k2[s] = rng.choice([a for a in range(A) if a not in inuse] or [k2[s]])
            sc = m.score_idx(k2[ct])
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
        if cur > best:
            best, bkey = cur, key.copy()
    return best / len(ct), ''.join(m.alpha[i] for i in bkey[ct])


def run(ct, tag, seed):
    rng = random.Random(seed)
    res = []
    for crib in CRIBS:
        hits = [(p, f) for p in range(len(ct) - len(crib) + 1) if (f := fits(ct, crib, p))]
        if len(crib) < 6:              # short cribs fit almost anywhere; sample a few placements
            hits = rng.sample(hits, min(6, len(hits)))
        for p, f in hits:
            sc, txt = anneal_fixed(ct, f, rng)
            res.append((sc, crib, p, txt))
    res.sort(reverse=True)
    print(f'{tag}: {len(res)} placements, best {res[0][0]:.3f}', flush=True)
    for r in res[:5]:
        print(f'   {r[0]:.3f} {r[1]}@{r[2]} {r[3]}', flush=True)
    return res[0][0]


syms = sorted(set(open(os.path.join(HERE, 'ct.txt')).read().split()))
ct = np.array([syms.index(t) for t in open(os.path.join(HERE, 'ct.txt')).read().split()])
run(ct, 'DORABELLA', 0)
for j in range(int(sys.argv[1]) if len(sys.argv) > 1 else 4):
    run(np.random.default_rng(j).permutation(ct), f'null{j}', 100 + j)
