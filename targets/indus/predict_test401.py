"""Set 401 (goal run loop 47): inscribed pottery against square seals. Writes results/predict_test401.md."""
import loopkit as L
import rtools as R
from predict_test371 import test
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-first registered predictions: goal loop 47, pottery against seals', 'predict_test401')
    _, (tr, te) = L.splits_c()
    kind = lambda t: 'pot' if L.META.get(t, ('', '', ''))[1] == 'POT' else ('seal' if L.SUBTYPE.get(t) == 'SEAL:S' else None)
    o1 = test(tr, te, kind, 'pot', 'seal', lambda t: True, rd, 'PT1', 'pottery against square seals')
    allines = sorted(set(tr) | set(te))
    band = lambda t: min(max(len(t), 2), 7)
    ends = lambda t: any(g in R.END for g in t[-2:])
    tabs = []
    for b in sorted({band(t) for t in allines}):
        a_ = [ends(t) for t in allines if band(t) == b and kind(t) == 'pot']
        c_ = [ends(t) for t in allines if band(t) == b and kind(t) == 'seal']
        tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
    o2, p2 = mantel_haenszel(tabs)
    ok2 = o2 < 1 and p2 < 0.05
    rd.rec('PT2', 'pottery texts close with 740/520 less often at equal length', 'odds ratio %.2f, p = %.4f' % (o2, p2), ok2)
    rd.rec('P', 'progress rule: PT1 (replicated finding)', 'PT1 %s' % o1, o1)
    rd.finish()


if __name__ == '__main__':
    main()
