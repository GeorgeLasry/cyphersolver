"""Set 457 (goal run loop 103): fish share before the formula against before plain 520. A and B. Writes results/predict_test457.md."""
import rtools as R
from predict_test448 import FISH
from scipy.stats import fisher_exact
from signs import load


def main():
    rd = R.Round('Four-hundred-and-fifty-seventh registered predictions: goal loop 103, the formula against plain 520', 'predict_test457')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    out = []
    for L in (DA, DB):
        pf = [t[i - 1] for t in L for i in range(1, len(t) - 1) if t[i] in ('705', '706') and t[i + 1] == '33']
        p5 = [t[i - 1] for t in L for i in range(1, len(t)) if t[i] == '520' and not (i >= 2 and t[i - 1] == '33')]
        a, n = sum(FISH(g) for g in pf), len(pf)
        c, m = sum(FISH(g) for g in p5), len(p5)
        out.append((a, n, c, m, fisher_exact([[a, n - a], [c, m - c]])[1]))
    for k, (name, r) in enumerate(zip('AB', out)):
        rd.rec('FX%d' % (k + 1), 'fish share before the formula differs from before plain 520 (two-sided), %s' % name, '%d of %d against %d of %d, p = %.4f' % r, r[4] < 0.05)
    rd.rec('P', 'progress rule: both hold (the formula selects a different name class from plain 520)', '', all(r[4] < 0.05 for r in out))
    rd.finish()


if __name__ == '__main__':
    main()
