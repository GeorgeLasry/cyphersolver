# Find text-line bands on each page by row ink density; prints counts and centres.
from PIL import Image
import json
out={}
for p in (1,2,3,4):
    im=Image.open(f'img/n73_{p}.jpg').convert('L'); W,H=im.size; px=im.load()
    x0,x1=int(W*0.08),int(W*0.95)
    prof=[sum(1 for x in range(x0,x1,2) if px[x,y]<110) for y in range(H)]
    sm=[sum(prof[max(0,y-4):y+5])/9 for y in range(H)]
    peaks=[y for y in range(10,H-10) if sm[y]==max(sm[max(0,y-12):y+13]) and sm[y]>8]
    ded=[]
    for y in peaks:
        if not ded or y-ded[-1]>18: ded.append(y)
    out[p]=ded; print(p,len(ded),ded)
json.dump(out,open('bands.json','w'))
