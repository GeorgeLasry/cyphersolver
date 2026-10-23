"""DECODE DOC_*.txt -> tx/R*.txt (C: cipher tokens, M: margin decipherment), same parsing as read.py."""
import re,glob,sys,os
sys.stdout.reconfigure(encoding='utf-8')
exec(open('seg.py',encoding='utf8').read().split('import glob')[0])
os.makedirs('tx',exist_ok=True)
for r in [*range(966,985),1001]:
    f=glob.glob(f'img/DOC_R{r}_*.txt')[0]
    raw=open(f,encoding='utf8',errors='replace').read().lstrip('﻿')
    cl=[re.sub(r'<[^>]*>',' ',l) for l in raw.splitlines() if not l.startswith('#')]
    spaced=sum(bool(re.search(r'\S \S  \S',l)) for l in cl)<3
    out=[];mode='c'
    for line in raw.splitlines():
        if line.startswith('#') and 'margin' in line.lower(): mode='m';continue
        if line.startswith('#IMAGE'): mode='c'; out.append('#'+line[1:]); continue
        if line.startswith('#'): continue
        if mode=='m' and line.startswith('<'): out.append('M: '+re.sub(r'<|>|(CLEAR|PLAIN)TEXT \w+','',line).strip());continue
        c=re.sub(r'<[^>]*>',' | ',line);C=[]
        if spaced:
            for ch in c.split('|'):
                ch=re.sub(r'\s','',ch).replace('?','').replace('_','')
                if ch: C+=seg(ch)
        else:
            for sgm in re.split(r'\s{2,}|\|',c):
                s=sgm.replace(' ','').strip().strip('()=').rstrip('?')
                if s: C.append(s)
        C=[t.replace('?','') for t in C if not re.search(r'CIPHERTEXT|IMAGE|png',t)]
        C=[t for t in C if t]
        if C: out.append('C: '+' '.join(C))
    open(f'tx/R{r}.txt','w',encoding='utf8').write('\n'.join(out)+'\n')
