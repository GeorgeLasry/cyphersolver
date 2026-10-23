"""b02 helper: show each line of a fiesque1567 transcription as sign=value pairs.
usage: python reread_b02_signs.py <page> [line ...]"""
import sys, re, pathlib
D = pathlib.Path(__file__).resolve().parents[2] / 'targets/fiesque1567/contributed/data'
key = {}
for ln in open(D/'key.tsv', encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    p = ln.rstrip('\n').split('\t'); key[p[0]] = p[1]
page = sys.argv[1]; want = set(sys.argv[2:])
for ln in open(D/f'transcription_{page}.txt', encoding='utf-8'):
    m = re.match(r'(c\w+):\s*(.*)', ln)
    if not m or (want and m.group(1) not in want): continue
    out = []
    for t in m.group(2).split():
        tt = t[:-1] if t.endswith('?') and len(t) > 1 else t
        v = key.get(tt, '?')
        if v == '(null)': v = '_'
        out.append(f'{t}={v}')
    print(m.group(1), ' '.join(out))
