"""Set 470 (goal run loop 116): set 469's doubled-sign finding on two random halves of the seals. Writes results/predict_test470.md."""
import hashlib
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test430 import seals


def main():
    rd = R.Round('Four-hundred-and-seventieth registered predictions: goal loop 116, doubled signs on two halves', 'predict_test470')
    sq = seals(31)
    cut = median(s for s, t, x in sq)
    band = lambda t: min(max(len(t), 2), 7)
    dbl = lambda t: any(t[i] == t[i + 1] and t[i] not in R.NUMS for i in range(len(t) - 1))
    half = lambda t, s: int(hashlib.md5(('%s%.2f' % (' '.join(t), s)).encode()).hexdigest(), 16) % 2
    res = []
    for h in (0, 1):
        rows = [(s, t, x) for s, t, x in sq if half(t, s) == h]
        tabs = []
        for k in sorted({(band(t), x) for s, t, x in rows}):
            lg = [dbl(t) for s, t, x in rows if (band(t), x) == k and s > cut]
            sm = [dbl(t) for s, t, x in rows if (band(t), x) == k and s <= cut]
            tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
        res.append(mantel_haenszel(tabs))
    rd.rec('DH1', 'doubled signs on small seals in half 1', 'odds ratio %.2f, p = %.4f' % res[0], res[0][0] < 1 and res[0][1] < 0.05)
    rd.rec('DH2', 'doubled signs on small seals in half 2', 'odds ratio %.2f, p = %.4f' % res[1], res[1][0] < 1 and res[1][1] < 0.05)
    rd.rec('P', 'progress rule: none (replication of set 469)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
