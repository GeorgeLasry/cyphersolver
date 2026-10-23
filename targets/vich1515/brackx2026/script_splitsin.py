# Split the transcription's 'sin' tokens into 'sin' (es) and 'sim' (en) by the Spanish 5-gram in context.
# Writes v15s.txt and splitsin.tsv (line, position, left, right, score margin, choice).
import array
A='abcdefghilmnopqrstuxyz'; K=22; IX={c:i for i,c in enumerate(A)}
raw=array.array('f'); raw.frombytes(open('es.lm','rb').read()); lp=[None]; off=0
for o in range(1,6): lp.append(raw[off:off+K**o]); off+=K**o
S=dict(kv.split('=') for kv in open('signs.txt').read().split())
G=dict(kv.split('=') for kv in open('groups.txt').read().split())
L=[l.split() for l in open('v15.txt') if l.strip()]
isg=lambda t: t.islower() and t.isalpha()
def val(t):
    if t=='sin': return None
    if isg(t): return G.get(t)
    v=S.get(t); return v.lower() if v else None
def score(s):
    c=[];tot=0.0
    for i,ch in enumerate(s):
        x=IX[ch]; idx=0
        for q in c: idx=idx*K+q
        tot+=lp[len(c)+1][idx*K+x]; c=(c+[x])[-4:]
    return tot
T=[(i,j,t) for i,l in enumerate(L) for j,t in enumerate(l)]
out=[];rows=[]
for k,(i,j,t) in enumerate(T):
    if t!='sin': out.append(t); continue
    left=''
    for _,_,x in reversed(T[max(0,k-5):k]):
        v=val(x)
        if v is None: break
        left=v+left
    right=''
    for _,_,x in T[k+1:k+6]:
        v=val(x)
        if v is None: break
        right+=v
    left=left[-4:]; right=right[:6]
    es=score(left+'es'+right)-score(left); en=score(left+'en'+right)-score(left)
    ch='sin' if es>=en else 'sim'; out.append(ch)
    rows.append(f'{i+1}\t{j+1}\t{left}\t{right}\t{es-en:+.2f}\t{ch}')
it=iter(out)
open('v15s.txt','w').write('\n'.join(' '.join(next(it) for _ in l) for l in L)+'\n')
open('splitsin.tsv','w').write('\n'.join(rows)+'\n')
print('sin->es',sum(r.endswith('sin') for r in rows),'sim->en',sum(r.endswith('sim') for r in rows))
print('close calls (|margin|<1):',sum(abs(float(r.split('\t')[4]))<1 for r in rows))
