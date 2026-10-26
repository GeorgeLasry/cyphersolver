"""Set 473 (goal run loop 119): the 'man' sign 90 and text variety by seal size (sizekit). Writes results/predict_test473.md."""
import rtools as R
from sizekit import size_test


def main():
    rd = R.Round('Four-hundred-and-seventy-third registered predictions: goal loop 119, 90 and variety by seal size', 'predict_test473')
    o1, p1 = size_test(lambda t: '90' in t)
    rd.rec('SM1', "large and small seals differ in carrying the 'man' sign 90 (two-sided)", 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = size_test(lambda t: len(set(t)) == len(t))
    rd.rec('SM2', 'they differ in texts with no repeated sign (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'SM1 %s, SM2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
