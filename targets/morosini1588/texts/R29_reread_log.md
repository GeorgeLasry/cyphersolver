# Re-reading log, R29 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R29_decryption.txt` (character-model segmentation of DECODE's
transcription D1693, KaJo, April 2016, under Meister no. 40) scored 0.50 clean sentences: the topics visible
(Rucellai, Saluzzo, Soissons, Denmark) but garbled words in most lines ("constancia", "aatorit orno", "oirni natione").

## 1. Is there a text already?

- DECODE images: 4 cipher pages (152r–153v) and 13 "cleartext" images (contact sheet of four checked): Morosini's
  despatches in clear and an address leaf, not a decipherment of this sheet. No interlinear glosses on the cipher.
- Docket on 152r: "dup.to di l[ette]ra x Ott." (duplicate of the letter of 10 October [1588]).
- Tempesti, *Vita di Sisto V* II, book X, treats the seizure of Saluzzo from Morosini's letters of 17 October onward;
  nothing that paraphrases this letter. No other print found.

## 2. Word decode and hand re-parsing (R29_corrections.tsv, 44 rows)

- Codes written without their dot, which the decoder spelled out as letters: 217 corriere (four times: "un corriere",
  "questo corriere", "dice eso corriere", "il corriere"), 126 Gran Duca, 129 duca (twice), 131 cardinale di (twice).
  In 152r l. 2 the encipherer wrote 212 and corrected it to 217 with a 7 above the line (image).
- Spurious dots: 247 (la sposa), 149 (hora), 417 (sig. + 8), "?20." (medesma).
- Abbreviations with 8: S. Alt. (sua + a lt + 8), ueram., grandem., sig.
- Vocabulary gaps where the figures were right: di ritorno, la sposa, medesma, perché portase, procurarano, permeti,
  contenteze, Suisons, radolcirli, l'abiuratione, per uedere, Danimarcha, uaseli franzesi.
- Image checks (crops, scratchpad only): 152r ll. 1–3 (docket; 212→217 correction), 152r ll. 10–11 (medesma; questo
  corriere).

## 3. Alignment

`python reread_b00_align.py R29`: `TOTAL R29: 541 words, 1 supplied, 8 partly`. Checked one by one: "il" in "con il
già re di Nauarra" is part of code 232; "medesma", "hora" are the spurious dots; "catolica" (code 226, expanded in the
singular), "cardinale" (131 without dot), "sposa", "pericolosi", "credendo" (one-figure slips listed in the tsv). One
unbracketed supplied article was removed ("la sua speditione" → "sua speditione").

## Result

Before: 0.50. After: 0.587 clean-sentence share on the "## Reading" body (hole rate 0.107; the clerk's spellings count
as holes). By hand: 6 unread stretches ([…]), 6 partly carried words, about 540 words; every paragraph builds sentences
except the short stretches listed below. Grade B: the sentences hold, but with more holes than R17 and several
figure-context corrections.

## Still open, and why

No outside blocker was found for these; they do not parse under any slip tried (both homophone readings, 8 null,
1/2/7, 0/6/8, 3/5, dropped/doubled figure):
- 152r l. 2 opening (5 5 4 7 2 2 1 2 1 6 9 5 2 1 2 1 8);
- 152r l. 21 (1 7 1 0 1 5 1 6 5 before "a fine di");
- 152v l. 4 (5 0 2 2 2 6 1 6 5 6 before "inanzi");
- 153r l. 15 ("1 1 3" after "dele");
- 153v l. 1 (4 5 1 7 2 0 5 between "poche" and "parole") and the last line (4 2 2 7 9 1 2 1 3^. 0 1 2 7 4 2 9 6 0 1 0 2).
Rome's decipherment (Segr. Stato Francia 27, per Hübner) would settle them (physical access).
