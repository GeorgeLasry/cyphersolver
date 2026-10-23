"""b08: malsburg1637 line decode with the group under each letter, for checking breaks on the images.

    python b08_dec.py <f003.txt ...>          each line: running decode, then group=letter pairs (P=1)
    python b08_dec.py --corr <corrections.tsv> <f003.txt>   apply corrections (line<TAB>old<TAB>new<TAB>why) first

Uses targets/malsburg1637/key.txt unchanged (letter signs as in dec.py); codes and unknown signs in [ ].
"""
import os, re, sys, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'malsburg1637'
K = {}
for line in open(T / 'key.txt', encoding='utf8'):
    if not line.startswith('#'):
        for kv in line.split():
            k, v = kv.split('=')
            K[k] = v


def tok(t):
    t0 = t.rstrip("'?_")
    if re.fullmatch(r'\d\d', t0):
        return K.get(t0, '?')
    if t0 in K and not t0.endswith('#'):
        return K[t0].upper()
    return f'[{t}]'


def dec(line):
    out, pairs = [], []
    for m in re.finditer(r'\{([^}]*)\}|(\S+)', line):
        if m.group(1) is not None:
            out.append(' {' + m.group(1) + '} ')
            continue
        v = tok(m.group(2))
        out.append(v)
        pairs.append(f'{m.group(2)}={v}')
    return ''.join(out), ' '.join(pairs)


def load(f, corr=None):
    lines = [l.rstrip('\n') for l in open(f, encoding='utf8')]
    if corr:
        for row in open(corr, encoding='utf8'):
            if row.startswith('#') or not row.strip():
                continue
            n, old, new = row.rstrip('\n').split('\t')[:3]
            n = int(n)
            assert old in lines[n - 1], (n, old, lines[n - 1])
            lines[n - 1] = lines[n - 1].replace(old, new, 1)
    return lines


if __name__ == '__main__':
    a = sys.argv[1:]
    corr = None
    if a and a[0] == '--corr':
        corr = a[1]; a = a[2:]
    for f in a:
        print('=====', f)
        for i, line in enumerate(load(f, corr), 1):
            if line.startswith('#'):
                if 'letter-cipher' in line:
                    break
                print(f'{i:3d} {line}')
                continue
            d, p = dec(line)
            print(f'{i:3d} {d}')
            if os.environ.get('P'):
                print('     ' + p)
