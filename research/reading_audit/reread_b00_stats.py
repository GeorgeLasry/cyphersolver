"""Batch b00 (morosini1588): per-record figures for the profile — items, clean share before/after, holes, corrections.

    PYTHONUTF8=1 python research/reading_audit/reread_b00_stats.py > <scratch>/stats.json
"""
import csv, glob, io, json, os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import reread_b00_decode as D  # noqa: E402

T = os.path.join(ROOT, 'targets', 'morosini1588')
RECS = 'R17 R18 R19 R20 R21 R22 R27 R28 R29 R30 R31 R32 R33 R34 R35 R36 R37 R38 R39 R40 R41 R42 R43 R44 R45 R46 R47 R48 R49 R51 R52 R55 R56 R57 R58'.split()


def share(path):
    out = subprocess.run([sys.executable, os.path.join(ROOT, 'docs', '_check_reading.py'), '--file', path],
                         capture_output=True, text=True, encoding='utf-8', env=dict(os.environ, PYTHONUTF8='1')).stdout
    m = re.search(r'"clean_share":\s*([\d.]+)', out)
    w = re.search(r'"words":\s*(\d+)', out)
    return (float(m.group(1)) if m else None, int(w.group(1)) if w else None)


res = {}
for r in RECS:
    c = glob.glob(os.path.join(T, 'decode', f'DOC_{r}_D1[67]*.txt'))
    path = c[0] if c else os.path.join(T, 'R17_transcription_decode.txt')
    items = sum(len(i) for p, i in D.parse(path) if p)
    dec = os.path.join(T, 'texts', f'{r}_decryption.txt') if r != 'R17' else os.path.join(T, 'R17_decryption.txt')
    before = share(dec)[0]
    txt = open(os.path.join(T, 'texts', f'{r}_reading.md'), encoding='utf-8').read()
    m = re.search(r'^## Reading\s*$(.*?)(^## |\Z)', txt, re.S | re.M)
    bodyt = m.group(1)
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(bodyt)
    after, words = share(f.name)
    os.unlink(f.name)
    unread = len(re.findall(r'\[…\]|\[\.\.\.\]', bodyt))
    partly = len(re.findall(r'\[\?', bodyt))
    codes = len(re.findall(r'\[\d{2,4}\]', bodyt))
    rows = list(csv.reader(open(os.path.join(T, 'texts', f'{r}_corrections.tsv'), encoding='utf-8'), delimiter='\t'))[1:]
    basis = [x[-1].strip() for x in rows if x]
    res[r] = dict(items=items, before=before, after=after, words=words, unread=unread, partly=partly, codes=codes,
                  corr=len(rows), image=sum(1 for b in basis if b.startswith('image')),
                  context=sum(1 for b in basis if 'context' in b))
    print(r, res[r], file=sys.stderr)
print(json.dumps(res, indent=1))
