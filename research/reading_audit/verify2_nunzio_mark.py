"""Verification pass 2 (22 Oct 2026), nunzio1736: bracket the words of the Spagna 423 readings that the key decode does
not carry (found with verify2_nunzio_align.py, checked against the figures of texts/423-<n>_decode_b04.txt), and the
matching words of the English translations. Each edit is (file, old phrase, new phrase); whitespace in the old phrase
matches any run of whitespace; each old phrase must match exactly once.

    python research/reading_audit/verify2_nunzio_mark.py
"""
import pathlib
import re

T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'nunzio1736' / 'texts'

EDITS = [
    # 423/1 f. l. 106-109: "i st a n to e a l" = istanto e al: the ze of istanze is not carried (to written)
    ('423-1_reading.md', 'le\nistanze e al', 'le\n[?istanze] e al'),
    ('423-1_en.md', 'the demands', 'the [?demands]'),
    # 423/1 l. 399-400: "p o st o u i l {1646} r i m e di o": one i for postovi il (or l' only)
    ('423-1_reading.md', 'postovi il\n[1646]', 'postovi [?il]\n[1646]'),
    ('423-1_en.md', 'applied the [1646] remedy', 'applied [?the] [1646] remedy'),
    # 423/10 l. 225-226: "u e r i f a r e" = verifare: the ic of verificare is not carried
    ('423-10_reading.md', 'esaminare e verificare', 'esaminare e [?verificare]'),
    ('423-10_en.md', 'examining and verifying', 'examining and [?verifying]'),
    # 423/11 l. 278-283: "mi l l i o ne | e s c u s a d o": no figure for a separate e (and)
    ('423-11_reading.md', 'millione e escusado', 'millione [e] escusado'),
    ('423-11_en.md', 'millones and excusado', 'millones [and] excusado'),
    # 423/11: the figures give "impegnar il medesim": impegnar, not impegnare (replaced)
    ('423-11_reading.md', 'dovrebbe impegnare il', 'dovrebbe impegnar il'),
]


def main():
    for fn, old, new in EDITS:
        f = T / fn
        s = f.read_text(encoding='utf8')
        if new in s:
            print('already:', fn, new); continue
        pat = r'\s+'.join(re.escape(x) for x in old.split())
        ms = list(re.finditer(pat, s))
        assert len(ms) == 1, (fn, old, len(ms))
        m = ms[0]
        # keep the original line break where the phrase had one
        s = s[:m.start()] + new + s[m.end():]
        f.write_text(s, encoding='utf8', newline='')
        print(fn, '|', old.replace('\n', ' '), '->', new.replace('\n', ' '))


if __name__ == '__main__':
    main()
