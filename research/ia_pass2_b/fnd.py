import re,sys,glob,os
def pth(S,fn):
    p=S+'/'+fn+'.txt'
    return p if os.path.exists(p) else '../ia_meta/_txt/'+fn+'.txt'

S=glob.glob("C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/*/scratchpad/txt2")[0]
fn=sys.argv[1]; snip=sys.argv[2]; b=int(sys.argv[3]) if len(sys.argv)>3 else 900; f=int(sys.argv[4]) if len(sys.argv)>4 else 300
t=re.sub(r"\s+"," ",open(pth(S,fn),encoding="utf8",errors="ignore").read())
n=0
for m in re.finditer(re.escape(snip),t):
    n+=1
    print("=== %s #%d @%d\n%s\n"%(fn,n,m.start(),t[max(0,m.start()-b):m.end()+f]))
    if n>=3: break
if n==0: print("not found")
