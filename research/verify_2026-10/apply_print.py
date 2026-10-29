"""Apply the printed-edition checks (p_english.json, p_french.json) and the Martinique key result to catalogue.json.
    python apply_print.py [--write]
printed_deciphered: the row is dropped from the open catalogue and listed in CLOSED.md.
partly_printed / printed_with_cipher / not_found: the finding is appended to status and prior_art; a printed crib is
noted in verify.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.join(ROOT, 'research', 'verify_2026-10')
cat_path = os.path.join(ROOT, 'catalogue.json')
cat = json.load(open(cat_path, encoding='utf-8'))
leads_path = os.path.join(ROOT, 'research', 'leads.json')
ld = json.load(open(leads_path, encoding='utf-8'))
by_id = {e['id']: e for e in cat['entries'] + ld['leads']}
F = []
for n in ('p_english.json', 'p_french.json'):
    F += json.load(open(os.path.join(HERE, n), encoding='utf-8'))

closed = []
for f in F:
    e = by_id.get(f['id'])
    if not e:
        print('missing', f['id'])
        continue
    fd = f['finding']
    cite = f.get('citation', '').strip()
    note = (f.get('note') or '').strip()
    if fd == 'printed_deciphered':
        closed.append((e['id'], e['title'], cite, note))
        continue
    label = {'partly_printed': 'Partly in print', 'printed_with_cipher': 'In print with the cipher figures (a crib)',
             'not_found': 'Not found in the printed edition checked', 'edition_unreachable': 'Edition not reachable'}[fd]
    e['status'] = (e.get('status', '') + ' Printed-edition check, 28 Oct 2026: ' + label + '. ' + cite + ' ' + note).strip()
    e['prior_art'] = (e.get('prior_art', '') + ' Printed edition: ' + label.lower() + ' (' + cite + ').').strip()

# Martinique (entries 1202, 1203): key source found in the same series
for i, txt in ((1202, 'Key status 28 Oct 2026 (targets/martinique1778): the sibling mercier1761 key does not fit (28 groups exceed its maximum, output nonsense); the Bouillé code is a larger third code. A contemporary interlinear decipherment sits on C8 A 78 f.123 (11 Oct 1779) and the same code runs through the 1778-79 letters; with it the key has 123 values and 68% of this letter is valued (read in part, a monthly troop return). Not at the read bar.'),
               (1203, 'Correction 28 Oct 2026: several letters in this run DO carry a contemporary interlinear decipherment (C8 A 78 ff. 3, 5, 31, 123, 144), and they supply the key for the whole 1778-82 Bouillé code (targets/martinique1778). Cipher-only letters in the run: C8 A 78 f.1 and image 0075, C8 A 79 ff. 19 and 70, C8 A 77 f.101 (an enclosure table), the ciphered part of C8 A 81 f.114.')):
    if i in by_id:
        by_id[i]['status'] = (by_id[i].get('status', '') + ' ' + txt).strip()
        by_id[i]['solvability'] = 4

print('to close', [c[0] for c in closed])
if '--write' in sys.argv:
    for path, d in ((cat_path, cat), (leads_path, ld)):
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(d, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
    import subprocess
    for i, t, c, n in closed:
        subprocess.run([sys.executable, os.path.join(ROOT, 'docs', '_check_catalogue.py'), '--close', str(i), 'read',
                        ('Printed deciphered: ' + c)[:300]], check=False)
    with open(os.path.join(HERE, 'CLOSED.md'), 'w', encoding='utf-8') as fh:
        fh.write('# Leads closed by the printed-edition check (28 Oct 2026)\n\nThese catalogue rows were removed: the letter is already printed deciphered.\n\n')
        for i, t, c, n in closed:
            fh.write('- **%s** %s. %s %s\n' % (i, t, c, n))
    print('written')
