"""Set 468 (goal run loop 114): numeral value and stroke series by seal size (length x site strata).
Writes results/predict_test468.md."""
from statistics import median

import numerals
import rtools as R
from predict_test379 import mantel_haenszel
from predict_test430 import seals


def main():
    rd = R.Round('Four-hundred-and-sixty-eighth registered predictions: goal loop 114, numbers and seal size', 'predict_test468')
    sq = [r for r in seals(31) if any(g in numerals.NUMS for g in r[1])]
    cut = median(s for s, t, x in seals(31))
    band = lambda t: min(max(len(t), 2), 7)

    def mh(feat):
        tabs = []
        for k in sorted({(band(t), x) for s, t, x in sq}):
            lg = [feat(t) for s, t, x in sq if (band(t), x) == k and s > cut]
            sm = [feat(t) for s, t, x in sq if (band(t), x) == k and s <= cut]
            tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda t: max(numerals.NUMS[g][0] for g in t if g in numerals.NUMS) >= 5)
    rd.rec('NV1', 'large seals carry numerals of 5 or more more often (seals with a numeral)', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh(lambda t: any(numerals.NUMS[g][1] == 'long' for g in t if g in numerals.NUMS))
    rd.rec('NV2', 'large seals use the long-stroke series more often (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'NV1 %s, NV2 %s' % (o1 > 1 and p1 < 0.05, p2 < 0.05), (o1 > 1 and p1 < 0.05) or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
