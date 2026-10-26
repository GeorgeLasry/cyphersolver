"""Group the per-letter Torre do Tombo rows into one row per writer and volume (catalogue convention).

    python research/torre_do_tombo/group.py

Reads candidates_ungrouped.json (the sweep's original output; copied there on the first run) and writes
candidates.json.
"""
import json, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, OUT = os.path.join(HERE, 'candidates_ungrouped.json'), os.path.join(HERE, 'candidates.json')
if not os.path.exists(SRC):
    shutil.copy(OUT, SRC)
rows = json.load(open(SRC, encoding='utf-8'))

GROUPS = [
    (range(0, 6), 'João IV → marquês de Nisa, ambassador in Paris: six letters mostly in cipher, 1642-44 (embassy letter-book)',
     'ANTT, Manuscritos da Livraria, nº 1017 (PT/TT/MSLIV/1017), letters 9 ff.'),
    (range(8, 17), 'D. Fernando Teles de Faro → Francisco de Melo, The Hague embassy: nine letters in cipher, 1658-59',
     'ANTT, Miscelâneas Manuscritas do Convento da Graça, tomo 1E (PT/TT/MMCG/1E)'),
    (range(17, 27), 'Luís Álvares Ribeiro, embassy secretary at The Hague → Francisco de Melo: letters partly in cipher, 1659',
     'ANTT, Miscelâneas Manuscritas do Convento da Graça, tomo 2L (PT/TT/MMCG/2L)'),
    (range(27, 41), 'Conde de Miranda, ambassador at The Hague → Francisco de Melo: letters partly in cipher, 1659-60',
     'ANTT, Miscelâneas Manuscritas do Convento da Graça, tomo 3L (PT/TT/MMCG/3L)'),
    (range(59, 63), 'Paiva Couceiro monarchist papers: letters in or partly in cipher (Taveira, Joaquim Pais), 1921, with a draft giving the cipher',
     'ANTT, Henrique de Paiva Couceiro, mç. 24 (PT/TT/HPC/0024)'),
]


def code(r):
    m = re.search(r'\((PT/TT/[^)]+)\)', r['shelfmark'])
    return m.group(1) if m else r['shelfmark']


grouped, used = [], set()
for idx, title, shelf in GROUPS:
    part = [rows[i] for i in idx]
    used |= set(idx)
    g = dict(part[0])
    years = [r['year'] for r in part]
    g['year'] = min(years)
    g['date'] = f'{min(years)}-{max(years)}' if min(years) != max(years) else str(years[0])
    g['title'] = title
    g['shelfmark'] = shelf
    g['folio_note'] = f'{len(part)} letters: ' + '; '.join(f"{r['date']} ({code(r)})" for r in part)
    g['status'] = f'{len(part)} letters grouped. ' + part[0]['status']
    seen_links, links = set(), []
    for r in part:
        for l in r['links']:
            if l['href'] not in seen_links and (l['label'].startswith('Volume') or len(links) < 4):
                seen_links.add(l['href']); links.append(l)
    g['links'] = links
    if any(r['seen'] == 'image' for r in part): g['seen'] = 'image'
    if len({r['correspondents'] for r in part}) > 1 and 'Couceiro' in title:
        g['correspondents'] = 'José Rogério Taveira; Joaquim Pais → Henrique de Paiva Couceiro'
    grouped.append((min(idx), g))

out = [g for _, g in grouped] + [r for i, r in enumerate(rows) if i not in used]
out.sort(key=lambda r: r['year'])
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{len(rows)} rows -> {len(out)}')
