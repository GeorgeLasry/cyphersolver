"""Set 480 (goal run loop 126): yoke-carrier signs by seal size (sizekit). Writes results/predict_test480.md."""
import rtools as R
import sizekit


def main():
    rd = R.Round('Four-hundred-and-eightieth registered predictions: goal loop 126, yoke-carriers by seal size', 'predict_test480')
    sizekit._SQ = None
    o1, p1 = sizekit.size_test(lambda t: bool({'154', '155', '157', '158'} & set(t)))
    rd.rec('YC1', 'large and small seals differ in carrying 154 / 155 / 157 / 158 (the family without 156; two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = sizekit.size_test(lambda t: '151' in t)
    rd.rec('YC2', 'they differ in carrying the plain yoke-carrier 151 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'YC1 %s, YC2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
