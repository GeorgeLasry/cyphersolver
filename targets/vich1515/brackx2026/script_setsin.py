# Apply image-read decisions for sin/sim: (line, k-th sin token in the line) -> 'sin' (es) or 'sim' (en).
import sys
IMG={(12,1):'sin',(12,2):'sim',(13,1):'sin',(17,1):'sim',(21,1):'sim',(35,2):'sin'}
L0=[l.split() for l in open('v15.txt') if l.strip()]; L1=[l.split() for l in open('v15s.txt') if l.strip()]
for n,(a,b) in enumerate(zip(L0,L1),1):
    k=0
    for j,t in enumerate(a):
        if t=='sin':
            k+=1
            if (n,k) in IMG: b[j]=IMG[(n,k)]
open('v15s.txt','w').write('\n'.join(' '.join(l) for l in L1)+'\n')
print(sum(t=='sim' for l in L1 for t in l),'sim tokens')
