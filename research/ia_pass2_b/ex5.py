import re,os,glob,json,collections
S=glob.glob("C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/*/scratchpad/txt2")[0]
A=r"(?:cipher|cypher|cyphers|ciphers|chiffre|cifra|figures)"
B=r"(?:illegible|unintelligible|no\s+key|key\s+(?:is\s+)?(?:lost|wanting|missing|not\s+found|unknown)|baffl\w+|defied|unsolved|cannot\s+be\s+read|can\s*not\s+be\s+read|obscure|difficult\s+cipher|no\s+decipher|without\s+decipher|decipher\s+(?:is\s+)?(?:lost|wanting|missing)|not\s+(?:been\s+)?(?:found|preserved)|cannot\s+be\s+made\s+out|unread)"
rx=re.compile(r"(?is)(?:%s.{0,60}?%s|%s.{0,60}?%s)"%(A,B,B,A))
skip=re.compile(r"stuart|thurloe|bim_|treasu|cu319240310|birch|bub_gb_sqs|bub_gb_H4|bub_gb_k2|bub_gb_stp|claren|U7Kp|^1[0-9]{7}bsb$")
dirs=[S,"../ia_meta/_txt"]
seen=set();n=0
for d in dirs:
  for fn in sorted(os.listdir(d)):
    if skip.search(fn[:-4]) : continue
    t=re.sub(r"\s+"," ",open(os.path.join(d,fn),encoding="utf8",errors="ignore").read())
    last=-999
    for m in rx.finditer(t):
        if m.start()-last<300: continue
        last=m.start()
        w=t[max(0,m.start()-230):m.end()+150]
        k=re.sub(r"\W","",w[200:300]).lower()
        if k in seen: continue
        seen.add(k); n+=1
        print("[%s] %s\n"%(fn[:28],w))
print(n)
