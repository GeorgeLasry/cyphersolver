"""b21: build a messages-style json from Brice Dudout's current Wenmi pages (en/gongmi.html, en/rongmi.html), which carry
newer digit re-readings than his repository's messages.json (e.g. N30 group 14 read 2847 請, not 1847 隸).

    python -I research/reading_audit/b21_wenmi_page.py <page.txt> <messages.json> <family> <out.json>

page.txt is the page converted to text (tags stripped). Per telegram: the digit table ('Digits and CTC, group by group',
rows '<n> <C> <CTC> <char> <sheet>'), 'Raw decoding', 'Proposed reading' (absent for N17/N18 on the gongmi page: his
messages.json reading is used and the page's probable-reading table checked by hand) and 'Translation'.
"""
import json, re, sys
from pathlib import Path

page, msgs, fam, out = sys.argv[1:5]
lines = Path(page).read_text(encoding='utf-8').split('\n')
M = json.loads(Path(msgs).read_text(encoding='utf-8'))['messages']
res, cur = {}, None
for i, ln in enumerate(lines):
    s = ln.strip()
    if re.fullmatch(r'(N\d+\w?|V4\w)', s) and i + 1 < len(lines) and 'groups ·' in lines[i + 1]:
        cur = s; res[cur] = dict(groups=[], raw=None, reading=None, translation=None, head=lines[i + 1].strip())
        continue
    m = re.match(r'(N\d+\w?|V4\w) — ', s)
    if m and i + 1 < len(lines) and 'groups ·' in lines[i + 1]:
        cur = m.group(1); res[cur] = dict(groups=[], raw=None, reading=None, translation=None, head=lines[i + 1].strip())
        continue
    if cur is None: continue
    for key, lab in (('raw', r'Raw decoding[^㐀-鿿]*'), ('reading', r'Proposed reading\s*'), ('translation', r'Translation\s*')):
        mm = re.search(lab + r'(.*)', s)
        if mm and res[cur][key] is None and not s.startswith('Digits'):
            v = mm.group(1)
            if key == 'raw':
                v = re.split(r'\s+Translation\s', v)[0].strip()
                t = re.search(r'Translation\s+(.*)', s)
                if t and res[cur]['translation'] is None: res[cur]['translation'] = t.group(1).strip()
            res[cur][key] = v.strip()
    r = re.match(r'(\d+) ([\d?]{4}) (\S+) (\S) ', s + ' ')
    if r and int(r.group(1)) == len(res[cur]['groups']) + 1:
        res[cur]['groups'].append(r.group(2))
data = {}
for k, v in res.items():
    old = M.get(k, {})
    if old.get('family') != fam: continue
    og = [g['cipher'] for g in old['groups']]
    diff = [(n + 1, a, b) for n, (a, b) in enumerate(zip(og, v['groups'])) if a != b]
    print(k, len(v['groups']), 'repo', len(og), 'changed', diff, 'reading' if v['reading'] else 'NO READING')
    data[k] = dict(family=fam, dir=old.get('dir'), date=old.get('date'), date_note=old.get('date_note'),
                   groups=[dict(cipher=g) for g in (v['groups'] or og)],
                   reading_published=v['reading'] or old.get('reading_published'),
                   raw_page=v['raw'], translation=v['translation'], head=v['head'],
                   reading_source='page' if v['reading'] else 'messages.json')
Path(out).write_text(json.dumps(dict(messages=data), ensure_ascii=False, indent=1), encoding='utf-8')
