"""One-to-one substitution anneal for the 1644 passage (letter 153), scored on lang pt-modern with spaces.

Each cipher letter gets a distinct plain letter (swap moves), simulated annealing, many restarts.
Usage: python solve153b.py [file] [restarts] [seed]
"""
import os, sys, random, math
sys.path.insert(0, os.path.dirname(__file__))
from solve153 import load, M

PLAIN = list('aeosrinmdtculpvgqfhbzjx')


def anneal(ct, syms, rnd, iters=30000, t0=6.0):
    perm = PLAIN[:]
    rnd.shuffle(perm)
    key = dict(zip(syms, perm))
    spare = perm[len(syms):]
    dec = lambda: ''.join(key.get(c, c) for c in ct)
    cur = M.score(dec())
    best = (cur, dict(key))
    for i in range(iters):
        t = t0 * (1 - i / iters) + 0.05
        a = rnd.choice(syms)
        if spare and rnd.random() < 0.3:
            j = rnd.randrange(len(spare))
            old = key[a]; key[a] = spare[j]; spare[j] = old
            new = M.score(dec())
            if new >= cur or rnd.random() < math.exp((new - cur) / t):
                cur = new
            else:
                spare[j] = key[a]; key[a] = old
        else:
            b = rnd.choice(syms)
            key[a], key[b] = key[b], key[a]
            new = M.score(dec())
            if new >= cur or rnd.random() < math.exp((new - cur) / t):
                cur = new
            else:
                key[a], key[b] = key[b], key[a]
        if cur > best[0]:
            best = (cur, dict(key))
    return best


if __name__ == '__main__':
    path = sys.argv[1]
    restarts = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    rnd = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    words = load(path)
    ct = ' '.join(words)
    syms = sorted(set(ct) - {' '})
    top = (-1e18, None)
    for r in range(restarts):
        sc, key = anneal(ct, syms, rnd)
        if sc > top[0]:
            top = (sc, key)
            print(r, round(sc, 1), ''.join(key.get(c, c) for c in ct), flush=True)
    print(sorted(top[1].items()))
