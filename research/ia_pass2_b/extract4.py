import re, os, json, sys, glob
S=glob.glob("C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/*/scratchpad/txt2")[0]
Q=r"(?:chiefly|wholly|entirely|mostly|mainly|largely|partly|partially|great\s+part|greater\s+part|nearly\s+all|almost\s+all|much|long\s+passages?|passages?|lines|postscript|portions?|words|names|part|half)"
rx=re.compile(r"(?is)(?:\bin\s+(?:cipher|cypher|ciphers|cyphers|figures|numerals|code)\b|\bciphered\b|\bcyphered\b|\bwritten\s+in\s+(?:cipher|cypher)\b)")
neg=re.compile(r"(?i)decipher|decypher|deciph|interlin|translat|explained|key to|solved|decoded|read by|unciphered")
skipfn=re.compile(r"bim_|thurloe|stuart|treasu|cu319240310|birch|bub_gb_sqs|bub_gb_H4|bub_gb_k2|bub_gb_stp|claren|U7Kp|nicholas|11481219")
only=[a for a in sys.argv[1:] if not a.startswith("--")]
out=[]
for fn in sorted(os.listdir(S)):
    if only and not any(o in fn for o in only): continue
    if not only and skipfn.search(fn): continue
    t=re.sub(r"\s+"," ",open(os.path.join(S,fn),encoding="utf8",errors="ignore").read())
    last=-999
    for m in rx.finditer(t):
        if m.start()-last<150: continue
        pre=t[max(0,m.start()-60):m.start()]
        if not re.search(Q,pre,re.I) and not re.search(r"(?i)\b(are|is|was|were|letter|despatch|all|whole)\s*$",pre): continue
        w=t[max(0,m.start()-250):m.end()+160]
        if neg.search(t[m.start()-80:m.end()+110]): continue
        last=m.start()
        out.append({"id":fn[:-4],"pos":m.start(),"ctx":w})
json.dump(out,open("matches4.json","w",encoding="utf8"),ensure_ascii=False)
import collections
c=collections.Counter(o["id"] for o in out)
print(len(out)); print([(k[:26],v) for k,v in c.most_common(80)])
