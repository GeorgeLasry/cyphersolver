"""Set 507 (goal run loop 153): 415 and 455 by seal size (auditkit strata). Writes results/predict_test507.md."""
import auditkit
import rtools as R


def main():
    rd = R.Round('Five-hundred-and-seventh registered predictions: goal loop 153, 415 and 455 by seal size', 'predict_test507')
    o1, p1 = auditkit.size_motif(lambda t: '415' in t)
    rd.rec('S415', 'large and small seals differ in carrying 415 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '455' in t)
    rd.rec('S455', 'they differ in carrying 455 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'S415 %s, S455 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
