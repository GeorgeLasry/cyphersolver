"""Newberry Transcribe keyword search via /search/results?keyword=..&format=json (all pages), 3 s spacing. Output nt_hits.json."""
import json, sys, time, requests, urllib.parse
UA={'User-Agent':'cyphersolver research (catalogue sweep)'}
res={}; counts={}
for t in sys.argv[1:]:
    r=requests.get('https://nt.newberry.org/search/results?keyword=%s&format=json'%urllib.parse.quote(t),headers=UA,timeout=90)
    try: d=r.json()
    except Exception: d=[]; print('nonjson',t,r.status_code)
    counts[t]=len(d); print(t,len(d),flush=True)
    for x in d: res.setdefault(x['page_permalink'],{**x,'terms':[]})['terms'].append(t)
    time.sleep(3)
json.dump({'counts':counts,'pages':list(res.values())},open('nt_hits.json','w'),ensure_ascii=False,indent=1)
