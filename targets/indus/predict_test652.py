"""Set 652 (lead 2): do the small-number units behave like persons / objects (name heads when uncounted) and the
large-number units like commodities (never heads)? Writes results/predict_test652.md."""
import rtools as R
from leadkit import ab
from numerals import NUMS
from scipy.stats import fisher_exact

SMALL = {'176', '233', '235', '240', '61', '803', '806'}
LARGE = {'390', '405', '407', '575', '585', '900'}


def tab(L, fn):
    t2 = [[0, 0], [0, 0]]
    for t in L:
        for i, g in enumerate(t):
            if (g in SMALL or g in LARGE) and not (i and t[i - 1] in NUMS):
                t2[0 if g in SMALL else 1][0 if fn(t, i) else 1] += 1
    return t2


def main():
    rd = R.Round('Set 652 registered predictions: small-number units as heads, large-number units not', 'predict_test652')
    DA, DB = ab()
    head = lambda t, i: i + 1 < len(t) and t[i + 1] in R.END
    final = lambda t, i: all(g in ('400', '90') for g in t[i + 1:])
    oks = []
    for key, name, L in (('UH1', 'A', DA), ('UH2', 'B', DB)):
        a = tab(L, head)
        p = fisher_exact(a, alternative='greater')[1]
        rd.rec(key, 'uncounted small-number units take an ending more often than large-number units, %s' % name, 'small %d of %d, large %d of %d, p = %.4g' % (a[0][0], sum(a[0]), a[1][0], sum(a[1]), p), p < 0.05)
        oks.append(p < 0.05)
    out = []
    for name, L in (('A', DA), ('B', DB)):
        a = tab(L, final)
        p = fisher_exact(a, alternative='less')[1]
        out.append('%s: small %d of %d final, large %d of %d, p = %.4g' % (name, a[0][0], sum(a[0]), a[1][0], sum(a[1]), p))
        oks.append(p < 0.05)
    rd.rec('UH3', 'uncounted large-number units stand line-final (bare, no ending) more often than small ones, A and B', out, oks[2] and oks[3])
    rd.rec('P', 'progress rule: UH1 and UH2 (a replicated functional split: the small-number units are the kind of sign that names, the large-number units are not)', '', oks[0] and oks[1])
    rd.finish()


if __name__ == '__main__':
    main()
