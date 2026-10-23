# usage: python3 read.py ../transcriptions/n73_tokens.txt ../keys/signs.txt ../keys/groups.txt
import sys
KEY=dict(kv.split('=') for kv in open(sys.argv[2]).read().split())
G=dict(kv.split('=') for kv in open(sys.argv[3]).read().split())
L=[l.split() for l in open(sys.argv[1]) if l.strip()]
isg=lambda t: t.islower() and t.isalpha()
for i,l in enumerate(L):
    out=''
    for t in l:
        if isg(t): out+= G[t] if t in G else ' ['+t+'] '
        else: out+= KEY.get(t,'<'+t+'>').lower()
    print(f'{i+1:3d}',out)
