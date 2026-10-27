"""grp5.py <naId> ...: frames of a cached item with runs of >= 6 five-letter capital groups (enciphered text)."""
import json, os, sys, re
C = os.path.join(os.path.dirname(__file__), '..', 'nara_reels', 'cache')
RX = re.compile(r'(?:\b[A-Z]{5}\b[\s,.]*){6,}')
for naid in sys.argv[1:]:
    rec = json.load(open(os.path.join(C, f'{naid}.rec.json'), encoding='utf-8'))
    txt = {o['objectId']: o.get('extractedText') or '' for o in json.load(open(os.path.join(C, f'{naid}.txt.json'), encoding='utf-8'))}
    for o in rec['digitalObjects']:
        t = txt.get(o['objectId'], '')
        runs = RX.findall(t)
        n = sum(len(r.split()) for r in runs)
        if n >= 6:
            print(naid, o['objectFilename'], n, '|', re.sub(r'\s+', ' ', runs[0])[:120])
