"""v2 verify sweep (23 Oct 2026): ottobon ff. 37r-38r, score the crib-fit reading with the doubtful tokens as holes.

    python research/reading_audit/v2_ottobon_holes.py <out.md>

rd_f37r/f37v/f38r.txt give per line the tokens (ct:, '?' = token in a gap or channel log-prob < -5, i.e. a value the
crib fit set by sense) and the Italian (it:). Per line, the Italian is kept and every doubtful token not already
covered by an explicit gap ([...], ...) in that line is added as one hole [?]; lines marked conf: low become one hole
per token. Lines are joined page by page as in reading.txt.
"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'ottobon'
out = ['## Reading']
for pg in ('f37r', 'f37v', 'f38r'):
    blocks = re.split(r'^# f\.\S+ l\.\d+\s*$', (T / f'rd_{pg}.txt').read_text(encoding='utf-8'), flags=re.M)[1:]
    para = []
    for b in blocks:
        ct = re.search(r'^ct:\s*(.*)$', b, re.M); it = re.search(r'^it:\s*(.*)$', b, re.M)
        cf = re.search(r'^conf:\s*(\w+)', b, re.M)
        if not ct or not it: continue
        toks = ct.group(1).split(); q = sum('?' in x for x in toks)
        if cf and cf.group(1) == 'low':
            para.append(' '.join(['[?]'] * len(toks))); continue
        gaps = len(re.findall(r'\[\.\.\.\]|\.\.\.|…', it.group(1)))
        para.append(it.group(1) + ' ' + ' '.join(['[?]'] * max(0, q - gaps)))
    out.append(' '.join(para))
pathlib.Path(sys.argv[1]).write_text('\n\n'.join(out) + '\n', encoding='utf-8')
print('written')
