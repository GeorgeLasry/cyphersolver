import sys,io,json,re
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8',errors='replace')
from fts import fts
for q in sys.argv[1:]:
    for p in (1,2):
        try: d=fts(q,50,p); hs=d["response"]["body"]["hits"]["hits"]
        except Exception as e: print('ERR',e); break
        print('##',q,p,len(hs))
        for h in hs:
            f=h["fields"]; hl=h.get("highlight") or {}
            sn=(hl.get("text") or [''])[0] if isinstance(hl,dict) else ''
            print(f.get("identifier"),'|',(f.get("title") or '')[:50],'|',f.get("year"),'|',re.sub(r'\s+',' ',sn)[:260])
        if len(hs)<50: break
