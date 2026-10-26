"""Set 383 (goal run loop 29): what the repeated square-seal texts are. Writes results/predict_test383.md."""
from collections import Counter

import rtools as R
from predict_test379 import mantel_haenszel
from scipy.stats import fisher_exact


def main():
    rd = R.Round('Three-hundred-and-eighty-third registered predictions: goal loop 29, what the repeated texts are', 'predict_test383')
    A, B, rowsA, recs, F = R.load_all()
    texts = [tuple(r['flat']) for r in F if recs.get(r['sealid']) and str(recs[r['sealid']][20]).startswith('SEAL:S') and r['flat']]
    cnt = Counter(texts)
    two = sorted({t for t in cnt if len(t) == 2})
    rep = [any(g in R.NUMS for g in t) for t in two if cnt[t] > 1]
    one = [any(g in R.NUMS for g in t) for t in two if cnt[t] == 1]
    o, p = fisher_exact([[sum(rep), len(rep) - sum(rep)], [sum(one), len(one) - sum(one)]], alternative='greater')
    rd.rec('TW1', 'repeated two-sign texts contain a numeral more often', 'repeated %d of %d, unique %d of %d, p = %.4f' % (sum(rep), len(rep), sum(one), len(one), p), p < 0.05)
    band = lambda t: min(max(len(t), 2), 7)
    ends = lambda t: any(g in R.END for g in t[-2:])
    tabs = []
    for b in sorted({band(t) for t in cnt}):
        rp = [ends(t) for t in cnt if band(t) == b and cnt[t] > 1]
        un = [ends(t) for t in cnt if band(t) == b and cnt[t] == 1]
        tabs.append([[sum(rp), len(rp) - sum(rp)], [sum(un), len(un) - sum(un)]])
    orr, p2 = mantel_haenszel(tabs)
    rd.rec('TW2', 'repeated texts end in 740/520 less often at equal length', 'odds ratio repeated/unique %.2f, p = %.4f' % (orr, p2), orr < 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'TW1 %s, TW2 %s' % (p < 0.05, orr < 1 and p2 < 0.05), p < 0.05 or (orr < 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
