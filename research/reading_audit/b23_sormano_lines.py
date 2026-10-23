"""b23 re-read, sormano: cut line strips (two halves, overlapping) centred on given y values of a raw view.

    python b23_sormano_lines.py <view> <x0> <x1> <tag> <y1,y2,...> [scale=0.85] [h=150]
"""
import sys
from PIL import Image, ImageOps
RAW = 'C:/Users/dbour/cypher/targets/sormano/raw/full%d.jpg'
OUT = ('C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/'
       '6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/sormano/')
view, x0, x1 = map(int, sys.argv[1:4]); tag = sys.argv[4]
ys = [int(v) for v in sys.argv[5].split(',')]
scale = float(sys.argv[6]) if len(sys.argv) > 6 else 0.85
h = int(sys.argv[7]) if len(sys.argv) > 7 else 150
im = Image.open(RAW % view).convert('L')
mid = (x0 + x1) // 2
for y in ys:
    for s, (a, b) in zip('ab', ((x0, mid + 80), (mid - 80, x1))):
        c = ImageOps.autocontrast(im.crop((a, y - h // 2, b, y + h // 2)), cutoff=0.5)
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
        c.save(OUT + '%s_%d%s.jpg' % (tag, y, s), quality=92)
print('ok')
