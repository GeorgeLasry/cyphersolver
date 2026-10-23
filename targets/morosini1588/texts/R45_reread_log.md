# Re-reading log, R45 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R45_decryption.txt` (DECODE D1710, KaJo, Jan 2016, Meister no. 40):
clean-sentence share 0.724, hole rate 0.089. The decryption followed DECODE's image order, which is wrong.

## 1. Is there a text already?

- DECODE "cleartext" images (D1077, D1086, D1091, D1096, D1100): a covering letter in clear (ff. 355–356, Blois [?]
  January 1589), its address leaf ("Bles … di Genaro … Card.le Morosino", with a
  short summary) — not decipherments.
- Francia 27 (Rome's decipherments) not imaged. Tempesti not used for this letter.

## 2. Page order

The transcriber noted the catchwords and suspected the order. Decoding the catchwords settles it: 359v's catchword
0 1 2 1 3 7 2 1 0 0 9 ("nauarro") opens 360r; 360v's 2 1 2 5 0 ("a le[gato]") opens 358r; 358v ends "suce-" and 361r
opens "-dere ala corona"; 361v's 2 5 3 5 0 0 2 5 2 ("[ri]cercase") opens 357r. Reading order: 359r, 359v, 360r, 360v,
358r, 358v, 361r, 361v, 357r — one letter, not two ciphers as the transcriber wondered.

## 3. Decode and repairs

- Batch decoder, scratch variant `dec2.py`, hand re-parsing with `fit.py`, as R32. Most garbles were vocabulary gaps
  (l'infelice sucesso, presentito, impiastro, nel'edito dela pacificatione, mutilati, timorose, refrigerio, saluis
  iuribus regis et regni, astenese) and m + 8 abbreviations (ten of them).
- Spurious dots: 215, 516 (= 151 with the dot misplaced), 912 (twice), 317, 021.
- Decoder word choices corrected from the figures: "uendere" (not prendere), "note" (not morte), "io non so se".
- Failures: the opening four figures; "conspirarà" and "sperando" at 358r l. 15 only partly fit; the object after
  "aprouare" (358v l. 6); the see "8 1 7 3 7 0 0 3 7 4 5" (Eurus/Évreux?); the closing.

## 4. Image checks

None decisive (corroded leaves); corrections `figures` / `figures+context`.

## Result

Before 0.724 → after 0.833 clean-sentence share on the "## Reading" body (hole rate 0.089 → 0.075). By hand: 4 unread
stretches […] (opening, "aprouare […]", "non […] mi laso", the closing) and 7 partly
carried words in about 2,050 words. Every sentence holds: the audience after the Queen Mother's death, Morosini's
remonstrance on Navarre, the King's answers (Nevers recalled; the Edict of Union already excludes heretics; Navarre's
envoy denied), the King's confidence about the Vendôme–Bourbon clause, the Council of Trent "saluis iuribus regis et
regni", Morosini's answer to Montalto's reproach ("la burla … discorsi"), the Guise trials and the Archbishop of Lyon.
Grade A.

## Still open, and why

The opening (359r l. 1, probably on a lost leaf), "[?un] Re" (359v l. 12), "[?conspirarà] [?sperando]" (358r l. 15),
the object at 358v l. 6, the date "[?5]" of Montalto's cipher (361r l. 6), the see of the bishop (361v l. 12), two
figures at 357r l. 7, the closing (357r l. 24). No parse fits the transcribed figures; Francia 27 would settle them.

## Word-by-word alignment (`reread_b00_align.py`, REREAD_BRIEF step 3)

- First run TOTAL R45: 2076 words, 2 supplied, 10 partly. Changed quell'altra → quella altra (165), le esplicai → l'esplicai, acciò → aciò; bracketed concili[i]. Left as artefacts: incapace and propria (letters inside spurious dotted 215 and 317).

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`; the pages are clean), cancellation strokes looked for (none), the figures parsed (`r2p_parseall.py`).
Filled:
- 360r l. 10 "incapace": "171 01 25 21 70 21 5 25" (DECODE's dot on 215 is not on the image): every letter carried.
Left, with blockers:
- 359r l. 1 "[…] se bene": "4 4 5 2 2 7 0 0 1 8" (best parse "sscapn"). Blocker: no-key-material.
- 359r l. 1 "prima che ritornar[e] al audientia": "1 1 7 1 5 9 1 1 3 0 1 2 1 4 5" (best parse "ritornas"). Blocker: no-key-material.
- 359v l. 13 "conueniua a [?un] Re christianisimo": "9 8 2 1 2" (best parse "oa"). Blocker: no-key-material.
- 360r l. 22 "che quello [?mi]": "0 2". Blocker: no-key-material.
- 358r l. 11 "posi mai [pe] ruenire a": "(none)". Blocker: nothing written there; no-key-material.
- 358r l. 15 "più animosam[ente] [?conspirarà] [?sperando] di": "2 1 2 0 1 1 7 2 0 9 1 4 5 2 1 2 0 8 1 9 4 4 1 7 0 0 2 1 0 0 2 9 9 4 6 4 1 7 1" (best parse "animosanospiraraquandosperi"). Blocker: no-key-material.
- 358v l. 7 "meno aprouare […] che restino": "0 5 1 7 1 9 1 6" (best parse "liot"). Blocker: no-key-material.
- 361r l. 6 "ma di [?5] del pasato": "8 5". Blocker: no-key-material.
- 361r l. 12 "che i concili[i] generali confirmati": "1 9 2 5 1 7 5 0 7" (best parse "concili"). Blocker: no-key-material.
- 361v l. 12 "uescouo di [?Eureus] et sotoscrita": "8 1 7 3 7 0 0 3 7 4 5 8" (best parse "uirus"). Blocker: no-key-material.
- 357r l. 1 "nome dela [Santità di] N S": "(none)". Blocker: nothing written there; no-key-material.
- 357r l. 6-7 "che non […] mi laso": "9 1 | 9 8" (best parse "ocon"). Blocker: no-key-material.
- 357r l. 8 "ala burla [?non] mi tengo": "7 1". Blocker: no-key-material.
- 357r l. 21 "l arciuescouo [di] Lione ma": "(none)". Blocker: nothing written there; no-key-material.
- 357r l. 23-24 "ha fato […]": "8 0 | 2 7 111^. 4 2 0 0 1 7 1 0 2 2" (best parse "mi[il"). Blocker: no-key-material.
Result: 1 hole filled; 15 left, each with its blocker.
