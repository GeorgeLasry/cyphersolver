"""r2i: print raw N.60 transcription lines (labels) and their build for lines a..b.  python r2i_n60lab.py L0414 L0420"""
import sys, re, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'vich1511'
a, b = sys.argv[1], sys.argv[2]
B = {l.split(' | ')[0]: l.split(' | ', 1)[1].strip() for l in open(T / 'n60_build.txt', encoding='utf8') if re.match(r'L\d{4} \|', l)}
for l in open(T / 'n60_transcription_v4.txt', encoding='utf8'):
    m = re.match(r'(L\d{4}):(.*)', l)
    if m and a <= m.group(1) <= b:
        print(m.group(1), m.group(2).strip(), '   >', B.get(m.group(1), ''))
