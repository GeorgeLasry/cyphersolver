import json,re,sys
m=json.load(open("matches4.json",encoding="utf8"))
a,b=int(sys.argv[1]),int(sys.argv[2])
seen=set();k=0
for i,x in enumerate(m):
    core=re.sub(r"\W","",x["ctx"][230:330]).lower()
    if core in seen: continue
    seen.add(core)
    if "stuart" in x["id"] or "manusc03" in x["id"]: continue
    k+=1
    if k<a or k>b: continue
    print("#%d %s @%d\n  %s\n"%(i,x["id"][:26],x["pos"],x["ctx"]))
