"""Set 413 (goal run loop 59): the rectangular-seal formula: numeral first; count without ending. Writes results/predict_test413.md."""
import loopkit as L
import rtools as R
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-thirteenth registered predictions: goal loop 59, the rectangular-seal formula', 'predict_test413')
    (tr, te), _ = L.splits()
    lines = sorted(set(tr) | set(te))
    lab = lambda t: {'SEAL:R': 'r', 'SEAL:S': 's'}.get(L.SUBTYPE.get(t))
    band = lambda t: min(max(len(t), 2), 7)

    def mh(feat):
        tabs = []
        for b in sorted({band(t) for t in lines}):
            a_ = [feat(t) for t in lines if band(t) == b and lab(t) == 'r']
            c_ = [feat(t) for t in lines if band(t) == b and lab(t) == 's']
            tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda t: t[0] in R.NUMS)
    rd.rec('RF1', 'rectangular seals open with a numeral more often at equal length', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh(lambda t: any(g in R.NUMS for g in t) and not any(g in R.END for g in t))
    rd.rec('RF2', 'rectangular seals more often carry a numeral and no ending at equal length', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'RF1 %s, RF2 %s' % (o1 > 1 and p1 < 0.05, o2 > 1 and p2 < 0.05), (o1 > 1 and p1 < 0.05) or (o2 > 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
