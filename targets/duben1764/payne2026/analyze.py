"""Audit the preliminary transcription and apply ONLY attested key samples.
Run: python3 targets/duben1764/analyze.py
This is a lookup diagnostic, not a cryptanalytic solver or plaintext reading.
"""
from pathlib import Path
import csv, json, collections
root = Path(__file__).resolve().parent
lines = []
for line in (root/'image107_cipher.txt').read_text().splitlines():
    if line and not line.startswith('#'):
        label, text = line.split(':', 1)
        lines.append((label, text.split()))
tokens = [t for _, ts in lines for t in ts]
certain = [t for t in tokens if '?' not in t]
keys = collections.defaultdict(dict)
for row in csv.DictReader((root/'key_samples.tsv').open(), delimiter='\t'):
    if row['grade'] == 'H':
        keys[row['image']][row['code']] = row['value']
# Positive control for lookup/line alignment only; no solver was run.
for k in keys.values():
    sample = list(k)[:8]
    expected = [k[x] for x in sample]
    assert [k.get(x, f'[{x}]') for x in sample] == expected
report = {'lines':len(lines), 'tokens':len(tokens),
          'uncertain_tokens':len(tokens)-len(certain),
          'distinct_certain_tokens':len(set(certain)),
          'range_certain':[min(map(int,certain)), max(map(int,certain))],
          'frequencies':collections.Counter(certain).most_common(),
          'reading_obtained':False, 'fraction_coherent':0,
          'warning':'Partial key samples: lookup coverage is NOT full-key coverage or sense coverage.'}
(root/'statistics.json').write_text(json.dumps(report, indent=2)+'\n')
out = ['# Attested-key sample diagnostics', '',
       'Only H-grade entries in key_samples.tsv are substituted. Brackets are unresolved cipher tokens.',
       'These strings are NOT decipherments. Missing sample values do not prove the full key lacks a code.', '']
for image,k in keys.items():
    out += [f'## Key sheet image {image}', '']
    for label,ts in lines:
        out.append(label+': '+' | '.join(k.get(t, f'[{t}]') for t in ts))
    out.append('')
(root/'key_diagnostics.md').write_text('\n'.join(out).rstrip()+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='frequencies'},indent=2))
