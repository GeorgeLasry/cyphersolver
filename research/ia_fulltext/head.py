import sys,re,json
S="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/txt/"
i=sys.argv[1]; poss=[int(x) for x in sys.argv[2:]]
t=re.sub(r"[ \t]+"," ",open(S+i+".txt",encoding="utf8",errors="ignore").read())
rx=re.compile(r"(?:^|\n|\.\]\s)\s*(?:(?:Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)[a-z]*\.? ?\d{0,2}\.? ?)?(\d{1,4})\. ((?:[A-Z\[][^\n]{2,100}? to [^\n]{3,90}))")
for p in poss:
    seg=t[max(0,p-5000):p+400]
    ms=[m for m in rx.finditer(seg) if m.start()<p-max(0,p-5000)+400]
    # last heading before match position
    off=p-max(0,p-5000)
    pre=[m for m in ms if m.start()<=off]
    print(p, "|", pre[-1].group(1),pre[-1].group(2)[:110] if pre else None)
