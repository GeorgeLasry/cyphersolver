import sys,collections
KEY=dict(kv.split('=') for kv in "AH=g B8=r BO=i CT=p D=NT DH=n FH=n GS=d KH=i LO=t N8=b O=a OT=c PHI=s PSI=t RH=e RS=u SS=q TH=o X=r YH=y Z=a ZH=e ZO=m".split())
for kv in sys.argv[2:] if len(sys.argv)>2 else []: k,v=kv.split('='); KEY[k]=v
L=[l.split() for l in open('v15.txt') if l.strip()]
isg=lambda t: t.islower() and t.isalpha()
def dec(t): return '['+t+']' if isg(t) else KEY.get(t,'<'+t+'>').lower()
mode=sys.argv[1]
if mode=='text':
    for i,l in enumerate(L): print(f'{i+1:3d}',' '.join(dec(t) for t in l))
else:
    T=[t for l in L for t in l]
    for i,t in enumerate(T):
        if t==mode: print(' '.join(dec(x) for x in T[max(0,i-6):i]),' ##',t,'##',' '.join(dec(x) for x in T[i+1:i+7]))
