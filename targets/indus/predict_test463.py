"""Set 463 (goal run loop 109): does the long fish-name form end the line more than the short form? A and B.
Writes results/predict_test463.md."""
import rtools as R
from predict_test448 import FISH
from scipy.stats import fisher_exact
from signs import load


def main():
    rd = R.Round('Four-hundred-and-sixty-third registered predictions: goal loop 109, the long form at the line end', 'predict_test463')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    fin = lambda t, j: all(g in ('400', '90') for g in t[j + 1:])
    out = []
    for L in (DA, DB):
        lo, sh = [], []
        for t in L:
            for i in range(1, len(t)):
                if FISH(t[i - 1]):
                    if i < len(t) - 2 and t[i] in ('705', '706') and t[i + 1] == '33' and t[i + 2] == '520':
                        lo.append(fin(t, i + 2))
                    elif t[i] == '520':
                        sh.append(fin(t, i))
        out.append((sum(lo), len(lo), sum(sh), len(sh), fisher_exact([[sum(lo), len(lo) - sum(lo)], [sum(sh), len(sh) - sum(sh)]], alternative='greater')[1]))
    rd.rec('FE1', 'the long form ends the line more often than the short form, A', '%d of %d against %d of %d, p = %.4f' % out[0], out[0][4] < 0.05)
    rd.rec('FE2', 'the same on B', '%d of %d against %d of %d, p = %.4f' % out[1], out[1][4] < 0.05)
    rd.rec('P', 'progress rule: both hold', 'FE1 %s, FE2 %s' % (out[0][4] < 0.05, out[1][4] < 0.05), all(o[4] < 0.05 for o in out))
    rd.finish()


if __name__ == '__main__':
    main()
