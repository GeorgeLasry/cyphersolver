import re,glob,os,json,hashlib,sys
T="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/p2txt"
rx=re.compile(r"(?i)(un-?\s?de-?c[iy]ph|not\s+(?:been\s+|yet\s+)?de-?c[iy]ph|undeciph|c[iy]pher\w*,?\s+(?:is\s+|are\s+)?(?:un|not)|\bun-?read|no\s+key\b|key\s+(?:not|has\s+not)\s+(?:been\s+)?found|without\s+(?:a\s+|the\s+)key|partly\s+in\s+c[iy]ph|in\s+c[iy]pher.{0,40}(?:not|un))")
rows=[];seen=set()
for p in sorted(glob.glob(T+"/*.txt")):
    i=os.path.basename(p)[:-4]
    t=re.sub(r"[ \t]+"," ",open(p,encoding="utf8",errors="replace").read())
    last=-999
    for m in rx.finditer(t):
        if m.start()-last<150: continue
        last=m.start()
        w=t[max(0,m.start()-300):m.end()+200].replace("\n"," ")
        h=hashlib.md5(re.sub(r"\W","",w[250:420]).lower().encode()).hexdigest()
        if h in seen: continue
        seen.add(h); rows.append({"id":i,"pos":m.start(),"ctx":w})
json.dump(rows,open("matches4.json","w"))
import collections
print(len(rows)); print(collections.Counter(r["id"] for r in rows).most_common(100))
