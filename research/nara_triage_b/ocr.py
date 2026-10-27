"""Print OCR of frames of a cached item. python research/nara_triage_b/ocr.py <naId> <first> <last> [maxchars]
Frames are numbered by the trailing number in their filename."""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'nara_reels', 'cache')
naid, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 1500
rec = json.load(open(os.path.join(C, naid + '.rec.json'), encoding='utf-8'))
names = {o['objectId']: o['objectFilename'] for o in rec.get('digitalObjects') or []}
urls = {o['objectId']: o.get('objectUrl') for o in rec.get('digitalObjects') or []}
for o in json.load(open(os.path.join(C, naid + '.txt.json'), encoding='utf-8')):
    fn = names.get(o['objectId'], '')
    m = re.search(r'(\d+)\.\w+$', fn)
    if m and a <= int(m.group(1)) <= b:
        print('=====', fn, o['objectId'], urls.get(o['objectId']))
        print(' '.join((o.get('extractedText') or '').split())[:mx])
