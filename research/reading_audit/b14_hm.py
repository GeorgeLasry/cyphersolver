"""b14: hm1645 - decode each cipher line of Lasry's interlinear file (DECODE D3060, scratchpad copy) with his key
(D3059), print it beside his plaintext line, and list the lines whose columns do not line up.

    python research/reading_audit/b14_hm.py <dir with DOC files> <section e.g. 0213-0215>
"""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'hm1645'))
from apply_key import load_key
D = pathlib.Path(sys.argv[1]); sec = sys.argv[2]
key = load_key(D / 'DOC_R785_D3059_3059.txt')
# b14 changes: two key corrections that hold in every occurrence, and code values proposed from the codebook's
# alphabetical bands plus context (printed in braces; the reading marks single-context ones [?word]).
key.update({'292': 'BY', '435': 'NEXT'})
PROPOSED = {'295': 'business', '313': 'concern', '325': 'do', '326': 'doth', '329': 'design', '330': 'dispatch',
            '340': 'foot', '363': 'haste', '372': 'her', '392': 'lord', '405': 'master', '446': 'particular',
            '457': 'post', '459': 'public', '474': 'remainder', '475': 'religion', '476': 'rebel', '491': 'sir',
            '495': 'see', '497': 'succour', '498': 'ship', '502': 'she', '514': 'them', '518': 'those', '528': 'there',
            '539': 'what', '548': 'who', '164': 'Ireland', '221': 'Pope', '229': 'Rome', '124': 'England', '335': 'ever'}
if '--plain' not in sys.argv:
    for g, v in PROPOSED.items(): key[g] = '{' + v + '}'
cur, lines = None, []
for l in (D / 'DOC_R785_D3060_3060.txt').read_text(encoding='utf-8', errors='replace').splitlines():
    m = re.match(r'#{6,}\s*tna[ _]sp106.(\S+?)(\.txt)?\s*$', l)
    if m: cur = m.group(1); continue
    if cur == sec: lines.append(l)
body = []
for l in lines:
    if l.lstrip().startswith('#IMAGE') or l.lstrip().startswith('#COMMENTS'): body.append(('#', l.strip())); continue
    if not l.strip() or l.lstrip().startswith(('#', '<CLEAR')): continue
    body.append(('t', l))
i = 0; n = 0; mis = 0
rows = [b for b in body]
k = 0
while k < len(rows):
    t, l = rows[k]
    if t == '#': print(l); k += 1; continue
    c = l.rstrip().rstrip('|').split(); p = rows[k + 1][1].rstrip().rstrip('|').split(); k += 2; n += 1
    dec = ''.join((key[g] if len(key.get(g, '?')) == 1 else ' ' + key[g] + ' ') if g in key else (' <%s> ' % g if len(g) == 3 else '_') for g in c)
    flag = '' if len(c) == len(p) else '  ** COLUMNS %d/%d' % (len(c), len(p))
    print('%3d K: %s%s' % (n, ' '.join(dec.split()), flag))
    print('    L: %s' % ' '.join(p))
