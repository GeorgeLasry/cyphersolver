"""Print cached OCR of frames around a hit:  python show.py <naId> <frame-substring> [before] [after] [maxchars]"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'nara_reels', 'cache')
naid, sub = sys.argv[1], sys.argv[2]
b = int(sys.argv[3]) if len(sys.argv) > 3 else 1; a = int(sys.argv[4]) if len(sys.argv) > 4 else 1
mx = int(sys.argv[5]) if len(sys.argv) > 5 else 1500
rec = json.load(open(f'{C}/{naid}.rec.json', encoding='utf-8')); objs = json.load(open(f'{C}/{naid}.txt.json', encoding='utf-8'))
names = {o['objectId']: o['objectFilename'] for o in rec.get('digitalObjects') or []}
txt = {names.get(o['objectId'], o['objectId']): o.get('extractedText') or '' for o in objs}
order = sorted(txt)
idx = [i for i, n in enumerate(order) if sub in n]
for i in idx[:1]:
    for j in range(max(0, i - b), min(len(order), i + a + 1)):
        print(f'=== {order[j]}'); print(' '.join(txt[order[j]].split())[:mx])
