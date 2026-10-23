"""b29 helper (copy kept in research/reading_audit/b29_kd_lines.py): decode a Kauderbach transcription line by line."""
import json,re,sys,os
sys.path.insert(0,os.getcwd())
sys.argv=[sys.argv[0],'key.json']+sys.argv[1:]
import decode as D
K=D.K
f=sys.argv[2]
lines=open(f,encoding='utf-8-sig').read().split('\n')
for i,l in enumerate(lines,1):
    if l.startswith('#') or not l.strip(): print(i, l[:60]); continue
    parts=re.split(r'(<CLEARTEXT[^>]*>)',l); out=[]
    for p in parts:
        if p.startswith('<CLEARTEXT'): out.append('['+p[13:60]+'...]'); continue
        d=re.sub(r'[^0-9?]','',p)
        # treat ? as unknown digit: drop for decode but flag
        d2=d.replace('?','').replace('5','').replace('8','')
        if not d2: continue
        tk=D.align1(d2)
        out.append('.'.join((K.get(x,'<'+x+'>')) if not x.startswith('*') else '{'+x[1:]+'}' for x in tk))
    print(i, ' '.join(out))
