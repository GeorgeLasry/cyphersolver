"""Set 511 (goal run loop 157): 817 and 861 by seal size (auditkit strata). Writes results/predict_test511.md."""
import auditkit
import rtools as R


def main():
    rd = R.Round('Five-hundred-and-eleventh registered predictions: goal loop 157, 817 and 861 by seal size', 'predict_test511')
    o1, p1 = auditkit.size_motif(lambda t: '817' in t)
    rd.rec('S817', 'large and small seals differ in carrying 817 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '861' in t)
    rd.rec('S861', 'they differ in carrying 861 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'S817 %s, S861 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
