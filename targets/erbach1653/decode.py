"""Decipher a ct_*.txt transcription with key.txt (letter b of key line a). Clear text in {braces} kept.
Usage: python decode.py ct_004.txt [--cells key_cells.tsv]  (the second shows where crib cells disagree)"""
import re, sys
def load_key(path='key.txt'):
    K = {}
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        n, txt = l.split(' ', 1)
        K[int(n)] = re.sub(r'[^a-z?]', '', txt.lower())
    return K
K = load_key()
def val(a, b):
    row = K.get(a, '')
    return row[b - 1] if 0 < b <= len(row) else '#'
def decode_line(body):
    out = []
    for part in re.split(r'(\{[^}]*\}|\[X\]|\|)', body):
        if part.startswith('{'):
            out.append(' ' + part[1:-1] + ' ')
        elif part == '[X]':
            out.append('[X]')
        elif part == '|':
            out.append(' | ')
        else:
            out.append(''.join(val(int(a), int(b)) for a, b in re.findall(r'(\d+),(\d+)', part)))
    return re.sub(r' +', ' ', ''.join(out)).strip()
if __name__ == '__main__':
    path = sys.argv[1]
    for line in open(path, encoding='utf8'):
        if line.startswith('#') or not line.strip():
            continue
        lab = line.split()[0]
        print(lab, decode_line(line[len(lab):]))
    if '--cells' in sys.argv:
        print('\ncrib cells that disagree with the key text:')
        for l in open(sys.argv[sys.argv.index('--cells') + 1], encoding='utf8'):
            p = l.split('#')[0].split()
            if len(p) == 2:
                a, b = map(int, p[0].split(','))
                if val(a, b) != p[1]:
                    print(' ', p[0], 'crib', p[1], 'key', val(a, b))
