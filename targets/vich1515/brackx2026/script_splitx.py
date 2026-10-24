# Per-token value for sign X among r / s / z by the Spanish 5-gram in context (8 letters each side).
# Writes v15x.txt with X replaced by Xr / Xs / Xz (signs.txt gets Xr=r Xs=s Xz=z) and splitx.tsv.
import array
A='abcdefghilmnopqrstuxyz'; K=22; IX={c:i for i,c in enumerate(A)}
raw=array.array('f'); raw.frombytes(open('es.lm','rb').read()); lp=[None]; off=0
for o in range(1,6): lp.append(raw[off:off+K**o]); off+=K**o
S=dict(kv.split('=') for kv in open('signs.txt').read().split())
G=dict(kv.split('=') for kv in open('groups.txt').read().split())
L=[l.split() for l in open('v15s.txt') if l.strip()]
isg=lambda t: t.islower() and t.isalpha()
def val(t):
    if t=='X': return None
    if isg(t): return G.get(t)
    v=S.get(t); return v.lower() if v else None
def score(s):
    c=[];tot=0.0
    for ch in s:
        x=IX[ch]; idx=0
        for q in c: idx=idx*K+q
        tot+=lp[len(c)+1][idx*K+x]; c=(c+[x])[-4:]
    return tot
T=[t for l in L for t in l]; out=[]; rows=[]
for k,t in enumerate(T):
    if t!='X': out.append(t); continue
    left=''
    for x in reversed(T[max(0,k-6):k]):
        v=val(x)
        if v is None: break
        left=v+left
    right=''
    for x in T[k+1:k+7]:
        v=val(x)
        if v is None: break
        right+=v
    left=left[-6:]; right=right[:8]
    sc={c:score(left+c+right)-score(left) for c in 'rsz'}
    best=max(sc,key=sc.get); m=sc[best]-sorted(sc.values())[-2]
    out.append('X'+best); rows.append(f'{k}\t{left}\t{right}\t{best}\t{m:.2f}')
it=iter(out); open('v15x.txt','w').write('\n'.join(' '.join(next(it) for _ in l) for l in L)+'\n')
open('splitx.tsv','w').write('\n'.join(rows)+'\n')
import collections; print(collections.Counter(r.split('\t')[3] for r in rows))
