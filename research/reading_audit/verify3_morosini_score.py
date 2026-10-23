"""VERIFY_BRIEF pass 3, morosini1588: score the "## Reading" body of each texts/<R>_reading.md.

    PYTHONUTF8=1 python research/reading_audit/verify3_morosini_score.py [R..] > out.json

Prints {R: {"share": clean_share, "words": n, "supplied": [..] count, "partly": [?..] count}}.
"""
import json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
T = os.path.join(ROOT, 'targets', 'morosini1588', 'texts')
RECS = ('R17 R18 R19 R20 R21 R22 R27 R28 R29 R30 R31 R32 R33 R34 R35 R36 R37 R38 R39 R40 R41 R42 R43 R44 R45 '
        'R46 R47 R48 R49 R51 R52 R55 R56 R57 R58').split()


def body(r):
    txt = open(os.path.join(T, f'{r}_reading.md'), encoding='utf-8').read()
    m = re.search(r'^## Reading\s*$(.*?)(^## |\Z)', txt, re.S | re.M)
    return m.group(1)


def score(text):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(text)
    out = subprocess.run([sys.executable, os.path.join(ROOT, 'docs', '_check_reading.py'), '--file', f.name],
                         capture_output=True, text=True, encoding='utf-8', env=dict(os.environ, PYTHONUTF8='1')).stdout
    os.unlink(f.name)
    m = re.search(r'"clean_share":\s*([\d.]+)', out)
    w = re.search(r'"words":\s*(\d+)', out)
    return (float(m.group(1)) if m else None, int(w.group(1)) if w else None)


def main():
  res = {}
  for r in (sys.argv[1:] or RECS):
    b = body(r)
    s, w = score(b)
    brk = re.findall(r'\[([^\]]*)\]', b)
    res[r] = dict(share=s, words=w,
                  supplied=sum(1 for x in brk if x and not x.startswith('?') and not x.startswith('…')
                               and not re.fullmatch(r'\d+(\s*=.*)?', x) and x != '...'),
                  partly=sum(1 for x in brk if x.startswith('?')),
                  unread=sum(1 for x in brk if x.startswith('…') or x == '...'))
    print(r, res[r], file=sys.stderr)
  print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
