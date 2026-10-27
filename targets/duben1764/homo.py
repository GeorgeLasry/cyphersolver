"""Ciphertext-only homophonic solver: each group stands for one letter.

Simulated annealing over the group -> letter map, scored with the shared lang/ model
fr-1750-nospace (order 5, a-z, no spaces). Several restarts; best key and text are printed.
Usage: python homo.py <cipher tx> [restarts] [steps] [--drop 7,8,...]
"""
import os, sys, math, random, json
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
from wem import load_cipher

M = lm.load('fr-1750-nospace', order=int(os.environ.get('ORDER', '5')))
K, A, LP = M.order, M.A, M.lp
ALPHA = M.meta.get('alpha') if isinstance(M.meta, dict) and M.meta.get('alpha') else 'abcdefghijklmnopqrstuvwxyz'
FREQ = np.array([8.1, .9, 3.3, 3.7, 17.0, 1.1, 1.0, .7, 7.5, .5, .1, 5.5, 3.0, 7.1, 5.3, 3.0, 1.4, 6.6, 7.9, 7.2, 6.3, 1.8, .1, .4, .3, .1])
FREQ = FREQ / FREQ.sum()
LAMBDA = float(os.environ.get('LAMBDA', '1.0'))


def windows_score(x, W):
    ctx = np.zeros(len(W), dtype=np.int64)
    for j in range(K):
        ctx = ctx * A + x[W + j]
    return LP[ctx].sum()


def solve(T, steps=200000, t0=float(os.environ.get("T0", "3.0")), t1=0.05, seed=0):
    rng = random.Random(seed)
    nsym = T.max() + 1
    N = len(T)
    pos = [np.nonzero(T == s)[0] for s in range(nsym)]
    wins = []
    for s in range(nsym):
        w = set()
        for p in pos[s]:
            for st in range(p - K + 1, p + 1):
                if 0 <= st <= N - K:
                    w.add(st)
        wins.append(np.array(sorted(w), dtype=np.int64))
    syms = [s for s in range(nsym) if len(pos[s])]
    key = np.array([np.random.default_rng(seed + s).choice(26, p=FREQ) for s in range(nsym)])
    x = key[T]
    cnt = np.bincount(x, minlength=26).astype(float)
    exp = FREQ * N
    def pen(c):
        if os.environ.get('PEN') == 'kl':
            o = c / N; m = o > 0
            return -LAMBDA * N * float((o[m] * np.log(o[m] / FREQ[m])).sum())
        return -LAMBDA * float(((c - exp) ** 2 / (exp + 1)).sum())
    cur = windows_score(x, np.arange(N - K + 1)) + pen(cnt)
    best, bkey = cur, key.copy()
    for step in range(steps):
        temp = t0 * (t1 / t0) ** (step / steps)
        s = rng.choice(syms)
        old = key[s]
        new = rng.randrange(26)
        if new == old:
            continue
        W = wins[s]
        before = windows_score(x, W)
        x[pos[s]] = new
        m = len(pos[s])
        c2 = cnt.copy(); c2[old] -= m; c2[new] += m
        d = windows_score(x, W) - before + pen(c2) - pen(cnt)
        if d >= 0 or rng.random() < math.exp(d / temp):
            key[s] = new; cur += d; cnt = c2
            if cur > best:
                best, bkey = cur, key.copy()
        else:
            x[pos[s]] = old
    return best / (N - K + 1), bkey


def run(groups, restarts=8, steps=200000):
    syms = sorted(set(groups))
    si = {g: k for k, g in enumerate(syms)}
    T = np.array([si[g] for g in groups])
    res = []
    for r in range(restarts):
        sc, key = solve(T, steps, seed=r * 101)
        txt = ''.join(ALPHA[k] for k in key[T])
        res.append((sc, txt, {syms[k]: ALPHA[key[k]] for k in range(len(syms))}))
        print(f'restart {r}: {sc:.3f} {txt[:90]}', flush=True)
    res.sort(key=lambda r: -r[0])
    return res


if __name__ == '__main__':
    args = sys.argv[1:]
    drop = set()
    if '--drop' in args:
        i = args.index('--drop'); drop = set(args[i + 1].split(',')); args = args[:i] + args[i + 2:]
    groups = [g for g in load_cipher(args[0]) if g not in drop]
    restarts = int(args[1]) if len(args) > 1 else 8
    steps = int(args[2]) if len(args) > 2 else 200000
    print('groups', len(groups), 'distinct', len(set(groups)))
    res = run(groups, restarts, steps)
    sc, txt, key = res[0]
    print('BEST', round(sc, 3)); print(txt)
    out = os.path.splitext(os.path.basename(args[0]))[0]
    json.dump({'score': float(sc), 'text': txt, 'key': key}, open(f'homo_{out}.json', 'w'), indent=0)
