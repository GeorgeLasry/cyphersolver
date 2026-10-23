# Re-reading log, R36 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R36_decryption.txt` (character-model segmentation of DECODE D1700, KaJo,
May 2016): clean-sentence share 0.687, hole rate 0.098.

## 1. Is there a text already?

- DECODE "cleartext" images: D1057 = f. 247, the covering letter in clear (Blois, 10 November 1588); D1058–D1059 =
  ff. 248r–v, a letter of the Duke of Savoy (signed "Il Duca di Savoia") on the marquisate of Saluzzo and Poigny — the
  enclosure the cipher calls "una lettera di sua Altezza … ne mando in questa copia". Not decipherments.
- 249r: clear docket "dup.to di li 10 novembre" (this is the duplicate of the 10 November cipher).
- Rome's decipherments (Francia 27) not imaged: physical access.
- Tempesti II, book VII §§ XXII–XXVII paraphrases the same events (Poigny's report, the King's anger, the Savoy
  ambassador, the Duke's letter to Montalto on Carmagnola); names and sense only.

## 2. Decode and repairs

- Batch decoder, then the scratch variant (`dec2.py`, extra names, 1/5 confusion), then hand re-parsing with the
  forced-alignment helper (`fit.py`), as for R32.
- Abbreviations closed by a null 8: Alt[ezza] written a + lt + 8 or a + lt + e + 8 (three times); gagliardam[ente],
  chiaram[ente] (m + 8 = -mente, as R43/R32).
- Undotted codes: 129 196 (duca di Sauoia), 221 (lettera).
- Vocabulary gaps that the figures carried: efimera, disseminando, odiosisimo, pergiuro, sganando, amorzare, bramano,
  luogotenente, stimano.
- Failures: "conosce" for the verb at 249v l. 11; "qui l'" at 249r l. 7; "dela … che" at 249v l. 15; none fit.

## 3. Image checks

Not decisive: the leaves are corroded like R32's (see the R32 log); no correction rests on the image.

## Result

Before 0.687 → after 0.738 clean-sentence share on the "## Reading" body (hole rate 0.098 → 0.089). By hand: 14
unread stretches […] (all one or two words except the opening of 249r l. 2, the clause start at 250r l. 7 and the
closing formula), 4 partly carried words, about 740 words. Every sentence carries its sense: the fever, the Savoy
ambassador's report of Poigny's failure (Savoy will keep the rest of Saluzzo, will not trust Poigny for his two heretic
brothers), the Duke's claim to act by the Pope's order, Morosini's denials, the Estates urging war, the King's
resolve, the Nemours proposal with conditions. Grade B (one figure-context reading changes a word of sense: "nondimeno"
read "non" at 250v l. 10; several single-word holes).

## Still open, and why

The opening of 249r l. 2; "[?Rouen]" at 249r l. 10; the nouns at 249v ll. 6, 15, 18; the verb at 249v l. 11; 250r l. 7
(start of "…termini … qui mi sono gouernato"); single words at 250r ll. 13, 16, 17, 19; the closing 250v l. 10. No
parse fits the transcribed figures; the image cannot be compared figure by figure (corrosion). Francia 27 would
settle them (physical access).

## Word-by-word alignment (`reread_b00_align.py`, REREAD_BRIEF step 3)

- First run TOTAL R36: 727 words, 1 supplied, 10 partly. Changed: ch'haueuo → c'haueuo (25 14 = c h, the h belongs to haueuo); bracketed [?rimasta], da[l]a, dissemin[a]ndo.
