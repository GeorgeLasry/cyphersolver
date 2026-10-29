import re,sys,glob,os
def pth(S,fn):
    p=S+'/'+fn+'.txt'
    return p if os.path.exists(p) else '../ia_meta/_txt/'+fn+'.txt'

S=glob.glob("C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/*/scratchpad/txt2")[0]
fn=sys.argv[1]
t=re.sub(r"\s+"," ",open(pth(S,fn),encoding="utf8",errors="ignore").read())
for a in sys.argv[2:]:
    p,_,r=a.partition(":"); pos=int(p); b,_,f=(r or "900:200").partition(":")
    print("=== %s @%d\n%s\n"%(fn,pos,t[max(0,pos-int(b)):pos+int(f or 200)]))
