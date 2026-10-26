"""Set 425 (goal run loop 71): audit of set 380 HS2 (small seals repeat texts) against site. Writes results/predict_test425.md."""
from collections import Counter
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-twenty-fifth registered predictions: goal loop 71, audit of set 380 against site', 'predict_test425')
    A, B, rowsA, recs, F = R.load_all()
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
    cnt = Counter(t for s, t, x in sq)
    cut = median(s for s, t, x in sq)
    band = lambda t: min(max(len(t), 2), 7)

    def mh(rows, strat):
        tabs = []
        for k in sorted({strat(t, x) for s, t, x in rows}):
            sm = [cnt[t] > 1 for s, t, x in rows if strat(t, x) == k and s <= cut]
            lg = [cnt[t] > 1 for s, t, x in rows if strat(t, x) == k and s > cut]
            tabs.append([[sum(sm), len(sm) - sum(sm)], [sum(lg), len(lg) - sum(lg)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(sq, lambda t, x: (band(t), x))
    rd.rec('RA1', 'HS2 holds stratified by length x site', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh([r for r in sq if r[2] == 'Mohenjo-daro'], lambda t, x: band(t))
    rd.rec('RA2', 'HS2 holds within Mohenjo-daro', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: none (audit)', 'RA1 %s, RA2 %s' % (o1 > 1 and p1 < 0.05, o2 > 1 and p2 < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
