import json,sys,re
m=json.load(open("matches.json",encoding="utf8"))
pat=re.compile(sys.argv[1]); a=int(sys.argv[2]) if len(sys.argv)>2 else 130; b=int(sys.argv[3]) if len(sys.argv)>3 else 520
for o in m:
    if pat.search(o["id"]): print("##",o["id"],o["pos"],"\n",o["ctx"][a:b],"\n")
