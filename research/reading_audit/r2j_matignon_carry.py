"""r2j (matignon1586c3): align ff379-381_reading.md word by word with Burford's signs (DP, monotone), allowing the
r2j second values / look-alike alternates; prints every reading word that rests on an alternate (altN) or is not
carried by the figures (nc). Usage: python research/reading_audit/r2j_matignon_carry.py [reading.md]"""
import re,json,sys
import numpy as np
D='C:/Users/dbour/cypher/.worktrees/reading-gate/targets/matignon1586c3/f379_381/'
X={'C':'h','p+':'b','b':'y','Lr':'n','g':'o','9t':'e','+':'r','S':'q','xi':'c'}
seq=[]
for p in ['f379r','f379v','f380r','f380v','f381r','f381v']:
    t=json.load(open(D+'burford/'+p+'/key.json',encoding='utf-8'))['pipeline'][0]['table']
    for raw in open(D+'burford/'+p+'/signs.txt',encoding='utf-8'):
        if raw.startswith('#') or not raw.strip(): continue
        n,_,s=raw.rstrip('\n').partition('\t')
        for k,x in enumerate(s.split()):
            if p=='f379v' and n=='3' and k==12: continue
            v=(t.get(x) or {}).get('v'); v=list(v) if isinstance(v,list) else ([v] if v else [])
            v=[a.replace('_','') for a in v]
            base=list(v)
            if x in X: v=v+[X[x]]
            seq.append((v,base,p,int(n),k,x))
S=len(seq)
def norm(w): return w.lower().replace('j','i').replace('v','u')
body=open(sys.argv[1] if len(sys.argv)>1 else D+'ff379-381_reading.md',encoding='utf8').read().split('## Reading')[1]
body=re.sub(r'le roy de Navarre','leroydenavarre',body)
toks=re.findall(r"\[[^\]]*\]|[A-Za-zÀ-ÿ]+(?:\[[^\]]*\][A-Za-zÀ-ÿ]*)*",body)
def ends(w,s):
    out=[]
    def rec(i,j,alt):
        if j==len(w): out.append((i,alt)); return
        if i>=S: return
        for v in seq[i][0]:
            v=norm(v); a=alt+(0 if v in [norm(b) for b in seq[i][1]] else 1)
            if w.startswith(v,j): rec(i+1,j+len(v),a)
            elif j>0 and len(v)>1 and v.startswith(w[j:]): out.append((i+1,a))
    rec(s,0,0); return out
INF=10**9
W=len(toks)
Dp=np.full((W+1,S+1),INF,dtype=np.int64); Dp[0,0]=0
back={}
for i,tk in enumerate(toks):
    cur=Dp[i]
    br=tk.startswith('[') or '[' in tk
    # cheapest arrival at t after skipping from any s<=t: cost(s)+(t-s)
    tmp=cur-np.arange(S+1); run=np.minimum.accumulate(tmp); skip=run+np.arange(S+1)
    arg=np.zeros(S+1,dtype=int)  # not tracking exact s
    nxt=Dp[i+1]
    if br:
        # bracketed: free skip up to 12 signs
        for t in range(S+1):
            lo=max(0,t-12); m=cur[lo:t+1].min()
            if m<nxt[t]: nxt[t]=m; back[(i+1,t)]=('br',None)
        continue
    w=norm(tk)
    nxt_nc=cur+12
    for t in range(S+1):
        if nxt_nc[t]<nxt[t]: nxt[t]=nxt_nc[t]; back[(i+1,t)]=('nc',t)
    for s in range(S):
        if skip[s]>=INF: continue
        for e,a in ends(w,s):
            c=skip[s]+a*0
            if c<nxt[e]: nxt[e]=c; back[(i+1,e)]=('m',s,a)
e=int(np.argmin(Dp[W])); print('total cost',Dp[W,e],'end',e,'of',S)
# backtrack
res=[]; t=e
for i in range(W,0,-1):
    b=back.get((i,t))
    if b is None: res.append((toks[i-1],'?')); continue
    if b[0]=='m': res.append((toks[i-1],'ok' if b[2]==0 else 'alt%d'%b[2],seq[b[1]][2:5])); 
    else: res.append((toks[i-1],b[0]))
    # find previous t
    if b[0]=='m':
        s=b[1]; prev=Dp[i-1][:s+1]-np.arange(s+1); t=int(np.argmin(prev))
    elif b[0]=='nc': pass
    else:
        lo=max(0,t-12); t=lo+int(np.argmin(Dp[i-1][lo:t+1]))
res.reverse()
for r in res:
    if r[1] not in ('ok','br'): print(r)
