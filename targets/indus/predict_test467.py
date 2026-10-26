"""Set 467 (goal run loop 113): star-type names (numeral + fish) and seal size. Writes results/predict_test467.md."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test430 import seals
from predict_test448 import FISH
from scipy.stats import mannwhitneyu


def star(t):
    return any(t[i] in R.NUMS and FISH(t[i + 1]) for i in range(len(t) - 1))


def fishname(t):
    return any(FISH(g) for g in t)


def main():
    rd = R.Round('Four-hundred-and-sixty-seventh registered predictions: goal loop 113, star names and seal size', 'predict_test467')
    sq = seals(31)
    a = [s for s, t, x in sq if star(t)]
    c = [s for s, t, x in sq if fishname(t) and not star(t)]
    p1 = mannwhitneyu(a, c, alternative='greater').pvalue if a and c else 1
    med = lambda x: sorted(x)[len(x) // 2] if x else 0
    rd.rec('SS1', 'seals with a numeral + fish are larger than seals with other fish signs', 'median %.1f (n %d) against %.1f (n %d), p = %.4f' % (med(a), len(a), med(c), len(c), p1), p1 < 0.05)
    cut = median(s for s, t, x in sq)
    band = lambda t: min(max(len(t), 2), 7)
    tabs = []
    for k in sorted({(band(t), x) for s, t, x in sq}):
        lg = [star(t) for s, t, x in sq if (band(t), x) == k and s > cut]
        sm = [star(t) for s, t, x in sq if (band(t), x) == k and s <= cut]
        tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
    o2, p2 = mantel_haenszel(tabs)
    rd.rec('SS2', 'large seals carry numeral + fish more often (length x site strata)', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: SS2 (stratified)', 'SS1 %s, SS2 %s' % (p1 < 0.05, o2 > 1 and p2 < 0.05), o2 > 1 and p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
