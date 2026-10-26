"""Set 485 (goal run loop 131): graphic families by seal size (sizekit): ICIT 800-819 tree / plant block; 90-99 man block.
Writes results/predict_test485.md."""
import rtools as R
import sizekit


def fam(lo, hi):
    return lambda t: any(g.isdigit() and lo <= int(g) <= hi for g in t)


def main():
    rd = R.Round('Four-hundred-and-eighty-fifth registered predictions: goal loop 131, sign families by seal size', 'predict_test485')
    sizekit._SQ = None
    o1, p1 = sizekit.size_test(fam(800, 819))
    rd.rec('GF1', 'large and small seals differ in carrying a sign of the 800-819 block (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = sizekit.size_test(fam(90, 99))
    rd.rec('GF2', 'they differ in carrying a sign of the 90-99 (man) block (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'GF1 %s, GF2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
