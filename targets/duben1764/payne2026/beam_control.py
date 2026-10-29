"""Same-length variable-value substitution control for the exploratory aligner.
Success requires recovering original per-token values, not merely matching the known text.
"""
import json,random,re,unicodedata,collections
from pathlib import Path
from beam_align import align,norm
r=Path(__file__).resolve().parent
x=json.loads((r/'image126_pair.json').read_text());p=norm(x['plaintext']);cts=' '.join(x['cipher_lines']).split();N=len(cts);S=len(set(cts));rng=random.Random(450)
inv=set('abcdefghijklmnopqrstuvwxyz')
for l in (r/'key218.txt').read_text().splitlines():
 if l and not l.startswith('#'):
  v=l.split(maxsplit=1)[1]
  if len(v)<=4 and '?' not in v:inv.add(norm(v))
# Include complete French words, as a nomenclator can.
inv.update(norm(w) for w in re.findall('[a-zA-Z]+',x['plaintext']))
options={j:[v for v in inv if v and p.startswith(v,j)] for j in range(len(p))}
dp={(len(p),0)}
for j in range(len(p)-1,-1,-1):
 for n in range(1,N+1):
  if any((j+len(v),n-1) in dp for v in options[j]):dp.add((j,n))
assert (0,N) in dp
segments=[];j=0
while len(segments)<N:
 opts=[v for v in options[j] if (j+len(v),N-len(segments)-1) in dp];opts.sort();v=rng.choice(opts);segments.append(v);j+=len(v)
vals=sorted(set(segments));assert len(vals)<=S
pool=sorted(set(cts),key=int);rng.shuffle(pool);key={pool[i]:v for i,v in enumerate(vals)};byval=collections.defaultdict(list)
for c,v in key.items():byval[v].append(c)
for c in pool[len(vals):]:
 eligible=[v for v in vals if len(byval[v])<segments.count(v)]
 v=rng.choice(eligible);key[c]=v;byval[v].append(c)
# Ensure every chosen code occurs at least once, where enough homophones exist.
queues={v:list(cs) for v,cs in byval.items()};ts=[]
for v in segments:
 q=queues[v];ts.append(q.pop() if q else rng.choice(byval[v]))
control={'plaintext':x['plaintext'],'cipher':ts,'true_key':key,'groups':N,'distinct_actual':len(set(ts)),'distinct_target':S,'seed':450}
(r/'beam_control_input.json').write_text(json.dumps(control,indent=2)+'\n')
out=align(ts,p,5000,55)
if out['status']=='consistent_alignment':
 out['token_value_accuracy']=sum(out['key'][t]==key[t] for t in ts)/N
 out['usable']=out['token_value_accuracy']>=.95
else:out['usable']=False
(r/'beam_control_result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['key','values']},indent=2))
