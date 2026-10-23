"""Decode tx/R*.txt with keyx.py (Balbases key + sibling additions + values from the margins/images) and measure:
groups in key, and groups read as sense (sense.py). Writes read2/R*.txt."""
import re,glob,sys,os,json
sys.stdout.reconfigure(encoding='utf-8')
exec(open('keyx.py',encoding='utf8').read())
import sense
os.makedirs('read2',exist_ok=True)
FIX={}
if os.path.exists('fix.tsv'):
    for l in open('fix.tsv',encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        p=l.rstrip('\n').split('\t')
        FIX[(p[0],int(p[1]))]=p[2].split()      # rec, token index in tx -> replacement tokens (image reading)
RULES=set((os.environ.get('RULES') or '96,00,fire,27').split(','))
def fixtx(C):
    """Systematic correction of DECODE misreadings found on the R982 images (applied to letters not yet re-imaged)."""
    out=[]
    for t in C:
        if 'fire' in RULES and t.startswith('fire'):
            out.append('d+'); t=t[4:]
            if not t: continue
        if t not in K:
            if '96' in RULES and t in ('96','92','189'): t={'96':'46','92':'42','189':'184'}[t]
            elif '00' in RULES and t=='00': t='xo'
            elif '27' in RULES and re.fullmatch(r'\d+',t):
                for i,ch in enumerate(t):
                    if ch in '23' and t[:i]+'7'+t[i+1:] in K: t=t[:i]+'7'+t[i+1:];break
        if '30' in RULES and t=='30': t='70'
        out.append(t)
    return out
rows=[];T=[0,0,0]
recs=sys.argv[1:] or [f'R{r}' for r in [*range(966,985),1001]]
for rec in recs:
    C=[];M=[]
    src=f'txi/{rec}.txt' if os.path.exists(f'txi/{rec}.txt') else f'tx/{rec}.txt'
    for l in open(src,encoding='utf8'):
        if l.startswith('C:'): C+=l[2:].split()
    M=[l[2:].strip() for l in open(f'tx/{rec}.txt',encoding='utf8') if l.startswith('M:')]
    C2=[]
    for i,t in enumerate(C): C2+=FIX.get((rec,i),[t])
    C2=[t for t in C2 if t!='-']
    if src.startswith('tx/'): C2=fixtx(C2)
    vals=[K.get(t) for t in C2]
    n,ok,flags=sense.measure(vals)
    ink=sum(v is not None for v in vals)
    T[0]+=n;T[1]+=ink;T[2]+=ok
    out=''.join((v if f else ('['+t+']' if v is None else '{'+(v or '·')+'}')) for t,v,f in zip(C2,vals,flags))
    open(f'read2/{rec}.txt','w',encoding='utf8').write(f'# {rec}: {n} groups, in key {ink/n:.1%}, read as sense {ok/n:.1%}\n# [x] = group not in key, {{v}} = value not inside a word\n\n{out}\n\n# margin (DECODE transcription)\n'+'\n'.join(m for m in M if m)+'\n')
    print(f'{rec:6s} {n:5d} key {ink/n:6.1%} sense {ok/n:6.1%}')
print(f'total  {T[0]:5d} key {T[1]/T[0]:6.1%} sense {T[2]/T[0]:6.1%}')
