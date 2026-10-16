import sys, numpy as np
out=sys.argv[1]; alpha=sys.argv[2]; files=sys.argv[3:]
ai={c:i for i,c in enumerate(alpha)}; n=len(alpha)
txt=''.join(open(f,errors='ignore').read() for f in files)
x=np.array([ai[c] for c in txt if c in ai],dtype=np.int64); print(out,n,len(x))
idx=(((x[:-4]*n+x[1:-3])*n+x[2:-2])*n+x[3:-1])*n+x[4:]
c5=np.bincount(idx,minlength=n**5).astype(np.float64).reshape((n,)*5); c4=c5.sum(axis=4,keepdims=True)
idx4=((x[:-3]*n+x[1:-2])*n+x[2:-1])*n+x[3:]
c4b=np.bincount(idx4,minlength=n**4).astype(np.float64).reshape((n,)*4)
p4=(c4b+0.05)/(c4b.sum(axis=3,keepdims=True)+0.05*n); lam=c4/(c4+3.0)
p=lam*(c5/np.maximum(c4,1))+(1-lam)*p4[None]
np.log(p).astype(np.float32).tofile(out); np.savetxt(out+'.uni',np.bincount(x,minlength=n)/len(x)); open(out+'.alpha','w').write(alpha+'\n')
