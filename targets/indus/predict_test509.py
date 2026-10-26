"""Set 509 (goal run loop 155): 368 and 342 by seal size (auditkit strata). Writes results/predict_test509.md."""
import auditkit
import rtools as R


def main():
    rd = R.Round('Five-hundred-and-ninth registered predictions: goal loop 155, 368 and 342 by seal size', 'predict_test509')
    o1, p1 = auditkit.size_motif(lambda t: '368' in t)
    rd.rec('S368', 'large and small seals differ in carrying 368 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '342' in t)
    rd.rec('S342', 'they differ in carrying 342 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'S368 %s, S342 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
