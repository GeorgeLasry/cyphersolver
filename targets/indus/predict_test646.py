"""Set 646 (lead 5): the book's positional claims on the graffiti side (tngraffiti.in concordance: composites with the
queried base sign's position, 1 = initial). Writes results/predict_test646.md."""
import glob
import json

import rtools as R
from scipy.stats import binomtest


def data():
    recs = {}
    for f in glob.glob('data/graffiti/raw/conc_*.json'):
        for r in json.load(open(f, encoding='utf-8')).get('unique_response', []):
            recs[r['_id']] = r
    return list(recs.values())


def main():
    rd = R.Round("Set 646 registered predictions: the book's positional claims on the graffiti side", 'predict_test646')
    D = data()
    for key, b, name in (('GC1', 16, 'the jar without arms (16)'), ('GC2', 23, 'the ladder (23)')):
        comp = [r for r in D if r['base'] == b and 's2' in r and r.get('position')]
        n = sum(r['occurrence_count'] for r in comp)
        k = sum(r['occurrence_count'] for r in comp if r['position'] == 1)
        exp = sum(r['occurrence_count'] / sum(1 for j in range(1, 7) if r.get('s%d' % j) is not None) for r in comp)
        p = binomtest(k, n, exp / n, alternative='greater').pvalue if n else 1
        rd.rec(key, '%s stands first in its composites more than chance' % name, 'first in %d of %d occurrences (%d composite types), expected %.1f, p = %.4g' % (k, n, len(comp), exp, p), n > 0 and p < 0.05)
    solus = {}
    joined = {}
    for r in D:
        if 's2' in r:
            joined[r['base']] = joined.get(r['base'], 0) + r['occurrence_count']
        elif r['type'] == 'Base':
            solus[r['base']] = solus.get(r['base'], 0) + r['occurrence_count']
    rate = sum(solus.values()) / (sum(solus.values()) + sum(joined.values()))
    s34, j34 = solus.get(34, 0), joined.get(34, 0)
    exp = (s34 + j34) * rate
    p3 = binomtest(s34, s34 + j34, rate, alternative='less').pvalue if s34 + j34 else 1
    rd.rec('GC3', 'the wavy line (34) is almost never solus, against the general solus rate', 'solus %d, in composites %d; expected solus %.1f at the general rate %.2f, p = %.4g' % (s34, j34, exp, rate, p3), p3 < 0.05)
    rd.rec('P', 'progress rule: none (checks of published claims)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
