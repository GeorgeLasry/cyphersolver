"""Set 465 (goal run loop 111): do the two name classes share multi-line objects? Writes results/predict_test465.md."""
import random

import rtools as R
from signs import load


def cls(ln):
    e = [g for g in ln if g in R.END]
    return e[-1] if e else None


def test(objs, rnd):
    lines = [l for o in objs for l in o]
    obs = sum(1 for o in objs if {'740', '520'} <= {cls(l) for l in o})
    ge = le = 0
    for _ in range(1000):
        rnd.shuffle(lines)
        k, s = 0, 0
        for o in objs:
            if {'740', '520'} <= {cls(l) for l in lines[k:k + len(o)]}:
                s += 1
            k += len(o)
        ge += s >= obs
        le += s <= obs
    return obs, len(objs), min(1, 2 * min(ge, le) / 1000)


def main():
    rnd = random.Random(465)
    rd = R.Round('Four-hundred-and-sixty-fifth registered predictions: goal loop 111, the two name classes on one object', 'predict_test465')
    A, B, rowsA, recs, F = R.load_all()
    oa = [[tuple(l) for l in r['seq'] if l] for r in F]
    oa = [o for o in oa if len(o) > 1]
    ob = [[tuple(l) for l in r['seq'] if l] for r in load(only_m77=True)]
    ob = [o for o in ob if len(o) > 1]
    a = test(oa, rnd)
    b = test(ob, rnd)
    rd.rec('OB1', 'ICIT multi-line objects carry both classes at a rate other than chance (two-sided)', '%d of %d objects, p = %.4f' % a, a[2] < 0.05)
    rd.rec('OB2', "the same on Mahadevan's objects", '%d of %d objects, p = %.4f' % b, b[2] < 0.05)
    rd.rec('P', 'progress rule: both hold', 'OB1 %s, OB2 %s' % (a[2] < 0.05, b[2] < 0.05), a[2] < 0.05 and b[2] < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
