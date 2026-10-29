"""Test fixed one/two-digit letter-code hypothesis against the interlinear passage.
This hypothesis is distinct from a three-digit syllable substitution.
"""
import json,re,unicodedata,sys
from pathlib import Path
import z3
r=Path(__file__).resolve().parent;x=json.loads((r/'image126_pair.json').read_text())
p=re.sub('[^a-z]','',unicodedata.normalize('NFD',x['plaintext'].lower()))
cs=''.join(''.join(x['cipher_lines']).split())
drop=int(sys.argv[1]);cs=cs.replace('0','') if drop else cs
s=z3.Solver();s.set(timeout=45000)
v={c:z3.String('c'+c) for c in set(p)}
for y in v.values():s.add(z3.Length(y)>=1,z3.Length(y)<=2)
# Allow limited padding around the paragraph; preserve every interior digit.
pre=z3.String('pre');post=z3.String('post');s.add(z3.Length(pre)<=12,z3.Length(post)<=12)
s.add(z3.Concat(pre,*[v[c] for c in p],post)==cs)
print('remove_zeros',drop,'chars',len(p),'digits',len(cs),flush=True)
res=s.check();print(res,flush=True)
if res==z3.sat:
 m=s.model();print({c:str(m.eval(v[c])) for c in v})
