"""b16 (wotton1585): cut horizontal strips from a full-resolution DECODE page image (main checkout decode/) into the
session scratchpad. Usage: b16_wotton_crop.py REC PAGE X0 X1 Y0 Y1 NSTRIPS [WIDTH]  (fractions of the page)."""
import sys
from PIL import Image, ImageOps
rec, page = sys.argv[1], sys.argv[2]
x0, x1, y0, y1 = map(float, sys.argv[3:7]); n = int(sys.argv[7]); W = int(sys.argv[8]) if len(sys.argv) > 8 else 1800
S = 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/wotton/'
im = Image.open(f'C:/Users/dbour/cypher/targets/wotton1585/decode/R{rec}_p{page}.jpg').convert('L')
w, h = im.size
step = (y1 - y0) / n
for i in range(n):
    a = y0 + i * step; b = min(y1, a + step * 1.15)
    c = im.crop((int(x0 * w), int(a * h), int(x1 * w), int(b * h)))
    c = ImageOps.autocontrast(c, cutoff=1)
    c = c.resize((W, int(c.size[1] * W / c.size[0])), Image.LANCZOS)
    fn = S + f's{rec}_{page}_{i:02d}.jpg'; c.save(fn, quality=88); print(fn, c.size)
