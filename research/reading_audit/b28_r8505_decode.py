"""b28: decode harley1582r8505 final/f*.txt with key.json, fixing reading.py's bug (a lone '#' is the d sign, not a
code; '#81' etc. are nomenclator numbers). Prints per run the raw letters and a word segmentation.
    python research/reading_audit/b28_r8505_decode.py [files-glob]  (default targets/harley1582r8505/final/f*.txt)"""
import sys, os, json, glob, re, collections, math, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from lang import lm
T = ROOT / 'targets' / 'harley1582r8505'
key = json.load(open(T / 'key.json'))
VC = ROOT / 'lang' / 'cache' / 'r8505_vocab_b28.json'   # git-ignored cache
if VC.exists():
    VOC = json.load(open(VC))
else:
    cnt = collections.Counter()
    for f in glob.glob(str(ROOT / 'lang' / 'corpora' / 'fr-*.txt')):
        cnt.update(w for w in lm.norm(open(f, encoding='utf-8', errors='replace').read(), 'early').split() if len(w) <= 18)
    tot = sum(cnt.values())
    VOC = {w: math.log(c / tot) for w, c in cnt.items() if c >= 2}
    json.dump(VOC, open(VC, 'w'))
UNK = -16.0; BCOST = 1.0

def segment(s):
    n = len(s); best = [-1e18] * (n + 1); bp = [0] * (n + 1); best[0] = 0
    for i in range(1, n + 1):
        b = best[i - 1] + UNK; p = i - 1
        for j in range(max(0, i - 18), i):
            lp = VOC.get(s[j:i])
            if lp is not None and best[j] + lp - BCOST > b: b, p = best[j] + lp - BCOST, j
        best[i] = b; bp[i] = p
    out = []; i = n
    while i > 0:
        j = bp[i]; w = s[j:i]; out.append(w if w in VOC else w.upper()); i = j
    return ' '.join(reversed(out))

def decode_field(field):
    out = []; seg = []
    for t in field.replace('/', ' ').split():
        t = t.rstrip('?')
        if re.fullmatch(r'[:.]+|:[234]', t) or t in ('DOT',):
            seg.append('m'); continue
        if t == '-' or not t:
            continue
        if re.fullmatch(r'#\d+', t):
            if seg: out.append(''.join(seg)); seg = []
            out.append('[%s]' % t[1:]); continue
        seg.append(key.get(t, '?'))
    if seg: out.append(''.join(seg))
    return out

if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob(str(T / 'final' / 'f*.txt')))
    tot = cov = 0
    for fn in files:
        for line in open(fn, encoding='utf-8'):
            p = [x.strip() for x in line.rstrip('\n').split('|')]
            if len(p) < 3: continue
            pieces = [x for f in p[2::2] for x in decode_field(f) + ['|']][:-1]
            raw = ' '.join(pieces)
            pieces = [x for x in pieces if x != '|']
            sg = ' '.join(x if x.startswith('[') else segment(x) for x in pieces)
            for x in pieces:
                if not x.startswith('['):
                    tot += len(x); s = segment(x); cov += sum(len(w) for w in s.split() if not w.isupper())
            print('%s\t<%s>\t%s\t||\t%s\t<%s>' % (p[0], p[1][-35:], raw, sg, p[-1][:35] if len(p) > 3 else ''))
    print('letters', tot, 'in words', cov, '%.3f' % (cov / max(1, tot)), file=sys.stderr)

def show(fn):
    """token / letter pairs per run, for checking against the image."""
    for line in open(fn, encoding='utf-8'):
        p = [x.strip() for x in line.rstrip('\n').split('|')]
        if len(p) < 3: continue
        toks = ' | '.join(p[2::2]).replace('/', ' ').split()
        print(p[0], ' '.join('%s=%s' % (t, 'm' if re.fullmatch(r'[:.]+|:[234]', t.rstrip('?')) else ('[%s]' % t[1:] if re.fullmatch(r'#\d+', t) else key.get(t.rstrip('?'), '?'))) for t in toks))
