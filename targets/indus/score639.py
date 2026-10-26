"""Scores set 639 (registered four scorers, SP1-SP2) and its single-scorer audit. Writes results/predict_test639.md."""
import csv
import json

import rtools as R
from scipy.stats import fisher_exact

KEY = json.load(open('data/shapes/KEY_do_not_show_scorers.json', encoding='utf-8'))


def counts(prefix):
    out = {}
    for L in 'PQRS':
        rows = list(csv.DictReader(open('data/shapes/%s_%s.tsv' % (prefix, L), encoding='utf-8'), delimiter='\t'))
        out[KEY[L]['inventory']] = (sum(r['verdict'].strip().upper() == 'EXACT' for r in rows), sum(r['verdict'].strip().upper() == 'NEAR' for r in rows), len(rows))
    return out


def main():
    rd = R.Round('Set 639: the chance rate of graffiti-Indus shape parallels', 'predict_test639')
    for name, prefix in (('registered (one scorer per inventory)', 'score'), ('audit (one scorer for all four)', 'score_one')):
        c = counts(prefix)
        rd.say('- %s: %s.' % (name, '; '.join('%s exact %d, near %d of %d' % (k, *v) for k, v in sorted(c.items()))))
        ie = c['indus'][0]
        ctl = [v for k, v in c.items() if k != 'indus']
        ce, cn = sum(v[0] for v in ctl), sum(v[2] for v in ctl)
        p = fisher_exact([[ie, 42 - ie], [ce, cn - ce]], alternative='greater')[1]
        each = all(ie > v[0] for v in ctl)
        share = ce / cn
        if prefix == 'score':
            rd.rec('SP1', 'more exact parallels in the Indus sample than in the controls pooled and each', 'Indus %d of 42 against %d of %d, p = %.4f; above each control: %s' % (ie, ce, cn, p, each), p < 0.05 and each)
            rd.rec('SP2', 'controls average 20%+ exact parallels', '%.1f%%' % (100 * share), share >= 0.2)
        else:
            rd.say('- audit: Indus %d of 42 against %d of %d, p = %.4f; above each control: %s; controls %.1f%%.' % (ie, ce, cn, p, each, 100 * share))
    rd.rec('P', 'progress rule: none', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
