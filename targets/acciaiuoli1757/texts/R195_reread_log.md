# Re-reading log, R195 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b12)

## Starting point

Reading audit (22 Oct): decoded, not read. The repository had Lasry's letter-level decryption (decode/DOC_R25_D3231)
split into words in READING.md (19 Sept), with most nomenclator codes open and "open codes and gaps in nearly every
sentence".

## What was done

1. **Is there a text already?** Yes. The DECODE record's attachments, fetched with the project cookie
   (research/reading_audit/b12_fetch.py; images kept in the session scratchpad only), were described in NOTES as "key and
   work images" and never looked at. They are the Secretariat of State's own decipherments: for R195, DOC_R25_D946 = DOC_R195_D1402 (clear fair copy f. 94r, 'Decif. li 21 8bre'); working draft D947 = D1403 (f. 95r).
2. **Transcription** of the decipherment from the images at native resolution, line by line
   (texts/R195_decipherment.txt).
3. **Alignment** word by word with the key decode (research/reading_audit/b12_dec.py, Lasry's key with one change found
   here: 03 = per, not nel; b12_align.py, a dynamic-programming aligner in which a code group may stand for any run of
   clear words): texts/R195_align.tsv lists every clear word with the figures that carry it. The code values implied by
   the four decipherments agree across the letters (2300 tutt-, 2171 molt-, 2183 qual-, 2189 quest-, 2159 -mente, 2774
   Re [di Portogallo], 2530 Marchese, 2378 Città, 2398 Corte, 2538 Ministr-, 2740 prim-, 2743 Principess-, 2813 Spagna,
   2817 Stato, 2893 anni, 2908 tre ...), so the decipherments are of these figures.
4. **Result**: _check_reading.py on the reading body 0.91 (10 of 11 sentences); 150 clear words: 112 carried letter by letter, 26 by codes. The decipherer's one hole ('poiché non . . .', margin '(non s\'intende)') read on the cipher image: 2180 14 55 75 05 59 98 55 98 53 = 'poiché non ha da durari' (DECODE: '2 1 8 0 ? 4 5 5 ...'; texts/R195_corrections.tsv), agreeing with the draft 'che non ha da durare'.
5. **Open**: 'solamente assicurato' and 'della gente di quei paesi' not confirmed by the figures as transcribed (marked [?]).

## Failures and corrections

- READING.md's guesses 2530 = chirurgo and 2823 = an unknown title are wrong: 2530 = Marchese/Marchesa, 2823 = Sua
  Maestà (from the decipherments).
- Several stretches of DECODE's digit transcriptions do not decode to the decipherment's words; where checked on the
  image (R195 l. 3, l. 11) the transcription, not the decipherment, was at fault in l. 11; l. 3 stays unexplained.
