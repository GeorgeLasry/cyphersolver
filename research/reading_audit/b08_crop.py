"""b08: crop a region of a malsburg1637 HCPortal scan (saved only in the session scratchpad).

    python b08_crop.py <page e.g. 0003|14> <x0> <y0> <x1> <y1> <out-name> [scale]

Coordinates are original pixels; fractions (0-1) are taken as a share of the width/height.
"""
import sys, pathlib
from PIL import Image, ImageOps

S = pathlib.Path(r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/'
                 r'6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/b08')
page = sys.argv[1]
im = Image.open(S / 'img' / f'hstam_4_h_1411_{page}_Cryp.jpg')
c = [float(v) for v in sys.argv[2:6]]
c = [int(v * (im.width if i % 2 == 0 else im.height)) if v <= 1 else int(v) for i, v in enumerate(c)]
sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
out = im.crop(tuple(c))
if sc != 1.0:
    out = out.resize((int(out.width * sc), int(out.height * sc)), Image.LANCZOS)
out = ImageOps.autocontrast(out.convert('L'), cutoff=1)
(S / 'c').mkdir(exist_ok=True)
p = S / 'c' / (sys.argv[6] + '.png')
out.save(p)
print(p, out.size)
