"""b23 re-read, sormano: cut one region of a raw/full<view>.jpg (IIIF full-resolution master) for reading by eye.

    python b23_sormano_slab.py <view> <x0> <x1> <y0> <y1> <out-name> [scale=0.6]
"""
import sys
from PIL import Image, ImageOps

RAW = 'C:/Users/dbour/cypher/targets/sormano/raw/full%d.jpg'
OUT = ('C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/'
       '6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/sormano/')

view, x0, x1, y0, y1 = map(int, sys.argv[1:6])
name = sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 0.6
c = Image.open(RAW % view).convert('L').crop((x0, y0, x1, y1))
c = ImageOps.autocontrast(c, cutoff=0.5)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(OUT + name + '.jpg', quality=92)
print(OUT + name + '.jpg', c.size)
