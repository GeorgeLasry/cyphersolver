# Re-reading log, R94, R95, R100, R101 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch "aless")

## Starting point

Reading audit (22 Oct): the four letters "decoded, not read": the beam search under Lasry's polyphonic key corrupted
words mid-sentence (R94 "liberagemptume", R95 "desersaleaniosina", R100 "dingaeldetpie ... ??????", R101
"unmannifestsobismain"). _check_reading.py on the old decryption files: 0.75, 0.89, 0.78, 0.81 (inflated by the
nomenclator words).

## 1. Is there a text already?

- **DECODE images.** Each record carries, besides the cipher, "cleartext" images of the neighbouring folios
  (R94: 18, 037v-052r; R95: 10, 053r-061v; R100: 6, 278v-282v; R101: 11, 286v-293v). All fetched with the DECODE
  session cookie (targets/bordeaux/decode/cookie.txt; request form as in sauli1579's log) into the session scratchpad
  only (ASV images). Contact sheets first, then native-resolution strips.
  - **R94**: f. 45r is the contemporary decipherment (rough hand, no heading, 14 lines). The covering letter in clear,
    Rome 7 Nov 1567 (f. 44r), ends "Con questa un poco di cifra"; so R94 dates from 7 Nov 1567, not 1568.
  - **R95**: f. 58r is the decipherment (15 lines, a fast draft with strikings and words above the line).
  - **R100**: the decipherment is written under the cipher on the cipher page itself (f. 280r, 7 lines); the record's
    metadata says "Inline Cleartext Yes". Clear letters around it: 25 April and [..] May 1569.
  - **R101**: no decipherment among 286v-293v (clear letters, June-July 1569); none on the cipher pages, which are
    burned through by the ink.
- **Print.** Serrano, *Correspondencia diplomática entre España y la Santa Sede durante el pontificado de S. Pío V*
  (1914, 4 vols.): not on archive.org (the "correspondenciae0Ncath" items there are the Felipe III nunciature, 1960);
  HathiTrust full text returns 403 from here; Google Books API quota exhausted. Serrano's *Liga de Lepanto* (1918-19,
  on archive.org) covers 1570-73, after these letters. So print is still not checked: blocker = access.

## 2. Alignment of the decipherments with the figures

`reread_aless_align.py` aligns a reading with one page's figures by dynamic programming: each figure 1-9 may give
either of its two letters, 0 is a null, X0Y0 a code; a mismatch, a figure left over or a letter with no figure each
cost 1. It prints every word with its figures and marks disagreements. First pass on R94 with the decipherment as
written: 74 of 171 words disagreed. Each disagreement was looked at; most were the key, not the decipherer:

| finding | evidence |
|---|---|
| 9 also = the syllable "con" | con bona, con V.S., concesso, concesse, con forze; R95 conscientia, concessione, si contenta; R100 comprende (con-prende) |
| dotted group 0^.0 (00.) = "et" | occasione et invitato, ampliarli et di usarli, gratie et li privilegii, gagliarda et viva |
| a doubled letter is enciphered once | occasione, delli, essi, interesse, hanno, allegati, predecessori |
| X0Y0 codes are often written X0Y | 2 0 9 (che) + 1010, 5 0 2 (per), 3 0 2 0 / 3 0 2 |
| 3 0 9 without dot = qua | li quali, il quale, di qua |
| dotted 0 = z | forze (3 5 7 0^. 6), terzo, patienza, senza (R101) |
| 3060 = -mente | libera+3060 (decipherer "apertamente"); R95 particolar+3060; "4 3060" 9 times in the file |
| 6090 is a demonstrative, not only "quel" | queste materie, questa santa sede, questo |
| 1040 = lettere | R95 "alle lettere sue del mese passato" (Lasry: "Regina di Francia?") |
| 3020 = quando | R94, R95 ("quando succedesse"), R100 (3 0 2), R101 |
| 4040 = Milano (R95); "come" in R94's decipherment | conflicting; R94's use rests on the decipherment only |
| 4020 = come | R95 "come n'è avvenuto", R101 "come li suoi ministri dicono" |
| 4080 = et, 5070 = Imbasciatore, 6060 (6 0 6) = Inquisitione | R100 |
| 6050 = Imbasciatore (di Francia), 7070 with it | R95 twice |
| 8090 = havere (Lasry "sauere?") | R101 "possano havere notarii" |
| dotted 4 + 8 = perché | R95 twice (decipherer "p[er]chè") |
| 2 0 9 = "chi" as a syllable | R101 chinea, Chiesa (twice), chiarire; R94 anti+che |

With these, disagreements fell to 12 of 172 words (R94), 21 of 190 (R95, mostly where the draft is illegible), 6 of
79 (R100). Where the decipherer and the figures differ, the figures were followed (R94: liberamente not apertamente,
N.S. not S.S., queste materie, "si haverà" not "si rimette", "de fatto" not "et fatto", "non con forze" not "non ha
forze", "et viva" which he skipped; R95: si contenta, nova concessione, lasciò, ne doleria; R100: quella, sia
rimessa, sì che).

## 3. R101 on the figures

`reread_aless_decode.py` re-runs the beam search with the extended key (9 = con, 00. = et, X0Y codes, the new code
values, doubled letters). The R101 transcription had a stray comment line read as five illegible items (fixed:
texts/R101_transcription_corrected.txt). The new decode gave continuous sense for most of the letter; then word by
word on the figures (both letters of each figure written out) and on the image for the doubtful places: "fisco" (3 2
5 8 5, not "gioco"), "aderendo", "censo" (8 6 6 5 5), "devolutione" (7 = d), "Iulio secondo et Iulio terzo, sante
memorie", "levando la obedientia", "onde né li vescovi né loro vicarii possano havere notarii che li servano né
esecutori", "regii carcerati", "se tale è la mente di S.M.", "che liberi sua santa Chiesa", "il quale suole ben
permettere", "chi la travaglia non ne sarà senza castigo". Images: rows 1-2 of 291r zoomed at 3x for the two burned
places (no better reading). Final alignment: 158 of 168 words (291r) and 73 of 74 (291v) carried.

## Result

| record | before (audit) | after: clean-sentence share of the reading | rests on |
|---|---|---|---|
| R94 | 0.75, decoded, not read | 1.00 (16 sentences), 2 gaps | decipherment f. 45r + figures |
| R95 | 0.89, decoded, not read | 0.94 (18), 4 holes | decipherment f. 58r + figures |
| R100 | 0.78, decoded, not read | 1.00 (7), none | decipherment f. 280r + figures |
| R101 | 0.81, decoded, not read | 0.84 (19), 5 holes, 3 codes | figures, extended key |

(_check_reading.py's score_text on the "## Reading" body of each texts/R*_reading.md.)

## Still open, and why

- R94: the stretch "9 0 4 0 2 0" before S.M. and the verb "6 2 4 7 6" after "comincia": the decipherer left the
  first as dots and guessed the second ("negare", "giovare"), neither fitting; no other text.
- R95: [08.] (the Crusade?), "co[…]" after "detto", the person [3.] who pressed the request, the verb "[?fece]" (3 6
  7 6): the decipherer's words are illegible at those places; unlisted dotted groups.
- R101: three places under burns or a hole in the paper (row 1 twice, row 14 one group), "[?Sora]" (5 5 7 4), codes
  9090, 6020, 8020: illegible / no key material.
- Serrano 1914 not checked (access).
