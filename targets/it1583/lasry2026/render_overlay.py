"""Rebuild the red overlay from edition.json and the original 1.jpg.

Requires Pillow: python render_overlay.py /path/to/1.jpg --output overlay_rebuilt.png
The original manuscript image is verified by SHA-256 and is never modified.
The shipped image uses Windows Arial; DejaVu Sans is a fallback on other systems.
"""
from pathlib import Path
from statistics import median
import argparse
import hashlib
import json
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser()
parser.add_argument("source", type=Path)
parser.add_argument("--output", type=Path, default=Path("overlay_rebuilt.png"))
args = parser.parse_args()
root = Path(__file__).resolve().parent
data = json.loads((root / "edition.json").read_text(encoding="utf-8"))
assert hashlib.sha256(args.source.read_bytes()).hexdigest() == data["source_image_sha256"], "Unexpected source image"
assert args.source.resolve() != args.output.resolve()
regular = "C:/Windows/Fonts/arial.ttf"
bold = "C:/Windows/Fonts/arialbd.ttf"
if not Path(bold).exists():
    regular, bold = "DejaVuSans.ttf", "DejaVuSans-Bold.ttf"
font = ImageFont.truetype(bold, 16)
small = ImageFont.truetype(bold, 10)
heading = ImageFont.truetype(bold, 20)
source = Image.open(args.source).convert("RGB")
pad, top, bottom = 20, 64, 36
canvas = Image.new("RGB", (source.width + 2*pad, source.height + top + bottom), "white")
canvas.paste(source, (pad, top))
draw = ImageDraw.Draw(canvas)
draw.text((pad, 8), "BnF italien 1583, f. 68 | 4 May 1446 | DECODE R7898", font=heading, fill="#252525")
draw.text((pad, 35), "Current key in red | ? = unresolved | Lasry / CTTS; refined by Astra and Fable 5.1", font=font, fill="#a00000")
for row in data["rows"]:
    cipher = [b for b in row["boxes"] if b["label"] != "[Plaintext]"]
    baseline = median(b["y"] for b in cipher) - 10
    for b in cipher:
        value = b["value"].upper()
        f = small if len(value) > 1 else font
        draw.text((pad + b["x"] + b["w"]/2, top + baseline), value, font=f, fill="#ed3030", anchor="mb")
draw.text((pad, canvas.height - 25), "Reproducible overlay from CTTS positions and key saved 20 October 2026; the clear text remains in the manuscript.", font=small, fill="#555555")
canvas.save(args.output, optimize=True)
print(args.output)
