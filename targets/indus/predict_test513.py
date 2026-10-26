"""Set 513 (goal run loop 159): 920 and 692 by seal size (auditkit strata). Writes results/predict_test513.md."""
import auditkit
import rtools as R


def main():
    rd = R.Round('Five-hundred-and-thirteenth registered predictions: goal loop 159, 920 and 692 by seal size', 'predict_test513')
    o1, p1 = auditkit.size_motif(lambda t: '920' in t)
    rd.rec('S920', 'large and small seals differ in carrying 920 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '692' in t)
    rd.rec('S692', 'they differ in carrying 692 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'S920 %s, S692 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
