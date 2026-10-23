# Re-reading log, R93, R96, R97, R98, R99, R102, R115 (23 Oct 2026, Claude Opus 5.5; batch r2g)

## Starting point

Verification 4 (23 Oct): the seven letters demoted to decoded, not read. Their beam decodes, word-divided, scored 0.17-0.56
on v2_score's explicit-hole measure (R102 0.556, R97 0.486, R99 0.45, R96 0.429, R93 0.375, R98 0.333, R115 0.167). Their
DECODE cleartext images had never been opened.

## 1. Is there a text already? Yes, for all seven

`research/reading_audit/r2g_fetch.py` fetched every page image and attachment of R93, R96-R99, R102, R115 and of the
neighbours R92, R103, R114, R116 (record pages) with the project cookie, into the session scratchpad only (ASV images).
Contact sheets first (`sheets/R*.jpg`), then native-resolution strips (`r2g_crop.py`).

| record | cipher | decipherment (DECODE image) | other images |
|---|---|---|---|
| R93 | f. 6r | slip f. 8 (DOC_R93_D1216), 9 lines | clear letters of Jan-Feb 1568 |
| R96 | f. 81r | slip f. 80 (DOC_R96_D1255), 13 lines | covering letter Rome 19 May 1568, f. 79 ("Con questa sarà un poco di cifra") |
| R97 | ff. 88r-89v | f. 90r-v (DOC_R97_D1264, D1265), 45 lines | covering letter, f. 87 |
| R98 | f. 136r | slip f. 139 (DOC_R98_D1275), 12 lines | clear letters |
| R99 | f. 169r-v | leaf after it (DOC_R99_D1284), 27 lines | clear letters 21 June - 27 July 1568 |
| R102 | f. 306r | slip f. 307 (DOC_R102_D1308), 12 lines | covering letter docketed 27 June / 6 Aug 1569 |
| R115 | f. 641r | half-sheet (DOC_R115_D1340), 14 lines | clear letters of Jan 1572 (ff. 639, 642) |

R103 and R114 (Spagna 6/II, other Alessandrino ciphers, not in this target) were looked at too: R114 has five
cleartext images, R103 one; not pursued here.

## 2. Alignment and reading

The decipherments are fast drafts: right in substance, loose in wording (the decipherer writes "S.S." for 1010, adds
"Catholico" after Re, guesses names). Each was transcribed as written (`texts/<rec>_decifrato_*.txt`), aligned with the
figures by `reread_aless_align.py` (extended this session: `all` or `a+b` joins pages; `#` header lines skipped;
dotted group + 8 = word signs ancora / perché / acciò), and every disagreement looked at in the figures, on the cipher
image where the transcription was in doubt (R96 l. 16, R98 ll. 14-15, R99 ll. 7-8, R115 ll. 12-13). The reading then
follows the figures, the decipherment choosing between the two letters of each figure; where the figures say
something else the figures win (each reading's header lists the cases).

Code values first attested here: 2010 Imperatore (R93 "Imper.re", R96 "Imp.re"; R115 has 2010 where the decipherer
writes N.S. - left open), 4010 Re di Francia (R93, R96, R97; Lasry glossed Sua Santità, which does not fit "tra
Imperatore et [4010]"), 1020 esser (R96), 8020 avviso, 8070 Ugonotti (R97, R98), 3050 / 6030 Italia, 7040 galere,
9090 havendo (R99; fits R101's [9090] too), 6020 causa / negocio (R99, R115), 7030 Cardinale (R102), 7070
Imbasciatore (R97; with 2 = plural), dotted 1 + 8 ancora (R98, R115; R94's "anchora"), dotted 9 + 8 acciò (R115).
Not resolved: 4050, 9070 (R115 "risposta"?), 2020 (R99 twice), dotted 3 + 8 (R115 twice), [02.] 1040 at the head
of R99's Milan paragraph.

Persons identified: Count Ercole Tassone and Piali Pasha (R97, read on the figures where the decipherer left
blanks), Cardinal Diego de Espinosa (R102, the decipherer's "Card.le Spinosa"; the cipher writes 7030 alone),
Francisco de Reinoso, Pius V's scalco, for the see of Monreale (R115).

## 3. Scores

`python research/reading_audit/v2_score.py texts/<rec>_reading.md it` on the reading bodies:

| record | before (v4, beam) | after: explicit holes | plain | hole rate | words disagreeing with figures |
|---|---|---|---|---|---|
| R93 | 0.375 | 1.0 (8/8) | 1.0 | 0.011 | 4 / 98 |
| R96 | 0.429 | 1.0 (12/12) | 0.917 | 0.025 | 7 / 157 |
| R97 | 0.486 | 1.0 (38/38) | 0.868 | 0.017 | 26 / 465 |
| R98 | 0.333 | 1.0 (11/11) | 1.0 | 0.015 | 5 / 134 |
| R99 | 0.45 | 0.87 (20/23) | 0.783 | 0.056 | 15 / 249 |
| R102 | 0.556 | 1.0 (9/9) | 0.556 | 0.031 | 4 / 125 |
| R115 | 0.167 | 0.667 (8/12) | 0.583 | 0.115 | 19 / 132 |

(The disagreement counts include every bracketed hole, which the aligner skips. R102's plain score is low on period
spellings: nela, sapia, comise, facesi, apreso, deto, fato, potese, coretione.)

Look-alike alternates: not applicable in the usual sense; each figure has two letters, both its own values, and the
choice rests on the contemporary decipherment, not on sense alone.

## Still open, and why

- R93: 6 5 4 before "l'habbia". R96: the heretic's surname ([?Cuttinardo]), [?quanto]. R97: four short runs
  ("2 6" before che ho voluto, "5 2 5" in starà … avertita, "4 6 4 . 4 9 4" before mal Imbasciatore, "5 2 2 6 2 5" after
  là); 4060 5050 (Duca di Ferrara) and dotted 3 + 4 (Principe di Condé) rest on the decipherer. R98: [?possa], [?et],
  the closing group. R99: the stretch after "d'Oria" and the head of the Milan paragraph. R102: three single words.
  R115: codes 4050, 2010, 9070, dotted 3 + 8, four runs. Blocker for all: no key material (the decipherer left them
  blank or wrote words the figures do not carry; the codes occur nowhere else in the eleven letters).
- Serrano 1914 still not reached (needs physical access).
