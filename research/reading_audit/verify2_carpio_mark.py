"""verify2 (carpio1677): the margin decipherments transcribed from the images on 22 Oct 2026 (read/R10xx_margin.txt)
checked against the readings word by word; apply the changes the margins call for to read/R*_reading.md and the
matching read/R*_en.md. Each edit is (file, old phrase, new phrase); whitespace in the phrase matches any run of
whitespace; each old phrase must match exactly once. Brackets placed by verify1 are kept even where the margin now
carries the word (VERIFY_BRIEF.md: do not remove brackets).

    python research/reading_audit/verify2_carpio_mark.py
"""
import pathlib
import re

R = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'carpio1677' / 'read'

EDITS = [
    # R1007 foot of p. 1: margin "no haviendo passado / [?] a tomar resolucion por quedar esperando una"; key "is que da r"
    # (quedar): "quedo" is neither margin nor key
    ('R1007_reading.md', 'tomar resolución, quedo esperando una respuesta',
     'tomar resolución por quedar esperando una respuesta'),
    ('R1007_en.md', 'Not having gone so\nfar as to take a resolution, I am waiting for an answer',
     'I have not gone so\nfar as to take a resolution, as I am waiting for an answer'),
    # R1002 p. 2: margin "que habla-/se a Su Beatitud", key "que ha go la se": hablase, not hable (bracket kept)
    ('R1002_reading.md', 'que [?hable] a Su Beatitud', 'que [?hablase] a Su Beatitud'),
    # R1003 p. 2: margin "respuesta de pare-/cer", key "re s pu es ta de pa re ce r": de, not del
    ('R1003_reading.md', 'la respuesta del parecer que', 'la respuesta de parecer que'),
]


def main():
    for fn, old, new in EDITS:
        f = R / fn
        s = f.read_text(encoding='utf8')
        pat = r'\s+'.join(re.escape(w) for w in old.split())
        ms = list(re.finditer(pat, s))
        if not ms:
            print('already applied or not found:', fn, old[:40]); continue
        assert len(ms) == 1, (fn, old)
        m = ms[0]
        s = s[:m.start()] + new + s[m.end():]
        f.write_text(s, encoding='utf8', newline='')
        print(fn, '|', old[:50].replace('\n', ' '), '->', new[:50].replace('\n', ' '))


def headers():
    """Name the margin file in each reading's header comment."""
    for f in sorted(R.glob('R10*_reading.md')):
        doc = f.name.split('_')[0]
        if not (R / f'{doc}_margin.txt').exists():
            continue
        s = f.read_text(encoding='utf8')
        add = f' The margin transcription is saved as read/{doc}_margin.txt (22 Oct 2026).'
        if add in s:
            continue
        i = s.index('-->')
        f.write_text(s[:i].rstrip() + add + ' ' + s[i:], encoding='utf8', newline='')
        print('header', f.name)


if __name__ == '__main__':
    main()
    headers()
