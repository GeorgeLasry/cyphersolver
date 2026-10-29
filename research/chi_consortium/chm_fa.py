"""Enumerate CARLI chm_fa (Chicago History Museum finding-aid PDFs), download each (3 s spacing), grep for cipher terms. Keeps only matches in chm_fa_hits.json; PDFs in dl/chm (git-ignore)."""
import json, os, re, time, requests, pymupdf
UA={'User-Agent':'cyphersolver research (catalogue sweep)'}
os.makedirs('dl/chm',exist_ok=True)
items=[]
for p in range(1,10):
    r=requests.get('https://collections.carli.illinois.edu/digital/api/search/collection/chm_fa/searchterm/the/maxRecords/50/page/%d'%p,headers=UA,timeout=60).json()
    items+= [(i['itemId'],i['title']) for i in r['items']]; time.sleep(3)
    if len(items)>=r['totalResults'] or not r['items']: break
json.dump(items,open('chm_fa_items.json','w'))
print(len(items),flush=True)
PAT=re.compile(r'(?i)ciph|cypher|cryptogr|cryptolog|in code\b|coded\b|code (letter|message|telegram|book|word)|secret (writing|code|ink|alphabet)|invisible ink|sympathetic ink|nomenclat|chiffr|cifra|geheimschrift|decod|encod|enciph|hieroglyph')
hits={}
for iid,title in items:
    f='dl/chm/%s.pdf'%iid
    if not os.path.exists(f):
        try:
            r=requests.get('https://collections.carli.illinois.edu/digital/api/collection/chm_fa/id/%s/download'%iid,headers=UA,timeout=120)
            if r.status_code!=200: print('ERR',iid,r.status_code); time.sleep(3); continue
            open(f,'wb').write(r.content)
        except Exception as e: print('ERR',iid,e); continue
        time.sleep(3)
    try:
        t='\n'.join(p.get_text() for p in pymupdf.open(f))
    except Exception as e: print('PDFERR',iid,e); continue
    ms=[t[max(0,m.start()-200):m.end()+250].replace('\n',' ') for m in PAT.finditer(t)]
    if ms: hits[iid]={'title':title,'n':len(ms),'ctx':ms[:15],'pages_chars':len(t)}; print(iid,title[:60],len(ms),flush=True)
    json.dump(hits,open('chm_fa_hits.json','w'),ensure_ascii=False,indent=1)
print('done')
