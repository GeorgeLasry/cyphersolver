"""Sense measure: a cipher token counts as read only if every letter it yields lies inside a Spanish word.
Each letter's decrypt is segmented (DP) into dictionary words from lang/ Spanish corpora (es-gutenberg, es-quijote,
es-vasto-memorias) plus the volume's own margin decipherments; letters not covered by a word of length >=2
(or a, e, o, y) are unread, and so is every token touching them. Declared nulls count as read only between
two read tokens. Spelling is folded (accents, v/b, z/c, h, y/i, j/x) on both sides."""
import re,glob,math,collections,sys,os,pickle
sys.path.insert(0,'../..')
def fold(s):
    s=s.lower()
    for a,b in zip('áéíóúàèìòùâêîôûüç','aeiouaeiouaeiouuz'): s=s.replace(a,b)
    s=s.replace('ñ','n')
    s=re.sub(r'[^a-z$]','',s)
    return s.replace('v','b').replace('z','c').replace('h','').replace('y','i').replace('j','x').replace('ss','s').replace('qu','c').replace('k','c')
CACHE='sense_vocab.pkl'
def vocab():
    if os.path.exists(CACHE): return pickle.load(open(CACHE,'rb'))
    from lang import corpora
    txt=corpora.text(['es-gutenberg','es-quijote','es-vasto-memorias'])
    W=collections.Counter(fold(w) for w in re.findall(r'[A-Za-zÁÉÍÓÚáéíóúñÑüçÇ]+',txt))
    for f in glob.glob('tx/R*.txt')+glob.glob('../balbases1677/tx/R*.txt')+glob.glob('../hernannunez1674/tx/R*.txt'):
        for l in open(f,encoding='utf8'):
            if l.startswith('M:'):
                for w in re.findall(r'[A-Za-zÁÉÍÓÚáéíóúñÑüçÇ]+',l):
                    if '?' not in w and '*' not in w: W[fold(w)]+=3
    for w in ['$','mte','embax','embaxr','embaxres','monsr','duq','ord','sr','sra','md','mag','magd','exa','exmo','sa','dha','dho','dhos','qe','qto']: W[fold(w)]+=50
    W={w:c for w,c in W.items() if w and (len(w)>=2 or w in ('a','e','o','i'))}
    pickle.dump(W,open(CACHE,'wb'));return W
W=vocab();TOT=sum(W.values());MAXW=max(len(w) for w in W if W[w]>2)
def _ok(w,c):
    if len(w)==1: return w in ('a','e','o','i')
    if len(w)==2: return (c>=1500 and w not in ('of','to','is','ai')) or w in ('$','sr','md')
    if len(w)==3: return c>=60
    return c>=3
LW={w:-math.log(c/TOT) for w,c in W.items() if _ok(w,c)}
def segment(s):
    """s folded; returns covered[] booleans"""
    n=len(s);INF=1e18;D=[INF]*(n+1);B=[None]*(n+1);D[0]=0
    for i in range(n):
        if D[i]>=INF: continue
        if D[i]+25<D[i+1]: D[i+1]=D[i]+25;B[i+1]=(i,False)
        for L in range(1,min(22,n-i)+1):
            w=s[i:i+L]
            if w in LW and D[i]+LW[w]<D[i+L]: D[i+L]=D[i]+LW[w];B[i+L]=(i,True)
    cov=[False]*n;j=n
    while j>0:
        i,ok=B[j]
        for k in range(i,j): cov[k]=ok
        j=i
    return cov
def measure(vals):
    """vals: list per token of str (value) or None (unread). returns (n_tokens, n_sense, flags)"""
    seq=[];own=[]
    for i,v in enumerate(vals):
        if v is None: seq.append('#');own.append(i);continue
        f=fold(v.replace('V.S.','$'))
        for ch in f: seq.append(ch);own.append(i)
    ok=[True]*len(vals); s=''.join(seq)
    for m in re.finditer(r'[^#]+',s):
        cov=segment(m.group())
        for k,c in enumerate(cov):
            if not c: ok[own[m.start()+k]]=False
    for i,v in enumerate(vals):
        if v is None: ok[i]=False
    for i,v in enumerate(vals):   # empty values (nulls) read only if neighbours read
        if v is not None and fold(v)=='':
            ok[i]=(i==0 or ok[i-1]) and (i==len(vals)-1 or ok[i+1]) and not (i>0 and vals[i-1] is None)
    return len(vals),sum(ok),ok
