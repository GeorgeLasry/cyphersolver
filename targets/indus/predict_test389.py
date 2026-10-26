"""Set 389 (goal run loop 35): copies of a seal text and seal size; numerals and seal size. Writes results/predict_test389.md."""
import random
from collections import defaultdict
from statistics import median, pstdev

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test388 import objects


def main():
    rnd = random.Random(389)
    rd = R.Round('Three-hundred-and-eighty-ninth registered predictions: goal loop 35, copies and numerals by seal size', 'predict_test389')
    sq = objects('SEAL:S')
    by = defaultdict(list)
    for s, t in sq:
        if len(t) >= 2:
            by[t].append(s)
    groups = [v for v in by.values() if len(v) > 1]
    obs = sum(pstdev(v) for v in groups) / len(groups)
    sizes = [s for s, t in sq]
    ge = 0
    for _ in range(1000):
        sim = sum(pstdev(rnd.sample(sizes, len(v))) for v in groups) / len(groups)
        ge += sim <= obs
    p = (ge + 1) / 1001
    rd.rec('TT1', 'copies of one text are made at nearly one size', '%d texts on 2+ seals: mean spread %.2f; random seals as tight in %d of 1000, p = %.4f' % (len(groups), obs, ge, p), p < 0.05)
    cut = median(sizes)
    band = lambda t: min(max(len(t), 2), 7)
    num = lambda t: any(g in R.NUMS for g in t)
    tabs = []
    for b in sorted({band(t) for s, t in sq}):
        sm = [num(t) for s, t in sq if band(t) == b and s <= cut]
        lg = [num(t) for s, t in sq if band(t) == b and s > cut]
        tabs.append([[sum(sm), len(sm) - sum(sm)], [sum(lg), len(lg) - sum(lg)]])
    orr, p2 = mantel_haenszel(tabs)
    rd.rec('TT2', 'small square seals carry numerals more often at equal length', 'odds ratio small/large %.2f, p = %.4f' % (orr, p2), orr > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'TT1 %s, TT2 %s' % (p < 0.05, orr > 1 and p2 < 0.05), p < 0.05 or (orr > 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
