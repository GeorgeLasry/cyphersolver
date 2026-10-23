"""v4 (23 Oct 2026): papai1706 - print, per cipher line, the decode2 reading (<rec>_read2.txt) beside the transcriber's
copy of the contemporary interlinear decipherment (<PLAINTEXT HU ...> lines of the DECODE transcription) and any
<CLEARTEXT> passage, to help word-divide the readings.   python v4_papai_lines.py <rec>   (e.g. R796)"""
import re, sys, pathlib
D = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'papai1706'
rec = sys.argv[1]
tr = next(D.glob(f'DOC_{rec}_D*_*.txt')).read_text(encoding='utf-8-sig').splitlines()
rd = [l for l in (D / f'{rec}_read2.txt').read_text(encoding='utf-8').splitlines() if not l.startswith('=====')
      and not l.startswith('#') and not l.startswith('--')]
plain, clear = [], []
for l in tr:
    for m in re.finditer(r'<CLEARTEXT[^ ]* ?[A-Z]* ([^>]*)>', l): clear.append(m.group(1).strip())
    m = re.match(r'\s*<PLAINTEXT[^ ]* ?[A-Z]* ([^>]*)>', l)
    if m: plain.append(re.sub(r'\s+', '', m.group(1)))
print('cleartext passages:', clear)
for i, r in enumerate(rd):
    print(f'{i:3} D {r}')
    if i < len(plain): print(f'    I {plain[i]}')
