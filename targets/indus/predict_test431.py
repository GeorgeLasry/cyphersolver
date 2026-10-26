"""Set 431 (goal run loop 77): are the small-seal signs one formula? Writes results/predict_test431.md."""
import itertools
import random
from collections import Counter

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test388 import objects

SMALL = ('156', '400', '590')


def main():
    rnd = random.Random(431)
    rd = R.Round('Four-hundred-and-thirty-first registered predictions: goal loop 77, the small-seal formula', 'predict_test431')
    A, B, rowsA, recs, F = R.load_all()
    lines = sorted({tuple(ln) for r in F if recs.get(r['sealid']) and str(recs[r['sealid']][20]).startswith('SEAL:S') for ln in r['seq'] if ln})
    obs = sum(sum(1 for t in lines if a in t and b in t) for a, b in itertools.combinations(SMALL, 2))
    ge = 0
    for _ in range(1000):
        sh = []
        pool = [g for t in lines for g in t]
        rnd.shuffle(pool)
        k = 0
        for t in lines:
            sh.append(tuple(pool[k:k + len(t)]))
            k += len(t)
        ge += sum(sum(1 for t in sh if a in t and b in t) for a, b in itertools.combinations(SMALL, 2)) >= obs
    p = (ge + 1) / 1001
    rd.rec('SF1', '156, 400 and 590 share lines more than chance', '%d pair co-occurrences; sign-shuffled lines as many in %d of 1000, p = %.4f' % (obs, ge, p), p < 0.05)
    sq = objects('SEAL:S')
    cnt = Counter(t for s, t in sq)
    band = lambda t: min(max(len(t), 2), 7)
    tabs = []
    for b in sorted({band(t) for s, t in sq}):
        w = [cnt[t] > 1 for s, t in sq if band(t) == b and any(g in t for g in SMALL)]
        o = [cnt[t] > 1 for s, t in sq if band(t) == b and not any(g in t for g in SMALL)]
        tabs.append([[sum(w), len(w) - sum(w)], [sum(o), len(o) - sum(o)]])
    orr, p2 = mantel_haenszel(tabs)
    rd.rec('SF2', 'texts with a small-seal sign recur on other seals more often at equal length', 'odds ratio %.2f, p = %.4f' % (orr, p2), orr > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'SF1 %s, SF2 %s' % (p < 0.05, orr > 1 and p2 < 0.05), p < 0.05 or (orr > 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
