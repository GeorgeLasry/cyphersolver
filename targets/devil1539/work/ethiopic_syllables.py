import numpy as np, random, sys
corp=sys.argv[1]
txt=open(corp).read()[:1500000]
A='abcdefghilmnopqrstuxz'; ai={c:i for i,c in enumerate(A)}; n=len(A)
x=np.array([ai[c] for c in txt if c in ai])
q=np.zeros((n,n,n,n))+0.02; np.add.at(q,(x[:-3],x[1:-2],x[2:-1],x[3:]),1); q=np.log(q/q.sum(axis=3,keepdims=True))
MERGE={'T2':'T','Et':'E','Ar':'C','B2':'B','Ws':'W','Rb':'R','Cq':'Q','Ob':'O','Lb':'L','j':'L','e':'O'}
toks=[u for u in (MERGE.get(t,t) for t in open('w/tr1.txt').read().split()) if u not in ('∷','∴','Q','W','8')]
# visual Ethiopic consonants ('' = vowel carrier)
vis=dict(A='',T='t',G='g',V='l',S='s',H='h',M='h',N='b',D='b',I='n',U='q',Y='h',X='i',C='r',O='',Z='d',F='f',L='l',E='n',P='c',B='r',R='',K='z',J='d')
V=['a','e','i','o','u','']
def best(m,beam=400):
    states={(): 0.0}
    for t in toks:
        c=m[t]; new={}
        for hist,s in states.items():
            for v in V:
                add=c+v
                if not add: continue
                h=list(hist); sc=s
                for ch in add:
                    if len(h)>=3: sc+=q[ai[h[-3]],ai[h[-2]],ai[h[-1]],ai[ch]]
                    else: sc+=-3.0
                    h.append(ch)
                key=tuple(h[-3:])
                if key not in new or new[key]<sc: new[key]=sc
        states=dict(sorted(new.items(),key=lambda kv:-kv[1])[:beam])
    return max(states.values())
real=best(vis); print('real',round(real,1))
syms=sorted(set(toks)); vals=[vis[s] for s in syms]; rs=[]
random.seed(1)
for i in range(int(sys.argv[2])):
    random.shuffle(vals); rs.append(best(dict(zip(syms,vals)),beam=200))
rs=np.array(rs); print('perm mean %.1f sd %.1f max %.1f z=%.2f'%(rs.mean(),rs.std(),rs.max(),(real-rs.mean())/rs.std()))
