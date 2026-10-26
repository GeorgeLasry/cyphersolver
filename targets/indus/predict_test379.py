"""Set 379 (goal run loop 25): are set 378's size signs a text-length or site effect? Writes results/predict_test379.md."""
from statistics import median

import loopkit as L
import rtools as R
from predict_test376 import size
from scipy.stats import chi2


def mantel_haenszel(tabs):
    """Pooled odds ratio and the CMH chi-square test (1 df, continuity-corrected) over 2x2 tables."""
    num = den = a_sum = e_sum = v_sum = 0.0
    for (a, b), (c, d) in tabs:
        n = a + b + c + d
        if n <= 1:
            continue
        num += a * d / n
        den += b * c / n
        a_sum += a
        e_sum += (a + b) * (a + c) / n
        v_sum += (a + b) * (c + d) * (a + c) * (b + d) / (n * n * (n - 1))
    stat = (abs(a_sum - e_sum) - 0.5) ** 2 / v_sum if v_sum else 0.0
    return (num / den if den else float('inf')), chi2.sf(stat, 1)

LARGE, SMALL = ('32', '706'), ('156', '390', '400', '5', '590')


def main():
    rd = R.Round('Three-hundred-and-seventy-ninth registered predictions: goal loop 25, size signs against length and site', 'predict_test379')
    (tr, te), (DA, DB) = L.splits()
    S = [t for t in sorted(set(tr) | set(te)) if L.SUBTYPE.get(t) == 'SEAL:S' and size(t)]
    cut = median(size(t) for t in S)
    band = lambda t: min(max(len(t), 2), 7)
    ok_len = 0
    for g in LARGE + SMALL:
        tabs = []
        for b in sorted({band(t) for t in S}):
            sub = [t for t in S if band(t) == b]
            lg = [t for t in sub if size(t) > cut]
            sm = [t for t in sub if size(t) <= cut]
            a, c = sum(g in t for t in lg), sum(g in t for t in sm)
            tabs.append([[a, len(lg) - a], [c, len(sm) - c]])
        orr, p = mantel_haenszel(tabs)
        right = (orr > 1) == (g in LARGE) and p < 0.05
        ok_len += right
        rd.say('- %s (%s): pooled odds ratio large/small %.2f within length bands, p = %.4f%s.' % (g, 'large' if g in LARGE else 'small', orr, p, ' *' if right else ''))
    rd.say()
    rd.rec('LZ1', 'the size signs hold within length bands (4+ of 7 right way, p < 0.05)', '%d of 7' % ok_len, ok_len >= 4)
    md = [t for t in S if L.META.get(t, ('', '', ''))[0] == 'Mohenjo-daro']
    c2 = median(size(t) for t in md)
    same = 0
    for g in LARGE + SMALL:
        lg = [t for t in md if size(t) > c2]
        sm = [t for t in md if size(t) <= c2]
        d = sum(g in t for t in lg) / len(lg) - sum(g in t for t in sm) / len(sm)
        same += (d > 0) == (g in LARGE)
    rd.rec('LZ2', 'within Mohenjo-daro, 5+ of 7 signs lean the same way', '%d of 7 (%d seals)' % (same, len(md)), same >= 5)
    rd.rec('P', 'progress rule: LZ1', 'LZ1 %s' % (ok_len >= 4), ok_len >= 4)
    rd.finish()


if __name__ == '__main__':
    main()
