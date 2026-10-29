"""Screen explicitly bounded numeric recodings by key-table coverage only.
A coverage hit is not a reading. Key values are not changed to improve results.
"""
from pathlib import Path
import numpy as np,json,collections,math
r=Path(__file__).resolve().parent
k={}
for line in (r/'key218.txt').read_text().splitlines():
 if line and not line.startswith('#'):
  c,v=line.split(maxsplit=1); k[int(c)]=k.get(int(c),'')+('/' if int(c) in k else '')+v
xs=[]
for ln in (r/'image107_cipher.txt').read_text().splitlines():
 if ln and not ln.startswith('#'):xs += [int(t.rstrip('?')) for t in ln.split(':',1)[1].split() if '?' not in t]
x=np.array(xs);u,c=np.unique(x,return_counts=True);mask=np.array([int(i in k) for i in range(1000)])
best=[]
for a in range(1,1000):
 if math.gcd(a,1000)!=1:continue
 vals=(a*u[None,:]+np.arange(1000)[:,None])%1000
 hits=mask[vals]@c
 for b in np.argsort(hits)[-3:]: best.append((int(hits[b]),a,int(b)))
best=sorted(best,reverse=True)[:20]
rows=[]
for hits,a,b in best:
 rows.append({'hits':hits,'tokens':len(x),'a':a,'b':b,'preview':' '.join(k.get((a*int(z)+b)%1000,'['+str((a*int(z)+b)%1000)+']') for z in x[:70])})
(r/'arithmetic218.json').write_text(json.dumps(rows,indent=2)+'\n')
for row in rows[:5]:print(row)
