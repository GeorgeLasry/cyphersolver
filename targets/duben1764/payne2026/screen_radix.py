"""Bounded base-9 indexing/affine screen; table membership alone is not a reading."""
import numpy as np,json,math
from pathlib import Path
r=Path(__file__).resolve().parent
counts={int(a):int(b) for a,b in (ln.split() for ln in (r/'permutation_frequencies.txt').read_text().splitlines())}
u=np.array(list(counts));cnt=np.array(list(counts.values()));out=[]
for sheet in [218,220]:
 key={}
 for ln in (r/f'key{sheet}.txt').read_text().splitlines():
  if ln and not ln.startswith('#'):
   raw,v=ln.split(maxsplit=1)
   if len(raw)==3 and '0' not in raw:
    a,b,c=map(int,raw);k=(a-1)*81+(b-1)*9+c-1
    key[k]=key.get(k,'')+('/' if k in key else '')+v
 mask=np.array([int(i in key) for i in range(729)])
 best=[]
 for a in range(729):
  if math.gcd(a,729)!=1:continue
  vals=(a*u[None,:]+np.arange(729)[:,None])%729;scores=mask[vals]@cnt
  for b in np.argsort(scores)[-2:]:best.append((int(scores[b]),a,int(b)))
 for hits,a,b in sorted(best,reverse=True)[:10]:
  preview=[]
  for ln in (r/'image107_cipher.txt').read_text().splitlines():
   if ln and not ln.startswith('#'):
    preview.append(' '.join(key.get((a*int(t.rstrip('?'))+b)%729,'['+t+']') for t in ln.split(':',1)[1].split()))
  out.append({'sheet':sheet,'hits':hits,'groups':sum(counts.values()),'a':a,'b':b,'preview':preview})
(r/'radix_screens.json').write_text(json.dumps(out,indent=2)+'\n')
for sheet in [218,220]:
 row=next(o for o in out if o['sheet']==sheet);print(sheet,row['hits'],row['groups'],row['a'],row['b'],row['preview'][0])
