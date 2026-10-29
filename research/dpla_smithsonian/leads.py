import json,sys
from load import *
d=load()
byp={}
for x in d.values(): byp.setdefault(x['id'][:6],x)
P=sys.argv[1].split(',')
for p in P:
    x=byp.get(p)
    if not x: print(p,'MISSING'); continue
    print('##',p,x['prov'],'|',x['dp'] if isinstance(x['dp'],str) else '', '|', x['url'])
    print(' T:',' / '.join(x['title'])[:150]); print(' D:',' '.join(x['date'])[:40],'| type',x['type'],'| lang',x['lang'],'| cr',x['creator'][:2])
    print(' N:',' '.join(x['desc'])[:520].replace('\n',' '))
