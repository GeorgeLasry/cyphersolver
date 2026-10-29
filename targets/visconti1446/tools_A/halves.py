"""Single-line zooms, split into N pieces. usage: halves.py desk.jpg prefix 'peaks' x0 x1 N scale halfh"""
import sys
from PIL import Image
im=Image.open(sys.argv[1]); pre=sys.argv[2]; pk=[int(v) for v in sys.argv[3].split()]
x0,x1,N=int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]); s=float(sys.argv[7]); h=int(sys.argv[8])
w=(x1-x0)/N
for i,y in enumerate(pk):
    for j in range(N):
        a=int(x0+j*w-30); b=int(x0+(j+1)*w+30)
        t=im.crop((a,y-h,b,y+h)); t.resize((int(t.width*s),int(t.height*s)),Image.LANCZOS).save(f'{pre}_L{i+1:02d}{"abcd"[j]}.jpg')
