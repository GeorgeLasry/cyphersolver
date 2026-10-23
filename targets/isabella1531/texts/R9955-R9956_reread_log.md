# Re-reading log, R9955 and R9956 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b20)

## Starting point

Reading audit (22 Oct): both records "decoded, not read"; no transcription, decode or decipherment of either letter in
the repository. Closed on 21 Sept from Tomokiyo's cryptiana page without viewing the images.

## What was done

1. **Every file on the DECODE records** fetched with the shared cookie (research/reading_audit/b20_fetch.py), into the
   session scratchpad only (AGS images, not public domain): R9955 six page images, R9956 eight; no DOC_* text or other
   attachment on either record; no comment blocks. Record text: R9956 "Correspondence between the emperor and the
   empress dated in the years 1531 and 1532", Isabella → Charles V, Brussels (both wrong).
2. **Existing text?** Yes, for both, on the records themselves:
   - R9955: P1 = doc. 195 f. 1r (letter, clear with two cipher passages), P4 = f. 1v (third cipher passage, date,
     "Yo el Rey", "Covos"), P6 = address leaf with docket; **P3 = doc. 196, the contemporary decipherment of the three
     cipher passages** (P5 its blank verso, P2 a blank leaf). Also printed by Wanruo Luo (2021, thesis, Universitat
     de València) pp. 285-287 from docs. 195-196; cited only, not copied (modern edition).
   - R9956: archive order P3 = f. 205r, P2 = f. 205v (cipher from f. 205r l. 9 to f. 205v l. 21; clear tail, date,
     signature "A vuestro servicio, Covos comendador mayor"), P1 = address, **P4/P8 = doc. 206, the contemporary
     decipherment** (recto and verso); P5, P6, P7 blank. Not in Luo's edition (searched the thesis text for
     "496", "205", "1531", "sobrino"); not known in print.
3. **Transcription.** Both letters' clear text and both decipherment sheets transcribed from native-resolution strips
   (research/reading_audit/b20_crop.py), spelling as written, abbreviations expanded. Doubtful places zoomed:
   R9955 "para nra salida" (nuestra, overline on "nra"), "pudo escusar" (stroke over the word; kept "pudo");
   R9956 "de q me a[b?] / sazon" (cramped abbreviation, read [?avise]), "se ha ropto" ([?scripto]), "tra çgas a nro
   sor" ([?gracias] a nuestro señor), "q berna / yo / no se sabe" ([?Yo]).
4. **Address of R9956 settles the recipient**: "Al muy noble señor mi sobrino Juan Vazquez, secretario de Su
   Mag.t" (Tomokiyo had "probably Juan Vázquez de Molina" from the salutation). The signature is Cobos's.
5. **Figures.** The cipher is the general cipher AGS Estado leg. 1.1.1 doc. 112 (Tomokiyo; Luo 2021 p. 601 prints the
   key table as images). Not decoded sign by sign here; spot-checked: R9955 opening ς² u x³ δ³ V⁴ m+² m+³ u =
   la-s-ne-ce-si-da-de-s ("las necesidades"), R9956 opening m+³ u 9 δ² x m+⁵ V³ a+ u h³ δ⁵ ... = de-s-p(a)-ca-n-do-se
   e-s-te-co... ("despachandose este correo"), "to Y 3³ e³ δ² m+³ e³ s" = de mercaderes, "V² ʒ⁵ d" = sazon. The
   decipherments agree with the figures wherever checked. Between "me a" and "sazon" stand two or three signs (20,
   n, ρ) the printed key does not settle at a glance; [?avise] stays doubtful.
6. **Discrepancy noted**: R9956's decipherment sheet copies the clear tail and ends "de Bruselas a x[?] de hebr[er]o",
   while the letter's clear date line is "a xj de enero de 1531", followed by a clear line "De hebrero [...]" (a
   postscript or forwarding date, not read: "qnto? de zur? aqui"). The reading follows the letter.
7. **Alignment.** The readings are the clear text plus the decipherment, word for word; no word supplied. Bracketed:
   R9955 none; R9956 [?avise], [?scripto], [?gracias], [?Yo], "De hebrero [...]".
8. **Score** (research/reading_audit/b17_score.py on the reading body, es): R9955 0.744 (29/39), explicit holes
   (HOLES=1) 1.00 (39/39); R9956 0.714 (10/14), explicit holes 1.00 (14/14). Before: no text (0.00). The sentences
   hold. Unclean sentences are 16th-century spellings and names the modern word list does not know (cedulas, Baeça,
   alvala, previllejo, Benavides, catorze); spelling not modernised.

## Result

Both read from their contemporary decipherments (grade A: coherent sentences, scattered holes; figures spot-checked only).

## Open

- R9956: the abbreviation "a[b?]" before "sazon", "ropto", the postscript line "De hebrero ..."; R9955/R9956: the
  cipher not decoded sign by sign against doc. 112 (spot checks only). Blocker for the sign-by-sign check:
  not-attempted (the key is printed as images in Luo 2021 p. 601; not needed for the reading).
