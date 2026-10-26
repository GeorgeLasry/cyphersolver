"""Set 464 (goal run loop 110): lines with both endings: does 740 come before 520? A and B. Writes results/predict_test464.md."""
import rtools as R
from scipy.stats import binomtest
from signs import load


def main():
    rd = R.Round('Four-hundred-and-sixty-fourth registered predictions: goal loop 110, the order of the two endings', 'predict_test464')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    out = []
    for L in (DA, DB):
        first = []
        for t in L:
            if '740' in t and '520' in t:
                first.append(t.index('740') < t.index('520'))
        k, n = sum(first), len(first)
        out.append((k, n, binomtest(k, n, 0.5, alternative='greater').pvalue if n else 1))
    rd.rec('EO1', 'in lines with both endings, 740 comes first in most, A', '%d of %d, p = %.4f' % out[0], out[0][2] < 0.05)
    rd.rec('EO2', 'the same on B', '%d of %d, p = %.4f' % out[1], out[1][2] < 0.05)
    rd.rec('P', 'progress rule: both hold', 'EO1 %s, EO2 %s' % (out[0][2] < 0.05, out[1][2] < 0.05), all(o[2] < 0.05 for o in out))
    rd.finish()


if __name__ == '__main__':
    main()
