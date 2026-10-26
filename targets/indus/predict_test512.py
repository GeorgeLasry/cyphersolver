"""Set 512 (goal run loop 158): 840 and 176 by seal size (auditkit strata). Writes results/predict_test512.md."""
import auditkit
import rtools as R


def main():
    rd = R.Round('Five-hundred-and-twelfth registered predictions: goal loop 158, 840 and 176 by seal size', 'predict_test512')
    o1, p1 = auditkit.size_motif(lambda t: '840' in t)
    rd.rec('S840', 'large and small seals differ in carrying 840 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '176' in t)
    rd.rec('S176', 'they differ in carrying 176 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'S840 %s, S176 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
