"""List the Ambrosiana's fully digitised manuscripts (biblioteca-digitale/?start=N, 20 per page).
    PYTHONUTF8=1 python -I research/milan_archives/ambrosiana_digital_list.py
Writes ambrosiana_digital.json: [{id, title}] (title carries the shelfmark).
"""
import html, json, os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
out, seen = [], set()
for start in range(0, 1500, 20):
    s = subprocess.run(['curl', '-s', '-L', '-m', '60', f'https://ambrosiana.comperio.it/biblioteca-digitale/?start={start}'],
                       capture_output=True).stdout.decode('utf-8', 'replace')
    new = 0
    for b in s.split('<div id="man_')[1:]:
        mid = re.match(r'(\d+)', b).group(1)
        t = re.search(r'class="cover" property="url" href="[^"]*" title="([^"]*)"', b)
        if mid in seen:
            continue
        seen.add(mid); new += 1
        out.append({'id': 'ambro:catalog:' + mid, 'title': html.unescape(t.group(1)).strip() if t else ''})
    if not new:
        break
json.dump(out, open(os.path.join(HERE, 'ambrosiana_digital.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out))
