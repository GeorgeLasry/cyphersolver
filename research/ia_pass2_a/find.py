import json,urllib.parse,urllib.request,time,sys
Q=[
 'title:("calendar of state papers" AND venetian)',
 'title:("calendar of letters" AND spain)',
 'title:("calendar of state papers" AND spain)',
 'title:("calendar of state papers" AND milan)',
 'title:("calendar of state papers" AND rome)',
 'title:("calendar of the manuscripts" AND (salisbury OR hatfield))',
 'title:("Historical Manuscripts Commission" AND salisbury)',
 'title:("calendar of state papers" AND foreign AND elizabeth)',
 'title:("calendar of state papers" AND foreign AND (edward OR mary))',
 'title:("calendar of state papers" AND domestic AND (charles OR james))',
 'title:("calendar of state papers" AND (domestic OR foreign) AND (elizabeth OR james OR charles))',
 'title:("further supplement" AND spain)',
 'title:("supplement to volume" AND spain)',
 'title:("letters, despatches, and state papers")',
 'title:("calendar of state papers" AND "henry viii")',
]
out={}
for q in Q:
  for p in (1,2,3):
    u="https://archive.org/advancedsearch.php?q=%s&fl[]=identifier&fl[]=title&fl[]=date&fl[]=imagecount&rows=100&page=%d&output=json"%(urllib.parse.quote(q+' AND mediatype:texts'),p)
    try:
      d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=60))
    except Exception as e: print("err",q,e); break
    docs=d["response"]["docs"]
    for x in docs: out[x["identifier"]]=x
    if len(docs)<100: break
    time.sleep(1)
  time.sleep(1)
json.dump(out,open("vols_found.json","w"),indent=0)
for k,v in sorted(out.items(),key=lambda kv:str(kv[1].get("title"))):
  print(k,"|",str(v.get("title"))[:110],"|",str(v.get("date"))[:4],v.get("imagecount"))
