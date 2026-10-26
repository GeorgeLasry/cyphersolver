"""Set 440 (goal run loop 86): the U-family size step: 705 against 700 on square seals; stroked U against 700 on
rectangular seals. Writes results/predict_test440.md."""
import rtools as R
from predict_test388 import objects
from scipy.stats import mannwhitneyu


def main():
    rd = R.Round('Four-hundred-and-fortieth registered predictions: goal loop 86, the U-family size step', 'predict_test440')
    med = lambda x: sorted(x)[len(x) // 2] if x else 0
    sq = objects('SEAL:S')
    a = [s for s, t in sq if '705' in t and '706' not in t]
    c = [s for s, t in sq if '700' in t and '705' not in t and '706' not in t]
    p1 = mannwhitneyu(a, c, alternative='greater').pvalue if a and c else 1
    rd.rec('UR1', '705 square seals are larger than plain-700 square seals', 'median %.1f (n %d) against %.1f (n %d), p = %.4f' % (med(a), len(a), med(c), len(c), p1), p1 < 0.05)
    rc = objects('SEAL:R')
    a2 = [s for s, t in rc if '705' in t or '706' in t]
    c2 = [s for s, t in rc if '700' in t and '705' not in t and '706' not in t]
    p2 = mannwhitneyu(a2, c2, alternative='greater').pvalue if a2 and c2 else 1
    rd.rec('UR2', 'rectangular seals with a stroked U are larger than with plain 700', 'median %.1f (n %d) against %.1f (n %d), p = %.4f' % (med(a2), len(a2), med(c2), len(c2), p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'UR1 %s, UR2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
