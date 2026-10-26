"""Set 405 (goal run loop 51): what chooses the heading variant (817 / 820 / 861): object kind; seal size.
Writes results/predict_test405.md."""
from collections import Counter
from statistics import median

import loopkit as L
import rtools as R
from predict_test388 import objects
from scipy.stats import chi2_contingency

HEAD = ('817', '820', '861')


def table(lines, lab, cats):
    c = {k: Counter() for k in cats}
    for t in lines:
        k = lab(t)
        if k in c and t and t[0] in HEAD:
            c[k][t[0]] += 1
    return [[c[k][h] for h in HEAD] for k in cats]


def main():
    rd = R.Round('Four-hundred-and-fifth registered predictions: goal loop 51, the heading variant', 'predict_test405')
    _, (tr, te) = L.splits_c()
    kind = lambda t: {'SEAL': 'seal', 'TAB': 'tablet'}.get(L.META.get(t, ('', '', ''))[1])
    ta, tb = table(tr, kind, ('seal', 'tablet')), table(te, kind, ('seal', 'tablet'))
    pa = chi2_contingency([r for r in ta if sum(r)])[1] if all(sum(r) for r in ta) else 1
    share = lambda tab, k, h: tab[k][h] / max(1, sum(tab[k]))
    dirs = [share(ta, 0, j) > share(ta, 1, j) for j in range(3)]
    same = sum((share(tb, 0, j) > share(tb, 1, j)) == d for j, d in enumerate(dirs))
    rd.say('- C-train seal %s, tablet %s (817/820/861); C-test seal %s, tablet %s.' % (ta[0], ta[1], tb[0], tb[1]))
    ok1 = pa < 0.05 and same == 3
    rd.rec('HV1', 'seals and tablets choose different heading variants (C-train p < 0.05, all three directions on C-test)', 'p = %.4f, %d of 3 directions' % (pa, same), ok1)
    sq = objects('SEAL:S')
    cut = median(s for s, t in sq)
    tab = [[sum(1 for s, t in sq if (s > cut) == big and t[0] == h) for h in HEAD] for big in (True, False)]
    p2 = chi2_contingency(tab)[1] if all(sum(r) for r in tab) else 1
    rd.rec('HV2', 'large and small square seals choose different heading variants', 'large %s, small %s, p = %.4f' % (tab[0], tab[1], p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'HV1 %s, HV2 %s' % (ok1, p2 < 0.05), ok1 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
