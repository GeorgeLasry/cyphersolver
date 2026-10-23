# Re-reading log, R42 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R42_decryption.txt` (DECODE D1707, KaJo, Dec 2015) scored 0.435 clean,
the lowest of this batch: the transcriber notes that 8s, 1s and 2s are hard to see and that the ink bleeds through.

## 1. Is there a text already?

- DECODE "cleartext" images D1071–D1073 (contact sheet; docket and last lines cropped): the covering letter in clear,
  docketed "Bles 19 9bre" [1588], "Dal S. Car. Morosino Legato"; it speaks of the Archbishop of Lyon, Rambouillet and
  the finances for the war. Not a decipherment.
- Tempesti (1754) book VII §§ XXXI–XXXV narrates the Council-of-Trent negotiation of November–December 1588 but does
  not paraphrase this letter.
- Rome's decipherments: ASV Francia 27 (not imaged).

## 2. Hand re-parse

The worddecode was only a starting point here: almost every line was re-parsed on the raw figures (printed with the
decoder's parser, line by line). `R42_corrections.tsv` (39 rows). Patterns:
- 1/2 confusion systematic in the transcription ("9 2 0 2 5" for -ione), 8 for 5 (carico, dargli), 3 2 for 3 1 (nt),
  9 0 for 3 0 (fa).
- Spurious dots: 212, 920, 716, 057, 215, 526, 616 (= che + 161 quanto), 517; 219 cifra is a real code.
- 75 = et used as letters inside "settanta".
- No image crop was made for R42; the figures+context corrections in the tsv were not checked on the images.

Aligner (`reread_b00_align.py R42`): fixed "la Santità di N. S." (the aligner expands at most four words) and moved the
303v page mark before "la". Left as artefacts: catolica (226), "di"/"male" at the spurious dot 526, "aspetando" and
"sempre" (words split by a page break), religione/risposta/meco (one slip each in this transcription). TOTAL in the
report.

## Result

Before 0.435 -> after 0.727 (reading body). By hand: about 16 unread stretches […] and 8 partly carried words in ~700
words; the sentences of the audience, the Guise advice and the Queen Mother's illness hold, the opening and two
passages on 304r (the bull, the archbishop) do not. Grade B.

## Still open, and why

- 303r opening (the reference to Montalto's letters and their date); 304r ll. 6–11 (the archbishop "[?d'Arli]", the
  bull "contra […]", "[…] primo", "[…] altro"); 304v the close; a dozen short stretches.
- Blocker: none outside; the next step is an image pass on these stretches (the transcription's 1/2 and 8/5 errors are
  the likely cause). Francia 27 holds Rome's decipherment (physical access).

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`), cancellation strokes looked for (none; show-through on 303r and 304r), the figures parsed
(`r2p_parseall.py`).
Filled:
- 304r l. 6 "l'arciuescouo d'Arli": "26 8 21 00 50 17 8" = d (null 8) a r l i (null 8): Arles, every letter carried.
Left, with blockers:
- 303r l. 1 "[…] per risposta": "5 0 7 194^. 0 2 9 7 8" (best parse "li[austriaci]mqui"). Blocker: no-key-material.
- 303r l. 1 "dela cifra […] nele lettere": "1 7 9 335^. 0 1 3 7 1 5 2 1 2" (best parse "iouenuta"). Blocker: no-key-material.
- 303r l. 1-2 "dele 7 [?del pasato] […] che": "8 2 6 2 6 3 5 0 5 | 7 0 2 1 4 5 2 1 5 2 9 2 0 1 7 8 9 2 5 9 2 0 0 5 2 6 1 7 0 0 5 0 5" (best parse "tdelpasacomicoaredirle"). Blocker: no-key-material.
- 303r l. 4 "N S [?sente] che nela": "4 3 5 0 2 5 1 5" (best parse "semet"). Blocker: no-key-material.
- 303r l. 8 "catolica come […] S M": "3 0 2 1 250^. 2" (best parse "facm"). Blocker: no-key-material.
- 303r l. 9 "uolere più […] questa debita": "(none)". Blocker: nothing written there; no-key-material.
- 303r l. 10-11 "che soto […] pretesti di": "3 2 1 5 0 4 5 | 1 7 1" (best parse "ualsi"). Blocker: no-key-material.
- 303r l. 14 "che posi [?concedere con] la autorità": "2 9 2 5 3 5 0 0 2 0 3 5 0" (best parse "aoaeermen"). Blocker: no-key-material.
- 303r l. 15 "et il [?benefitio] di questo": "4 2 3 5 0 1 2 5 9 0 1 7 2 5 1 7 9" (best parse "benconicio"). Blocker: no-key-material.
- 303v l. 1 "risposta di [266] et in": "266^.". Blocker: too-short.
- 303v l. 4 "tà non [si] confidaua con": "(none)". Blocker: nothing written there; no-key-material.
- 303v l. 8 "del regno [?et] la esortai": "2 6". Blocker: no-key-material.
- 303v l. 23 "tratenirsi tenendolo […] sempre": "(none)". Blocker: nothing written there; no-key-material.
- 304r l. 4 "la quale […] sapeua che": "(none)". Blocker: nothing written there; no-key-material.
- 304r l. 4 "bene non [?era] in tuto": "8 1 5 3 9 2" (best parse "eoa"). Blocker: no-key-material.
- 304r l. 8-9 "S contra […] dal sig": "3 3 9 1 2 5 3 7 0 0 2 1 0 1 5 1 3 5 4 2 1 2 4 2 9 1 0 0 1 5 3 7 0 2 8 2 0 2 1 0 1 | 6 2 2 1 5 1 2 1 2 0 7" (best parse "procurantesaboreimmandatap"). Blocker: no-key-material.
- 304r l. 9 "sig arciuescouo […] primo Mi": "7 0 1 7 0 1 3 5 0 5 7 1 8 2 5 0" (best parse "pinelirl"). Blocker: no-key-material.
- 304r l. 10-11 "arciuescouo Gondi […] altro che": "8 1 6 2 | 5 0" (best parse "dl"). Blocker: no-key-material.
- 304r l. 19 "che le […] parlaria seco": "7 9 2 0 1 5 3" (best parse "iome"). Blocker: no-key-material.
- 304r l. 21 "non resto […] contento perché": "7 0 7 7 7 1 1 9 1 8" (best parse "ipinono"). Blocker: no-key-material.
- 304v l. 2 "dal male [?et] con settanta": "8 2 6". Blocker: no-key-material.
- 304v l. 3 "temere ognuno […] gli altri": "6 3 9 000^. 2" (best parse "tuorm"). Blocker: no-key-material.
- 304v l. 9 "sua misericordia […] a quello": "7 2 9 0 2 1 2 517^." (best parse "impnati"). Blocker: no-key-material.
- 304v l. 9 "a quello [che] s[ia] di": "4 1 7 1 7 1" (best parse "sii"). Blocker: no-key-material.
- 304v l. 11 "dela christianità […]": "8 4 7 9 9 6 152^. 2 7 9 6 0 0 2 111^. 7 4 4 9 113^." (best parse "stoque[franzesi]ltotrarispo[sua"). Blocker: no-key-material.
Result: 1 hole filled; 26 left, each with its blocker.
