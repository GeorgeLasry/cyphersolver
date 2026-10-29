"""Fill the @@...@@ placeholders of docs/visconti1446.html from texts/ (token counts and readings). Run from the repo root
once, after the slips are final: python targets/visconti1446/fill_page.py"""
import html, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, 'texts')
PAGE = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'docs', 'visconti1446.html')

ROWS = [  # folio, volume, date and place, canvas or record, clear text
 (110, 1583, '1 Nov 1446, Milan', 'DECODE R7902', 'none found'),
 (130, 1583, '25 Nov 1446, Milan', 'DECODE R7904', 'translation f. 131 (not reached)'),
 (136, 1583, '29 Nov 1446, Milan', 'DECODE R7907', 'none'),
 (154, 1583, '12 Dec 1446, Milan', 'DECODE R7914', 'none'),
 (158, 1583, '31 Dec 1446, Cusago', 'DECODE R7915', 'none'),
 (5, 1584, '10 Jan 1447, Abbiategrasso', 'canvas 9', 'translation f. 6 (1447)'),
 (8, 1584, '11 Jan 1447, Abbiategrasso', 'canvas 11', 'translation f. 9 (1447)'),
 (24, 1584, '5 Feb 1447, Milan', 'canvas 24', 'none'),
 (23, 1584, 'the same, re-sent 24 Feb', 'canvas 24', 'none'),
 (30, 1584, '9 Feb 1447, Milan', 'canvas 30', 'later copy f. 29'),
 (31, 1584, 'the same, re-sent 24 Feb', 'canvas 30', 'later copy f. 29'),
 (36, 1584, '12 Feb 1447, Milan', 'canvas 34', 'later copy f. 35'),
 (37, 1584, 'the same, re-sent 25 Feb', 'canvas 34', 'later copy f. 35'),
 (64, 1584, '6 Mar 1447, Milan', 'canvas 62', 'later copy f. 63'),
 (65, 1584, 'the same, sent again that day', 'canvas 62', 'later copy f. 63'),
 (72, 1584, '7 Mar 1447, Milan', 'canvas 69', 'none'),
 (83, 1584, '11 Mar 1447, Milan', 'canvas 80', 'later copy ff. 82, 85 (sample checked)'),
 (94, 1584, '18 Mar 1447, Milan', 'canvas 91', 'later copy f. 92 (sample checked)'),
 (102, 1584, '23 Mar 1447, Milan (duplicate)', 'canvas 98', 'none (f. 103 is a parallel letter)'),
]


def counts(n):
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, f'f{n}_tokens.tsv'), encoding='utf-8')]
    rows = [r for r in rows if len(r) >= 3 and r[0] != 'line']
    tot = len(rows); nul = sum(1 for r in rows if r[2] in ('{null}', '{null?}')); unr = sum(1 for r in rows if '[..]' in r[2])
    return tot, nul, unr


def reading(n):
    s = open(os.path.join(T, f'f{n}_reading.md'), encoding='utf-8').read().split('\n', 2)[2].strip()
    return html.escape(re.sub(r'\s+', ' ', s), quote=False)


page = open(PAGE, encoding='utf-8').read()
trs, T_all, R_all = [], 0, 0
for f, vol, date, where, clear in ROWS:
    tot, nul, unr = counts(f); T_all += tot; R_all += tot - nul - unr
    share = (tot - nul - unr) / (tot - nul)
    shown = f'{share:.1%}' + (' (sample)' if f in (83, 94) else '')
    trs.append(f'<tr><td>ital. {vol} f. {f}</td><td>{date}</td><td>{shown}</td><td>{clear}</td></tr>')
t110, n110, u110 = counts(110)
rep = {'@@TABLE@@': '\n'.join(trs), '@@TOTAL@@': f'{T_all:,}', '@@TOTREAD@@': f'{R_all:,}',
       '@@F110@@': f'{(t110 - n110 - u110) / (t110 - n110):.0%} of signs read',
       '@@F110OPEN@@': f'{u110:,} of {t110 - n110:,} signs unread, most of the recto body and the verso.',
       '@@F136@@': reading(136), '@@F158@@': reading(158), '@@F24@@': reading(24), '@@F72@@': reading(72),
       '@@F102@@': reading(102)}
for k, v in rep.items():
    page = page.replace(k, v)
assert '@@' not in page, re.findall(r'@@\w+@@', page)
open(PAGE, 'w', encoding='utf-8').write(page)
print(f'filled: {R_all} of {T_all} signs read')
