"""Set 452 (goal run loop 98): numeral + fish names and the long form. A and B. Writes results/predict_test452.md."""
import rtools as R
from predict_test448 import FISH, forms
from scipy.stats import fisher_exact
from signs import load


def main():
    rd = R.Round('Four-hundred-and-fifty-second registered predictions: goal loop 98, numeral + fish names and the long form', 'predict_test452')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    res = []
    for L in (DA, DB):
        rows = []
        for t in L:
            for i in range(1, len(t)):
                if FISH(t[i - 1]) and (t[i] == '520' or (i < len(t) - 2 and t[i] in ('705', '706') and t[i + 1] == '33' and t[i + 2] == '520')):
                    num = i >= 2 and t[i - 2] in R.NUMS
                    rows.append((num, t[i] != '520'))
        a = sum(1 for n, l in rows if n and l)
        na = sum(1 for n, l in rows if n)
        c = sum(1 for n, l in rows if not n and l)
        nc = sum(1 for n, l in rows if not n)
        p = fisher_exact([[a, na - a], [c, nc - c]], alternative='greater')[1]
        res.append((a, na, c, nc, p))
    ok = all(r[4] < 0.05 for r in res)
    rd.rec('NF1', 'numeral + fish names take the long form more often, A', '%d of %d against %d of %d, p = %.4f' % res[0], res[0][4] < 0.05)
    rd.rec('NF2', 'the same on B', '%d of %d against %d of %d, p = %.4f' % res[1], res[1][4] < 0.05)
    rd.rec('P', 'progress rule: NF1 and NF2 (replicated)', 'NF1 %s, NF2 %s' % (res[0][4] < 0.05, res[1][4] < 0.05), ok)
    rd.finish()


if __name__ == '__main__':
    main()
