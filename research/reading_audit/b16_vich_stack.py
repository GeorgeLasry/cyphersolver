"""b16: stack vich1511 half-line strips (half/h57_NNa/b.png) or page strips for viewing. Images go to the scratchpad.
python b16_vich_stack.py <out.png> <strip names...>"""
import sys
from PIL import Image
D = 'C:/Users/dbour/cypher/targets/vich1511/'
out, names = sys.argv[1], sys.argv[2:]
ims = [Image.open(D + n if '/' in n else D + 'half/' + n + '.png') for n in names]
W = max(i.size[0] for i in ims); H = sum(i.size[1] for i in ims)
c = Image.new('RGB', (W, H), 'white'); y = 0
for i in ims: c.paste(i, (0, y)); y += i.size[1]
c.save(out)
