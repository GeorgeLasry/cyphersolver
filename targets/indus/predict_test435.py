"""Set 435 (goal run loop 81): seal size with other marked signs: stroked jars; caged fish. Writes results/predict_test435.md."""
import rtools as R
from predict_test388 import objects
from scipy.stats import mannwhitneyu

STROKED = {'741', '742', '744', '745', '746'}
CAGED = {'226', '232', '153', '236', '241'}
FISH = {'220', '231', '235', '240', '233'}


def main():
    rd = R.Round('Four-hundred-and-thirty-fifth registered predictions: goal loop 81, seal size with marked signs', 'predict_test435')
    sq = objects('SEAL:S')
    med = lambda x: sorted(x)[len(x) // 2] if x else 0
    a = [s for s, t in sq if STROKED & set(t)]
    c = [s for s, t in sq if '740' in t and not STROKED & set(t)]
    p1 = mannwhitneyu(a, c, alternative='greater').pvalue
    rd.rec('MS1', 'seals with stroked jars are larger than seals with only the plain jar', 'median %.1f (n %d) against %.1f (n %d), p = %.4f' % (med(a), len(a), med(c), len(c), p1), p1 < 0.05)
    a2 = [s for s, t in sq if CAGED & set(t)]
    c2 = [s for s, t in sq if FISH & set(t) and not CAGED & set(t)]
    p2 = mannwhitneyu(a2, c2, alternative='greater').pvalue if a2 else 1
    rd.rec('MS2', 'seals with caged fish are larger than seals with plain fish', 'median %.1f (n %d) against %.1f (n %d), p = %.4f' % (med(a2), len(a2), med(c2), len(c2), p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'MS1 %s, MS2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
