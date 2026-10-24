# usage: rank.py GROUP [GROUP...] [-n N]  : rank candidate values for unread groups by the Spanish 5-gram,
# given the fixed signs (signs.txt) and known groups (groups.txt); unread neighbours break the context.
import sys,array,math
A='abcdefghilmnopqrstuxyz'; K=22; IX={c:i for i,c in enumerate(A)}
raw=array.array('f'); raw.frombytes(open('es.lm','rb').read()); lp=[None]; off=0
for o in range(1,6): lp.append(raw[off:off+K**o]); off+=K**o
S=dict(kv.split('=') for kv in open('signs.txt').read().split())
G=dict(kv.split('=') for kv in open('groups.txt').read().split())
T=[t for l in open('v15x.txt') for t in l.split()]
isg=lambda t: t.islower() and t.isalpha()
def val(t):
    if isg(t): return G.get(t)
    v=S.get(t); return v.lower() if v else None
def score(left,s):
    c=[IX[x] for x in left][-4:]; tot=0.0
    for ch in s:
        x=IX[ch]; idx=0
        for q in c: idx=idx*K+q
        tot+=lp[len(c)+1][idx*K+x]; c=(c+[x])[-4:]
    return tot
cands=[l.strip() for l in open('wide2.txt') if l.strip()]+list(A)
cands=sorted(set(c for c in cands if all(ch in IX for ch in c)))
args=[a for a in sys.argv[1:] if not a.startswith('-')]; N=int(sys.argv[sys.argv.index('-n')+1]) if '-n' in sys.argv else 8
for g in args:
    occ=[]
    for i,t in enumerate(T):
        if t!=g: continue
        left=''
        for x in reversed(T[max(0,i-6):i]):
            v=val(x)
            if v is None: break
            left=v+left
        right=''
        for x in T[i+1:i+8]:
            v=val(x)
            if v is None: break
            right+=v
            if len(right)>=8: break
        occ.append((left[-4:],right[:8]))
    if not occ: print(g,0); continue
    res=[]
    for c in cands:
        res.append((sum(score(l,c+r)-score('',c)-score('',r) for l,r in occ)/len(occ),c))
    res.sort(reverse=True)
    print(g,len(occ),' '.join(f'{c}:{s:.1f}' for s,c in res[:N]))
