import re,os,sys,json,glob
D=sys.argv[1]
C=r'(chiffr|cifr|cipher|ziffer|zifer|chiffer|cijfer|cyfr|szyfr|ciphr|cifra|Chiffre)'
N=r'(non\s+d[ée]chiffr|ind[ée]chiffr|non\s+r[ée]solu|nicht\s+(?:ent|auf)(?:ziffert|gel[öo]st)|unentziffert|nicht\s+aufgel|unaufgel|non\s+decifr|indecifr|non\s+sciolt|non\s+interpret|sin\s+descifr|no\s+descifr|indescifr|niet\s+ontcijfer|onontcijfer|por\s+decifr|n[ãa]o\s+decifr|indecifr|nicht\s+gel[öo]st|ungel[öo]st|n.a\s+pas\s+[ée]t[ée]\s+d[ée]chiffr|reste\s+ind|not\s+deciph|undeciph|nicht\s+lesbar|unlesbar|unverst[äa]ndlich|non\s+intelligib|sans\s+cl[ée]|non\s+traduit|non\s+expliqu|nicht\s+aufgel[öo]st)'
cr=re.compile(C,re.I); nr=re.compile(N,re.I)
res=[]
for f in sorted(glob.glob(D+'/*.txt')):
    t=open(f,encoding='utf8',errors='ignore').read()
    last=-999
    for m in nr.finditer(t):
        w=t[max(0,m.start()-160):m.end()+160]
        if cr.search(w) and m.start()-last>400:
            last=m.start()
            res.append((os.path.basename(f)[:-4],m.start(),t[max(0,m.start()-500):m.end()+300].replace(chr(10),' ')))
json.dump(res,open(sys.argv[2] if len(sys.argv)>2 else 'matches.json','w'),ensure_ascii=False)
print(len(res))
import collections
c=collections.Counter(r[0] for r in res)
for k,v in c.most_common(80): print(k,v)
