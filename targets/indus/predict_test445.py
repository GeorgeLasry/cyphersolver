"""Set 445 (goal run loop 91): what goes with the closing formula in a text. A and B. Writes results/predict_test445.md."""
import rtools as R
from predict_test379 import mantel_haenszel
from predict_test441 import has_formula
from signs import load

HEAD = {'817', '820', '861'}


def before(t):
    for i in range(len(t) - 1):
        if t[i] in ('705', '706') and t[i + 1] == '33':
            return t[:i]
    return t


def main():
    rd = R.Round('Four-hundred-and-forty-fifth registered predictions: goal loop 91, what goes with the closing formula', 'predict_test445')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    band = lambda t: min(max(len(t), 2), 8)
    r1, r2 = [], []
    for L in (DA, DB):
        for feat, out in ((lambda t: '740' in before(t), r1), (lambda t: t[0] in HEAD, r2)):
            tabs = []
            for b in sorted({band(t) for t in L}):
                x = [feat(t) for t in L if band(t) == b and has_formula(t)]
                y = [feat(t) for t in L if band(t) == b and not has_formula(t)]
                tabs.append([[sum(x), len(x) - sum(x)], [sum(y), len(y) - sum(y)]])
            out.append(mantel_haenszel(tabs))
    ok1 = all(o > 1 and p < 0.05 for o, p in r1)
    ok2 = all(o > 1 and p < 0.05 for o, p in r2)
    rd.rec('FN1', 'a 740 stands before the formula more often than in other texts of equal length, A and B', '; '.join('odds ratio %.2f, p = %.4f' % x for x in r1), ok1)
    rd.rec('FN2', 'formula texts open with the heading more often, A and B', '; '.join('odds ratio %.2f, p = %.4f' % x for x in r2), ok2)
    rd.rec('P', 'progress rule: either holds', 'FN1 %s, FN2 %s' % (ok1, ok2), ok1 or ok2)
    rd.finish()


if __name__ == '__main__':
    main()
