"""Set 638: Rajan & Sivanantham 2025's positional claims (p. 37) tested on the Indus lines. Writes results/predict_test638.md."""
from collections import Counter

import rtools as R
from scipy.stats import binomtest

JAR, LADDER, WAVY = {'740'}, {'315', '317'}, {'450', '460'}


def lines():
    A, B, rowsA, recs, F = R.load_all()
    return sorted({tuple(ln) for r in F for ln in r['seq'] if ln})


def initial(L, S):
    toks = [(t, i) for t in L for i, g in enumerate(t) if g in S and len(t) >= 2]
    k = sum(i == 0 for t, i in toks)
    kf = sum(i == len(t) - 1 for t, i in toks)
    exp = sum(1 / len(t) for t, i in toks)
    return k, kf, len(toks), exp


def main():
    rd = R.Round("Set 638 registered predictions: Rajan & Sivanantham 2025's positional claims on the Indus lines", 'predict_test638')
    L = lines()
    rd.say('- %d distinct clean ICIT lines (reading order), %d of one sign.' % (len(L), sum(len(t) == 1 for t in L)))
    for key, name, S in (('PC1', 'the jar (Mahadevan 342 = ICIT 740)', JAR), ('PC2', 'the ladder (their 23.0 = M186 = ICIT 315/317)', LADDER)):
        k, kf, n, exp = initial(L, S)
        p = binomtest(k, n, exp / n, alternative='greater').pvalue if n else 1
        rd.rec(key, '%s opens Indus lines more than chance' % name, 'initial %d of %d, expected %.1f, p = %.4g; final (the mirrored claim) %d of %d' % (k, n, exp, p, kf, n), n > 0 and p < 0.05)
    one = sum(len(t) == 1 for t in L) / len(L)
    occ_lines = [t for t in L if any(g in WAVY for g in t)]
    alone = sum(len(t) == 1 for t in occ_lines)
    tot_tok = Counter(g for t in L for g in t)
    single_tok_share = sum(1 for t in L if len(t) == 1) / sum(tot_tok.values())
    exp = sum(tot_tok[g] for g in WAVY) * single_tok_share
    ok = alone == 0 and exp >= 3
    rd.rec('PC3', 'the wavy line (their 34.0 = M132 = ICIT 450; variant 460) never stands alone in Indus',
           'in %d lines, alone in %d; expected alone at the general rate %.1f (testable if 3+)' % (len(occ_lines), alone, exp), ok)
    rd.rec('P', 'progress rule: none (checks of published claims)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
