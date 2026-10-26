"""Set 462 (goal run loop 108): seal size and signs, stratified, split C: rectangular seals; square seals (held-out check
of set 430). Writes results/predict_test462.md."""
import loopkit as L
import rtools as R
from predict_test461 import run


def main():
    rd = R.Round('Four-hundred-and-sixty-second registered predictions: goal loop 108, seal size and signs on split C', 'predict_test462')
    _, (tr, te) = L.splits_c()
    o1 = run('SEAL:R', tr, te, rd, 'RS1')
    o2 = run('SEAL:S', tr, te, rd, 'RS2')
    rd.rec('P', 'progress rule: RS1 only (RS2 is consistency)', 'RS1 %s, RS2 %s' % (o1, o2), o1)
    rd.finish()


if __name__ == '__main__':
    main()
