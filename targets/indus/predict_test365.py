"""Set 365 (goal run loop 11): regional variants inside graphic families (decade blocks). Writes results/predict_test365.md."""
import math
import random
from collections import Counter, defaultdict

import loopkit as L
import rtools as R
from famlm import fam
from scipy.stats import fisher_exact


def reg(t):
    return R.region(L.META.get(t, ('', '', ''))[0])


def skews(S, minn=10):
    c = {'sindh': Counter(), 'north': Counter()}
    for t in S:
        if reg(t) in c:
            c[reg(t)].update(t)
    n = {k: sum(v.values()) for k, v in c.items()}
    out = {}
    for g in set(c['sindh']) | set(c['north']):
        s, m = c['sindh'][g], c['north'][g]
        if s + m >= minn and g.isdigit():
            p = fisher_exact([[s, n['sindh'] - s], [m, n['north'] - m]])[1]
            out[g] = (s / n['sindh'] - m / n['north'], p)
    return out


def opposite(sk, pairs):
    return sum(1 for a, b in pairs if sk[a][1] < 0.05 and sk[b][1] < 0.05 and (sk[a][0] > 0) != (sk[b][0] > 0))


def main():
    rnd = random.Random(365)
    rd = R.Round('Three-hundred-and-sixty-fifth registered predictions: goal loop 11, regional variants in graphic families', 'predict_test365')
    (tr, te), (DA, DB) = L.splits()
    res = []
    for name, S in (('A', DA), ('B', DB)):
        sk = skews(S)
        gs = sorted(sk)
        fam_pairs = [(a, b) for i, a in enumerate(gs) for b in gs[i + 1:] if fam(a) == fam(b)]
        obs = opposite(sk, fam_pairs)
        other = [(a, b) for i, a in enumerate(gs) for b in gs[i + 1:] if fam(a) != fam(b)]
        null = [opposite(sk, rnd.sample(other, len(fam_pairs))) for _ in range(1000)]
        p = (sum(x >= obs for x in null) + 1) / 1001
        rd.say('- %s: %d same-family pairs, %d opposite-skewed (both p < 0.05); random cross-family pairs mean %.2f; p = %.4f; pairs %s.' % (
            name, len(fam_pairs), obs, sum(null) / 1000, p, ' '.join('%s/%s' % ab for ab in fam_pairs if opposite(sk, [ab]))))
        res.append((p, sk, fam_pairs, S))
    rd.say()
    ok1 = all(p < 0.05 for p, *_ in res)
    rd.rec('RA1', 'family members split by region more than chance, on A and on B', 'A p = %.4f, B p = %.4f' % (res[0][0], res[1][0]), ok1)
    p, sk, fam_pairs, S = res[0]
    DL = sorted(set(DA) | set(DB))
    prev = {'sindh': defaultdict(Counter), 'north': defaultdict(Counter)}
    for t in DL:
        if reg(t) in prev:
            for i in range(1, len(t)):
                prev[reg(t)][t[i]][t[i - 1]] += 1

    def cos(va, vb):
        num = sum(va[k] * vb[k] for k in va)
        den = math.sqrt(sum(x * x for x in va.values())) * math.sqrt(sum(x * x for x in vb.values()))
        return num / den if den else 0.0
    pairs = [(a, b) if sk[a][0] > 0 else (b, a) for a, b in fam_pairs if opposite(sk, [(a, b)])]
    if pairs:
        obs = sum(cos(prev['sindh'][s], prev['north'][n]) for s, n in pairs) / len(pairs)
        north_signs = [g for g in prev['north'] if sum(prev['north'][g].values()) >= 5]
        ge = sum(sum(cos(prev['sindh'][s], prev['north'][rnd.choice(north_signs)]) for s, n in pairs) / len(pairs) >= obs for _ in range(1000))
        p2 = (ge + 1) / 1001
        rd.rec('RA2', 'the Sindh variant fills the same slots as its northern counterpart', 'mean cosine %.3f over %d pairs, p = %.4f' % (obs, len(pairs), p2), p2 < 0.05)
    else:
        rd.rec('RA2', 'the Sindh variant fills the same slots as its northern counterpart', 'no opposite-skewed pairs on A', False)
    rd.rec('P', 'progress rule: RA1 (replicated)', 'RA1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
