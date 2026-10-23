"""b35: rotate a DECODE page image and cut it into overlapping horizontal strips (scratchpad only).

    python b35_strips.py <image> <rotate_degrees> <strip_height> <outprefix> [x0 x1] [y0 y1]
"""
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB')
rot = int(sys.argv[2])
if rot: im = im.rotate(rot, expand=True)
h = int(sys.argv[3]); pre = sys.argv[4]
x0, x1 = (int(sys.argv[5]), int(sys.argv[6])) if len(sys.argv) > 6 else (0, im.size[0])
y0, y1 = (int(sys.argv[7]), int(sys.argv[8])) if len(sys.argv) > 8 else (0, im.size[1])
print(im.size)
i = 0
for y in range(y0, y1, int(h * 0.8)):
    im.crop((x0, y, x1, min(y + h, y1))).save('%s_%02d.jpg' % (pre, i), quality=88); i += 1
print(i, 'strips')
