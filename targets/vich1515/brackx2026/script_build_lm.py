# Spanish char 1-5-gram tables (22 letters, no spaces) and word list, from La Celestina (x2) and Don Quijote.
import re,unicodedata,collections,struct,math,sys
A='abcdefghilmnopqrstuxyz'; K=len(A); IX={c:i for i,c in enumerate(A)}
def body(p):
    t=open(p,encoding='utf-8',errors='ignore').read(); a=t.find('*** START'); b=t.find('*** END'); return t[t.find('\n',a):b]
def words(t):
    t=t.lower().replace('ñ','n').replace('ç','c')
    t=unicodedata.normalize('NFD',t); t=''.join(c for c in t if unicodedata.category(c)!='Mn')
    t=t.translate(str.maketrans('jvkw','iucu'))
    return re.findall(r'[a-z]+',t)
W=words(body('corp/g1619.txt'))*2+words(body('corp/g2000.txt'))
s=''.join(W); x=[IX[c] for c in s if c in IX]; n=len(x); print('letters',n,'words',len(W))
cnt=[collections.Counter() for _ in range(6)]
for o in range(1,6):
    cnt[o]=collections.Counter(tuple(x[i:i+o]) for i in range(n-o+1))
out=open('es.lm','wb')
p_prev=None
for o in range(1,6):
    tab=[0.0]*(K**o)
    for idx in range(K**o):
        t=[];v=idx
        for _ in range(o): t.append(v%K); v//=K
        t=tuple(reversed(t))
        c=cnt[o][t]
        if o==1: p=(c+1)/(n+K)
        else:
            ctx=cnt[o-1][t[:-1]]; lower=math.exp(p_prev[idx%(K**(o-1))])
            p=(c+3*lower)/(ctx+3)
        tab[idx]=math.log(p)
    out.write(struct.pack(f'{K**o}f',*tab)); p_prev=tab
out.close()
wc=collections.Counter(w for w in W if all(c in IX for c in w))
tot=sum(wc.values())
with open('words.txt','w') as f:
    for w,c in wc.most_common(600): f.write(f'{w} {math.log(c/tot):.4f}\n')
print('top',wc.most_common(30))
