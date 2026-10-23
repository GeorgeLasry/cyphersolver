"""r2c (23 Oct 2026): build the reading body of R9414's read lines (wardein1537) from r9414/reading_v5.txt.
<run> doubtful runs -> [?run], [..n] -> n x [...], word? -> [?word]; bands P1.12-32, P2.15-19, P3.01-09, P3.39-P4.01,
P4.21-35, P5.05-07 left out (texts[1], decoded, not read). Paragraph per contiguous read range; line-end hyphens joined.
    python research/reading_audit/r2c_ward_body.py targets/wardein1537/r9414/reading_v5.txt
"""
import re, sys
BANDS = [('P1.12', 'P1.32'), ('P2.15', 'P2.19'), ('P3.01', 'P3.09'), ('P3.39', 'P4.01'), ('P4.21', 'P4.35'), ('P5.05', 'P5.07')]
k = lambda l: (int(l[1]), int(l[3:5]))
inb = lambda lab: any(k(a) <= k(lab) <= k(b) for a, b in BANDS)
paras, cur, prev_band = [], [], None
for line in open(sys.argv[1], encoding='utf8').read().splitlines():
    lab, _, t = line.partition(' ')
    b = inb(lab)
    if b:
        if cur: paras.append(cur); cur = []
        continue
    t = re.sub(r'<([^>]*)>', lambda m: '[?' + m.group(1).strip() + ']', t)
    t = re.sub(r'\[\.\.(\d)\]', lambda m: ' '.join(['[…]'] * int(m.group(1))), t)
    t = re.sub(r'(?<![\[\w])(\w+)\?', r'[?\1]', t)
    cur.append((lab, t))
if cur: paras.append(cur)
for p in paras:
    s = ''
    for lab, t in p:
        if s.endswith('-'): s = s[:-1] + t.lstrip()
        else: s = (s + ' ' + t).strip()
    print(f'{p[0][0]}-{p[-1][0]}: {s}\n')
