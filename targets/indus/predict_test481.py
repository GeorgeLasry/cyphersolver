"""Set 481 (goal run loop 127): do the large-seal formula and the small-seal signs avoid each other in a line? A and B.
Writes results/predict_test481.md."""
import random

import rtools as R
from predict_test441 import has_formula
from signs import load

SMALL = {'156', '400', '590'}


def main():
    rnd = random.Random(481)
    rd = R.Round('Four-hundred-and-eighty-first registered predictions: goal loop 127, formula and small-seal signs apart', 'predict_test481')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    res = []
    for L in (DA, DB):
        obs = sum(1 for t in L if has_formula(t) and SMALL & set(t))
        exp = []
        pool = [g for t in L for g in t]
        for _ in range(1000):
            rnd.shuffle(pool)
            k, c = 0, 0
            for t in L:
                s = pool[k:k + len(t)]
                k += len(t)
                ft = has_formula(t)
                c += ft and bool(SMALL & set(s))
            exp.append(c)
        p = (sum(e <= obs for e in exp) + 1) / 1001
        res.append((obs, sum(exp) / 1000, p))
    rd.rec('AV1', 'on A, formula lines carry a small-seal sign less often than chance', 'observed %d, expected %.1f, p = %.4f' % res[0], res[0][2] < 0.05)
    rd.rec('AV2', 'the same on B', 'observed %d, expected %.1f, p = %.4f' % res[1], res[1][2] < 0.05)
    rd.rec('P', 'progress rule: both hold', 'AV1 %s, AV2 %s' % (res[0][2] < 0.05, res[1][2] < 0.05), all(r[2] < 0.05 for r in res))
    rd.finish()


if __name__ == '__main__':
    main()
