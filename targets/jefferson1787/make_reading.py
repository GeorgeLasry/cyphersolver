"""Per-token reading of every transcribed Code No. 11 group, with grade and source; measures the share read.

Grades (README Conventions): H = TJ's own decoding over the group or his clear-text sheet; C = the group's value
is attested in another letter (key.tsv) and agrees; M = only the editors' printed reading, not checked by an
independent occurrence; I = conjecture (editors' brackets, or a value proposed here) with no independent support.
Unread: no value (blank). Illegible digits ('?') count as read only when the plaintext is fixed by TJ's clear sheet
or interlinear. Writes reading.tsv and prints counts per letter and overall. Also writes validation.tsv
(code TAB reading) for docs/_validate.py, from H and C tokens.
"""
import csv, glob, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
FRAC = re.compile(r'\s*[\[(](\d+)/(\d+)[\])]?\s*$')


def clean(c):
    return re.sub(r'[^0-9?]', '', c)


def main():
    key = {r['code']: r for r in csv.DictReader(open(os.path.join(HERE, 'key.tsv'), encoding='utf-8'),
                                                 delimiter='\t')}
    out, val = [], []
    tot = {}
    for path in sorted(glob.glob(os.path.join(HERE, 'transcription', '*.tsv'))):
        name = os.path.basename(path)[:-4]
        rows = [r for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t')
                if (r.get('code') or '').strip() not in ('', '=')]
        clear_sheet = name in ('tj_17870925', 'tj_17880603', 'tj_17910411')
        n = read = 0
        for r in rows:
            c = clean(r['code'])
            il = (r.get('interlinear') or '').strip()
            pl = FRAC.sub('', (r.get('plain') or '').strip())
            note = r.get('note') or ''
            unsure = '?' in c
            bracket = pl.startswith('[') or ']' in pl
            if il and not il.startswith('['):
                reading, grade = (pl or il), 'H'
            elif clear_sheet and pl and not pl.startswith('(quoted') and not pl.startswith('(not'):
                reading, grade = pl, 'H'
            elif pl and not pl.startswith('(not in') and not pl.startswith('(quoted') and pl != '(?)':
                k = key.get(c)
                if bracket:
                    grade = 'I'
                elif k and not unsure and any(l != name for l in k['letters'].split()):
                    grade = 'C'
                else:
                    grade = 'M'
                reading = pl
            else:
                reading, grade = '', ''
            if 'struck' in il.lower() or 'struck' in pl.lower():
                reading, grade = '', ''
            if pl.startswith('(cited') or pl.startswith('(quoted') or 'struck' in (il + pl + note).lower():
                out.append([name, r.get('image', ''), r.get('seq', ''), r['code'], 'excluded: quotation or struck', 'x'])
                continue
            n += 1
            if reading and not (unsure and grade not in ('H',)):
                read += 1
            out.append([name, r.get('image', ''), r.get('seq', ''), r['code'], reading, grade])
            if grade in ('H', 'C') and not unsure and reading and not reading.startswith('('):
                val.append((c, reading))
        tot[name] = (n, read)
    with open(os.path.join(HERE, 'reading.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['letter', 'image', 'seq', 'code', 'reading', 'grade'])
        w.writerows(out)
    with open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8', newline='') as f:
        for c, v in val:
            f.write(f'{c}\t{v}\n')
    N = sum(a for a, _ in tot.values()); R = sum(b for _, b in tot.values())
    for k, (a, b) in tot.items():
        print(f'{k:22s} {b:4d}/{a:<4d} {100*b/a:5.1f}%')
    print(f'{"all":22s} {R:4d}/{N:<4d} {100*R/N:5.1f}%')
    from collections import Counter
    print('grades:', dict(Counter(g for *_, g in out)))


if __name__ == '__main__':
    main()
