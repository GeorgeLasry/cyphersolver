"""Set 642 (lead 1): does what is counted (large-number against small-number units, sets 552/562) go with the picture on
the object? Writes results/predict_test642.md."""
import random

import rtools as R
from leadkit import mi, objects
from numerals import NUMS

LARGE = {'390', '405', '407', '575', '585', '900'}
SMALL = {'176', '233', '235', '240', '61', '803', '806'}


def main():
    rd = R.Round('Set 642 registered predictions: counted units and the picture on the object', 'predict_test642')
    rnd = random.Random(642)
    ok = []
    for key, site in (('PU1', 'Mohenjo-daro'), ('PU2', 'Harappa')):
        obs = []
        for s, ty, mo, size, lines, rec in objects():
            if s != site:
                continue
            for t in lines:
                for i in range(1, len(t)):
                    if t[i - 1] in NUMS and (t[i] in LARGE or t[i] in SMALL):
                        obs.append((ty, 'L' if t[i] in LARGE else 'S', mo or 'None'))
        real = sum(mi([(g, m) for t, g, m in obs if t == ty]) * sum(1 for x in obs if x[0] == ty) for ty in {o[0] for o in obs})
        ge = 0
        for _ in range(1000):
            sh = []
            for ty in {o[0] for o in obs}:
                gs = [g for t, g, m in obs if t == ty]
                rnd.shuffle(gs)
                sh += [(ty, g, m) for g, (t, _, m) in zip(gs, [o for o in obs if o[0] == ty])]
            v = sum(mi([(g, m) for t, g, m in sh if t == ty]) * sum(1 for x in sh if x[0] == ty) for ty in {o[0] for o in sh})
            ge += v >= real - 1e-12
        p = (ge + 1) / 1001
        rd.rec(key, 'at %s the unit group predicts the motif within object kinds' % site, '%d counted units; weighted MI %.3f bits; shuffles as high %d of 1000, p = %.4f' % (len(obs), real, ge, p), p < 0.05)
        ok.append(p < 0.05)
    rd.rec('P', 'progress rule: PU1 and PU2', '', all(ok))
    rd.finish()


if __name__ == '__main__':
    main()
