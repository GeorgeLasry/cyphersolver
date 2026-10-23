"""v3 verify (a), lebel1593 no. 62: running reading from reading62_final.md (f. 130r body and f. 130v first paragraph)
without the [code value, grade] notation the scorer misreads. A code graded H or C (glossed, or confirmed by siblings)
is written {value}; graded M (inferred), forced, open, or with alternatives (a/b) it is [?value] or [?]; an ungraded
repeat takes the grade of the code's graded occurrence. Italics marks dropped; [n null] dropped; other brackets kept.

    python research/reading_audit/v3a_lebel.py
"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets/lebel1593'
L = (T / 'reading62_final.md').read_text(encoding='utf8').splitlines()
i0 = L.index('## Full text, f. 130r') + 1
i1 = next(i for i in range(i0, len(L)) if L[i].startswith('Settled at native'))
j0 = next(i for i in range(len(L)) if L[i].startswith('## Full text, f. 130v')) + 1
j1 = next(i for i in range(j0 + 1, len(L)) if L[i].startswith('- Line 1'))
text = ' '.join(l.strip() for l in L[i0:i1] + ['¶'] + L[j0:j1] if l.strip())
grade = {}
for m in re.finditer(r'\[(\d+\S*) ([^\]]*?), (H|C|M|open)', text):
    grade.setdefault(m.group(1), m.group(3))


def code(m):
    num, rest = m.group(1), m.group(2).strip()
    if rest.endswith('null'):
        return ''
    parts = [p.strip() for p in rest.split(',')]
    val, g = parts[0], (parts[1].split()[0] if len(parts) > 1 else grade.get(num, 'M'))
    if val in ('open', '?') or g == 'open' or not val:
        return '[?]'
    sure = g in ('H', 'C') and '/' not in val and '?' not in val and 'forced' not in rest
    return '{' + val + '}' if sure else '[?' + val.split('/')[0].rstrip('?') + ']'


text = re.sub(r'\[(\d+\+?|ⅅX) ?([^\]]*)\]', code, text)
text = re.sub(r'\[blot:[^\]]*\]', '[?]', text)
text = text.replace('*', '').replace(' | ', ' ').replace('¶', '\n\n')
text = re.sub(r'  +', ' ', text)
head = """# Lebel to the Duke of Savoy, Paris, 10 March 1593 (BnF fr. 3983 f. 130r-v, no. 62): reading in running text

Rests on: `reading62_final.md` (pass 3; letter signs read with the key, code values from codes_harvest.tsv graded
H glossed at the time, C confirmed by sibling contexts, M inferred from sense). Written out for the v3 verification
(23 Oct 2026) without its [code value, grade] notation, which the scorer misreads: H and C codes as {value}; M,
forced, alternative or open codes as [?value] or [?]; clear and deciphered text alike in roman. f. 130v (after the
paragraph break) is read only in its first lines; the rest of that page is under recto ink.

## Reading

"""
(T / 'no62_reading.md').write_text(head + text.strip() + '\n', encoding='utf8')
print(text)
