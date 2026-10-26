"""Set 460 (goal run loop 106): audit of set 459 TZ2 with text length held. Writes results/predict_test460.md."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-sixtieth registered predictions: goal loop 106, audit of the small count tablets', 'predict_test460')
    A, B, rowsA, recs, F = R.load_all()
    tb = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('TAB:B') and r['flat']:
            try:
                s = float(rec[31])
            except (TypeError, ValueError):
                continue
            if s > 0:
                tb.append((s, tuple(r['flat']), r['site']))
    cut = median(s for s, t, x in tb)
    band = lambda t: min(max(len(t), 2), 6)

    def mh(rows):
        tabs = []
        for b in sorted({band(t) for s, t, x in rows}):
            a = [s <= cut for s, t, x in rows if band(t) == b and '700' in t]
            c = [s <= cut for s, t, x in rows if band(t) == b and '700' not in t]
            tabs.append([[sum(a), len(a) - sum(a)], [sum(c), len(c) - sum(c)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(tb)
    rd.rec('TA1', 'moulded tablets with 700 are small more often within length bands', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh([r for r in tb if r[2] == 'Harappa'])
    rd.rec('TA2', 'the same within Harappa', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: none (audit of set 459)', 'TA1 %s, TA2 %s' % (o1 > 1 and p1 < 0.05, o2 > 1 and p2 < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
