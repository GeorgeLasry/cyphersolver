"""Rank the unscreened PARES hits by their hit-list title (offline; no requests to PARES).

    python research/pares_ags/screen.py [--base COMMIT]

Reads hits.jsonl, dedups by PARES id (the terms a row hit are joined), drops the ids already screened (every PARES
id linked from candidates.json, plus the 74 rows of the first sweep, read from hits.jsonl at COMMIT, default
afe1562b3) and scores the rest on the title, date and signatura alone:

  + cipher words: cifra, cifrada, en cifra, parte en cifra, contracifra, carta cifrada, descifrar,
    sin descifrar, no descifrada
  - strong negatives: descifrada/descifrado without 'no'/'sin' before it (read at the time), clave/clavo de cifra
    and similar key sheets, transcripción / descifre / descifración (a clear text exists), telegraphic material,
    items after 1900, fonds- or series-level rows (no signatura)
  + bonus: AGS Estado / Patronato Real / Guerra y Marina, AHN or AGI Estado, dates before 1830

Writes screen_ranked.tsv (score, id, signatura, first year, terms, images, title), best first. The score is a
reading order for a person, not a verdict.
"""
import csv, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = 'afe1562b3'

POS = [(r'\bparte en cifra\b', 4), (r'\bsin descifrar\b', 5), (r'\bno descifrad[ao]s?\b', 5),
       (r'\bcarta[s]? cifrada', 3), (r'\ben cifra\b', 3), (r'\bcontracifra', 2), (r'\bcifrad[ao]s?\b', 2),
       (r'\bcifras?\b', 1), (r'\bdescifrar\b', 1)]
NEG = [(r'(?<!no )(?<!sin )\bdescifrad[ao]s?\b', -4), (r'\bclav[eo]s? (de|para) (la )?cifra', -4),
       (r'\bclaves? para (cifrar|descifrar)', -4), (r'\bcifra con su clave', -3), (r'tel[eé]gra', -5),
       (r'\btabla para descifrar', -3)]
BONUS = [(r'^EST,', 3), (r'^PTR,', 2), (r'^GM,', 2), (r'^GYM,', 1), (r'^ESTADO,', 2), (r'^SANTA CRUZ', 1)]


def year(date):
    m = re.search(r'\b(1[0-9]{3})\b', date or '')
    return int(m.group(1)) if m else None


def screened_ids(base):
    ids = set()
    for c in json.load(open(os.path.join(HERE, 'candidates.json'), encoding='utf-8')):
        for link in c.get('links', []):
            ids.update(re.findall(r'description/(\d+)', link.get('href', '')))
    try:
        old = subprocess.run(['git', 'show', f'{base}:research/pares_ags/hits.jsonl'], cwd=HERE,
                             capture_output=True, text=True, encoding='utf-8', check=True).stdout
        ids.update(json.loads(l)['id'] for l in old.splitlines() if l.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f'warning: could not read hits.jsonl at {base}; only candidates.json ids dropped', file=sys.stderr)
    return ids


def score(r):
    t, sig, y = r['title'].lower(), r['sig'], year(r['date'])
    s = sum(w for p, w in POS if re.search(p, t)) + sum(w for p, w in NEG if re.search(p, t))
    s += sum(w for p, w in BONUS if re.search(p, sig))
    if sig == '?':
        s -= 8
    if y is not None and y > 1900:
        s -= 8
    elif y is not None and y < 1830:
        s += 2
    if r.get('images'):
        s += 1
    return s, y


def main(argv):
    base = argv[argv.index('--base') + 1] if '--base' in argv else BASE
    rows = {}
    for line in open(os.path.join(HERE, 'hits.jsonl'), encoding='utf-8'):
        r = json.loads(line)
        if r['id'] in rows:
            rows[r['id']]['terms'].add(r['term'])
        else:
            rows[r['id']] = dict(r, terms={r['term']})
    done = screened_ids(base)
    todo = [r for i, r in rows.items() if i not in done]
    out = []
    for r in todo:
        s, y = score(r)
        out.append((s, r['id'], r['sig'], y or '', '; '.join(sorted(r['terms'])), int(bool(r.get('images'))),
                    r['title']))
    out.sort(key=lambda x: (-x[0], x[3] or 9999, x[2]))
    with open(os.path.join(HERE, 'screen_ranked.tsv'), 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh, delimiter='\t', lineterminator='\n')
        w.writerow(['score', 'id', 'sig', 'year', 'terms', 'images', 'title'])
        w.writerows(out)
    print(f'{len(rows)} unique ids, {len(rows) - len(todo)} already screened, {len(todo)} ranked -> screen_ranked.tsv')


if __name__ == '__main__':
    main(sys.argv[1:])
