import re,glob,os,json,sys
T="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/9b550102-0a57-408e-82db-2b82e44e748c/scratchpad/p2txt"
skip=set(os.path.basename(p)[:-4] for p in glob.glob("../ia_meta/_txt/*.txt"))|set(os.path.basename(p)[:-4] for p in glob.glob(T+"/../txt/*.txt"))
C=r"(?:c[iy]ph?ers?|c[iy]ph?ered|c[iy]pher|figures|characters|cifra|cifras|chiffre)"
N=r"(?:un-?\s?(?:de|dec)[iy]ph?ered|not\s+(?:been\s+)?(?:de|dec)[iy]ph?ered|undec[iy]phered|unintelligible|not\s+(?:been\s+)?(?:decoded|read|made out)|(?:no|without)\s+(?:the\s+)?key|illegible|not\s+deciph|sin\s+descifrar|no\s+descifrad|undeciphered|cannot\s+be\s+read|impossible\s+to\s+read|not\s+(?:been\s+)?(?:solved|translated|interpreted))"
rx=re.compile(r"(?is)(%s.{0,60}?%s|%s.{0,60}?%s)"%(C,N,N,C))
out={}
for p in sorted(glob.glob(T+"/*.txt")):
    i=os.path.basename(p)[:-4]
    t=open(p,encoding="utf8",errors="replace").read()
    t=re.sub(r"[ \t]+"," ",t)
    hits=[]
    last=-999
    for m in rx.finditer(t):
        if m.start()-last<300: continue
        last=m.start()
        hits.append((m.start(),t[max(0,m.start()-500):m.end()+300]))
    out[i]=hits
json.dump(out,open("matches2.json","w"))
for k,v in out.items(): print(k,len(v))
