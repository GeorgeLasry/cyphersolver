import sys,re,os
import io;sys=__import__("sys");sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf8",errors="replace")
S='C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/'
vol,pat=sys.argv[1],sys.argv[2]; pre=int(sys.argv[3]) if len(sys.argv)>3 else 500; post=int(sys.argv[4]) if len(sys.argv)>4 else 250
for d in ('txt','txt3','txt4'):
    p=S+d+'/'+vol+'.txt'
    if os.path.exists(p): break
t=re.sub(r'\s+',' ',open(p,encoding='utf8',errors='ignore').read())
last=-9999
for m in re.finditer(pat,t,re.I):
    if m.start()-last<pre//2: continue
    last=m.start()
    print('@%d: %s\n'%(m.start(),t[max(0,m.start()-pre):m.end()+post]))
