# Re-reading log, R34 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R34_decryption.txt` (character-model segmentation of DECODE's
transcription D1698, KaJo, Feb 2017, under Meister no. 40) scored 0.62: the subject visible (the Spanish ambassador,
Saluzzo, Orléans) but long garbled runs ("fiorentini spianare uia hauto", "aiizi", "raniera").

## 1. Is there a text already?

- DECODE images: 5 cipher pages (198r, 199r, 199v, 200r, 200v) and 8 "cleartext" images (contact sheet of four checked):
  despatches in clear (ff. 193–197), not a decipherment. The transcriber noted that the images may hold two ciphers:
  they do (198r ends one; 199r, docketed "duplicato", starts another). 198v is not imaged.
- Tempesti (1754) covers the Saluzzo affair from Morosini's letters but nothing that paraphrases this sheet.

## 2. Word decode and hand re-parsing (R34_corrections.tsv, 59 rows)

- Codes without their dot: 154 Spagna, 131 cardinale di; spurious dots: 261 (di), 151 inside "risolutione".
- "per" (64) inside words: spera, spero, sapere (4 21 64 5) — the decoder's vocabulary split them.
- m + 8 abbreviations: estremam., grandem., facilm., intrinsicam., uiuam., diritam.
- Vocabulary gaps where the figures were right: la Ualeta suo fratelo, causaria, carica d'anni, proponeria, d'orechio,
  la Rocela, conuerso, uasali, l'istirpatione, coadiuare, mescolarmi, Hieronimo Gondi, Momoransi, acarezarlo, intorbidare,
  nasce speso, d'Orliens.
- Image checks: the page headers (docket "duplicato" on 199r) and 199v ll. 18–19 (show-through, paper hole).

## 3. Alignment

`python reread_b00_align.py R34`: `TOTAL R34: 945 words, 0 supplied, 7 partly` after two fixes the first run showed: a
supplied "per" ("non solo per le cose" → "non solo le cose") and the 200r/200v page break inside "Maie|stà". The seven
remaining flags are words beside codes (catolico, anzi, grande, che tutauia, continuando) that the figures carry.

## Result

Before: 0.62. After: 0.75 clean-sentence share on the "## Reading" body (hole rate 0.084). By hand: 14 unread stretches
([…]), 6 partly carried words, 945 words; the 199r–200v letter builds sentences throughout. Grade B: sentences hold; a
dozen holes and about twenty figure-context corrections.

## Still open, and why

Short stretches that do not parse under any slip tried: 198r l. 1 (6 2 6 2), the end of 198r (l. 12, beyond "N. S."
and "questo"), 199r l. 1 opening, 199r ll. 11–12 (after "condurla a"), the language named in 199r l. 20, the remains of
the armada (199v ll. 8–9), 199v ll. 16 and 18–19 (what Spain offers to help France take), 200r l. 7 ("2 7 7 8"), 200v
l. 7 ("3 1? 8?"). 199v ll. 18–19 were checked on the image: heavy show-through from the verso and a hole in the paper at the start of
l. 19 (where the transcriber put "2 6?") — an outside blocker for that stretch. The others were not re-checked on the
images in this pass (no outside blocker known; left for an image pass).
