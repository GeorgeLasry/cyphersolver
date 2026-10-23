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

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`), cancellation strokes looked for, the figures parsed (`r2p_parseall.py`). 198r is clean; on
199r-200v the ink has spread and the verso shows through over the lines; a hole in the paper on 199v l. 19.
Filled:
- 200r l. 17 "ragionato": "1 21 40 17 91 01 21 51 9", every letter carried (was "r[a]gionato").
Left, with blockers:
- 198r l. 1 "[…] loro [?et]": "(none)". Blocker: nothing written there; no-key-material.
- 198r l. 1 "[…] loro [?et] da S": "1 6". Blocker: no-key-material.
- 198r l. 3 "di questo moti[u]o Come si": "2 0 9 1 5 1 1 7 9" (best parse "motio"). Blocker: no-key-material.
- 198r l. 11 "deta di [?sopra] sortirà quel": "4 9 1 3 7 2 8" (best parse "soua"). Blocker: no-key-material.
- 198r l. 12 "si aspeta […] N S": "8 5 5 9 6" (best parse "eque"). Blocker: no-key-material.
- 198r l. 12 "N S […] questo […]": "7 0 0 9 0" (best parse "irqu"). Blocker: no-key-material.
- 198r l. 12 "[…] questo […]": "7 166^. 2 2 9 0 1" (best parse "i[questo]cron"). Blocker: no-key-material.
- 199r l. 1 "[…] l ambasciatore": "0 1 7 9 5 2 4 9 6 0 8" (best parse "niocsquen"). Blocker: illegible (spread ink and show-through).
- 199r l. 12 "a fine […] in [?risposta]": "1 6 5 6" (best parse "etet"). Blocker: illegible (spread ink and show-through).
- 199r l. 12 "[…] in [?risposta] haueua hauto": "1 1 7 4 4 9 7 2 1 2" (best parse "ristria"). Blocker: illegible (spread ink and show-through).
- 199r l. 13 "estremam[ente] la [?buona] intentione di": "4 2 1 3 1 2" (best parse "brz"). Blocker: illegible (spread ink and show-through).
- 199r l. 20 "in lingua […] Pare a": "1 5 5 1 7 1 0 4 9 1 4 7 2 1 0 1 2 2" (best parse "teinsostanza"). Blocker: illegible (spread ink and show-through).
- 199v l. 2 "ha però [?fato] il secretario": "3 0". Blocker: illegible (spread ink and show-through).
- 199v l. 9 "con i [?resti] […] armata": "1 5 3 5 4 5 1 7 2 6 3 7 1 7 1 2 6 3 5 0 1 2 7" (best parse "estiduidenzi"). Blocker: illegible (spread ink and show-through).
- 199v l. 12 "posi molto [pr] esto et": "(none)". Blocker: nothing written there; no-key-material.
- 199v l. 16 "uasali dicendo […] che quando": "9 2". Blocker: illegible (spread ink and show-through).
- 199v l. 18-19 "per sino […] et al": "4 1 7 3 5 0 5 | 1 1 7 3 7 5 2 6 5 8 0 0 3 5 0 1 9 1 0 1 6" (best parse "siultiuederenont"). Blocker: illegible (hole in the paper, show-through).
- 199v l. 19 "al incontro […] ela si[a]": "9 2". Blocker: illegible (spread ink and show-through).
- 199v l. 19 "[…] ela si[a] aiutata nel": "4 1 7 1 7 1" (best parse "sii"). Blocker: illegible (spread ink and show-through).
- 200r l. 7 "afeto sia […] hora tratato": "7 7 8". Blocker: illegible (spread ink and show-through).
- 200v l. 7 "di Lione […] del qual": "8". Blocker: illegible (spread ink and show-through).
- 200v l. 23 "posta in ma[…]": "2 0 2 1 8" (best parse "ma"). Blocker: illegible (spread ink and show-through).
Result: 1 hole filled; 22 left, each with its blocker.
