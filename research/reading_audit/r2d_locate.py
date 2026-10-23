"""r2d (23 Oct 2026): where a token of a Spagna 423 b04 decode sits in the DECODE transcription (image, line), with
the line's digits shown and the token's digits bracketed; optionally crop that line band from the page image.

    python research/reading_audit/r2d_locate.py <item> <token-index-without-nulls> [img-dir out-dir]
"""
import os, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
import b04_seg as S


def lines(item):
    t = open(os.path.join(S.T, 'decode', 'keep', 'DOC_%s.txt' % S.DOC[item]), encoding='utf8', errors='replace').read()
    img, out, k = None, [], 0
    for raw in t.split('\n'):
        m = re.match(r'#IMAGE NAME:\s*(\S+)', raw)
        if m and not '-' in m.group(1): img = m.group(1); ln = 0; continue
        s = re.sub(r'<[^>]*>', ' ', raw); s = re.sub(r'#.*', ' ', s)
        n = sum(1 for tok in s.split() if re.sub(r'[^0-9?]', '', tok))
        if n:
            ln += 1; out.append((img, ln, k, k + n, s.strip())); k += n
    return out


def where(item, idx):
    ds = S.digits(item); tk = S.segment(ds)
    pos, j, nn = 0, 0, 0
    starts = []
    for t in tk:
        starts.append(pos); pos += len(t)
    real = [i for i, t in enumerate(tk) if t != '7']
    ti = real[idx]; d0 = starts[ti]; d1 = d0 + len(tk[ti])
    for img, ln, a, b, s in lines(item):
        if a <= d0 < b:
            return img, ln, a, b, ''.join(ds[a:d0]) + '[' + ''.join(ds[d0:d1]) + ']' + ''.join(ds[d1:b]), tk[ti]


if __name__ == '__main__':
    item = int(sys.argv[1])
    for x in sys.argv[2].split(','):
        print(x, where(item, int(x)))
