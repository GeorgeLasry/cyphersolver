import re,sys
from show import load
pat=re.compile(r"(?i)(un-?\s?de-?c[iy]ph|not\s+(?:been\s+|yet\s+)?de-?c[iy]ph|undeciph|c[iy]pher\w*,?\s+(?:is\s+|are\s+)?(?:un|not|without)|no\s+key\b|key\s+(?:not|has\s+not|is\s+(?:lost|missing|wanting))|without\s+(?:a\s+|the\s+)key|in\s+c[iy]pher.{0,40}(?:not|un)|unread|undecod|cipher.{0,30}missing|decipher.{0,20}(?:missing|wanting|lost))")
for i in sys.argv[1:]:
    t=load(i); last=-999
    print("#####",i,len(t))
    for m in pat.finditer(t):
        if m.start()-last<150: continue
        w=t[max(0,m.start()-280):m.end()+180]
        if not re.search(r"(?i)c[iy]ph|figures|characters",w): continue
        last=m.start()
        print(m.start(),"|",re.sub(r"\s+"," ",w))
