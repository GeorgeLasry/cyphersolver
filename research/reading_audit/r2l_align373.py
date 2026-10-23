"""r2l (23 Oct 2026; copy of r2f_align370.py): align the f. 373 figure transcription with the Brienne 13 clear copy, maisse1592.

    python research/reading_audit/r2l_align373.py

Reads targets/maisse1592/texts/f373_figures.txt and f373_brienne_copy.txt; decodes the figures with Tomokiyo's key
(plus 71 = rr, 73 = tt found here); aligns the letter streams by edit distance, where an abbreviation bar (~) may stand
for 0-6 copy letters, a code group (any figure not in the key) for 0-13, and a gutter mark (G) for 0-19; prints the
line-by-line alignment (differences in capitals), letter and word counts, and the words where figures and copy differ.
"""
import pathlib
D = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'maisse1592' / 'texts'
import re,unicodedata,sys
T=open(D/'f373_brienne_copy.txt',encoding='utf8').read()
body=' '.join(l for l in T.splitlines() if not l.startswith('#') and not l.startswith('[fol'))
body=body.replace('= ','').replace('=','')   # line-end hyphen marks of the copy
body=re.sub(r'\[\?([^\]]*)\]',r'\1',body)
K={'a':7,'b':8,'c':9,'d':10,'e':11,'f':1,'g':2,'h':3,'i':4,'l':5,'m':6,'n':12,'o':13,'p':14,'q':15,'r':16,'s':17,'t':18,'u':19,'x':20,'y':21,'z':22}
def norm(w):
    w=unicodedata.normalize('NFD',w.lower()); w=''.join(c for c in w if c.isalpha() and ord(c)<128)
    return w.replace('j','i').replace('v','u').replace('k','c')
words=[norm(w) for w in re.split(r"[\s'.,;:]+",body) if norm(w)]

"""Align the f.370 figure transcription (t370.txt) with the Brienne copy encoded by Tomokiyo's key.
Decodes each group; aligns letter strings (copy normalised) by edit distance; reports per line."""
import sys,re
K={7:'a',8:'b',9:'c',10:'d',11:'e',1:'f',2:'g',3:'h',4:'i',5:'l',6:'m',12:'n',13:'o',14:'p',15:'q',16:'r',17:'s',18:'t',19:'u',20:'x',21:'y',22:'z',66:'ff',67:'mm',68:'nn',72:'ss',73:'tt',71:'rr'}  # 71=rr: not in Tomokiyo's table, read here from context (grade C)
lines=[]
for l in open(D/'f373_figures.txt',encoding='utf8'):
    if l.startswith('#') or ':' not in l: continue
    tag,toks=l.split(':',1); lines.append((tag.strip(),toks.split()))
# cipher letter stream with origin
cs=[];org=[];unc=[]
for li,(tag,toks) in enumerate(lines):
    for t in toks:
        q=t.endswith('?'); t=t.rstrip('?')
        if t=='G': cs.append('G'); org.append(li); unc.append(False); continue
        if t=='~': cs.append('~'); org.append(li); unc.append(False); continue
        if t=='w': s='d'
        elif t.isdigit() and int(t) in K: s=K[int(t)]
        else: s='{'+t+'}'
        cs.append(s); org.append(li); unc.append(q)
# expand groups into chars, keep group index
C=[];G=[]
for gi,s in enumerate(cs):
    if s in ('~','G'): C.append(s); G.append(gi); continue
    if s.startswith('{'): C.append('#'); G.append(gi); continue
    for ch in s: C.append(ch); G.append(gi)
P=''.join(words)
# semi-global alignment: cipher stream fully, copy from start to anywhere
n,m=len(C),len(P)
import numpy as np
INF=10**9
D=np.zeros((n+1,m+1),dtype=np.int32); B=np.zeros((n+1,m+1),dtype=np.int8)
D[0,:]=0  # free start in copy
for i in range(1,n+1):
    D[i,0]=i*2 if C[i-1]!='~' else D[i-1,0]; B[i,0]=1
    ci=C[i-1]
    for j in range(1,m+1):
        if ci in '~#G':
            # abbreviation mark: may absorb 0..6 copy letters at cost 0
            best=D[i-1,j]+(1 if ci=='#' else 0);bb=1
            for k in range(1,7 if ci=='~' else 14 if ci=='#' else 20):
                c=D[i-1,j-k]+(1 if ci=='#' else 0) if j-k>=0 else INF
                if c<best: best=c;bb=10+k
            D[i,j]=best;B[i,j]=bb;continue
        sub=D[i-1,j-1]+(0 if ci==P[j-1] else 2)
        dele=D[i-1,j]+2; ins=D[i,j-1]+2
        if sub<=dele and sub<=ins: D[i,j]=sub;B[i,j]=0
        elif dele<=ins: D[i,j]=dele;B[i,j]=1
        else: D[i,j]=ins;B[i,j]=2
j=int(np.argmin(D[n,:])); i=n; ops=[]
while i>0:
    b=int(B[i,j])
    if b==0: ops.append((i-1,j-1));i-=1;j-=1
    elif b==1: ops.append((i-1,None));i-=1
    elif b==2: ops.append((None,j-1));j-=1
    else: k=b-10; ops.append((i-1,('abbr',j-k,j)));i-=1;j-=k
    if i>0 and j==0 and b!=1: pass
ops.reverse()
jstart=next(o[1] for o in ops if isinstance(o[1],int))
print('copy aligned from char',jstart,'to',j if False else max(o[1] for o in ops if isinstance(o[1],int)),'of',m)
# per line report
match=sub=dele=ins=abbr=0
out={li:[[],[]] for li in range(len(lines))}
lastli=0
for a,b in ops:
    li=org[G[a]] if a is not None else lastli
    lastli=li
    if a is not None and b is not None and isinstance(b,int):
        if C[a]==P[b]: match+=1; out[li][0].append(C[a]); out[li][1].append(P[b])
        else: sub+=1; out[li][0].append(C[a].upper()); out[li][1].append(P[b].upper())
    elif a is not None and isinstance(b,tuple):
        abbr+=1; mk={'~':'~','#':'#','G':'_'}[C[a]]; out[li][0].append(mk*(b[2]-b[1]) if b[2]>b[1] else mk); out[li][1].append(P[b[1]:b[2]] or '-')
    elif a is not None:
        dele+=1; out[li][0].append(C[a].upper()); out[li][1].append('-')
    else:
        ins+=1; out[li][0].append('-'); out[li][1].append(P[b].upper())
for li,(tag,_) in enumerate(lines):
    print(tag,'fig :',''.join(out[li][0])); print(tag,'copy:',''.join(out[li][1]))
print(f'letters matched {match}, substituted {sub}, extra in figures {dele}, missing from figures {ins}, abbreviation marks {abbr}')

# ---- word-level summary (copy words) ----
state=['?']*m   # per copy letter: M match, S sub, I missing in figures, A abbrev, C code, G gutter
for a,b in ops:
    if a is not None and isinstance(b,int): state[b]='M' if C[a]==P[b] else 'S'
    elif a is not None and isinstance(b,tuple):
        for k in range(b[1],b[2]): state[k]={'~':'A','#':'C','G':'G'}[C[a]]
    elif a is None: state[b]='I'
from collections import Counter
print('copy letters by state', Counter(state))
pos=0; wc=Counter(); bad=[]
for w in words:
    st=state[pos:pos+len(w)]; pos+=len(w)
    if all(s=='G' for s in st): wc['hidden in gutter']+=1
    elif any(s=='G' for s in st): wc['partly in gutter']+=1
    elif all(s in 'MA' for s in st): wc['agree' if 'A' not in st else 'agree (abbreviated)']+=1
    elif all(s in 'MAC' for s in st): wc['code group']+=1
    else: wc['differ']+=1; bad.append(w)
print('copy words', len(words), dict(wc))
print('differing words:', ' '.join(bad))

# ---- per-word figure vs copy (including figure letters inserted inside or after a word) ----
wstart=[];p=0
for w in words: wstart.append(p); p+=len(w)
import bisect
fig_of=[[] for _ in words]
lastw=0
for a,b in ops:
    if isinstance(b,int): wi=bisect.bisect_right(wstart,b)-1; lastw=wi
    elif isinstance(b,tuple): wi=bisect.bisect_right(wstart,max(b[1],0))-1 if b[2]>b[1] else lastw; lastw=wi
    else: wi=lastw
    if a is None: continue
    s=C[a]
    if isinstance(b,tuple): s={'~':'~','#':'#','G':'_'}[s]*(b[2]-b[1])
    fig_of[wi].append(s)
diffs=[]
for wi,w in enumerate(words):
    f=''.join(fig_of[wi])
    if '_' in f or '#' in f: continue
    if f.replace('~','')!=w and not ('~' in f and len(f)==len(w) and all(x==y or x=='~' for x,y in zip(f,w))):
        diffs.append((wi,w,f))
print(len(diffs),'words where figures differ from copy:')
for wi,w,f in diffs: print(f'  {wi:3d} {" ".join(words[max(0,wi-2):wi])} [{w}] figs:{f}')
