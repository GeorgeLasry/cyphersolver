# r2n_line.py scan x0 x1 name y [y ...]: each line cut [y-UP,y+DN] at native size x1.4, split into 3 overlapping pieces stacked
import sys, os
from PIL import Image, ImageOps
S=r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/r2n'
scan=int(sys.argv[1]); x0=float(sys.argv[2]); x1=float(sys.argv[3]); name=sys.argv[4]; ys=[float(v) for v in sys.argv[5:]]
im=Image.open(S+'/na/NL-HaNA_3.01.18_401_%04d.jpg'%scan).convert('L'); X,Y=im.size
up=float(os.environ.get('UP','0.03')); dn=float(os.environ.get('DN','0.012')); n=int(os.environ.get('N','3'))
parts=[]; w=(x1-x0)/n
for y in ys:
    for k in range(n):
        a=x0+k*w-0.01; b=x0+(k+1)*w+0.01
        c=ImageOps.autocontrast(im.crop((int(a*X),int((y-up)*Y),int(b*X),int((y+dn)*Y))),cutoff=1)
        c=c.resize((1750,int(c.size[1]*1750/c.size[0])),Image.LANCZOS); parts.append(c)
H=sum(p.size[1]+6 for p in parts); s=Image.new('L',(1750,H),0); yy=0
for p in parts: s.paste(p,(0,yy)); yy+=p.size[1]+6
s.save(S+'/c/'+name+'.jpg',quality=88); print(name,s.size)
