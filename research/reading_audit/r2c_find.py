"""r2c (23 Oct 2026): find lines in kurtz1639 tr/ files containing a token sequence; print file, side, line no/of.
    python research/reading_audit/r2c_find.py R3813 "29 m" """
import sys, glob, os, re
rec, pat = sys.argv[1], sys.argv[2]
for f in sorted(glob.glob(f'targets/kurtz1639/tr/IMG_{rec}_*.txt')):
    side, lines = 'F', {}
    for l in open(f, encoding='utf8'):
        s = l.strip()
        if s.startswith('## '):
            side = 'L' if 'left' in s.lower() else 'R' if 'right' in s.lower() else 'F'; continue
        if not s or s.startswith('#') and not s.startswith('#4') and not re.match(r'#[a-z]', s) or s.startswith('legend'): continue
        lines.setdefault(side, []).append(s)
    for sd, ls in lines.items():
        for i, s in enumerate(ls):
            if re.search(r'(^|\s)' + re.escape(pat) + r'($|\s)', s):
                print(os.path.basename(f)[:-4], sd, i + 1, '/', len(ls), ':', s)
