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
