# holecheck.py: compares, line by line, the holes of the reading (reading_original.md) and of the English
# (translation_en.md): every word containing [?...] or [...] counts as one hole of its kind.
import re,sys
def lines(p):
    t=open(p).read(); b=t[t.index('```')+3:]; b=b[:b.index('```')]
    out={}
    for l in b.split('\n'):
        m=re.match(r'\s*(\d+)\s+(.*)',l)
        if m: out[int(m.group(1))]=m.group(2)
    return out
def holes(s):
    q=len(re.findall(r'\S*\[\?[^\]]*\]\S*',s)); sup=len(re.findall(r'\S*\[(?!\?)[^\]]+\]\S*',s))
    return q,sup
R=lines('reading_original.md'); E=lines('translation_en.md'); bad=0
for n in sorted(R):
    a=holes(R[n]); b=holes(E.get(n,''))
    if a!=b:
        bad+=1
        if '-v' in sys.argv: print(f'{n:3d} es{a} en{b}\n    ES: {R[n]}\n    EN: {E.get(n,"")}')
        else: print(n,a,b)
print('mismatched lines:',bad,'of',len(R))
