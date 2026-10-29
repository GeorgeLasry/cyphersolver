"""Zoom a region of a canvas: python texts/zoom.py <canvas> x0 y0 x1 y1 <outname> [scale] -> img/<outname>.jpg (run from targets/visconti1446)"""
import sys
from PIL import Image
c,x0,y0,x1,y1=map(int,sys.argv[1:6]); out=sys.argv[6]; sc=float(sys.argv[7]) if len(sys.argv)>7 else 2
im=Image.open(f'img/c{c}.jpg').crop((x0,y0,x1,y1)); im.resize((int(im.width*sc),int(im.height*sc)),Image.LANCZOS).save(f'img/{out}.jpg')
