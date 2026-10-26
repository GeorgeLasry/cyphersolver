"""Set 476 (goal run loop 122): stroked jars and mid-line 2 / 60 by seal size (sizekit). Writes results/predict_test476.md."""
import rtools as R
from sizekit import size_test

STROKED = {'741', '742', '744', '745', '746'}


def main():
    rd = R.Round('Four-hundred-and-seventy-sixth registered predictions: goal loop 122, stroked jars and mid-line 2 / 60 by size', 'predict_test476')
    o1, p1 = size_test(lambda t: bool(STROKED & set(t)))
    rd.rec('SJ1', 'large and small seals differ in carrying a stroked jar (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = size_test(lambda t: any(t[i] in ('2', '60') for i in range(1, len(t) - 1)))
    rd.rec('SJ2', 'they differ in carrying 2 or 60 mid-line (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'SJ1 %s, SJ2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
