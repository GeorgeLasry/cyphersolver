import re,glob,os,json,hashlib
T="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/p2txt"
A=r"(?:cipher|cypher|cyphers|ciphers|chiffres?|cifr[ae]s?|cifre|ziffern|figures|characters|ciphered|cyphered|decipher\w*|decypher\w*)"
B=r"(?:not\s+(?:yet\s+|been\s+)?(?:de-?cipher|de-?cypher|decod|read|solved|explained|interpreted|translated|made\s+out)\w*|un-?de-?c[iy]pher\w*|unsolved|unintelligible|no\s+key|key\s+(?:is\s+)?(?:lost|wanting|missing)|without\s+(?:the\s+)?key|cannot\s+(?:be\s+)?(?:read|deciphered)|illegible|non\s+d[eé]chiffr\w*|sin\s+descifrar)"
rx=re.compile(r"(?is)(?:%s.{0,80}?%s|%s.{0,80}?%s)"%(A,B,B,A))
seen=set(); rows=[]
for p in sorted(glob.glob(T+"/*.txt")):
    i=os.path.basename(p)[:-4]
    t=re.sub(r"[ \t]+"," ",open(p,encoding="utf8",errors="replace").read())
    last=-999
    for m in rx.finditer(t):
        if m.start()-last<200: continue
        last=m.start()
        w=t[max(0,m.start()-450):m.end()+250].replace("\n"," ")
        h=hashlib.md5(re.sub(r"\W","",w[300:600]).lower().encode()).hexdigest()
        if h in seen: continue
        seen.add(h); rows.append({"id":i,"pos":m.start(),"ctx":w})
json.dump(rows,open("matches3.json","w"))
import collections
print(len(rows)); print(collections.Counter(r["id"] for r in rows).most_common(80))
