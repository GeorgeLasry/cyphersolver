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

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`; the pages are clean), cancellation strokes looked for (none), the figures parsed (`r2p_parseall.py`).
Filled:
- 249v l. 10 "dala quale": "8 26 21 50 21".
- 249v l. 11 "si arguisce il contrario": "2 00 40 37 17 34 5" (34 = sc), heading l. 11.
- 249v ll. 12-13 "tocando": "6 91 25 21 | 01 26 191".
- 249v l. 16 "diseminando": the image has "... 20 17 01 21 01 26 9" (DECODE drops "2 1 0 1"), single s as written.
Left, with blockers:
- 249r l. 2 "[…] con l": "0 1 9 7 5 2 4 7 9 8" (best parse "noicsto"). Blocker: no-key-material.
- 249r l. 7-8 "è capitato […] l ambasciatore": "7 3 0 2 1 7 | 2" (best parse "iumia"). Blocker: no-key-material.
- 249r l. 10 "cose di [?Rouen] per il": "8 0 0 9 1 3 7 3 5 0 5 8" (best parse "nouel"). Blocker: no-key-material.
- 249r l. 14 "Pugni che [?la] conclusione era": "7 1". Blocker: no-key-material.
- 249r l. 15 "che sua Alte[zza] non poteua": "8 2 2 7 3 5 8" (best parse "lte"). Blocker: no-key-material.
- 249v l. 1 "[?rimasta] malisimo sodisfata": "4 7 2 1 2" (best parse "sta"). Blocker: no-key-material.
- 249v l. 2 "sodeto partito da[l]a Regina Madre": "2 6 2 1 2" (best parse "da"). Blocker: no-key-material.
- 249v l. 6 "posto questo […] di sua": "2 2 1". Blocker: too-short.
- 249v l. 15 "nei popoli […] che di": "2 6 3 5 0 5 1 5 1" (best parse "deltr"). Blocker: no-key-material.
- 249v l. 16-17 "di Sauoia […] haueua fata": "1 7 1 5 0 | 4 1 7 4 0 2 2 9 1 9 6" (best parse "ilhismaoot"). Blocker: no-key-material.
- 249v l. 18 "tuta la […] hauendo tuti": "5 1". Blocker: too-short.
- 250r l. 7 "del suo […] termini […]": "8 7 6 1 7 1 9 5 7" (best parse "tioei"). Blocker: no-key-material.
- 250r l. 8 "[…] termini […] qui mi": "1 7 1 9 4 1 7 0 8" (best parse "iohp"). Blocker: no-key-material.
- 250r l. 13 "animi arabiati […] da tute": "4 5 1 7 2 0 7" (best parse "siap"). Blocker: no-key-material.
- 250r l. 16-17 "da alcuni […] et che": "3 2 | 1 4 7" (best parse "uast"). Blocker: no-key-material.
- 250r l. 17 "che molti […] stimano che": "1 5 2". Blocker: too-short.
- 250r l. 18 "gli altri […] altro non": "9 1 7". Blocker: too-short.
- 250v l. 8-9 "Nemurs nondimeno [?uorrà] altre conditioni": "3 7 3 9 1 | 0 0 2 1 2" (best parse "uuorra"). Blocker: no-key-material.
- 250v l. 10 "mai acetate […]": "8 4 2 2 7 9 6 167^. 0 0 111^. 9 2 7 0 1 2" (best parse "bltque[u.s."). Blocker: no-key-material.
Result: 4 holes filled; 19 left, each with its blocker.
