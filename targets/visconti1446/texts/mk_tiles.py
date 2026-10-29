"""Cut a slip into regular overlapping bands (about two lines each), left and right half, upscaled.
usage: python texts/mk_tiles.py <folio>  -> img/b<folio>_<kk><a|b>.jpg  (run from targets/visconti1446)"""
from PIL import Image
import sys, math
# folio: (canvas, crop box in the full IIIF image, line pitch in px)
S={'30':(30,(4120,690,6950,1570),75),'31':(30,(3900,1860,7050,2870),80),
   '36':(34,(4100,520,7460,2680),77),'37':(34,(3560,2800,7460,4660),72),
   '64':(62,(3920,840,6960,2180),74),'65':(62,(4020,2620,6620,4240),70)}
f=sys.argv[1]; sc=1.5
c,b,p=S[f]
im=Image.open(f'img/c{c}.jpg').crop(b)
W,H=im.size; half=W//2+90
n=math.ceil(H/(2*p))
for k in range(n):
    y0=max(0,int(k*2*p-0.35*p)); y1=min(H,int((k+1)*2*p+0.35*p))
    for j,(x0,x1) in enumerate([(0,half),(W-half,W)]):
        t=im.crop((x0,y0,x1,y1)); t=t.resize((int(t.width*sc),int(t.height*sc)),Image.LANCZOS)
        t.save(f'img/b{f}_{k:02d}{"ab"[j]}.jpg')
print(f,'bands',n)
