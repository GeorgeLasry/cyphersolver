# Re-reading log, R9767 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b34)

## Starting point

Reading audit (22 Oct): "decoded, not read". `read_r9767.md` had the clear text and, for the two cipher passages of
f. 563r, code values with `…` between them (spelled runs unread; `pem`, `yol` not in the key). No reading file to score:
before = 0.00.

## 1. Is there a text already?

- DECODE R9767 record page (`decode/rec9767.htm`, main checkout): 2 images (ff. 563-564 as two spreads), no attachment,
  transcription or comment block. Both images opened in full: no interlinear or marginal decipherment; f. 563v (left page
  of P2) is the clear close, f. 564 the address.
- **Neighbouring records.** Fetched the record pages of R9764-R9766, R9768, R9771, R9772 with the project cookie
  (scratchpad only). R9764-R9766, R9771-R9772 are Luis Fernández (Rome). **R9768 (ff. 565-568, Alonso Sánchez, status
  "Decrypted")** had never been fetched; its four images were downloaded to the scratchpad:
  - f. 565r (P1 right): the second copy of the same letter in cipher, same text, same nulls; partly clearer (*yoh
    mostrando siepre* is written half in clear in the copy).
  - f. 565v/566r (P3): the clear close *Pareciendo nos lo mismo … De Venecia a xvj de agosto de Mil D xxiij* and the
    subscription; f. 566v/567v address and docket.
  - **f. 567r (P4 right): the contemporary decipherment**, headed *Al Rey De Alonso sanchez de xvj de agosto de Mil D
    xxiij*, a clear copy of both cipher passages with the clear words between them. Transcribed:
    `R9767_decifrado_f567r.txt`. A tear at the right edge takes the end of l. 8 (*antes d…*).
- Print: not calendared (NOTES, Sept). Nothing on cryptiana for 1523.

## 2. Alignment with the figures

Full-resolution crops of the cipher lines (P1 right, scratchpad only); every cipher group set against the decipherment's
word: `R9767_cipher_align.md`. All the codes are in the 1522 key except `pem`. Results:

- The decipherment and the figures agree word for word except three places, where the reading follows the figures:
  *porque dan los* (decipherment *por dar a los*), *una paz* (decipherment *paz*), and the torn *antes d…*, which the
  figures carry as *di-v-e-r-s-?-s* (one sign unmatched: `[?diversas]`).
- Corrections to the earlier partial decode: the run after *ho nuf ta* is ∝-n-9 = *mal* (not a code `xug`); `yol` is
  `yoh` = *causa*; the run *suf ∂ ꝏ ao ɡ y / ∝ a4 vuc* is *expremido*, not *expressado*.
- **Key value `pem` = *-mos***, adopted: it holds at all three occurrences in the August letters (*diximos* here,
  *prometiessemos* and *procuraremos* in the joint letter R9769, each confirmed by a contemporary decipherment), and its
  alphabetical slot (after `pol` *mi*, before the n-block *muy*) fits *mos*. Not written to `../sanchez1522/key_codes.tsv`
  in this batch (proposed).
- Look-alike letters: **0 letters of the reading rest on a look-alike choice**; every letter of the cipher passages is
  fixed by the contemporary decipherment, which the figures were checked against, not the other way round.

## 3. Reading and score

`R9767_reading.md`: the clear opening, the two cipher passages, the clear close. Word-by-word alignment: every
unbracketed cipher word is in `R9767_cipher_align.md` and in the decipherment, except the three figure readings noted
(carried by the figures). Supplied words: none.

| | before | after |
|---|---|---|
| reading body, b17 plain (LANG_=es) | no reading (0.00) | **0.684 (13/19)** |
| reading body, b17 HOLES=1 | — | **1.000 (19/19)** |

The six unclean sentences are period spellings (*escriuimos*, *uezes*, *danyar*, *ahunque*, *monarchia*) and names;
one query (*[?diversas]*). Reader's judgement: every sentence holds and translates (`R9767_en.md`).

## Result

Read from the contemporary decipherment (R9768 f. 567r), checked group by group against the figures; grade A.

## Open

- `[?diversas]`: one sign of the word not matched, the decipherment torn there. Blocker: illegible (tear).
