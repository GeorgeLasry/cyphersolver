"""Set 471 (goal run loop 117): fish signs and the 740 ending by seal size (sizekit). Writes results/predict_test471.md."""
import rtools as R
from predict_test448 import FISH
from sizekit import size_test


def main():
    rd = R.Round('Four-hundred-and-seventy-first registered predictions: goal loop 117, fish signs and 740 by seal size', 'predict_test471')
    o1, p1 = size_test(lambda t: any(FISH(g) for g in t))
    rd.rec('SK1', 'large and small seals differ in carrying a fish sign (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = size_test(lambda t: any(g == '740' for g in t[-2:]))
    rd.rec('SK2', 'large and small seals differ in ending with 740 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'SK1 %s, SK2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
