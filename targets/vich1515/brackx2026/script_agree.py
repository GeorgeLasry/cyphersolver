import json,collections,sys
res=json.load(open(sys.argv[1])); signs,groups,ws=json.load(open(sys.argv[1]+'.meta'))
from drv import A
import syl
L=[l.split() for l in open('v15.txt') if l.strip()]; cnt=collections.Counter(t for l in L for t in l)
top=res[:int(sys.argv[2]) if len(sys.argv)>2 else 8]
print('scores',[round(r[0]/3163,3) for r in top])
rows=[]
for gi,g in enumerate(groups):
    c=collections.Counter((ws[r[3][gi]] if r[3][gi]<len(ws) else '?') for r in top)
    v,n=c.most_common(1)[0]; rows.append((cnt[g],g,v,n,dict(c.most_common(3))))
for r in sorted(rows,reverse=True)[:60]: print(r[0],r[1],'->',r[2],f'{r[3]}/{len(top)}',r[4])
def unit(u): return A[u] if u<len(A) else (syl.PAIRS[u-len(A)].upper() if u<len(A)+len(syl.PAIRS) else '_')
print('signs:')
for si,s in enumerate(signs):
    c=collections.Counter(unit(r[2][si]) for r in top); print(s,cnt[s],dict(c.most_common(3)))
