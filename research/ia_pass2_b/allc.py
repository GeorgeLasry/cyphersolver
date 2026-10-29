import re,os,sys,glob
S=glob.glob("C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/*/scratchpad/txt2")[0]
pat=re.compile(r"(?i)cipher|cypher|ciphre|cyphr|cifra|chiffre")
seen=set()
pre=int(os.environ.get("PRE",220)); post=int(os.environ.get("POST",160))
for fn in sys.argv[1:]:
    t=re.sub(r"\s+"," ",open(os.path.join(S,fn),encoding="utf8",errors="ignore").read())
    last=-999
    for m in pat.finditer(t):
        if m.start()-last<250: continue
        last=m.start()
        core=re.sub(r"\W","",t[m.start()-30:m.start()+60]).lower()
        if core in seen: continue
        seen.add(core)
        print("[%s @%d] %s\n"%(fn[:30],m.start(),t[max(0,m.start()-pre):m.end()+post]))
