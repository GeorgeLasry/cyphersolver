"""b33 riksarkivet1628 (Bremen 1631): crop a band of a DECODE phone photograph for reading.

    python b33_br_crop.py <img> <out> <y0> <y1> [x0 x1] [width]
y/x as fractions (0-1) of the image; the crop is resized to <width> px (default 1600) and saved to <out>.
"""
import sys
from PIL import Image, ImageOps
im = Image.open(sys.argv[1]); im = ImageOps.exif_transpose(im)
W, H = im.size
y0, y1 = float(sys.argv[3]), float(sys.argv[4])
x0, x1 = (float(sys.argv[5]), float(sys.argv[6])) if len(sys.argv) > 6 else (0, 1)
w = int(sys.argv[7]) if len(sys.argv) > 7 else 1600
c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
c = c.resize((w, int(c.size[1] * w / c.size[0])), Image.LANCZOS)
c.save(sys.argv[2], quality=90)
print(sys.argv[2], im.size, c.size)
