"""r2p (23 Oct 2026), morosini1588: stack line crops of DECODE cipher pages into one labelled sheet (scratchpad).

    python research/reading_audit/r2p_sheet.py R17 out_name 234r:1 234r:11:2 235r:4:2:-1
                                   page:line[:n[:shift]]  (shift moves the band if the row grid is off by a line); env PMAP overrides page->image
Each crop is the line band cut in two halves stacked (as r2d_mcrop.py), labelled with page and line.
"""
import os, sys
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reread_b00_crop as C

OUT = r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\r2p\crops'
rec, name = sys.argv[1], sys.argv[2]
tiles = []
for spec in sys.argv[3:]:
    p = spec.split(':')
    page, line = p[0], int(p[1]); n = int(p[2]) if len(p) > 2 else 1; sh = int(p[3]) if len(p) > 3 else 0
    MAP = dict(x.split('=') for x in os.environ.get('PMAP', '').split(',') if '=' in x)   # PMAP="162v=5,162r=4r": image P<k>, r = turned 180
    if page in MAP:
        k = int(MAP[page].rstrip('r'))
        im = Image.open(C.find_image(rec, k)).convert('RGB')
        if MAP[page].endswith('r'): im = im.rotate(180)
    else:
        k = C.page_index(rec, page)[0]
        im = Image.open(C.find_image(rec, k)).convert('RGB')
    first, sp = C.grid(C.rows(im))
    f0 = C.first_line(rec, page)
    y0 = int(max(0, first + (line + sh - f0) * sp - sp * 0.7)); y1 = int(min(im.size[1], first + (line + sh + n - 1 - f0) * sp + sp * 0.7))
    W = im.size[0]
    L = im.crop((0, y0, W // 2 + 80, y1)); R = im.crop((W // 2 - 80, y0, W, y1))
    o = Image.new('RGB', (L.size[0], L.size[1] * 2 + 34), 'white'); o.paste(L, (0, 26)); o.paste(R, (0, L.size[1] + 34))
    ImageDraw.Draw(o).text((8, 4), f'{rec} {page} l.{line}' + (f'-{line + n - 1}' if n > 1 else ''), fill=(200, 0, 0))
    if o.size[0] > 1100:
        o = o.resize((1100, o.size[1] * 1100 // o.size[0]))
    tiles.append(o)
H = sum(t.size[1] for t in tiles) + 6 * len(tiles)
S = Image.new('RGB', (max(t.size[0] for t in tiles), H), (90, 90, 90))
y = 0
for t in tiles:
    S.paste(t, (0, y)); y += t.size[1] + 6
os.makedirs(OUT, exist_ok=True)
f = os.path.join(OUT, f'{rec}_{name}.jpg'); S.save(f, quality=85); print(f, S.size)
