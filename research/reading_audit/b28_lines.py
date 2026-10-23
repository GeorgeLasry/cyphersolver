"""b28: find text-line centres on a deskewed page (row ink profile, smoothed), print them.
    python b28_lines.py <img> x0 x1 y0 y1"""
import sys, numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
im = Image.open(sys.argv[1]).convert('L'); x0, x1, y0, y1 = map(int, sys.argv[2:6])
a = 255 - np.asarray(im.crop((x0, y0, x1, y1)), float)
p = (a > 90).sum(1).astype(float)
k = np.ones(31) / 31; s = np.convolve(p, k, 'same')
peaks = [i for i in range(40, len(s) - 40) if s[i] == s[i-40:i+41].max() and s[i] > 0.15 * s.max()]
print(len(peaks), [y0 + i for i in peaks])
