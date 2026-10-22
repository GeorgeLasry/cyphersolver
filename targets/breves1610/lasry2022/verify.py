from pathlib import Path
import csv, hashlib, json, re
from html.parser import HTMLParser
R=Path(__file__).parent
for f in json.loads((R/'source_manifest.json').read_text(encoding='utf-8'))['files']:
    assert hashlib.sha256((R/f['package']).read_bytes()).hexdigest()==f['sha256'],f['package']
key=json.loads((R/'key.json').read_text(encoding='utf-8'))['mapping']
rows=list(csv.DictReader((R/'alignment.tsv').open(encoding='utf-8'),delimiter='\t'))
for stem in ['b1','b2','3']:
    previous=None; expected=[]
    lines=[l for l in (R/f'ctts/transcription/{stem}.txt').read_text(encoding='utf-8-sig').splitlines() if l and not l.startswith('#')]
    for i,l in enumerate(lines,1):
        for j,s in enumerate(filter(None,l.split(';')),1):
            if s=='PLAINTEXT': val='[cleartext]';previous=None
            elif s=='s-': assert previous is not None;val=previous
            else: val=key.get(s,f'[{s}]').lower();previous=val
            expected.append((str(i),str(j),s,val))
    actual=[(x['ctts_line'],x['token_in_line'],x['label'],x['literal_value']) for x in rows if x['image']==stem]
    assert actual==expected,stem
class Check(HTMLParser):
    def __init__(self): super().__init__(); self.links=[];self.ids=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        for n in ['src','href']:
            if n in a:self.links.append(a[n])
c=Check();c.feed((R/'index.html').read_text(encoding='utf-8'))
assert len(c.ids)==len(set(c.ids))
for link in c.links:
    if link.startswith('http'):continue
    if link.startswith('#'):assert link[1:] in c.ids,link
    else:assert (R/link).is_file(),link
data=json.loads((R/'reading.json').read_text(encoding='utf-8'))
assert [len(x['fr']) for x in data]==[17,10,7]
assert all(len(x['fr'])==len(x['en']) for x in data)
assert '3t' not in key and key['v']=='G'
assert 'croyance' not in ''.join(x for p in data for x in p['fr'])
assert '3;d-;j;v;x;f;a,' in (R/'ctts/transcription/3.txt').read_text(encoding='utf-8')
print('PASS: source hashes, deterministic token alignment, 34 bilingual manuscript lines, current AROGANCE key, HTML links and anchors.')
