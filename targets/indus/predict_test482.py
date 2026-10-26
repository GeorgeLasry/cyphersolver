"""Set 482 (goal run loop 128): pieces of the long form by seal size (sizekit): 33 outside the formula; fish + 705/706
without 33. Writes results/predict_test482.md."""
import rtools as R
import sizekit
from predict_test441 import has_formula
from predict_test448 import FISH


def main():
    rd = R.Round('Four-hundred-and-eighty-second registered predictions: goal loop 128, pieces of the long form by size', 'predict_test482')
    sizekit._SQ = None
    o1, p1 = sizekit.size_test(lambda t: '33' in t and not has_formula(t))
    rd.rec('PL1', 'large and small seals differ in carrying 33 outside the formula (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = sizekit.size_test(lambda t: any(FISH(t[i]) and t[i + 1] in ('705', '706') and (i + 2 >= len(t) or t[i + 2] != '33') for i in range(len(t) - 1)))
    rd.rec('PL2', 'they differ in carrying fish + stroked U without 33 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'PL1 %s, PL2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
