"""Set 433 (goal run loop 79): seal size inside the U family (700 plain, 705, 706 with inner strokes).
Writes results/predict_test433.md."""
import rtools as R
from predict_test388 import objects
from scipy.stats import mannwhitneyu


def main():
    rd = R.Round('Four-hundred-and-thirty-third registered predictions: goal loop 79, seal size in the U family', 'predict_test433')
    sq = objects('SEAL:S')
    s706 = [s for s, t in sq if '706' in t]
    s705 = [s for s, t in sq if '705' in t and '706' not in t]
    s700 = [s for s, t in sq if '700' in t and '705' not in t and '706' not in t]
    p1 = mannwhitneyu(s706, s705, alternative='greater').pvalue if s706 and s705 else 1
    p2 = mannwhitneyu(s706, s700, alternative='greater').pvalue if s706 and s700 else 1
    med = lambda x: sorted(x)[len(x) // 2] if x else 0
    rd.rec('U1', '706 seals are larger than 705 seals', '706 median %.1f (n %d), 705 %.1f (n %d), p = %.4f' % (med(s706), len(s706), med(s705), len(s705), p1), p1 < 0.05)
    rd.rec('U2', '706 seals are larger than plain-700 seals', '706 median %.1f, 700 %.1f (n %d), p = %.4f' % (med(s706), med(s700), len(s700), p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'U1 %s, U2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
