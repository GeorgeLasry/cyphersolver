"""Decode a Deboli cipher transcription with the key rebuilt from the pairs.

Known groups print their value. An unknown group prints [lo~hi], the values of the nearest known groups below and
above it in the same alphabetical run, which brackets what it can stand for. Coverage is counted over cipher tokens.

usage: python decode.py c107_1789-12-22 [--key key_pass.tsv] [--boundary 1860]
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from align import read_cipher, num  # noqa: E402


def load_key(path, mincount=1):
    key = {}
    for line in open(path, encoding='utf-8'):
        if line.startswith('#'):
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) < 3 or p[1] == '?':
            continue
        k = int(p[2].split('/')[0]) if '/' in p[2] else int(p[2] or 0)
        if not p[1] and k < 3:
            continue  # empty value seen once or twice: not a null, just unaligned
        if k >= mincount:
            key[p[0]] = p[1]
    return key


def bracket(v, key, boundary):
    n = num(v)
    run = sorted((num(k), s) for k, s in key.items() if s and (num(k) >= boundary) == (n >= boundary))
    lo = max((x for x in run if x[0] < n), default=(0, ''))
    hi = min((x for x in run if x[0] > n), default=(0, ''))
    return f'[{lo[1]}~{hi[1]}]'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('stem')
    ap.add_argument('--key', default='key_pass.tsv')
    ap.add_argument('--boundary', type=int, default=1860)
    ap.add_argument('--mincount', type=int, default=1)
    a = ap.parse_args()
    key = load_key(os.path.join(HERE, a.key), a.mincount)
    toks = read_cipher(os.path.join(HERE, 'transcription', a.stem + '.txt'))
    known = 0
    line, buf = None, []
    out = []
    for v, loc, unsure in toks:
        if loc != line:
            if buf:
                out.append(f'{line}: ' + ' '.join(buf))
            line, buf = loc, []
        if v.startswith('='):
            known += 1
            buf.append('«' + v[1:] + '»')
        elif v in key:
            known += 1
            buf.append((key[v] or '·') + ('?' if unsure else ''))
        elif re.sub(r'[a-z]$', '', v) in key:
            buf.append(key[re.sub(r'[a-z]$', '', v)] + '{' + v + '}')
        else:
            buf.append(bracket(v, key, a.boundary) + v)
    out.append(f'{line}: ' + ' '.join(buf))
    print('\n'.join(out))
    print(f'# {known}/{len(toks)} tokens with a value from the key ({100 * known / max(len(toks), 1):.1f}%)')


if __name__ == '__main__':
    main()
