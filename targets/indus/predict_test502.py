"""Set 502 (goal run loop 148): audit of set 501 with length and site held: 590 against 156 seals.
Writes results/predict_test502.md."""
from statistics import median

import auditkit
import rtools as R
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Five-hundred-and-second registered predictions: goal loop 148, audit of the small-seal size grade', 'predict_test502')
    rows = auditkit.rows()
    cut = median(s for t, u, x, s in rows)
    band = lambda t: min(max(len(t), 2), 7)
    sel = [(t, x, s, '590' in t) for t, u, x, s in rows if ('590' in t) != ('156' in t)]

    def mh(strat):
        tabs = []
        for k in sorted({strat(t, x) for t, x, s, is590 in sel}):
            a = [s > cut for t, x, s, is590 in sel if strat(t, x) == k and is590]
            c = [s > cut for t, x, s, is590 in sel if strat(t, x) == k and not is590]
            tabs.append([[sum(a), len(a) - sum(a)], [sum(c), len(c) - sum(c)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda t, x: band(t))
    rd.rec('GA1', '590 seals are large more often than 156 seals within length bands', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh(lambda t, x: (band(t), x))
    rd.rec('GA2', 'the same within length band x site', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: none (audit of set 501)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
