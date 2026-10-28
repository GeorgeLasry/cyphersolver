"""Drop the noise from raw/hits.jsonl and print what is left for reading: pre-1951 or undated, not naturalization,
newsletter, docket, scrapbook or other series that only matched by OCR on a common word."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, 'raw', 'hits.jsonl'), encoding='utf-8')]
NOISE = re.compile(r'Naturali|Declaration|Petition Numbers|Certificate Numbers|Heard & Seen|Newsletter|Docket|Scrapbook|'
                   r'Index to|Employment Assistance|Bankruptcy|Admiralty|Land Entry|Homestead|Tract|Allotment|Census', re.I)
out = []
for o in rows:
    blob = ' '.join(str(o.get(k) or '') for k in ('title', 'series', 'fileUnit'))
    if NOISE.search(blob): continue
    ys = o['years']
    if ys and min(ys) > 1950: continue
    out.append(o)
print(len(rows), 'harvested;', len(out), 'after noise/date filter', file=sys.stderr)
json.dump(out, open(os.path.join(HERE, 'raw', 'triage.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
for o in sorted(out, key=lambda o: (o['rg'] or 0, str(o.get('fileUnit')), o['naId'])):
    print(f"{o['naId']} {o['level']} RG{o['rg']} {o['years'][:2]} obj={o['nObjects']} q={','.join(o['queries'])[:80]}")
    print('   T:', (o['title'] or '')[:160], '| FU:', (o.get('fileUnit') or '')[:90])
    if o['scope']: print('   C:', o['scope'][:250].replace('\n', ' '))
