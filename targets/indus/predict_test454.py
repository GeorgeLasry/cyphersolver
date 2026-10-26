"""Set 454 (goal run loop 100): the long fish-name form by seal kind and by city. Writes results/predict_test454.md."""
import loopkit as L
import rtools as R
from predict_test448 import FISH
from scipy.stats import fisher_exact


def tally(lines, keep):
    lo = sh = 0
    for t in lines:
        if not keep(t):
            continue
        for i in range(1, len(t)):
            if FISH(t[i - 1]):
                if t[i] == '520':
                    sh += 1
                elif i < len(t) - 2 and t[i] in ('705', '706') and t[i + 1] == '33' and t[i + 2] == '520':
                    lo += 1
    return lo, sh


def main():
    rd = R.Round('Four-hundred-and-fifty-fourth registered predictions: goal loop 100, the long form by seal kind and city', 'predict_test454')
    (tr, te), (DA, DB) = L.splits()
    lines = sorted(set(tr) | set(te) | set(DA))
    a = tally(lines, lambda t: L.SUBTYPE.get(t) == 'SEAL:S')
    b = tally(lines, lambda t: L.SUBTYPE.get(t) == 'SEAL:R')
    p1 = fisher_exact([[a[0], a[1]], [b[0], b[1]]], alternative='greater')[1]
    rd.rec('LK1', 'the long form is a larger share of fish names on square than on rectangular seals', 'square %d / %d, rectangular %d / %d (long / short), p = %.4f' % (a + b + (p1,)), p1 < 0.05)
    site = lambda t: L.META.get(t, ('', '', ''))[0]
    c = tally(lines, lambda t: site(t) == 'Mohenjo-daro')
    d = tally(lines, lambda t: site(t) == 'Harappa')
    p2 = fisher_exact([[c[0], c[1]], [d[0], d[1]]])[1]
    rd.rec('LK2', 'Mohenjo-daro and Harappa differ in the long-form share (two-sided)', 'MD %d / %d, H %d / %d, p = %.4f' % (c + d + (p2,)), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'LK1 %s, LK2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
