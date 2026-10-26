"""Set 506 (goal run loop 152): the fish 235 and 233 by seal size (auditkit strata). Writes results/predict_test506.md."""
import auditkit
import rtools as R


def main():
    rd = R.Round('Five-hundred-and-sixth registered predictions: goal loop 152, fish 235 and 233 by seal size', 'predict_test506')
    o1, p1 = auditkit.size_motif(lambda t: '235' in t)
    rd.rec('F235', 'large and small seals differ in carrying 235 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '233' in t)
    rd.rec('F233', 'they differ in carrying 233 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'F235 %s, F233 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
