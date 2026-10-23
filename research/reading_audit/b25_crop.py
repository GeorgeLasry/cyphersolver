"""b25: crop + upscale a region of an image into the scratchpad.
    python b25_crop.py <img> <out> x0 y0 x1 y1 [scale]"""
import sys
from PIL import Image, ImageOps
im = Image.open(sys.argv[1]).convert('L')
x0, y0, x1, y1 = map(int, sys.argv[3:7]); sc = float(sys.argv[7]) if len(sys.argv) > 7 else 2
c = im.crop((x0, y0, x1, y1)); c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
ImageOps.autocontrast(c, cutoff=1).save(sys.argv[2])
