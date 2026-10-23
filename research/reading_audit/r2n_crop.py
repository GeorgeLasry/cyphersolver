import sys
from PIL import Image, ImageOps
S=r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/r2n'
scan,x0,y0,x1,y1,w=sys.argv[1:7]; name=sys.argv[7]
src = S+'/na/NL-HaNA_3.01.18_401_%04d.jpg'%int(scan) if not scan.startswith('k') else S+'/key/NL-HaNA_1.10.29_1209_%04d.jpg'%int(scan[1:])
im=Image.open(src).convert('L')
X,Y=im.size
c=im.crop((int(float(x0)*X),int(float(y0)*Y),int(float(x1)*X),int(float(y1)*Y)))
c=ImageOps.autocontrast(c,cutoff=1)
w=int(w); c=c.resize((w,int(c.size[1]*w/c.size[0])),Image.LANCZOS)
c.save(S+'/c/'+name+'.jpg',quality=90); print(S+'/c/'+name+'.jpg',c.size)
