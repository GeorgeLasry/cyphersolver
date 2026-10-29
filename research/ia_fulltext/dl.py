import json, os, re, sys, time, urllib.request
S=os.environ.get("TXT","C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/txt")
os.makedirs(S,exist_ok=True)
d=json.load(open("hits_raw.json",encoding="utf8"))
ids=sorted({v["id"] for v in d.values()})
extra=[l.strip() for l in open("extra_ids.txt")] if os.path.exists("extra_ids.txt") else []
for i in ids+extra:
    p=os.path.join(S,i+".txt")
    if os.path.exists(p): continue
    try:
        r=urllib.request.urlopen(urllib.request.Request("https://archive.org/download/%s/%s_djvu.txt"%(i,i),headers={"User-Agent":"Mozilla/5.0"}),timeout=120)
        open(p,"wb").write(r.read()); print("ok",i,flush=True)
    except Exception as e: print("fail",i,e,flush=True)
    time.sleep(.3)
