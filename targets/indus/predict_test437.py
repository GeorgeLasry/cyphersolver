"""Set 437 (goal run loop 83): one-line against multi-line square seals. Writes results/predict_test437.md."""
import loopkit as L
import rtools as R
from predict_test371 import test
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-thirty-seventh registered predictions: goal loop 83, one-line against multi-line seals', 'predict_test437')
    lab = lambda t: None if L.SUBTYPE.get(t) != 'SEAL:S' else ('multi' if t in L.OTHERS else 'one')
    _, (tr, te) = L.splits_c()
    o1 = test(tr, te, lab, 'one', 'multi', lambda t: True, rd, 'ML1', 'one-line against multi-line square seals')
    lines = sorted(set(tr) | set(te))
    band = lambda t: min(max(len(t), 2), 7)
    ends = lambda t: any(g in R.END for g in t[-2:])
    tabs = []
    for b in sorted({band(t) for t in lines}):
        a_ = [ends(t) for t in lines if band(t) == b and lab(t) == 'multi']
        c_ = [ends(t) for t in lines if band(t) == b and lab(t) == 'one']
        tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
    o2, p2 = mantel_haenszel(tabs)
    rd.rec('ML2', 'lines of multi-line seals differ in closing with 740/520 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'ML1 %s, ML2 %s' % (o1, p2 < 0.05), o1 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
