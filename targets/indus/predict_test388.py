"""Set 388 (goal run loop 34): seal size and multiple endings; size signs on rectangular seals. Writes results/predict_test388.md."""
from statistics import median

import rtools as R
from predict_test379 import LARGE, SMALL, mantel_haenszel


def objects(prefix):
    A, B, rowsA, recs, F = R.load_all()
    out = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith(prefix) and r['flat']:
            try:
                sz = float(rec[31])
            except (TypeError, ValueError):
                continue
            if sz > 0:
                out.append((sz, tuple(r['flat'])))
    return out


def main():
    rd = R.Round('Three-hundred-and-eighty-eighth registered predictions: goal loop 34, seal size: endings, rectangular seals', 'predict_test388')
    sq = objects('SEAL:S')
    cut = median(s for s, t in sq)
    band = lambda t: min(max(len(t), 2), 7)
    two = lambda t: sum(g in R.END for g in t) >= 2
    tabs = []
    for b in sorted({band(t) for s, t in sq}):
        lg = [two(t) for s, t in sq if band(t) == b and s > cut]
        sm = [two(t) for s, t in sq if band(t) == b and s <= cut]
        tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
    orr, p = mantel_haenszel(tabs)
    rd.rec('LG1', 'large square seals carry two endings more often at equal length', 'odds ratio %.2f, p = %.4f' % (orr, p), orr > 1 and p < 0.05)
    rc = objects('SEAL:R')
    c2 = median(s for s, t in rc)
    same = 0
    for g in LARGE + SMALL:
        lg = [t for s, t in rc if s > c2]
        sm = [t for s, t in rc if s <= c2]
        d = sum(g in t for t in lg) / max(1, len(lg)) - sum(g in t for t in sm) / max(1, len(sm))
        same += (d > 0) == (g in LARGE)
    rd.rec('LG2', 'the size signs lean the same way on rectangular seals (5+ of 7)', '%d of 7 (%d seals)' % (same, len(rc)), same >= 5)
    rd.rec('P', 'progress rule: either holds', 'LG1 %s, LG2 %s' % (orr > 1 and p < 0.05, same >= 5), (orr > 1 and p < 0.05) or same >= 5)
    rd.finish()


if __name__ == '__main__':
    main()
