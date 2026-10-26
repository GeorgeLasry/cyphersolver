"""Set 514 (goal run loop 160): 692 on two random halves (motif, length, site strata). Writes results/predict_test514.md."""
import hashlib
from statistics import median

import auditkit
import rtools as R
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Five-hundred-and-fourteenth registered predictions: goal loop 160, 692 on two halves', 'predict_test514')
    rows = auditkit.rows()
    cut = median(s for t, u, x, s in rows)
    band = lambda t: min(max(len(t), 2), 7)
    half = lambda t, s: int(hashlib.md5(('%s%.2f' % (' '.join(t), s)).encode()).hexdigest(), 16) % 2
    res = []
    for h in (0, 1):
        R_ = [r for r in rows if half(r[0], r[3]) == h]
        tabs = []
        for k in sorted({(band(t), x, u) for t, u, x, s in R_}):
            lg = [('692' in t) for t, u, x, s in R_ if (band(t), x, u) == k and s > cut]
            sm = [('692' in t) for t, u, x, s in R_ if (band(t), x, u) == k and s <= cut]
            tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
        res.append(mantel_haenszel(tabs))
    rd.rec('H692a', '692 leans to large seals in half 1', 'odds ratio %.2f, p = %.4f' % res[0], res[0][0] > 1 and res[0][1] < 0.05)
    rd.rec('H692b', '692 leans to large seals in half 2', 'odds ratio %.2f, p = %.4f' % res[1], res[1][0] > 1 and res[1][1] < 0.05)
    rd.rec('P', 'progress rule: none (replication of a scan hit)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
