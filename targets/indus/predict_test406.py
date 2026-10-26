"""Set 406 (goal run loop 52): the 520 class among endings by object kind and by seal size. Writes results/predict_test406.md."""
from statistics import median

import loopkit as L
import rtools as R
from predict_test379 import mantel_haenszel
from predict_test388 import objects


def last_end(t):
    for g in reversed(t):
        if g in R.END:
            return g
    return None


def main():
    rd = R.Round('Four-hundred-and-sixth registered predictions: goal loop 52, the 520 class by object kind and size', 'predict_test406')
    (tr, te), _ = L.splits()
    lines = [t for t in sorted(set(tr) | set(te)) if last_end(t)]
    kind = lambda t: {'SEAL': 'seal', 'TAB': 'tablet'}.get(L.META.get(t, ('', '', ''))[1])
    band = lambda t: min(max(len(t), 2), 7)
    tabs = []
    for b in sorted({band(t) for t in lines}):
        a_ = [last_end(t) == '520' for t in lines if band(t) == b and kind(t) == 'tablet']
        c_ = [last_end(t) == '520' for t in lines if band(t) == b and kind(t) == 'seal']
        tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
    o1, p1 = mantel_haenszel(tabs)
    rd.rec('EK1', 'tablets and seals differ in the 520 share among endings (two-sided)', 'odds ratio tablet/seal %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    sq = [(s, t) for s, t in objects('SEAL:S') if last_end(t)]
    cut = median(s for s, t in sq)
    tabs = []
    for b in sorted({band(t) for s, t in sq}):
        a_ = [last_end(t) == '520' for s, t in sq if band(t) == b and s > cut]
        c_ = [last_end(t) == '520' for s, t in sq if band(t) == b and s <= cut]
        tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
    o2, p2 = mantel_haenszel(tabs)
    rd.rec('EK2', 'large and small square seals differ in the 520 share (two-sided)', 'odds ratio large/small %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'EK1 %s, EK2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
