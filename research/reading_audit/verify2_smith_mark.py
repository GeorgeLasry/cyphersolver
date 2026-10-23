"""verify2 (smith1562): apply the word-by-word verification edits (22 Oct 2026) to no<NN>_reading.md and the matching
no<NN>_en.md. Each edit is (file, old phrase, new phrase); whitespace in the old phrase matches any run of whitespace;
each old phrase must match exactly once (or the new phrase is already there).

Grade-A readings (nos. 01, 03, 04, 05, 19, 20) were aligned with Forbes's print (verify2_smith_align.py): every word is
carried by the print (the listed words were OCR garbles, checked against the second OCR in
targets/throckmorton/sources/forbes2.txt). Grade-B readings (nos. 06, 08, 09, 11, 13, 15-18, 22) were checked passage
by passage against the glyph strings (decipher_A/D.md, no01-no23_corrections.tsv, the re-read log) and, where those
left a word unsettled, on crops of the DECODE images (R9236, R9250 p. 1, R9252 p. 2, R9254 p. 1) with the key sheet
R9261 p. 1.

    python research/reading_audit/verify2_smith_mark.py
"""
import pathlib
import re

T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'smith1562'

EDITS = [
    # no. 08 (7): ":L .o ⊢̈5:5.6⊓8:" = Lord of Murray, no sign for "the" (passage 18 has T :L .o)
    ('no08_reading.md', 'The Lord of Murray; such lords', '[The] Lord of Murray; such lords'),
    ('no08_en.md', 'The Lord of Murray (James Stewart', '[The] Lord of Murray (James Stewart'),
    # no. 08 (10): last group .T ξπ9:L = that w-i-s/y-e: "wise", not "way" (the calendar's word)
    ('no08_reading.md', 'great enterprise that way.', 'great enterprise that wise.'),
    # no. 08 (14): the first sign (a c-like sign with a bar) is not on the key sheet; "The Earl of" rests on context
    ('no08_reading.md', 'The Earl of Huntly died', '[?The Earl of] Huntly died'),
    ('no08_en.md', 'The Earl of Huntly died', '[?The Earl of] Huntly died'),
    # no. 11 (4): ! 凸 .A ⩓ = in England and Scotland (! = in; "into" is ! T̈ in no. 04)
    ('no11_reading.md', 'Into England and Scotland.', 'In England and Scotland.'),
    ('no11_en.md', 'Into England and Scotland.', 'In England and Scotland.'),
    # no. 15 (6): A: ·T ɛ̣ = all that [ɛ̣] (·T = that, as in no. 17 (5) "! ·T" in that)
    ('no15_reading.md', 'All the […]; in the marriage', 'All that […]; in the marriage'),
    ('no15_en.md', 'All the […] (of Guise)', 'All that […] (house of Guise)'),
    # no. 16 (7): ":F" alone = French (key), no sign for "the"
    ('no16_reading.md', 'the Emperor; the French; the Queen', 'the Emperor; [the] French; the Queen'),
    ('no16_en.md', 'Charles of Austria); the French;', 'Charles of Austria); [the] French;'),
    # no. 22 l. 4: .o T. 9.⊓⊢L m. = of the same matter (T. = the; .T = that); the calendar has "the same matter"
    ('no22_reading.md', 'I wrote of that same matter', 'I wrote of the same matter'),
]


def main():
    for fn, old, new in EDITS:
        f = T / fn
        s = f.read_text(encoding='utf8')
        pat = r'\s+'.join(re.escape(x) for x in old.split())
        ms = list(re.finditer(pat, s))
        if not ms:
            print('already applied or not found:', fn, old, '| new present:', new.split()[0] in s)
            continue
        assert len(ms) == 1, (fn, old, len(ms))
        s = s[:ms[0].start()] + new + s[ms[0].end():]
        f.write_text(s, encoding='utf8', newline='')
        print(fn, ':', old, '->', new)


if __name__ == '__main__':
    main()
