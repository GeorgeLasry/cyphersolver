"""Set 386 (goal run loop 32): faience against steatite square seals; incised against moulded tablets (split C).
Writes results/predict_test386.md."""
import loopkit as L
import rtools as R
from predict_test371 import test


def main():
    rd = R.Round('Three-hundred-and-eighty-sixth registered predictions: goal loop 32, material and tablet kind', 'predict_test386')
    _, (tr, te) = L.splits_c()
    mat = L.field(13)
    o1 = test(tr, te, lambda t: mat.get(t), 'Faience', 'Steatite', lambda t: L.SUBTYPE.get(t) == 'SEAL:S', rd, 'FM1', 'faience against steatite square seals')
    o2 = test(tr, te, lambda t: L.SUBTYPE.get(t), 'TAB:I', 'TAB:B', lambda t: True, rd, 'FM2', 'incised against moulded tablets')
    rd.rec('P', 'progress rule: either holds', 'FM1 %s, FM2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
