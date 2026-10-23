# Re-reading log, R9653 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b23)

## Starting point

Reading audit (22 Oct): "decoded, not read". `read_r9653.md` had the clear middle of f. 299r (the Rhodes news), the
foot cipher paragraph read only to "cartas de Francia de xxvi y xxvii del passado de …", and "a cipher paragraph of
six lines at the head" called illegible (ink bleed). No reading file to score.

## 1. Is there a text already?

- DECODE R9653 re-fetched logged in (`research/reading_audit/b23_fetch.py`): 2 images, no attachment, transcription or
  comment block. Both opened in full.
- **The "head paragraph" is not on f. 299r.** P2 (left page) is f. 299v, and it carries an eleven-line cipher passage
  in a clean hand, followed by the clear close (*Nuestro señor la imperial vida …, De Venecia a xx de noviembre de
  DXXII*), the subscription and the signature. The lines at the head of f. 299r are its mirror-image bleed-through.
  So the cipher of the letter is the two lines at the foot of f. 299r continued by the eleven of f. 299v, about
  160 tokens, fully legible.
- No decipherment: nothing interlinear or marginal on either page. f. 300r (P2, right) shows only faint offset/
  bleed-through of a second copy of the letter (f. 300v, not imaged), with the foot cipher repeated in cipher: a
  duplicate, not a decipherment, and not legible at the top. R9654 (ff. 301-302, same date, "Inline cleartext: Yes")
  has no images on DECODE. R9655 (f. 303) is a different cipher letter of 24 Nov 1522 ("es treslada de otra"), no
  decipherment.
- Print: not in CSP Spain 2 (NOTES, 21 Sept check). Not in Tomokiyo's article (stops at R9632).

## 2. Reading on the image

Crops of each line at 1.6-2.6x (`research/reading_audit/b23_sanchez_strip.py`; crops in the scratchpad only).
Transcription and decode line by line: `R9653_cipher.txt`. Sign values used, beyond `alpha.py`:

| sign | value | where it holds |
|---|---|---|
| `∝` (sideways 8) | m | *fundamento*, *mentiras*, *Geronimo*, *Manuel*, *Sangerman*: five words, every occurrence; Tomokiyo's table has it under m |
| `Ꝁo` / `Lo` | s **or** t (look-alikes) | t in *tienen*, *este*, *tierra*, *Bretanya*, *siguiente*; s in *ingleses*, *dos*, *mentiras*, *llegase*. Tomokiyo circles the two forms together; the hand does not separate them, so every such letter is counted as a look-alike below |
| `ꞔ`, `∂` | e | *dieron*, *tierra*, *Sanger-*; *este*, *siguiente*, *detenido* |
| `g#` / `ǂ#` | u / v | *estava*, *traves*, *nuevas*, *siguiente*, *Manuel*, *toda-via*, *fundamento* |
| `ẗ4` | n | *tienen*, *Bretanya*, *nuevas*, *sin*, *don*, *Ioan*, *Manuel*, *passando* |
| `q` | t | *traves*, *fundamento*, *mentiras*, *detenido* (Tomokiyo's t; alpha.py's q = s from R9605 is the double-barred plural sign) |
| `3` | d | *perdieron*, *dieron*, *fundamento*, *dia* |
| `∞` (bold) | g | *ingleses*, *Geronimo*, *siguiente* |
| `ƀ` | b | *Bretanya* |

Codes used for syllables, as R9605 showed: `mog`+n+`vuc` *passando*, i-n-g-l-e+`gad`+s *ingleses*, `geg`+g-u-i+`vog`+t-e
*siguiente*, `xig`+t-e+`nef`+`vuc` *detenido*, `vuc`+n *don*, M-a-n-u+`veg` *Manuel*, `fef`+v-i-a *todavia*,
`mod` in n-a+`mod` *naos*, `vog` in *tienen*, *fundamento*, *mentiras*.

Key values (none written to `key_codes.tsv` in this batch; proposed):

- adopted on a contemporary text: `feb` = *tanto* (R9635's decipherment on f. 22r, found in this batch); here
  *detenido tanto por …*.
- sense and slot only, flagged for review: `fef` = *toda* (between `faf` todo and `fug` tres); `ref` = *Italia*
  (between `rec` Inglaterra and `rof` justa?); `zub` = *Adorno* (first slot of the z-block before `zid` a(h)un; Girolamo
  Adorno was at Venice with Sánchez that winter, CSP Spain 2 no. 515).
- open: `xug` (en la …), `zi`, `tac` (R9635 suggests *tenian?*, which does not fit here), `lud`, `qef`, `sob` (twice,
  a place: *llegase en …*, *alli en …*), `ca`, `nu`+s; the run b-r-a-v-s-a after *el rey de Francia*; `çi xe` at the
  right edge of l. 8; a stain at the end of l. 9.

**Look-alike letters in the reading: 15** (11 `Ꝁo`/`Lo` read s or t by sense; 1 `8` read r in *Sanger-*; 2 `⊥` read r in
*mentiras*, *espera-*; 1 `ꞵ` read rr in *tierra*).

## 3. Alignment

Every unbracketed cipher word of `R9653_reading.md` is a (b) item of `R9653_cipher.txt` (checked by hand, 147 words;
the clear text is the image's). Supplied words: none. *ahun* for `zid` follows the clear hand's spelling of the same
word (*tienen ahun mejores nueuas*).

## Result

| | before | after |
|---|---|---|
| reading body, b17 plain | no reading file | 0.368 (14/38) |
| reading body, b17 HOLES=1 | — | 0.842 (32/38) |
| cipher passages only, b17 plain / HOLES=1 | — | 0.091 (1/11) / 0.455 (5/11) |

The whole-body figure passes the bar only because two thirds of the letter is clear text. The cipher, which is what
the decoded-not-read label is about, builds sentences in its first paragraph (*dize que passando los ingleses a su
tierra se perdieron dos naos dellos …, y los otros dieron a traves en Bretanya … Nuevas sin fundamento*) but not in its
second (Adorno, the protonotary, Juan Manuel: seven open code groups in four sentences). **Kept "decoded, not read"**;
the reading stays as a partial reading.

Blocker for what is open: no-key-material (eight code groups absent from Tomokiyo's table, each in a single context
here; no decipherment of this letter is bound or imaged; the second copy on f. 300v and R9654 are not imaged:
needs-physical-access for those).
