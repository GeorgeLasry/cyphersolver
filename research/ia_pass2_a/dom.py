import re,glob,os,json,hashlib
T="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/p2txt/"
ids=[os.path.basename(p)[:-4] for p in glob.glob(T+"*.txt")]
dom=[i for i in ids if re.match(r"cu319240917|bub_gb_(GWQ|og3|c63|9it|ghI|Cif|RH0|fsAZ|Gna)|calendarstatepa0.(hami|brit|unkn|gree|leva)|calendarofstatep0000(john|will|mary|unse)|10278843|10278844|10278845|10278848|10278853|10278858|10278859|11355763|11576082|11576097|calendarofstatep11grea|sim_.*charles-ii",i)]
print(len(dom))
rx=re.compile(r"(?i)(?:in|partly in|written in|part in|mostly in|chiefly in|entirely in|wholly in)\s+(?:c[iy]pher|characters|figures|numbers|numerals|symbols|short-?hand)s?\b")
seen=set();rows=[]
for i in dom:
    t=re.sub(r"[ \t]+"," ",open(T+i+".txt",encoding="utf8",errors="replace").read())
    for m in rx.finditer(t):
        w=t[max(0,m.start()-350):m.end()+200]
        if re.search(r"(?i)decipher|decypher|deciphered|decyphered|translat|key|explained|numbered",w[250:]) : continue
        w=w.replace("\n"," ")
        h=hashlib.md5(re.sub(r"\W","",w[300:450]).lower().encode()).hexdigest()
        if h in seen: continue
        seen.add(h); rows.append({"id":i,"pos":m.start(),"ctx":w})
print(len(rows))
json.dump(rows,open("dom.json","w"))
import collections
print(collections.Counter(r["id"] for r in rows).most_common(20))
