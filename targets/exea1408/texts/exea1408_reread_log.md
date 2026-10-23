# Re-reading log, exea1408 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b27)

## Starting point

Reading audit (22 Oct): "decoded, not read"; nothing of the letter in the repository, only a Google Books link to Puig
y Puig 1920 pp. 500-503, said to be blocked to scripts. No image of the cipher exists (ACB Çapera papers, not
digitised); no DECODE record.

## What was done

1. **Existing text?** Yes: Puig y Puig, *Pedro de Luna* (1920), app. LXIV, pp. 500-503, the whole letter with his
   decipherment in italics. The `jscmd=click3` endpoint (used for comuel1415/1416 in b26) still answers with signed
   page-image URLs: PA498-PA507 fetched at 1600 px (`research/reading_audit/b26_gbooks_fetch.py`; images in the
   session scratchpad only). The letter starts at the foot of the LXIV heading on p. 500 and ends on p. 503 with the
   subscription and the shelf number (ACB *Documentos inéditos del obispo Çapera* no. 133). It is followed by LXV,
   Benedict XIII's letter of 2 Aug 1408 ordering Climent to arrest the Cardinal's benefices, the "litera pape" the
   letter speaks of (clear Latin, not transcribed here).
2. **Transcription.** Whole letter transcribed from the page images, with Puig's spelling, abbreviations and
   punctuation; italic runs (his decipherment) marked `_..._`: everything from "Cardinalis ispanie" to "archiepiscopus"
   except one roman "per" on p. 503. The opening formula ("Reverende pater ... noveritis quod") is roman. Misprints
   kept as printed after a crop check (p. 500 l. 3 "fiuxit" for finxit; "redisivit", "dictu", "parisins",
   "toletamum", "cerificari", "Aragoniat", "colibero"). Puig's footnote numbers are left out of the body and his notes
   listed in the header.
3. **Figures.** None: the ciphertext is neither imaged nor printed, so the decipherment cannot be checked letter by
   letter and no key value can be tested. Letters resting on a look-alike alternate: 0 (no figures read here).
4. **Alignment.** The reading is Puig's text word for word; no word supplied; no bracket. In the English, "colibero"
   (p. 503, the courier "de quo colibero") is left as [?] (the sense is unclear; perhaps a misprint).
5. **Score** (b17_score.py, LANG_=la, reading body): 0.376 (76/202); explicit holes (HOLES=1) 1.0 (202/202). The low
   plain figure is the word list: the Latin lexicon is classical and does not know the 15th-century spellings
   (michi, nichil, eclesie, possesiones, execucionem, negocia) or Castilian names. Reader's judgement: the sentences
   are grammatical late-medieval chancery Latin and the argument runs through (the Cardinal of Spain's defection at
   Genoa, the arrest of his revenues, the four candidates for Osma, the Infante's expulsion of the prelates and of
   Leonor López, the Pope's rebuke for the silence from Castile). Before: no text (0.00).

## Result

Read from the existing decipherment (Puig 1920), grade A for the sentences; the decipherment itself is not checked
against figures (outside blocker: the ACB original, needs-physical-access).

One sentence: "Cardinalis ispanie ... fecit nobis trebelianam ... statim concessit et publicavit suum recessum
parisins" (the Cardinal of Spain played a Trebellian trick on us ... at once agreed and announced his departure for
Paris).
