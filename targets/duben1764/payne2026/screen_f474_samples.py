"""Partial primary-key fingerprints only, NOT a cryptanalytic solver or exclusion.
Source PDF pages refer to Uppsala F474, Alvin record164482,39th attachment PDF.
"""
from pathlib import Path
import csv,collections,json
r=Path(__file__).resolve().parent
samples=list(csv.DictReader((r/'f474_key_samples.tsv').open(),delimiter='\t'));keys=collections.defaultdict(dict)
for row in samples:keys[row['family']][row['code']]=row['value']
frequencies=dict(json.loads((r/'letter_statistics.json').read_text())['frequencies'])
top=[c for c,n in sorted(frequencies.items(),key=lambda z:-z[1])[:8]]
results=[]
for family,key in keys.items():
 selected={t:key.get(t,'['+t+']') for t in top}
 results.append({'family':family,'top_group_fingerprint':selected,'warning':'Partial sample lookup only. No accepted reading; alternate transforms, polyphony, null rules and untranscribed values remain open.'})
assert keys['clavis']['578']=='ob' and keys['lary']['578']=='Parme'
(r/'f474_fingerprints.json').write_text(json.dumps(results,indent=2)+'\n')
for row in results:print(row['family'],row['top_group_fingerprint'])
