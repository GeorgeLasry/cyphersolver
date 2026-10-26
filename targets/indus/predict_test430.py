"""Set 430 (goal run loop 76): audit of set 379's size signs: length x site strata; size by the second dimension.
Writes results/predict_test430.md."""
from statistics import median

import rtools as R
from predict_test379 import LARGE, SMALL, mantel_haenszel


def seals(field):
    A, B, rowsA, recs, F = R.load_all()
    out = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL:S') and r['flat']:
            try:
                sz = float(rec[field])
            except (TypeError, ValueError):
                continue
            if sz > 0:
                out.append((sz, tuple(r['flat']), r['site']))
    return out


def count(S, strat):
    cut = median(s for s, t, x in S)
    ok = 0
    lines = []
    for g in LARGE + SMALL:
        tabs = []
        for k in sorted({strat(t, x) for s, t, x in S}):
            lg = [t for s, t, x in S if strat(t, x) == k and s > cut]
            sm = [t for s, t, x in S if strat(t, x) == k and s <= cut]
            a, c = sum(g in t for t in lg), sum(g in t for t in sm)
            tabs.append([[a, len(lg) - a], [c, len(sm) - c]])
        orr, p = mantel_haenszel(tabs)
        right = (orr > 1) == (g in LARGE) and p < 0.05
        ok += right
        lines.append('%s %.2f (p %.3f)' % (g, orr, p))
    return ok, lines


def main():
    rd = R.Round('Four-hundred-and-thirtieth registered predictions: goal loop 76, audit of the size signs', 'predict_test430')
    band = lambda t: min(max(len(t), 2), 7)
    ok1, l1 = count(seals(31), lambda t, x: (band(t), x))
    rd.rec('SZA1', '4+ of 7 size signs keep their direction (p < 0.05) with length x site strata', ['%d of 7' % ok1, '; '.join(l1)], ok1 >= 4)
    ok2, l2 = count(seals(32), lambda t, x: band(t))
    rd.rec('SZA2', '4+ of 7 with size measured by the second dimension (field 32), length strata', ['%d of 7' % ok2, '; '.join(l2)], ok2 >= 4)
    rd.rec('P', 'progress rule: none (audit of set 379)', 'SZA1 %s, SZA2 %s' % (ok1 >= 4, ok2 >= 4), False)
    rd.finish()


if __name__ == '__main__':
    main()
