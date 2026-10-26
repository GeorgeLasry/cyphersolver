"""Per-line sense check of the decipherments (dec_*.tsv) against early-modern French.

Groups tokens into lines at each '# line' / '# s...' comment, concatenates the letter readings (codes as 'x'), and
scores each line with fr-1600-letters (order 4, no spaces). Lines below the threshold are listed for re-reading.
Usage: python sense.py [threshold]   (default -3.0 per char; real text scores about -2, shuffled letters about -5)
"""
import glob, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
TH = float(sys.argv[1]) if len(sys.argv) > 1 else -3.0
model = lm.load('fr-1600-letters', order=4, spaces=False)
good = bad = 0
flag = []
for f in sorted(glob.glob(os.path.join(HERE, 'dec_*.tsv'))):
    lines, cur, label = [], [], 'start'
    for raw in open(f, encoding='utf8'):
        if raw.startswith('# line') or re.match(r'# s\d', raw):
            if cur: lines.append((label, cur))
            cur, label = [], raw[2:60].strip()
            continue
        if raw.startswith('#') or '\t' not in raw:
            continue
        tok, val = raw.rstrip('\n').split('\t')[:2]
        val = val.strip()
        if val == '|' or val.startswith('['):
            continue
        if re.fullmatch(r'\d+', tok.strip()):
            continue
        if re.fullmatch(r'[a-z]{1,2}', val):
            cur.append(val)
        else:
            cur.append('?')
    if cur: lines.append((label, cur))
    for label, toks in lines:
        text = ''.join(t for t in toks if t != '?')
        if len(text) < 12:
            continue
        sc = model.per_char(text)
        n = len(toks)
        if sc >= TH:
            good += n
        else:
            bad += n
            flag.append((os.path.basename(f), label, round(sc, 2), ''.join(toks)[:70]))
tot = good + bad
print(f'letter signs on lines scoring >= {TH}: {good}/{tot} ({good / tot:.1%})')
print(f'{len(flag)} lines flagged:')
for x in flag:
    print('  ', *x)
