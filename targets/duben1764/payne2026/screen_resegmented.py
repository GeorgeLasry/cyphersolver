"""Bounded coverage screen: remove zeros, regroup triples, then affine recode.
No text is accepted from coverage alone. Every transformation is recorded.
"""
from pathlib import Path
import numpy as np,json,math
r=Path(__file__).resolve().parent
key={}
for line in (r/'key218.txt').read_text().splitlines():
 if line and not line.startswith('#'):
  c,v=line.split(maxsplit=1);key[int(c)]=key.get(int(c),'')+('/' if int(c) in key else '')+v
mask=np.array([int(i in key) for i in range(1000)])
source=json.loads((r/'image126_pair.json').read_text());digits=''.join(''.join(source['cipher_lines']).split()).replace('0','')
rows=[]
for off in range(3):
 x=np.array([int(digits[i:i+3]) for i in range(off,len(digits)-2,3)])
 u,c=np.unique(x,return_counts=True)
 best=[]
 for a in range(1,1000):
  if math.gcd(a,1000)!=1:continue
  vals=(a*u[None,:]+np.arange(1000)[:,None])%1000;hits=mask[vals]@c
  for b in np.argsort(hits)[-2:]:best.append((int(hits[b]),a,int(b)))
 for hits,a,b in sorted(best,reverse=True)[:10]:
  rows.append({'offset':off,'hits':hits,'groups':len(x),'a':a,'b':b,'text':' '.join(key.get((a*int(z)+b)%1000,'['+str((a*int(z)+b)%1000)+']') for z in x)})
(r/'resegmented218.json').write_text(json.dumps(rows,indent=2)+'\n')
for row in sorted(rows,key=lambda row:-row['hits']/row['groups'])[:3]:print(row)
