"""SIKN national archival network search API (svc-search-sikn.anri.go.id/archives); writes sikn_hits.jsonl.
Open JSON endpoint used by sikn.anri.go.id's own search page (found in its Nuxt bundle)."""
import json, sys, time
from fetch import get
API='https://svc-search-sikn.anri.go.id/archives'
out=open('sikn_hits.jsonl','a',encoding='utf8')
for term in sys.argv[1:]:
    page=1; n=0
    while True:
        try:
            r=get(API,params={'page':page,'limit':100,'qword':term}); j=r.json()
        except Exception as e:
            print(term,'ERR',e); break
        data=j.get('data') or []; ps=j.get('pageSummary') or {}
        for d in data:
            out.write(json.dumps({'term':term,'id':d.get('id'),'identifier':d.get('identifier'),'title':d.get('title'),
              'start':d.get('startDate'),'end':d.get('endDate'),'scope':d.get('scopeContent'),'extent':d.get('extentMedium'),
              'level':d.get('levelName'),'n_digital':len(d.get('digitalObject') or []),
              'repo':[x.get('name') for x in d.get('repositories') or []],'fond':(d.get('fond') or {}).get('name'),
              'actors':[x.get('name') for x in d.get('actors') or []],'slug':d.get('slug')},ensure_ascii=False)+'\n'); n+=1
        tot=ps.get('total') or ps.get('totalData') or ps.get('total_data')
        if page==1: print(term,'summary',ps,flush=True)
        if len(data)<100 or page>=50: break
        page+=1; time.sleep(0.5)
    print(term,'rows',n,flush=True)
