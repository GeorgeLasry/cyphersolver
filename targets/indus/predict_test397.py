"""Set 397 (goal run loop 43): what precedes a divider, and each divider separately. Writes results/predict_test397.md."""
import random
from collections import Counter

import predict_test395 as T
import rtools as R
from signs import load


def main():
    rnd = random.Random(397)
    rd = R.Round('Three-hundred-and-ninety-seventh registered predictions: goal loop 43, before the divider; each divider', 'predict_test397')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    ok = []
    for name, L in (('A', DA), ('B', DB)):
        pre740 = Counter(t[i - 1] for t in L for i in range(1, len(t)) if t[i] == '740')
        occ = Counter(g for t in L for g in t)
        heads = {g for g in occ if occ[g] >= 5 and pre740[g] / occ[g] >= 0.3 and g not in R.NUMS}
        before = [t[i - 1] in heads for t in L for i in range(1, len(t) - 1) if t[i] in T.DIV and t[i - 1] not in R.NUMS and t[i + 1] not in R.NUMS]
        mids = [t[i - 1] in heads for t in L for i in range(1, len(t) - 1) if t[i - 1] not in R.NUMS]
        a, n = sum(before), len(before)
        ge = sum(sum(rnd.sample(mids, n)) >= a for _ in range(1000))
        p = (ge + 1) / 1001
        rd.say('- %s: before a divider %d of %d are name heads (30%%+ of their tokens before 740); random mid-line %.1f%%; p = %.4f.' % (name, a, n, 100 * sum(mids) / len(mids), p))
        ok.append(p < 0.05)
    rd.say()
    rd.rec('DB1', 'the sign before a divider is a name head more often than chance, A and B', 'A %s, B %s' % tuple(ok), all(ok))
    per = []
    for d in ('2', '1', '60'):
        T.DIV = {d}
        o, n, p = T.divider_test(DA, rnd)
        per.append(p < 0.05)
        rd.say('- %s alone on A: cosine %.3f over %d tokens, p = %.4f.' % (d, o, n, p))
    rd.rec('DB2', 'each of 2, 1, 60 alone works as a divider on A', '%d of 3' % sum(per), all(per))
    rd.rec('P', 'progress rule: DB1', 'DB1 %s' % all(ok), all(ok))
    rd.finish()


if __name__ == '__main__':
    main()
