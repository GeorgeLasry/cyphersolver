"""Exact order-preserving merge checker.
A plaintext P fits a line pair (A,B) if every letter of A and of B is consumed, in order, by letters of P,
P's remaining letters being 'omitted' (dropped by the encipherer).  Optionally a cipher letter may be a
misprint (consumed against a different plaintext letter) or a null (consumed against nothing).
Cost is lexicographic: (misprints+nulls, omissions)."""
import sys, re
from functools import lru_cache

def clean(s): return re.sub(r"[^A-Za-z]","",s).upper()

def fit(A,B,P,allow_err=True):
    A,B,P = clean(A),clean(B),clean(P)
    la,lb,lp = len(A),len(B),len(P)
    INF = 10**9
    sys.setrecursionlimit(100000)
    @lru_cache(maxsize=None)
    def f(i,j,k):
        # returns (cost, move) ; cost = 1000*(err) + omissions
        if i==la and j==lb and k==lp: return (0,None)
        best=(INF,None)
        if k<lp:
            if i<la and A[i]==P[k]:
                c=f(i+1,j,k+1)[0]
                if c<best[0]: best=(c,'A')
            if j<lb and B[j]==P[k]:
                c=f(i,j+1,k+1)[0]
                if c<best[0]: best=(c,'B')
            c=f(i,j,k+1)[0]+1
            if c<best[0]: best=(c,'-')
            if allow_err:
                if i<la and A[i]!=P[k]:
                    c=f(i+1,j,k+1)[0]+1000
                    if c<best[0]: best=(c,'a')
                if j<lb and B[j]!=P[k]:
                    c=f(i,j+1,k+1)[0]+1000
                    if c<best[0]: best=(c,'b')
        if allow_err:
            if i<la:
                c=f(i+1,j,k)[0]+1000
                if c<best[0]: best=(c,'x')
            if j<lb:
                c=f(i,j+1,k)[0]+1000
                if c<best[0]: best=(c,'y')
        return best
    cost,_=f(0,0,0)
    if cost>=INF: return None
    # reconstruct
    i=j=k=0; out=[]
    while not (i==la and j==lb and k==lp):
        _,mv=f(i,j,k)
        if mv=='A': out.append(A[i]); i+=1; k+=1
        elif mv=='B': out.append(B[j].lower()); j+=1; k+=1
        elif mv=='-': out.append('['+P[k].lower()+']'); k+=1
        elif mv=='a': out.append('{'+A[i]+'>'+P[k]+'}'); i+=1; k+=1
        elif mv=='b': out.append('{'+B[j].lower()+'>'+P[k]+'}'); j+=1; k+=1
        elif mv=='x': out.append('<'+A[i]+'>'); i+=1
        elif mv=='y': out.append('<'+B[j].lower()+'>'); j+=1
    err=cost//1000; om=cost%1000
    return err,om,"".join(out)

def show(A,B,P,allow_err=True):
    r=fit(A,B,P,allow_err)
    if r is None: return f"{P!r}: NO FIT"
    err,om,al=r
    return f"err={err} om={om}  {P}  ::  {al}"

if __name__=="__main__":
    A,B=sys.argv[1],sys.argv[2]
    for P in sys.argv[3:]:
        print(show(A,B,P))
