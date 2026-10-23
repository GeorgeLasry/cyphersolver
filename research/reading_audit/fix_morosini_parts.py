"""morosini1588: parts label, method_basis and gaps after verification sweep 3 (31 read; R27, R35, R51, R57 not)."""
import json, pathlib

p = pathlib.Path(__file__).resolve().parent.parent.parent / 'targets' / 'morosini1588' / 'profile.json'
raw = p.read_bytes().decode('utf-8')
d = json.loads(raw)
o = d['outcome']
for k in ('label', 'basis'):
    if k in o['parts'][0]:
        o['parts'][0][k] = o['parts'][0][k].replace('34 read as sentences', '31 read as sentences').replace('R35 not yet', 'R27, R35, R51, R57 not yet')
o['method_basis'] = o['method_basis'].replace('34 read as sentences', '31 read as sentences').replace('R35 not yet', 'R27, R35, R51, R57 not yet')
items = {g['item'] for g in o.get('gaps') or []}
new = {'item': 'R27, R51, R57 decoded, not read (0.55, 0.57, 0.56 clean sentences after the word-by-word check)',
       'blocker': 'not-attempted',
       'detail': 'transcription not yet checked on the images at the breaks; Rome\'s decipherments (ASV Francia 27) not imaged'}
if new['item'] not in items:
    o.setdefault('gaps', []).append(new)
out = json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if raw.endswith('\n') else '')
if '\r\n' in raw: out = out.replace('\n', '\r\n')
p.write_bytes(out.encode('utf-8'))
print(o['parts'][0].get('label', '')[:120])
