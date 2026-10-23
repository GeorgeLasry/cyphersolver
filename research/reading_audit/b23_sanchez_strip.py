import sys
from PIL import Image, ImageOps
f,x0,x1,y0,y1,step,out=sys.argv[1],*map(int,sys.argv[2:7]),sys.argv[7]
im=Image.open(f).convert('L')
y=y0;i=0
while y<y1:
    for h,(a,b) in enumerate([(x0,(x0+x1)//2+40),((x0+x1)//2-40,x1)]):
        c=im.crop((a,y-10,b,y+step+25)); c=ImageOps.autocontrast(c,cutoff=1)
        c=c.resize((int(c.size[0]*1.6),int(c.size[1]*1.6)),Image.LANCZOS); c.save('%s_%02d%s.png'%(out,i,'ab'[h]))
    y+=step;i+=1
print(i)
