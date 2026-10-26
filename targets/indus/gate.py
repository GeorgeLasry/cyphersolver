"""The copper-tablet gate (25 Oct 2026, tier 2 bookkeeping): a proposed key must be consistent with the sign = picture
equations of the Mohenjo-daro copper tablets (rebus/copper_tablets.tsv; results/copper.md). Two checks per key, on its
own glosses (no lexicon needed): (1) anchor signs 749 = markhor goat, 341 = rhinoceros, 753 = hare: if the key gives the
sign a value, does its gloss name the animal; (2) anchor texts (A2 goat, B5 rhinoceros, B1 bull, B7 hare): does any
gloss of the text's signs name the picture. A key passes if it covers at least one anchor and none it covers is wrong.
Writes results/gate.md."""
import glob
import os
import re

import bench

HERE = os.path.dirname(os.path.abspath(__file__))
SIGNS = {'749': 'goat', '341': 'rhino', '753': 'hare'}
TEXTS = [('806 233 384 740', 'goat'), ('503 615 740', 'rhino'), ('744 760 95 595 1 142 615 615', 'bull'),
         ('235 705 33 845 407 321 407', 'hare')]
PAT = {'goat': r'goat|markhor|ibex', 'rhino': r'rhino', 'hare': r'\bhare|rabbit', 'bull': r'\bbull|\bcow|\box\b|cattle|zebu'}


def main():
    out = ['# The copper-tablet gate', '', '| key | anchor signs (right / covered) | anchor texts naming their picture | verdict |', '|---|---|---|---|']
    for p in sorted(p for p in glob.glob(os.path.join(HERE, 'keys', '*.tsv')) if not p.endswith('_raw.tsv')):
        meta, key, gloss = bench.load_key(p)
        cov = [(s, re.search(PAT[a], gloss.get(s, '').lower()) is not None) for s, a in SIGNS.items() if s in key]
        th = [(t, any(re.search(PAT[a], gloss.get(g, '').lower()) for g in t.split())) for t, a in TEXTS if any(g in key for g in t.split())]
        right = sum(ok for s, ok in cov)
        verdict = 'untested (covers no anchor sign)' if not cov else ('passes' if right == len(cov) else 'fails')
        out.append('| %s | %d / %d | %d of %d covered | %s |' % (meta.get('title', os.path.basename(p))[:60], right, len(cov), sum(ok for t, ok in th), len(th), verdict))
    out += ['', "Parpola's later readings (rebus/parpola_later.tsv) name no anchor sign (749, 341, 753, the lens sign): untested.", '']
    open(os.path.join(HERE, 'results', 'gate.md'), 'w', encoding='utf-8').write('\n'.join(out))
    print('\n'.join(out))


if __name__ == '__main__':
    main()
