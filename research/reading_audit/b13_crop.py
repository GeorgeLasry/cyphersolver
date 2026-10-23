"""b13: crop a box of a page image (fractions of width/height) to the scratchpad, optionally scaled.
usage: b13_crop.py <image> <out.jpg> x0 x1 y0 y1 [scale]
       b13_crop.py --size <image> [...]   print sizes
Crops go only to the session scratchpad (reread/b13/)."""
import sys, os
from PIL import Image

if sys.argv[1] == '--size':
    for f in sys.argv[2:]:
        print(os.path.basename(f), Image.open(f).size)
    sys.exit()
im = Image.open(sys.argv[1]).convert('RGB')
W, H = im.size
x0, x1, y0, y1 = (float(a) for a in sys.argv[3:7])
sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
if sc != 1.0:
    c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
os.makedirs(os.path.dirname(sys.argv[2]), exist_ok=True)
c.save(sys.argv[2], quality=90)
print(sys.argv[2], c.size)
