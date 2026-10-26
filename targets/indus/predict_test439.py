"""Set 439 (goal run loop 85): unicorn seals with and without the 'standard' (secondary motif SAN, field 19).
Writes results/predict_test439.md."""
import loopkit as L
import rtools as R
from predict_test371 import test
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-thirty-ninth registered predictions: goal loop 85, unicorn seals with the standard', 'predict_test439')
    mot, sec = L.field(18), L.field(19)
    lab = lambda t: None if L.SUBTYPE.get(t) != 'SEAL:S' or not str(mot.get(t, '')).startswith('Bull1') else ('san' if sec.get(t, '').startswith('SAN') else 'none')
    _, (tr, te) = L.splits_c()
    o1 = test(tr, te, lab, 'san', 'none', lambda t: True, rd, 'SN1', 'unicorn seals with against without the standard')
    lines = sorted(set(tr) | set(te))
    band = lambda t: min(max(len(t), 2), 7)
    ends = lambda t: any(g in R.END for g in t[-2:])
    tabs = []
    for b in sorted({band(t) for t in lines}):
        a_ = [ends(t) for t in lines if band(t) == b and lab(t) == 'san']
        c_ = [ends(t) for t in lines if band(t) == b and lab(t) == 'none']
        tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
    o2, p2 = mantel_haenszel(tabs)
    rd.rec('SN2', 'they differ in closing with 740/520 at equal length (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'SN1 %s, SN2 %s' % (o1, p2 < 0.05), o1 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
