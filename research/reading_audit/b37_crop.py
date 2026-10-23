"""b37 crop helper: python b37_crop.py <img> <x0> <y0> <x1> <y1> <out> [width]  (fractions 0-1 or pixels)"""
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
f,x0,y0,x1,y1,out=sys.argv[1:7]; W=int(sys.argv[7]) if len(sys.argv)>7 else 1600
im=Image.open(f); w,h=im.size
def c(v,s):
    v=float(v); return int(v*s) if v<=1 else int(v)
box=(c(x0,w),c(y0,h),c(x1,w),c(y1,h))
cr=im.crop(box)
if cr.width>W: cr=cr.resize((W,int(cr.height*W/cr.width)))
cr.save(out); print(box,cr.size)
