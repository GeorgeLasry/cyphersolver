"""Set 495 (goal run loop 141): rare signs and unique texts on other-animal seals (length x site x size strata).
Writes results/predict_test495.md."""
from collections import Counter
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-ninety-fifth registered predictions: goal loop 141, rare signs on other-animal seals', 'predict_test495')
    A, B, rowsA, recs, F = R.load_all()
    sign_cnt = Counter(g for r in F for g in r['flat'])
    rows = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL:S') and r['flat']:
            m = str(rec[18]).split(':')[0]
            try:
                sz = float(rec[31])
            except (TypeError, ValueError):
                sz = 0
            if m not in ('', '-', 'None') and sz > 0:
                rows.append((tuple(r['flat']), m != 'Bull1', r['site'], sz))
    txt = Counter(t for t, o, x, s in rows)
    cut = median(s for t, o, x, s in rows)
    band = lambda t: min(max(len(t), 2), 7)

    def mh(feat):
        tabs = []
        for k in sorted({(band(t), x, s > cut) for t, o, x, s in rows}):
            a = [feat(t) for t, o, x, s in rows if (band(t), x, s > cut) == k and o]
            c = [feat(t) for t, o, x, s in rows if (band(t), x, s > cut) == k and not o]
            tabs.append([[sum(a), len(a) - sum(a)], [sum(c), len(c) - sum(c)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda t: any(sign_cnt[g] <= 2 for g in t))
    rd.rec('OR1', 'other-animal seals carry rare signs more often', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh(lambda t: txt[t] == 1)
    rd.rec('OR2', 'other-animal seal texts are unique more often', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: OR1 (OR2 is the converse of set 493)', 'OR1 %s, OR2 %s' % (o1 > 1 and p1 < 0.05, o2 > 1 and p2 < 0.05), o1 > 1 and p1 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
