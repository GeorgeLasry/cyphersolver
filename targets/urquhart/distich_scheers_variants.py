import sys, re, random, math, collections
sys.path.insert(0,'.')
import pages, ct
D=ct.DISTICH; L1,L2=D[:32],D[32:]
P=pages.load(numbering='physical')
# Logopandecteision (A64608) pages by <pb>
x=open('src/tcp_A64608.xml').read()
body=re.sub(r'<note[^>]*>.*?</note>','',x,flags=re.S)
parts=re.split(r'<pb[^>]*>',body)
LP={}
for i,p in enumerate(parts[1:],1):
    t=re.sub(r'<[^>]+>',' ',p); t=re.sub(r'-\s*\n\s*','',t)
    LP[i]=re.findall(r"[A-Za-z]+",t)
# English char 4-gram model from local 17th-c English
src=open('src/sirthomasurquhar00willuoft.txt',errors='ignore').read()+open('src/bim_early-english-books-1641-1700_logopandecteision-or-an_urquhart-sir-thomas_1653.txt',errors='ignore').read()
src+=' '.join(' '.join(w) for w in P.values())
s=re.sub('[^a-z]','',src.lower()); A='abcdefghijklmnopqrstuvwxyz'
c4=collections.Counter(s[i:i+4] for i in range(len(s)-3)); c3=collections.Counter(s[i:i+3] for i in range(len(s)-2))
def lp(t):
    t=re.sub('[^a-z]','',t.lower())
    if len(t)<8: return -9
    return sum(math.log((c4.get(t[i-3:i+1],0)+0.1)/(c3.get(t[i-3:i],0)+2.6)) for i in range(3,len(t)))/(len(t)-3)
def word(pg,n): return pg[n-1] if 0<n<=len(pg) else None
def letters(pg): return ''.join(pg)
def dec(nums,book,start,mode):
    out=[]
    for k,n in enumerate(nums):
        pg=book.get(start+k)
        if not pg: out.append('_'); continue
        if mode=='first': w=word(pg,n); out.append(w[0] if w else '_')
        elif mode=='last': w=word(pg,n); out.append(w[-1] if w else '_')
        elif mode=='letter':
            L=letters(pg); out.append(L[n-1] if 0<n<=len(L) else '_')
    return ''.join(out).lower()
def series(nums):
    return {'distich':nums}
pairs={'sum':[a+b for a,b in zip(L1,L2)],'diff':[abs(a-b) for a,b in zip(L1,L2)],'l1':L1,'l2':L2,'all':D,
       'interleave':[v for ab in zip(L1,L2) for v in ab]}
def best(numsets,shuffle=None):
    res=[]
    for name,nums in numsets.items():
        if shuffle is not None:
            r=random.Random(shuffle); nums=nums[:]; r.shuffle(nums)
        for bname,book in (('jewel',P),('logo',LP)):
            for mode in ('first','last','letter'):
                for start in range(1,max(book)-len(nums)+2):
                    t=dec(nums,book,start,mode)
                    if t.count('_')>len(t)//4: continue
                    res.append((lp(t),name,bname,mode,start,t))
    res.sort(reverse=True); return res
real=best(pairs)
print('REAL top 12'); [print(round(r[0],3),r[1:5],r[5]) for r in real[:12]]
for s in range(1,6):
    sh=best(pairs,shuffle=s); print('SHUF',s,round(sh[0][0],3),sh[0][1:5],sh[0][5])
