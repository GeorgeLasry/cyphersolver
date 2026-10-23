# Re-reading log, R2122 and R2131 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b19)

## Starting point

Reading audit (22 Oct): both "decoded, not read". The block-alphabetical slot model (`../alpha/`) gave firm values to
40% of R2122's groups and 30% of R2131's; the running text was fragments (4 of 113 sentences clean).

## 1. Is there a text already?

- DECODE records R2122 and R2131 re-fetched with the project cookie (`research/reading_audit/b19_fetch.py`): images
  only (2 and 4), no DOC attachment, no transcription, no comment block; status "Non-decrypted". Every image opened:
  no interlinear, margin or slip decipherment. DECODE's note on R2131 says the same codebook served Kroll, Wasmuht,
  Schenck and Van Haeften.
- Sibling records with solutions (R1948-R1952 Kroll, R2132-R2134 Van Haeften/Wasmuht, R2141 Schenck) fetched and listed;
  not transcribed, because the next find made them unnecessary as cribs.
- **The codebook itself.** The legation inventory (`targets/roell1809/turk_inv.txt`) lists under Kroll (chargé
  1784-85, before Van Dedem's arrival) inv. 785 "Sleutel geheimschrift. z.d." It is scanned on the Nationaal Archief
  site (6 scans; `research/reading_audit/b19_na_fetch.py`, scratchpad only): a bound codebook headed "Kroll. Un Chiffre",
  four spreads of 500-group pages, five columns of 100, words written alphabetically across the rows with their
  numbers (rows 89-100 of each column in a small table of letters and syllables at the foot), names and titles in
  3001-3500, the years 1770-1799 and a "Nota" in 3501-4000. It is the same code: the slot model's A-grade values agree
  (2 aan, 17 als, 86 de, 238 belang, 541/641/741/841 en, 1124 het, 1518 met, 1764 oorlog, 2088 te, 3273 Porta ...).
  The layout explains the slot model exactly (rows across five columns of 100).
- inv. 686 (De Weiler's cipher, 15 scans) holds the 1775 "Berigt" the Nota refers to: nonsense groups may open a
  letter before a "begin des briefs" character; an "einde des briefs" character closes it, followed by meaningless
  groups; some characters annul the one or two before them; nulls only in the middle of letters.
- No printed edition of either letter found (Boon 2012 not seen).

## 2. Look-up and re-reading

- Every one of the 238 distinct groups of R2122 and R2131 was looked up on the codebook scans with
  `research/reading_audit/b19_keylook.py` (a five-row window of the group's column, read with the printed number next
  to the word); values in `../key/kroll785_values.tsv`. Doubtful cells (1245, 2756, 3213, 591, 2535) re-cut wider.
- The cipher of both letters re-read on the DECODE images (rotated, full resolution, line by line). Corrections in
  `R2131_corrections.tsv` and `R2122_corrections.tsv`: R2131 2261 -> 2262 (sig; the same group as in line 1), 311 ->
  317? (als dat). R2122's clear salutation and close transcribed into `R2122_cipher.txt`.
- Decode `R2122_decode.txt`, `R2131_decode.txt` (`research/reading_audit/b19_dedem_decode.py`): 307 of 308 groups have a
  codebook value (4414 does not exist).
- Values that differ from the slot model, from the book: 16 alliantie (not alleen), 194 s (spelling unit; 704 194 =
  demarche+s), 526 drie, 675 ge, 1455 instructie (not interest), 1069 konnen, 2364 einde des briefs, 3445/2504/701 begin
  des briefs, 3610 de Envoyé van Pruissen, 3340 Zijne Majesteit de Koning van Pruissen, 1463 de Keizer van Rusland,
  3213 Zee, 2756 voor een.
- The code spells many words in pieces (el+der+s, du+r+ven, ho+ven, ver+lee+gen, onge+pas+te, ver+ne+der+ing,
  meer+gemeld+e); the readings join them.

Failures and open points (named in the readings): 1230, 1330 (numbers where none is meant), 80, 760 twice after an
infinitive (probably the Nota's example number copied in place of a "g" character; not adopted), 4414 (no such code),
3928 de Middellandsche Zee, 1605 Maison, 1463 after "te kennen ge", 2622 troupes (carried but odd); R2131 319 Son
Altesse where "alle" (314) is needed, 591 "g" after "verbond". The marks under most groups (straight and wavy lines,
hooks) are described neither in the codebook nor in the Berigt; the decode makes sense without them.

## 3. Readings and scores

`R2122_reading.md` (whole letter, clear and cipher) and `R2131_reading.md` (the cipher paragraph), with `_en.md`.
Word check (`research/reading_audit/b19_wordcheck.py`): every unbracketed word is carried by the groups or the clear
text. Clean-sentence share of the reading bodies:

| document | _check_reading (modern Dutch list) | explicit holes only (`HOLES=1`) |
|---|---|---|
| R2122 | 0.222 (10/45) | 0.933 (42/45) |
| R2131 | 0.200 (1/5) | 0.800 (4/5) |

As for battier1686, the checker's Dutch list is modern Gutenberg Dutch and fails 18th-century spelling ("zig",
"geeven", "maaken", "hoogenaamt", "insinuaties"); the decision rests on the reading and the explicit holes. R2122's
first three paragraphs read as continuous Dutch; the last cipher paragraph (Sweden, the Kapudan Pasha) has most of the
holes but its sentences still build. R2131 is one sentence with four partial holes. Both set read, grade B.
