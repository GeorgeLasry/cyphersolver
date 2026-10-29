import re,sys,glob
S=glob.glob("C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/*/scratchpad/txt2")[0]
fn=sys.argv[1]; pos=int(sys.argv[2]); back=int(sys.argv[3]) if len(sys.argv)>3 else 5000; fwd=int(sys.argv[4]) if len(sys.argv)>4 else 600
t=re.sub(r"[ \t]+"," ",open(S+"/"+fn,encoding="utf8",errors="ignore").read())
t=re.sub(r"\n+","\n",t)
# pos is in whitespace-collapsed (spaces only) text, approximate
seg=t[max(0,pos-back):pos+fwd]
print(seg)
