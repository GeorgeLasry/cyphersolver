import re, os, json, sys
S="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/txt2"
dirs=[S,"../ia_meta/_txt"] if "--all" in sys.argv else [S]
A=r"(?:cipher|cypher|cyphers|ciphers|chiffres?|cifr[ae]s?|figures)"
B=r"(?:not\s+(?:yet\s+|been\s+)?(?:de-?cipher|decypher|decod|read|solved|explained|interpreted|translated|intelligible)\w*|undecipher\w*|undecypher\w*|unsolved|unintelligible|illegible|cannot\s+be\s+(?:read|deciphered)|no\s+key|key\s+(?:is\s+)?(?:lost|wanting|missing)|without\s+(?:the\s+)?key|not\s+decoded|uncertain)"
rx=re.compile(r"(?is)(?:%s.{0,45}?%s|%s.{0,45}?%s)"%(A,B,B,A))
only=[a for a in sys.argv[1:] if not a.startswith("--")]
out=[]
for S_ in dirs:
  for fn in sorted(os.listdir(S_)):
    if only and not any(o in fn for o in only): continue
    t=open(os.path.join(S_,fn),encoding="utf8",errors="ignore").read()
    t2=re.sub(r"[ \t]+"," ",t)
    last=-999
    for m in rx.finditer(t2):
        if m.start()-last<200: continue
        last=m.start()
        a=max(0,m.start()-300); b=min(len(t2),m.end()+170)
        out.append({"id":fn[:-4],"pos":m.start(),"ctx":t2[a:b].replace("\n"," ")})
json.dump(out,open("matches2.json","w",encoding="utf8"),ensure_ascii=False,indent=0)
import collections
print(len(out)); print(collections.Counter(o["id"] for o in out).most_common(80))
