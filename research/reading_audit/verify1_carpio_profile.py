"""verify1 (carpio1677): append the word-by-word verification count to each document's reading_review.note in
profile.json (targeted text edit, the rest of the file untouched).

    python research/reading_audit/verify1_carpio_profile.py
"""
import json
import pathlib

P = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'carpio1677' / 'profile.json'
COUNTS = {  # doc: (bracketed supplied, bracketed partly, replaced)
    'R1002': (2, 1, 1), 'R1003': (0, 0, 1), 'R1006': (0, 1, 0), 'R1007': (2, 2, 1),
    'R1008': (0, 1, 0), 'R1009': (0, 0, 0), 'R1010': (0, 0, 0), 'R1011': (4, 3, 0),
}
s = P.read_text(encoding='utf8')
for doc, (sup, part, rep) in COUNTS.items():
    i = s.index(f'"doc": "{doc}"')
    j = s.index('"reading_review"', i)
    k = s.index('"note": "', j) + len('"note": ')
    val, end = json.decoder.scanstring(s, k + 1)
    if 'verified word by word' in val:
        continue
    add = (f' Verified word by word 22 Oct 2026: {sup + part} words bracketed ({sup} supplied, {part} partly carried),'
           f' {rep} replaced.')
    s = s[:k] + json.dumps(val + add, ensure_ascii=False) + s[end:]
P.write_text(s, encoding='utf8', newline='')
print('done')
