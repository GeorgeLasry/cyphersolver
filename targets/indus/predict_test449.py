"""Set 449 (goal run loop 95): the long fish-name form as a role in R; the long form on seals against tablets.
Writes results/predict_test449.md."""
import inspect

import loopkit as L
import progress as P
import rtools as R
from scipy.stats import fisher_exact

FISH = lambda g: g.isdigit() and 220 <= int(g) <= 249


def main():
    rd = R.Round('Four-hundred-and-forty-ninth registered predictions: goal loop 95, the long form in the roles', 'predict_test449')
    DL, tr, te = P.data()
    r0 = P.roles(DL, edges=True, head2=True)[0]
    src = inspect.getsource(P.roles).replace("            num_before = g in R.NUMS\n            tot += 1",
        "            if role is None and g in ('705', '706', '33') and LONG(t, i):\n                role = 'long-form closer'\n            num_before = g in R.NUMS\n            tot += 1")

    def LONG(t, i):
        for j in range(1, len(t) - 2):
            if t[j] in ('705', '706') and t[j + 1] == '33' and t[j + 2] == '520' and FISH(t[j - 1]) and i in (j, j + 1):
                return True
        return False
    ns = dict(P.__dict__)
    ns['LONG'] = LONG
    exec(src, ns)
    r1, by, tot = ns['roles'](DL, edges=True, head2=True)
    ok1 = r1 - r0 >= 0.003
    rd.rec('LR1', "a 'long-form closer' role raises R by 0.3 points or more", 'R %.2f%% -> %.2f%% (%d tokens)' % (100 * r0, 100 * r1, by['long-form closer']), ok1)
    (tr2, te2), _ = L.splits()
    lines = sorted(set(tr2) | set(te2))
    kind = lambda t: L.META.get(t, ('', '', ''))[1]
    def cnt(k):
        lo = sh = 0
        for t in lines:
            if kind(t) != k:
                continue
            for j in range(1, len(t)):
                if t[j] == '520' and FISH(t[j - 1]):
                    sh += 1
                if j < len(t) - 2 and t[j] in ('705', '706') and t[j + 1] == '33' and t[j + 2] == '520' and FISH(t[j - 1]):
                    lo += 1
        return lo, sh
    ls, ss = cnt('SEAL')
    lt, st = cnt('TAB')
    o, p = fisher_exact([[ls, ss], [lt, st]], alternative='greater')
    rd.rec('LR2', 'the long form is a larger share of fish names on seals than on tablets', 'seals %d long / %d short, tablets %d / %d, p = %.4f' % (ls, ss, lt, st, p), p < 0.05)
    rd.rec('P', 'progress rule: LR1 (the roles benchmark moves)', 'LR1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
