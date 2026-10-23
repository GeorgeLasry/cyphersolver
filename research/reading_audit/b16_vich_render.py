"""b16: turn a vich1511 build file (Lnn | text) into the body of a reading: lines joined, a line ending in '-' runs
on into the next without a space; a line '## ...' or '¶' in the build starts a new paragraph.
python b16_vich_render.py <build.txt> <header.md> <out_reading.md>"""
import sys, re
build, header, out = sys.argv[1:4]
paras, cur = [], ''
for line in open(build, encoding='utf-8'):
    line = line.rstrip('\n')
    if line.startswith('¶') or line.startswith('##'):
        if cur.strip(): paras.append(cur.strip())
        cur = ''; continue
    if not line.startswith('L'): continue
    text = line.split('|', 1)[1].strip()
    if cur.endswith('-'): cur = cur[:-1] + text
    else: cur = (cur + ' ' + text) if cur else text
if cur.strip(): paras.append(cur.strip())
body = '\n\n'.join(re.sub(r' +', ' ', p) for p in paras)
open(out, 'w', encoding='utf-8').write(open(header, encoding='utf-8').read().rstrip() + '\n\n' + body + '\n')
print(out, sum(len(p.split()) for p in paras), 'words')
