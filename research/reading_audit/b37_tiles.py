"""b37: cut a page into overlapping half-width tiles at 1.6x: python b37_tiles.py <img> <prefix> <x0> <x1> <y0> <y1> <band>"""
import sys
from PIL import Image
f,pre=sys.argv[1:3]; x0,x1,y0,y1,band=map(int,sys.argv[3:8])
im=Image.open(f).convert('RGB'); mid=(x0+x1)//2; k=0
y=y0
while y<y1:
    for (a,b,t) in ((x0,mid+60,'L'),(mid-60,x1,'R')):
        c=im.crop((a,y,b,min(y+band+40,im.height))); c=c.resize((int(c.width*1.6),int(c.height*1.6)))
        c.save(f'{pre}{k:02d}{t}.jpg'); 
    k+=1; y+=band
print(k)
