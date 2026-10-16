import sys, re, unicodedata, numpy as np
A='abcdefghilmnopqrstuxz'; ai={c:i for i,c in enumerate(A)}; n=len(A)
def norm(t):
    t=unicodedata.normalize('NFD',t.lower()); t=''.join(c for c in t if not unicodedata.combining(c))
    t=t.replace('j','i').replace('v','u').replace('k','c').replace('y','i').replace('w','u')
    return re.sub('[^a-z]','',t)
out=sys.argv[1]; files=sys.argv[2:]
txt=''.join(norm(open(f,errors='ignore').read()) for f in files)
x=np.array([ai[c] for c in txt if c in ai],dtype=np.int64)
print(out,len(x))
idx=(((x[:-4]*n+x[1:-3])*n+x[2:-2])*n+x[3:-1])*n+x[4:]
c5=np.bincount(idx,minlength=n**5).astype(np.float64).reshape(n,n,n,n,n)
c4=c5.sum(axis=4,keepdims=True)
# interpolated conditional with 4-gram backoff
idx4=((x[:-3]*n+x[1:-2])*n+x[2:-1])*n+x[3:]
c4b=np.bincount(idx4,minlength=n**4).astype(np.float64).reshape(n,n,n,n)
p4=(c4b+0.05)/(c4b.sum(axis=3,keepdims=True)+0.05*n)   # P(d|abc)
lam=c4/(c4+3.0)
p=lam*(c5/np.maximum(c4,1))+(1-lam)*p4[None,:,:,:,:]
lp=np.log(p).astype(np.float32)
lp.tofile(out)
uni=np.bincount(x,minlength=n)/len(x); np.savetxt(out+'.uni',uni)
