"""Wells 1998 sign -> ICIT glyph by object intersection (set 394): for each Wells sign, the ICIT glyph present on the
largest share of the CISI objects Wells lists for it (data/wells/wells1998_signs.tsv), matched to the ICIT records by
CISI number (record field 1). Writes data/wells/wells_icit_concordance.tsv."""
import csv
import os
from collections import Counter, defaultdict

import icit_full
import rtools as R

HERE = os.path.dirname(os.path.abspath(__file__))


def icit_by_cisi():
    out = defaultdict(set)
    for rec in icit_full.records(R.FPATH):
        c = str(rec[1]).strip()
        if c and c != '-':
            for ln in icit_full.lines_of(rec[34]):
                out[c].update(g for g in ln['signs'] if g and g != '?')
    return out


def wells_signs():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'data', 'wells', 'wells1998_signs.tsv'), encoding='utf-8'), delimiter='\t'))
    return {r['wells_sign']: [o.strip() for o in r['cisi_objects'].split(',') if o.strip()] for r in rows}


def concordance(min_objects=3):
    by = icit_by_cisi()
    out = {}
    for w, objs in wells_signs().items():
        found = [by[o] for o in objs if o in by]
        if len(found) < min_objects:
            continue
        c = Counter(g for s in found for g in s)
        g, n = c.most_common(1)[0]
        out[w] = (g, n / len(found), len(found), len(objs))
    return out


if __name__ == '__main__':
    con = concordance()
    with open(os.path.join(HERE, 'data', 'wells', 'wells_icit_concordance.tsv'), 'w', encoding='utf-8', newline='') as f:
        f.write('wells_sign\ticit\tshare\tobjects_found\tobjects_listed\n')
        for w, (g, s, n, m) in sorted(con.items()):
            f.write('%s\t%s\t%.2f\t%d\t%d\n' % (w, g, s, n, m))
    print(len(con), 'signs;', sum(1 for v in con.values() if v[1] >= 0.8), 'with share >= 0.8')
