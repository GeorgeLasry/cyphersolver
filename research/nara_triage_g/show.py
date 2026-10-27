"""Print cached NARA OCR for an item (fetch first with research/nara_reels/reels.py fetch <naId>).

    python research/nara_triage_g/show.py <naId> frame <n> [<m>]   # frames n..m (by file sequence number)
    python research/nara_triage_g/show.py <naId> grep <regex>       # frames whose OCR matches
    python research/nara_triage_g/show.py <naId> info               # title, ancestors, frame count, image url pattern
"""
import json, os, re, sys

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'nara_reels', 'cache')


def load(naid):
    rec = json.load(open(os.path.join(CACHE, f'{naid}.rec.json'), encoding='utf-8'))
    objs = json.load(open(os.path.join(CACHE, f'{naid}.txt.json'), encoding='utf-8'))
    text = {str(o['objectId']): o.get('extractedText') or '' for o in objs}
    frames = []
    for d in rec.get('digitalObjects') or []:
        name = d.get('objectFilename') or d.get('objectUrl', '').rsplit('/', 1)[-1]
        m = re.search(r'(\d+)\.\w+$', name)
        frames.append((int(m.group(1)) if m else -1, name, d.get('objectUrl'), text.get(str(d.get('objectId')), '')))
    return rec, frames


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    naid, cmd = sys.argv[1], sys.argv[2]
    rec, frames = load(naid)
    if cmd == 'info':
        print(rec.get('title'), '|', ' > '.join(a.get('title', '') for a in rec.get('ancestors', [])))
        print(len(frames), 'frames;', frames[0][1] if frames else '', frames[0][2] if frames else '')
        print((rec.get('scopeAndContentNote') or '')[:1500])
    elif cmd == 'frame':
        a = int(sys.argv[3]); b = int(sys.argv[4]) if len(sys.argv) > 4 else a
        for n, name, url, t in frames:
            if a <= n <= b:
                print(f'=== {name} {url}\n{t}\n')
    elif cmd == 'grep':
        rx = re.compile(sys.argv[3], re.I)
        for n, name, url, t in frames:
            for m in rx.finditer(t):
                print(name, '|', t[max(0, m.start() - 150):m.end() + 150].replace('\n', ' '))
                break


if __name__ == '__main__':
    main()
