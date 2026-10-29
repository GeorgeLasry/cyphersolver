import sys,re
from show import load
def eh(i,pos,back=3500,show=420):
    t=load(i)
    seg=t[max(0,pos-back):pos]
    ms=list(re.finditer(r"(?<![\d.,])(\d{1,4})\.\s+(?=[A-Z\[“\"'(])",seg))
    # choose last match
    if not ms: return "NO HEAD"
    m=ms[-1]
    a=max(0,pos-back)+m.start()
    # also grab date marker lines before
    pre=t[max(0,a-160):a]
    return "PRE: "+re.sub(r"\s+"," ",pre)+"\n  HEAD: "+re.sub(r"\s+"," ",t[a:a+show])+"\n  ... TAIL: "+re.sub(r"\s+"," ",t[pos-120:pos+200])
if __name__=="__main__":
    for a in sys.argv[1:]:
        i,p=a.split(":"); print("==",a); print(" ",eh(i,int(p)))
