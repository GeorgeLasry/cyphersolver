"""r2p (23 Oct 2026), morosini1588: enlarge part of a transcription line (x0..x1 as fractions of the page width).

    python research/reading_audit/r2p_zoom.py R17 234r 1 0.15 0.5 [n] [shift] [name]
"""
import os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reread_b00_crop as C

OUT = r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\r2p\crops'
rec, page, line, x0, x1 = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
n = int(sys.argv[6]) if len(sys.argv) > 6 else 1
sh = float(sys.argv[7]) if len(sys.argv) > 7 else 0
name = sys.argv[8] if len(sys.argv) > 8 else f'{rec}_{page}_l{line}_z{x0:.2f}'
MAP = dict(x.split('=') for x in os.environ.get('PMAP', '').split(',') if '=' in x)
if page in MAP:
    im = Image.open(C.find_image(rec, int(MAP[page].rstrip('r')))).convert('RGB')
    if MAP[page].endswith('r'): im = im.rotate(180)
else:
    im = Image.open(C.find_image(rec, C.page_index(rec, page)[0])).convert('RGB')
first, sp = C.grid(C.rows(im))
f0 = C.first_line(rec, page)
y0 = int(max(0, first + (line + sh - f0) * sp - sp * 0.75)); y1 = int(min(im.size[1], first + (line + sh + n - 1 - f0) * sp + sp * 0.75))
W = im.size[0]
c = im.crop((int(W * x0), y0, int(W * x1), y1))
if c.size[0] < 1100:
    c = c.resize((1100, c.size[1] * 1100 // c.size[0]))
elif c.size[0] > 1400:
    c = c.resize((1400, c.size[1] * 1400 // c.size[0]))
os.makedirs(OUT, exist_ok=True)
f = os.path.join(OUT, name + '.jpg'); c.save(f, quality=88); print(f, c.size)
