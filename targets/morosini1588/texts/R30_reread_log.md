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
