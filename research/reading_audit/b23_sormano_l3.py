"""b23 re-read, sormano: one line in three overlapping thirds at higher scale.

    python b23_sormano_l3.py <view> <x0> <x1> <tag> <y1,y2,...> [scale=1.25] [h=150] [dy_right=0]
dy_right: extra y offset for the right third (lines slope on these leaves).
"""
import sys
from PIL import Image, ImageOps
RAW = 'C:/Users/dbour/cypher/targets/sormano/raw/full%d.jpg'
OUT = ('C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/'
       '6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/sormano/')
view, x0, x1 = map(int, sys.argv[1:4]); tag = sys.argv[4]
ys = [int(v) for v in sys.argv[5].split(',')]
scale = float(sys.argv[6]) if len(sys.argv) > 6 else 1.25
h = int(sys.argv[7]) if len(sys.argv) > 7 else 150
dyr = int(sys.argv[8]) if len(sys.argv) > 8 else 0
im = Image.open(RAW % view).convert('L')
w = (x1 - x0) // 3
for y in ys:
    for k, s in enumerate('abc'):
        a = x0 + k * w - (60 if k else 0); b = x0 + (k + 1) * w + 60
        dy = dyr * k // 2
        c = ImageOps.autocontrast(im.crop((a, y - h // 2 + dy, b, y + h // 2 + dy)), cutoff=0.5)
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
        c.save(OUT + '%s_%d%s.jpg' % (tag, y, s), quality=90)
print('ok')
