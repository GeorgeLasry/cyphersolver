import json,urllib.parse,urllib.request,time,sys
out=json.load(open("vols_found.json"))
for q in sys.argv[1:]:
  u="https://archive.org/advancedsearch.php?q=%s&fl[]=identifier&fl[]=title&fl[]=date&rows=60&output=json"%urllib.parse.quote(q)
  try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=60))
  except Exception as e: print("err",e); continue
  print("##",q)
  for x in d["response"]["docs"]:
    print(x["identifier"],"|",str(x.get("title"))[:100],"|",str(x.get("date"))[:4])
    if x["identifier"] not in out: out[x["identifier"]]=x
  time.sleep(1)
json.dump(out,open("vols_found.json","w"))
