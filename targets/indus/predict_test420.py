"""Set 420 (goal run loop 66): copper tablets against incised and against moulded tablets (skew test, split C).
Writes results/predict_test420.md."""
import loopkit as L
import rtools as R
from predict_test371 import test


def main():
    rd = R.Round('Four-hundred-and-twentieth registered predictions: goal loop 66, copper tablets against other tablets', 'predict_test420')
    _, (tr, te) = L.splits_c()
    st = lambda t: L.SUBTYPE.get(t)
    o1 = test(tr, te, st, 'TAB:C', 'TAB:I', lambda t: True, rd, 'CI1', 'copper against incised tablets')
    o2 = test(tr, te, st, 'TAB:C', 'TAB:B', lambda t: True, rd, 'CI2', 'copper against moulded tablets')
    rd.rec('P', 'progress rule: either holds', 'CI1 %s, CI2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
