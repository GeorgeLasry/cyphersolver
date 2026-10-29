import json,sys
m=json.load(open("matches2.json",encoding="utf8"))
a=int(sys.argv[1]);b=int(sys.argv[2]); f=sys.argv[3] if len(sys.argv)>3 else ""
k=0
for i,x in enumerate(m):
    if f and f not in x["id"]: continue
    k+=1
    if k<a or k>b: continue
    print("#%d %s @%d\n  %s\n"%(i,x["id"],x["pos"],x["ctx"]))
