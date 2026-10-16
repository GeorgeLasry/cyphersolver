import sys, random, math, numpy as np, argparse
ap=argparse.ArgumentParser(); ap.add_argument('corpus'); ap.add_argument('tr'); ap.add_argument('--rtl',action='store_true')
ap.add_argument('--shuf',type=int,default=0); ap.add_argument('--restarts',type=int,default=10); ap.add_argument('--iters',type=int,default=80000)
ap.add_argument('--merge',default=''); ap.add_argument('--lam',type=float,default=1.0)
a=ap.parse_args()
MERGE=dict(x.split('=') for x in a.merge.split(',') if x)
txt=open(a.corpus).read()
letters=sorted(set(txt)); n=len(letters); li={c:i for i,c in enumerate(letters)}
x=np.array([li[c] for c in txt])
q=np.zeros((n,n,n,n))+0.01; np.add.at(q,(x[:-3],x[1:-2],x[2:-1],x[3:]),1)
q=np.log(q/q.sum(axis=3,keepdims=True))   # conditional P(d|abc)
uni=np.bincount(x,minlength=n)/len(x); lu=np.log(uni)
toks=[]
for line in open(a.tr):
    l=[MERGE.get(t,t) for t in line.split() if t not in ('∷','∴')]
    toks+= l[::-1] if a.rtl else l
if a.shuf: random.seed(a.shuf); random.shuffle(toks)
syms=sorted(set(toks)); si={s:i for i,s in enumerate(syms)}; ct=np.array([si[t] for t in toks]); S=len(syms); N=len(ct)
def sc(k):
    p=k[ct]; s=q[p[:-3],p[1:-2],p[2:-1],p[3:]].sum()+lu[p[:3]].sum()
    obs=np.bincount(p,minlength=n); ex=uni*N
    return s - a.lam*((obs-ex)**2/(ex+0.5)).sum()
best_all=None
for rs in range(a.restarts):
    rng=random.Random(rs*7+a.shuf)
    key=np.array([rng.choices(range(n),weights=uni)[0] for _ in syms]); cur=sc(key); best=(cur,key.copy()); T=8.0
    for it in range(a.iters):
        if rng.random()<0.3:
            i,j=rng.sample(range(S),2); key[i],key[j]=key[j],key[i]; s=sc(key)
            if s>cur or rng.random()<math.exp((s-cur)/T): cur=s
            else: key[i],key[j]=key[j],key[i]
        else:
            i=rng.randrange(S); old=key[i]; key[i]=rng.choices(range(n),weights=uni)[0] if rng.random()<0.5 else rng.randrange(n)
            s=sc(key)
            if s>cur or rng.random()<math.exp((s-cur)/T): cur=s
            else: key[i]=old
        if cur>best[0]: best=(cur,key.copy())
        T=max(0.15,T*(1-6.0/a.iters))
    if best_all is None or best[0]>best_all[0]: best_all=best
k=best_all[1]
p=k[ct]; lm=q[p[:-3],p[1:-2],p[2:-1],p[3:]].sum()/N
print('shuf%d'%a.shuf if a.shuf else 'REAL', 'rtl' if a.rtl else 'ltr', round(best_all[0]/N,3), 'lm',round(lm,3), ''.join(letters[j] for j in k[ct]))
