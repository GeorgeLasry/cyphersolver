"""Set 486 (goal run loop 132): the U family and the jar family by seal size (sizekit). Writes results/predict_test486.md."""
import rtools as R
import sizekit
from predict_test485 import fam


def main():
    rd = R.Round('Four-hundred-and-eighty-sixth registered predictions: goal loop 132, U and jar families by seal size', 'predict_test486')
    sizekit._SQ = None
    o1, p1 = sizekit.size_test(fam(700, 706))
    rd.rec('UJ1', 'large and small seals differ in carrying a U sign 700-706 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = sizekit.size_test(fam(741, 749))
    rd.rec('UJ2', 'they differ in carrying a marked jar 741-749 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: UJ2 (UJ1 overlaps the formula of set 441)', 'UJ1 %s, UJ2 %s' % (p1 < 0.05, p2 < 0.05), p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
