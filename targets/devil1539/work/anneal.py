import sys, random, math, numpy as np, argparse
ap=argparse.ArgumentParser(); ap.add_argument('corpus'); ap.add_argument('tr'); ap.add_argument('--rtl',action='store_true')
ap.add_argument('--shuf',type=int,default=0); ap.add_argument('--merge',default='T2=T,Et=E,Ar=C,B2=B,Ws=W,Rb=R,Cq=Q,Ob=O,Lb=L,j=L,e=O')
ap.add_argument('--restarts',type=int,default=12); ap.add_argument('--free',type=int,default=-1)
a=ap.parse_args()
MERGE=dict(x.split('=') for x in a.merge.split(',') if x)
txt=open(a.corpus).read().replace(' ','').replace('\n','')
letters=sorted(set(txt)); n=len(letters); li={c:i for i,c in enumerate(letters)}
x=np.array([li[c] for c in txt])
q=np.zeros((n,n,n,n))+0.05; np.add.at(q,(x[:-3],x[1:-2],x[2:-1],x[3:]),1); q=np.log(q/q.sum())
toks=[]
for line in open(a.tr):
    l=[MERGE.get(t,t) for t in line.split() if t not in ('∷','∴')]
    toks+= l[::-1] if a.rtl else l
if a.shuf: random.seed(a.shuf); random.shuffle(toks)
syms=sorted(set(toks),key=lambda s:-toks.count(s)); si={s:i for i,s in enumerate(syms)}
ct=np.array([si[t] for t in toks]); S=len(syms)
nb=min(S,n) if a.free<0 else S-a.free
def sc(k):
    p=k[ct]; return q[p[:-3],p[1:-2],p[2:-1],p[3:]].sum()
best_all=None
for rs in range(a.restarts):
    rng=random.Random(rs)
    key=np.array(rng.sample(range(n),n)[:nb]+[rng.randrange(n) for _ in range(S-nb)])
    cur=sc(key); best=(cur,key.copy()); T=15.0
    for it in range(60000):
        if rng.random()<0.7 or S<=nb:
            if rng.random()<0.15 and nb<n:   # swap a bound symbol with an unused letter
                i=rng.randrange(nb); used=set(key[:nb]); un=[l for l in range(n) if l not in used]; old=key[i]; key[i]=rng.choice(un); s=sc(key)
                if s>cur or rng.random()<math.exp((s-cur)/T): cur=s
                else: key[i]=old
            else:
                i,j=rng.sample(range(nb),2); key[i],key[j]=key[j],key[i]; s=sc(key)
                if s>cur or rng.random()<math.exp((s-cur)/T): cur=s
                else: key[i],key[j]=key[j],key[i]
        else:
            i=rng.randrange(nb,S); old=key[i]; key[i]=rng.randrange(n); s=sc(key)
            if s>cur or rng.random()<math.exp((s-cur)/T): cur=s
            else: key[i]=old
        if cur>best[0]: best=(cur,key.copy())
        T=max(0.2,T*0.99993)
    if best_all is None or best[0]>best_all[0]: best_all=best
k=best_all[1]
print('shuf%d'%a.shuf if a.shuf else 'REAL', 'rtl' if a.rtl else 'ltr', round(best_all[0]/(len(ct)-3),3), ''.join(letters[j] for j in k[ct]))
print(' '.join(f'{s}={letters[k[si[s]]]}' for s in syms))
