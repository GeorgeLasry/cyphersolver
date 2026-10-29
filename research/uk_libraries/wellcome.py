import json,sys
from net import get
terms=['cipher','cypher','in cipher','decipher','deciphered','code','secret writing','key to the cipher','cryptogram','cryptography','nomenclator','in code','ciphered','enciphered']
out={}
for t in terms:
    p=1
    while True:
        r=get('https://api.wellcomecollection.org/catalogue/v2/works',params={'query':'"%s"'%t if ' ' in t else t,'pageSize':100,'page':p,'production.dates.from':'1350-01-01','production.dates.to':'1950-12-31'})
        if r.status_code!=200: print(t,p,r.status_code);break
        j=r.json()
        for w in j['results']: out[w['id']]=w
        print(t,p,j['totalResults'],len(out),flush=True)
        if p>=j['totalPages'] or p>=15: break
        p+=1
json.dump(out,open('wellcome_raw.json','w'),ensure_ascii=False)
