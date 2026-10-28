# Malicorne to Henri III, Niort, 21 April 1586: cipher letter in BnF fr. 15572 ff. 162–164 (Malicorne's cipher)

Status: in progress (26 Oct 2026: all six pages read as far as the key allows; the label checks on f. 162r, f. 163r
and canvas 171 done after deskewing (Brackx, issue #92, 26 Oct 08:17): no shape split resolves the remaining
two-valued labels; open only for a second deciphered letter in this key).

**Read in part, 24 Oct 2026.** Contributed by Michael Brackx (@brackxm, issue #92, 22–23 Oct 2026), with Claude Code
(Claude Opus 5.5). Method: **read with known key**: Tomokiyo's key table ("Malycorne's Cipher", Cryptiana henryiii
page), corrected by Brackx and checked against the contemporary margin decipherment on f. 163r. f. 163r stretch A
reads as one sentence confirmed by the margin (read_share 0.727, read in part); f. 162r (0.622) and f. 163r stretch B
(0.694) are *decoded, not read*; the other four pages (f. 162v, canvases 171 and 172) are *decoded, not read*
from Brackx's raw aligned decode, with no reading built yet.

Same volume as Camus's cipher ([`targets/camus1586/`](../camus1586/NOTES.md)) and the Matignon/Forget ciphers
([`targets/matignon1586/`](../matignon1586/NOTES.md)): different ciphers, each with its own page.

## The document

Jean de Chourses, sieur de Malicorne, governor of Poitou, to Henri III, *"A Nyort ce xxie avril 1586"*, signed
*Malycorne*; ark `btv1b9061879d`, address leaf *"Au Roy"* canvas 173 right.

| canvas | leaf | content |
|---|---|---|
| 169 right | f. 162r | 4 clear lines, then 27 cipher lines |
| 170 left | f. 162v | 31 cipher lines |
| 170 right | f. 163r | clear text with stretches A (2 lines) and B (9 lines), deciphered in the margin |
| 171 left / right | | clear letters with a 4-line and a 16-line cipher block |
| 172 left / right | | 31 and 24 cipher lines, then the clear close and signature |

## Files

- `brackx2026/aligned_f162r.txt`, `brackx2026/aligned_f163r.txt`: the aligned decode (transcription, value per sign,
  decoded line; not edited by hand), issue #92 comment of 23 Oct 2026.
- `brackx2026/margin_f163r.txt`: the margin decipherment as read at full size. `brackx2026/key_r2.txt`: the key.
- `brackx2026/aligned_f162v.md`, `aligned_c171.md`, `aligned_c172l.md`, `aligned_c172r.md`: the same format for the
  other four pages (raw decoder output), and `brackx2026/legend.md`, every label with count, value(s), sign shape and the
  basis of the shape; `brackx2026/aligned_readme.md` the gist's readme (issue #92 gist, 23 Oct 2026).
- `measure_pages.py` → `measure_pages.tsv`: per-page signs, multi-valued letters and lexicon coverage with a shuffled control.
- `brackx2026/transcription_issue.txt`: the transcriptions as posted in the issue body (pages not headed before f. 163r).
- `texts/`: per text the transcription, the raw decryption, the reading in the decode's spelling and the English.

## Measured (v10_relabel.measure; in-word bracket expansions count as holes)

| text | words | holes | read_share | state |
|---|---|---|---|---|
| f. 162r | 107 | 65 | 0.622 | decoded, not read |
| f. 163r A | 8 | 3 | 0.727 | read in part |
| f. 163r B | 34 | 15 | 0.694 | decoded, not read |

Reviewed as sentences, grade B, Claude Opus 5.5, 24 Oct 2026.

**All six pages, raw decode (`measure_pages.py`, 23 Oct 2026).** Share of decoded letters that fall in French words of
four letters or more under the best segmentation, against the same letters shuffled:

| page | signs | letters | on multi-valued labels | unvalued signs | lexicon coverage | shuffled |
|---|---|---|---|---|---|---|
| f. 162r | 739 | 807 | 15.6% | 3 | 72.7% | 24-26% |
| f. 163r (A + B) | 257 | 276 | 17.0% | 1 | 71.4% | 18-22% |
| f. 162v | 863 | 940 | 14.1% | 0 | 69.3% | 23-27% |
| canvas 171 | 585 | 633 | 9.6% (Brackx; 9.8% before one relabel) | 0 | 68.4% | 22-28% |
| canvas 172 left | 865 | 925 | 13.3% | 0 | 71.6% | 22-32% |
| canvas 172 right | 609 | 673 | 11.1% | 0 | 81.1% | 23-32% |

The four new pages decode as well as f. 162r, whose reading measured 0.622: French throughout, but with 10-14% of
letters on two-valued labels and no margin to confirm the choices. They are *decoded, not read*.

**Readings of the four pages and the split checks (Brackx, issue #92 comment of 25 Oct 2026; `brackx2026/reading_r3.md`,
split per page into `texts/reading_<page>.md` and `_en.md`).** Measured here with `v10_relabel.share`:

| page | words | holes | read_share | look-alike share (hand-chosen) | state |
|---|---|---|---|---|---|
| f. 162v | 145 | 85 | 0.630 | 8 of 948 letters (0.8%) | decoded, not read |
| canvas 171 | 92 | 45 | 0.672 | 2 of 633 (0.3%) | decoded, not read |
| canvas 172 left | 104 | 80 | 0.565 | 0 of 925 | decoded, not read |
| canvas 172 right | 132 | 35 | 0.790 | 4 of 673 (0.6%) | decoded, not read |

Sentences build only between holes: f. 162v ll. 1-6, [?Laval] dead of grief after his two brothers were killed at
Saintes; canvas 172 right, soldiers with intelligences with the enemy and the companies still to come; canvas 171,
ladders of [?wood] and rope to surprise a town on an intelligence.

Split checks on tiles (canvases 170 left, 172 left and right, 25 Oct, cut by template matching; f. 162r, f. 163r and
canvas 171 after deskewing the blocks, -3.5°, -1° and -2.25°/-2.5°, 26 Oct 08:17; Brackx, issue #92; 45 tokens of
`Lb`, `Lc`, `Lm` and `cr` checked). **The barred £ is always *m*** (`Lc`). **The looped ℒ (`Lb`) is *b* or *m***, with
six *m* tokens (162r l. 7; 162v l. 11; 171 right ll. 10, 16; 172 left l. 31), so `Lb` stays two-valued: the 25 Oct
rule "looped ℒ = *b*" was wrong. The canvas 172 *m* tokens (two-valued share 172 left 13.3% to 11.9%, 172 right 11.1%
to 10.3%) and 171 right l. 9 were moved to `Lc`; 162r l. 19 (a looped ℒ) was left as `Lc`. `Lm` (*m*/*n*): one barred
£ shape throughout (21 tokens on f. 162r/163r/171, plus f. 162v), no split. `cr` (*h*/*s*): crossed p, crossed v and
dagger forms, none keeping to one value, so no split (the 25 Oct "probable split" withdrawn). `F` (all 19 tokens the
same barred f) and `y_` (one possible ꝩ flagged) do not split. The decoded text is unchanged by every relabelling.
The deskewed positions (`brackx2026/shape_check_r3_positions.tsv`, 45 tokens, canvas x/y +-40 px), the relabelled canvas 171
transcription (`f171_groups_r3.txt`, line 13 token 24 Lb -> Lc) and his notes (`splits_r3.md`) arrived in the gist on 28 Oct
(07:04) and are copied here; the aligned files, legend and reading_r3.md were refreshed from the same gist. Checked here: the
file has 20 cipher lines, 3 Lb and 3 Lc tokens, and line 13 token 24 is Lc; the 45 positions are not re-located on the images.

**Split candidates** (Brackx's legend): `F` (*d* / *la*: Tomokiyo draws *la* as the same looped f with a bar, so a bar
check per token should separate them); `cr` (*h* / *s*: a crossed p and a dagger-like stroke on the canvas 172 tiles);
`Lb` (*b* / *m*) and `Lm` (*m* / *n*): script ℒ, barred £ and plain L not told apart in transcription; `a2` (*n* / *o*);
`y_` (15 tokens on canvas 172, hooked ɣ = *s* or looped ꝩ = *p*). Not splittable by shape at this resolution: `dc`/`dcL`
(one ∂ shape for c / s / o); too few tiles: `zz`, `s`. Usable sign positions exist only for canvas 172 (f. 163 and
canvas 171 have none; the f. 162 positions are misaligned). (25 Oct; on 26 Oct Brackx cut positions for f. 162r, f. 163r and canvas 171 after
deskewing, see the split checks above.)

> A: [?] consiste en la creance du [?] porteur et [l]esdicts articles. (margin: *consiste en la creance du port[eu]r, & les articles*)

## Departures from the raw decode

| page, line | raw decode | reading | kind | letters |
|---|---|---|---|---|
| 162r l. 3 | `lusignam` | {Lusignan} | `Lm` read *n*, not *m* | 1 |
| 162r l. 10 | `seulx` | {ceulx} | `dc` read *c*, not *s* | 1 |
| 162r l. 23 | `ioi` | {ici} | `dc` read *c*, not *o* | 1 |
| 162r l. 26 | `onssart` | {Cossart} | `dc` read *c*, not *o*; `a2` read *o*, not *n* | 2 |
| 163r B l. 5 | `tranee` | {tramee} | `Lm` read *m*, not *n* | 1 |
| 163r B l. 10 | `se` | {ce} | `dc` read *c*, not *s* | 1 |
| 163r B l. 4 | `iauous` | i'auois° | margin *que j'avois*; `oo` = *u* in the key | 1 |
| 163r B l. 5 | `charbonnoere` | charbonnieres° | margin *aux charbonnieres* | 2 |
| 163r B l. 7 | `desobueertes` | descouuertes° | margin *descouvertes(?)* | 3 |

Six hand-chosen readings (7 letters, all on two-valued labels: 0.6% of f. 162r's letters, 0.7% of f. 163r's, under the
3% look-alike limit) and three margin-carried words on f. 163r B.

## Controls

- Crib A 97.6% (shuffled 22–27%); crib B ll. 1–3 83.3% (21–26%). **Crib B restated:** the posted 72.8% for B ll.
  4–14 could not be reproduced (rows and crib text not recorded); under a stated definition (legible margin words
  against cipher rows 4–8) it is **79.3%**, shuffled keys 15–24%.
- Language-model coverage: posted 76.5%; with the corrected *Essais* I–III model 72.3% (shuffled 32.5–47.7%).

## Remaining gaps

- f. 162v and canvases 171-172 (four pages): decoded, not read (read share 0.565-0.790) - blocker: no-key-material; readings built and the split candidates checked (issue #92); no contemporary decipherment of these pages or of another letter in this key
- f. 162r and f. 163r B: decoded, not read (0.622, 0.694) - blocker: no-key-material; 13 labels still carry two values; shape checks after deskewing (26 Oct) split none of `Lb` (ℒ), `Lm`, `cr`, `F`, `y_`, so the values can only be fixed from context or a second deciphered letter, and the B margin is mostly illegible between 'argent' and 'descouvertes'
- f. 163r A: the opening group, the word before 'porteur', the supplied l of lesdicts - blocker: too-short; single groups at the edges of a two-line stretch with no margin word

## Escalation

- [x] siblings: all six pages of the letter transcribed by Brackx; Camus's and Matignon's ciphers in the same volume are other keys
- [x] clear-pages: the f. 163r margin decipherment used as the crib; no clear copy found among ff. 162-173
- [x] known-keys: Tomokiyo's Malycorne table applied and corrected
- [x] print: Tomokiyo gives the key table only; no edition found by Brackx's web search
- [x] key-rebuild: aligned decodes of all six pages and the 195-label shape legend (23 Oct 2026); split candidates checked on tiles (25 Oct 2026); `Lb` barred £ moved to `Lc` (*m*), looped ℒ still *b*/*m*; `F`, `Lm`, `y_`, `cr` do not split (25-26 Oct, deskewed tiles on all six pages)
- [x] retry: all four pages re-decoded after the `Lb` split (no letter changes) and read in the f. 163r format (Brackx, 25 Oct 2026); 26 Oct: canvas 171 relabel, decode unchanged

## Log

- 2026-10-26 08:17 Brackx (issue #92): deskewed f. 162r/163r/171; 45 tokens of `Lb`/`Lc`/`Lm`/`cr` checked; `Lb` rule
  corrected (looped ℒ = *b* or *m*), `cr` no split; one token relabelled (171 right l. 9, `Lb` to `Lc`); text unchanged.
  Recorded here 27 Oct 2026.
