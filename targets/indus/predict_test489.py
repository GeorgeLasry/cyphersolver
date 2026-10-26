"""Set 489 (goal run loop 135): set 488's rare-sign finding on two random halves. Writes results/predict_test489.md."""
import hashlib
from collections import Counter
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test430 import seals


def main():
    rd = R.Round('Four-hundred-and-eighty-ninth registered predictions: goal loop 135, rare signs on two halves', 'predict_test489')
    A, B, rowsA, recs, F = R.load_all()
    cnt = Counter(g for r in F for g in r['flat'])
    sq = seals(31)
    cut = median(s for s, t, x in sq)
    band = lambda t: min(max(len(t), 2), 7)
    rare = lambda t: any(cnt[g] <= 2 for g in t)
    half = lambda t, s: int(hashlib.md5(('%s%.2f' % (' '.join(t), s)).encode()).hexdigest(), 16) % 2
    res = []
    for h in (0, 1):
        rows = [(s, t, x) for s, t, x in sq if half(t, s) == h]
        tabs = []
        for k in sorted({(band(t), x) for s, t, x in rows}):
            lg = [rare(t) for s, t, x in rows if (band(t), x) == k and s > cut]
            sm = [rare(t) for s, t, x in rows if (band(t), x) == k and s <= cut]
            tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
        res.append(mantel_haenszel(tabs))
    rd.rec('RH1', 'rare signs on large seals in half 1', 'odds ratio %.2f, p = %.4f' % res[0], res[0][0] > 1 and res[0][1] < 0.05)
    rd.rec('RH2', 'rare signs on large seals in half 2', 'odds ratio %.2f, p = %.4f' % res[1], res[1][0] > 1 and res[1][1] < 0.05)
    rd.rec('P', 'progress rule: none (replication of set 488)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
