import json,urllib.parse,urllib.request,time
Q=['title:(venice AND "state papers" AND english affairs)','title:(venetian AND calendar AND state papers)','title:("English affairs" AND archives AND venice)',
'title:(milan AND "state papers")','title:(rome AND "state papers" AND english affairs)','title:("relating to English affairs" AND rome)',
'title:("Henry VIII" AND spanish AND calendar)','title:("supplement" AND "negotiations between england and spain")','title:("Further supplement")',
'title:("Hatfield House" AND manuscripts)','title:("Cecil" AND manuscripts AND "Hatfield")','title:("Salisbury" AND "Historical Manuscripts Commission")',
'title:("calendar of state papers" AND domestic AND "Charles II")','title:("calendar of state papers" AND domestic AND "James II")','title:("Calendar of State Papers" AND foreign AND Elizabeth)',
'title:("calendar of treasury papers")', 'title:(Venetian AND Rawdon Brown)','creator:("Brown, Rawdon")','title:("Spain" AND "Calendar" AND "Henry VIII" AND "Supplement")',
'title:("State papers, foreign series" AND Elizabeth)','title:("Calendar of state papers, foreign series" AND "Mary")']
out=json.load(open("vols_found.json"))
new={}
for q in Q:
  for p in (1,2):
    u="https://archive.org/advancedsearch.php?q=%s&fl[]=identifier&fl[]=title&fl[]=date&rows=100&page=%d&output=json"%(urllib.parse.quote(q+' AND mediatype:texts'),p)
    try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=60))
    except Exception as e: print("err",q,e); break
    docs=d["response"]["docs"]
    for x in docs:
      if x["identifier"] not in out: new[x["identifier"]]=x
      out[x["identifier"]]=x
    if len(docs)<100: break
    time.sleep(1)
  time.sleep(1)
json.dump(out,open("vols_found.json","w"))
import re
for k,v in sorted(new.items(),key=lambda kv:str(kv[1].get('title')).lower()):
  print(k,'|',str(v.get('title'))[:100],'|',str(v.get('date'))[:4])
