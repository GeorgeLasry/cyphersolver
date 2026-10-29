import json,os,re,sys,time,urllib.request
S="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/txt2"
os.makedirs(S,exist_ok=True)
have=set()
for p in ["../ia_meta/_txt"]:
    have|={f[:-4] for f in os.listdir(p)}
ids=json.load(open(sys.argv[1]))
pat=re.compile(sys.argv[2] if len(sys.argv)>2 else ".",re.I)
excl=re.compile(r"^sim_|warofrebellion|warrebellion|uswardepartment|officialrecord|journalsofcontin|journalscontine|index|bwb_C0|Domestic|Edward VI",re.I)
for i,v in ids.items():
    t=(v.get("title") or "")
    if i in have or excl.search(i) or excl.search(t) or (v.get("n") or 0)<120: continue
    if not pat.search(t+i): continue
    p=os.path.join(S,i+".txt")
    if os.path.exists(p): continue
    try:
        r=urllib.request.urlopen(urllib.request.Request("https://archive.org/download/%s/%s_djvu.txt"%(i,i),headers={"User-Agent":"Mozilla/5.0"}),timeout=180)
        open(p,"wb").write(r.read()); print("ok",i,t[:50],flush=True)
    except Exception as e: print("fail",i,e,flush=True)
    time.sleep(1)
