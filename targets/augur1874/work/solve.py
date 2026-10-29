import sys, itertools, math
sys.path.insert(0, r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/2f6a28a5-ed6e-4735-b6ce-d50c145ce7bc/scratchpad/wt')
from lang import lm
import wlm
sys.path.insert(0, r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/2f6a28a5-ed6e-4735-b6ce-d50c145ce7bc/scratchpad/augur'); from ct import W
m = lm.load('en-modern')
def S(s): return m.score(lm.norm(s))
cache={}
def pair(a,b):
    k=(a,b)
    if k not in cache: cache[k]=wlm.pmi(a,b)
    return cache[k]
def solve(cols):
    C=len(cols); R=len(cols[0])
    nodes=[(i,d) for i in range(C) for d in (0,1)]
    seq={ (i,d): (cols[i] if d==0 else cols[i][::-1]) for i,d in nodes}
    def ps(u,v): return sum(pair(seq[u][r],seq[v][r]) for r in range(R))
    P={(u,v):ps(u,v) for u in nodes for v in nodes if u[0]!=v[0]}
    best={}
    for u in nodes: best[(1<<u[0],u)]=(0.0,[u])
    for mask in range(1,1<<C):
        for u in nodes:
            k=(mask,u)
            if k not in best: continue
            sc,path=best[k]
            for v in nodes:
                if mask>>v[0]&1: continue
                k2=(mask|1<<v[0],v); s2=sc+P[(u,v)]
                if k2 not in best or best[k2][0]<s2: best[k2]=(s2,path+[v])
    full=(1<<C)-1
    res=sorted((best[(full,u)] for u in nodes if (full,u) in best),key=lambda x:-x[0])
    out=[]
    for sc,path in res[:2]:
        rows=[' '.join(seq[u][r] for u in path) for r in range(R)]
        if True:
            r2=rows[::-1] ; f=lambda rr:(lambda ws: sum(wlm.pmi(a,b) for a,b in zip(ws,ws[1:]))/(len(ws)-1))(' '.join(rr).split())
            if f(r2)>f(rows): rows=r2
            tot=f(rows)
        out.append((tot,sc,path,rows))
    return out
results=[]
for k,w in [(k,W[k]) for k in sys.argv[1:]]:
    for ind in (0,1):
        body=w[ind:]; n=len(body)
        for chk in (0,1):
            for C in range(3,11):
                if n%C: continue
                L=n//C; R=L-chk
                if R<2: continue
                cols=[body[i*L:i*L+R] for i in range(C)]
                for pc,sc,path,rows in solve(cols)[:1]:
                    results.append((k,pc,ind,chk,C,R,path,rows))
for k in sys.argv[1:]:
    rs=sorted([r for r in results if r[0]==k],key=lambda r:-r[1])[:12]
    for r in rs:
        print(k,'pc=%.3f ind=%d chk=%d C=%d R=%d'%r[1:6],r[6]); print('   '+' / '.join(r[7]))
