import sys
from PIL import Image
# usage: crop.py canvas x0 y0 x1 y1 out [maxw]
c,x0,y0,x1,y1,out=sys.argv[1:7];mw=int(sys.argv[7]) if len(sys.argv)>7 else 2000
im=Image.open(f'img/full/c{int(c):03d}.jpg');W,H=im.size
r=im.crop((int(W*float(x0)),int(H*float(y0)),int(W*float(x1)),int(H*float(y1))))
if r.width>mw: r=r.resize((mw,r.height*mw//r.width))
r.save(out,quality=90);print(r.size)
