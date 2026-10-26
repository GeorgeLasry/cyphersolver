"""Set 641: Wells 2015's proposed sign values (Fig. 6.20-6.21) as predictions on the ICIT lines (A, with objects) and
Mahadevan's lines (B). Writes results/predict_test641.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from scipy.stats import binomtest, fisher_exact
from signs import load


def samples():
    A, B, rowsA, recs, F = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    return DA, DB, F, recs


def matched(S, g, rnd, k=200):
    occ = Counter(x for t in S for x in t)
    pool = sorted((x for x in occ if x != g and x not in R.NUMS), key=lambda x: abs(occ[x] - occ[g]))[:20]
    return [rnd.choice(pool) for _ in range(k)]


def counted(S, g):
    toks = [(t, i) for t in S for i, x in enumerate(t) if x == g]
    return sum(i > 0 and t[i - 1] in R.NUMS for t, i in toks) / max(1, len(toks)), len(toks)


def diversity(S, g):
    left, right, n = set(), set(), 0
    for t in S:
        for i, x in enumerate(t):
            if x == g:
                n += 1
                left.add(t[i - 1] if i else '^')
                right.add(t[i + 1] if i + 1 < len(t) else '$')
    return (len(left) + len(right)) / max(1, 2 * n), n


def main():
    rnd = random.Random(641)
    rd = R.Round('Set 641 registered predictions: Wells 2015 proposed values', 'predict_test641')
    DA, DB, F, recs = samples()
    res = {}
    for key, title, fn, g in (('WV1', "840 'parai, rice measure' is counted (a numeral right before it) more than frequency-matched signs", counted, '840'),
                              ('WV2', "850 'ko', a syllable sign, has more distinct neighbours per token than frequency-matched signs", diversity, '850')):
        out = []
        for name, S in (('A', DA), ('B', DB)):
            obs, n = fn(S, g)
            null = [fn(S, h)[0] for h in matched(S, g, rnd)]
            p = (sum(x >= obs for x in null) + 1) / (len(null) + 1)
            out.append((name, obs, n, sum(null) / len(null), p))
        ok = all(p < 0.05 for *_, p in out)
        rd.rec(key, title, ['%s: %.3f over %d tokens, matched signs %.3f, p = %.3f' % o for o in out], ok)
    hare = [[0, 0], [0, 0]]
    for r in F:
        rec = recs.get(r['sealid'])
        if not rec:
            continue
        lines = [tuple(ln) for ln in r['seq'] if ln]
        pair = any(t[i:i + 2] == ('752', '820') for t in lines for i in range(len(t) - 1))
        single = not pair and any(('752' in t) or ('820' in t) for t in lines)
        if not (pair or single):
            continue
        is_hare = 'hare' in rec[18].lower() or rec[18].split(':')[0].strip().lower().startswith('lep')
        hare[0 if pair else 1][0 if is_hare else 1] += 1
    p3 = fisher_exact(hare, alternative='greater')[1]
    rd.rec('WV3', "objects with 752 820 ('kevi-yan', hare) show a hare more often than objects with 752 or 820 alone",
           'pair %d of %d hare, alone %d of %d hare, p = %.4f' % (hare[0][0], sum(hare[0]), hare[1][0], sum(hare[1]), p3), p3 < 0.05)
    out = []
    for name, S in (('A', DA), ('B', DB)):
        toks = [(t, i) for t in S if len(t) >= 2 for i, x in enumerate(t) if x == '32']
        k = sum(i == len(t) - 1 for t, i in toks)
        exp = sum(1 / len(t) for t, i in toks)
        p = binomtest(k, len(toks), exp / len(toks), alternative='greater').pvalue if toks else 1
        out.append((name, k, len(toks), exp, p))
    rd.rec('WV4', "032 '-ir', a 2nd-person plural ending, stands line-final more than chance, on A and B",
           ['%s: final %d of %d, expected %.1f, p = %.4g' % o for o in out], all(o[4] < 0.05 for o in out))
    rd.rec('P', 'progress rule: none (checks of published proposals)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
