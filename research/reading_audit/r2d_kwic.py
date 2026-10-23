"""r2d (23 Oct 2026): contexts of a Spagna 423 group in the b04 decode files (labels around each occurrence).

    python research/reading_audit/r2d_kwic.py <group> [width]
"""
import glob, pathlib, re, sys
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'nunzio1736' / 'texts'


def tokens(f):
    ls = f.read_text(encoding='utf8').split('\n')
    out = []
    i = 2
    while i + 1 < len(ls):
        a, b = ls[i].split(), ls[i + 1].split()
        if ls[i].startswith('Running decode'): break
        if a and all(re.fullmatch(r'[\d?]+', x) for x in a) and len(a) == len(b):
            out += list(zip(a, b)); i += 3; continue
        i += 1
    return out


if __name__ == '__main__':
    g, w = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 12
    for f in sorted(T.glob('423-*_decode_b04.txt'), key=lambda p: int(p.name.split('-')[1].split('_')[0])):
        ts = tokens(f)
        for k, (c, l) in enumerate(ts):
            if c == g:
                L = ''.join(x[1] if not x[1].startswith(('{', '[', '<', '(')) else ' ' + x[1] + ' ' for x in ts[max(0, k - w):k])
                R = ''.join(x[1] if not x[1].startswith(('{', '[', '<', '(')) else ' ' + x[1] + ' ' for x in ts[k + 1:k + 1 + w])
                print(f'{f.name[:6]:7s} {k:4d}  {L[-60:]:>60s} [{g}={l}] {R[:60]}')
