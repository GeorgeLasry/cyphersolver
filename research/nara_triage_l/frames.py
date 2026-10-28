"""frames.py <naId> <first> <last> [maxchars]: OCR of frames of a cached reel by the trailing frame number."""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'nara_reels', 'cache')
n, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); mx = int(sys.argv[4]) if len(sys.argv) > 4 else 900
T = {o['objectId']: o for o in json.load(open(os.path.join(C, f'{n}.txt.json'), encoding='utf-8'))}
R = json.load(open(os.path.join(C, f'{n}.rec.json'), encoding='utf-8'))
for d in R['digitalObjects']:
    m = re.search(r'(\d+)\.\w+$', d.get('objectFilename', ''))
    if m and a <= int(m.group(1)) <= b:
        print('=====', d['objectFilename'], re.sub(r'\s+', ' ', (T.get(str(d['objectId'])) or {}).get('extractedText') or '')[:mx])
