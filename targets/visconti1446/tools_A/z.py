"""zoom: z.py desk.jpg yc x0 x1 out [scale] [half-height]"""
import sys
from PIL import Image
im=Image.open(sys.argv[1]); yc=int(sys.argv[2]); x0,x1=int(sys.argv[3]),int(sys.argv[4])
s=float(sys.argv[6]) if len(sys.argv)>6 else 2.5; h=int(sys.argv[7]) if len(sys.argv)>7 else 55
t=im.crop((x0,yc-h,x1,yc+h)); t.resize((int(t.width*s),int(t.height*s)),Image.LANCZOS).save(sys.argv[5])
