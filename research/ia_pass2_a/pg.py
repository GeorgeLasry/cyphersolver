import sys,re
from show import load
def pg(i,pos,span=9000):
    t=load(i)
    seg=t[pos-span:pos+span]
    out=[]
    for m in re.finditer(r"(?:^|\n)\s*(\d{2,3})\s*\n+\s*(?:DOMESTIC|DOMESTIC STATE|[A-Z ,-]{6,40}ELIZABETH|[A-Z ,.-]*CHARLES|[A-Z]+\s+[IVX]+\.?)|(?:DOMESTIC[ —-]+(?:ELIZABETH|CHARLES I+|JAMES I|STATE PAPERS)\.?\s*(\d{2,3}))\b|\b(\d{2,3})\s*\n+\s*DOMESTIC",seg):
        out.append((m.start()-span,m.group(0).strip().replace("\n"," ")[:40]))
    return out
if __name__=="__main__":
    print(pg(sys.argv[1],int(sys.argv[2])))
