"""Rebuild the full-size assembled key (4438 x 2998) from the six fragments and original-key-assembly.json.

The committed assets/original-key-assembled.png is a half-size copy (added 21 Oct 2026 to keep the repository small;
the full-size PNG in PR #61 was 8.9 MB). This script paints the fragments at their recorded integer offsets, in the
recorded order, on a white canvas, and writes assets/original-key-assembled-full.png (git-ignored size, not committed).

  python assemble_key.py
"""
import json, pathlib
from PIL import Image

R = pathlib.Path(__file__).resolve().parent
spec = json.loads((R / 'original-key-assembly.json').read_text(encoding='utf-8'))
canvas = Image.new('L', (spec['width'], spec['height']), 255)
for p in spec['placements_in_paint_order']:
    frag = Image.open(R / 'assets' / 'key-fragments' / p['fragment']).convert('L')
    canvas.paste(frag, (p['x'], p['y']))
canvas.save(R / 'assets' / 'original-key-assembled-full.png', optimize=True)
print('wrote assets/original-key-assembled-full.png', canvas.size)
