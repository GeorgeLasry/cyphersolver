"""Build the three lexicons used by bench.py / anchors_bench.py / equation_rebus.py from the raw downloads.

Raw downloads (data/lexicons/raw/, see data/lexicons/README.md):
  raw/mw/mw.txt                csl-orig Monier-Williams, already in the <L>...<LEND> format bench parses
  raw/dedr/forms.csv           Dravidian Database v1.1 CLDF forms (Zenodo 22286173)
  raw/dedr/dedr_entry_v11.csv  Dravidian Database v1.1 lemma table (read by bench.dedr_glosses)
  raw/epsd2/epsd2.zip          Oracc ePSD2 JSON (gloss-sux.json -> sux_gloss.tsv: cf, gw, pos, senses)

Usage: python -I build_lexicons.py [data/lexicons]
"""
import csv
import json
import os
import shutil
import sys
import zipfile


def sux_gloss(zpath, out):
    with zipfile.ZipFile(zpath) as z, z.open('epsd2/gloss-sux.json') as f:
        d = json.load(f)
    n = 0
    with open(out, 'w', encoding='utf-8', newline='') as fo:
        w = csv.writer(fo, delimiter='\t')
        w.writerow(['cf', 'gw', 'pos', 'senses'])
        for e in d.get('entries', []):
            w.writerow([e.get('cf', ''), e.get('gw', ''), e.get('pos', ''),
                        ' | '.join(s.get('mng', '') for s in e.get('senses', []) if 'mng' in s)])
            n += 1
    return n


def main(base='data/lexicons'):
    raw = os.path.join(base, 'raw')
    shutil.copyfile(os.path.join(raw, 'mw', 'mw.txt'), os.path.join(base, 'mw.txt'))
    for fn in ('forms.csv', 'dedr_entry_v11.csv'):
        shutil.copyfile(os.path.join(raw, 'dedr', fn), os.path.join(base, fn))
    n = sux_gloss(os.path.join(raw, 'epsd2', 'epsd2.zip'), os.path.join(base, 'sux_gloss.tsv'))
    print('sux entries', n)


if __name__ == '__main__':
    main(*sys.argv[1:2])
