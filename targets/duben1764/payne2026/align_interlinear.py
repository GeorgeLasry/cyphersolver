from pathlib import Path
import json,re,unicodedata,sys,time
import z3
r=Path(__file__).resolve().parent
x=json.loads((r/'image126_pair.json').read_text())
p=re.sub('[^a-z]','',unicodedata.normalize('NFD',x['plaintext'].lower()))
ts=' '.join(x['cipher_lines']).split()
s=z3.Solver();s.set(timeout=45000)
v={t:z3.String('v'+t) for t in set(ts)}
for t,val in v.items():s.add(z3.Length(val)>=(0 if int(t)<=100 else 1),z3.Length(val)<=10)
# Ignore the final two padding-looking numbers as a hypothesis, not a fact.
s.add(z3.Concat(*[v[t] for t in ts[:-2]])==p)
print('chars',len(p),'groups',len(ts),flush=True)
a=s.check();print(a,flush=True)
if a==z3.sat:
 m=s.model();out={t:m.eval(val).as_string() for t,val in v.items()};print(json.dumps(out,indent=2));(r/'interlinear_provisional_model.json').write_text(json.dumps(out,indent=2))
