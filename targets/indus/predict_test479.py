"""Set 479 (goal run loop 125): plain U 700 and short-stroked U 702 / 703 by seal size (sizekit). Writes results/predict_test479.md."""
import rtools as R
import sizekit


def main():
    rd = R.Round('Four-hundred-and-seventy-ninth registered predictions: goal loop 125, plain and short-stroked U by size', 'predict_test479')
    sizekit._SQ = None
    o1, p1 = sizekit.size_test(lambda t: '700' in t)
    rd.rec('PU1', 'large and small seals differ in carrying the plain U 700 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = sizekit.size_test(lambda t: '702' in t or '703' in t)
    rd.rec('PU2', 'they differ in carrying the short-stroked U 702 / 703 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'PU1 %s, PU2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
