"""b05: decode runs of the Schenck letter table (a = 7 8 9 ... in blocks of three; 67-69 v/w, 70 w, 76-78 y, 79 z).

    python b05_dec.py "34 20 32 43 ..." ["..." ...]
"""
import sys
ALPH = 'abcdefghiklmnopqrstuwxyz'
def L(n):
    n = int(n)
    if n == 70: return 'w'
    if n in (76, 77, 78): return 'y'
    if n == 79: return 'z'
    if 7 <= n <= 69: return ALPH[(n - 7) // 3]
    return '<%d>' % n
for a in sys.argv[1:]:
    print(a, '->', ''.join(L(x) for x in a.replace('.', ' ').split()))
