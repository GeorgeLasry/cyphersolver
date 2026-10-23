# Re-reading log, lopehurtado R9634, R9645, R9646, R9656 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b13)

## Starting point

Reading audit (22 Oct): R9644/R9648, R9650, R9652 and R9649 read; R9634, R9645, R9646, R9656 "decoded, not read"
(61-80% of tokens valued, holes or paraphrase in most cipher sentences). The repository held the token transcriptions
(`r9634_cipher.txt`, `r9645_cipher.txt`, `r9656_cipher.txt`, `texts/R9646_transcription.txt`), the line-by-line
readings (`r96*_reading.tsv`) and the per-letter notes (`read_r96*.md`); no continuous reading.

## Step 1: is there a text already?

* **Contemporary decipherment / clear copy.** R9645: the second hand's glosses at the foot of f. 243v (ll. 13-21) only;
  none on f. 243r or upper f. 243v (checked again on the image). R9656: the faded clear copy on f. 335r; re-enhanced
  today (`research/reading_audit/b13_enhance.py`, background subtraction at blur 12 and 20): still only the right half
  of each line is legible, and it adds no word the decode lacked except confirming "por paz" and the B section. R9634,
  R9646: none on the images (R9634's three openings, R9646's one).
* **Neighbouring records.** R9644/R9648, R9649, R9650, R9652 are different letters (checked 20 Sept-3 Oct); R9649's
  subject (Ostia) gives the word in R9656 v. B1 (below).
* **Print.** CSP Spain ii has no Hurtado letter of Sept-Nov 1522; Sanuto XXXIII has no report of the Provence plan
  (both 21 Sept / 3 Oct); not repeated.
* **Better images.** DECODE has none larger (3 Oct); the RAH Biblioteca Digital sits behind a proof-of-work bot check
  (not to be bypassed). Blocker for the sign-level doubts below: needs-physical-access (or Daniel in a browser).

## Step 2: read on the images

The DECODE images are in the main checkout (`C:\Users\dbour\cypher\targets\lopehurtado\img\`, 3256-3552 px per
opening). The unread stretches of R9646 (runs 3-5), R9656 (ll. 6, 9, 13-16, f. 334v), R9645 (f. 243r ll. 1-17, f. 243v
ll. 1-10) and R9634 (f. 14r) were cropped at 1-4x (`research/reading_audit/b13_crop.py`; crops in the scratchpad only).
The look-alike lessons of lopehurtado1523 (b07: ß-like a written ʇʇ; y ʇʇ = g; m̶ = f/c) were tried on every unread
word with ʇʇ: none gives a word here, so they do not transfer to these 1522 transcriptions. What the images settle
(`texts/<doc>_corrections.tsv`, corrected copies `texts/R9645_cipher_corrected.txt`, `texts/R9656_cipher_corrected.txt`):

* **The crossed t-form (t) is m, not ϑ (t)** in four words: R9645 r01 `ϑ&t7 xm` = *tomado* (was ϑ8ϑ7, unread), R9656
  v01 `8&tßɣ̊Ho4` = *[?tomaran]*, R9656 l6 (last sign), R9646 run 3 *de-[?cima]*.
* **The 8-form stands for the t-sign ϑ** (the 8/ϑ confusion of read_r9649.md) in R9656 vB1 `&δϑα7` = o-s-t-i-a,
  *[?Ostia]* (was ∂∂8∂7, unread): the fortress R9649 asks the Emperor to write about; and in R9645 r05 `∂&ε8m`.
* **R9656 v01 is `zuc`** (1524 assi-), not `zil`; **R9656 l9 opens with the run mark Ꮒ**; **R9645 v07 `xod ɣ3&` = fecho**
  (was `xod yzα`), as in R9656 vB4.
* **Context readings, bracketed** (each carried by most of its signs, the rest by the sense): R9645 r05 *los dineros del
  feudo que el papa Alexandro le [?solto] con el [?casamiento] de su [?fija]* (Alexander VI lowered Ferrara's census at
  Lucrezia Borgia's marriage, 1501); r07-08 *con [?ningun] [?principe] ni [?señoria] pudiese confederarse*.
* Unchanged after the look: R9646 run 4 `ð∠89&Ho` and run 5 `ð∠47` (the same unkeyed looped sign opens both), `zip`,
  `zob`, `ʃof`; R9656 `ɲ4∠&ɣ̊t`, `ɣαδ8`, `teɡ∂ ϯ∠8ɣ̊oo`, `ϙ8`, `8x&`, `ßϑ7`, `30`; R9645 `#ʇʇHoε97`, `xωt74`, `tec`, `zuf`,
  `ʃen`, `ɣ7∠8ϑ9Ho`, `8&ɣ̊98`, `ϑωε7ϙ`; R9634's ~45 single-occurrence codes and its spelled place names. No sibling
  carries any of them with a crib (codes pooled over 21 letters on 3 Oct).

## Step 3: alignment

Each reading was written from its decode line by line; every cipher word is plain only where every sign carries it,
`[?…]` where a sign or the value is probable or the word rests on context, `[…]` where nothing reads, `[word]` for the
one supplied word (R9645 *capitula[cion]*, *deservidor[es]*, R9656 *dinero[s]*, R9646 *la[s]*). The alignment notes are
in each `<doc>_reading.md`. Changes from the old line readings: R9656 l5 "cerca" withdrawn (it rested on the copy's line
position, which the enhanced copy does not show); R9645 r13 "a pena" is the null group `ɣto ʃta`; R9645 v08 "en fe-" is
*he [dicho]* read with `yuc` left out.

## Step 4: result (clean-sentence share of the reading body, `research/reading_audit/b13_score.py`, LANG_=es)

| doc | before | after | state | why |
|---|---|---|---|---|
| R9646 (f. 252r, Nov 1522) | decoded, not read | 0.727 on the whole letter | decoded, not read | the clear dominates; of the five cipher runs, 1-3 read (Ferrara, *[?decima]*), runs 4 and 5 keep 2 and 4 holes: what the Pope feared and what the offer was are lost |
| R9656 (ff. 334r-v, 22 Nov 1522) | decoded, not read | 0.564 | decoded, not read | ll. 4-6 and 13-17 break on single-occurrence codes and spelled words; f. 334v now reads (*lo de [?Ostia]*, *[?tomaran]*) |
| R9645 (ff. 243r-v, Nov 1522) | decoded, not read | 0.528 | decoded, not read | f. 243r now reads to l. 12 (the Ferrara capitulation terms); r13-r17 and upper f. 243v break on ten unkeyed groups |
| R9634 (ff. 14r-16r, Genoa 13 Sept 1522) | decoded, not read | 0.506 (clear-heavy) | decoded, not read | about 45 codes seen once and the spelled place names: holes in most cipher sentences |

## One sentence per document (partial readings)

* R9646: *como el papa era concertado con el duque de Ferrara* — "that the Pope had come to terms with the Duke of Ferrara."
* R9656: *que esta muy sospechoso el papa que de alla se le haya mandado lo que ha fecho* — "for the Pope is very
  suspicious that he was ordered from over there to do what he has done."
* R9645: *que abia tomado assiento con el duque de Ferrara* — "that he had reached a settlement with the Duke of Ferrara."
* R9634: *estan [?muertos] de miedo del saco de Genova* — "they are [?dead] with fear of the sack of Genoa."

## What stays open and why

* The unread codes (R9646 zip, zob, ʃof; R9645 tec, zuf, ʃen, tep; R9656 30; R9634 ~45 groups) occur once in the 21
  letters of this hand with no gloss, copy or print: **no-key-material**.
* The spelled words with one unkeyed or look-alike sign (R9646 `ð∠89&Ho`, `ð∠47`; R9645 `#ʇʇHoε97`, `ɣ7∠8ϑ9Ho`; R9656
  `ɲ4∠&ɣ̊t`, `ϯ∠8ɣ̊oo`; R9634's place names): the signs are at the limit of DECODE's 1,700 px per folio and the RAH
  images are behind a bot check: **needs-physical-access** (a better image from the RAH).
* R9656's f. 335r clear copy: the left half of every line is faded beyond background subtraction: **illegible**.
