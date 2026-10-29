import sys; sys.path.insert(0,'.')
import wlm
from ct import W
def run(k,ind,K,top=3):
    w=W[k][ind:]; R=len(w)//K; rows=[w[i*K:(i+1)*K] for i in range(R)]
    nodes=[(c,d) for c in range(K) for d in 'du']
    col={n:([r[n[0]] for r in rows] if n[1]=='d' else [r[n[0]] for r in rows][::-1]) for n in nodes}
    wi={n:sum(wlm.pmi(a,b) for a,b in zip(col[n],col[n][1:])) for n in nodes}
    J={(u,v):wlm.pmi(col[u][-1],col[v][0]) for u in nodes for v in nodes if u[0]!=v[0]}
    best={(1<<n[0],n):(wi[n],[n]) for n in nodes}
    for m in range(1,1<<K):
        for u in nodes:
            if (m,u) not in best: continue
            s,p=best[(m,u)]
            for v in nodes:
                if m>>v[0]&1: continue
                k2=(m|1<<v[0],v); s2=s+J[(u,v)]+wi[v]
                if k2 not in best or best[k2][0]<s2: best[k2]=(s2,p+[v])
    f=(1<<K)-1
    res=sorted([best[(f,u)] for u in nodes],key=lambda x:-x[0])[:top]
    for s,p in res:
        print(k,'ind',ind,'K',K,round(s/len(w),3),p); print('   '+' / '.join(' '.join(col[n]) for n in p))
for a in sys.argv[1:]:
    k,ind,K=a.split(','); run(k,int(ind),int(K))
