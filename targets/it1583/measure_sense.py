"""Measure how much of the two 1446 letters reads as sense, from George Lasry's CTTS edition (lasry2026/edition.json).

Assignment coverage (a value on the token) is not the read bar. Here a cipher token counts as read as sense only
when it sits in a word segment of the edition that is an Italian word in context. Segments containing '?' are
unread throughout (the assigned letters next to a '?' do not make a word). The NOISE list below marks the remaining
assigned segments that do not read: isolated letters at boundaries, the f. 70 signature block, and words the
edition itself leaves untranslated. Writes validation.tsv (token TAB value, '?' for unread) for docs/_validate.py.

    python targets/it1583/measure_sense.py
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ED = json.loads((HERE / 'lasry2026/edition.json').read_text(encoding='utf-8'))

# (document id, line, first token) of assigned segments that do not read as sense
NOISE = {
    'R7898': {(1, 50),            # 'o ?' after maino
              (4, 14), (4, 25),   # 'n' after siano; 'o' before the clear 'tocha'
              (8, 2),             # 'n o ? ? n l'
              (10, 1), (10, 15), (10, 16),   # '? n o'; 'n ?intita'
              (11, 27)},          # 'n ? ? ?'
    'f70': {(1, 1), (1, 2), (1, 20), (1, 29), (1, 33),   # n, o, a, l, 'mono'
            (3, 49),              # 'do' (untranslated)
            (4, 35),              # 'da' among unread signs
            (5, 18), (5, 19),     # the extra 'o o' in 'sarano o o spazate'
            } | {(8, t) for t in range(20, 44)},          # signature block after 'mai'
}

out = ['# model: it-cinquecento',
       '# source: lasry2026/edition.json (George Lasry CTTS edition, PR #60), token values as assigned; provisional l/n/in kept',
       '# note: f. 68 tokens first, then f. 70']
total = {}
for doc in ED['documents']:
    did = doc['id']; n = assigned = sense = 0
    for row in doc['rows']:
        boxes = row['boxes']
        for seg in row['segments']:
            if seg['kind'] == 'clear_box':
                continue
            a, b = seg['tokens']
            toks = [x for x in boxes[a - 1:b] if x['label'] != '[Plaintext]']
            noisy = '?' in seg['text'] or (row['line'], a) in NOISE[did]
            for x in toks:
                n += 1
                v = x['value']
                if v != '?':
                    assigned += 1
                    if not noisy:
                        sense += 1
                out.append(f"{x['label']}\t{v.upper() if v != '?' else '?'}")
    total[did] = (n, assigned, sense)
    print(f'{did}: {n} cipher tokens, {assigned} assigned ({assigned/n:.1%}), {sense} read as sense ({sense/n:.1%})')
N = sum(t[0] for t in total.values()); A = sum(t[1] for t in total.values()); S = sum(t[2] for t in total.values())
print(f'both: {N} cipher tokens, {A} assigned ({A/N:.1%}), {S} read as sense ({S/N:.1%})')
(HERE / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
