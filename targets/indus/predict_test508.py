"""Set 508 (goal run loop 154): 798 and 820 by seal size (auditkit strata). Writes results/predict_test508.md."""
import auditkit
import rtools as R


def main():
    rd = R.Round('Five-hundred-and-eighth registered predictions: goal loop 154, 798 and 820 by seal size', 'predict_test508')
    o1, p1 = auditkit.size_motif(lambda t: '798' in t)
    rd.rec('S798', 'large and small seals differ in carrying 798 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '820' in t)
    rd.rec('S820', 'they differ in carrying 820 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'S798 %s, S820 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
