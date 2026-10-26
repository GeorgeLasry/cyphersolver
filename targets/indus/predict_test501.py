"""Set 501 (goal run loop 147): the small-seal signs by size within small seals, and by Mohenjo-daro phase.
Writes results/predict_test501.md."""
import auditkit
import loopkit as L
import rtools as R
from scipy.stats import chi2_contingency, kruskal


def main():
    rd = R.Round('Five-hundred-and-first registered predictions: goal loop 147, small-seal signs by size and phase', 'predict_test501')
    rows = auditkit.rows()
    pick = lambda t: next((g for g in ('156', '400', '590') if g in t), None)
    groups = [[s for t, u, x, s in rows if pick(t) == g] for g in ('156', '400', '590')]
    p1 = kruskal(*groups).pvalue if all(groups) else 1
    med = lambda v: sorted(v)[len(v) // 2] if v else 0
    rd.rec('SG1', 'the three small-seal signs sit on seals of different sizes (Kruskal-Wallis)', 'medians %s, p = %.4f' % ([med(v) for v in groups], p1), p1 < 0.05)
    ph = L.field(9)
    era = lambda t: {'Early': 'e', 'Intermediate': 'e', 'Late': 'l'}.get(ph.get(t))
    tab = [[sum(1 for t, u, x, s in rows if x == 'Mohenjo-daro' and era(t) == e and pick(t) == g) for g in ('156', '400', '590')] for e in ('e', 'l')]
    ok = all(sum(r) for r in tab) and all(sum(c) for c in zip(*tab))
    p2 = chi2_contingency(tab)[1] if ok else 1
    rd.rec('SG2', 'the choice differs between Mohenjo-daro phases', '%s, p = %.4f' % (tab, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'SG1 %s, SG2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
