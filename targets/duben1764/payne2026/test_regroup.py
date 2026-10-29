from pathlib import Path
import collections,json
root=Path(__file__).resolve().parent
key=collections.defaultdict(list)
for ln in (root/'key218.txt').read_text().splitlines():
 if ln and not ln.startswith('#'):
  k,v=ln.split(maxsplit=1);key[k].append(v)
lines=[]
for ln in (root/'image107_cipher.txt').read_text().splitlines():
 if ln and not ln.startswith('#'):lines.append(ln.split(':',1)[1].split())
tokens=[t.rstrip('?') for ts in lines for t in ts]
digits=''.join(tokens)
results=[]
for drop in [False,True]:
 stream=digits.replace('0','') if drop else digits
 for offset in range(3):
  groups=[stream[i:i+3] for i in range(offset,len(stream)-2,3)]
  hits=sum(t in key for t in groups)
  result={'remove_zeros':drop,'offset':offset,'groups':len(groups),'hits':hits,'fraction':hits/len(groups),'preview':' '.join('/'.join(key.get(t,['['+t+']'])) for t in groups[:80])}
  results.append(result)
(root/'regroup218.json').write_text(json.dumps(results,indent=2)+'\n')
for r in sorted(results,key=lambda r:-r['fraction']):print(r)
