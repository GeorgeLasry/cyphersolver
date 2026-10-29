"""Literal and zero-stripped table lookup, with explicit offsets; not a solver.
A self-enciphered control verifies the lookup mechanism, not the historical key.
"""
from pathlib import Path
import re,json
r=Path(__file__).resolve().parent
keys={}
for sheet in (218,219,220):
 k={}
 for ln in (r/f'key{sheet}.txt').read_text().splitlines():
  if ln and not ln.startswith('#'):
   raw,v=ln.split(maxsplit=1)
   if raw.isdigit():k.setdefault(int(raw),[]).append(v)
 keys[sheet]=k
rows=[]
for image in (105,106,107,108):
 tokens=[]
 for ln in (r/f'image{image}_cipher.txt').read_text().splitlines():
  if ln and not ln.startswith('#'):tokens.extend(ln.split(':',1)[1].split())
 for sheet,key in keys.items():
  certain=[int(t) for t in tokens if t.isdigit()]
  found=[t for t in certain if t in key]
  rows.append(dict(image=image,sheet=sheet,mode='literal groups',total=len(certain),hits=len(found),preview=' '.join('/'.join(key[int(t)]) if t.isdigit() and int(t) in key else '['+t+']' for t in tokens[:45])))
  digits=''.join(t.rstrip('?') for t in tokens).replace('0','')
  for offset in range(3):
   groups=[int(digits[i:i+3]) for i in range(offset,len(digits)-2,3)]
   rows.append(dict(image=image,sheet=sheet,mode=f'delete zero, offset {offset}',total=len(groups),hits=sum(t in key for t in groups),preview=' '.join('/'.join(key[t]) if t in key else '['+str(t)+']' for t in groups[:45]),warning='Uses provisional digits, including uncertain groups; no validated French reading.'))
# Removing seven initial digits only changes regrouping phase by one; each phase covered.
controls={}
for sheet,key in keys.items():
 codes=[c for c,v in key.items() if len(v)==1 and '?' not in v[0]][:30]
 encoded=''.join(str(c) for c in codes)
 recovered=[int(encoded[i:i+3]) for i in range(0,len(encoded),3)]
 assert recovered==codes
 controls[sheet]=dict(groups=len(codes),passed=True,scope='literal lookup only; codes are three digits')
(r/'table_comparison.json').write_text(json.dumps(dict(controls=controls,results=rows),indent=2)+'\n')
for row in rows:
 if row['image']==107: print(row['sheet'],row['mode'],str(row['hits'])+'/'+str(row['total']),row['preview'][:140])
