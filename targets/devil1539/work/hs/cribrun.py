import subprocess, itertools, sys
from concurrent.futures import ThreadPoolExecutor
cribs_it=['antoniomaria','marchantonio','dinari','denari','piacenza','caualiero','ritrouati','trouati','qualloco','tesoro','danari','figliolo']
cribs_la=['pecunia','thesaurus','antoniusmaria','marcusantonius','placentia']
jobs=[]
for tr in ['sch.txt','own.txt','ownm.txt']:
    n=sum(len(l.split()) for l in open(tr))
    for d in (0,1):
        for c in cribs_it: jobs+=[('it5.bin',tr,d,c,o) for o in range(n-len(c)+1)]
        for c in cribs_la: jobs+=[('la5.bin',tr,d,c,o) for o in range(n-len(c)+1)]
def run(j):
    t,tr,d,c,o=j
    out=subprocess.run(['./hscrib',t,tr,'3','400000','0.5','3',str(d),'0',c,str(o)],capture_output=True,text=True).stdout.split('\n')[0]
    return j,out
res=[]
with ThreadPoolExecutor(4) as ex:
    for j,out in ex.map(run,jobs):
        if out.startswith('REAL'): res.append((float(out.split()[1]),j,out))
res.sort(reverse=True)
print(len(jobs),'placements;',len(res),'consistent')
for r in res[:25]: print(round(r[0],3),r[1],r[2][:140])
