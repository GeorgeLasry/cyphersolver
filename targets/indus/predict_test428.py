"""Set 428 (goal run loop 74): mid-line numerals as phrase openers (set 397). A and B. Writes results/predict_test428.md."""
import random

import rtools as R
from scipy.stats import fisher_exact
from signs import load

N = {'1', '2'}


def main():
    rnd = random.Random(428)
    rd = R.Round('Four-hundred-and-twenty-eighth registered predictions: goal loop 74, mid-line numerals open a name', 'predict_test428')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    r1, r2 = [], []
    for name, L in (('A', DA), ('B', DB)):
        mid = [t[i + 2] in R.END for t in L for i in range(1, len(t) - 2) if t[i] in N and t[i - 1] not in R.NUMS and t[i + 1] not in R.NUMS]
        ini = [t[2] in R.END for t in L if len(t) > 2 and t[0] in N and t[1] not in R.NUMS]
        o, p = fisher_exact([[sum(mid), len(mid) - sum(mid)], [sum(ini), len(ini) - sum(ini)]], alternative='greater')
        rd.say('- %s: after mid-line N X an ending follows in %d of %d; after line-initial N X in %d of %d; p = %.4f.' % (name, sum(mid), len(mid), sum(ini), len(ini), p))
        r1.append(p < 0.05)

        def near(t, i):
            return any(g in R.END for g in t[i + 1:i + 4])
        hits = [near(t, i) for t in L for i in range(1, len(t) - 1) if t[i] in N and t[i - 1] not in R.NUMS and t[i + 1] not in R.NUMS]
        pool = [near(t, i) for t in L for i in range(1, len(t) - 1) if t[i] not in R.NUMS]
        ge = sum(sum(rnd.sample(pool, len(hits))) >= sum(hits) for _ in range(1000))
        p2 = (ge + 1) / 1001
        rd.say('- %s: an ending within three signs after a mid-line numeral in %d of %d; random mid-line %.1f%%; p = %.4f.' % (name, sum(hits), len(hits), 100 * sum(pool) / len(pool), p2))
        r2.append(p2 < 0.05)
    rd.say()
    rd.rec('NO1', 'mid-line N X is followed by an ending more than line-initial N X, A and B', 'A %s, B %s' % tuple(r1), all(r1))
    rd.rec('NO2', 'an ending follows within three signs of a mid-line numeral more than chance, A and B', 'A %s, B %s' % tuple(r2), all(r2))
    rd.rec('P', 'progress rule: either holds', 'NO1 %s, NO2 %s' % (all(r1), all(r2)), all(r1) or all(r2))
    rd.finish()


if __name__ == '__main__':
    main()
