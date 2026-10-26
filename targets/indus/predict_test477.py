"""Set 477 (goal run loop 123): bare texts (no ending) and opening fish by seal size (sizekit). Writes results/predict_test477.md."""
import rtools as R
from predict_test448 import FISH
from sizekit import size_test


def main():
    rd = R.Round('Four-hundred-and-seventy-seventh registered predictions: goal loop 123, bare texts and opening fish by size', 'predict_test477')
    o1, p1 = size_test(lambda t: not any(g in R.END for g in t))
    rd.rec('SB1', 'large and small seals differ in carrying texts with no ending (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = size_test(lambda t: FISH(t[0]))
    rd.rec('SB2', 'they differ in texts opening with a fish (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'SB1 %s, SB2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
