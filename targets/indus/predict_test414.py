"""Set 414 (goal run loop 60): seal size, name-body length and fish signs (square seals, clean ICIT, with a size).
Writes results/predict_test414.md."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test388 import objects


def body_len(t):
    for i in range(len(t) - 1, 0, -1):
        if t[i] in R.END:
            k = 0
            j = i - 1
            while j >= 0 and t[j] not in R.NUMS and t[j] not in ('817', '820', '861') and t[j] not in R.END:
                k += 1
                j -= 1
            return k
    return None


def main():
    rd = R.Round('Four-hundred-and-fourteenth registered predictions: goal loop 60, seal size, name length and fish signs', 'predict_test414')
    sq = objects('SEAL:S')
    cut = median(s for s, t in sq)
    band = lambda t: min(max(len(t), 2), 7)

    def mh(feat, keep=lambda t: True):
        tabs = []
        for b in sorted({band(t) for s, t in sq}):
            a_ = [feat(t) for s, t in sq if band(t) == b and s > cut and keep(t)]
            c_ = [feat(t) for s, t in sq if band(t) == b and s <= cut and keep(t)]
            tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda t: body_len(t) >= 3, keep=lambda t: body_len(t) is not None)
    rd.rec('SB1', 'large seals carry 3+ sign name bodies more often at equal length', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh(lambda t: any(g.isdigit() and 220 <= int(g) <= 249 for g in t))
    rd.rec('SB2', 'large seals carry a fish-family sign (220-249) more often at equal length', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'SB1 %s, SB2 %s' % (o1 > 1 and p1 < 0.05, o2 > 1 and p2 < 0.05), (o1 > 1 and p1 < 0.05) or (o2 > 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
