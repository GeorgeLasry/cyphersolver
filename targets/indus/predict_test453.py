"""Set 453 (goal run loop 99): marked fish and the long form; modifiers before the fish. A and B.
Writes results/predict_test453.md."""
import rtools as R
from predict_test448 import FISH
from scipy.stats import fisher_exact, mannwhitneyu
from signs import load


def names(L):
    out = []
    for t in L:
        for i in range(1, len(t)):
            if FISH(t[i - 1]) and (t[i] == '520' or (i < len(t) - 2 and t[i] in ('705', '706') and t[i + 1] == '33' and t[i + 2] == '520')):
                k, j = 0, i - 2
                while j >= 0 and t[j] not in R.NUMS and t[j] not in R.END and t[j] not in ('817', '820', '861'):
                    k += 1
                    j -= 1
                out.append((t[i - 1], t[i] != '520', k))
    return out


def main():
    rd = R.Round('Four-hundred-and-fifty-third registered predictions: goal loop 99, marked fish and the long form', 'predict_test453')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    r1, r2 = [], []
    for L in (DA, DB):
        N = names(L)
        a = sum(1 for f, l, k in N if f != '220' and l)
        na = sum(1 for f, l, k in N if f != '220')
        c = sum(1 for f, l, k in N if f == '220' and l)
        nc = sum(1 for f, l, k in N if f == '220')
        r1.append((a, na, c, nc, fisher_exact([[a, na - a], [c, nc - c]], alternative='greater')[1]))
        lo = [k for f, l, k in N if l]
        sh = [k for f, l, k in N if not l]
        r2.append((sum(lo) / max(1, len(lo)), sum(sh) / max(1, len(sh)), mannwhitneyu(lo, sh, alternative='greater').pvalue if lo and sh else 1))
    ok1 = all(r[4] < 0.05 for r in r1)
    ok2 = all(r[2] < 0.05 for r in r2)
    rd.rec('MF1', 'marked fish take the long form more often than plain 220, A and B', ['%d of %d against %d of %d, p = %.4f' % r for r in r1], ok1)
    rd.rec('MF2', 'long-form names carry more modifiers before the fish, A and B', ['mean %.2f against %.2f, p = %.4f' % r for r in r2], ok2)
    rd.rec('P', 'progress rule: either holds', 'MF1 %s, MF2 %s' % (ok1, ok2), ok1 or ok2)
    rd.finish()


if __name__ == '__main__':
    main()
