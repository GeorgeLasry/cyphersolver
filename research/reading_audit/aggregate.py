"""Collect the reading audit (22 Oct 2026): the readers' grades (llm/out_*.jsonl, rubric llm/RUBRIC.md) joined with
the automatic sentence score (auto_scores.csv, docs/_check_reading.py --audit) and the profile's claim.

    python research/reading_audit/aggregate.py      writes audit.csv and prints the summary and the action lists
"""
import csv, glob, json, os, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent

auto = {r['folder']: r for r in csv.DictReader(open(HERE / 'auto_scores.csv', encoding='utf-8'))}
graded = {}
for f in sorted(glob.glob(str(HERE / 'llm' / 'out_*.jsonl'))):
    for line in open(f, encoding='utf-8'):
        line = line.strip()
        if not line: continue
        try: r = json.loads(line)
        except ValueError: continue
        if r.get('grade') in ('A', 'B', 'C', 'D', 'N'): graded[r['folder']] = r
cal = set(json.load(open(HERE / 'llm' / 'calibration.json'))['calibration_high'])


def claim(folder):
    p = ROOT / 'targets' / folder / 'profile.json'
    if not p.exists(): return {}
    o = json.load(open(p, encoding='utf-8')).get('outcome') or {}
    return dict(method=o.get('method'), cls=o.get('class'), frac=o.get('fraction_read'),
                provenance=o.get('provenance'), texts=len(o.get('texts') or []),
                translated=sum(bool(t.get('translation')) for t in o.get('texts') or []))


rows = []
for folder in sorted(set(auto) | set(graded)):
    a, g, c = auto.get(folder, {}), graded.get(folder, {}), claim(folder)
    grade = g.get('grade') or ('A?' if folder in auto and float(a.get('clean_share') or 0) >= 0.70 else '?')
    frac = c.get('frac')
    high = c.get('cls') == 'read' or (isinstance(frac, (int, float)) and frac >= 0.9)
    if grade in ('C', 'D'): action = 'relabel decoded-not-read / re-read' if grade == 'D' else 'mark weak documents; re-read'
    elif grade == 'B': action = 'normalise + translate'
    elif grade == 'N': action = 'check file list / mark not prose'
    else: action = 'translate' if not c.get('translated') else 'none'
    if 'excerpt' in (g.get('why') or '').lower() or g.get('fix') == 'check file list': action = 'add full texts (only an excerpt) / ' + action
    rows.append(dict(folder=folder, grade=grade, reviewed=folder in graded, calibration=folder in cal,
                     auto_clean=a.get('clean_share'), method=c.get('method'), cls=c.get('cls'), fraction_read=frac,
                     provenance=c.get('provenance'), mismatch=bool(high and grade in ('C', 'D')),
                     translated=f"{c.get('translated', 0)}/{c.get('texts', 0)}", action=action,
                     why=(g.get('why') or '')[:300], fix=g.get('fix') or ''))

with open(HERE / 'audit.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)

cnt = collections.Counter(r['grade'] for r in rows)
print('targets:', len(rows), dict(sorted(cnt.items())))
print('reviewed by a reader:', sum(r['reviewed'] for r in rows), ' calibration sample (auto >= 0.70):',
      collections.Counter(r['grade'] for r in rows if r['calibration']))
print('with any English translation:', sum(not r['translated'].startswith('0/') for r in rows))
for g in ('D', 'C'):
    sel = [r for r in rows if r['grade'] == g]
    print(f'\n{g} ({len(sel)}):')
    for r in sel:
        print(f"  {r['folder']:22} {str(r['cls']):13} frac={r['fraction_read']}  {'MISMATCH ' if r['mismatch'] else ''}{r['why'][:110]}")
