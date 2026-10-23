# Re-reading log, R201 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b12)

## Starting point

Reading audit (22 Oct): decoded, not read. The repository had Lasry's letter-level decryption (decode/DOC_R25_D3231)
split into words in READING.md (19 Sept), with most nomenclator codes open and "open codes and gaps in nearly every
sentence".

## What was done

1. **Is there a text already?** Yes. The DECODE record's attachments, fetched with the project cookie
   (research/reading_audit/b12_fetch.py; images kept in the session scratchpad only), were described in NOTES as "key and
   work images" and never looked at. They are the Secretariat of State's own decipherments: for R201, DOC_R201_D1414-D1415 (clear fair copy f. 161, stamp 278, 'Decif. li 13 Marzo'); a second clear text addressed to Card. Torrigiani, f. 162 (D1416).
2. **Transcription** of the decipherment from the images at native resolution, line by line
   (texts/R201_decipherment.txt).
3. **Alignment** word by word with the key decode (research/reading_audit/b12_dec.py, Lasry's key with one change found
   here: 03 = per, not nel; b12_align.py, a dynamic-programming aligner in which a code group may stand for any run of
   clear words): texts/R201_align.tsv lists every clear word with the figures that carry it. The code values implied by
   the four decipherments agree across the letters (2300 tutt-, 2171 molt-, 2183 qual-, 2189 quest-, 2159 -mente, 2774
   Re [di Portogallo], 2530 Marchese, 2378 Città, 2398 Corte, 2538 Ministr-, 2740 prim-, 2743 Principess-, 2813 Spagna,
   2817 Stato, 2893 anni, 2908 tre ...), so the decipherments are of these figures.
4. **Result**: _check_reading.py on the reading body 0.95 (18 of 19 sentences); 232 clear words: 151 carried letter by letter, 72 by codes, 9 partly or not (garbled transcription stretches).
5. **Open**: none.

## Failures and corrections

- READING.md's guesses 2530 = chirurgo and 2823 = an unknown title are wrong: 2530 = Marchese/Marchesa, 2823 = Sua
  Maestà (from the decipherments).
- Several stretches of DECODE's digit transcriptions do not decode to the decipherment's words; where checked on the
  image (R195 l. 3, l. 11) the transcription, not the decipherment, was at fault in l. 11; l. 3 stays unexplained.
