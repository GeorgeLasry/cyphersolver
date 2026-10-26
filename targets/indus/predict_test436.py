"""Set 436 (goal run loop 82): tablets with one inscribed side against two or more (ICIT field 21). Split C.
Writes results/predict_test436.md."""
import loopkit as L
import rtools as R
from predict_test371 import test


def main():
    rd = R.Round('Four-hundred-and-thirty-sixth registered predictions: goal loop 82, one-sided against multi-sided tablets', 'predict_test436')
    sides = L.field(21)
    lab = lambda t: None if t not in sides else ('one' if sides[t] == '1' else 'multi')
    _, (tr, te) = L.splits_c()
    o1 = test(tr, te, lab, 'one', 'multi', lambda t: L.SUBTYPE.get(t) == 'TAB:B', rd, 'SD1', 'moulded tablets')
    o2 = test(tr, te, lab, 'one', 'multi', lambda t: L.SUBTYPE.get(t) == 'TAB:I', rd, 'SD2', 'incised tablets')
    rd.rec('P', 'progress rule: either holds', 'SD1 %s, SD2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
