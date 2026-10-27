"""Seeded one-to-one anneal for letter 153: fixed seeds from short words (p=e, E=m, v=u, n=a)."""
import sys, random, math
sys.path.insert(0, '.')
from solve153 import load, M
PLAIN = list('aeosrinmdtculpvgqfhbzjx')
def run(fixed, restarts=10, iters=25000, seed=1):
    rnd = random.Random(seed)
    ct = ' '.join(load('l153_cipher.txt'))
    syms = sorted(set(ct) - {' '} - set(fixed))
    free = [p for p in PLAIN if p not in fixed.values()]
    top = (-1e18, None)
    for r in range(restarts):
        perm = free[:]; rnd.shuffle(perm)
        key = dict(zip(syms, perm)); spare = perm[len(syms):]; key.update(fixed)
        dec = lambda: ''.join(key.get(c, c) for c in ct)
        cur = M.score(dec()); best = (cur, dict(key))
        for i in range(iters):
            t = 5.0 * (1 - i / iters) + 0.05
            a = rnd.choice(syms)
            if spare and rnd.random() < 0.3:
                j = rnd.randrange(len(spare)); old = key[a]; key[a] = spare[j]; spare[j] = old
                new = M.score(dec())
                if new >= cur or rnd.random() < math.exp((new - cur) / t): cur = new
                else: spare[j] = key[a]; key[a] = old
            else:
                b = rnd.choice(syms); key[a], key[b] = key[b], key[a]
                new = M.score(dec())
                if new >= cur or rnd.random() < math.exp((new - cur) / t): cur = new
                else: key[a], key[b] = key[b], key[a]
            if cur > best[0]: best = (cur, dict(key))
        if best[0] > top[0]:
            top = best; print(r, round(best[0], 1), ''.join(best[1].get(c, c) for c in ct), flush=True)
    return top
if __name__ == '__main__':
    fixed = dict(x.split('=') for x in sys.argv[1].split(',')) if len(sys.argv) > 1 else {}
    print(sorted(run(fixed, int(sys.argv[2]) if len(sys.argv) > 2 else 8)[1].items()))
