"""Set 444 (goal run loop 90): the closing formula over time (Mohenjo-daro phases, Harappa periods). Writes results/predict_test444.md."""
import loopkit as L
import rtools as R
from predict_test379 import mantel_haenszel
from predict_test385 import era as hera
from predict_test441 import has_formula


def main():
    rd = R.Round('Four-hundred-and-forty-fourth registered predictions: goal loop 90, the closing formula over time', 'predict_test444')
    ph, per = L.field(9), L.field(8)
    (tr, te), (DA, DB) = L.splits()
    lines = sorted(set(tr) | set(te) | set(DA))
    site = lambda t: L.META.get(t, ('', '', ''))[0]
    md = lambda t: {'Early': 'early', 'Intermediate': 'early', 'Late': 'late'}.get(ph.get(t)) if site(t) == 'Mohenjo-daro' else None
    hp = lambda t: hera(per.get(t, '')) if site(t) == 'Harappa' else None
    strat = lambda t: (min(max(len(t), 2), 7), L.SUBTYPE.get(t, ''))

    def mh(era):
        rows = [t for t in lines if era(t)]
        tabs = []
        for k in sorted({strat(t) for t in rows}):
            a = [has_formula(t) for t in rows if strat(t) == k and era(t) == 'late']
            b = [has_formula(t) for t in rows if strat(t) == k and era(t) == 'early']
            tabs.append([[sum(a), len(a) - sum(a)], [sum(b), len(b) - sum(b)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(md)
    rd.rec('FT1', 'the formula changes between Mohenjo-daro phases (two-sided)', 'odds ratio late/early %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = mh(hp)
    rd.rec('FT2', 'the formula changes between Harappa periods (two-sided)', 'odds ratio late/early %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'FT1 %s, FT2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
