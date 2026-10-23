"""b16: stack the vich1511 N.45 line strips (lines/s45pPP_NN.png, three lines each) holding the given tags.
python b16_n45_strip.py <out.png> L0419 L0708 ..."""
import sys
from PIL import Image
D = 'C:/Users/dbour/cypher/targets/vich1511/lines/'
out, tags = sys.argv[1], sys.argv[2:]
seen, ims = [], []
for t in tags:
    p, l = int(t[1:3]), int(t[3:5]); f = f'{D}s45p{p:02d}_{(l - 1) // 3:02d}.png'
    if f not in seen: seen.append(f); ims.append(Image.open(f))
W = max(i.size[0] for i in ims); H = sum(i.size[1] for i in ims)
c = Image.new('RGB', (W, H), 'white'); y = 0
for i in ims: c.paste(i, (0, y)); y += i.size[1]
c.save(out); print(seen)
