"""b28: estimate skew (row-profile variance of the text box, angles -2.5..2.5) and save a deskewed grey copy.
    python b28_deskew.py <img> <out> x0 y0 x1 y1"""
import sys, numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
im = Image.open(sys.argv[1]).convert('L')
c = im.crop(tuple(map(int, sys.argv[3:7]))); sm = c.resize((c.width // 4, c.height // 4))
best = max((np.asarray(sm.rotate(a, fillcolor=255), float).__rsub__(255).sum(1).var(), a) for a in np.arange(-2.5, 2.51, 0.05))
print('angle', round(best[1], 2))
im.rotate(best[1], resample=Image.BICUBIC, fillcolor=255).save(sys.argv[2], quality=92)
