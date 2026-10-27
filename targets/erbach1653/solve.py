"""Homophonic attack on the Erbach number-pair cipher (ct_004.txt).

Each pair a,b is taken as one cipher symbol (a cell of the key: line a, letter b of a short key text).
Simulated annealing assigns a plaintext letter to every cell and scores the cipher runs with a Latin
character model from lang/ (no spaces). Runs separated by clear text are scored as separate segments.

usage: python solve.py [ct file] [--restarts N] [--iters N] [--model la] [--fix cell=letter ...]
"""
import argparse, math, random, re, sys, os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm

def parse(path):
    segs = []
    for line in open(path, encoding='utf8'):
        if line.startswith('#'):
            continue
        line = re.sub(r'^p\d\.\S+', '', line)
        for part in re.split(r'\{[^}]*\}|\[X\]', line):
            toks = [(int(a), int(b)) for a, b in re.findall(r'(\d+),(\d+)', part)]
            if toks:
                segs.append(toks)
    # glue a segment that continues on the next manuscript line (no clear text between)
    return segs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ct', nargs='?', default=os.path.join(os.path.dirname(__file__), 'ct_004.txt'))
    ap.add_argument('--restarts', type=int, default=8)
    ap.add_argument('--iters', type=int, default=60000)
    ap.add_argument('--model', default='la')
    ap.add_argument('--fix', nargs='*', default=[])
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--keymodel', default=None, help='model for the key text rows (e.g. la, de-1640s)')
    ap.add_argument('--kw', type=float, default=1.0, help='weight of the key-text score')
    ap.add_argument('--lam', type=float, default=1.0, help='weight of the letter-frequency penalty')
    a = ap.parse_args()
    random.seed(a.seed)
    M = lm.load(a.model, spaces=False)
    A = M.A
    segs = parse(a.ct)
    cells = sorted({c for s in segs for c in s})
    ci = {c: i for i, c in enumerate(cells)}
    S = [np.array([ci[c] for c in s]) for s in segs]
    where = [[] for _ in cells]
    for k, s in enumerate(S):
        for c in set(s.tolist()):
            where[c].append(k)
    fixed = {}
    for f in a.fix:
        c, l = f.split('=')
        x, y = map(int, c.split(','))
        fixed[ci[(x, y)]] = M.index[l]
    # expected letter frequencies from the model's corpus text (order-1 marginal)
    # standard Latin letter frequencies (per cent; i/j and u/v merged)
    LAT = dict(a=8.9, b=1.6, c=3.7, d=2.7, e=11.4, f=0.9, g=1.2, h=0.7, i=11.4, l=3.2, m=5.4, n=6.3,
               o=5.4, p=3.0, q=1.5, r=6.7, s=7.6, t=8.0, u=8.5, x=0.6, z=0.05)
    pf = np.array([LAT.get(c, 0.05) for c in M.alpha]); pf = pf / pf.sum()
    ntok = sum(len(s) for s in S)
    E = pf * ntok
    weight = np.array([len(s) for s in segs])
    cnt_tok = np.zeros(len(cells), int)
    for s in S:
        for i in s:
            cnt_tok[i] += 1

    def penalty(key):
        n = np.bincount(key, weights=cnt_tok, minlength=A)
        return -a.lam * float(((n - E) ** 2 / E).sum())

    def segscore(key, k):
        return M.score_idx(key[S[k]])

    # key-text rows: contiguous runs of observed positions, scored as text by a second model
    KM = lm.load(a.keymodel, spaces=False) if a.keymodel else None
    runs = []
    if KM is not None:
        tr = np.array([KM.index[c] if c in KM.index else 0 for c in M.alpha])
        rows = {}
        for (x, y), i in ci.items():
            rows.setdefault(x, {})[y] = i
        for x, d in rows.items():
            cur = []
            for y in range(1, 26):
                if y in d:
                    cur.append(d[y])
                elif cur:
                    runs.append(np.array(cur)); cur = []
            if cur:
                runs.append(np.array(cur))
        runs = [r for r in runs if len(r) >= KM.order]

    def keyscore(key):
        if KM is None:
            return 0.0
        return a.kw * sum(KM.score_idx(tr[key[r]]) for r in runs)

    best_all = None
    for r in range(a.restarts):
        key = np.array([random.randrange(A) for _ in cells])
        for c, l in fixed.items():
            key[c] = l
        sc = np.array([segscore(key, k) for k in range(len(S))])
        pen = penalty(key) + keyscore(key)
        tot = sc.sum() + pen
        T0, T1 = 20.0, 0.5
        best, bkey = tot, key.copy()
        free = [c for c in range(len(cells)) if c not in fixed]
        for it in range(a.iters):
            T = T0 * (T1 / T0) ** (it / a.iters)
            c = random.choice(free)
            old = key[c]
            new = random.randrange(A)
            if new == old:
                continue
            key[c] = new
            ks = where[c]
            ns = np.array([segscore(key, k) for k in ks])
            npen = penalty(key) + keyscore(key)
            d = ns.sum() - sc[ks].sum() + npen - pen
            if d >= 0 or random.random() < math.exp(d / T):
                sc[ks] = ns
                pen = npen
                tot += d
                if tot > best:
                    best, bkey = tot, key.copy()
            else:
                key[c] = old
        print(f'restart {r}: {best:.1f}  ({best/ntok:.3f}/char)', flush=True)
        if best_all is None or best > best_all[0]:
            best_all = (best, bkey)
    best, key = best_all
    al = M.alpha
    print('\nbest', round(best, 1))
    for s in S:
        print(''.join(al[key[i]] for i in s))
    print()
    rows = {}
    for (x, y), i in ci.items():
        rows.setdefault(x, {})[y] = al[key[i]]
    for x in sorted(rows):
        print(x, ''.join(rows[x].get(y, '.') for y in range(1, 25)))

if __name__ == '__main__':
    main()
