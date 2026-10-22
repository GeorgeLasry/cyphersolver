"""Homophonic anneal for the cipher runs of Baluze 156 f. 157r (f157r.txt).

Each run is scored inside its clear context (before + decrypt + after) with fr-1600-letters, letters only, order 5.
Two-digit signs (12, 36, 94) are treated as codes and break the run.

  python solve.py [restarts] [--fix sign=letter,...] [--lasry]
"""
import os, random, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from lang import lm

HERE = os.path.dirname(__file__)
CODES = {'12', '36', '94'}
M = lm.load('fr-1600-letters', order=5, spaces=False)
LET = 'abcdefghilmnopqrstuxyz'


def runs():
    out = []
    for line in open(os.path.join(HERE, 'f157r.txt'), encoding='utf8'):
        if line.startswith('#') or not line.strip():
            continue
        n, before, signs, after = line.rstrip('\n').split('\t')
        out.append((before, signs.split(), after if not after.startswith('(') else ''))
    return out


def decrypt(key, signs):
    return ''.join(key.get(s, '') if s not in CODES else '|' for s in signs)


def score(key, R):
    t = 0.0
    for before, signs, after in R:
        parts = decrypt(key, signs).split('|')
        for k, p in enumerate(parts):
            ctx_b = lm.norm(before, 'early', False)[-6:] if k == 0 else ''
            ctx_a = lm.norm(after, 'early', False)[:6] if k == len(parts) - 1 else ''
            s = ctx_b + p + ctx_a
            t += M.score(s) - (M.score(ctx_b) + M.score(ctx_a))
    return t


def anneal(R, fixed, iters=60000, T0=3.0):
    signs = sorted({s for _, ss, _ in R for s in ss if s not in CODES})
    free = [s for s in signs if s not in fixed]
    key = dict(fixed)
    for s in free:
        key[s] = random.choice(LET)
    cur = score(key, R)
    best, bk = cur, dict(key)
    for i in range(iters):
        T = T0 * (1 - i / iters) + 0.05
        s = random.choice(free)
        old = key[s]
        key[s] = random.choice(LET)
        new = score(key, R)
        if new > cur or random.random() < math.exp((new - cur) / T):
            cur = new
            if cur > best:
                best, bk = cur, dict(key)
        else:
            key[s] = old
    return best, bk


if __name__ == '__main__':
    R = runs()
    fixed = {}
    if '--fix' in sys.argv:
        for kv in sys.argv[sys.argv.index('--fix') + 1].split(','):
            a, b = kv.split('=')
            fixed[a] = b
    n = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8
    res = []
    for r in range(n):
        random.seed(r)
        b, k = anneal(R, fixed)
        res.append((b, k))
        print(f'restart {r}: {b:.1f}', flush=True)
    res.sort(key=lambda x: -x[0])
    for b, k in res[:3]:
        print(f'\n== {b:.1f}')
        print(' '.join(f'{s}={k[s]}' for s in sorted(k)))
        for before, signs, after in R:
            print(f'  {before[-25:]:>25} [{decrypt(k, signs)}] {after[:25]}')
