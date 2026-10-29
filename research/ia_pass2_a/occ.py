import sys,re
from show import load
i=sys.argv[1]; w=int(sys.argv[2]) if len(sys.argv)>2 else 160
pat=re.compile(sys.argv[3] if len(sys.argv)>3 else r"(?i)c[iy]ph[ae]r|c[iy]phers|figures")
t=load(i)
body=t[:int(len(t)*0.93)]
last=-9999
for m in pat.finditer(body):
    if m.start()-last<w: continue
    last=m.start()
    print(m.start(),"|",re.sub(r"\s+"," ",body[max(0,m.start()-w):m.start()+w]))
