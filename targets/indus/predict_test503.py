"""Set 503 (goal run loop 149): fish + 740 and the sign 60 by seal size (auditkit: length x site x motif strata).
Writes results/predict_test503.md."""
import auditkit
import rtools as R
from predict_test448 import FISH


def main():
    rd = R.Round('Five-hundred-and-third registered predictions: goal loop 149, fish + 740 and 60 by seal size', 'predict_test503')
    o1, p1 = auditkit.size_motif(lambda t: any(FISH(t[i]) and t[i + 1] == '740' for i in range(len(t) - 1)))
    rd.rec('F7', 'large and small seals differ in carrying fish + 740 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: '60' in t)
    rd.rec('S60', 'they differ in carrying 60 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'F7 %s, S60 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
