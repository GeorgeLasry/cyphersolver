"""Session-2 loops 38-41: four quick structural tests (VARIANT)."""
import random
from collections import Counter

import rtools as R
import s2kit as K
from scipy.stats import binomtest, fisher_exact

V = 'noend'
OP = {'104', '491', '692', '817', '820', '853', '861', '920'}
SPEC = {
    'single': ('single-sign texts are names', 'the signs of one-sign texts are name heads (stand before an ending) in longer lines more often than frequency-matched signs (200 draws)'),
    'afterend': ('what follows a mid-line ending', 'the sign after a mid-line ending (not 400 / 90) is an opener or numeral more often than signs at the same positions in general'),
    'openers': ('two openers lead into different texts', 'the signs after 920 and after 820 differ: 3+ follower signs skewed at p < 0.05 on A, and 75% of testable ones keep their side on B'),
    'noend': ('signs that never take an ending', 'signs with 15+ A tokens never before an ending stay under 5% before an ending on B for 90%+ of those with 5+ B tokens'),
}
TITLE, CLAIM = SPEC[V]
REG = '''(`hyp_s2_q.py`, VARIANT=%s)

- **Q1** On A: %s (p < 0.05 where a test applies).
- **Q2** The same on B (for 'openers' and 'noend' Q2 is the B part of the claim).
- Progress rule: Q1 and Q2, except 'noend' (consistency: recorded, no progress).''' % (V, CLAIM)
SUMMARY = ''


def headrate(S):
    occ = Counter(g for t in S for g in t)
    hd = Counter(t[i] for t in S for i in range(len(t) - 1) if t[i + 1] in R.END)
    return occ, hd


def run(rd):
    global SUMMARY
    rnd = random.Random(573)
    DA, DB = K.ab()
    res = []
    if V == 'single':
        for key, S in (('Q1', DA), ('Q2', DB)):
            sing = {t[0] for t in S if len(t) == 1}
            occ, hd = headrate([t for t in S if len(t) > 1])
            sing = [g for g in sing if occ[g] >= 3]
            obs = sum(hd[g] / occ[g] for g in sing) / max(1, len(sing))
            pool = sorted(occ, key=occ.get)
            ge = 0
            for _ in range(200):
                v = []
                for g in sing:
                    k = pool.index(g)
                    h = pool[max(0, min(len(pool) - 1, k + rnd.randint(-5, 5)))]
                    v.append(hd[h] / occ[h])
                ge += sum(v) / max(1, len(v)) >= obs
            p = (ge + 1) / 201
            rd.rec(key, CLAIM, 'mean head rate %.3f over %d single signs, p = %.4f' % (obs, len(sing), p), p < 0.05)
            res.append(p < 0.05)
    elif V == 'afterend':
        for key, S in (('Q1', DA), ('Q2', DB)):
            a = [t[i + 1] for t in S for i in range(len(t) - 1) if t[i] in R.END and t[i + 1] not in ('400', '90')]
            base = [t[i] for t in S for i in range(1, len(t))]
            hit = lambda g: g in OP or g in R.NUMS
            x, y = sum(map(hit, a)), sum(map(hit, base))
            p = fisher_exact([[x, len(a) - x], [y, len(base) - y]], alternative='greater')[1]
            rd.rec(key, CLAIM, '%d of %d against %d of %d, p = %.4g' % (x, len(a), y, len(base), p), p < 0.05)
            res.append(p < 0.05)
    elif V == 'openers':
        f = lambda S, o: Counter(t[1] for t in S if len(t) > 1 and t[0] == o)
        a9, a8 = f(DA, '920'), f(DA, '820')
        n9, n8 = sum(a9.values()), sum(a8.values())
        sk = {g: a9[g] / n9 > a8[g] / n8 for g in set(a9) | set(a8) if a9[g] + a8[g] >= 5 and fisher_exact([[a9[g], n9 - a9[g]], [a8[g], n8 - a8[g]]])[1] < 0.05}
        b9, b8 = f(DB, '920'), f(DB, '820')
        m9, m8 = max(1, sum(b9.values())), max(1, sum(b8.values()))
        rep = [g for g in sk if b9[g] + b8[g] >= 3]
        same = sum((b9[g] / m9 > b8[g] / m8) == sk[g] for g in rep)
        ok1, ok2 = len(sk) >= 3, bool(rep) and same / len(rep) >= 0.75
        rd.rec('Q1', '3+ skewed followers on A', '920: %s; 820: %s' % (' '.join(g for g in sk if sk[g]), ' '.join(g for g in sk if not sk[g])), ok1)
        rd.rec('Q2', 'kept on B', '%d of %d' % (same, len(rep)), ok2)
        res = [ok1, ok2]
    else:
        occ, hd = headrate(DA)
        ne = [g for g in occ if occ[g] >= 15 and hd[g] == 0]
        ob, hb = headrate(DB)
        test = [g for g in ne if ob[g] >= 5]
        stay = sum(hb[g] / ob[g] < 0.05 for g in test)
        rd.rec('Q1', 'signs never before an ending on A', '%d signs' % len(ne), bool(ne))
        rd.rec('Q2', 'stay under 5%% on B for 90%%+', '%d of %d' % (stay, len(test)), bool(test) and stay / len(test) >= 0.9)
        res = [False]
    SUMMARY = '%s: %s.' % (V, res)
    return all(res)
