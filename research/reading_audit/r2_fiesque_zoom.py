"""r2_fiesque helper: upscale a line strip (two halves a/b) for viewing. usage: python r2_fiesque_zoom.py <dir> <prefix> <line> [scale]"""
import sys
from PIL import Image
d, pre, i = sys.argv[1], sys.argv[2], int(sys.argv[3]); sc = float(sys.argv[4]) if len(sys.argv) > 4 else 1.3
for h in 'ab':
    im = Image.open(f'{d}/{pre}_{i:02d}{h}.jpg')
    im = im.resize((int(im.width*sc), int(im.height*sc)), Image.LANCZOS)
    im.save(f'{d}/z_{pre}_{i:02d}{h}.jpg')
