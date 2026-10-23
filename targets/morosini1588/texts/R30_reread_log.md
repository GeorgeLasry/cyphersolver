# Re-reading log, R30 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R30_decryption.txt` (DECODE D1694, KaJo, May 2016, under Meister no. 40)
gave the topics (Nevers and Guise, the Council of Trent, the clergy) with garbles in most lines; `_check_reading.py`
0.646.

## 1. Is there a text already?

- The DECODE record has five cipher images and no "cleartext" images. The clear docket at the head of 162v, as
  transcribed by DECODE: "Del s. Car. Mo[rosini] … 3 ottobre da Bles". No interlinear glosses.
- Rome's decipherments (Francia 27) are not imaged; Tempesti (1754) gives the Nevers–Guise quarrel and the clergy's
  reservations on the Council only in outline. Not used for words.

## 2. Page order

DECODE lists the pages 162v, 162r, 161v, 161r, 160r and its transcriber noted that the order "might be wrong". It is
right: the docket heads 162v, and each page turn continues a sentence ("a S. M.tà andai li giorni pasati" / "a
ritrouarla"; "si maritò nela" / "sorela dela sua moglie"; "cardinale di Guisa" / "suo fratelo"; "ne mancarò" / "di fare
ogni oficio"). The leaves are bound reversed. 160r ends in mid-sentence; its continuation is not imaged.

## 3. Hand re-parsing (R30_corrections.tsv)

About one word in nine re-parsed, nearly all carried by the transcribed figures:
- Words the decoder split or missed: "tiene con mons. di Guisa", scoperto/scoperta/superfluo/apertam. (64 = per inside
  words), "con S. E." (4 8 153 8, also 162r l. 19), "però a fine", "per nuocersi l'uno et l'altro", seminati,
  d'interpormi, "se la lo trouaua buono", "mostrò il Re", date, fidase, "santis. gratia", "io non mancarò" (DECODE
  decode "i ornano caro"), "che io per nome di N. S.", raguagliarò, "questo punto, con dire".
- Codes written without their dot: 129 (twice), 131, 141 (clero), 165.
- Figure habits: 3 2 for 37 (u), 30 for 70 (p), "pr"/"fr" as 7 0 0 0 / 3 0 0 0, 80 for 00.
- Sense check: "sua Ecel." / "S. E." is Nevers at 162v and Guise at 162r l. 19 (who complains of Nevers "from the time he
  married his wife's sister": Nevers and Guise married the Clèves sisters); "ritrouarla", "ela", "lei" on 162r
  ll. 1–9 are S. M.tà.
- No image checks were needed for the sense; the open groups are listed in the reading's notes.

## 4. Alignment (reread_b00_align.py)

`TOTAL R30: 877 words, 0 supplied, 4 partly`. "mancarò" (161r/160r) is split by the page marker (the word runs over the
page turn); "raguagliarò" has the uncertain 6? for g. 160r: 546 of 556 figures used (the unparsed last line).

## Result

Before: 0.646 clean-sentence share (`R30_decryption.txt`). After: 0.688 on the "## Reading" body (892 words; the checker
counts the clerk's spellings as holes). By hand: 12 unread stretches ([…]), 3 partly carried words and 4 supplied
letters in about 880 words; every sentence carried except the last line of 160r. Grade B: the sentences hold
throughout, with a dozen short holes and several figure+context corrections.

## Still open, and why

- Short groups that parse into no word: 162v l. 2 (after "l'altre"), l. 13 ("lasciaua"), l. 15, l. 16, l. 24; 162r
  l. 10, l. 20; 161v l. 19, l. 21 (DECODE "?" figure); 161r l. 21. Not re-checked on the image (no outside blocker; left
  for a second image pass).
- 160r l. 9 and the continuation of the letter: the next page is not imaged (outside blocker).
- Rome's decipherment in Francia 27 would settle the rest (physical access).

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), looked at on the image (scratchpad `reread/r2p/crops`),
cancellation strokes looked for, parsed (`r2p_parseall.py`). The DECODE images are not in the transcription's page
order and some are turned (the transcriber's note): 162v = P5, 162r = P4, 161v = P3, 161r = P2, 160r = P1
(`PMAP` in `r2p_sheet.py`). Many lines carry long diagonal strokes over runs of figures (162v ll. 15-16, 162r ll. 10 and
19-20, 161r ll. 18-21); enlarged, they are the verso's figures showing through the spread ink, not cancellations,
but they make those runs hard to read.
Filled:
- 162v l. 13 "non lascia di fare": "50 21 34 17 212 | 62 171 | 30 21 00 5" (was "[?lasciaua]"; the -ua is not written).
Left, with blockers:
- 162v l. 2 "l'altre […] i ragionamenti" (no figures left between; a group obscured by show-through before "212"), l. 16 "autorità di […]
  N. S." and l. 24 "giorni […] pasati" (nothing written; a group obscured by show-through before "li giorni"). Blocker: no-key-material.
- 162v l. 15 "dela […] et dopo": "1 4 [blot] 2 3 2 1 2 2 2 6" in a stretch obscured by show-through. Blocker: illegible (figures obscured by show-through).
- 162r l. 10 "buono […] disi": "7 1 0 5 6" in a line obscured by show-through; l. 19 "e[s]endo" ("5 5 3 5 0 1 2 6 1 9 1"); l. 20 "uolese
  […] darmi" ("0 3 5 7 9 2"), both lines obscured by show-through. Blocker: illegible.
- 161v l. 2 "[?fidase]" ("3 0 1 7 6 2 4 5 2 1 5 4 5"), l. 19 "concilio […]" ("2 1 2 5 0 3 5 6 8"), l. 21 "duca […] di"
  (DECODE "129. ?26."). Blocker: no-key-material.
- 161r ll. 18-19 "ragua[g]liarò" and "[?inteso]" (171 33 35 45 9 = i preso), l. 21 "si […] che" (7 1 = non, which the
  sentence does not take): lines obscured in part by show-through. Blocker: no-key-material.
- 160r l. 9 the close ("8 4 2 5 9 111. 2 7 0" and "2 0 1 3 7 7 6 9 7 0"). Blocker: no-key-material.
Result: 1 hole filled; 16 left, each with its blocker.
