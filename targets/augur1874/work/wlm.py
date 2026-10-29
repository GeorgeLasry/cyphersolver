import re, math, collections, pickle, os
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'wlm.pkl')
if os.path.exists(P):
    U,B,N=pickle.load(open(P,'rb'))
else:
    t=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..","..","lang","corpora","en-gutenberg.txt"),encoding='utf8').read().lower()
    w=re.findall(r"[a-z]+",t)
    U=collections.Counter(w); B=collections.Counter(zip(w,w[1:])); N=len(w)
    B={k:v for k,v in B.items() if v>1}
    pickle.dump((U,B,N),open(P,'wb'))
V=len(U)
def lp(a,b):
    a=re.sub('[^a-z]','',a.lower()); b=re.sub('[^a-z]','',b.lower())
    pu=(U.get(b,0)+0.5)/(N+V)
    ca=U.get(a,0)
    pb=B.get((a,b),0)/ca if ca else 0
    lam=0.7 if ca>5 else 0.3
    return math.log(lam*pb+(1-lam)*pu)
def pmi(a,b):
    bb=re.sub('[^a-z]','',b.lower())
    return lp(a,b)-math.log((U.get(bb,0)+0.5)/(N+V))
