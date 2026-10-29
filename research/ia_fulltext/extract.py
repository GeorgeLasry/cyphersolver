import re, os, json, sys
S="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/txt"
A=r"(?:cipher|cypher|cyphers|ciphers|chiffres?|chiffr[ée]e?s?|cifr[ae]s?|cifre|ziffern|chiffern|chiffreschrift|geheimschrift|cijfer\w*)"
B=r"(?:not\s+(?:yet\s+|been\s+)?(?:de-?cipher|decypher|decod|read|solved|explained|interpreted|translated)\w*|undecipher\w*|undecypher\w*|unsolved|unintelligible|non\s+d[ée]chiffr\w*|ind[ée]chiffr\w*|non\s+decifrat\w*|indecifrat\w*|sin\s+descifrar|no\s+descifrad\w*|nicht\s+(?:ent|auf)\w+|niet\s+ontcijferd|cannot\s+read|can\s*not\s+(?:read|decipher)|no\s+key|key\s+(?:is\s+)?lost)"
rx=re.compile(r"(?is)(?:%s.{0,40}?%s|%s.{0,40}?%s)"%(A,B,B,A))
out=[]
for fn in sorted(os.listdir(S)):
    t=open(os.path.join(S,fn),encoding="utf8",errors="ignore").read()
    t2=re.sub(r"[ \t]+"," ",t)
    for m in rx.finditer(t2):
        a=max(0,m.start()-350); b=min(len(t2),m.end()+200)
        out.append({"id":fn[:-4],"pos":m.start(),"ctx":t2[a:b].replace("\n"," ")})
json.dump(out,open("matches.json","w"),ensure_ascii=False,indent=0)
import collections
print(len(out)); print(collections.Counter(o["id"] for o in out).most_common(60))
