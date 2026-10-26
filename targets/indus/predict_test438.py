"""Set 438 (goal run loop 84): towns against the big cities inside square seals. Split C. Writes results/predict_test438.md."""
import loopkit as L
import rtools as R
from predict_test371 import test


def main():
    rd = R.Round('Four-hundred-and-thirty-eighth registered predictions: goal loop 84, towns against cities', 'predict_test438')
    site = lambda t: L.META.get(t, ('', '', ''))[0]
    reg = lambda t: R.region(site(t))
    _, (tr, te) = L.splits_c()
    sq = lambda t: L.SUBTYPE.get(t) == 'SEAL:S'
    o1 = test(tr, te, lambda t: None if reg(t) != 'north' else ('city' if site(t) == 'Harappa' else 'town'), 'town', 'city', sq, rd, 'TC1', 'northern towns against Harappa')
    o2 = test(tr, te, lambda t: {'Chanhu-daro': 'town', 'Mohenjo-daro': 'city'}.get(site(t)), 'town', 'city', sq, rd, 'TC2', 'Chanhu-daro against Mohenjo-daro')
    rd.rec('P', 'progress rule: either holds', 'TC1 %s, TC2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
