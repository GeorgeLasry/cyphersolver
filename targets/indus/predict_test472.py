"""Set 472 (goal run loop 118): numeral first, any numeral, by seal size (sizekit). Writes results/predict_test472.md."""
import rtools as R
from sizekit import size_test


def main():
    rd = R.Round('Four-hundred-and-seventy-second registered predictions: goal loop 118, numerals by seal size', 'predict_test472')
    o1, p1 = size_test(lambda t: t[0] in R.NUMS)
    rd.rec('SN1', 'large and small seals differ in opening with a numeral (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = size_test(lambda t: any(g in R.NUMS for g in t))
    rd.rec('SN2', 'they differ in carrying any numeral (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'SN1 %s, SN2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
