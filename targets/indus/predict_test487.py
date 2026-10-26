"""Set 487 (goal run loop 133): numeral + 520 and post-ending 90 by seal size (sizekit). Writes results/predict_test487.md."""
import rtools as R
import sizekit


def main():
    rd = R.Round('Four-hundred-and-eighty-seventh registered predictions: goal loop 133, numeral + 520 and post-ending 90 by size', 'predict_test487')
    sizekit._SQ = None
    o1, p1 = sizekit.size_test(lambda t: any(t[i] in R.NUMS and t[i + 1] == '520' for i in range(len(t) - 1)))
    rd.rec('NE1', 'large and small seals differ in carrying a numeral directly before 520 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = sizekit.size_test(lambda t: any(t[i] in R.END and t[i + 1] == '90' for i in range(len(t) - 1)))
    rd.rec('NE2', 'they differ in carrying 90 directly after an ending (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: NE2 (NE1 overlaps the formula, 33 520)', 'NE1 %s, NE2 %s' % (p1 < 0.05, p2 < 0.05), p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
