"""r2h: decode R9416 f.263 sign-label transcription with the hand key (lines 11-16 key, extended).
usage: python r2h_dec263.py <transcription> ; prints line-by-line decode. Upper-case = look-alike/ambiguous.
"""
import sys, re
KEY = {'z':'e','Z':'S','f':'o','j':'z','H':'u','K':'k','s':'a','q':'a','O':'t','Q':'n','b':'d','B':'l','>':'m',
       'A':'g','D':'f','y':'r','m':'i','io':'e','n':'c','g':'h','a':'b','p':'w','4':'s','c':'t','d':'r',
       'X':'[X]','T':'[T]','w':'[w]','L':'s','Y':'d','u':'n','v':'e','S':'n','I':'r','e':'[e]','#':'[#]','i':'i',
       'o':'o','?':'','E':'[E]','+':'+','x':'[x]','2':'[2]'}
def dec(s):
    s = re.sub(r'\{[^}]*\}', '', s)
    out=[]; i=0
    while i < len(s):
        if s.startswith('io', i): out.append('e'); i+=2; continue
        ch=s[i]
        if ch==' ': out.append(' ')
        elif ch in '=|': out.append('-')
        elif ch in KEY: out.append(KEY[ch])
        else: out.append('['+ch+']')
        i+=1
    return ''.join(out)
if __name__ == '__main__':
  for line in open(sys.argv[1], encoding='utf-8'):
    line=line.rstrip('\n')
    m=re.match(r'^(\w?\d+):\s?(.*)$', line)
    if not m or line.startswith('g'): continue
    print(m.group(1), dec(m.group(2)))
