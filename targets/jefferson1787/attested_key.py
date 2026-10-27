"""Attested key for Code No. 11 and a per-letter check of the printed readings.

A value counts as attested when it comes from outside the editors' reconstruction:
  T  TJ's interlinear decoding over that one group (RCs of Barclay and Carmichael),
  S  TJ's clear-text sheet, where the word sits on one group (no [k/n] split),
  P  a pair printed in the Founders notes (TJ's or Carmichael's own statement).
The editors' aligned readings of TJ-written letters without a clear sheet are not evidence.

Writes key.tsv (code, value, classes, count, conflicts) and coverage.tsv (per letter: groups, groups
with an attested value, groups whose only support is the reading of that letter itself).
"""
import csv, glob, os, re
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SPLIT = re.compile(r'[\[(]\d+/\d+[\])]?')

PRINTED = [('1077', 'never'), ('1097', ';'), ('1081', 'nar'), ('146', 'President'), ('1140', 'and'),
           ('329', 'now'), ('707', '4'), ('1555', 'yet'), ('959', '8'), ('1371', 'Tunis'),
           ('1611', 'Mr. Barclay'), ('140', 'Sweden'), ('317', 'ai')]


def clean(c):
    return re.sub(r'[^0-9?]', '', c)


def main():
    ev = defaultdict(list)       # code -> [(value, class, letter)]
    letters = {}
    for path in sorted(glob.glob(os.path.join(HERE, 'transcription', '*.tsv'))):
        name = os.path.basename(path)[:-4]
        rows = [r for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t')
                if (r.get('code') or '').strip() not in ('', '=')]
        letters[name] = rows
        for i, r in enumerate(rows):
            c = clean(r['code'])
            if '?' in c or not c:
                continue
            il = (r.get('interlinear') or '').strip()
            nxt = (rows[i + 1].get('interlinear') or '').strip() if i + 1 < len(rows) else 'END'
            if il and nxt and not il.endswith('?'):
                ev[c].append((il.lower(), 'T', name))
            pl = (r.get('plain') or '').strip()
            note = r.get('note') or ''
            if 'clear sheet' in note or (name.startswith('tj_') and 'aligned' not in note and pl):
                if pl and not SPLIT.search(pl) and '(' not in pl and name in ('tj_17870925', 'tj_17880603', 'tj_17910411'):
                    ev[c].append((pl.lower(), 'S', name))
    for c, v in PRINTED:
        ev[c].append((v.lower(), 'P', 'founders-notes'))

    key = {}
    with open(os.path.join(HERE, 'key.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['code', 'value', 'classes', 'n', 'other_readings', 'letters'])
        for c in sorted(ev, key=int):
            cnt = Counter(v for v, _, _ in ev[c])
            v, n = cnt.most_common(1)[0]
            key[c] = v
            w.writerow([c, v, ''.join(sorted({k for _, k, _ in ev[c]})), len(ev[c]),
                        ' | '.join(f'{x} x{y}' for x, y in cnt.most_common()[1:]),
                        ' '.join(sorted({l for _, _, l in ev[c]}))])

    with open(os.path.join(HERE, 'coverage.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['letter', 'groups', 'attested_here_or_elsewhere', 'attested_elsewhere', 'illegible'])
        for name, rows in letters.items():
            g = len(rows)
            ill = sum(1 for r in rows if '?' in r['code'])
            att = sum(1 for r in rows if clean(r['code']) in key)
            other = sum(1 for r in rows if clean(r['code']) in key and
                        any(l != name for _, _, l in ev[clean(r['code'])]))
            w.writerow([name, g, att, other, ill])
    print(len(key), 'attested values -> key.tsv; coverage.tsv written')


if __name__ == '__main__':
    main()
