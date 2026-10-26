"""Set 366 (goal run loop 12): bound phrases as a role. Writes results/predict_test366.md."""
import inspect
from collections import Counter

import progress as P
import rtools as R


def bound(S, minlines=5, q=0.5):
    big = Counter()
    first, second = Counter(), Counter()
    for t in S:
        for a, b in set(zip(t, t[1:])):
            big[(a, b)] += 1
        for a in set(t[:-1]):
            first[a] += 1
        for b in set(t[1:]):
            second[b] += 1
    return {ab for ab, n in big.items() if n >= minlines and n / first[ab[0]] >= q and n / second[ab[1]] >= q}, big, first


def main():
    rd = R.Round('Three-hundred-and-sixty-sixth registered predictions: goal loop 12, bound phrases', 'predict_test366')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    from signs import load
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    ba, _, _ = bound(DA)
    _, bigB, firstB = bound(DB)
    rep = [ab for ab in ba if firstB[ab[0]] >= 3]
    kept = [ab for ab in rep if bigB[ab] / firstB[ab[0]] >= 0.5]
    rd.say('- %d bound pairs on A (5+ lines, each sign predicts the other 50%%+); %d with 3+ B lines of the first sign; %d stay bound.' % (len(ba), len(rep), len(kept)))
    rd.say('- pairs: %s.' % ' '.join('%s_%s' % ab for ab in sorted(ba)))
    rd.say()
    ok1 = bool(rep) and len(kept) / len(rep) >= 0.7
    rd.rec('RR1', 'bound pairs stay bound on B', '%d of %d' % (len(kept), len(rep)), ok1)
    DL, tr, te = P.data()
    src = inspect.getsource(P.roles).replace("            num_before = g in R.NUMS\n            tot += 1",
        "            if role is None and ((i + 1 < len(t) and (g, t[i + 1]) in BOUND) or (i > 0 and (t[i - 1], g) in BOUND)):\n                role = 'bound phrase'\n            num_before = g in R.NUMS\n            tot += 1")
    ns = dict(P.__dict__)
    ns['BOUND'] = ba
    exec(src, ns)
    r0 = P.roles(DL, edges=True, head2=True)[0]
    r1, by, tot = ns['roles'](DL, edges=True, head2=True)
    ok2 = r1 - r0 >= 0.01
    rd.rec('RR2', 'the bound-phrase role raises R by 1 point or more', 'R %.1f%% -> %.1f%% (%d tokens)' % (100 * r0, 100 * r1, by['bound phrase']), ok2)
    rd.rec('P', 'progress rule: RR1 and RR2', 'RR1 %s, RR2 %s' % (ok1, ok2), ok1 and ok2)
    rd.finish()


if __name__ == '__main__':
    main()
