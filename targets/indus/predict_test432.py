"""Set 432 (goal run loop 78): do 156, 400, 590 fill one slot? Context similarity against frequency-matched random
signs. Writes results/predict_test432.md."""
import itertools
import math
import random
from collections import Counter, defaultdict

import rtools as R

SMALL = ('156', '400', '590')


def cos(a, b):
    num = sum(a[k] * b[k] for k in a)
    den = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return num / den if den else 0.0


def main():
    rnd = random.Random(432)
    rd = R.Round('Four-hundred-and-thirty-second registered predictions: goal loop 78, one slot for the small-seal signs?', 'predict_test432')
    A, B, rowsA, recs, F = R.load_all()
    lines = sorted({tuple(ln) for r in F if recs.get(r['sealid']) and str(recs[r['sealid']][20]).startswith('SEAL') for ln in r['seq'] if ln})
    prev, nxt = defaultdict(Counter), defaultdict(Counter)
    for t in lines:
        s = ('^',) + t + ('$',)
        for i in range(1, len(s) - 1):
            prev[s[i]][s[i - 1]] += 1
            nxt[s[i]][s[i + 1]] += 1
    cnt = Counter(g for t in lines for g in t)

    def test(ctx, key, title):
        obs = sum(cos(ctx[a], ctx[b]) for a, b in itertools.combinations(SMALL, 2)) / 3
        pools = {g: [h for h in cnt if 0.5 * cnt[g] <= cnt[h] <= 2 * cnt[g] and h not in SMALL] for g in SMALL}
        ge = 0
        for _ in range(1000):
            pick = {g: rnd.choice(pools[g]) for g in SMALL}
            ge += sum(cos(ctx[pick[a]], ctx[pick[b]]) for a, b in itertools.combinations(SMALL, 2)) / 3 >= obs
        p = (ge + 1) / 1001
        rd.rec(key, title, 'mean pairwise cosine %.3f, random signs as high in %d of 1000, p = %.4f' % (obs, ge, p), p < 0.05)
        return p < 0.05
    o1 = test(prev, 'SL1', 'they share preceding signs')
    o2 = test(nxt, 'SL2', 'they share following signs')
    rd.rec('P', 'progress rule: either holds', 'SL1 %s, SL2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
