"""Set 426 (goal run loop 72): audit of set 384 BR1 (rectangular against square seal signs) within one city.
Writes results/predict_test426.md."""
import loopkit as L
import rtools as R
from predict_test371 import test


def main():
    rd = R.Round('Four-hundred-and-twenty-sixth registered predictions: goal loop 72, audit of set 384 within a city', 'predict_test426')
    _, (tr, te) = L.splits_c()
    lab = lambda t: {'SEAL:R': 'rect', 'SEAL:S': 'square'}.get(L.SUBTYPE.get(t))
    site = lambda t: L.META.get(t, ('', '', ''))[0]
    o1 = test(tr, te, lab, 'rect', 'square', lambda t: site(t) == 'Mohenjo-daro', rd, 'RS1', 'within Mohenjo-daro')
    o2 = test(tr, te, lab, 'rect', 'square', lambda t: site(t) == 'Harappa', rd, 'RS2', 'within Harappa')
    rd.rec('P', 'progress rule: none (audit)', 'RS1 %s, RS2 %s' % (o1, o2), False)
    rd.finish()


if __name__ == '__main__':
    main()
