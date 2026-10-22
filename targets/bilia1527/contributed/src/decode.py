# 書き起こし（tr_*.txt）を key.tsv で読む。使い方: decode.py 書き起こし [鍵]
import sys,csv,re
def load_key(p):
    k={}
    for r in csv.DictReader(open(p),delimiter='\t'):
        v=r['value']; k[r['token']]='' if v in ('(null)','') else v.strip('<>?')
    return k
def tokens(p):
    out=[]
    for line in open(p):
        line=line.strip()
        if not line or line.startswith('#'): continue
        lab,*toks=line.split(); out.append((lab,toks))
    return out
def norm(t): return t.rstrip('?')
def dec(toks,k):
    s=[]
    for t in toks:
        t0=norm(t)
        if t0 in k: s.append(k[t0])
        else: s.append('['+t0+']')
    return s
if __name__=='__main__':
    k=load_key(sys.argv[2] if len(sys.argv)>2 else 'key.tsv')
    for lab,toks in tokens(sys.argv[1]):
        print(lab,''.join(dec(toks,k)))
