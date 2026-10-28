"""Round 32: a large, parallel simple-substitution search on Dorabella (search-failure check).

Each worker runs independent annealing restarts (strict one-to-one key, longer schedule) and returns its best
key and score; the overall best and the spread of the top solutions are reported. Compare the best score with
real Elgar text under the same model (round 31) to see whether any reading could be hiding.

python targets/dorabella/bigsearch.py <model> <ct file> <restarts> [iters]
"""
import os, sys, random, math
import numpy as np
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL, CTF = sys.argv[1], sys.argv[2]
RESTARTS = int(sys.argv[3]); ITERS = int(sys.argv[4]) if len(sys.argv) > 4 else 60000


def work(seed):
    from lang import lm
    m = lm.load(MODEL, order=4, spaces=False)
    toks = open(os.path.join(HERE, CTF)).read().split()
    syms = sorted(set(toks)); ct = np.array([syms.index(t) for t in toks])
    rng = random.Random(seed)
    key = np.array(rng.sample(range(m.A), len(syms))); cur = m.score_idx(key[ct]); best = (cur, key.copy())
    for i in range(ITERS):
        T = 4.0 * (1 - i / ITERS) ** 2 + 0.03
        k2 = key.copy(); s = rng.randrange(len(syms))
        if rng.random() < 0.3:
            free = [a for a in range(m.A) if a not in set(k2.tolist())]; k2[s] = rng.choice(free)
        else:
            t = rng.randrange(len(syms)); k2[s], k2[t] = k2[t], k2[s]
        sc = m.score_idx(k2[ct])
        if sc >= cur or rng.random() < math.exp((sc - cur) / T):
            key, cur = k2, sc
            if cur > best[0]:
                best = (cur, key.copy())
    return best[0] / len(ct), ''.join(m.alpha[i] for i in best[1][ct])


if __name__ == '__main__':
    with Pool(max(1, (os.cpu_count() or 2) - 1)) as pool:
        res = pool.map(work, range(RESTARTS))
    res.sort(reverse=True)
    sc = np.array([r[0] for r in res])
    print(f'{MODEL} {CTF}: {RESTARTS} restarts x {ITERS} iterations')
    print(f'  best {sc[0]:.3f}; 10th {sc[min(9, len(sc) - 1)]:.3f}; median {np.median(sc):.3f}')
    distinct = []
    for s, t in res:
        if all(sum(a != b for a, b in zip(t, d)) > 20 for _, d in distinct):
            distinct.append((s, t))
        if len(distinct) == 5:
            break
    for s, t in distinct:
        print(f'  {s:.3f} {t}')
    print(f'  times the best text was found: {sum(1 for s, t in res if t == res[0][1])} of {RESTARTS}')
