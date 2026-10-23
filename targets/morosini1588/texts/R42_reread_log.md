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
