"""Render either red overlay from the original hash-verified source image.
python render_overlay.py SOURCE_IMAGE --document R7898 --output overlay.png
Use --document f70 for the companion. Requires Pillow; does not modify the source.
"""
from pathlib import Path
from statistics import median
import argparse,hashlib,json
from PIL import Image,ImageDraw,ImageFont
p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('--document',choices=['R7898','f70'],default='R7898');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
data=json.loads((Path(__file__).parent/'edition.json').read_text(encoding='utf-8'))
doc=next(d for d in data['documents'] if d['id']==a.document)
assert hashlib.sha256(a.source.read_bytes()).hexdigest()==doc['source_image_sha256'],'Wrong original image'
assert a.source.resolve()!=a.output.resolve()
font='C:/Windows/Fonts/arial.ttf';bold='C:/Windows/Fonts/arialbd.ttf'
if not Path(bold).exists():font,bold='DejaVuSans.ttf','DejaVuSans-Bold.ttf'
f=lambda n,b=False:ImageFont.truetype(bold if b else font,n)
im=Image.open(a.source).convert('RGB');scale=2
base=im.resize((im.width*scale,im.height*scale));canvas=Image.new('RGB',(base.width+40,base.height+90),'white');canvas.paste(base,(20,65));draw=ImageDraw.Draw(canvas)
draw.text((20,8),doc['shelfmark']+' | current key in red | ? unresolved; (8)=L, (24)=N, (16)=IN provisional',font=f(24,True),fill='#222')
draw.text((20,36),'Lasry / CTTS; refined by Astra and Fable 5.1 | 20 October 2026',font=f(18),fill='#555')
for rec in doc['rows']:
 glyphs=[b for b in rec['boxes'] if b['label']!='[Plaintext]'];y=median(b['y'] for b in glyphs)*scale+62
 for b in glyphs:
  value=b['value'].upper();draw.text((20+(b['x']+b['w']/2)*scale,y),value,font=f(15 if len(value)>1 else 22,True),fill='#e32626',anchor='mb')
canvas.save(a.output,optimize=True)
