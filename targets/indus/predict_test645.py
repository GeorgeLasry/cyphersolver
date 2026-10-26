"""Set 645 (lead 4): stroke signs on Indus-script objects from the Gulf, Mesopotamia, Iran and Central Asia: counts or
sound signs? Writes results/predict_test645.md."""
import random
from collections import Counter

import icit_full
import rtools as R
from scipy.stats import fisher_exact

FOREIGN = {'Persian Gulf', 'Mesopotamia', 'Iranian Plateau', 'Central Asia'}
HOME = {'Inter-Riverine', 'Lower Indus', 'Gujarat/Kutch'}


def lines(regions, seals_only=True):
    R.load_all()
    out = []
    for rec in icit_full.records(R.FPATH):
        if rec[2].strip() not in regions or (seals_only and not rec[20].startswith('SEAL')):
            continue
        for ln in icit_full.lines_of(rec[34]):
            run = []
            for g in ln['signs'] + [None]:
                if g in (None, '?'):
                    if len(run) >= 2:
                        out.append(tuple(run))
                    run = []
                else:
                    run.append(g)
    return out


def main():
    rd = R.Round('Set 645 registered predictions: strokes on Indus-script seals found abroad', 'predict_test645')
    rnd = random.Random(645)
    home, abroad = lines(HOME), lines(FOREIGN)
    occ = Counter(g for t in home for g in t)
    cnt = Counter(t[i] for t in home for i in range(1, len(t)) if t[i - 1] in R.NUMS)
    counted = {g for g in occ if occ[g] >= 8 and cnt[g] / occ[g] >= 0.5}
    def follow(L):
        x = [(t[i + 1] in counted) for t in L for i in range(len(t) - 1) if t[i] in R.NUMS and t[i + 1] not in R.NUMS]
        return sum(x), len(x)
    a, na = follow(abroad)
    b, nb = follow(home)
    p1 = fisher_exact([[a, na - a], [b, nb - b]], alternative='less')[1]
    rd.say('- %d legible runs abroad, %d at home; counted signs (home): %d.' % (len(abroad), len(home), len(counted)))
    rd.rec('GS1', 'abroad, a stroke sign is followed by a usual counted sign less often than at home', 'abroad %d of %d, home %d of %d, p = %.4g' % (a, na, b, nb, p1), p1 < 0.05)
    def div(L):
        toks = [(t, i) for t in L for i, g in enumerate(t) if g in R.NUMS]
        nb_ = {(t[i - 1] if i else '^', t[i + 1] if i + 1 < len(t) else '$') for t, i in toks}
        return len(nb_) / max(1, len(toks)), toks
    obs, ta = div(abroad)
    _, th = div(home)
    ge = 0
    for _ in range(1000):
        smp = rnd.sample(th, len(ta))
        v = len({(t[i - 1] if i else '^', t[i + 1] if i + 1 < len(t) else '$') for t, i in smp}) / len(smp)
        ge += v >= obs
    p2 = (ge + 1) / 1001
    rd.rec('GS2', 'abroad, stroke signs stand in more varied contexts than equal-sized home samples', '%.3f distinct (left, right) contexts per stroke token over %d tokens; home samples as high %d of 1000, p = %.4f' % (obs, len(ta), ge, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: GS1 and GS2 (strokes used as sound signs abroad: a lead to values)', '', p1 < 0.05 and p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
