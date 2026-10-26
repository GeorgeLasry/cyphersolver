"""Set 390 (goal run loop 36): are names local? Name bodies (signs before 740/520) shared between objects, against
site shares. Writes results/predict_test390.md."""
from collections import Counter, defaultdict

import rtools as R
from scipy.stats import binomtest


def body(t):
    for i in range(len(t) - 1, 0, -1):
        if t[i] in R.END:
            return tuple(t[max(0, i - 3):i]) if i >= 2 else None
    return None


def main():
    rd = R.Round('Three-hundred-and-ninetieth registered predictions: goal loop 36, are names local?', 'predict_test390')
    A, B, rowsA, recs, F = R.load_all()
    seals, tabs = [], []
    for r in F:
        rec = recs.get(r['sealid'])
        if not rec:
            continue
        ty = str(rec[20])
        for ln in r['seq']:
            b = body(tuple(ln)) if ln else None
            if b:
                (seals if ty.startswith('SEAL') else tabs if ty.startswith('TAB') else []).append((b, r['site'], r['sealid']))
    share = Counter(s for b, s, i in seals)
    n = sum(share.values())
    sb = defaultdict(list)
    for b, s, i in seals:
        sb[b].append((s, i))
    hit = exp = tot = 0
    for b, s, i in tabs:
        for s2, i2 in sb.get(b, []):
            tot += 1
            hit += s2 == s
            exp += share[s] / n
    p1 = binomtest(hit, tot, exp / max(1, tot), alternative='greater').pvalue if tot else 1
    rd.rec('NL1', 'a seal sharing a tablet name is from the same city more than site shares predict', '%d of %d pairs same site, expected %.1f, p = %.4g' % (hit, tot, exp, p1), p1 < 0.05)
    hit2 = exp2 = tot2 = 0
    for b, lst in sb.items():
        for a in range(len(lst)):
            for c in range(a + 1, len(lst)):
                if lst[a][1] == lst[c][1]:
                    continue
                tot2 += 1
                hit2 += lst[a][0] == lst[c][0]
                exp2 += share[lst[a][0]] / n
    p2 = binomtest(hit2, tot2, exp2 / max(1, tot2), alternative='greater').pvalue if tot2 else 1
    rd.rec('NL2', 'seals sharing a name are from the same city more than site shares predict', '%d of %d pairs same site, expected %.1f, p = %.4g' % (hit2, tot2, exp2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'NL1 %s, NL2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
