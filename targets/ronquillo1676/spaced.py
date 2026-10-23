"""ronq batch, 22 Oct 2026: key decode of each letter split into words (sense.py's DP), page by page, with
DECODE's margin transcription for that page beside it. Writes read/R*.dec.txt, the working sheet for the readings.
[t] = group not in key; {v} = value not inside a word; | = image boundary."""
import re,sys,os,math
sys.stdout.reconfigure(encoding='utf-8')
exec(open('keyx.py',encoding='utf8').read())
import sense
def words(vals,toks):
    seq=[];own=[]
    for i,v in enumerate(vals):
        if v is None: seq.append('#');own.append(i);continue
        for ch in v.lower().replace('v.s.','$'): seq.append(ch);own.append(i)
    s=''.join(seq);out=[]
    for m in re.finditer(r'#|[^#]+',s):
        if m.group()=='#': out.append('['+toks[own[m.start()]]+']');continue
        seg=m.group();n=len(seg);INF=1e18;D=[INF]*(n+1);B=[None]*(n+1);D[0]=0
        for i in range(n):
            if D[i]>=INF: continue
            if D[i]+25<D[i+1]: D[i+1]=D[i]+25;B[i+1]=(i,False)
            for L in range(1,min(24,n-i)+1):
                w=sense.fold(seg[i:i+L])
                if w and w in sense.LW and D[i]+sense.LW[w]<D[i+L]: D[i+L]=D[i]+sense.LW[w];B[i+L]=(i,True)
        cuts=[];j=n
        while j>0:
            i,ok=B[j];cuts.append((i,j,ok));j=i
        cuts.reverse();buf=''
        for i,j,ok in cuts:
            if ok:
                if buf: out.append('{'+buf+'}');buf=''
                out.append(seg[i:j])
            else: buf+=seg[i:j]
        if buf: out.append('{'+buf+'}')
    return ' '.join(out).replace('$','V.S.')
recs=sys.argv[1:] or [f'R{r}' for r in [*range(966,985),1001]]
for rec in recs:
    src=f'txi/{rec}.txt' if os.path.exists(f'txi/{rec}.txt') else f'tx/{rec}.txt'
    pages=[];cur=None
    for l in open(src,encoding='utf8'):
        if l.startswith('#IMAGE'): cur=[l.strip(),[],[]];pages.append(cur);continue
        if cur is None: cur=['#',[],[]];pages.append(cur)
        if l.startswith('C:'): cur[1]+=l[2:].split()
    mp={};cur=None
    for l in open(f'tx/{rec}.txt',encoding='utf8'):
        if l.startswith('#IMAGE'): cur=l.strip();mp.setdefault(cur,[]);continue
        if l.startswith('M:'): mp.setdefault(cur,[]).append(l[2:].strip())
    out=[]
    for name,C,_ in pages:
        C=[t for t in C if t!='-']
        vals=[K.get(t) for t in C]
        out.append(f'=== {name}  ({len(C)} groups)\n'+words(vals,C)+'\n--- margin (DECODE):\n'+' / '.join(mp.get(name,[]))+'\n')
    open(f'read/{rec}.dec.txt','w',encoding='utf8').write('\n'.join(out))
    print(rec,'ok')
