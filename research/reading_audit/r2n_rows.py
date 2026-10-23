# r2n_rows.py scan x0 x1 [y0 y1]: print row-ink profile peaks (text lines) as fractions
import sys
import numpy as np
from PIL import Image
S=r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/r2n'
scan=int(sys.argv[1]); x0=float(sys.argv[2]); x1=float(sys.argv[3]); y0=float(sys.argv[4]) if len(sys.argv)>4 else 0.05; y1=float(sys.argv[5]) if len(sys.argv)>5 else 0.95
im=np.asarray(Image.open(S+'/na/NL-HaNA_3.01.18_401_%04d.jpg'%scan).convert('L')).astype(float)
Y,X=im.shape
a=im[int(y0*Y):int(y1*Y),int(x0*X):int(x1*X)]
ink=(a<np.percentile(a,8)).sum(1).astype(float)
k=np.ones(15)/15; s=np.convolve(ink,k,'same')
pk=[i for i in range(8,len(s)-8) if s[i]==s[i-8:i+9].max() and s[i]>s.mean()*0.8]
out=[]
for i in pk:
    if out and i-out[-1]<25: continue
    out.append(i)
print(' '.join('%.3f'%((i+int(y0*Y))/Y) for i in out))
