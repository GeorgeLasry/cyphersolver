"""Set 484 (goal run loop 130): inside the formula: 706 against 705, and plain fish 220 against marked fish, by seal size.
Writes results/predict_test484.md."""
from statistics import median

import rtools as R
from predict_test430 import seals
from predict_test448 import FISH
from scipy.stats import mannwhitneyu


def formula(t):
    for i in range(1, len(t) - 1):
        if t[i] in ('705', '706') and t[i + 1] == '33':
            return t[i - 1], t[i]
    return None


def main():
    rd = R.Round('Four-hundred-and-eighty-fourth registered predictions: goal loop 130, inside the formula by seal size', 'predict_test484')
    rows = [(s, formula(t)) for s, t, x in seals(31) if formula(t)]
    a = [s for s, f in rows if f[1] == '706']
    c = [s for s, f in rows if f[1] == '705']
    p1 = mannwhitneyu(a, c, alternative='greater').pvalue if a and c else 1
    med = lambda x: sorted(x)[len(x) // 2] if x else 0
    rd.rec('IF1', 'formula seals with 706 are larger than formula seals with 705', 'median %.1f (n %d) against %.1f (n %d), p = %.4f' % (med(a), len(a), med(c), len(c), p1), p1 < 0.05)
    a2 = [s for s, f in rows if FISH(f[0]) and f[0] != '220']
    c2 = [s for s, f in rows if f[0] == '220']
    p2 = mannwhitneyu(a2, c2).pvalue if a2 and c2 else 1
    rd.rec('IF2', 'formula seals with a marked fish differ in size from those with plain 220 (two-sided)', 'median %.1f (n %d) against %.1f (n %d), p = %.4f' % (med(a2), len(a2), med(c2), len(c2), p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'IF1 %s, IF2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
