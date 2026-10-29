"""Experimental known-plaintext syllable aligner.
Beam search is incomplete; only a consistent alignment plus independent validation could establish a key.
Unique-occurrence key entries are merged away during search and reconstructed from the chosen path.
"""
import json,re,unicodedata,collections,math,sys,time
from pathlib import Path
r=Path(__file__).resolve().parent
norm=lambda s:re.sub('[^a-z]','',unicodedata.normalize('NFD',s.lower()))
def align(ts,p,beam=15000,timeout=50):
 counts=collections.Counter(ts);last={c:max(i for i,t in enumerate(ts) if t==c) for c in counts}
 mins=[sum(int(z)>100 for z in ts[j:]) for j in range(len(ts)+1)]
 remaining=counts.copy(); states=[(0.,0,(),())];start=time.monotonic();bestpos=0
 # Score plausible code values without inventing target-specific plaintext.
 inventory=set('abcdefghijklmnopqrstuvwxyz')
 for ln in (r/'key218.txt').read_text().splitlines():
  if ln and not ln.startswith('#'):
   v=ln.split(maxsplit=1)[1]
   if len(v)<=4 and '?' not in v:inventory.add(norm(v))
 source_text=json.loads((r/'image126_pair.json').read_text())['plaintext']
 words={norm(w) for w in re.findall('[a-zA-Z]+',source_text)}
 def prior(v):
  if not v:return -.8
  if v in words:return -.12
  if v in inventory:return -.15*len(v)
  # Explicitly allow any written substring, but prefer normal syllable shapes.
  vowels=sum(c in 'aeiouy' for c in v)
  if len(v)<=4 and 0<vowels<len(v):return -.7-.12*len(v)
  return -1.5-.2*len(v)
 for i,t in enumerate(ts):
  remaining[t]-=1;islast=last[t]==i;nxt={};freq=remaining[t]+1
  for score,pos,km,path in states:
   key=dict(km)
   if t in key:
    val=key[t];opts=[val] if p.startswith(val,pos) else []
   else:
    opts=[]
    if int(t)<=100:opts.append('')
    for n in range(1,min(13,len(p)-pos)+1):
     v=p[pos:pos+n]
     if freq>1 and p[pos:].count(v)<freq:continue
     opts.append(v)
   for val in opts:
    q=pos+len(val);left=len(ts)-i-1
    if q+13*left<len(p):continue
    if q>len(p):continue
    # Allow ordinary small numeric nulls; every larger code must contribute.
    minimum=mins[i+1]
    if q+minimum>len(p):continue
    nk=dict(key)
    if not islast:nk[t]=val
    else:nk.pop(t,None)
    ks=tuple(sorted(nk.items()));newscore=score+(prior(val) if t not in key else .5*len(val))
    # Position heuristic used only to prioritize, never as a validity rule.
    rank=newscore-.012*(q-len(p)*(i+1)/len(ts))**2
    label=(q,ks)
    if label not in nxt or rank>nxt[label][0]:nxt[label]=(rank,newscore,q,ks,path+(val,))
  if not nxt:return {'status':'no_alignment_in_beam','step':i,'max_position':bestpos,'elapsed':time.monotonic()-start}
  ranked=sorted(nxt.values(),reverse=True)[:beam]
  states=[(sc,q,ks,path) for rank,sc,q,ks,path in ranked];bestpos=max(q for sc,q,ks,path in states)
  if i%10==0:print(i,len(states),bestpos,round(time.monotonic()-start,1),flush=True)
  if time.monotonic()-start>timeout:return {'status':'timeout','step':i,'max_position':bestpos,'elapsed':time.monotonic()-start}
 for sc,q,km,path in sorted(states,reverse=True):
  if q==len(p):
   key={}
   for t,v in zip(ts,path):
    assert t not in key or key[t]==v;key[t]=v
   assert ''.join(key[t] for t in ts)==p
   return {'status':'consistent_alignment','key':key,'values':path,'score':sc,'elapsed':time.monotonic()-start}
 return {'status':'incomplete','max_position':bestpos,'elapsed':time.monotonic()-start}
if __name__=='__main__':
 x=json.loads((r/'image126_pair.json').read_text());p=norm(x['plaintext']);ts=' '.join(x['cipher_lines'][:-int(sys.argv[2])] if len(sys.argv)>2 and int(sys.argv[2]) else x['cipher_lines']).split()
 out=align(ts,p,int(sys.argv[1]) if len(sys.argv)>1 else 10000)
 (r/('beam126_result_'+(sys.argv[2] if len(sys.argv)>2 else 'all')+'.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['key','values']},indent=2))
