"""Set 441 (goal run loop 87): the closing formula 705/706 33 and seal size. Writes results/predict_test441.md."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test430 import seals


def has_formula(t):
    return any(t[i] in ('705', '706') and t[i + 1] == '33' for i in range(len(t) - 1))


def main():
    rd = R.Round('Four-hundred-and-forty-first registered predictions: goal loop 87, the closing formula and seal size', 'predict_test441')
    sq = seals(31)
    cut = median(s for s, t, x in sq)
    band = lambda t: min(max(len(t), 2), 7)

    def mh(rows, feat):
        tabs = []
        for k in sorted({(band(t), x) for s, t, x in rows}):
            lg = [feat(t) for s, t, x in rows if (band(t), x) == k and s > cut]
            sm = [feat(t) for s, t, x in rows if (band(t), x) == k and s <= cut]
            tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(sq, has_formula)
    rd.rec('CF1', 'large seals carry the closing formula more often (length x site strata)', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh([r for r in sq if not has_formula(r[1])], lambda t: '706' in t or '705' in t)
    rd.rec('CF2', 'outside the formula, the stroked U still goes with large seals', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'CF1 %s, CF2 %s' % (o1 > 1 and p1 < 0.05, o2 > 1 and p2 < 0.05), (o1 > 1 and p1 < 0.05) or (o2 > 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
