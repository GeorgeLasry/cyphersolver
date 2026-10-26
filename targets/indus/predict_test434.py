"""Set 434 (goal run loop 80): audit of set 433 (706 against 705) with length held and within Mohenjo-daro.
Writes results/predict_test434.md."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test430 import seals
from scipy.stats import mannwhitneyu


def main():
    rd = R.Round('Four-hundred-and-thirty-fourth registered predictions: goal loop 80, audit of the U-family sizes', 'predict_test434')
    sq = seals(31)
    cut = median(s for s, t, x in sq)
    band = lambda t: min(max(len(t), 2), 7)
    rows = [(s, t, x) for s, t, x in sq if '706' in t or ('705' in t and '706' not in t)]
    tabs = []
    for b in sorted({band(t) for s, t, x in rows}):
        a_ = [s > cut for s, t, x in rows if band(t) == b and '706' in t]
        c_ = [s > cut for s, t, x in rows if band(t) == b and '706' not in t]
        tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
    orr, p = mantel_haenszel(tabs)
    rd.rec('UA1', '706 seals are large more often than 705 seals within length bands', 'odds ratio %.2f, p = %.4f' % (orr, p), orr > 1 and p < 0.05)
    md = [r for r in rows if r[2] == 'Mohenjo-daro']
    a = [s for s, t, x in md if '706' in t]
    c = [s for s, t, x in md if '706' not in t]
    p2 = mannwhitneyu(a, c, alternative='greater').pvalue if a and c else 1
    rd.rec('UA2', 'within Mohenjo-daro 706 seals are larger than 705 seals', 'n %d / %d, p = %.4f' % (len(a), len(c), p2), p2 < 0.05)
    rd.rec('P', 'progress rule: none (audit of set 433)', 'UA1 %s, UA2 %s' % (orr > 1 and p < 0.05, p2 < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
