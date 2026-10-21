import numpy as np, random, itertools
A='abcdefghilmnopqrstuxz'; ai={c:i for i,c in enumerate(A)}; n=21
# my sign codes (v3) -> Amadi demon name (visual match); None = no Amadi counterpart
M={'E':'Acheron','A':'Belzebub','S':'Lybicon','H':'Zael','M':'Lucifer','N':'Radamastra','D':'Radamastra',
   'U':'Astaroth','Y':'Aletho','B':'Minos','B2':'Thesiphon','G':'Sathan','O':'Pluton','P':'Charon','F':'Cerber',
   'Z':'Megera','Q':'Phlegeton','W':'Oziel','J':'Raziel','e':'Sachao','T2':'Xac','R':'Uriel','I':'Gax','Lb':'Gax',
   'T':'Stix','Ws':'Oziel','Et':'Acheron','Rb':'Uriel','Cq':'Phlegeton','Ob':'Pluton','Dd':'Barion','L':'Gax','8':'Dis'}
lines=[l.split() for l in open('v3.txt')]
for variant in ('first','second'):
    def val(code):
        nm=M.get(code); 
        if not nm: return None
        c=nm.lower()[0 if variant=='first' else 1]
        return {'j':'i','v':'u','y':'i','k':'c','w':'u'}.get(c,c)
    out=[]; 
    for l in lines:
        out.append(''.join((val(c) or '?') for c in l))
    print(variant, '\n'+'\n'.join(out))
lp_it=np.fromfile('it5.bin',dtype=np.float32); lp_la=np.fromfile('la5.bin',dtype=np.float32)
def score(s,lp):
    p=[ai[c] for c in s if c in ai]
    return sum(lp[(((p[i-4]*n+p[i-3])*n+p[i-2])*n+p[i-1])*n+p[i]] for i in range(4,len(p)))/max(1,len(p)-4)
toks=[c for l in lines for c in l]
codes=sorted(set(c for c in toks if c in M))
real=''.join(M[c].lower()[0] for c in toks if c in M).replace('y','i').replace('k','c')
for name,lp in (('it',lp_it),('la',lp_la)):
    r=score(real,lp); rs=[]
    vals=[M[c].lower()[0].replace('y','i') for c in codes]
    for t in range(2000):
        random.shuffle(vals); m=dict(zip(codes,vals)); rs.append(score(''.join(m[c] for c in toks if c in M),lp))
    rs=np.array(rs); print(name,'acrophonic %.3f  permuted mean %.3f sd %.3f  z=%.2f'%(r,rs.mean(),rs.std(),(r-rs.mean())/rs.std()))
