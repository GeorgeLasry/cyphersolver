"""v3 verify (a), estrada1503: write PTR53-69_reading.md from reading_X.md lines 1-11 and 14-15 (the read part):
code=value tags reduced to the value, the upper-case letter runs written in lower case (a notation change only; names
capitalised), supplied letters in brackets kept lower case so they count as holes, ll. 12-13 marked unread.

    python research/reading_audit/v3a_estrada.py
"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets/estrada1503'
L = (T / 'reading_X.md').read_text(encoding='utf8').splitlines()
NAMES = {'ROSELLON': 'Rosellon', 'GUIPUZCOA': 'Guipuzcoa', 'LENGUADOQUE': 'Lenguadoque', 'TERRABIA': 'terrabia'}
lines = {}
for l in L:
    m = re.match(r'^(\d+)\.\s+(.*)$', l)
    if m and int(m.group(1)) not in lines:
        lines[int(m.group(1))] = m.group(2)


def conv(t):
    t = re.sub(r'\b\w+=(\S)', r'\1', t)
    t = re.sub(r'[A-ZÑ]{2,}|\b[YA]\b', lambda m: NAMES.get(m.group(0), m.group(0).lower()), t)
    t = re.sub(r'\[([^\]]*)\]', lambda m: '[' + m.group(1).lower() + ']', t)
    return t


body = ' '.join(conv(lines[n]) for n in range(1, 12)) + ' [... ll. 12-13 not read ...] ' + ' '.join(conv(lines[n]) for n in (14, 15)) + ' [...]'
body = body.replace('[fuen]terrabia', '[Fuen]terrabia').replace('ya sabeys', 'Ya sabeys')
head = """# Isabella to Estrada, Segovia 20 Aug 1503: copy X recto ll. 1-11 and 14-15, reading

Rests on: `reading_X.md` (copy X, collated with Y and Z; code groups from Galende's *Cifra general*, letter-sign runs
read on the PARES images). This file is the read part of it in running text, for the v3 verification (23 Oct 2026): the
code=value tags reduced to the value, the letter runs (upper case there) written in lower case, a notation change only;
letters supplied in brackets are holes; [..] a stretch not read; lines 12-13 are not read and marked. Spelling as
read.

## Reading

"""
(T / 'PTR53-69_reading.md').write_text(head + body + '\n', encoding='utf8')
print(body)
