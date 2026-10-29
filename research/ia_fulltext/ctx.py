import sys,re
S="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/txt/"
i=sys.argv[1]; a=int(sys.argv[2]); pre=int(sys.argv[3]) if len(sys.argv)>3 else 700; post=int(sys.argv[4]) if len(sys.argv)>4 else 150
t=re.sub(r"[ \t]+"," ",open(S+i+".txt",encoding="utf8",errors="ignore").read())
print(t[max(0,a-pre):a+post].replace("\n"," "))
