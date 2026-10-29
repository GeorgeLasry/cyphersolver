import json,os,re,sys,time,urllib.request,glob
T="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/p2txt"
os.makedirs(T,exist_ok=True)
have=set(os.path.basename(p)[:-4] for p in glob.glob("../ia_meta/_txt/*.txt")+glob.glob(T+"/../txt/*.txt")+glob.glob(T+"/*.txt"))
d=json.load(open("vols_found.json"))
extra=[l.strip() for l in open("extra_ids.txt")] if os.path.exists("extra_ids.txt") else []
pat=re.compile(r"ZZZZnomatch")
ids=[]
for k,v in d.items():
    t=str(v.get("title"))
    if k.startswith("sim_"): continue
    if re.search(r"(?i)index|treasury|philadelphia|insurance|hybridity|four years|correspondence of king|Ireland",t): continue
    if pat.search(t): ids.append(k)
ids+=extra
print(len(ids),flush=True)
for i in ids:
    if i in have or os.path.exists(f"{T}/{i}.txt"): continue
    try:
        r=urllib.request.urlopen(urllib.request.Request(f"https://archive.org/download/{i}/{i}_djvu.txt",headers={"User-Agent":"Mozilla/5.0"}),timeout=180)
        open(f"{T}/{i}.txt","wb").write(r.read()); print("ok",i,flush=True)
    except Exception as e: print("fail",i,e,flush=True)
    time.sleep(1)
print("done")
