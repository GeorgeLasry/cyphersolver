import re,glob,os,json,hashlib
T="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/p2txt/"
rx=re.compile(r"(?i)(de-?c[iy]pher\w*|key|c[iy]pher\w*)[^.\[\]]{0,40}(?:is\s+|are\s+|being\s+|was\s+|were\s+)?(?:wanting|missing|lost|not\s+(?:extant|preserved|found|forthcoming|attached|with)|has\s+not\s+been\s+found|does\s+not\s+(?:exist|survive)|no\s+longer\s+(?:extant|exists))|without\s+(?:the\s+)?(?:key|decipher\w*)|no\s+decipher\w*|not\s+accompanied\s+by\s+(?:a\s+)?decipher")
rows=[];seen=set()
for p in sorted(glob.glob(T+"*.txt")):
    i=os.path.basename(p)[:-4]
    t=re.sub(r"[ \t]+"," ",open(p,encoding="utf8",errors="replace").read())
    for m in rx.finditer(t):
        w=t[max(0,m.start()-300):m.end()+150].replace("\n"," ")
        if not re.search(r"(?i)c[iy]ph|decipher",w): continue
        h=hashlib.md5(re.sub(r"\W","",w[250:400]).lower().encode()).hexdigest()
        if h in seen: continue
        seen.add(h); rows.append({"id":i,"pos":m.start(),"ctx":w})
json.dump(rows,open("miss.json","w"))
import collections
print(len(rows)); print(collections.Counter(r["id"] for r in rows).most_common(40))
