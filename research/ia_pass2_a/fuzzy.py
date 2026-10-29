import re,glob,os,json,hashlib
T="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/p2txt"
rx=re.compile(r"(?i)bun[s-]?w{0,7}p(?:h|li)w{0,4}(?:ered|cred|cd|ed)b|bun[s-]?(?:de|dec)w{0,8}b|baffled|undecodw*|indecipherw*|bnots+(?:yets+|beens+)?(?:de|dis)?c[iy]phw*|no keyb|bunreadw*")
need=re.compile(r"(?i)c[iy]ph|cipher|figures|characters|numbers")
rows=[];seen=set()
for p in sorted(glob.glob(T+"/*.txt")):
    i=os.path.basename(p)[:-4]
    t=re.sub(r"[ \t]+"," ",open(p,encoding="utf8",errors="replace").read())
    last=-999
    for m in rx.finditer(t):
        if m.start()-last<120: continue
        w=t[max(0,m.start()-250):m.end()+150].replace("\n"," ")
        if not re.search(r"(?i)c[iy]ph|cypher|cipher|ciphr|figur|charact|numbers|cifr|chiffr",w): continue
        last=m.start()
        h=hashlib.md5(re.sub(r"\W","",w[200:330]).lower().encode()).hexdigest()
        if h in seen: continue
        seen.add(h); rows.append({"id":i,"pos":m.start(),"ctx":w})
json.dump(rows,open("fuzzy.json","w"))
print(len(rows))
