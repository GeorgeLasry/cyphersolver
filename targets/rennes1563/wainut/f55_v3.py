"""fr. 3181 f. 55, third pass (WAINUT, 27 Oct 2026): the repo's f55_v2.txt tokens with the v3 edits as checked on
the image, decoded and scored, with controls. Standard library only.

    python f55_v3.py            decode v2, v3 (first proposal) and v3 as checked ("ver"), scores and controls
    python f55_v3.py --write    also write f55_v3.txt (the "ver" token list, one cipher line per line)

The decode takes the first value of each token, so word signs such as sc (v2 value "lettre", read "le" in the
reading) show their v2 value here; f55_v3_decryption.md has the line-by-line reading. The score is the share of
letters covered by French words of 3 or more letters (lexicon: ../../dinteville1592/data/fr_words.tsv plus about 55
Middle French forms, the same for every run, controls included). New token names: EE = the ligatured pair of e-signs
read ss [?]; xp=- and the l.7 b=- are nulls; phi=chres is the chi of the xp(ienté) abbreviation.
"""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
import random, re, sys, unicodedata
L=[l.split() for l in open(HERE.parent / 'f55_v2.txt',encoding='utf-8').read().splitlines() if l.strip() and not l.startswith('#')]
assert len(L)==13, len(L)
lex=set()
for l in open(HERE.parent.parent / 'dinteville1592' / 'data' / 'fr_words.tsv',encoding='utf-8'):
    if l.startswith('#'): continue
    w=l.split('\t')[0].strip().lower()
    if len(w)>=2: lex.add(w)
lex |= {'a','y'}
# a few Middle French spellings that the 19th-c lexicon lacks (added equally for all runs incl. controls)
lex |= {'veoy','sceu','descouvert','iceulx','faict','desain','dessain','yssue','ysue','sesions','promect','mesme','trante','delibere','deliberay','vostre','conduicte','monstrer','bone','verray','vera','ay','auss','aussi','mist','avoit','chrestiente','sommes','somes','desquelz','oy','estant','dernierement','concile','fructueuse','utilite','sortir','sortira','entendu','advis','intention','conforme','tenu','chemin','dont','avancer','chacun','part','sessions','decembre','mariage','mariages','pourra','poura'}
def tok(t):
    k,_,v=t.partition('='); v=v.split('|')[0]
    return k,v
def edits(lines,mode):
    L=[list(x) for x in lines]
    if mode in('v3','ver'):
        L[1]=[t if not t.startswith('xp=') else 'xp=-' for t in L[1]]
        L[1]=[('rc=d' if t.startswith('rc=') else t) for t in L[1]]
        L[3]=[('r=y' if t=='r=?' else t) for t in L[3]]
        L[3]=[('gd=me' if t.startswith('gd=') else t) for t in L[3]]
        L[3]=[('dag=con' if t.startswith('dag=') else t) for t in L[3]]
        # l.7 xp-ienté abbreviation
        L[6]=[('phi=chres' if t.startswith('phi=') else ('b=-' if t.startswith('b=') else t)) for t in L[6]]
        # l.9: crop shows y e e u e La (v2 had y e e u e e La); ee = ss
        i=L[8].index('y=y'); assert L[8][i:i+6]==['y=y','e=e','e=e','dv=u','e=e','e=e']
        L[8][i:i+6]=['y=y','EE=ss','dv=u','e=e']
        # l.11: s e e e i -> s e ss i
        i=[j for j in range(len(L[10])) if L[10][j:j+4]==['ct=s','e=e','e=e','e=e']][0]
        L[10][i:i+4]=['ct=s','e=e','EE=ss']
    if mode=='v3':
        # solver: l.8 "La e e z" -> d e s a, last sign struck; l.9 opening b o e
        i=[j for j in range(len(L[7])) if L[7][j:j+4]==['La=d','e=e','e=e','z=a']][0]
        L[7][i:i+4]=['La=d','e=e','E1=s','z=a']; L[7][-1]='xb=-'
        L[8][0]='g=b'; L[8][1]='f4=o'
    if mode=='ver':
        # as checked on the image: crop shows La e [ee] z (three e-signs, last two ligatured); l.8 end b kept; l.9 g=o, f4=n (as in l.8 monstrer)
        i=[j for j in range(len(L[7])) if L[7][j:j+4]==['La=d','e=e','e=e','z=a']][0]
        L[7][i:i+4]=['La=d','e=e','EE=ss','z=a']
        L[8][1]='f4=n'
    return L
def dec(L,vmap=None):
    out=[]
    for line in L:
        s=''
        for t in line:
            k,v=tok(t)
            if vmap is not None and k in vmap: v=vmap[k]
            if v=='-': continue
            s+= '#' if v in('?','') else v
        out.append(s)
    return out
def cover(s):
    best=[0]*(len(s)+1)
    for i in range(1,len(s)+1):
        best[i]=best[i-1]
        for j in range(max(0,i-14),i):
            w=s[j:i]
            if '#' not in w and len(w)>=3 and w in lex: best[i]=max(best[i],best[j]+len(w))
    return best[-1]
def score(lines):
    s=''.join(lines); n=len(s.replace('#',''))
    return sum(cover(x) for x in lines)/max(1,n)
for mode in ('v2','v3','ver'):
    LL=edits(L,mode); d=dec(LL)
    print('==',mode,'coverage(words>=3) = %.3f'%score(d))
    for n,x in enumerate(d,1): print('%2d %s'%(n,x))
# controls on verifier version
LL=edits(L,'ver')
letters={}
for line in LL:
    for t in line:
        k,v=tok(t)
        if len(v)==1 and v.isalpha(): letters[k]=v
keys=list(letters); vals=[letters[k] for k in keys]
random.seed(1); cs=[]
for _ in range(200):
    p=vals[:]; random.shuffle(p); cs.append(score(dec(LL,dict(zip(keys,p)))))
ts=[]
for _ in range(200):
    sh=[random.sample(l,len(l)) for l in LL]; ts.append(score(dec(sh)))
cs.sort(); ts.sort()
print('control shuffled key values: median %.3f max %.3f'%(cs[100],cs[-1]))
print('control shuffled token order: median %.3f max %.3f'%(ts[100],ts[-1]))

if '--write' in sys.argv:
    NL = chr(10)
    with open(HERE / 'f55_v3.txt', 'w', encoding='utf-8', newline=NL) as fh:
        fh.write('# BnF fr. 3181 f. 55, cipher lines 1-13: repo f55_v2.txt with the third-pass edits as checked on the image' + NL +
                 '# (WAINUT, 27 Oct 2026; written by f55_v3.py --write). Token = sign=value[|other value]; value - = null,' + NL +
                 '# ? = unread. EE = the ligatured pair of e-signs, read ss [?]. See f55_v3_decryption.md.' + NL)
        for line in edits(L, 'ver'): fh.write(' '.join(line) + NL)
