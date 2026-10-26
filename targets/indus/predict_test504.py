"""Set 504 (goal run loop 150): marked fish (231-240, not caged) and 806 by seal size (auditkit strata).
Writes results/predict_test504.md."""
import auditkit
import rtools as R

MARKED = {'231', '233', '234', '235', '237', '238', '239', '240'}


def main():
    rd = R.Round('Five-hundred-and-fourth registered predictions: goal loop 150, marked fish and 806 by seal size', 'predict_test504')
    o1, p1 = auditkit.size_motif(lambda t: bool(MARKED & set(t)))
    rd.rec('MK1', 'large and small seals differ in carrying a marked fish (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '806' in t)
    rd.rec('MK2', 'they differ in carrying 806 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'MK1 %s, MK2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
