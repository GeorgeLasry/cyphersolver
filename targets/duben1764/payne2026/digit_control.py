"""Exhaustive 1/2-digit monoalphabetic encoding check with synthetic positive control.
Allows 0..12 padding digits at either end. Does not model homophones or bad transcription.
"""
import json,re,unicodedata,random
from pathlib import Path
r=Path(__file__).resolve().parent
x=json.loads((r/'image126_pair.json').read_text())
p=re.sub('[^a-z]','',unicodedata.normalize('NFD',x['plaintext'].lower()))
cs=''.join(''.join(x['cipher_lines']).split())
def solve(p,cs):
 nodes=0
 def dfs(i,j,m):
  nonlocal nodes
  nodes+=1
  if i==len(p):return dict(m) if len(cs)-j<=12 else None
  if len(cs)-j<len(p)-i or len(cs)-j>2*(len(p)-i)+12:return
  c=p[i]
  if c in m:
   v=m[c]
   return dfs(i+1,j+len(v),m) if cs.startswith(v,j) else None
  for ln in (1,2):
   v=cs[j:j+ln]
   if len(v)<ln:continue
   m[c]=v
   ans=dfs(i+1,j+ln,m)
   if ans is not None:return ans
  m.pop(c,None)
 for off in range(13):
  ans=dfs(0,off,{})
  if ans is not None:return {'match':True,'offset':off,'mapping':ans,'nodes':nodes}
 return {'match':False,'nodes':nodes}
rng=random.Random(450);alphabet=sorted(set(p));mapping={c:('9'+str(i) if i<10 else str(i)) for i,c in enumerate(alphabet)}
# A same-length plaintext, one/two digit alphabet, and explicit padding control.
# Use a prefix-free construction with eight common single-digit letters.
common='esaitnru';digits='01234567';mapping={c:d for c,d in zip(common,digits)}
others=[c for c in alphabet if c not in mapping]
for i,c in enumerate(others):mapping[c]=str(8+i//10)+str(i%10)
control='450'+''.join(mapping[c] for c in p)+'32'
ctrl=solve(p,control);assert ctrl['match']
results={'control':ctrl,'retain_zeros':solve(p,cs),'discard_zeros':solve(p,cs.replace('0','')),
'limitation':'Rejects only an exact fixed 1/2-digit letter code on these provisional texts, not the historical cipher.'}
(r/'digit_control_results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
