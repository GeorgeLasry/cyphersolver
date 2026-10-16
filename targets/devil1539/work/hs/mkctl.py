import random, re, unicodedata, collections, sys
def norm(t):
    t=unicodedata.normalize('NFD',t.lower()); t=''.join(c for c in t if not unicodedata.combining(c))
    t=t.replace('j','i').replace('v','u').replace('k','c').replace('y','i').replace('w','u')
    return re.sub('[^a-z]','',t)
S='/tmp/claude-0/-home-user-cyphersolver/2ef8c832-830c-52cb-a6b5-c2867e369991/scratchpad'
src={'it':norm(open('/home/user/cyphersolver/targets/it1583/asl1883.txt',errors='ignore').read()),   # held-out Italian
     'la':norm(open(S+'/corp/la_caesar_gall7.txt',errors='ignore').read()+open(S+'/corp/la_sall.2.txt',errors='ignore').read())}
nsym=int(sys.argv[1]) if len(sys.argv)>1 else 31; L=153
for lang,t in src.items():
    for k in range(6):
        random.seed(1000+k); off=random.randrange(20000,len(t)-1000); pt=t[off:off+L]
        c=collections.Counter(pt); letters=[l for l,_ in c.most_common()]
        # allocate symbols: one each, extra to most frequent letters proportional to frequency
        alloc={l:1 for l in letters}; extra=nsym-len(letters)
        while extra>0:
            l=max(letters,key=lambda l:c[l]/alloc[l]); alloc[l]+=1; extra-=1
        syms=[f's{i}' for i in range(sum(alloc.values()))]; random.shuffle(syms); it=iter(syms)
        hom={l:[next(it) for _ in range(alloc[l])] for l in letters}
        ct=[random.choice(hom[ch]) for ch in pt]
        open(f'ctl_{lang}{k}.txt','w').write(' '.join(ct)+'\n'); open(f'ctl_{lang}{k}.pt','w').write(pt+'\n')
        print(lang,k,len(set(ct)),pt[:60])
