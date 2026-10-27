"""Build validation.tsv and reading.tsv from the ct_*.txt files: each pair with its key value (key.txt), and
the intended letter where the sense shows that the writer took a neighbouring cell (FIX below)."""
import re
from decode import val
# segment as deciphered by the key -> segment as intended (same length); only segments with a slip
FIX = {'col': 'con', 'secundnm': 'secundum', 'connci': 'consci', 'ertiam': 'entiam', 'rbdsuxoris': 'rbusuxoris',
       'lsreg': 'isreg', 'onsrliisiuven': 'onsiliisiuven', 'msubdido': 'msubdito', 'subdidoru': 'subditoru',
       'defectul': 'defectus', 'fiuelita': 'fidelita', 'entiertoffensione': 'entieetoffensione',
       'hecoonia': 'hecomnia', 'derebeschafmenhei': 'derebeschaffenhei', 'nitznbe': 'nitzube',
       'ionorumdiviaio': 'bonorumdivisio', 'unsirs': 'unsers', 'mutationns': 'mutationes'}
rows, nfix, ntok = [], 0, 0
for f in ['ct_004.txt', 'ct_003.txt', 'ct_006.txt']:
    for line in open(f, encoding='utf8'):
        if line.startswith('#') or not line.strip():
            continue
        lab = line.split()[0]
        for part in re.split(r'\{[^}]*\}|\[X\]|\|', line[len(lab):]):
            t = [(int(a), int(b)) for a, b in re.findall(r'(\d+),(\d+)', part)]
            if not t:
                continue
            got = ''.join(val(a, b) for a, b in t)
            want = FIX.get(got, got)
            assert len(want) == len(got), got
            for (a, b), g, w in zip(t, got, want):
                rows.append((f, lab, f'{a},{b}', g, w))
                ntok += 1
                nfix += g != w
with open('validation.tsv', 'w', encoding='utf8') as o:
    o.write('# model: la\n# source: ct_004.txt, ct_003.txt, ct_006.txt deciphered with key.txt\n')
    o.write('# note: reading = intended letter; where the writer took a neighbouring key cell the intended letter is given\n')
    for f, lab, c, g, w in rows:
        o.write(f'{c}\t{w}\n')
with open('reading.tsv', 'w', encoding='utf8') as o:
    o.write('file\tline\tpair\tkey_value\tintended\n')
    for r in rows:
        o.write('\t'.join(r) + '\n')
print(ntok, 'pairs,', nfix, 'read with the intended letter differing from the key value')
