"""v3 verify (a), ancel1577: write texts/<doc>_reading.md from the reading column of contributed/READING.en.md.

    python research/reading_audit/v3a_ancel_write.py

Rules (header of each file repeats them): hyphenated line ends joined; the contributor's marks dropped; the plain-letter
groups OPEN.en.md section 3 lists as nulls (fec, sec, sanc, sane, pome, estre, toe, vib, roc, ar, puis, x) dropped;
code words whose meaning a contemporary margin decipherment confirms written {code: meaning} (saturnus, Juno, my, my3,
my3θ); other code words stay [code] (a hole); the contributor's parenthesised letters, i.e. supplied or conjectured,
become brackets ([?est], ce[s disc]ours), so they count as holes; editorial remarks in parentheses dropped.
"""
import pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).parent))

NULLS = r'fec|fec\?|sec|sanc|sane|pome|estre|toe|vib|roc|ar|puis|x'
CODES = {'saturnus': "l'Empereur", 'Juno': "le Roy d'Espagne", 'my': "qu'il", 'my3': "qu'il", 'my3θ': "qu'ilz",
         'my3z': "qu'ilz"}
s = (ROOT / 'targets/ancel1577/contributed/READING.en.md').read_text(encoding='utf8')
parts = re.split(r'^## ', s, flags=re.M)


def column(start):
    sec = [p for p in parts if p.startswith(start)][0]
    out = ''
    for l in sec.splitlines():
        if not l.startswith('|') or l.startswith('| line') or l.startswith('|---'):
            continue
        r = [x.strip() for x in l.strip('|').split('|')][2]
        if out.endswith('-'):
            out = out[:-1] + (r[1:] if r.startswith('-') else r)
        else:
            out += ' ' + (r[1:] if r.startswith('-') else r)
    return out.strip()


def clean(t):
    t = re.sub(r'\((?:Admira[^)]*|end of[^)]*)\)', '', t)
    t = re.sub(r'\[(?:%s)\]' % NULLS, '', t)
    t = re.sub(r'\[(\w+)\](z?)', lambda m: '{%s: %s}' % (m.group(1) + m.group(2), CODES[m.group(1) + m.group(2)])
               if m.group(1) + m.group(2) in CODES else m.group(0), t)
    t = re.sub(r'\(([^()]*)\?\)', r'[?\1]', t)            # (est?) -> [?est]
    t = re.sub(r'\(([^()]*)\)', r'[\1]', t)                # (re)verence -> [re]verence
    t = re.sub(r'  +', ' ', t).replace(' ,', ',').replace(' .', '.')
    return t


DOCS = [('p525-526', 'p.525', '22 October 1577, pp. 524 end-526'), ('p539', 'p.539', '2 November 1577, p. 539'),
        ('p561-563', 'p.561', '14 December 1577, pp. 561-563'), ('p565', 'p.565', '21 December 1577, p. 565')]
HEAD = """# Ancel, letter of {label}: reading

Rests on: the contributed reading (`contributed/READING.en.md`, reading column; transcription and key output in
`contributed/transcription/` and `contributed/decoded/`), which applies Tomokiyo's key for BnF Cinq Cents de Colbert
398 to an image-adjudicated transcription. This file only puts the reading column into running text for the v3
verification (23 Oct 2026): hyphenated line ends joined; the contributor's marks dropped; plain-letter groups that
`contributed/OPEN.en.md` section 3 lists as nulls dropped; code words whose meaning a contemporary margin decipherment
on the calibration pages confirms written {{code: meaning}} (saturnus = l'Empereur, Juno = le Roy d'Espagne, my/my3 =
qu'il, my3θ = qu'ilz); other code words stay [code]; letters the contributor supplied in parentheses are bracketed
([?word], part[ial]) so they count as holes; "…" is an unreadable stretch. Spelling as the contributor gives it.

## Reading

"""
for doc, start, label in DOCS:
    body = clean(column(start))
    f = ROOT / 'targets/ancel1577/texts' / f'{doc}_reading.md'
    f.parent.mkdir(exist_ok=True)
    f.write_text(HEAD.format(label=label) + body + '\n', encoding='utf8')
    print(f.name, len(body.split()))
