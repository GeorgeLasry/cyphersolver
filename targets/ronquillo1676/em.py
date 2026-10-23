# hard-EM: learn values of tokens the key lacks by aligning each margined letter against its margin decipherment
import re,math,collections,sys,glob,json
sys.stdout.reconfigure(encoding='utf-8')
exec(open('keyx.py',encoding='utf8').read())
def norm(s):
    s=s.lower().replace('ç','z').replace('ñ','n')
    for a,b in zip('áéíóúàèìòùâêîôû','aeiouaeiouaeiou'): s=s.replace(a,b)
    s=re.sub(r'\bv\.?\s?s\.?\b','$',s); s=re.sub(r'[?*]','#',s)
    return re.sub(r'[^a-z#$]','',s)
def kn(v): return norm(v.replace('V.S.','$'))
data=[]
for f in sorted(glob.glob('tx/R*.txt')):
    T=[];M=[]
    for l in open(f,encoding='utf8'):
        if l.startswith('C:'): T+=l[2:].split()
        elif l.startswith('M:'): M.append(l[2:])
    s=norm(' '.join(M))
    if len(s)>200: data.append((f[3:-4],T,s))
MAXL=8;LP={0:.15,1:.2,2:.3,3:.2,4:.08,5:.03,6:.015,7:.01,8:.008}
cnt=collections.defaultdict(collections.Counter);SKIP=4.0
def cost(tok,sub):
    if '#' in sub and sub!='#'*len(sub): return 1e9
    if tok in K:
        v=kn(K[tok])
        if sub==v: return 0.0
        if len(sub)==len(v) and all(a==b or a=='#' for a,b in zip(sub,v)): return 1.0
        return 12.0
    c=cnt[tok];n=sum(c.values())
    p=(c[sub]+LP[len(sub)]*(1/20)**len(sub))/(n+1);return -math.log(p)
def align(t,s):
    I,J=len(t),len(s);INF=1e18
    D=[[INF]*(J+1) for _ in range(I+1)];B=[[None]*(J+1) for _ in range(I+1)];D[0][0]=0
    band=max(60,int(0.07*J))
    for i in range(I+1):
        Di=D[i];c=i*J/max(I,1);lo=max(0,int(c-band));hi=min(J,int(c+band))
        for j in range(lo,hi+1):
            d=Di[j]
            if d>=INF: continue
            if j<J and d+SKIP<Di[j+1]: Di[j+1]=d+SKIP;B[i][j+1]=(i,j,None)
            if i<I:
                if d+SKIP<D[i+1][j]: D[i+1][j]=d+SKIP;B[i+1][j]=(i,j,'@')
                tok=t[i];Dn=D[i+1]
                for L in range(0,min(MAXL,J-j)+1):
                    v=d+cost(tok,s[j:j+L])
                    if v<Dn[j+L]: Dn[j+L]=v;B[i+1][j+L]=(i,j,s[j:j+L])
    i,j=I,J;path=[]
    while (i,j)!=(0,0):
        pi,pj,sub=B[i][j]
        if sub is not None and sub!='@': path.append((t[pi],sub))
        i,j=pi,pj
    return D[I][J],path[::-1]
def job(a):
    global cnt
    cnt,(r,t,s)=a
    return align(t,s)
if __name__!='__main__': pass
else:
 from multiprocessing import Pool
 for it in range(int(sys.argv[1]) if len(sys.argv)>1 else 4):
    new=collections.defaultdict(collections.Counter);tot=0
    with Pool(16) as P: res=P.map(job,[(cnt,d) for d in data])
    for (r,t,s),(c,p) in zip(data,res):
        tot+=c
        for tok,sub in p:
            if tok not in K and '#' not in sub: new[tok][sub]+=1
    cnt=new;print('iter',it,round(tot),flush=True)
if __name__=='__main__':
 json.dump({k:dict(v) for k,v in cnt.items()},open('em_counts.json','w',encoding='utf8'),ensure_ascii=False,indent=0)
 fr=collections.Counter()
 for r,t,s in data: fr.update(x for x in t if x not in K)
 for tok,n in fr.most_common(100): print(tok,n,cnt[tok].most_common(4))
