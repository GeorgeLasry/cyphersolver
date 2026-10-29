"""Dump every ANRI record published on SIKN (repository 3bcfbe8a...) to anri_sikn_all.jsonl (titles only)."""
import json, time
from fetch import get
API='https://svc-search-sikn.anri.go.id/archives'; RID='3bcfbe8a-34bc-4f7c-a997-01b961e085b9'
out=open('anri_sikn_all.jsonl','w',encoding='utf8')
page=1
while True:
    for a in range(3):
        try: j=get(API,params={'page':page,'limit':100,'repositories':RID}).json(); break
        except Exception as e: time.sleep(5)
    data=j.get('data') or []
    for d in data:
        out.write(json.dumps({'id':d.get('id'),'identifier':d.get('identifier'),'title':d.get('title'),'start':d.get('startDate'),
          'end':d.get('endDate'),'scope':d.get('scopeContent'),'level':d.get('levelName'),'n_digital':len(d.get('digitalObject') or []),
          'fond':(d.get('fond') or {}).get('name'),'slug':d.get('slug')},ensure_ascii=False)+'\n')
    if page%50==0: print(page,j.get('pageSummary'),flush=True)
    if len(data)<100: break
    page+=1; time.sleep(0.3)
print('done',page)
