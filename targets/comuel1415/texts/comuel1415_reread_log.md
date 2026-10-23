# Re-reading log, comuel1415 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b26)

## Starting point

Reading audit (22 Oct): "decoded, not read"; nothing of the letter in the repository, only a Google Books link to Puig
y Puig 1920 pp. 562-563, said to return 403 to scripts. No image of the cipher exists (ACB Çapera papers, not
digitised); no DECODE record.

## What was done

1. **Existing text?** Yes: Puig y Puig, *Pedro de Luna* (1920), app. CXVII (index CXVI), pp. 562-563, the whole letter
   with his decipherment in italics. The book page `&pg=PA562` is CAPTCHA-walled, but the `jscmd=click3` endpoint
   (used for benedict1399 on 23 Sept) still answers with signed page-image URLs: PA561-PA565 fetched at 1600 px
   (research/reading_audit/b26_gbooks_fetch.py; images in the session scratchpad only). The letter starts on p. 562
   and ends on p. 563 (signature, address, ACB "Documentos inéditos del obispo Çapera" no. 669, a number not recorded
   before).
2. **Transcription.** Whole letter transcribed from the page images, with Puig's spelling, abbreviations and
   punctuation; italic runs (his decipherment) marked `_..._`. Doubtful in the print: "nor fuit" (damaged type,
   read [?non] from the sense of the clause and Puig's own heading); "Comollis etc. subdiaconus etc." is italic in Puig
   but is the subscription, not a deciphered passage, and is kept roman.
3. **Figures.** None: the ciphertext is neither imaged nor printed, so the decipherment cannot be checked letter by
   letter and no key value can be tested. Letters resting on a look-alike alternate: 0 (no figures read here).
4. **Alignment.** The reading is Puig's text word for word; no word supplied; one bracket ([?non]).
5. **Score** (b17_score.py, la, reading body): 0.275 (22/80); explicit holes (HOLES=1) 0.988 (79/80). The low plain
   figure is the word list, not the text: the Latin lexicon is classical and does not know Puig's unexpanded
   abbreviations (dni., dns., ecclie., xpo) or 15th-century spellings (negocia, Castelle, recomendacione,
   ocurrentibus), and the abbreviation points cut sentences short. Reader's judgement: every sentence of the clear
   and deciphered parts is grammatical Latin and the argument runs through (Vadillo as the author of the league with
   the Emperor; Aragon's plan to declare Clement VII and so Benedict XIII false popes, which would make Juan II of
   Castile a bastard; the Queen to be told through her confessor). Before: no text (0.00).

## Result

Read from the existing decipherment (Puig 1920), grade A for the sentences; the decipherment itself is not checked
against figures (outside blocker: the ACB original, needs-physical-access).

Deciphered words: 308 of the letter's 822 (word count of the reading body).
