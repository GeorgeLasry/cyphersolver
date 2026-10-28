import csv,collections,glob,sys
K=collections.defaultdict(collections.Counter)
for f in glob.glob('pairs_*.tsv'):
    for r in csv.reader(open(f,encoding='utf8'),delimiter='\t'):
        if len(r)<4 or not r[2].strip().isdigit(): continue
        p=r[3].strip()
        if p and p!='?': K[r[2].strip()][p]+=1
out=[];hit=tot=0
for line in open('ct_p5.txt'):
    w=[]
    for c in line.split():
        tot+=1
        if c in K: hit+=1; w.append(K[c].most_common(1)[0][0]+('' if len(K[c])==1 else '*'))
        else: w.append('['+c+']')
    out.append(' '.join(w))
print('\n'.join(out)); print(f'{hit}/{tot} groups known; key size {len(K)}')
