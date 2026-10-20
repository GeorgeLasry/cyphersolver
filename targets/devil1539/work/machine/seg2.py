import cv2, numpy as np, json
from PIL import Image, ImageDraw
IMG='/root/.claude/uploads/2ef8c832-830c-52cb-a6b5-c2867e369991/f5f8b525-image.png'
im=cv2.imread(IMG,0)
b=(im<90).astype(np.uint8)
n,lab,st,cen=cv2.connectedComponentsWithStats(b,8)
centers=[42,100,168,235,302,370,440]
comps=[]
for i in range(1,n):
    x,y,w,h,a=st[i]
    if a<5: continue
    comps.append(dict(id=i,x=int(x),y=int(y),w=int(w),h=int(h),a=int(a),cx=float(cen[i][0]),cy=float(cen[i][1])))
# big flourishes: long thin strokes
for c in comps:
    c['big']= c['h']>75 or c['w']>110
    c['mark']= (not c['big']) and c['a']<45 and max(c['w'],c['h'])<12
    c['line']=min(range(7),key=lambda k:abs(c['cy']-centers[k]))
glyphs=[]
for L in range(7):
    cs=sorted([c for c in comps if c['line']==L and not c['big'] and not c['mark']],key=lambda c:c['x'])
    groups=[]
    for c in cs:
        x0,x1=c['x'],c['x']+c['w']
        for g in groups:
            ov=min(x1,g['x1'])-max(x0,g['x0'])
            if ov>0.35*min(x1-x0,g['x1']-g['x0']):
                g['x0']=min(g['x0'],x0);g['x1']=max(g['x1'],x1);g['y0']=min(g['y0'],c['y']);g['y1']=max(g['y1'],c['y']+c['h']);g['ids'].append(c['id']);break
        else: groups.append(dict(line=L,x0=x0,x1=x1,y0=c['y'],y1=c['y']+c['h'],ids=[c['id']],marks=[]))
    groups.sort(key=lambda g:g['x0'])
    # attach marks to nearest glyph in the line
    for m in [c for c in comps if c['line']==L and c['mark']]:
        if not groups: continue
        def d(g):
            gx=(g['x0']+g['x1'])/2; return abs(m['cx']-gx)-0.5*(g['x1']-g['x0'])
        g=min(groups,key=d)
        if d(g)>14: continue
        gx0,gx1,gy0,gy1=g['x0'],g['x1'],g['y0'],g['y1']
        pos='above' if m['cy']<gy0+2 else 'below' if m['cy']>gy1-2 else 'right' if m['cx']>gx1-2 else 'left' if m['cx']<gx0+2 else 'inside'
        g['marks'].append(pos)
    # drop tiny residual groups (stroke fragments)
    groups=[g for g in groups if (g['x1']-g['x0'])*(g['y1']-g['y0'])>60]
    glyphs+=groups
for i,g in enumerate(glyphs): g['n']=i
json.dump(glyphs,open('glyphs2.json','w'))
print(len(glyphs),[sum(1 for g in glyphs if g['line']==l) for l in range(7)])
# feature: base shape only (components of the group), 32x32
feats=[]
for g in glyphs:
    m=np.isin(lab[g['y0']:g['y1'],g['x0']:g['x1']],g['ids']).astype(np.uint8)*255
    h,w=m.shape; s=max(h,w); pad=np.zeros((s,s),np.uint8); pad[(s-h)//2:(s-h)//2+h,(s-w)//2:(s-w)//2+w]=m
    r=cv2.resize(pad,(32,32),interpolation=cv2.INTER_AREA)
    r=cv2.GaussianBlur(r,(3,3),0)
    feats.append(np.concatenate([r.flatten()/255.0,[w/(h+1e-9)]]))
np.save('feats.npy',np.array(feats))
