import numpy as np, sys, collections
A='abcdefghilmnopqrstuxz'; ai={c:i for i,c in enumerate(A)}; n=21
lp=np.fromfile(sys.argv[1],dtype=np.float32); uni=np.loadtxt(sys.argv[1]+'.uni'); lam=0.5
for f in sys.argv[2:]:
    pt=open(f).read().strip(); p=[ai[c] for c in pt]; N=len(p)
    s=sum(np.log(uni[p[i]]) for i in range(4))+sum(lp[(((p[i-4]*n+p[i-3])*n+p[i-2])*n+p[i-1])*n+p[i]] for i in range(4,N))
    cnt=np.bincount(p,minlength=n); e=uni*N; chi=((cnt-e)**2/(e+0.5)).sum()
    print(f, 'score %.4f lm %.4f'%((s-lam*chi)/N, s/N))
