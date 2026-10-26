"""Set 500 (goal run loop 146): which small-seal sign (156 / 400 / 590): by city, by animal. Writes results/predict_test500.md."""
from collections import Counter

import auditkit
import rtools as R
from scipy.stats import chi2_contingency


def main():
    rd = R.Round('Five-hundredth registered predictions: goal loop 146, the choice among the small-seal signs', 'predict_test500')
    rows = auditkit.rows()
    pick = lambda t: next((g for g in ('156', '400', '590') if g in t), None)
    tab_site = [[sum(1 for t, u, x, s in rows if x == site and pick(t) == g) for g in ('156', '400', '590')] for site in ('Mohenjo-daro', 'Harappa')]
    p1 = chi2_contingency(tab_site)[1] if all(sum(r) for r in tab_site) and all(sum(c) for c in zip(*tab_site)) else 1
    rd.rec('CH1', 'the choice differs between Mohenjo-daro and Harappa', '%s, p = %.4f' % (tab_site, p1), p1 < 0.05)
    tab_m = [[sum(1 for t, u, x, s in rows if u == uu and pick(t) == g) for g in ('156', '400', '590')] for uu in (True, False)]
    p2 = chi2_contingency(tab_m)[1] if all(sum(r) for r in tab_m) and all(sum(c) for c in zip(*tab_m)) else 1
    rd.rec('CH2', 'the choice differs between unicorn and other-animal seals', '%s, p = %.4f' % (tab_m, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'CH1 %s, CH2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
