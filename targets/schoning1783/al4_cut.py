import sys
from PIL import Image
# usage: al4_cut.py name x0 y0 x1 y1 [scale]
n,x0,y0,x1,y1=sys.argv[1],*map(int,sys.argv[2:6]); s=int(sys.argv[6]) if len(sys.argv)>6 else 3
im=Image.open('img/full138.jpg').crop((x0,y0,x1,y1))
im=im.resize((im.width*s,im.height*s),Image.LANCZOS); im.save(f'crops/al4_{n}.png')
