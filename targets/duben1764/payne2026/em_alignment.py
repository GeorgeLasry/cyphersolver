"""Exploratory EM alignment for variable-length substitution, with controls.
A high score is not a decipherment. Low-frequency values require independent validation.
The stochastic emissions tolerate inconsistent values but make no claim those inconsistencies are historical polyphony.
"""
import numpy as np,json,re,unicodedata,collections,sys,time
from pathlib import Path
r=Path(__file__).resolve().parent
norm=lambda s:re.sub('[^a-z]','',unicodedata.normalize('NFD',s.lower()))
def fit(ts,text,seed=450,iters=30):
 p=norm(text);L=len(p);N=len(ts);K=12;rng=np.random.default_rng(seed)
 syms=sorted(set(ts));si={t:i for i,t in enumerate(syms)};ct=[si[t] for t in ts]
 vocab=['']+sorted({p[j:j+k] for k in range(1,K+1) for j in range(L-k+1)})
 vi={v:i for i,v in enumerate(vocab)};V=len(vocab)
 inv=set('abcdefghijklmnopqrstuvwxyz')
 for ln in (r/'key218.txt').read_text().splitlines():
  if ln and not ln.startswith('#'):
   v=ln.split(maxsplit=1)[1]
   if len(v)<=4 and '?' not in v:inv.add(norm(v))
 words={norm(w) for w in re.findall('[a-zA-Z]+',text)}
 prior=np.array([.02 if not v else (1. if v in words else .7 if v in inv else .05)*np.exp(-.3*len(v)) for v in vocab])
 probs=np.tile(prior,(len(syms),1))*np.exp(rng.normal(0,.2,(len(syms),V)))
 for i,t in enumerate(syms):
  if int(t)>100:probs[i,0]=0
 probs/=probs.sum(1,keepdims=True)
 # Each step length has its own substring-ID vector over possible positions.
 starts=[np.arange(L-k+1) for k in range(K+1)]
 ids=[np.zeros(L+1,dtype=int)]+[np.array([vi[p[j:j+k]] for j in range(L-k+1)]) for k in range(1,K+1)]
 def passes(logp):
  F=np.full((N+1,L+1),-np.inf);F[0,0]=0
  for i,t in enumerate(ct):
   for k in range(K+1):
    j=starts[k];v=ids[k]
    F[i+1,j+k]=np.logaddexp(F[i+1,j+k],F[i,j]+logp[t,v])
  B=np.full((N+1,L+1),-np.inf);B[N,L]=0
  for i in range(N-1,-1,-1):
   t=ct[i]
   for k in range(K+1):
    j=starts[k];v=ids[k]
    B[i,j]=np.logaddexp(B[i,j],logp[t,v]+B[i+1,j+k])
  return F,B
 for it in range(iters):
  with np.errstate(divide='ignore'):logp=np.log(probs)
  F,B=passes(logp);Z=F[N,L];counts=np.zeros_like(probs)
  for i,t in enumerate(ct):
   for k in range(K+1):
    j=starts[k];v=ids[k]
    mass=np.exp(F[i,j]+logp[t,v]+B[i+1,j+k]-Z)
    np.add.at(counts[t],v,mass)
  # Sparsity-promoting sharpening; calibrated on synthetic controls below.
  probs=(counts+.003*prior)**1.15
  for i,t in enumerate(syms):
   if int(t)>100:probs[i,0]=0
  probs/=probs.sum(1,keepdims=True)
 with np.errstate(divide='ignore'):logp=np.log(probs)
 F=np.full((N+1,L+1),-np.inf);F[0,0]=0;back=np.zeros((N+1,L+1),dtype=np.int16)
 for i,t in enumerate(ct):
  for k in range(K+1):
   j=starts[k];v=ids[k];z=F[i,j]+logp[t,v];better=z>F[i+1,j+k]
   F[i+1,j[better]+k]=z[better];back[i+1,j[better]+k]=k
 vals=[];j=L
 for i in range(N,0,-1):
  k=int(back[i,j]);vals.append(p[j-k:j]);j-=k
 vals.reverse();assert ''.join(vals)==p
 seen=collections.defaultdict(collections.Counter)
 for t,v in zip(ts,vals):seen[t][v]+=1
 repeated=[t for t in seen if sum(seen[t].values())>=2]
 agree=sum(seen[t].most_common(1)[0][1] for t in repeated)/sum(sum(seen[t].values()) for t in repeated)
 return {'log_likelihood':float(F[N,L]),'repeated_token_agreement':agree,'values':vals,'key_candidates':{t:dict(v) for t,v in seen.items()},'seed':seed,'iterations':iters}
if __name__=='__main__':
 source=sys.argv[1] if len(sys.argv)>1 else 'real';seed=int(sys.argv[2]) if len(sys.argv)>2 else 450
 if source=='control':
  x=json.loads((r/'beam_control_input.json').read_text());ts=x['cipher'];text=x['plaintext']
 else:
  x=json.loads((r/'image126_pair.json').read_text());ts=' '.join(x['cipher_lines']).split();text=x['plaintext']
  if source=='shuffled':np.random.default_rng(seed).shuffle(ts)
 start=time.time();out=fit(ts,text,seed,30)
 if source=='control':out['token_value_accuracy']=sum(v==x['true_key'][t] for t,v in zip(ts,out['values']))/len(ts)
 out['seconds']=time.time()-start
 (r/f'em_{source}_{seed}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['values','key_candidates']},indent=2))
