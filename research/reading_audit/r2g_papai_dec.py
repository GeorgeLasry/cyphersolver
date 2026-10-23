"""r2g: decode one papai1706 transcription file (DECODE format, or a corrected copy) with decode2.py's rules and print
line by line (figures, then decode).   python r2g_papai_dec.py <transcription> [--figs]"""
import re, sys
from pathlib import Path
R = Path(__file__).resolve().parents[2] / 'targets' / 'papai1706'
FIGS = '--figs' in sys.argv
MAPS = [a[6:] for a in sys.argv if a.startswith('--map=')]   # r2g: --map=87=ar overrides a key value for one letter
path = [a for a in sys.argv[1:] if not a.startswith('--')][0]
_argv = sys.argv
sys.argv = [sys.argv[0]]
exec(open(R / 'decode.py', encoding='utf-8').read().split('if __name__')[0].replace('Path(__file__).resolve().parent', repr(str(R)).join(['Path(', ')'])))
EXTRA = {220: 'a'}
for m in MAPS:
    k_, v_ = m.split('=', 1); KEY[int(k_)] = v_
def val(n): return KEY.get(n, EXTRA.get(n))
def split(s):
    best = None
    def rec(i, acc):
        nonlocal best
        if i == len(s):
            if best is None or len(acc) < len(best): best = acc[:]
            return
        for w in (2, 3):
            p = s[i:i+w]
            if len(p) == w and p[0] != '0' and val(int(p)) is not None: rec(i+w, acc+[int(p)])
    rec(0, []); return best
def toks(line):
    s = re.sub(r"<[^>]*>", " | ", line); out = []
    for tok in re.split(r"\s{2,}|\|", s):
        t = tok.replace(" ", "").strip("—-–.,")
        if re.fullmatch(r"\d+", t): out.append(t)
    return out
n = 0
for line in Path(path).read_text(encoding='utf-8-sig', errors='replace').splitlines():
    if line.startswith('#'):
        if 'IMAGE' in line: print(line)
        continue
    # r2g: lines carrying a <PLAINTEXT> tag also carry figures (decode2.py skipped them whole); the tag is stripped by toks()
    t = toks(line); i = 0; o = []
    while i < len(t):
        x = t[i]; k = int(x)
        if k in KEY: o.append(show(k))
        elif k == 220: o.append('a')
        elif i+1 < len(t) and k <= 322 and val(int(x+t[i+1])) is not None and val(int(t[i+1])) is None:
            o.append(show(int(x+t[i+1]))); i += 1
        elif len(x) >= 4 and split(x): o.append(''.join(show(p) if p in KEY else 'a' for p in split(x)))
        elif len(x) == 3 and k > 322: o.append('·')
        else: o.append(f' [{x}] ')
        i += 1
    if t:
        n += 1
        if FIGS: print('%3d F %s' % (n, ' '.join(t)))
        print('%3d D %s' % (n, ''.join(o)))
