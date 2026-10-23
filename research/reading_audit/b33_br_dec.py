"""b33 riksarkivet1628 (Bremen 1631): decode two-digit groups with the band key.
    python b33_br_dec.py 97 36 40 43 ...      (non-numbers pass through)
"""
import sys
BANDS = 'a g n t b h o u c i p w d k q x e l r y f m s z'.split()
def dec(n):
    n = int(n)
    if 8 <= n <= 103:
        return BANDS[(n - 8) // 4]
    return '[%d]' % n
def run(toks):
    return ''.join(dec(t) if t.isdigit() else ' %s ' % t for t in toks)
if __name__ == '__main__':
    print(run(' '.join(sys.argv[1:]).replace(',', ' ').split()))
