"""Set 450 (goal run loop 96): 740 90 and 740 400 by seal size (length x site strata). Writes results/predict_test450.md."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test430 import seals


def has(t, a, b):
    return any(t[i] == a and t[i + 1] == b for i in range(len(t) - 1))


def main():
    rd = R.Round('Four-hundred-and-fiftieth registered predictions: goal loop 96, 740 90 and 740 400 by seal size', 'predict_test450')
    sq = seals(31)
    cut = median(s for s, t, x in sq)
    band = lambda t: min(max(len(t), 2), 7)

    def mh(feat):
        tabs = []
        for k in sorted({(band(t), x) for s, t, x in sq}):
            lg = [feat(t) for s, t, x in sq if (band(t), x) == k and s > cut]
            sm = [feat(t) for s, t, x in sq if (band(t), x) == k and s <= cut]
            tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda t: has(t, '740', '90'))
    rd.rec('LM1', "large seals carry '740 90' more often", 'odds ratio large/small %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh(lambda t: has(t, '740', '400'))
    rd.rec('LM2', "small seals carry '740 400' more often", 'odds ratio large/small %.2f, p = %.4f' % (o2, p2), o2 < 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'LM1 %s, LM2 %s' % (o1 > 1 and p1 < 0.05, o2 < 1 and p2 < 0.05), (o1 > 1 and p1 < 0.05) or (o2 < 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
