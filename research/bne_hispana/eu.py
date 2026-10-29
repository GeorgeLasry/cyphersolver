import requests,json,time,os
S=requests.Session()
def flat(v):
    if isinstance(v,list): return ' | '.join(str(x) for x in v)
    return str(v or '')
def run(query,qf,out,maxn=3000):
    cur='*';rows=[];seen=set();tot=None
    while cur and len(rows)<maxn:
        d={}
        for t in range(4):
            try:
                r=S.get("https://api.europeana.eu/record/v2/search.json",params=dict(wskey='api2demo',query=query,qf=qf,rows=100,cursor=cur,profile='standard'),timeout=60);d=r.json();break
            except Exception: time.sleep(3)
        its=d.get('items',[]); tot=d.get('totalResults',tot)
        if not its: break
        for i in its:
            if i['id'] in seen: continue
            seen.add(i['id'])
            rows.append(dict(id=i['id'],title=flat(i.get('title')),desc=flat(i.get('dcDescription')),year=flat(i.get('year')),type=flat(i.get('dcType')),fmt=flat(i.get('dcFormat')),prov=flat(i.get('dataProvider')),creator=flat(i.get('dcCreator')),link=i.get('guid'),url=i.get('edmIsShownAt')))
        cur=d.get('nextCursor')
    json.dump(rows,open(out,'w',encoding='utf-8'),ensure_ascii=False)
    print(query,qf,len(rows),tot,flush=True)
