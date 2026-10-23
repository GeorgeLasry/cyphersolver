# Louis XIII to Brûlart de Léon, ambassador in Venice, 1615 and 1617 — BnF fr. 18043 f. 83–84, fr. 18044 f. 109–110 (DECODE R2785, R2786) — NOTES

Status: in progress (write-up not refreshed).

**23 Oct 2026, siblings step (escalation 0a).** Neighbours opened; nothing gives a decipherment or key of the residue,
but two clear companion letters confirm two doubtful names, and the R2785 spaced-sign lines are now judged nulls.
- DECODE R2782-R2789 (project cookie): R2782/R2783 Mazarin to Le Tellier 1652, R2784 no record, R2787 Villeroi to
  Henri III 1577, R2788/R2789 to Philibert du Croc 1567. Unrelated; the Brûlart letters have no DECODE siblings.
- Gallica, openapi.bnf.fr IIIF (fr. 18043 `btv1b90619879`, view = folio + 1, each view a spread f. n-1 v | f. n r;
  fr. 18044 `btv1b9061986w`, view = folio + 5). Images in the session scratchpad only.
  - fr. 18043 f. 80v: end of a clear French report (8 Oct 1615). ff. 81r-82r: clear Spanish copies of the Marqués de la
    Hinojosa's letters from Milan to Claudio Marini in Turin (Sept-Oct 1615). f. 82v blank.
  - fr. 18043 ff. 85r-86r: Puysieux's autograph **clear** letter to Léon, "De Poitiers ce x6 Septembre 1615" (same "x6"
    as R2785): Mantua's harshness to his rebels, Marini to retire to Genoa, "M. Mansau qui est a Rome" to go and reside
    with Savoy, the princess's illness holding the court. Address and docket on f. 86v.
  - fr. 18043 ff. 87r-v: a further Louis XIII letter to Léon, Poitiers, late Sept 1615 (day cut at the gutter, "xx…"),
    **in the same cipher with a full interlinear decipherment** ("L'obstination", "du duc de Mantoue", "au sr Marini de
    se retirer a Gennes", "Don Pedro di Toledo a Milan"); "Je partz de ceste ville" after the sister's illness, so later
    than R2785. Not on DECODE (a DECODE queue candidate). It has no spaced-sign lines.
  - fr. 18044 ff. 107r-108r: Puysieux's clear letter (secretary's hand), Paris 26 July 1617, answering Léon's of the 4th:
    Venice, the Savoy accord, Lesdiguières, Don Pedro. ff. 111r-v: Puysieux's autograph clear letter, Paris "xxv" July 1617:
    Gueffier's arrival, the Grisons, "la retraitte du Padavin". f. 112r blank.
- Applied: R2785 "[?Manjeaux]" -> **Manseau** (long s on the image; Puysieux's "Mansau qui est a Rome"); R2786
  "[?Padavin]" -> **Padavin** (Puysieux's "du Padavin"). R2785's spaced-sign lines (f. 83v rows 17-18, f. 84r row 2) are
  **judged nulls** and left out of the reading: no gloss, no French under Tomokiyo's key, doubled signs French does not
  give (g g, ʜ ʜ, tt ʃʃ, g g ʜ ʜ ʜ), the clear text closes over them in one sentence ("... du coste de Soissons, esperant
  que mon auctorite sera en fin recognue de ces princes par amour ou par force", the f. 84r line falling between "ces
  princes" and "par amour"), Tomokiyo's DECODE note, and the companion f. 87 letter has none. This is a judgement from
  the text, not a key value.
- Scores: read_share (v10_relabel.share) R2785 0.962 -> 0.971, R2786 0.959 -> 0.961; v2_score explicit holes R2785
  0.902 -> 0.927, R2786 0.902. Both stay *read in part* (R2786 rows 9-11; three R2785 glosses).
- Not settled: the Puysieux letters give the sense of R2786's Savoy paragraph (Savoy to use the French forces for an
  accord, not to prolong the war) but not the words of rows 9-11, so nothing is filled there. The R2785 glosses are no
  clearer on the Gallica full-resolution images. R2785's date: the day is written "x6" (read 16 on 22 Oct), Tomokiyo has
  26, the docket on f. 84v reads "15 sep. 1615" or "25"; Puysieux's companion letter has the same "x6". Left at 16, open.
- `texts/R2785_align.tsv` runs 25-26 now say "nulls" (re-running `research/reading_audit/b17_brulart_align.py` would
  overwrite that column).

23 Oct 2026, consistency pass: class **read -> read in part**. The read bar needs every document read in full; both letters keep unread passages (R2785's ~60 spaced signs at the foot of f. 83v / head of f. 84r, R2786 f. 109v rows 9-11 outside the glosses) and three illegible glosses, so `documents[].read` is *read in part* for both and the profile's 1.0 counts letters whose sentences read, not signs. The siblings step was done the same day (block above).

Both letters read 22 Oct 2026 (re-read b17) from their contemporary interlinear decipherments, checked against Tomokiyo's key: `texts/R2785_reading.md`, `texts/R2786_reading.md`.

**22 Oct 2026, reading audit** (George Lasry's test): Tomokiyo's key is on both DECODE records, but his page gives the key and remarks on undeciphered symbols, not the letters, and nothing of either letter is transcribed here. Both are *decoded, not read*; class already solved -> not read, method -> not solved. The R2785 page image shows contemporary decipherments over most cipher runs, so the letters are workable with his key.

**22 Oct 2026, re-read (REREAD_BRIEF, batch b17).** All four page images of each record fetched with the DECODE cookie
(`research/reading_audit/b17_fetch.py`; scratchpad only). Both letters carry a contemporary interlinear decipherment over
most cipher runs. Clear text and decipherments transcribed, every run aligned with its gloss and checked against
Tomokiyo's key (`texts/R2785_align.tsv`, `texts/R2786_align.tsv`); log: `texts/R2785-R2786_reread_log.md`.
- R2785 (Poitiers, **16** Sept 1615, not 15): Louis XIII disapproves of Mantua's harshness to his rebel subjects, fears
  Savoy will use it to renew the quarrel, suspends his good offices, orders Marini to withdraw to Genoa, is held at
  Poitiers by his eldest sister's illness. _check_reading.py on the body 0.854. Read.
- R2786 (Paris, 25 July 1617): Venice should take the openings offered to end the war; Savoy must use
  the French forces to conclude a good accord; the Grisons, Padavino's expulsion, Gueffier's report on the Leagues.
  0.863. Read. The decipherer's "incommoditez" is "inconvenients" in the figures; "en mesme temps" (no gloss) decoded
  with the key.
- θ (not in Tomokiyo's table) is a null. Unread: R2785's three spaced-sign lines (no gloss, no French under the key;
  Tomokiyo: probably nulls), parts of R2786 f. 109v rows 9-11, three cramped glosses on R2785 f. 83v.

Split on 14 Oct 2026 from `louis1615` under the one-key rule (George Lasry, 14 Oct 2026). The old entry (catalogue
191) grouped these two letters with Louis XIII's letter of 1631 to Melchior de Sabran because DECODE lists all three
with Louis XIII as author. The Sabran letter is in another cipher, solved by George Lasry, with its own entry:
[`targets/sabran1631/`](../sabran1631/NOTES.md), page `sabran1631.html`. The old slug `louis1615` is a stub page
pointing to both.

**Outcome: read from existing decipherment.** Satoshi Tomokiyo reconstructed the key of the Brûlart de Léon cipher
(1615–18) and read both letters with it (DECODE records uploaded August 2021, status "Partially decrypted"); his
key is on cryptiana louisxiii.htm and attached to both records. Nothing about the text is added here and his key was not
re-applied. Session 2026-09-21; split and written up 2026-10-14.

## The letters

| record | shelfmark | date | route | DECODE status |
|---|---|---|---|---|
| R2785 | BnF fr. 18043 f. 83–84 | Poitiers?, 15 Sep 1615 | Louis XIII (countersigned Brûlart de Sillery) → Léon Brûlart, ambassador in Venice | Partially decrypted |
| R2786 | BnF fr. 18044 f. 109–110 | Paris, 25 Jul 1617 | same | Partially decrypted |

- DECODE lists 3 pages for each record; one image of each was fetched (`IMG_R2785_I17344_P1.jpg`,
  `IMG_R2786_I17348_P1.jpg`, git-ignored in the main checkout, `C:\Users\dbour\cypher\targets\louis1615\decode\`).
  The R2785 image is a text page: clear French with cipher runs, and most runs carry a decipherment written above
  them in what looks like a contemporary hand ("Marini", "retirer a Gennes", "domestiques", "aucun ombrage"). The writer is still
  held in the town by the illness of his eldest sister, which fits the court at Poitiers in September 1615. The R2786 image
  is the address leaf ("A Mons. de Leon conseiller en mon conseil d'Estat et mon ambass. a Venise").
- The DECODE files `DOC_2785_…png` and `DOC_2786_…png` are one image (same MD5): Tomokiyo's key table "Brulart de
  Leon's Cipher (1615-1618)". Alphabet of letter-like signs with two or three homophones for most letters; numbers
  with a virgule for words (2 amytie, 20 de, 97 pour …); numbers with an overbar for syllables and short words
  (5 pre, 7 que, 18 roi, 37 vous …); dotted vowels for princes (ö duc de Savoye, ä duc de Mantoue); a delete sign
  and a repeat sign.
- Residue, from Tomokiyo's notes on DECODE: R2785 "Some passages are not deciphered … They may be partially or totally
  nulls"; R2786 "Some symbols are not deciphered. At least some of them are insignificant (because of cancelling
  symbols)".
- The volumes hold many more letters to Brûlart de Léon partly in cipher, from Louis XIII, Marie de Médicis and
  Puysieux (fr. 18043, 1615–16; fr. 18044 ff. 20, 168, 184, 283, 315, 1617–18). The leaves next to R2785 and R2786
  were opened on 23 Oct 2026 (siblings block above); the farther cipher letters (fr. 18044 ff. 20, 168, 184, 283, 315)
  were not.

## Sources

- Tomokiyo, "French Ciphers during the Reign of Louis XIII", https://cryptiana.web.fc2.com/code/louisxiii.htm,
  "Brûlart de Léon" (the key). Copy in the main checkout's `targets/louis1615/` (git-ignored).
- DECODE R2785, R2786 (uploader Tomokiyo, Aug 2021): key file and notes on the undeciphered residue.

## What was done

1. 21 Sept 2026: fetched the two record views and one image of each with the shared DECODE cookie.
2. 21 Sept 2026: fetched louisxiii.htm; the key and the reading are Tomokiyo's. The entry was closed without applying
   the key.
3. 14 Oct 2026: split from louis1615; the R2785 image and the key file were looked at to describe the letter.

## Still open (here)

Tomokiyo's reading leaves some symbols undeciphered, probably nulls or cancelled signs (his notes). This project
made no transcription and did not apply his key, so it has no check of its own and no sign-level replay. The other
two pages of each record were not fetched.

## Escalation (record)

- [x] siblings: 23 Oct 2026, DECODE R2782-R2789 (unrelated) and the Gallica leaves next to both letters opened: Puysieux's clear companion letters (fr. 18043 ff. 85-86; fr. 18044 ff. 107-108, 111) confirm Manseau and Padavin; a further glossed Louis XIII letter in the same cipher (fr. 18043 f. 87, not on DECODE); no decipherment or key of the residue; R2785's spaced-sign lines judged nulls
- [x] clear-pages: contemporary interlinear decipherment on the R2785 text page
- [x] known-keys: Tomokiyo's 1615–18 key is the key of these letters
- [x] print: louisxiii.htm checked
- [x] key-rebuild: the key exists (Tomokiyo); 22 Oct 2026 θ identified as a null, no other change
- [x] retry: 22 Oct 2026 (b17) the pages fetched, decipherments transcribed and checked with the key; both letters read

## Remaining gaps

- R2786 f. 109v rows 9-11 / f. 110r row 1 outside the glossed words - blocker: no-key-material; no contemporary decipherment, no French under Tomokiyo's key with θ/φ as nulls, the companion Puysieux letters give the sense only (Tomokiyo: probably nulls)
- R2785 f. 83v: three cramped glosses ("m'est possible", "[?lors] de [?propos]", "l'Equidray", the gloss after "ont este") - blocker: illegible; blotted on the DECODE and the Gallica full-resolution images, signs beneath ambiguous in the key, no sibling repeats the clauses

Closed: R2785 and R2786 had no plaintext in the repository; closed 22 Oct 2026 (b17), both read, texts/.
Closed 23 Oct 2026 (siblings): R2785 f. 83v rows 17-18 and f. 84r row 2, judged nulls (see the siblings block); the clear name "[?Manjeaux]" = Manseau; R2786 "[?Padavin]" = Padavin.
