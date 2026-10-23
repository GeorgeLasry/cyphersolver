# Re-reading log, R47 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R47_decryption.txt` (DECODE D1712, KaJo, Dec 2015) carried the gist
(Morosini's defence, the English ambassador, the Council) with garbles in most lines; DECODE's transcriber noted that the
page order might be wrong.

## 1. Is there a text already?

- No "cleartext" images attached on DECODE for this record; no glosses on 385r–386v.
- Rome's decipherments (Francia 27) not imaged; not searched further in print for this letter.

## 2. Page order

386r begins inside a word ("[cons]iderare"); 385r begins inside a sentence ("a lo Re"). The catchword under 385v (figures "3 2 3 5 0 0 5
2 0 2", = "uere ma-", continuing "posi ha-") does not match 386r, so the sheet after 385v is missing. 386v ends "et
dare" and 385r begins "a lo Re"; 386r–v treats the Council (the King's audience), 385r–v Morosini's defence. Reading
order adopted: 386r, 386v, 385r, 385v, with the junction marked as uncertain.

## 3. Hand re-parsing

About one word in eight re-parsed (`R47_corrections.tsv`), nearly all on the transcribed figures: "io le disi"
(decoder "orleans"), "Mi disero" ("nimis uero"), "perché né i popoli né i parlamenti", "l'acetariano", "a lo Re et con
più prudenza", "del sig. Dio, il buon seruitio", "et se ben so", "lo reputo nondimeno (77)", "che uede l'intrinsico"
(32 = ntr), "però quando N. S. truouarà in me, non dico l'enorme et esecrabile mancamento", "né conosco né so",
"castigarmi con i più". Abbreviations m + 8 (parlam.) and 31 = nt (santa, parlamenti) as in the other letters.
No image checks were needed to make the sentences hold; the open words below were not checked on the image.

## Result

Before: 0.683 clean-sentence share (`R47_decryption.txt`). After: 0.862 (731 words) on the "## Reading" body. By hand: 2 unread stretches (the
junction, the end) and 8 partly carried words in about 900 words; every sentence carried.

## Still open, and why

- The junction 386v/385r and the missing verb in "non lo poteua certo": the record lacks the sheet(s) between; and the
  end on 385v runs into the missing following sheet (outside blocker: leaves not in the record).
- [?resto], [?imposibile], [?aperteneua], [?destratione], [?aspri], [?però]: one or two figures each do not fit; an image
  pass might settle them.

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`; the pages are clean), cancellation strokes looked for (a struck figure in 385v l. 18 after "64",
outside any hole), the figures parsed (`r2p_parseall.py`).
Filled:
- 386v l. 5 "imposibile": "171 29 91 54 17 42 17 50 5" (29 = mp), every letter carried.
- 385v l. 18 "ingratitudine": "171 01 59 21 51 17 15 37 26 17 01 5" (59 = gr; was "[in]gratitudine").
Left, with blockers (385r l. 11 "[?destratione]": the figure after "26 35" is overwritten, 4 or 49, illegible):
- 386r l. 1 "[…] [cons] iderare": "(none)". Blocker: nothing written there; no-key-material.
- 386r l. 19 "tuto il [?resto] dela christianità": "8 3 3 5 4 5 9" (best parse "usgr"). Blocker: no-key-material.
- 386v l. 9 "a quali [?aperteneua] d insegnare": "2 6 4 1 5 3 5 0 1 3 5 3 7 0 2 1 2" (best parse "dsteneuna"). Blocker: no-key-material.
- 386v l. 18 "concilio perché [se] i popoli": "(none)". Blocker: nothing written there; no-key-material.
- 385r l. 1 "lo Re […] Et con": "(none)". Blocker: nothing written there; no-key-material.
- 385r l. 11 "trata nela [?destratione] che si": "2 6 3 5 4 9 2 1 5 1 1 7 9 1 0 1 5" (best parse "detratione"). Blocker: illegible (an overwritten figure).
- 385v l. 10 "i più [?aspri] et seueri": "2 4 6 1 7 1" (best parse "bti"). Blocker: no-key-material.
- 385v l. 11 "del mondo [?però] io se": "8 1 6 4" (best parse "per"). Blocker: no-key-material.
- 385v l. 20 "che posi ha[uere ma-] […]": "1 4 2 1" (best parse "ha"). Blocker: no-key-material.
Result: 2 holes filled; 9 left, each with its blocker.
