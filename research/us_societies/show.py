import json,re,sys
site=sys.argv[1]; terms=set(sys.argv[2:])
seen={}
for l in open(f'raw/{site}.jsonl',encoding='utf-8'):
    r=json.loads(l)
    if r['term'] in terms and r['id'] not in seen: seen[r['id']]=r
def g(r,k):
    v=r.get(k); 
    if isinstance(v,list): v=' / '.join(map(str,v))
    return re.sub(r'\s+',' ',str(v or ''))
for r in seen.values():
    hl=g(r,'hl')
    print(r['id'],'|',g(r,'title')[:90],'|',g(r,'normalized_date_ssm') or g(r,'date')[:20],'|',(g(r,'repository_ssm') or g(r,'collection_title') or g(r,'parent_unittitles'))[:70],'|',hl[:200])
