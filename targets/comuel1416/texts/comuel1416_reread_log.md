# Re-reading log, comuel1416 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b26)

## Starting point

Reading audit (22 Oct): "decoded, not read"; nothing of the letter in the repository, only a Google Books link to Puig
y Puig 1920 pp. 578-579, said to return 403 to scripts. No image of the cipher exists (ACB Çapera papers, not
digitised); no DECODE record.

## What was done

1. **Existing text?** Yes: Puig y Puig, *Pedro de Luna* (1920), app. CXXXV, the whole letter with his decipherment in
   italics. Fetched through the `jscmd=click3` endpoint (signed page-image URLs; research/reading_audit/
   b26_gbooks_fetch.py), PA577-PA581 at 1600 px, scratchpad only. The letter is entirely on p. 578 (p. 579 is the
   next item, Jorba to Alfonso V); ACB "Documentos inéditos del obispo Çapera" no. 670.
2. **Transcription.** Whole letter transcribed with Puig's spelling, abbreviations and punctuation; italic runs
   marked `_..._`. The last deciphered clause is Catalan ("e desengana los clarament veus que fa un hom que gos
   parlar"). Puig's footnotes (2)-(4) summarised in the reading's notes; note 2 cites Comuel's earlier letter, ACB
   doc. 661 (not printed, not a cipher as far as Puig says).
3. **Figures.** None: the ciphertext is neither imaged nor printed. Letters resting on a look-alike alternate: 0.
4. **Alignment.** The reading is Puig's text word for word; no word supplied; no brackets.
5. **Score** (b17_score.py, la, reading body): 0.25 (9/36); explicit holes (HOLES=1) 1.00 (36/36). The plain figure
   fails on the classical word list (uideatis, negocia, Castelle, seruicio, absolucionem, the abbreviations dno., dns.,
   xpo., and the Catalan clause). Reader's judgement: the sentences hold (the Pope's exhortation to bear dangers; the
   ciphered instructions on Bartolomé and the church of Zaragoza, the young men of Vera, Juan Ugueti, keeping the Pope
   informed; Gil Sánchez Muñoz rousing the prelates at Barcelona). Before: no text (0.00).

## Result

Read from the existing decipherment (Puig 1920), grade A for the sentences; not checked against figures (the ACB
original, needs-physical-access).

Deciphered words: 85 of the letter's 401 (word count of the reading body).
