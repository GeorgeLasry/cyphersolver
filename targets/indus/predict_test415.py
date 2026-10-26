"""Set 415 (goal run loop 61): seal colour (ICIT field 14: white = fired steatite, against other colours).
Writes results/predict_test415.md."""
import loopkit as L
import rtools as R
from predict_test371 import test
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-fifteenth registered predictions: goal loop 61, seal colour', 'predict_test415')
    col = L.field(14)
    lab = lambda t: None if L.SUBTYPE.get(t) != 'SEAL:S' or t not in col else ('white' if col[t] == 'White' else 'other')
    _, (tr, te) = L.splits_c()
    o1 = test(tr, te, lab, 'white', 'other', lambda t: True, rd, 'CL1', 'white against other-coloured square seals')
    lines = sorted(set(tr) | set(te))
    band = lambda t: min(max(len(t), 2), 7)
    ends = lambda t: any(g in R.END for g in t[-2:])
    tabs = []
    for b in sorted({band(t) for t in lines}):
        a_ = [ends(t) for t in lines if band(t) == b and lab(t) == 'other']
        c_ = [ends(t) for t in lines if band(t) == b and lab(t) == 'white']
        tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
    o2, p2 = mantel_haenszel(tabs)
    rd.rec('CL2', 'other-coloured seals differ in closing with 740/520 (two-sided)', 'odds ratio other/white %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'CL1 %s, CL2 %s' % (o1, p2 < 0.05), o1 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
