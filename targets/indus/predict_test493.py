"""Set 493 (goal run loop 139): unicorn seals: repeated texts and doubled signs (length x site strata).
Writes results/predict_test493.md."""
from collections import Counter

import rtools as R
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-ninety-third registered predictions: goal loop 139, unicorn seals: repeats and doubles', 'predict_test493')
    A, B, rowsA, recs, F = R.load_all()
    rows = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL:S') and r['flat']:
            m = str(rec[18]).split(':')[0]
            if m not in ('', '-', 'None'):
                rows.append((tuple(r['flat']), m == 'Bull1', r['site']))
    cnt = Counter(t for t, u, x in rows)
    band = lambda t: min(max(len(t), 2), 7)

    def mh(feat):
        tabs = []
        for k in sorted({(band(t), x) for t, u, x in rows}):
            a = [feat(t) for t, u, x in rows if (band(t), x) == k and u]
            c = [feat(t) for t, u, x in rows if (band(t), x) == k and not u]
            tabs.append([[sum(a), len(a) - sum(a)], [sum(c), len(c) - sum(c)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda t: cnt[t] > 1)
    rd.rec('UR1', 'unicorn-seal texts recur more often (length x site)', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh(lambda t: any(t[i] == t[i + 1] and t[i] not in R.NUMS for i in range(len(t) - 1)))
    rd.rec('UR2', 'unicorn seals carry doubled signs more often (length x site)', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'UR1 %s, UR2 %s' % (o1 > 1 and p1 < 0.05, o2 > 1 and p2 < 0.05), (o1 > 1 and p1 < 0.05) or (o2 > 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
