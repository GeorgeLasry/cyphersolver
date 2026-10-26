"""Set 417 (goal run loop 63): signs over time: Mohenjo-daro phases and Harappa periods (skew test, split C).
Writes results/predict_test417.md."""
import loopkit as L
import rtools as R
from predict_test371 import test
from predict_test385 import era as hera


def main():
    rd = R.Round('Four-hundred-and-seventeenth registered predictions: goal loop 63, signs over time', 'predict_test417')
    _, (tr, te) = L.splits_c()
    ph, per = L.field(9), L.field(8)
    md = lambda t: {'Early': 'early', 'Intermediate': 'early', 'Late': 'late'}.get(ph.get(t)) if L.META.get(t, ('', '', ''))[0] == 'Mohenjo-daro' else None
    hp = lambda t: hera(per.get(t, '')) if L.META.get(t, ('', '', ''))[0] == 'Harappa' else None
    o1 = test(tr, te, md, 'early', 'late', lambda t: True, rd, 'TM1', 'Mohenjo-daro early/intermediate against late')
    o2 = test(tr, te, hp, 'early', 'late', lambda t: True, rd, 'TM2', 'Harappa early (to 3B) against late (3C on)')
    rd.rec('P', 'progress rule: either holds', 'TM1 %s, TM2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
