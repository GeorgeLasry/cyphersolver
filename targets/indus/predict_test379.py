"""Set 379 (goal run loop 25): are set 378's size signs a text-length or site effect? Writes results/predict_test379.md."""
from statistics import median

import loopkit as L
import rtools as R
from predict_test376 import size
from statsmodels.stats.contingency_tables import StratifiedTable

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
            tabs.append([[a + 0.5, len(lg) - a + 0.5], [c + 0.5, len(sm) - c + 0.5]])
        st = StratifiedTable(tabs)
        orr, p = st.oddsratio_pooled, st.test_null_odds().pvalue
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
