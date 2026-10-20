import numpy as np, json, cv2
from skimage.feature import hog
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from PIL import Image, ImageDraw
IMG='/root/.claude/uploads/2ef8c832-830c-52cb-a6b5-c2867e369991/f5f8b525-image.png'
im=cv2.imread(IMG,0); b=(im<90).astype(np.uint8); n,lab,st,cen=cv2.connectedComponentsWithStats(b,8)
G=json.load(open('glyphs2.json'))
H=[]
for g in G:
    m=np.isin(lab[g['y0']:g['y1'],g['x0']:g['x1']],g['ids']).astype(np.uint8)*255
    h,w=m.shape; s=max(h,w)+4; pad=np.zeros((s,s),np.uint8); pad[(s-h)//2:(s-h)//2+h,(s-w)//2:(s-w)//2+w]=m
    r=cv2.resize(pad,(40,40),interpolation=cv2.INTER_AREA)
    f=hog(r,orientations=9,pixels_per_cell=(8,8),cells_per_block=(2,2))
    H.append(np.concatenate([f,[np.log((w+1)/(h+1))*2]]))
H=np.array(H)
for k in (20,25,30,35,40,45):
    lb=AgglomerativeClustering(n_clusters=k,linkage='ward').fit_predict(H)
    print(k, round(silhouette_score(H,lb),3))
k=35; lb=AgglomerativeClustering(n_clusters=k,linkage='ward').fit_predict(H)
# reorder clusters by size
order=sorted(range(k),key=lambda c:-(lb==c).sum()); rm={c:i for i,c in enumerate(order)}; lb=np.array([rm[c] for c in lb])
np.save('labels.npy',lb)
# contact sheet: one row per cluster
S=56; maxper=14
sheet=Image.new('L',(60+maxper*S,k*S),255); d=ImageDraw.Draw(sheet)
for c in range(k):
    d.text((4,c*S+20),f'c{c} ({(lb==c).sum()})',fill=0)
    for j,i in enumerate([i for i in range(len(G)) if lb[i]==c][:maxper]):
        g=G[i]; p=Image.fromarray(im[g['y0']-3:g['y1']+3,g['x0']-3:g['x1']+3])
        sc=min((S-4)/p.width,(S-4)/p.height); p=p.resize((max(1,int(p.width*sc)),max(1,int(p.height*sc))))
        sheet.paste(p,(60+j*S,c*S+2))
sheet.save('clusters.png'); print(sheet.size)
