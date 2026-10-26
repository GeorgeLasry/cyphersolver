"""Session-2 loop 3: sign pairs written in both orders (free order) on A and B."""
from collections import Counter

import s2kit as K
from scipy.stats import binomtest

TITLE = 'pairs written in both orders'
REG = '''Adjacent sign pairs (a b) and (b a) both attested on A (3+ distinct lines each) are 'free-order' pairs; pairs with
one order only (6+ lines, 0 the other way) are 'fixed' (`hyp_s2_order.py`).

- **OR1** Free-order pairs on A with 2+ B lines in total are attested in both orders on B more often than fixed pairs
  are (Fisher-like comparison by binomial against the fixed pairs' rate).
- **OR2** Free-order pairs are mostly numerals or markers (R.NUMS, 400, 90): the reversals are counts, not words; 60%+.
- Progress rule: OR1 and OR2 both hold (a replicated finding about word order).'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    import rtools as R
    DA, DB = K.ab()

    def pairs(S):
        c = Counter()
        for t in S:
            for x in set(zip(t, t[1:])):
                c[x] += 1
        return c
    ca, cb = pairs(DA), pairs(DB)
    free = {tuple(sorted((a, b))) for (a, b) in ca if a != b and ca[(a, b)] >= 3 and ca[(b, a)] >= 3}
    fixed = {(a, b) for (a, b) in ca if a != b and ca[(a, b)] >= 6 and ca[(b, a)] == 0}
    fb = [(a, b) for a, b in free if cb[(a, b)] + cb[(b, a)] >= 2]
    xb = [(a, b) for a, b in fixed if cb[(a, b)] + cb[(b, a)] >= 2]
    f_both = sum(cb[(a, b)] > 0 and cb[(b, a)] > 0 for a, b in fb)
    x_both = sum(cb[(a, b)] > 0 and cb[(b, a)] > 0 for a, b in xb)
    base = x_both / max(1, len(xb))
    p = binomtest(f_both, len(fb), max(base, 0.01), alternative='greater').pvalue if fb else 1
    ok1 = bool(fb) and f_both / len(fb) > base and p < 0.05
    rd.rec('OR1', 'free-order pairs stay free on B', 'free %d of %d both orders on B; fixed %d of %d; p = %.4f' % (f_both, len(fb), x_both, len(xb), p), ok1)
    gram = set(R.NUMS) | {'400', '90'}
    g = sum(a in gram or b in gram for a, b in free)
    ok2 = bool(free) and g / len(free) >= 0.6
    rd.rec('OR2', 'free-order pairs involve numerals or markers', '%d of %d; pairs %s' % (g, len(free), ' '.join('%s/%s' % x for x in sorted(free))), ok2)
    SUMMARY = 'free pairs both orders on B %d/%d vs fixed %d/%d; numeral/marker share %d/%d.' % (f_both, len(fb), x_both, len(xb), g, len(free))
    return ok1 and ok2
