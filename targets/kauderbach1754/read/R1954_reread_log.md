# Re-reading log, R1954 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b29)

## Starting point

Reading audit (22 Oct): "decoded, not read": `read/R1954.txt` was a self-declared 65% reading on a weak transcription
(the copy is in a different hand, photographed as a photocopy), with `[...]` and bracketed guesses in most sentences.
Score of that reading's body (`b17_score.py`, LANG_=fr): 0.675 (27/40); explicit holes 0.775. That figure flatters it:
it supplies unbracketed words the figures do not carry (*[il est]*, *pourvu*, *[raisons dont on]* were bracketed, but
*entierement avec*, *se vengera*, *de l'Etat* and others were written as read).

## What was done

1. **Every file on the DECODE record**: R1954 has four images (in the main checkout, `img/`, 5472 x 3648, rotated) and no
   DOC_ attachment, no transcription and no comment (`decode/rec1954.htm`). No other copy of the letter is on DECODE.
   The original despatch is in the Hauptstaatsarchiv Dresden (Geheimes Kabinett, Gesandtschaften), not online
   (NOTES, prior work); no print found.
2. **Look-alike digits resolved by language model.** The September transcription marks 314 of 3,452 digits uncertain
   (5/7, 8/9, 4/11, 1/7, 0/6: the copyist's curly 5/7, open-top 8/9 and u-shaped 11/4). A beam search over every marked
   digit's look-alike alternative, the pair phase (5 and 8 nulls) and stray digits, scored by a French 5-gram model
   (`research/reading_audit/b29_kd_beam.py`, lang `fr-modern`), resolves them (`trans/R1954_b29.txt`: `d=` kept,
   `d!` alternative taken). It took the alternative at 137 places. It also showed its limits: it prefers modern
   spellings and skips archaic or proper-name stretches (*uiues*, *obiets*, *Yorcke*), so with the skip penalty raised
   (SKIP=14, UNK=14) and every place checked by eye, its choices were kept only where they make words.
3. **Checked on the images** (pages rotated, lines located by ink profile, `b29_kd_lines_img.py`, `b29_kd_line.py`,
   `b29_kd_bands.py`): seven places corrected (`trans/R1954_b29_corrections.tsv`): *l'inpossible*, *le colonel Yorcke*,
   *egards*, *deux objets*, *six mille hommes*, *de la proteger*; one beam choice reverted (f. 2, 47 = f). Places looked
   at and left open: f. 1 l. 3 *et [la de] plus que probable* (the image has 9, not the transcribed 8, which shifts the
   phase to *et me la de*, no better); f. 1 l. 12 *egards […] comme la […] y attend* (a stray 7 and *la m r*);
   f. 1 l. 15 *re-p-si-n-tations* (a crossed 6); f. 2 l. 6 *d'A[ffry]* (the image has *0 6 6 11* where the
   transcription has *06 11*; no reading of the run before *sa [T./.]* found); f. 2 l. 8 *de la tirer de […]*;
   f. 2 l. 13 *les m o ou on s don apuie* (*motifs dont on* not carried); f. 3 l. 22 *ietter* (the image has 4 where
   *jetter* needs 2: kept as [?jetter]); f. 4 l. 6 *d'A[…]* (two curly signs); f. 4 l. 8 *qu'on est […] de sa bonne*.
4. **Key**: no value changed. Flagged for review, not adopted (sense-only): code 21 read as *inte* in *l'interet*,
   *interets* (twice; 21 = *ce* reads in some twenty other places); 07 for *au* in *aujourdhui*; 41 for *on* in
   *raison*.
5. **Partial reading** (`R1954_partial_reading.md`) and English (`R1954_en.md`). Word by word: each cipher word is the
   decode of `trans/R1954_b29.txt`; words not carried are bracketed (*[que]*, *[la]*, *[?…]*), scribal repetitions and the
   false start *refulpasecoutre* noted. u/v and i/j rendered by position (the code has one sign for each).
   **Look-alike alternates: 195 letters** of the decode rest on a look-alike alternative (137 digits), counted by
   `b29_kd_beam.py` on `trans/R1954_b29.txt` (codes containing a `!` digit).
6. **Score** (reading body): **0.549 (28/51)**; explicit holes only (HOLES=1) **0.725 (37/51)**. The unclean sentences:
   explicit holes in 14; the rest fail on words the modern list lacks (*courront*, *succombera*, *animera*, *exigera*,
   *hessoises*) or period spellings (*allarmer*, *apellent*, *raportees*, *apuie*, *inpossible*, *inportant*).
7. **Reader's judgement**: the arguments paragraph (f. 2 l. 9 to f. 3) holds and translates; the first paragraph holds
   but for *[?la de]*; the d'Affry clause on f. 2 and the last paragraph (f. 4: *qu'on est […] de sa bonne […]*, *on […]
   ses craintes*, *l'engagement de […] viribus*, *la clause […] etats generaux […] retranchee*, *qu'on […] sur une
   declaration*) do not. **Stays decoded, not read** (0.549 is below the bar).

## Open

- The garbled runs of f. 2 l. 6 and l. 8, f. 2 l. 13, f. 4 ll. 6-10 and 17-25: the image digits are legible but do not
  decode to words with the key; they are slips of the copyist of this Dutch intercept copy. Blocker
  **needs-physical-access**: the original despatch in the Hauptstaatsarchiv Dresden (or a Dresden decipherment) would
  settle them; not online.
- The clear sigla [C./.], [Q./.], [S./.], [T./.], [U./.], [W./.], [B./.], [P./.], [E. C./.]: meanings of 1756 not all
  settled from context; blocker **no-key-material** (the 1761 key R936 does not carry this table's names).
