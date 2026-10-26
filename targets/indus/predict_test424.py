"""Set 424 (goal run loop 70): audit of set 423 ST2 against site. Writes results/predict_test424.md."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-twenty-fourth registered predictions: goal loop 70, audit of set 423 against site', 'predict_test424')
    A, B, rowsA, recs, F = R.load_all()
    tab_texts = {tuple(ln) for r in F if recs.get(r['sealid']) and str(recs[r['sealid']][20]).startswith('TAB') for ln in r['seq'] if ln}
    sq = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL:S') and r['flat']:
            try:
                sz = float(rec[31])
            except (TypeError, ValueError):
                continue
            if sz > 0:
                sq.append((sz, tuple(r['flat']), r['site']))
    cut = median(s for s, t, x in sq)
    band = lambda t: min(max(len(t), 2), 7)

    def mh(rows, strat):
        tabs = []
        for k in sorted({strat(t, x) for s, t, x in rows}):
            sm = [t in tab_texts for s, t, x in rows if strat(t, x) == k and s <= cut]
            lg = [t in tab_texts for s, t, x in rows if strat(t, x) == k and s > cut]
            tabs.append([[sum(sm), len(sm) - sum(sm)], [sum(lg), len(lg) - sum(lg)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(sq, lambda t, x: (band(t), x))
    rd.rec('SA1', 'ST2 holds stratified by length x site', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh([r for r in sq if r[2] == 'Harappa'], lambda t, x: band(t))
    rd.rec('SA2', 'ST2 holds within Harappa', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: none (audit)', 'SA1 %s, SA2 %s' % (o1 > 1 and p1 < 0.05, o2 > 1 and p2 < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
