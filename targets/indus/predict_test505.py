"""Set 505 (goal run loop 151): the fish 220 and 240 by seal size (auditkit strata). Writes results/predict_test505.md."""
import auditkit
import rtools as R


def main():
    rd = R.Round('Five-hundred-and-fifth registered predictions: goal loop 151, fish 220 and 240 by seal size', 'predict_test505')
    o1, p1 = auditkit.size_motif(lambda t: '220' in t)
    rd.rec('F220', 'large and small seals differ in carrying 220 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '240' in t)
    rd.rec('F240', 'they differ in carrying 240 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'F220 %s, F240 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
