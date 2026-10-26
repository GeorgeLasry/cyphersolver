"""Set 483 (goal run loop 129): set 384's rectangular / square seal signs by square-seal size (sizekit).
Writes results/predict_test483.md."""
import rtools as R
import sizekit


def main():
    rd = R.Round('Four-hundred-and-eighty-third registered predictions: goal loop 129, bar-seal signs by size', 'predict_test483')
    sizekit._SQ = None
    o1, p1 = sizekit.size_test(lambda t: bool({'1', '407', '55', '806'} & set(t)))
    rd.rec('BS1', 'on square seals, the rectangular-seal signs differ by size (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = sizekit.size_test(lambda t: bool({'390', '741', '760'} & set(t)))
    rd.rec('BS2', 'the square-seal signs 390 / 741 / 760 differ by size (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'BS1 %s, BS2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
