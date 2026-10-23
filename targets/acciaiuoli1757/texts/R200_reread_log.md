# Re-reading log, R200 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b12)

## Starting point

Reading audit (22 Oct): decoded, not read. The repository had Lasry's letter-level decryption (decode/DOC_R25_D3231)
split into words in READING.md (19 Sept), with most nomenclator codes open and "open codes and gaps in nearly every
sentence".

## What was done

1. **Is there a text already?** Yes. The DECODE record's attachments, fetched with the project cookie
   (research/reading_audit/b12_fetch.py; images kept in the session scratchpad only), were described in NOTES as "key and
   work images" and never looked at. They are the Secretariat of State's own decipherments: for R200, DOC_R200_D1456-D1458 (clear fair copy ff. 108r-109r, 'Decif. li 28 Decembre'); second fair copy D1459-D1460 (ff. 110r-111r); working draft D1412-D1413.
2. **Transcription** of the decipherment from the images at native resolution, line by line
   (texts/R200_decipherment.txt).
3. **Alignment** word by word with the key decode (research/reading_audit/b12_dec.py, Lasry's key with one change found
   here: 03 = per, not nel; b12_align.py, a dynamic-programming aligner in which a code group may stand for any run of
   clear words): texts/R200_align.tsv lists every clear word with the figures that carry it. The code values implied by
   the four decipherments agree across the letters (2300 tutt-, 2171 molt-, 2183 qual-, 2189 quest-, 2159 -mente, 2774
   Re [di Portogallo], 2530 Marchese, 2378 Città, 2398 Corte, 2538 Ministr-, 2740 prim-, 2743 Principess-, 2813 Spagna,
   2817 Stato, 2893 anni, 2908 tre ...), so the decipherments are of these figures.
4. **Result**: _check_reading.py on the reading body 1.0 (31 of 31 sentences); 349 clear words: 195 carried letter by letter, 99 by codes; Lasry's digit groups align worse here than DECODE's D1662. 2803 = Segretario (draft interlines it; R195 uses 2803 for Segretari/Segretario), so 'Segretario de Carvalho' where the fair copy has 'Sig.re'. 2339 left blank in the fair copy, 'Arciduchessa' struck in the second copy, 'Ambasciatore di Spagna' in the draft: read 'Ambasciatore di [?Spagna]'.
5. **Open**: 2339's 'Spagna' rests on the draft only.

## Failures and corrections

- READING.md's guesses 2530 = chirurgo and 2823 = an unknown title are wrong: 2530 = Marchese/Marchesa, 2823 = Sua
  Maestà (from the decipherments).
- Several stretches of DECODE's digit transcriptions do not decode to the decipherment's words; where checked on the
  image (R195 l. 3, l. 11) the transcription, not the decipherment, was at fault in l. 11; l. 3 stays unexplained.
