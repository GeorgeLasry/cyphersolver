"""show.py <naId> <file-substring> [n_after] [grep-regex] -- print cached OCR of a frame and the next frames."""
import json, os, sys, re
C = os.path.join(os.path.dirname(__file__), '..', 'nara_reels', 'cache')
naid, key = sys.argv[1], sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 0
rec = json.load(open(os.path.join(C, f'{naid}.rec.json'), encoding='utf-8'))
txt = {o['objectId']: o.get('extractedText') or '' for o in json.load(open(os.path.join(C, f'{naid}.txt.json'), encoding='utf-8'))}
objs = rec['digitalObjects']
if key == 'grep':
    rx = re.compile(sys.argv[4] if len(sys.argv) > 4 else sys.argv[3], re.I)
    for o in objs:
        t = re.sub(r'\s+', ' ', txt.get(o['objectId'], ''))
        for m in rx.finditer(t):
            print(o['objectFilename'], '|', t[max(0, m.start() - 150):m.end() + 150])
    sys.exit()
i = [k for k, o in enumerate(objs) if key in o['objectFilename']][0]
for o in objs[i:i + n + 1]:
    print('=====', o['objectFilename'], o['objectUrl'])
    print(re.sub(r'[ \t]+', ' ', txt.get(o['objectId'], '')))
