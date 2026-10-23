"""r2b: rejoin pass2/reading.txt (augurelio1535) into running text, one paragraph per page, word splits at line ends
joined by hand (JOIN = line labels whose last word continues on the next line). Prints the body."""
import re, sys, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets/augurelio1535/pass2/reading.txt'
JOIN = set('P3.05 P3.08 P3.12 P3.13 P3.17 P3.23 P3.24 P3.29 P5.03 P5.05 P5.06 P5.09 P5.15 P5.23 P6.01 P6.03 P6.09 '
           'P6.12 P6.16 P6.17 P6.25 P6.26 P6.32 P6.34 P4.02'.split())
L = [l.rstrip('\n') for l in T.read_text(encoding='utf8').splitlines() if re.match(r'P\d\.\d\d ', l)]
paras, cur, page = [], '', None
for l in L:
    lab, t = l[:5], l[6:].strip()
    if lab[:2] != page:
        if cur: paras.append(cur)
        cur, page, glue = '', lab[:2], ' '
    cur = (cur + glue + t) if cur else t
    glue = '' if lab in JOIN else ' '
paras.append(cur)
body = '\n\n'.join(paras)
body = body.replace('[V]und', '{V} und')
sys.stdout.write(body + '\n')
