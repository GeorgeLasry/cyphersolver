"""verify2 (nevers1574): replace the words of f15_reading.md (and f15_en.md) that the sources give otherwise, found
with verify2_nevers_align.py and checked against f15_signs.tsv and f15_gloss.md by hand.

f. 15v l. 16 opens `+F9+F (9886..74 4F9 9F87202FT 38T9 FʒF +1 b74` = mesme pou[..]oit tes-moigner lors elle m'a dict;
the gloss of ll. 15-16 has "mesme [?] [?pouvoit] ... tesmoign[er] [?] lors elle m'a dict". The reading had
"desquoy elle m'a dict […] tesmoigner", a doublet of the "lors elle m'a dict" that follows: the source words are
"mesme" (signs and gloss) and "pouvoit" (partly: p o u o . . i t, gloss doubtful).

    python research/reading_audit/verify2_nevers_mark.py
"""
import pathlib

T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'nevers1574'
REPLACE = [
    ('f15_reading.md', "c'estoit chose desquoy elle m'a dict […] tesmoigner ;",
     "c'estoit chose desquoy mesme [?pouvoit] tesmoigner ;"),
    ('f15_en.md', 'it was a thing about which she told me [...] to bear witness;',
     'it was a thing about which [one] himself [?could] bear witness;'),
]
for fn, old, new in REPLACE:
    f = T / fn
    s = f.read_text(encoding='utf8')
    if new in s:
        print('already', fn); continue
    assert s.count(old) == 1, (fn, old)
    f.write_text(s.replace(old, new), encoding='utf8', newline='')
    print(fn, 'ok')
