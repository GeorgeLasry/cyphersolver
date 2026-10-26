"""Set 474 (goal run loop 120): 740 anywhere, and 400 after an ending, by seal size (sizekit). Writes results/predict_test474.md."""
import rtools as R
from sizekit import size_test


def main():
    rd = R.Round('Four-hundred-and-seventy-fourth registered predictions: goal loop 120, 740 and post-ending 400 by size', 'predict_test474')
    o1, p1 = size_test(lambda t: '740' in t)
    rd.rec('SE1', 'large and small seals differ in carrying 740 anywhere (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = size_test(lambda t: any(t[i] in R.END and t[i + 1] == '400' for i in range(len(t) - 1)))
    rd.rec('SE2', 'they differ in carrying 400 directly after an ending (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds (SE2 overlaps set 430\'s 400; a pass there is counted only if 400 elsewhere does not carry it)', 'SE1 %s, SE2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
