import requests,json,time
from eu import flat
S=requests.Session();cur='*';rows=[];seen=set()
while cur:
    d={}
    for t in range(5):
        try:
            d=S.get("https://api.europeana.eu/record/v2/search.json",params=dict(wskey='api2demo',query='*',qf=['DATA_PROVIDER:"National Library of Spain"','proxy_dc_type:Manuscritos'],rows=100,cursor=cur,profile='standard'),timeout=90).json();break
        except Exception: time.sleep(4)
    its=d.get('items',[])
    if not its: break
    for i in its:
        if i['id'] in seen: continue
        seen.add(i['id']);rows.append(dict(id=i['id'],title=flat(i.get('title')),desc=flat(i.get('dcDescription')),year=flat(i.get('year')),creator=flat(i.get('dcCreator')),lang=flat(i.get('dcLanguage')),url=i.get('edmIsShownAt')))
    cur=d.get('nextCursor')
    if len(rows)%2000<100: print(len(rows),flush=True)
json.dump(rows,open('raw/bne_all_mss.json','w',encoding='utf-8'),ensure_ascii=False)
print('done',len(rows))
