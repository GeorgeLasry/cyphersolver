"""Set 469 (goal run loop 115): caged closers and doubled signs by seal size (length x site strata).
Writes results/predict_test469.md."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test430 import seals

CAGED = {'226', '232', '153', '236', '241'}


def main():
    rd = R.Round('Four-hundred-and-sixty-ninth registered predictions: goal loop 115, caged closers and doubled signs by size', 'predict_test469')
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
    o1, p1 = mh(lambda t: bool(CAGED & set(t)))
    rd.rec('CC1', 'large seals carry a caged closer more often (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = mh(lambda t: any(t[i] == t[i + 1] and t[i] not in R.NUMS for i in range(len(t) - 1)))
    rd.rec('CC2', 'large seals carry a doubled sign more often (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'CC1 %s, CC2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
