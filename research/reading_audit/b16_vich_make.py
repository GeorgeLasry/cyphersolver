"""b16: regenerate a vich1511 reading from its build: header (everything in the existing <doc>_reading.md above the
line '<!-- body -->') + the build rendered as is, in the figures' own spelling (no modernisation).
Also writes the body alone to the scratchpad and prints its _check_reading score.
python b16_vich_make.py n45|n57|n60"""
import sys, pathlib, subprocess, json, re
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from b16_vich_modern import modern
T = HERE.parents[1] / 'targets' / 'vich1511'
S = pathlib.Path('C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread')
MARK = '<!-- body -->'
doc = sys.argv[1]
reading = T / f'{doc}_reading.md'
head = reading.read_text(encoding='utf-8').split(MARK)[0].rstrip() + '\n\n' + MARK + '\n'
paras, cur = [], ''
for line in (T / f'{doc}_build.txt').read_text(encoding='utf-8').splitlines():
    if line.startswith('¶') or line.startswith('##'):
        if cur.strip(): paras.append(cur.strip())
        cur = ''; continue
    if not line.startswith('L'): continue
    text = line.split('|', 1)[1].strip()
    cur = cur[:-1] + text if cur.endswith('-') else (cur + ' ' + text if cur else text)
if cur.strip(): paras.append(cur.strip())
# 23 Oct 2026 (coordinator): the reading keeps the figures' spelling; no modernisation, B[eatitud] stays bracketed
body = '\n\n'.join(re.sub(r' +', ' ', p) for p in paras) + '\n'
reading.write_text(head + '\n' + body, encoding='utf-8')
(S / f'{doc}_body.md').write_text(body, encoding='utf-8')
out = subprocess.run([sys.executable, str(HERE.parents[1] / 'docs' / '_check_reading.py'), '--file', str(S / f'{doc}_body.md')],
                     capture_output=True, text=True).stdout
r = json.loads(out)
print(doc, 'words', len(body.split()), 'sentences', r['sentences'], 'clean', r['clean'], 'share', r['clean_share'], 'holes', r['hole_rate'])
