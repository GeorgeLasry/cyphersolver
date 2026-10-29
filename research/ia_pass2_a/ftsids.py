import sys,json,urllib.parse,urllib.request,time
def fts(q,page=1,n=50):
    u="https://archive.org/services/search/beta/page_production/?service_backend=fts&hits_per_page=%d&page=%d&user_query=%s"%(n,page,urllib.parse.quote(q))
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=60))["response"]["body"]["hits"]["hits"]
seen={}
for q in sys.argv[1:]:
  for p in (1,2,3):
    try: h=fts(q,p)
    except Exception as e: print("err",e); break
    for x in h:
        f=x["fields"]; seen.setdefault(f["identifier"],(f.get("title"),f.get("year") or f.get("date")))
    if len(h)<50: break
    time.sleep(1)
for k,v in seen.items(): print(k,"|",str(v[0])[:90],"|",v[1])
