# Re-reading log, R19 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R19_decryption.txt` (character-model segmentation of DECODE D1687,
TimB, Jan 2016, speech-recognition transcription) scored 0.672 clean on `_check_reading.py`; the gist (the Council of
Trent, the Estates) visible, many words garbled.

## 1. Is there a text already?

- DECODE "cleartext" images D954–D962 (contact sheet checked) are the covering letter in clear, ff. 66v–70v, which
  DECODE has also transcribed (D1807, JoH 2019): "Sciartes 23 agosto", Morosini's arrival at Chartres, the presentation
  of Bianco, the Council in general terms, the absolution of Conti and Soissons. A different text, not a decipherment;
  used for date, place and names (Suessione) only. No interlinear glosses on the cipher pages.
- Tempesti (1754) has nothing that paraphrases this letter (searched Sciartres, Soissons, Aumont).
- Rome's decipherments are in ASV Francia 27 (not imaged; physical access).

## 2. Word decode and hand re-parse

Started from `R19_worddecode.txt`; about one word in eight re-parsed (`R19_corrections.tsv`, 52 rows). Main causes:
- Decoder vocabulary/segmentation: "eso concilio" read as "estoit cilio" (twice), "l'intiera" as "li uienna", "io la
  pregauo" as "il a pregauo", "me li facese uedere, perché mi asicurauo" as "mentira ces e uederete miseria entrar",
  "io pensauo", "io che cosa l'importase che i preti et i monaci", "era sempre stato", "riuocarli", "nei medesmi
  oficii", "io uego", "Stati Generali", "il medesmo parlamento", "mi parlò", "adunando", "trouato bono", "parentarli".
- Codes written without their dot: 135 uescoui (72v l. 20), 131 cardinale di (73r l. 4), 129 duca di (73v l. 14,
  74v l. 1). 8 as abbreviation null after "sig" (71v l. 5, 73r l. 5) and m + 8 = -mente (longam., 72r l. 19).
- Image checks (crops, scratchpad): 71r l. 1 (opening, transcription right; dot on the middle 1 of 111), 72v l. 8
  (transcription right; the stretch after riuocarli still does not parse), 73v l. 18 (DECODE "0 0 8" is "8 5 0 0 8"
  on the image: "più di 500 gentilomini").
- Aligner (`reread_b00_align.py R19`): flagged molte (e has no figure: now molt[e]), Ill.ma (one l: Il[l].ma),
  maresciale (no e in the figures: now "marsciale"), dipendere (now [?dipendere]); doue and mancato flagged with one
  letter each, but the figures carry them (aligner artefacts). TOTAL after fixes in the report.

## Result

Before 0.672 -> after 0.739 (reading body). By hand: 9 unread stretches […], 2 unknown dotted groups [16], about 14
partly carried or supplied words in ~1,340 words. Grade B (several figure+context corrections; the opening and closing
formulas unread).

## Still open, and why

- Opening (71r l. 2) and closing (74v ll. 2–3) figures: no parse; both contain "0 0 2 7 … 111." (perhaps a formula).
- The recurrent lone "o" (191/91) where the sentence needs "Io" or nothing (five places): the reading supplies [I]o.
- 72v l. 8 after riuocarli (image-checked, no parse); 72v l. 3–4 "5 0 4 1 7 1"; 74r l. 17 and l. 21 short gaps;
  two dotted "1 6^." groups without a third figure (72v l. 14 quello?, 73r l. 22 questo?).
- No outside blocker for these except Francia 27 (physical access), which would settle them.

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located on its transcription line (`research/reading_audit/r2p_holes.py`), the line looked at on the image
(scratchpad `reread/r2p/crops`; on 71r the row grid is one line low), cancellation strokes looked for, the figures
parsed under Meister no. 40 (`r2p_parseall.py`). Cancellation strokes: a struck figure on 73r l. 6 and 73r l. 23 and
several struck figures in "auisata" (74v l. 2), none inside a hole.
Filled (every figure carries the word):
- "Io" four times (71v l. 9, 72r l. 16, 72v l. 13, 73r l. 8) and "Mi"/"mi" (72r l. 13, 73r l. 6): the image has "8 7 1 9 1"
  and "8 2 0 1 7 1": a single null 8 before 7 191 (io) and 20 171 (mi). Read before as the null 87/82.
- 71r l. 16 "ma" (8 20 2: 2 is a homophone of a); 71r l. 24 "un re" (173 0 1 35); 71v l. 6 "meritaria" (... 17 212).
- 71v l. 22 "come": the image has "8 7 9" (DECODE "8 9"): 79 = come.
- 72v l. 1 "se": the image has "5 6 4 1 5 3" (DECODE "5 6 3 1 5 3"): che se.
- 72v l. 4 "si" (4 171 between "quelli che" and "fosero": "whoever they were") and "come" (8 79).
- 72v l. 9 "Re": "6 21 01 51 91 1 153" = tanto re.
- 73r l. 4 "mi" (8 20 7); 73r l. 5 "s[e]" (8 4: the s is written, not the e); 73r l. 23 "io" (171 9).
- 73r l. 22 "medesmo": the image has "2 0 3 5 2 6 3 5 4 5 2 0 9" (DECODE "7 0 3 5 ..."); the "16" before it has two dots.
- 73v l. 1 "sino": the s is the "8 4" at the foot of 73r (l. 23 ends "... 1 9 1 8 4"), "ino" heads 73v.
- 73v l. 23 "dipendere": "dipe" ends 73v, "0 1 2 6 3 5 0 0 5" (ndere) heads 74r.
- 74r ll. 12-13 "Per questo io non manco di fare": "64 166. 7 191 | 71 20 21 01 25 191 26 17" (was "non o man[c]ato").
- 74r l. 14 "ho" (14 | 191); 74r l. 21 the "[…]" after "bono" held only a null 8: withdrawn.
Left, with blockers:
- 71r l. 2 opening "9 2 0 0 2 7" and "5 2 8 2 0 3 5 3 2 5" after N. S.: as transcribed, no parse. Blocker: no-key-material.
- 71r l. 13 "[?si]": "4 2 1 7 1" on the image, the 2 not used. Blocker: no-key-material.
- 71r l. 23 "molt[e]": "2 0 9 1 2 7." as transcribed. Blocker: no-key-material.
- 71v l. 6 "l[a]sase": "5 0 4 5 2 1 5 4 | 1 5 3" on the image; the first a is not written. Blocker: no-key-material.
- 71v l. 16 "[?manco]": "8 5 6 0 2 1 2 0 1 2 5 9" on the image (the 6 retouched); k/t + anco. Blocker: no-key-material.
- 72v l. 7 "[?il]": "1 7 1" (i) at the line end. 72v l. 8 "riuocarli; […]": "8 4 1 7 2 5 9 1 0 2 5 5 0 5 2 1 2 9 2"
  as transcribed, no parse. 72v l. 14 "[16]" and 73r l. 22 "[16]": dotted 16 with no third figure. 72v l. 16
  "[?asenblea]": as transcribed. Blocker for all: no-key-material.
- 73r l. 20 "[?le]" (the figures before 8 are crowded on the image) and "[?uolese]" ("3 9 1 5 0 1 ..."). Blocker: illegible.
- 73v l. 10 "i[n]": "1 7 1 | 90 35 05 153" = i quele, no n written. Blocker: no-key-material.
- 73v l. 15 "[…] pare": "9 1 8" (or). Blocker: too-short.
- 74r l. 17 "con sé […] magiore": the image has "1 7 1 5 0 9 1 0 0 9" (DECODE "...9 2 0 0 9") = i loro, which the
  sentence does not take. Blocker: no-key-material.
- 74r l. 21 "[?anco]" ("2 0 1 2 1 9 1"), "metere […]" ("1 4 4 2 3 2") and "questo […] disegno" ("1 9", con).
  Blocker: no-key-material (the last: too-short).
- 74v ll. 1-2 "[…] quello che": "8 6 | 1 7 1" (i). Blocker: too-short.
- 74v ll. 2-3 closing "8 2 1 5 2 7 4 9 1 2 2 9 111. 2 2 5 4 9 6 9 0 0 2 7 1 7 1", ended by a paragraph rule: no parse.
  Blocker: no-key-material.
Result: 27 holes filled; 21 left, each with its blocker.
