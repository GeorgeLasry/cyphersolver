import json,re,collections
rows=[json.loads(l) for l in open('raw/hung_detail.jsonl',encoding='utf-8')]
good=[r for r in rows if 'ref' in r]
print(len(rows),len(good))
def year(r):
    m=re.search(r'Konv\.? ?[^.]*?\.? ?(1[5-6]\d\d)',r['ref']) or re.search(r'(1[5-6]\d\d)',r['ref'])
    if m: return int(m.group(1))
    m=re.search(r'(1[5-6]\d\d)',r['date']); return int(m.group(1)) if m else 0
def short(r): 
    return re.sub(r'^ÖStA HHStA ','',r['ref'])
def series(r):
    ref=r['ref']
    if 'Verschwörerakten VII' in ref: return 'UA-VII'
    if 'Verschwörerakten IV' in ref: return 'UA-IV'
    if 'Ungarische Akten' in ref: return 'UA-other'
    if 'Türkei I' in ref: return 'T1'
    return '?'
c=collections.defaultdict(list)
for r in good:
    s=series(r)
    if s=='T1':
        y=year(r)
        key='T1<1573' if y<1573 else 'T1-1573-77' if y<=1577 else 'T1-1578-81' if y<=1581 else 'T1-1582-83' if y<=1583 else 'T1-1584-87' if y<=1587 else 'T1-1588-91' if y<=1591 else 'T1-1592-1610' if y<=1610 else 'T1-1611-20' if y<=1620 else 'T1-1621-31' if y<=1631 else 'T1-1632-40' if y<=1640 else 'T1-1641+'
    else: key=s
    c[key].append(r)
for k,v in sorted(c.items()):
    print(k,len(v))
json.dump({k:v for k,v in c.items()},open('hung_clusters.json','w',encoding='utf-8'),ensure_ascii=False)
for k in ['T1<1573','T1-1592-1610','T1-1641+','UA-other','UA-IV','UA-VII','?']:
    for r in c.get(k,[]): print(k,'|',short(r)[:90],'|',r['date'],'|',r['desc'][:140])
