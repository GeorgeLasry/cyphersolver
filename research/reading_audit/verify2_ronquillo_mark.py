"""verify2 (ronquillo1676): apply the word-by-word verification edits (22 Oct 2026) to read/R*_reading.md and the
matching read/R*_en.md. Each edit is (file, old phrase, new phrase); whitespace in the phrase matches any run of
whitespace (line breaks kept); each old phrase must match exactly once. [w] = supplied (neither the margin
decipherment nor the key decode carries it), [?w] = partly carried.

Found with verify2_ronquillo_align.py (reading aligned with the key decode of the corrected transcription and with
DECODE's margin transcription) and checked by hand against the groups (keyx.py values) and, where DECODE's margin
transcription was unclear, the margin on the image.

    python research/reading_audit/verify2_ronquillo_mark.py
"""
import pathlib
import re

R = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'ronquillo1676' / 'read'

EDITS = [
    # R971 = R972 (one letter, identical images). 5039 margin (image): "solicitando siempre / las ordenes de su /
    # servicio"; figures 182=siempre 55=la 28=s fon=ord-: no "de V.S."
    ('R971_reading.md', 'solicitando siempre de V.S. las órdenes', 'solicitando siempre [de] [V.S.] las órdenes'),
    ('R972_reading.md', 'solicitando siempre de V.S. las órdenes', 'solicitando siempre [de] [V.S.] las órdenes'),
    ('R971_en.md', "always seeking Your Lordship's orders", "always seeking [Your Lordship's] orders"),
    ('R972_en.md', "always seeking Your Lordship's orders", "always seeking [Your Lordship's] orders"),
    # R979 5072: figures "animosidades de dell-s es" (q+=de), DECODE margin "animo**dades es della es": no "que"
    ('R979_reading.md', 'animosidades que della es probable', 'animosidades [?que] della es probable'),
    # R979 5075: figures "comunicaron n daneses" (20=n, one digit from 21=a), margin "le comunicaron / Daneses"
    ('R979_reading.md', 'comunicaron a daneses', 'comunicaron [?a] daneses'),
    ('R979_en.md', 'communicated it to the Danes', 'communicated it [?to] the Danes'),
    # R982 (no margin) 5094: figures "despues t la perdida" (4=t)
    ('R982_reading.md', 'después de la pérdida', 'después [?de] la pérdida'),
    # R984 (no margin) 5107: figures "se ha ll a que pretestando": a-qu shared with "que", no i
    ('R984_reading.md', 'se halla aquí, que', 'se halla [?aquí], que'),
    ('R984_en.md', 'has been here more', 'has been [?here] more'),
]


def main():
    n = 0
    for fn, old, new in EDITS:
        f = R / fn
        s = f.read_text(encoding='utf8')
        pat = r'\s+'.join(re.escape(x) for x in old.split())
        ms = list(re.finditer(pat, s))
        if not ms:
            newpat = r'\s+'.join(re.escape(x) for x in new.split())
            print('already applied' if re.search(newpat, s) else 'NOT FOUND', fn, old)
            continue
        assert len(ms) == 1, (fn, old, len(ms))
        m = ms[0]
        seps = re.findall(r'\s+', m.group(0))
        toks = new.split()
        out = toks[0]
        for k, t in enumerate(toks[1:]):
            out += (seps[k] if k < len(seps) else ' ') + t
        s = s[:m.start()] + out + s[m.end():]
        f.write_text(s, encoding='utf8', newline='')
        n += 1
        print(fn, ':', old, '->', new)
    print(n, 'edits')


if __name__ == '__main__':
    main()
