"""Set 510 (goal run loop 156): 550 and 527 by seal size (auditkit strata). Writes results/predict_test510.md."""
import auditkit
import rtools as R


def main():
    rd = R.Round('Five-hundred-and-tenth registered predictions: goal loop 156, 550 and 527 by seal size', 'predict_test510')
    o1, p1 = auditkit.size_motif(lambda t: '550' in t)
    rd.rec('S550', 'large and small seals differ in carrying 550 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '527' in t)
    rd.rec('S527', 'they differ in carrying 527 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'S550 %s, S527 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
