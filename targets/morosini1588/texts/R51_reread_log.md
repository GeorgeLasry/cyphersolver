# Re-reading log, R51 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R51_decryption.txt` (DECODE D1715, KaJo, Feb 2016) scored 0.442 clean;
the word decode broke on most of the place and person names.

## 1. Is there a text already?

- DECODE "cleartext" image D1103 (contact sheet): a covering letter in clear, not a decipherment.
- Tempesti (1754): no passage paraphrasing this sheet found.
- Rome's decipherments: ASV Francia 27 (not imaged).
- The transcription's clear heading reads "Jours. ad 27. di Marzo 1589": Tours (the court moved there in March 1589).
  Its four figures "2 2 3 0" before the first page header (decoded "a a un") are stray and left out.

## 2. Hand re-parse

Re-parsed on the raw figures line by line (`R51_corrections.tsv`, 27 rows). Most breaks were names the decoder's
vocabulary lacks: Suisone, Sagona, Falandra, Umena, d'Umala, Longauila, San Quintino, ualoni, Etampes, Orliens, Amiens,
Niort, Lodun, Blanc … Berri, Argenton, Montmorilon, "Al'abate dal Bene" (decoded "la satieta"); null 8s around names and
numbers (10 milia, 1400). Sentences recovered by hand: "mi alegri dela rouina de miei suditi, anzi dela mia medesma",
"le ricete siano pagate a tesorieri di S. M.tà", "non partirà se non fate le feste", "non arriuano a 10 milia fanti et
1400 cauali", "cominci a respirare". Image check: 466r rows 7–9 (transcription right; "resta" for testa is the
encipherer's slip).

Aligner (`reread_b00_align.py R51`): respelled "caualli/città" as the figures give them (cauali, cità); left "caciato"
and one "le" (artefacts). TOTAL in the report.

## Result

Before 0.442 -> after 0.568 (reading body). The checker counts the many proper names and clerk's spellings as holes;
by hand the sentences hold except 7 short unread stretches and 6 partly carried words in ~465 words. Below the 0.60
bar: it stays "decoded, not read" on the measure, though it reads as sentences; grade B if the lead counts it.

## Still open, and why

- The opening before "hieri sera"; the refuge "in […]" and "nele [?rene]" (466r); "et esi […] nuoui ordini"
  (466r l. 22); "la quale […] non era" (466v l. 8); the close after "giustificare presto" (467r l. 9).
- [?Umans] and [?l'Isle Buchar] are name readings that the figures carry only in part. No outside blocker; Francia 27
  would settle them.

## 23 Oct 2026, r2d (Claude Opus 5.5)

Regraded on the v2 measure (research/reading_audit/r2d_score.py, body only, every conjecture and unread stretch a hole): see the profile reading_review for the scores; now read. DECODE attachments re-opened (no decipherment). Image checks this pass (crops in the session scratchpad, r2d/morosini/crops): 466r l. 3 (opening "4 2 1 9 4 2 7 1 2 8" as transcribed, no parse); 466v l. 8 read "la quale, che so, non era ancora montata" (21 95 05 56 4 191 71 5 00 2 92, enumerated with research/reading_audit/r2d_mparse.py); "Umans" unbracketed (every letter carried). Other parses tried and not adopted: "et esi conseruarela nuoui ordini" (19 45 35 00 37 21 1 35 05 212), the place "45 21 17 21 15 13 35 45".

## r2m, 23 Oct 2026 (Claude Opus 5.5): remaining holes checked on the DECODE images (IMG_R51_I263-I265, scratchpad)
- 466r: the image row holding the end of transcription line 22 reads "... 6 9 5 4 5 1 7 1 1 9 4 5 3 5 0 0 3 7 2 1 1 3"
  and the next row begins "5 0 5 2 1 2 0 7 7 9 ..." (nuoui): as transcribed. Parses (research/reading_audit/
  r2d_mparse.py): 69 5 45 171 19 45 35 00 37 21 1 35 05 212 = et esi conseruare la; reading now "et esi [?conseruare]
  [?la] nuoui ordini" (the verb form and the article do not agree with the sense: an encipherer's slip).
- 467r l. 1: "2 6 7 5 0 1 7 5 0 1 7 4 2 2 1 5 4 2 1 0 0 8" = di [7] li li basar [8]: every letter carried; reading
  "di Lilibasar" (L'Île-Bouchard), the bracket removed. "2 6 7 5 0 5 4 2 5 0 2 1 0 1 2 5 2 1 0 2 4 2 3 5 0 0 1 7" = del
  blanc a m berri: "[?in] Berri" kept (21 02 "am" where "in" is wanted).
- Done for R51: every hole has now been checked on the image (466r l. 3, ll. 7-9, l. 22-23, 466v l. 8, 467r ll. 1-2;
  the close on 467r l. 9 is the end of the sheet). Left: the opening and close (no parse), "in […]" (the place 45 21 17
  21 15 13 35 45), [?rene], [?testa] (slips), "et esi [?conseruare] [?la]".
