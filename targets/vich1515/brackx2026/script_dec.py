# usage: dec.py text | dec.py ctx GROUP [GROUP...] | dec.py freq   (keys from signs.txt / groups.txt in this folder)
import sys,collections
S=dict(kv.split('=') for kv in open('signs.txt').read().split())
G=dict(kv.split('=') for kv in open('groups.txt').read().split())
L=[l.split() for l in open('v15x.txt') if l.strip()]
isg=lambda t: t.islower() and t.isalpha()
def d(t):
    if isg(t): return G[t].upper() if t in G else '['+t+']'
    return S.get(t,'<'+t+'>').lower()
def line(l): 
    o=''
    for t in l:
        x=d(t); o+= (' '+x+' ') if x.startswith('[') else x
    return ' '.join(o.split())
T=[t for l in L for t in l]
if sys.argv[1]=='text':
    for i,l in enumerate(L): print(f'{i+1:3d}',line(l))
elif sys.argv[1]=='freq':
    c=collections.Counter(t for t in T if isg(t) and t not in G); tot=sum(1 for t in T if isg(t))
    print('unread group types',len(c),'tokens',sum(c.values()),'of',tot); print(c.most_common(80))
else:
    for g in sys.argv[2:]:
        print('====',g,T.count(g))
        for i,t in enumerate(T):
            if t==g: print('  ',line(T[max(0,i-7):i]),'  ##',g,'##  ',line(T[i+1:i+8]))
