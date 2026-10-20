"""Verify both documents, their CTTS exports, edition and package checksums. Standard library only."""
from pathlib import Path
import importlib.util, json, hashlib, sys, collections
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('ctts_verify',R/'ctts/Codex_verify.py')
v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
colors,key,projects,spec=v.read_projects(R/'ctts')
data=json.loads((R/'edition.json').read_text(encoding='utf-8'))
totals=collections.Counter();used=set()
for doc in data['documents']:
 stem=doc['stem'];rows=projects[stem];d=spec['documents'][stem]
 edits=v.render_edits(rows,d)
 alias='' if doc['id']=='R7898' else 'companion/'
 assert (R/(alias+'edited.txt')).read_text(encoding='utf-8')==edits
 assert (R/f'ctts/edited/{stem}_edits.txt').read_text(encoding='utf-8')==edits
 assert len(doc['rows'])==len(rows)
 for row,rec,base in zip(rows,doc['rows'],d['rows']):
  assert rec['boxes']==row and rec['line']==base['line']
  assert rec['suffix']==base.get('suffix','')
  assert len(rec['segments'])==len(base['segments'])
  for seg,orig in zip(rec['segments'],base['segments']):
   assert all(seg[k]==val for k,val in orig.items())
   a,b=seg['tokens'];boxes=row[a-1:b]
   expected=orig['text'] if orig['kind']=='clear_box' else orig.get('reading',orig.get('separator','').join(x['value'] for x in boxes))
   assert seg['text']==expected
  for box in row:
   if box['label']!='[Plaintext]':assert (R/'ctts/icons'/(colors[box['c']][0]+'.png')).is_file()
 cipher=[b for row in rows for b in row if b['label']!='[Plaintext]']
 stats=dict(lines=len(rows),boxes=sum(map(len,rows)),cipher=len(cipher),clear=sum(map(len,rows))-len(cipher),distinct=len({b['label'] for b in cipher}),assigned=sum(b['value']!='?' for b in cipher),provisional=sum(key[b['label']].islower() for b in cipher),unresolved=sum(b['value']=='?' for b in cipher))
 assert stats==doc['statistics'];totals.update({k:n for k,n in stats.items() if k!='distinct'});used.update(b['label'] for b in cipher)
 tokens=''.join(f'L{i:02d}: '+' '.join(b['label'] for b in row if b['label']!='[Plaintext]')+'\n' for i,row in enumerate(rows,1))
 assert (R/(alias+'cipher_tokens.txt')).read_text(encoding='utf-8')==tokens
 print('PASS',doc['shelfmark'],stats)
totals['distinct']=len(used);assert dict(totals)==data['statistics']
assert (R/'ctts/edited/edits.txt').read_text(encoding='utf-8')==''.join(stem+'\n'+v.render_edits(rows,spec['documents'][stem]) for stem,rows in projects.items())
for alias,src in [('positions.txt','positions/1_positions.txt'),('transcription.txt','transcription/1.txt'),('decryption.txt','decryption/1.txt')]:assert (R/'ctts'/alias).read_bytes()==(R/'ctts'/src).read_bytes()
fragment=(R/'cryptiana/maino1446.html').read_text(encoding='utf-8');preview=(R/'cryptiana/index.html').read_text(encoding='utf-8')
assert fragment in preview and fragment.count('class="letter-text"')==2 and fragment.count('class="translation-text"')==2 and 'class="line-number"' not in fragment and fragment.count('<section ')==1 and fragment.count('<img ')==3
manifest=json.loads((R/'manifest.json').read_text(encoding='utf-8'))['files']
actual={p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file() and p.name!='manifest.json' and '__pycache__' not in p.parts}
assert actual==set(manifest),'Manifest file inventory differs'
for rel,h in manifest.items():assert hashlib.sha256((R/rel).read_bytes()).hexdigest()==h,rel
print('PASS combined edition, CTTS, aliases, insertion HTML and all checksums.')
