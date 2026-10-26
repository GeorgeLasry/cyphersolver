"""Set 382 (goal run loop 28): the field motif read from ICIT record field 18 for every clean object. MO1 domain model
(split C); MO2 unicorn against other animals, sign skews on square seals (C-train -> C-test). loopkit.py."""
from collections import Counter

import loopkit as L
import rtools as R
from scipy.stats import binomtest, fisher_exact


def main():
    mot = {t: v.split(':')[0] for t, v in L.field(18).items()}
    L.run_domain_set_c(382, 'Three-hundred-and-eighty-second registered predictions: goal loop 28 (part 1), motif from field 18', [
        ('MO1', 'a motif domain model (field 18)', lambda t, m: mot.get(t, ''))])
    rd = R.Round('Three-hundred-and-eighty-second registered predictions: goal loop 28 (part 2), unicorn against other animals', 'predict_test3820')
    _, (tr, te) = L.splits_c()
    lab = lambda t: None if L.SUBTYPE.get(t) != 'SEAL:S' or mot.get(t) in (None, '', 'None') else ('unicorn' if mot[t] == 'Bull1' else 'other')

    def cnt(S):
        c = {'unicorn': Counter(), 'other': Counter()}
        for t in S:
            if lab(t):
                c[lab(t)].update(t)
        return c, {k: max(1, sum(v.values())) for k, v in c.items()}
    (ca, na), (cb, nb) = cnt(tr), cnt(te)
    sk = {}
    for g in set(ca['unicorn']) | set(ca['other']):
        x, y = ca['unicorn'][g], ca['other'][g]
        if x + y >= 10 and fisher_exact([[x, na['unicorn'] - x], [y, na['other'] - y]])[1] < 0.01:
            sk[g] = x / na['unicorn'] > y / na['other']
    rep = [(g, d) for g, d in sk.items() if cb['unicorn'][g] + cb['other'][g] >= 3]
    same = sum((cb['unicorn'][g] / nb['unicorn'] > cb['other'][g] / nb['other']) == d for g, d in rep)
    p = binomtest(same, len(rep), 0.5, alternative='greater').pvalue if rep else 1
    rd.say('- skewed: unicorn %s; other animals %s.' % (' '.join(sorted(g for g, d in sk.items() if d)), ' '.join(sorted(g for g, d in sk.items() if not d))))
    ok = bool(rep) and same / len(rep) >= 0.75 and p < 0.05
    rd.rec('MO2', 'unicorn / other-animal skews replicate on C-test', '%d of %d, p = %.4f' % (same, len(rep), p), ok)
    rd.finish()


if __name__ == '__main__':
    main()
