"""Cross-check every sweep candidate against the repo as it now stands (catalogue, ledgers, targets, older sweeps).

    python research/archive_sweep_2026-10/crosscheck.py > research/archive_sweep_2026-10/crosscheck.txt

For each candidate, searches its shelfmark's distinctive tokens (those with a digit) and the correspondents' surnames,
skipping the Oct 2026 sweep folders themselves. Prints only candidates with a hit, for review by hand.
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from merge import SWEEPS  # noqa: E402

SKIP = {os.path.join('research', s) for s in SWEEPS} | {os.path.join('research', 'archive_sweep_2026-10')}
FILES = ['catalogue.json', 'CATALOGUE.md', 'SOLVED_CATALOGUE.md', 'SOLVED_RANKING.md', 'README.md']
GLOBS = ['targets/*/NOTES.md', 'research/*/*.md', 'research/*/*/*.md', 'research/*/hits.json']
STOP = {'unknown', 'king', 'queen', 'duke', 'count', 'emperor', 'prince', 'marquis', 'general', 'letters', 'ambassador',
        'minister', 'envoy', 'from', 'with', 'the', 'and', 'des', 'del', 'van', 'von', 'der', 'den', 'les', 'his', 'her',
        'secretary', 'cardinal', 'conde', 'marquês', 'comte', 'baron', 'lord', 'states', 'general', 'abbé', 'family',
        'various', 'others', 'several', 'royal', 'chancery', 'french', 'spanish', 'swedish', 'danish', 'imperial'}


def corpus():
    paths = [os.path.join(ROOT, f) for f in FILES]
    for g in GLOBS:
        paths += glob.glob(os.path.join(ROOT, g))
    for p in sorted(set(paths)):
        rel = os.path.relpath(p, ROOT)
        if any(rel.startswith(s + os.sep) for s in SKIP) or not os.path.exists(p):
            continue
        yield rel, open(p, encoding='utf-8', errors='replace').read()


def terms(r):
    t = set()
    for tok in re.split(r'[\s,;()]+', r['shelfmark']):
        tok = tok.strip('.:')
        if re.search(r'\d', tok) and len(tok) >= 4 and not re.fullmatch(r'1[3-9]\d\d(-\d+)?', tok):
            t.add(tok)
    for name in re.findall(r"[A-ZÀ-Þ][\wà-ÿ'-]{3,}", r['correspondents']):
        if name.lower() not in STOP:
            t.add(name)
    return t


def main():
    C = list(corpus())
    for s in SWEEPS:
        p = os.path.join(ROOT, 'research', s, 'candidates.json')
        if not os.path.exists(p):
            continue
        for i, r in enumerate(json.load(open(p, encoding='utf-8'))):
            hits = []
            for t in sorted(terms(r)):
                rx = re.compile(r'(?<![\w/])' + re.escape(t) + r'(?![\w])')
                files = [n for n, txt in C if rx.search(txt)]
                if files and len(files) <= 6:  # a term found all over the repo is a common name, not a match
                    hits.append(f'{t}: {", ".join(files[:5])}{" …" if len(files) > 5 else ""}')
            if hits:
                print(f'{s}[{i}] {r["year"]} {r["title"][:90]}')
                for h in hits: print('    ' + h)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
