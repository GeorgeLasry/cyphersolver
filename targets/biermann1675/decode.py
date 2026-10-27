"""decode.py <transcription>: decipher a transcription with key.tsv; prints line-by-line plaintext
and the share of cipher tokens that the key resolves.

Signs are mapped by the labels documented in key.tsv. Clear words in [ ] are passed through.
Unknown tokens are printed as <token>.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

SIGNS = {
    # set1
    'H': 'a', 'n8': 'b', 'E': 'c', 'Z': 'd', 'y': 'e', 'lam': 'f', 'phi': 'g', 'box': 'h', 'th': 'i',
    'Lc': 'k', 'x=': 'l', 'a': 'm', 'III': 'n', 'q-': 'o', '^': 'p', 'hb': 'q', '8s': 'r', 'w': 's',
    'q': 't', 'cf': 'u', '7s': 'w', 'b-': 'x', 'nn': 'y', 'M-': 'z',
    # set2
    'g': 'a', 'db': 'b', 'A-': 'c', 'T': 'd', 'K': 'e', '#': 'f', 'psi': 'g', 'Cs': 'h', 'zh': 'i',
    'O': 'k', 'D': 'l', 'Gam': 'm', 'pi': 'n', 'ff': 'o', 'del': 'p', 'dia': 'q', 'A': 'r', 'J': 's',
    'q=': 't', 'X': 'u', 'q-l': 'w', 'C': 'x', 'm3': 'y', '###': 'z',
}


def load_key():
    key = {}
    with open(os.path.join(HERE, 'key.tsv'), encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            code, val = line.rstrip('\n').split('\t')[:2]
            key[code] = val
    return key


def main(path):
    key = load_key()
    total = known = 0
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^(p\d+v?\.\d+)\s+(.*)$', line.strip())
        if not m:
            continue
        ref, body = m.groups()
        out = []
        for tok in re.findall(r'\[[^\]]*\]|\S+', body):
            if tok.startswith('['):
                out.append(' ' + tok[1:-1].upper() + ' ')
                continue
            total += 1
            val = key.get(tok) if tok.isdigit() else SIGNS.get(tok)
            if val is None:
                out.append(f'<{tok}>')
            else:
                known += 1
                out.append(val.split(' ')[0] if tok.isdigit() and len(val) <= 4 else f'{{{val}}}')
        print(f'{ref}  {"".join(out).strip()}')
    print(f'\ncipher tokens: {total}; resolved by key: {known} ({100 * known / max(total, 1):.1f}%)')


if __name__ == '__main__':
    main(sys.argv[1])
