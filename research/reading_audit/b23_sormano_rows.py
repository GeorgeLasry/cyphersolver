"""b23 sormano: estimate text-line centres on a page region from the ink profile (peaks)."""
import sys, numpy as np
from PIL import Image
RAW = 'C:/Users/dbour/cypher/targets/sormano/raw/full%d.jpg'
view, x0, x1, y0, y1 = map(int, sys.argv[1:6])
a = np.asarray(Image.open(RAW % view).convert('L').crop((x0, y0, x1, y1)), float)
ink = (a < 100).sum(1).astype(float)
s = np.convolve(ink, np.ones(31) / 31, 'same')
pk = []
for i in range(40, len(s) - 40):
    if s[i] == s[i - 40:i + 41].max() and s[i] > 0.25 * np.percentile(s, 95):
        if not pk or i - pk[-1] > 60:
            pk.append(i)
print(','.join(str(y0 + p) for p in pk))
