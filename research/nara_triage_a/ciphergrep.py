"""Grep a cached item's OCR for cipher/decipher words and print frame + context."""
import sys, re
from analyze import frames
rx = re.compile(r'.{0,80}\b(de-?c[iy]pher\w*|c[iy]pher\w*|cypher\w*|decoded|in figures|not decyph\w*|translation)\b.{0,80}', re.I)
sys.stdout.reconfigure(encoding='utf-8')
for naid in sys.argv[1:]:
    for fn, url, text in frames(naid):
        t = ' '.join(text.split())
        for m in rx.finditer(t):
            print(fn, '|', m.group(0))
