"""v7 list 1: write lebel1593 no. 11 and no. 100 readings in running text from reading<n>_final.md, as no62_reading.md
was written (v3): [n value] (H/C) -> {value}; [n value M] or [n value?] -> [?value]; italics marks dropped.
    python research/reading_audit/t7_1_lebel.py"""
import re, pathlib
D = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'lebel1593'
HEAD = """# Lebel to the Duke of Savoy, Paris, {date} (BnF fr. 3983 {ff}, no. {n}): reading in running text

Rests on: `reading{n}_final.md` (pass 3; letter signs read with the key, code values from codes_harvest.tsv graded
H glossed at the time, C confirmed by sibling contexts, M inferred from sense). Written out 23 Oct 2026 (translation
wave v7) in the manner of `no62_reading.md`, without its [code value, grade] notation: H and C codes as {{value}}; M or
queried codes as [?value]; open groups as [?]; clear and deciphered text alike in roman (italics dropped); `…` and
`(?)` as in the source. Spelling as written.

## Reading

"""
def conv(t):
    t = t.replace('*', '')
    def rep(m):
        inner = m.group(1).strip()
        mm = re.match(r'^(?:XC|\d+(?:\(\d+\??\))?)\s+(.*)$', inner, re.S)
        if mm: mm = re.match(r'^(.*)$', ' '.join(mm.group(1).split()))
        if not mm: return m.group(0)
        val = mm.group(1).strip()
        if val.endswith(' M'): return '[?' + val[:-2].strip() + ']'
        if '?' in val: return '[?' + val.replace('?', '').strip() + ']'
        return '{' + val + '}'
    return re.sub(r'\[([^\[\]]+)\]', rep, t)
for n, date, ff in [('11', '17 January 1593', 'f. 26r-v'), ('100', '27 March 1593', 'ff. 194r-195r')]:
    src = (D / f'reading{n}_final.md').read_text(encoding='utf8')
    body = re.search(r'^## Text\n(.*?)(?=^## )', src, re.S | re.M).group(1).strip()
    (D / f'no{n}_reading.md').write_text(HEAD.format(n=n, date=date, ff=ff) + conv(body) + '\n', encoding='utf8')
    print('wrote', n)
