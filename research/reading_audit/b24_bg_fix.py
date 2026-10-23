"""b24 (bergamo1585): apply the label corrections read on the R16 images (DECODE IMG_R16_I95/I96) to TimB's transcription
D1610 -> targets/bergamo1585/R16_transcription_corrected.txt, and write R16_corrections.tsv. Lines are numbered as in
b24_bg_decode.py (non-# lines; L03-L35 = f. 206r, L37-L60 = f. 206v)."""
import pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'bergamo1585'
C = [  # line, old, new, kind, evidence
 (2, '3. di Marzo 1586', '7. di Marzo 1586', 'clear', 'heading on 206r reads "7. di Marzo. 1586."; the covering letter (DECODE D987) is dated Parigi 7 March 1586, "con cifra duplicata"'),
 (4, '1 3 0 3 3 1? 2 5 0 7', '1 3 0 3 3 7 2 5 0 7', 'label', 'image 13 03 37 25 07 "fermo" (DECODE 1? for 7)'),
 (6, '0 3 3 5 3 1 0 3 3 1 4 3', '0 3 3 5 3 1 0 3 3 7 4 3', 'label', 'image 37 "uendere" (DECODE 31, giving "uendede")'),
 (8, '1 7 0 1? 3 5', '1 7 0 7 3 5', 'label', 'image 17 07 35 "rispondere"'),
 (17, '8 9? 1 1 7', '8 4 1 1 7', 'label', 'image a crossed 4: 41 17 37 03 47 07 "apreso"'),
 (34, '4 7 0 4 8 0 3 4 7 6 7', '4 7 0 7 8 0 3 4 7 6 7', 'label', 'image 47 07 8 "uerso" (DECODE 4 for 7; the old decode read 48 Duca di Parma)'),
 (34, '8 0 7 2 5 3 3 5 0 5 8', '8 0 7 2 3 3 5 0 5 8', 'label', 'image 07 23 35 05 "ogni"; DECODE\'s 5 is an ink blot'),
 (40, '4 7 0 5 9? 5 8 3 6¸', '4 7 0 5 4 3 8 3 6¸', 'look-alike', 'image 47 05 4? 8: the second digit of the pair read 3 (43 = e) for "si e per partirsi"; it can be read 5 (45 = i)'),
 (42, '4 7 0^. 5 4 7', '4 7 0 5 4 7', 'label', 'image 37 03 47 05 47 57 03 37 03 "resistere" (no dot over the 0)'),
 (43, '3 1 6¸? 8', '3 1 6 7 8', 'look-alike', 'image 31 67 "ocorendo": the 7 has the hooked tail DECODE read as 6¸'),
 (44, '1 5 0 1 8 0 2 3 3 7', '1 5 0 1 8 0^. 2 3 3 7', 'label', 'image dotted 0 "con" before 23 37 03 23 "greg." (as at l.52)'),
 (46, '0 7 7? 5 5 7', '0 7 1 5 5 7', 'label', 'image 25 07 15 57 07 "molto"'),
 (47, '8 1 8 0 1 1 5 0 3', '8 1 5 0 1 1 5 0 3', 'look-alike', 'image "1 8|5": the 5 closed like an 8; 15 01 15 03 03 ... "l\'aleenatione"'),
 (50, '1 3 0 1 8 7 4 1 8', '1 3 0 1 5 7 4 1 8', 'look-alike', 'image "13 01 87 41": the 5 closed like an 8; 57 41 "fata"'),
 (55, '0 3 3 1 6¸? 8', '0 3 3 1 6 7 8', 'look-alike', 'image 03 31 67 "(u)edo": the hooked 7 again, as at l.43'),
 (54, '5 7 0 3 3? 5 5 7 0 1', '5 7 0 3 3 5 5 7 0 1', 'label', 'image 57 03 35 57 01 "tenta" (the 3 is sure)'),
]
lines = (T / 'R16_transcription_decode.txt').read_text(encoding='utf8').split('\n')
idx = [i for i, l in enumerate(lines) if not l.startswith('#')]
for ln, old, new, kind, ev in C:
    i = idx[ln - 1]
    assert old in lines[i], (ln, old, lines[i])
    lines[i] = lines[i].replace(old, new, 1)
hdr = '# b24 (23 Oct 2026): TimB\'s D1610 with the corrections of R16_corrections.tsv read on the DECODE images\n'
(T / 'R16_transcription_corrected.txt').write_text(hdr + '\n'.join(lines), encoding='utf8')
with open(T / 'R16_corrections.tsv', 'w', encoding='utf8') as f:
    f.write('line\tdecode_label\tcorrected\tkind\tevidence\n')
    for ln, old, new, kind, ev in C:
        f.write(f'L{ln:02d}\t{old}\t{new}\t{kind}\t{ev}\n')
print(len(C), 'corrections')
