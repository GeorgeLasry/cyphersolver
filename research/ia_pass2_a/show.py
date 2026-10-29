import sys,re,glob,os
T="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/p2txt/"
def load(i):
    p=T+i+".txt"
    if not os.path.exists(p): p="C:/Users/dbour/cypher/research/ia_meta/_txt/"+i+".txt"
    if not os.path.exists(p): p=T+"../txt/"+i+".txt"
    return re.sub(r"[ \t]+"," ",open(p,encoding="utf8",errors="replace").read())
if __name__=="__main__":
    i=sys.argv[1]; pos=int(sys.argv[2]); b=int(sys.argv[3]) if len(sys.argv)>3 else 1500; a=int(sys.argv[4]) if len(sys.argv)>4 else 800
    t=load(i)
    print(re.sub(r"\n+"," / ",t[max(0,pos-b):pos+a]))
