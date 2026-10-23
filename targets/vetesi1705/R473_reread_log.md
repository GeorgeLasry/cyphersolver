# Re-reading log, R473 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b37)

## Starting point

Reading audit (22 Oct): "decoded, not read". The only text was DECODE's transcription (MA, 2020), whose PLAINTEXT lines
render the contemporary interlinear gloss as garbled syllables; no reading file: before = 0.00.

## 1. Is there a text already?

- DECODE R473 record re-fetched (`b37_fetch.py`, scratchpad): three images (ff. 92-95), the DOC transcription; no
  attachment or comment block. All three images read at full resolution (crops `b37_tiles.py`, scratchpad).
- The letter carries the **contemporary interlinear decipherment** over nearly every cipher group: this is the text.
- Print: the pencil note on f. 92 cites *Ráday Pál iratai* I (1955), item 102 n. 1, p. 494. Web search: the 1955 volume
  is not online (REAL-EOD 18464 is the 2003 volume for 1709-1711; Szaktárs paywalled). Not compared; it is a
  copyrighted modern edition in any case (cite, not copy).
- **Neighbouring records.** R471, R472, R474, R475 fetched: R471/R472/R475 are Rákóczi keys (Latin, Latin, French), R474
  a Latin cipher letter. A scan of the DOC files of R380-R520 (`b37_keyscan.py`) against 18 glossed groups of R473
  found **R446** (Ráday Archives C64-4d2-25 no. 6, "key, original", Hungarian): 16 of 18 agree; nothing else above 1.
  R446's image was read to correct DECODE's transcription of it: 69 *al* (DECODE *ac*), 71 *an*, 72 *ar*, 73 *as*,
  74 *at* (DECODE shifted them and gave 74 to *az*), 80/32/58 *ö* and 70/33/59 *ü* (DECODE *O*, *U*), 35 *ly*
  (DECODE 36 twice), 296 *Belgium* (DECODE *Belgin*); the key's last column, headed *x*, holds 9 (and 8): nulls.

## 2. Reading on the image

- `R473_transcription.txt`: clear text and gloss transcribed afresh, line by line, gloss syllables as written over each
  group. Doubtful clear words marked (?).
- `b37_vetesi_dec.py`: every group decoded with R446 and set against the gloss (`R473_key_vs_gloss.tsv`,
  running decode `R473_decode_R446.txt`): 380 groups; 304 where both give a value; 253 agree. The 51 others: spelling
  variants (*Hollandia*/*Holandia*, *vö*/*vő*, *kogy* = *hogy* in the key), misalignment of my gloss syllables over long
  runs, the glossator's (or my) *mi*/*m* for 175 *ni*, 123 *go* glossed *na*, and four writer's figures that do not give
  the gloss's syllable (78 *Ba* for *az* twice, 150 *P* for *le*, 97 *eg* for *ab*, 83/48 in the subscription). Where
  key and gloss part, the reading follows the one that makes the word and says so, or marks [?word].
- No key value adopted beyond R446 itself (its image) and 2670 = *Nagyságod* (key "Angord" = *Nagod*, and the gloss).
  Groups outside the key (9, 8, 6, 7, 1000, 512, 750, 2820, 390, 412, 999, 730, 500, 1060, 3074, 680, 2100, 1560, 670,
  06, 3, 5) are nulls: none has a gloss, they fall where nothing is missing. One exception noted: 750 has *n* over it in
  *Sopro[750]t*, so [?Sopront].
- Key settled garbled glosses: *Niszevárat* (Nice castle, which surrendered to Louis XIV's army on 4 January 1706),
  *az király táborba*, *dolgok jól*, *Belgiummal*, *Namur felé által*, *hogy Herbaville ujjobban*, *December írt*, the
  heading *Méltóságos Fejedelem, nagy jó Kegyelmes Uram*.
- Clear words rechecked on crops: *hogy azon* (not *ugyan*), *habozni* (*Arragonia is közelget habozni*), *folyó(?)*,
  *kész(?)*. Still doubtful: *esmiten*, *eszerint*, *szövetségét*, *viretelu dalnad*, *lesett*, *floritani*, *visat*,
  *mandilat*, *hivel*, *hónap*, *parancsoll*, *Exme*: faded ink.

## 3. Alignment

`b37_align_gloss.py R473_transcription.txt R473_reading.md R473_decode_R446.txt` -> `R473_align.txt`: 358 unbracketed
words; the 7 not found verbatim are expansions (*orsz.* -> *ország*, *Kegs* -> *kegyes*) and *udvarnál|ok* joined across
two runs. One bracketed doubtful ending, *király[?nak]* (key *mü k*, gloss unclear).

## 4. Bar

- `b17_score.py` LANG_=hu: 0.086 (the hu word list is modern; 1706 spelling *esztendőben*, *hellyet*, *edgyütt*, *lött*
  are not in it); HOLES=1: **0.829** (29/35). `_check_reading.py --file`: 0.25 (detects French; pointer only).
- Look-alikes: none in the cipher (numbers); the glossator's *m/mi/ni* confusion is resolved by the key.
- Reader's judgement: the news-letter builds sentences throughout (French and Spanish war news, Dutch politics, his own
  position); about five sentences in the faded part of f. 94r (the Sopron/Herbeville passage and the following lines)
  keep two or three doubtful words.

Verdict: **read** (grade B). Open: doubtful clear words (illegible on the photographs); the 1955 edition not compared
(needs physical access).
