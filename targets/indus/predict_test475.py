"""Set 475 (goal run loop 121): 520 and the short fish-name form by seal size (sizekit). Writes results/predict_test475.md."""
import rtools as R
from predict_test441 import has_formula
from predict_test448 import FISH
from sizekit import size_test


def main():
    rd = R.Round('Four-hundred-and-seventy-fifth registered predictions: goal loop 121, 520 and the short form by size', 'predict_test475')
    o1, p1 = size_test(lambda t: '520' in t)
    rd.rec('S5A', 'large and small seals differ in carrying 520 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = size_test(lambda t: not has_formula(t) and any(FISH(t[i]) and t[i + 1] == '520' for i in range(len(t) - 1)))
    rd.rec('S5B', 'they differ in carrying the short form fish 520 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'S5A %s, S5B %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
