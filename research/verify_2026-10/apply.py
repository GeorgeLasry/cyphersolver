"""Apply the verification results (a_*.json ... g_*.json) to catalogue.json.  python apply.py [--write]

open / partly_read / unreachable: prior_art replaced, status_update appended to status, `verify` set to the next step,
seen upgraded to image where the agent viewed one, scores updated where the agent gave them.
duplicate: the row is dropped and a one-line pointer is added to the entry it duplicates.
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
cat_path = os.path.join(ROOT, 'catalogue.json')
cat = json.load(open(cat_path, encoding='utf-8'))
leads_path = os.path.join(ROOT, 'research', 'leads.json')    # the sweep rows moved to leads on 28 Oct 2026
ld = json.load(open(leads_path, encoding='utf-8'))
by_id = {e['id']: e for e in cat['entries'] + ld['leads']}
V = []
for f in sorted(glob.glob(os.path.join(ROOT, 'research/verify_2026-10/[a-g]_*.json'))):
    V += json.load(open(f, encoding='utf-8'))

drop = set()
n = 0
for v in V:
    e = by_id.get(v['id'])
    if not e:
        print('missing', v['id'])
        continue
    if v['verdict'] == 'duplicate':
        m = re.search(r'catalogue (?:entry )?(\d+)', v.get('status_update', '') + ' ' + v.get('prior_art', ''))
        tgt = by_id.get(int(m.group(1))) if m else None
        if tgt:
            tgt['status'] = (tgt.get('status', '') + ' Also listed by the Oct 2026 Swiss/Austrian sweep as ' + str(v['id'])
                             + ' (same Fasc.; merged here).').strip()
            drop.add(v['id'])
        else:
            print('duplicate without target', v['id'])
        continue
    if v.get('prior_art'):
        e['prior_art'] = v['prior_art']
    if v.get('status_update'):
        e['status'] = (e.get('status', '') + ' Checked 28 Oct 2026: ' + v['status_update'].strip()).strip()
    if v.get('next_step'):
        e['verify'] = v['next_step']
    if v.get('seen') == 'image':
        e['seen'] = 'image'
    for k in ('importance', 'solvability', 'difficulty'):
        if isinstance(v.get(k), int):
            e[k] = v[k]
    if v['verdict'] == 'unreachable':
        e['status'] += ' (could not be verified: see prior_art)'
    n += 1
cat['entries'] = [e for e in cat['entries'] if e['id'] not in drop]
ld['leads'] = [e for e in ld['leads'] if e['id'] not in drop]
print('updated', n, 'dropped', sorted(drop))
if '--write' in sys.argv:
    with open(cat_path, 'w', encoding='utf-8') as fh:
        json.dump(cat, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    with open(leads_path, 'w', encoding='utf-8') as fh:
        json.dump(ld, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    print('written')
