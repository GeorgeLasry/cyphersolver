"""Set 394 (goal run loop 40): the Wells 1998 -> ICIT concordance by object intersection (wells_concordance.py).
Writes results/predict_test394.md."""
import random
from collections import Counter

import rtools as R
import wells_concordance as W


def main():
    rnd = random.Random(394)
    rd = R.Round('Three-hundred-and-ninety-fourth registered predictions: goal loop 40, a Wells -> ICIT concordance', 'predict_test394')
    con = W.concordance()
    good = sum(1 for v in con.values() if v[1] >= 0.8)
    rd.say('- %d Wells signs with 3+ listed objects found in the ICIT; top glyph on 80%%+ of objects for %d.' % (len(con), good))
    m77 = {r[0]: r[1] for r in (l.rstrip('\n').split('\t') for l in open('data/icit_m77_map.tsv', encoding='utf-8')) if len(r) > 1}
    for w, m in (('247', '400'), ('303', '347')):
        if w in con:
            g = con[w][0]
            rd.say('- printed check: Wells %s = M77 %s; matched ICIT %s (its M77: %s).' % (w, m, g, m77.get(g, '?')))
    rd.say()
    rd.rec('WC1', 'one ICIT glyph covers 80%+ of the objects for 70%+ of Wells signs', '%d of %d' % (good, len(con)), good >= 0.7 * len(con))
    by = W.icit_by_cisi()
    pool = sorted(by)
    obs = sum(v[1] for v in con.values()) / len(con)
    ge = 0
    for _ in range(1000):
        tot = 0
        for g, share, n, m in con.values():
            found = [by[o] for o in rnd.sample(pool, n)]
            tot += Counter(x for s in found for x in s).most_common(1)[0][1] / n
        ge += tot / len(con) >= obs
    p = (ge + 1) / 1001
    rd.rec('WC2', 'top-glyph purity beats random object lists of the same size', 'mean share %.2f, random as high in %d of 1000, p = %.4f' % (obs, ge, p), p < 0.05)
    rd.rec('P', 'progress rule: none (infrastructure for the Wells tests)', 'WC1 %s, WC2 %s' % (good >= 0.7 * len(con), p < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
