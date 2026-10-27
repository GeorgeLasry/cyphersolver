"""Test Confederate letter-cipher runs against the three known Vigenere keys (and Beaufort/variant), every key offset.

    python vig.py "FOOR IWV BIDS SNECEY WBUII"     # prints best decrypts per key/mode with en-modern score
"""
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
KEYS = ['MANCHESTERBLUFF', 'COMPLETEVICTORY', 'COMERETRIBUTION']
M = lm.load('en-modern', order=4, spaces=False)

def dec(ct, key, off, mode):
    out = []
    for i, c in enumerate(ct):
        k = ord(key[(i + off) % len(key)]) - 65; x = ord(c) - 65
        p = (x - k) % 26 if mode == 'vig' else (k - x) % 26 if mode == 'beau' else (x + k) % 26
        out.append(chr(p + 97))
    return ''.join(out)

def test(text, top=3):
    ct = re.sub(r'[^A-Z]', '', text.upper())
    res = []
    for key in KEYS:
        for mode in ('vig', 'beau', 'var'):
            for off in range(len(key)):
                p = dec(ct, key, off, mode)
                res.append((M.per_char(p), key, mode, off, p))
    res.sort(reverse=True)
    return ct, res[:top]

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    for t in sys.argv[1:]:
        ct, best = test(t)
        print(ct)
        for s, k, m, o, p in best: print(f'  {s:.2f} {k} {m} off={o} {p}')
