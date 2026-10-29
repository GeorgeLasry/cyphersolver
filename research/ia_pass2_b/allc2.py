import re,os,sys,glob
S=glob.glob("C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/*/scratchpad/txt2")[0]
pat=re.compile(r"(?i)cipher|cypher|cifra|chiffre|figures|numerals")
skip=re.compile(r"(?i)decipher|decypher|interlin|explanation of|key to|cipher of|cypher of|cipher used by|cipher to|a cipher|the cipher|send.{0,15}cipher|index")
seen=set()
pre=int(os.environ.get("PRE",300)); post=int(os.environ.get("POST",150))
for fn in sys.argv[1:]:
    t=re.sub(r"\s+"," ",open(os.path.join(S,fn),encoding="utf8",errors="ignore").read())
    last=-999
    for m in pat.finditer(t):
        if m.start()-last<250: continue
        w=t[max(0,m.start()-120):m.end()+120]
        if skip.search(w): continue
        last=m.start()
        core=re.sub(r"\W","",t[m.start()-30:m.start()+60]).lower()
        if core in seen: continue
        seen.add(core)
        print("[%s @%d] %s\n"%(fn[:30],m.start(),t[max(0,m.start()-pre):m.end()+post]))
