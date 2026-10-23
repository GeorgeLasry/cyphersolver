# Re-reading log, f. 373 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b29)

## Starting point

Reading audit (22 Oct): "decoded, not read"; neither the cipher of f. 373 nor its Brienne 13 fol. 104v clear copy was
in the repository; the content was known only from a summary. Clean-sentence share before: no text (0.00).

## What was done

1. **Record and images.** f. 373 is not a DECODE target (BnF fr. 16093, Gallica ark btv1b90074656); nothing was ever
   downloaded for it (the main checkout has no `img/` for maisse1592). Fetched at full size through openapi.bnf.fr IIIF
   (`research/reading_audit/b29_gallica.py`): views 422 (f. 373r, 6959 x 6145) and 423 (f. 373v). f. 373r: three
   clear lines, then about 42 lines of figures; f. 373v: 11 lines of figures, the clear close *Sur ce je prie Dieu ...
   Escript le vij.e jour de Novembre 1592*, the King's signature, a **clear postscript of six lines** in the
   secretary's hand, and Revol's countersignature.
2. **Existing text?** Yes: the contemporary clear copy in Brienne 13 (NAF 6984, ark btv1b100904592), located in Sept
   from Xivrey's table (pièce 226 = fol. 104v). Fetched views 109-112 and transcribed it in full for the first time
   (`f373_brienne_copy.txt`): heading at the foot of fol. 104r, the letter on fol. 104v, 105r, 105v, 106r and the top
   of 106v. The copy stops at *a mondict service./*: it does not copy the close, the date or the postscript.
3. **Alignment with the figures** (key `key1.tsv`, Tomokiyo's table; the hand writes 11 as a *u*-like ligature, 6 like
   *b*, 2 like *z*). Read on native-resolution crops and decoded by hand:
   - f. 373r l. 3 end - l. 4: `10 7 19 18 7 12 18 15 19 11 9 11 5 7 6 11 14 11 19 18 8 11 7 19 9 | 13 19 14 7 21 10 11
     16 7 6 11 16 11 17 13 19 5 10 16 11` = *dautant que cela me peut beaucoup ayder a me resouldre* (copy: *d'autant que
     cela me peut beaucoup ayder a me resouldre*).
   - f. 373r (middle, about l. 20): `1 7 4 9 18 14 13 19 16 1 7 4 16 11 9 13 12 18 4 12 19 11 16` = *faict pour faire
     continuer*; next line `15 19 11 5 11 17 11 68 11 6 4 17 14 13 19 16 16 13 4 11 12 18 1 7 4 16 11 9 13 12 18 16 11`
     = *que les ennemis pourroient faire contre* (68 = nn), then *moy et aussi que vous aiez re-*; two lines on,
     `14 19 8 5 4 11 14 7 16 10 11 5 7 10 19` = *publie par dela du*. Copy: *faict pour faire continuer ... que les
     ennemis pourroient faire contre moy et aussi que vous ayez rejetté ... ce qui se publie par dela du tiers party*.
   - f. 373r about l. 27: `14 5 19 17 10 7 10 19 7 12 9 11 6 11 12 18 7 6 11 17 7 66 7 4 ...` = *plus dadvancement a mes
     affai[res]* (66 = ff). Copy: *plus d'advancement a mes affaires*.
   - f. 373v l. 1: `10 11 18 7 12 18 5 4 12 17 13 5 11 12 9 11 11 18 7 19 10 7 9 11 10 11 9 11 18 11 12 12 11 6 21` =
     *de tant linsolence et audace de cet ennemy*. Copy: identical.
   - f. 373v l. 11 (last cipher line): `... 5 7 7 6 13 12 10 4 9 18 17 11 16 19 4 9 11` = *la a mondict service*. Copy:
     *par dela a mondict service./*.
   The copy follows the cipher at every point checked; no disagreement found. Not settled on the image: the name the
   copy writes *Vivac* (the groups between *sur* and *sa partialite* were read only in part: `17 19 16 | 19 ? ? 7 9 |
   17 7 | 14 7 16 18 4 7 5 4 18 11`, and the copy's *et* before *sa* is not in the cipher there), and *du tiers party*
   (groups after *du* not read with confidence). The cipher was not transcribed group by group (not needed for the
   reading).
4. **Reading** (`f373_reading.md`): the original's clear opening and close, the copy for the cipher, and the clear
   postscript read from the original. Spelling as the copy writes it; abbreviations expanded. Holes: [?sainement],
   [?Vivac], [?chauvez], [?vij.e]; in the postscript two partly illegible lines. Supplied word: one, *[et]* in the
   postscript. Word-by-word alignment: the reading was compared line by line with `f373_brienne_copy.txt` and the
   original's clear lines; no unbracketed word is carried by neither.
   **Look-alike alternates: 0 letters** (no reading rests on a choice between look-alike figures; the anchor decodes
   above were made with the hand's usual figure shapes, and the reading's text rests on the copy).
5. **Score** (`research/reading_audit/b17_score.py`, LANG_=fr, reading body): **0.924 (85/92)**; explicit holes
   (HOLES=1) **0.978 (90/92)**. `docs/_check_reading.py --file` on the whole file: 0.829. The unclean sentences are the
   marked holes, *contenuz/esquelz* (period spellings) and the postscript.
6. **Reader's judgement**: the sentences hold and can be translated (`f373_en.md`): the King answers Maisse's letter of
   4 Oct, waits on the Gondi/Pisany mission, urges the Venetian friends to help him and to work on the Pope, approves
   Maisse's handling of the *tiers parti* rumour, the Retz disappointment over Swiss money, Lesdiguières in Piedmont,
   Brèves and the Levant, and asks Maisse to stay; the postscript announces Joyeuse's defeat at Villemur.

## Result

Read from the contemporary clear copy (Brienne 13 fol. 104v-106v), checked against the cipher at five places with the
published key; grade A.

## Open

- *[?Vivac]* and *[?chauvez]*: single words where the copy is the only witness read; blocker: not-attempted (the cipher
  groups at these two places can be decoded from view 422 at full size if needed).
- Postscript ll. 2 and 5 (clear, secretary's hand): blocker: illegible.
- The rest of f. 370 (about 550 groups) is a separate entry and untouched here.

## 23 Oct 2026, r2f: the two open words checked on the figures

On view 422 at full size (images in the session scratchpad, `reread/r2f/`):
- *[?Vivac]*: the line after *aiez re-* reads `16 11 4 11 9 | 18 11 | 17 19 16 | 19 11 16 7 9 | 17 7 | 14 7 16 18 4 7 5 4
  18 11` = *reiec-te sur uerac sa partialite*. The name is **Verac**: 19 and 16 are written with the 1 as a dot, as
  elsewhere in this hand. No *et* before *sa* in the figures; the reading keeps the copy's *et*.
- *[?chauvez]*: the line after *peuples de la ligue pour leur tenir tousiours les esp-* reads `(14 16 4 18 22) 9 3 7 16 6
  11 22 | 11 18 | 15 19 11 | 5 11 | 10 19 9` = *(espritz) charmez et que le duc*. The word is **charmez**.
Both brackets removed from `f373_reading.md`; English: *Verac*, *to keep their minds ever under the spell*. Score after:
v2_score.py 0.946 plain (87/92), 0.967 explicit-hole (89/92); the remaining holes are [?vij.e], the supplied [et]
and the two partly illegible postscript lines.
- *[?sainement]* (not in the task, checked while there): `... 8 4 11 12 | 17 7 4 12 11 6 11 12 18 | 9 13 12 17 4 10 11 16 11
  16` = *bien sainement considerer*; bracket removed.
