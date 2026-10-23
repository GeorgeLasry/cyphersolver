"""r2p (23 Oct 2026), morosini1588: turn an r2p_parseall.py listing into log lines, one per remaining hole, with a
default blocker (nothing written / too-short: 1-3 figures / no-key-material: no parse fits), to be corrected by hand
after the image check (illegible etc.).

    python research/reading_audit/r2p_logskel.py <parses.txt> [ILLEGIBLE_PAGES like 181v,183v]
"""
import re, sys

lines = open(sys.argv[1], encoding='utf8').read().split('\n')
ill = set(sys.argv[2].split(',')) if len(sys.argv) > 2 else set()
k = 0
seen = set()
while k < len(lines):
    ln = lines[k]
    m = re.match(r'(\S+) l\.([\d,]+)\t(.*)', ln)
    if m and k + 1 < len(lines) and 'figs:' in lines[k + 1]:
        page, ls, ctx = m.groups()
        figs = lines[k + 1].split('figs:', 1)[1].strip()
        hole = re.search(r'<<(.*?)>>', ctx)
        hole = hole.group(1) if hole else '?'
        if re.search(r'm\[ente\]|\[simo\]|\[issimo\]|\[ezza\]|\[olica\]', hole):
            k += 2; continue
        key = (page, ls, figs)
        best = lines[k + 2].split()[1] if k + 2 < len(lines) and re.match(r'\s+-?\d', lines[k + 2]) else ''
        nfig = len(re.findall(r'\d+', figs)) if not figs.startswith('(') else 0
        if nfig == 0:
            b = 'nothing written there; no-key-material'
        elif nfig <= 3 and not hole.startswith('[?'):
            b = 'too-short'
        else:
            b = 'no-key-material'
        if page in ill and nfig:
            b = 'illegible (spread ink and show-through)'
        ctx2 = re.sub(r'\s+', ' ', ctx.replace('<<', '').replace('>>', '')).strip()
        dup = key in seen
        seen.add(key)
        if not dup:
            print(f'- {page} l. {ls.replace(",", "-")} "{ctx2}": "{figs}"' + (f' (best parse "{best}")' if best and nfig > 3 else '') + f'. Blocker: {b}.')
        k += 2
        continue
    k += 1
