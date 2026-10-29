"""Exact repeat-consistency test, not a plaintext generator.
Requires z3-solver. No values should be accepted without image/linguistic review.
"""
import sys,json,re,unicodedata
from pathlib import Path
import z3
root=Path(__file__).resolve().parent
norm=lambda t: re.sub('[^a-z]','',unicodedata.normalize('NFD',t.lower()))
ts=[]
for ln in (root/'image096_cipher.txt').read_text().splitlines():
 if ln and not ln.startswith('#'): ts.extend(ln.split(':',1)[1].split())
name=sys.argv[1];n=int(sys.argv[2]);skip=int(sys.argv[3]) if len(sys.argv)>3 else 0
p=norm(json.load((root/'adjacent_candidates.json').open())[name]);ts=ts[skip:skip+n]
s=z3.Solver();s.set(timeout=45000)
v={t:z3.String('v'+t.replace('?','q')) for t in set(ts)}
for t,x in v.items():
 s.add(z3.Length(x)>= (0 if int(t.rstrip('?'))<100 else 1),z3.Length(x)<=16)
s.add(z3.PrefixOf(z3.Concat(*[v[t] for t in ts]),p))
result=s.check();print(name,n,skip,result,flush=True)
if result==z3.sat:
 m=s.model();print([(t,m.eval(v[t])) for t in ts]);print(m.eval(z3.Concat(*[v[t] for t in ts])))
