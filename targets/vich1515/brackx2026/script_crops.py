# Crops of transcription lines (1-based index into v15.txt) with their sin/sim sequence, 4 lines per sheet.
import json,sys
from PIL import Image, ImageDraw
B=json.load(open('bands.json')); B={int(k):v for k,v in B.items()}
B[1]=B[1][1:]   # page 1: first band is the docket
L=[l.split() for l in open('v15.txt') if l.strip()]
rows={}
for r in open('splitsin.tsv'):
    i,j,l,rt,m,ch=r.rstrip('\n').split('\t'); rows[(int(i),int(j))]=(float(m),ch,l,rt)
def where(n):
    if n<=38: return 1,n
    if n<=76: return 2,n-38
    if n<=113: return 3,n-76
    return 4,n-113
lines=sorted({i for (i,j),(m,ch,l,rt) in rows.items() if abs(m)<1 and where(i)[0]<4})
print('lines',len(lines),lines)
for s in range(0,len(lines),4):
    grp=lines[s:s+4]; tiles=[]
    for n in grp:
        p,k=where(n); y=B[p][k-1]; im=Image.open(f'img/n73_{p}.jpg')
        c=im.crop((60,y-24,im.width-20,y+22)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); tiles.append((n,c))
    H=sum(c.height+26 for _,c in tiles); Wd=max(c.width for _,c in tiles)
    sheet=Image.new('RGB',(Wd,H),'white'); d=ImageDraw.Draw(sheet); y=0
    for n,c in tiles:
        seq=[('C' if abs(rows[(n,j+1)][0])<1 else '')+str(len([1 for t in L[n-1][:j] if t=='sin'])+1) for j,t in enumerate(L[n-1]) if t=='sin']
        d.text((5,y+5),f'line {n}: sin tokens in order: '+' '.join(seq)+'   (C = close call)',fill='red'); y+=26
        sheet.paste(c,(0,y)); y+=c.height
    sheet.save(f'sheet_{s//4}.png')
print('sheets',(len(lines)+3)//4)
