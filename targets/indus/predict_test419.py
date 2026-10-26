"""Set 419 (goal run loop 65): Gujarat against Sindh within square seals. Writes results/predict_test419.md."""
import loopkit as L
import rtools as R
from predict_test371 import test
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-nineteenth registered predictions: goal loop 65, Gujarat against Sindh square seals', 'predict_test419')
    reg = lambda t: R.region(L.META.get(t, ('', '', ''))[0])
    _, (tr, te) = L.splits_c()
    o1 = test(tr, te, reg, 'gujarat', 'sindh', lambda t: L.SUBTYPE.get(t) == 'SEAL:S', rd, 'GS1', 'Gujarat against Sindh square seals')
    lines = [t for t in sorted(set(tr) | set(te)) if L.SUBTYPE.get(t) == 'SEAL:S']
    band = lambda t: min(max(len(t), 2), 7)
    ends = lambda t: any(g in R.END for g in t[-2:])
    tabs = []
    for b in sorted({band(t) for t in lines}):
        a_ = [ends(t) for t in lines if band(t) == b and reg(t) == 'gujarat']
        c_ = [ends(t) for t in lines if band(t) == b and reg(t) == 'sindh']
        tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
    o2, p2 = mantel_haenszel(tabs)
    rd.rec('GS2', 'Gujarat square seals differ in closing with 740/520 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'GS1 %s, GS2 %s' % (o1, p2 < 0.05), o1 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
