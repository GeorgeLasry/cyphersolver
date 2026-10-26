"""Set 448 (goal run loop 94): which fish take the long form; 705 against 706 by fish. A -> B. Writes results/predict_test448.md."""
from collections import Counter

import rtools as R
from scipy.stats import fisher_exact
from signs import load

FISH = lambda g: g.isdigit() and 220 <= int(g) <= 249


def forms(L):
    out = []
    for t in L:
        for i in range(1, len(t) - 2):
            if t[i] in ('705', '706') and t[i + 1] == '33' and t[i + 2] == '520' and FISH(t[i - 1]):
                out.append((t[i - 1], 'long', t[i]))
        for i in range(1, len(t)):
            if t[i] == '520' and FISH(t[i - 1]):
                out.append((t[i - 1], 'short', None))
    return out


def main():
    rd = R.Round('Four-hundred-and-forty-eighth registered predictions: goal loop 94, which fish take the long form', 'predict_test448')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    fa, fb = forms(DA), forms(DB)

    def skews(F, key, a, b):
        c = {a: Counter(), b: Counter()}
        for f, k, u in F:
            v = key(k, u)
            if v in c:
                c[v][f] += 1
        return c
    res = []
    for title, key, a, b in (('long against short form', lambda k, u: k, 'long', 'short'), ('706 against 705 in the long form', lambda k, u: u, '706', '705')):
        ca, cb = skews(fa, key, a, b), skews(fb, key, a, b)
        na, nb = {k: max(1, sum(v.values())) for k, v in ca.items()}, {k: max(1, sum(v.values())) for k, v in cb.items()}
        sk = {}
        for g in set(ca[a]) | set(ca[b]):
            x, y = ca[a][g], ca[b][g]
            if x + y >= 5 and fisher_exact([[x, na[a] - x], [y, na[b] - y]])[1] < 0.05:
                sk[g] = x / na[a] > y / na[b]
        rep = [(g, d) for g, d in sk.items() if cb[a][g] + cb[b][g] >= 3]
        same = sum((cb[a][g] / nb[a] > cb[b][g] / nb[b]) == d for g, d in rep)
        rd.say('- %s: skewed on A %s; %d of %d lean the same way on B.' % (title, dict(sk), same, len(rep)))
        res.append(bool(rep) and same == len(rep) and len(rep) >= 2)
    rd.say()
    rd.rec('WF1', 'fish skewed between long and short form on A all lean the same way on B (2+ testable)', str(res[0]), res[0])
    rd.rec('WF2', 'fish skewed between 706 and 705 on A all lean the same way on B (2+ testable)', str(res[1]), res[1])
    rd.rec('P', 'progress rule: either holds', 'WF1 %s, WF2 %s' % tuple(res), any(res))
    rd.finish()


if __name__ == '__main__':
    main()
