# 対照：鍵の値を記号のあいだでかき混ぜ（1000回）、本物の鍵とイタリア語らしさを比べる。
# イタリア語らしさ＝文字3連の対数尤度の平均。wordfreq の伊語上位5万語を頻度で重み付けし、
# 語の境目をまたぐ3連も入れる（暗号文に語の区切りがないため。語末2字＋語頭1字などを頻度の積で数える）。
# 使い方: python3 control.py ../key.tsv 書き起こし [回数] [--table-only]
#   --table-only : この書簡の文脈から値を決めた記号（source が「この書簡の文脈」）を外す
import sys, math, random, collections, csv
sys.path.insert(0, __file__.rsplit('/',1)[0])
from decode import tokens, norm
from wordfreq import top_n_list, word_frequency
def load(p, table_only):
    k={}
    for r in csv.DictReader(open(p),delimiter='\t'):
        v=r['value']
        if v in ('(null)',''): v=''
        v=v.strip('<>?')
        if ' ' in v or len(v)>4: v=None   # 名前・語の符号は採点から外す
        if table_only and 'この書簡の文脈' in r['source']: v=None
        k[r['token']]=v
    return k
def model():
    tri=collections.Counter(); bi=collections.Counter()
    tr=str.maketrans('àáèéìíòóùú','aaeeiioouu')
    W=[]
    for w in top_n_list('it',50000):
        w2=''.join(c for c in w.lower().translate(tr) if c.isalpha())
        if w2: W.append((w2,word_frequency(w,'it')))
    for w,f in W:
        for i in range(len(w)-2): tri[w[i:i+3]]+=f; bi[w[i:i+2]]+=f
    # 語の境目：上位2000語の語末・語頭の組を頻度の積で
    top=W[:2000]; ends=collections.Counter(); starts=collections.Counter(); e1=collections.Counter(); s1=collections.Counter()
    for w,f in top:
        if len(w)>=2: ends[w[-2:]]+=f; s1[w[0]]+=f
        e1[w[-1]]+=f
        if len(w)>=2: starts[w[:2]]+=f
    T=sum(f for _,f in top)
    for e,fe in ends.items():
        for s,fs in s1.items(): tri[e+s]+=fe*fs/T; bi[e]+=fe*fs/T
    for e,fe in e1.items():
        for s,fs in starts.items(): tri[e+s]+=fe*fs/T; bi[e+s[0]]+=fe*fs/T
    def lp(a): return math.log((tri[a]+1e-9)/(bi[a[:2]]+1e-9*26))
    return lp
def runs(lines,k):
    out=[]
    for _,toks in lines:
        cur=''
        for t in toks:
            v=k.get(norm(t))
            if v is None:
                if len(cur)>=3: out.append(cur)
                cur=''; continue
            cur+=v
        if len(cur)>=3: out.append(cur)
    return out
def score(rs,lp):
    tot=n=0
    for s in rs:
        for i in range(len(s)-2): tot+=lp(s[i:i+3]); n+=1
    return tot/max(n,1), n
if __name__=='__main__':
    args=[a for a in sys.argv[1:] if not a.startswith('--')]
    to='--table-only' in sys.argv
    k=load(args[0],to); lines=tokens(args[1]); N=int(args[2]) if len(args)>2 else 1000
    lp=model()
    real,n=score(runs(lines,k),lp)
    used=sorted({norm(t) for _,ts in lines for t in ts if k.get(norm(t)) not in (None,)})
    vals=[k[t] for t in used]
    random.seed(1); sh=[]
    for _ in range(N):
        v=vals[:]; random.shuffle(v); k2=dict(k); k2.update(zip(used,v))
        sh.append(score(runs(lines,k2),lp)[0])
    ge=sum(s>=real for s in sh)
    print(f'{args[1]} table_only={to} 3連の数={n} 本物={real:.3f} かき混ぜ: 最大={max(sh):.3f} 中央={sorted(sh)[N//2]:.3f} 本物以上={ge}/{N}')
