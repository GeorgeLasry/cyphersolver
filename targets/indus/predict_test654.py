"""Set 654: set 653 with a corrected null. Partners' classes are permuted across the minimal pairs (frame-weighted), so
the null keeps each slot's class frequencies; set 653 permuted labels among sign types, which a few numeral signs with
many frames made degenerate. Writes results/predict_test654.md."""
import random

import rtools as R
from leadkit import ab
from predict_test648 import minimal_pairs
from predict_test653 import indus_class, lb_class, lb_lines


def test(mp, cls, rnd, n=1000):
    a_, b_ = [], []
    for (a, b), k in mp.items():
        for _ in range(k):
            x, y = (a, b) if rnd.random() < 0.5 else (b, a)
            a_.append(cls[x])
            b_.append(cls[y])
    obs = sum(x == y for x, y in zip(a_, b_)) / len(a_)
    ge = 0
    for _ in range(n):
        rnd.shuffle(b_)
        ge += sum(x == y for x, y in zip(a_, b_)) / len(a_) >= obs
    return obs, (ge + 1) / (n + 1), len(a_)


def main():
    rd = R.Round('Set 654 registered predictions: substitution classes, corrected null', 'predict_test654')
    rnd = random.Random(654)
    L = lb_lines()
    obs, p, n = test(minimal_pairs(L), {x: lb_class(x) for t in L for x in t}, rnd)
    rd.rec('SD1', 'Linear B control: partners share a class beyond permuted partners', '%d frames; same class %.3f, p = %.4f' % (n, obs, p), p < 0.05)
    oks = [p < 0.05]
    for key, name, S in (('SD2', 'A', ab()[0]), ('SD3', 'B', ab()[1])):
        o, pp, nn = test(minimal_pairs(S), {g: indus_class(g) for t in S for g in t}, rnd)
        rd.rec(key, 'Indus %s: the same' % name, '%d frames; same class %.3f, p = %.4f' % (nn, o, pp), pp < 0.05)
        oks.append(pp < 0.05)
    rd.rec('P', 'progress rule: SD1, SD2 and SD3 (with set 653\'s SC4, a validated substitution method)', '', all(oks))
    rd.finish()


if __name__ == '__main__':
    main()
