"""Set 644 (lead 3): short labels (X + ending, set 551) by object kind and against the picture. Writes results/predict_test644.md."""
import random

import rtools as R
from leadkit import mi, objects
from scipy.stats import fisher_exact


def main():
    rd = R.Round('Set 644 registered predictions: short labels, object kind and picture', 'predict_test644')
    rnd = random.Random(644)
    O = objects()
    ok1 = []
    for key, site in (('SL1a', 'Mohenjo-daro'), ('SL1b', 'Harappa')):
        tab = [[0, 0], [0, 0]]
        for s, ty, mo, size, lines, rec in O:
            if s != site:
                continue
            for t in lines:
                short = len(t) == 2 and t[1] in R.END
                long_ = len(t) >= 5 and any(g in R.END for g in t)
                if short or long_:
                    tab[0 if short else 1][0 if not ty.startswith('SEAL') else 1] += 1
        p = fisher_exact(tab, alternative='greater')[1]
        rd.rec(key, 'at %s short labels stand on non-seal objects more often than long named texts' % site, 'short %d of %d non-seal, long %d of %d, p = %.4g' % (tab[0][0], sum(tab[0]), tab[1][0], sum(tab[1]), p), p < 0.05)
        ok1.append(p < 0.05)
    out = []
    for name, cond in (('short', lambda t: len(t) == 2 and t[1] in R.END), ('long', lambda t: len(t) >= 5)):
        pairs = []
        for s, ty, mo, size, lines, rec in O:
            if ty != 'SEAL:S':
                continue
            for t in lines:
                if cond(t):
                    heads = [t[i] for i in range(len(t) - 1) if t[i + 1] in R.END]
                    if heads:
                        pairs.append((heads[0], mo or 'None'))
        real = mi(pairs)
        hs = [h for h, m in pairs]
        ge = 0
        for _ in range(1000):
            rnd.shuffle(hs)
            ge += mi(list(zip(hs, [m for h, m in pairs]))) >= real - 1e-12
        out.append((name, len(pairs), real, (ge + 1) / 1001))
    rd.rec('SL2', 'on square seals, short-label heads predict the motif beyond shuffles', ['%s heads: %d seals, MI %.3f bits, p = %.4f' % o for o in out], out[0][3] < 0.05)
    rd.rec('P', 'progress rule: SL1a and SL1b, or SL2', '', all(ok1) or out[0][3] < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
