"""Word-by-word test of Confederate cipher words: for each cipher word, every key x offset x mode that yields an English
word (lexicon); then look for a consistent running offset across consecutive words.
    python vigword.py WORD WORD ...
"""
import gzip, json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
lex = json.load(gzip.open(os.path.join(HERE, '..', '..', 'lang', 'lexicons', 'en.json.gz'), 'rt', encoding='utf-8'))
words = set(w.lower() for w in (lex if isinstance(lex, list) else lex.keys()) if w.isalpha())
words |= {'thomas','mobile','corps','cavalry','meridian','augusta','richmond','pensacola','enemy','army','fourth','thousand'}
KEYS = ['MANCHESTERBLUFF', 'COMPLETEVICTORY', 'COMERETRIBUTION']
def dec(ct, key, off, mode):
    o = []
    for i, c in enumerate(ct):
        k = ord(key[(i + off) % len(key)]) - 65; x = ord(c) - 65
        o.append(chr(((x - k) if mode == 'vig' else (k - x) if mode == 'beau' else (x + k)) % 26 + 97))
    return ''.join(o)
def hits(w):
    w = ''.join(c for c in w.upper() if c.isalpha())
    out = []
    for key in KEYS:
        for mode in ('vig', 'beau', 'var'):
            for off in range(len(key)):
                p = dec(w, key, off, mode)
                if p in words and len(p) >= 3: out.append((key, mode, off, p))
    return w, out
if __name__ == '__main__':
    tot = 0
    for a in sys.argv[1:]:
        w, h = hits(a)
        if len(w) < 3: continue
        tot += 1
        print(w, len(h), h[:8])
