"""Item-level search of Nationaal Archief inventories that describe Jakarta-held items (2.10.14 etc.) for code terms;
writes na_jakarta_hits.jsonl."""
import json, sys, time
from fetch import get
ARCH=['2.10.14','2.10.17','2.10.36.15','2.10.36.22','2.10.29','2.10.62','2.13.132','2.10.50']
TERMS=['code','codetelegram','codetelegrammen','gecodeerd','cijfer','cijfertelegram','cijfertelegrammen','sleutel','codeboek','ontcijferd','gedecodeerd','sandi','onderschept','onderschepte','geheimschrift','decodering','radiogram','Arsip Nasional']
out=open('na_jakarta_hits.jsonl','w',encoding='utf8')
for a in ARCH:
    for t in TERMS:
        page=1
        while True:
            try: j=get(f'https://zvt.nationaalarchief.nl/api/search/eads/{a}',params={'q':t,'page':page}).json()
            except Exception as e: print(a,t,'ERR',e); break
            res=j.get('results',[])
            for x in res: out.write(json.dumps({'arch':a,'term':t,**x},ensure_ascii=False)+'\n')
            if page==1: print(a,t,j.get('pages'),len(res),flush=True)
            if page>=(j.get('pages') or 1) or page>=20: break
            page+=1; time.sleep(0.3)
