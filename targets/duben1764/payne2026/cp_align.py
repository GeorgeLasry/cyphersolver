"""Exact finite-domain known-plaintext alignment under a fixed syllabary model.
Requires ortools. Timeout is UNKNOWN, not rejection. No historical model is accepted as a key.
"""
from pathlib import Path
import json,re,unicodedata,collections,sys,time
from ortools.sat.python import cp_model
r=Path(__file__).resolve().parent
norm=lambda s: re.sub('[^a-z]','',unicodedata.normalize('NFD',s.lower()))
def solve(ts,p,seconds=45,maxpiece=12,skip=0,tail=0,lexical=False):
 ts=ts[skip:len(ts)-tail if tail else len(ts)];n=len(ts);m=len(p);start=time.monotonic()
 pieces={'':0}; triples=[]
 for a in range(m+1):
  for b in range(a,min(m,a+maxpiece)+1):
   v=p[a:b];pieces.setdefault(v,len(pieces));triples.append((a,b,pieces[v]))
 inverse={v:k for k,v in pieces.items()};freq=collections.Counter(ts)
 inventory=set('abcdefghijklmnopqrstuvwxyz')
 for sheet in (218,219,220):
  for ln in (r/f'key{sheet}.txt').read_text().splitlines():
   if ln and not ln.startswith('#'):
    value=ln.split(maxsplit=1)[1]
    if '?' not in value:
     for v in value.split(','):
      if '_' not in v and len(v)<=5:inventory.add(norm(v))
 inventory.update(norm(w) for w in re.findall('[a-zA-Z]+',json.loads((r/'image126_pair.json').read_text())['plaintext']))
 if lexical: triples=[(a,b,v) for a,b,v in triples if not v or inverse[v] in inventory]
 # A piece must occur at least as often as its code. Count overlapping occurrences.
 pc={v:sum(p.startswith(v,i) for i in range(m+1)) if v else n for v in pieces}
 model=cp_model.CpModel();pos=[model.new_int_var(0,m,f'p{i}') for i in range(n+1)]
 model.add(pos[0]==0);model.add(pos[-1]==m)
 key={t:model.new_int_var(0,len(pieces)-1,'v'+t) for t in freq}
 repeated={t for t in freq if freq[t]>1};cache={}
 for i,t in enumerate(ts):
  nullable=int(t)<=100
  # Unique symbols need only a bounded length; no value variable is necessary.
  if t not in repeated and not lexical:
   model.add(pos[i+1]>=pos[i]+(0 if nullable else 1));model.add(pos[i+1]<=pos[i]+maxpiece)
  else:
   ck=(freq[t],nullable)
   if ck not in cache:cache[ck]=[(a,b,v) for a,b,v in triples if (nullable or b>a) and pc[inverse[v]]>=freq[t]]
   model.add_allowed_assignments([pos[i],pos[i+1],key[t]],cache[ck])
 solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=seconds;solver.parameters.num_search_workers=4
 status=solver.solve(model);out={'status':solver.status_name(status),'seconds':time.monotonic()-start,'groups':n,'letters':m,'skip_groups':skip,'tail_groups':tail,'maxpiece':maxpiece,'lexical':lexical,'model':'Each code has one fixed contiguous written value; codes<=100 may be empty.'}
 if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
  values=[p[solver.value(pos[i]):solver.value(pos[i+1])] for i in range(n)];k={}
  for t,v in zip(ts,values):assert t not in k or k[t]==v;k[t]=v
  assert ''.join(k[t] for t in ts)==p
  out.update(key=k,values=values,warning='Consistent formal alignment only; historical validation still required.')
 return out
if __name__=='__main__':
 mode=sys.argv[1];x=json.loads((r/('beam_control_input.json' if mode.startswith('control') else 'image126_pair.json')).read_text())
 ts=x['cipher'] if mode.startswith('control') else ' '.join(x['cipher_lines']).split();p=norm(x['plaintext'])
 out=solve(ts,p,seconds=float(sys.argv[2]) if len(sys.argv)>2 else 45,skip=int(sys.argv[3]) if len(sys.argv)>3 else 0,tail=int(sys.argv[4]) if len(sys.argv)>4 else 0,lexical=mode.endswith('lex'))
 if mode.startswith('control') and 'key' in out:
  out['token_value_accuracy']=sum(out['key'][t]==x['true_key'][t] for t in ts)/len(ts);out['usable_for_key_recovery']=out['token_value_accuracy']>=.95
 (r/f'cp_{mode}_{out["skip_groups"]}_{out["tail_groups"]}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('key','values')},indent=2),flush=True)
