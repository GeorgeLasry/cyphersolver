import json,urllib.request,time,sys,glob,os
T="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/p2txt"
have=set(os.path.basename(p)[:-4] for p in glob.glob(T+"/*.txt")+glob.glob("../ia_meta/_txt/*.txt")+glob.glob(T+"/../txt/*.txt"))
res={}
for n in range(1,31):
  for suf in ["grea","grea_0","grea_1","greauoft"]:
    i="calendarofstatep%02d%s"%(n,suf)
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request("https://archive.org/metadata/"+i,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))
    except Exception as e: continue
    t=d.get("metadata",{}).get("title")
    if t: print(i,"|",str(t)[:110],"|",d["metadata"].get("date"),"| have" if i in have else "",flush=True); res[i]=t
    time.sleep(.4)
json.dump(res,open("probe.json","w"))
