"""v5a (23 Oct 2026): running text of one letter from affry1757/wainut/register_clear.txt (Fagel register clear copies).
    python research/reading_audit/v5a_affry_reg.py <inv> <page> [<page> ...]      e.g. 5186 16R 17L
MARGIN and '%' lines dropped; a line ending in '-' or '=' is joined to the next without a space. Prints the text."""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
src = (ROOT / 'targets/affry1757/wainut/register_clear.txt').read_text(encoding='utf-8').splitlines()
inv, pages = sys.argv[1], sys.argv[2:]
blocks, cur = {}, None
for l in src:
    m = re.match(r'@ (\d+) (\d+[LR])', l)
    if m: cur = (m.group(1), m.group(2)); blocks[cur] = []; continue
    if cur and not l.startswith(('MARGIN:', '%', '#')) and l.strip(): blocks[cur].append(l.strip())
t = ''
for p in pages:
    for l in blocks[(inv, p)]:
        if t.endswith(('-', '=')): t = t[:-1] + l
        else: t = (t + ' ' + l) if t else l
print(t)
