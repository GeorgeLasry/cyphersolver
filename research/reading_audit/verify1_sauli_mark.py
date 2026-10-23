"""verify1 (sauli1579): the word-by-word check of 22 Oct 2026, applied. Each edit: (file, old, new), matched once.
Sources: the interlinear decipherments (DECODE page images) and the key decode; see the hand-back for the reasons.
    python research/reading_audit/verify1_sauli_mark.py"""
import pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'sauli1579' / 'texts'
EDITS = [
    # R192 f. 197r: gloss "guerra" struck by the decipherer; group 40 = cattolici elsewhere: partly carried
    ('R192_reading.md', '{in una guerra}', '{in una [?guerra]}'),
    ('R192_en.md', 'in this {war}', 'in this {[?war]}'),
    # R192 f. 197v: no 84 (per) between quasi and porti; gloss "quasi por / porti per Inghilt.a": partly carried
    ('R192_reading.md', '{quasi per porti per', '{quasi [?per] porti per'),
    ('R192_en.md', '{almost as ports for England}', '{almost [?as] ports for England}'),
    # R192 f. 195v: gloss "tali", figures 37 00 75 05 (t a l i): replaced
    ('R192_reading.md', 'revocata tale\n', 'revocata tali\n'),
    ('R192_en.md', 'that promise was revoked', 'such a promise was revoked'),
    # R194 f. 281v: gloss "la Relig.ne Cat.ca in Fiandra", figures 75 01 (l a): replaced
    ('R194_reading.md', '{per mantenimento della religione', '{per mantenimento la religione'),
]
for f, old, new in EDITS:
    p = T / f
    s = p.read_text(encoding='utf8')
    assert s.count(old) == 1, (f, old, s.count(old))
    p.write_text(s.replace(old, new), encoding='utf8', newline='')
    print('ok', f, new)
