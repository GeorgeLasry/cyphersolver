"""CARLI CONTENTdm (all collections) search API sweep; 3 s spacing. Writes hits.jsonl and counts.json."""
import json, sys, time, urllib.parse, requests
UA={'User-Agent':'cyphersolver research (catalogue sweep)'}
B='https://collections.carli.illinois.edu/digital/api/search/collection/all/searchterm/%s/maxRecords/50/page/%d'
terms=sys.argv[1:]
out=open('hits.jsonl','a',encoding='utf-8'); counts={}
for t in terms:
    page=1; tot=None
    while True:
        r=requests.get(B%(urllib.parse.quote(t),page),headers=UA,timeout=60)
        if r.status_code!=200: print('STOP',r.status_code,t); break
        d=r.json(); tot=d['totalResults']
        for it in d['items']:
            m={f['field']:f['value'] for f in it['metadataFields']}
            out.write(json.dumps({'term':t,'coll':it['collectionAlias'],'id':it['itemId'],'title':it['title'],'meta':m},ensure_ascii=False)+'\n')
        time.sleep(3)
        if page*50>=tot or page>=10 or not d['items']: break
        page+=1
    counts[t]=tot; print(t,tot,flush=True)
json.dump(counts,open('counts_%d.json'%int(time.time()),'w'))
