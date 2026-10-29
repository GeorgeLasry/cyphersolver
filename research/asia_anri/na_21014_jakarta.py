"""All Nationaal Archief 2.10.14 items whose description says they are kept in the Arsip Nasional, Jakarta."""
import json, time
from fetch import get
out=open('na_21014_jakarta.jsonl','w',encoding='utf8'); page=1
while True:
    j=get('https://zvt.nationaalarchief.nl/api/search/eads/2.10.14',params={'q':'"Arsip Nasional"','page':page}).json()
    for x in j.get('results',[]): out.write(json.dumps(x,ensure_ascii=False)+'\n')
    if page>=(j.get('pages') or 1): break
    page+=1; time.sleep(0.2)
print(page)
