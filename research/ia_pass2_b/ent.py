import re,sys,glob,json
S=glob.glob("C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/*/scratchpad/txt2")[0]
# usage: ent.py file pos [fwd]   (pos in whitespace-collapsed 'spaces' text as in matches2.json)
fn=sys.argv[1]; pos=int(sys.argv[2]); fwd=int(sys.argv[3]) if len(sys.argv)>3 else 300
t=open(S+"/"+fn+".txt",encoding="utf8",errors="ignore").read()
t=re.sub(r"[ \t]+"," ",t)
t=re.sub(r"\n"," ",t)
t=re.sub(r"\s+"," ",t)
# positions in matches2 are computed on re.sub(r"[ \t]+"," ") text (newlines kept): recompute offset by mapping
t0=re.sub(r"[ \t]+"," ",open(S+"/"+fn+".txt",encoding="utf8",errors="ignore").read())
seg0=t0[max(0,pos-1800):pos+fwd]
seg=re.sub(r"\s+"," ",seg0)
# find last entry-number heading
hs=[m for m in re.finditer(r"(?<![\d,])(\d{1,4})\. (?=[A-Z])",seg)]
start=hs[-2].start() if len(hs)>=2 else 0
print(seg[max(0,start-60):])
