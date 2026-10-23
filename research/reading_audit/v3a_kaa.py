"""v3 verify (a), kaa4591 / kaa4591b: running text of a line-per-row reading (keys Pn.NN) with the writer's clear text,
which those files put in [brackets], written «..» so that it is not counted as supplied words. Supplied letters inside a
word (x[y]z), code signs ([F.G.], [K], [X]) stay as they are; {?} (a word not read) is written [?], since the scorer takes {..} for a resolved code. Comment lines (#) dropped. Optionally writes a
reading file with a header.

    python research/reading_audit/v3a_kaa.py <reading file> [<out.md> "<header text>"]
"""
import re, sys, pathlib
src = pathlib.Path(sys.argv[1])
out = []
for l in src.read_text(encoding='utf8').splitlines():
    m = re.match(r'^P\d+[a-z]?\.\d+\w*\s+(.*)$', l)
    if not m: continue
    t = m.group(1)
    t = re.sub(r'(?<![\w\]])\[([^\]]*(?:\s|[a-z]{3,})[^\]]*)\](?![\w\[])', lambda mm: '«' + mm.group(1) + '»' if not re.fullmatch(r'[A-Z.]+', mm.group(1)) else mm.group(0), t)
    t = t.replace('{?}', '[?]')     # {?} = word not read; the scorer would take {..} for a resolved code
    out.append(t.strip())
body = ' '.join(out)
if len(sys.argv) > 3:
    pathlib.Path(sys.argv[2]).write_text(sys.argv[3].rstrip() + '\n\n## Reading\n\n' + body + '\n', encoding='utf8')
else:
    print('## Reading\n\n' + body)
