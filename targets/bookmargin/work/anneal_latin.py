import sys, glob, re, random, math, numpy as np, unicodedata
corpus_glob=sys.argv[1]; fn=sys.argv[2]; mode=sys.argv[3]
MERGE={'T2':'T','Et':'E','Ar':'C','B2':'B','Ws':'W','Rb':'R','Cq':'Q','Ob':'O','Lb':'L','j':'L','e':'O'}
def norm(t):
    t=unicodedata.normalize('NFD',t.lower()); t=''.join(c for c in t if not unicodedata.combining(c))
    t=t.replace('j','i').replace('v','u').replace('k','c').replace('y','i').replace('w','u')
    return re.sub('[^a-z]','',t)
txt=''.join(norm(open(f,errors='ignore').read()) for f in glob.glob(corpus_glob))
letters=sorted(set(txt)); n=len(letters); li={c:i for i,c in enumerate(letters)}
x=np.array([li[c] for c in txt])
q=np.zeros((n,n,n,n))+0.05; np.add.at(q,(x[:-3],x[1:-2],x[2:-1],x[3:]),1); q=np.log(q/q.sum())
toks=[MERGE.get(t,t) for t in open(fn).read().split() if t not in ('∷','∴')]
if mode=='shuf': random.seed(int(sys.argv[4]) if len(sys.argv)>4 else 7); random.shuffle(toks)
syms=sorted(set(toks),key=lambda s:-toks.count(s)); si={s:i for i,s in enumerate(syms)}
ct=np.array([si[t] for t in toks]); S=len(syms)
def sc(k):
    p=k[ct]; return q[p[:-3],p[1:-2],p[2:-1],p[3:]].sum()
# slots: each letter appears once; extra symbols (beyond n) are free (homophones)
best_all=None
for rs in range(12):
    rng=random.Random(rs)
    key=np.array(rng.sample(range(n),n)[:min(S,n)]+[rng.randrange(n) for _ in range(max(0,S-n))])
    cur=sc(key); best=(cur,key.copy()); T=15.0
    for it in range(50000):
        if rng.random()<0.7 or S<=n:
            i,j=rng.sample(range(min(S,n)),2); key[i],key[j]=key[j],key[i]; s=sc(key)
            if s>cur or rng.random()<math.exp((s-cur)/T): cur=s
            else: key[i],key[j]=key[j],key[i]
        else:
            i=rng.randrange(n,S); old=key[i]; key[i]=rng.randrange(n); s=sc(key)
            if s>cur or rng.random()<math.exp((s-cur)/T): cur=s
            else: key[i]=old
        if cur>best[0]: best=(cur,key.copy())
        T=max(0.2,T*0.9999)
    if best_all is None or best[0]>best_all[0]: best_all=best
k=best_all[1]
print(mode, S, round(best_all[0]/(len(ct)-3),3), ''.join(letters[j] for j in k[ct]))
