# Re-reading log, R56 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R56_decryption.txt` (DECODE D1720 under Meister no. 40; transcriber's
note: 522v line 24 damaged) gave the gist (the monitory, Lyon, La Guiche, Mayenne) with garbles in most lines;
`_check_reading.py` 0.616.

## 1. Is there a text already?

- Clear heading on 522r as transcribed by DECODE: "Molins a li XV? di Giugno 1589" (day uncertain).
- DECODE "cleartext" image D1082: the address leaf of the covering letter; no decipherment, no glosses.
- Rome's decipherments (Francia 27) are not imaged; Tempesti tells the monitory and the legate's recall in outline only.

## 2. Hand re-parsing (R56_corrections.tsv)

About one word in eight re-parsed, nearly all carried by the figures: "in questa mia conualescenza", "di 29 del pasato",
"segue che non solo io con mia infinita molestia", "deba ragioneuolm. dubitare di qualche stratagema et fraude",
torbidarmi, sconsolatisimo, "io pensauo di ritirarmi a Lione", "afiso in San Pietro", "la partita di corte del sig.
cardinale di Gioiosa et del ambasciatore di Francia", "io poteuo sicuram. andare", cortesem., m'hauriano, "io corerò",
"non perché io tema la morte", "cora questo pericolo", "ali 15 del presente", Langres, "mons. dela Guicha",
"o uere o false", "soto l'obedientia", "un thesoriere", "oto in dieci leghe", "la Granche le …", Mirabelo,
"andarsi a congiungersi", parcam., "si dice, sarei sicuro".
- Separators "8 0 8" (three times) and "8 1 0 8" between sentences, as in R55 ("8 9 8", "8 0 8"): a feature of the
  Moulins letters; they carry no word.
- No image check was needed.

## 3. Alignment (reread_b00_align.py)

`TOTAL R56: 832 words, 0 supplied, 3 partly` (after respelling ritrouo and "quella hora" as the figures give them).
523r: 766 of 783 figures used (the unparsed last line).

## Result

Before: 0.616. After: 0.803 on the "## Reading" body (830 words). By hand: 5 unread stretches, 5 partly carried words and
2 supplied letters/words in about 830 words. Grade A: the sentences hold throughout.

## Still open, and why

- The opening (522r l. 3), "afligere […] più che" (522r l. 4), "[…] dicono" (522v l. 13), the castle's name ending
  (522v l. 32), and the closing line (523r l. 12). Not checked on the image (no outside blocker); Francia 27 would settle
  them.
