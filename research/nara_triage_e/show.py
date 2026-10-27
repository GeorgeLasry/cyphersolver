"""Print cached OCR of an item's frames.

    python research/nara_triage_e/show.py <naId> grep <regex> [ctx]   # frames whose OCR matches, with context
    python research/nara_triage_e/show.py <naId> frame <objectId|index> [n]   # full OCR of a frame (and n following)
Needs research/nara_reels/reels.py fetch <naId> first.
"""
import json, os, re, sys

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'nara_reels', 'cache')


def load(naid):
    objs = json.load(open(os.path.join(CACHE, f'{naid}.txt.json'), encoding='utf-8'))
    rec = json.load(open(os.path.join(CACHE, f'{naid}.rec.json'), encoding='utf-8'))
    names = {}
    for d in rec.get('digitalObjects') or []:
        names[str(d.get('objectId'))] = d.get('objectFilename') or d.get('objectUrl', '').split('/')[-1]
    return objs, names, rec


def main():
    naid, cmd = sys.argv[1], sys.argv[2]
    objs, names, rec = load(naid)
    if cmd == 'grep':
        rx = re.compile(sys.argv[3], re.I)
        ctx = int(sys.argv[4]) if len(sys.argv) > 4 else 300
        for i, o in enumerate(objs):
            t = o.get('extractedText') or ''
            for m in rx.finditer(t):
                a, b = max(0, m.start() - ctx), m.end() + ctx
                print(f"== [{i}] {o['objectId']} {names.get(str(o['objectId']), '')}")
                print(re.sub(r'\s+', ' ', t[a:b]))
                break
    elif cmd == 'frame':
        key, n = sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 0
        idx = next((i for i, o in enumerate(objs) if str(o['objectId']) == key), None)
        if idx is None:
            idx = int(key)
        for o in objs[idx:idx + n + 1]:
            print(f"== {o['objectId']} {names.get(str(o['objectId']), '')}")
            print(o.get('extractedText'))
    elif cmd == 'title':
        print(rec.get('title'), len(objs))


if __name__ == '__main__':
    main()
