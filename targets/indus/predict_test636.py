"""Set 636: the number-size units (sets 552, 562) on objects, and 892 against the U sign 700 (set 593).
Writes results/predict_test636.md."""
import math
import random
from collections import Counter

import rtools as R
from numerals import NUMS
from scipy.stats import fisher_exact

LARGE = {'390', '405', '407', '575', '585', '900'}
SMALL = {'176', '233', '235', '240', '61', '803', '806'}


def objects():
    A, B, rowsA, recs, F = R.load_all()
    out = []
    for r in F:
        rec = recs.get(r['sealid'])
        if not rec:
            continue
        out.append((rec[3].strip(), rec[20].split(':')[0], rec[18].split(':')[0].strip(), [tuple(t) for t in r['seq'] if t]))
    return out


def units(lines, G):
    return [(t, i) for t in lines for i in range(1, len(t)) if t[i] in G and t[i - 1] in NUMS]


def cos(a, b):
    num = sum(a[k] * b[k] for k in a)
    den = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return num / den if den else 0.0


def main():
    rd = R.Round('Set 636 registered predictions: number-size units on objects; 892 and the U sign 700', 'predict_test636')
    O = objects()
    res = {}
    for site in ('Harappa', 'Mohenjo-daro'):
        tab = [[0, 0], [0, 0]]
        lng = [[0, 0], [0, 0]]
        pic = [[0, 0], [0, 0]]
        for s, ty, mo, lines in O:
            if s != site:
                continue
            for row, G in ((0, LARGE), (1, SMALL)):
                for t, i in units(lines, G):
                    tab[row][0 if ty == 'TAB' else 1] += 1
                    lng[row][0 if NUMS[t[i - 1]][1] == 'long' else 1] += 1
                    if ty == 'TAB':
                        pic[row][0 if mo in ('', 'None', '-') else 1] += 1
        res[site] = (tab, lng, pic)
        rd.say('- %s: on tablets large %s small %s; long strokes large %s small %s; tablet units without a picture large %s small %s.' % (site, tab[0], tab[1], lng[0], lng[1], pic[0], pic[1]))
    rd.say()

    def both(k, alt='greater'):
        ps = [fisher_exact(res[s][k], alternative=alt)[1] for s in ('Harappa', 'Mohenjo-daro')]
        return ps, all(p < 0.05 for p in ps)
    p1, ok1 = both(0)
    rd.rec('CU1', 'large-number units stand on tablets more than small-number units, at Harappa and at Mohenjo-daro', 'p = %.4g, %.4g' % tuple(p1), ok1)
    p2, ok2 = both(1)
    rd.rec('CU2', 'large-number units take long-stroke numerals more, in both cities', 'p = %.4g, %.4g' % tuple(p2), ok2)
    p3, ok3 = both(2)
    rd.rec('CU3', 'on tablets, large-number units stand on unpictured tablets more (records, not labels), in both cities', 'p = %.4g, %.4g' % tuple(p3), ok3)
    rnd = random.Random(636)
    lines_all = [t for s, ty, mo, lines in O for t in lines]
    kinds = {}
    for s, ty, mo, lines in O:
        for t in lines:
            kinds[t] = ty
    def kind_share(g, uncounted):
        c = Counter(kinds[t] for t in lines_all for i, x in enumerate(t) if x == g and (not uncounted or i == 0 or t[i - 1] not in NUMS))
        return c
    k892, k700 = kind_share('892', False), kind_share('700', True)
    occ = Counter(x for t in lines_all for x in t)
    pool = [g for g in occ if 30 <= occ[g] <= 150 and g not in ('892', '700')]
    obs = cos(k892, k700)
    ge = sum(cos(kind_share(rnd.choice(pool), False), k700) >= obs for _ in range(300))
    p4 = (ge + 1) / 301
    rd.rec('U1', '892 is spread over object kinds like uncounted 700, beyond random signs of similar frequency',
           '892 %s; uncounted 700 %s; cosine %.3f; random as high %d of 300, p = %.4f' % (dict(k892), dict(k700), obs, ge, p4), p4 < 0.05)
    nx = lambda g: Counter(t[i + 1] if i + 1 < len(t) else '$' for t in lines_all for i, x in enumerate(t) if x == g and (g != '700' or i == 0 or t[i - 1] not in NUMS))
    n892, n700 = nx('892'), nx('700')
    obs5 = cos(n892, n700)
    ge5 = sum(cos(nx(rnd.choice(pool)), n700) >= obs5 for _ in range(300))
    p5 = (ge5 + 1) / 301
    rd.rec('U2', '892 is followed by the same signs as uncounted 700, beyond random signs', 'cosine %.3f; random as high %d of 300, p = %.4f' % (obs5, ge5, p5), p5 < 0.05)
    rd.rec('P', 'progress rule: CU1 or CU3 (the units belong to tablet records), or U1 and U2 (892 is a form of 700)', '', ok1 or ok3 or (p4 < 0.05 and p5 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
