"""Set 650 (lead 9): does the long closing formula (705/706 33 520) go with larger seals, and within the same name body?
Writes results/predict_test650.md."""
from collections import defaultdict

import rtools as R
from leadkit import objects
from scipy.stats import binomtest, mannwhitneyu

F = {('705', '33', '520'), ('706', '33', '520')}


def main():
    rd = R.Round('Set 650 registered predictions: seal size and the long closing formula', 'predict_test650')
    rows = []
    for s, ty, mo, size, lines, rec in objects():
        if not ty.startswith('SEAL'):
            continue
        try:
            x = float(size)
        except ValueError:
            continue
        if x <= 0:
            continue
        for t in lines:
            j = next((j for j in range(len(t) - 2) if tuple(t[j:j + 3]) in F), None)
            if j is not None:
                rows.append((x, True, tuple(t[:j])))
            elif t and t[-1] in R.END:
                rows.append((x, False, tuple(t[:-1])))
    a = [x for x, h, c in rows if h]
    b = [x for x, h, c in rows if not h]
    p1 = mannwhitneyu(a, b, alternative='greater').pvalue
    rd.rec('SF1', 'seals with the long formula are larger than seals with a plain ending', 'formula mean %.1f mm (%d), plain %.1f mm (%d), p = %.4g' % (sum(a) / len(a), len(a), sum(b) / len(b), len(b), p1), p1 < 0.05)
    by = defaultdict(list)
    for x, h, c in rows:
        by[c].append((x, h))
    wins = n = 0
    det = []
    for c, v in by.items():
        f = [x for x, h in v if h]
        pl = [x for x, h in v if not h]
        if f and pl:
            n += 1
            w = sum(f) / len(f) > sum(pl) / len(pl)
            wins += w
            det.append('%s: formula %.1f (%d) vs plain %.1f (%d)' % (' '.join(c) or '(none)', sum(f) / len(f), len(f), sum(pl) / len(pl), len(pl)))
    p2 = binomtest(wins, n, 0.5, alternative='greater').pvalue if n else 1
    rd.rec('SF2', 'within the same name body, the formula copy is on the larger seal', ['%d of %d bodies, p = %.4f' % (wins, n, p2)] + det, n >= 5 and p2 < 0.05)
    rd.rec('P', 'progress rule: SF1 and SF2 (the long formula is a size / status marking of the same name)', '', p1 < 0.05 and n >= 5 and p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
