# Malicorne to Henri III, Niort, 21 April 1586: cipher letter in BnF fr. 15572 ff. 162–164 (Malicorne's cipher)

Status: in progress (all six pages' aligned decodes and the shape legend received 23 Oct 2026; the per-token shape
checks of the merged labels are next).

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
| canvas 171 | 585 | 633 | 9.8% | 0 | 68.4% | 22-28% |
| canvas 172 left | 865 | 925 | 13.3% | 0 | 71.6% | 22-32% |
| canvas 172 right | 609 | 673 | 11.1% | 0 | 81.1% | 23-32% |

The four new pages decode as well as f. 162r, whose reading measured 0.622: French throughout, but with 10-14% of
letters on two-valued labels and no margin to confirm the choices. They are *decoded, not read*.

**Split candidates** (Brackx's legend): `F` (*d* / *la*: Tomokiyo draws *la* as the same looped f with a bar, so a bar
check per token should separate them); `cr` (*h* / *s*: a crossed p and a dagger-like stroke on the canvas 172 tiles);
`Lb` (*b* / *m*) and `Lm` (*m* / *n*): script ℒ, barred £ and plain L not told apart in transcription; `a2` (*n* / *o*);
`y_` (15 tokens on canvas 172, hooked ɣ = *s* or looped ꝩ = *p*). Not splittable by shape at this resolution: `dc`/`dcL`
(one ∂ shape for c / s / o); too few tiles: `zz`, `s`. Usable sign positions exist only for canvas 172 (f. 163 and
canvas 171 have none; the f. 162 positions are misaligned).

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

- f. 162v and canvases 171-172 (four pages): decoded, not read (lexicon coverage 68-81%, 10-14% of letters on multi-valued labels) - blocker: not-attempted; the per-token shape checks on canvas 172 (`F` bar, `cr`, `Lb`/`Lm`, `y_`), then re-decode and build readings
- f. 162r and f. 163r B: decoded, not read (0.622, 0.694) - blocker: no-key-material; 13 labels still carry two values with shapes not split at this resolution, and the B margin is mostly illegible between 'argent' and 'descouvertes'
- f. 163r A: the opening group, the word before 'porteur', the supplied l of lesdicts - blocker: too-short; single groups at the edges of a two-line stretch with no margin word

## Escalation

- [x] siblings: all six pages of the letter transcribed by Brackx; Camus's and Matignon's ciphers in the same volume are other keys
- [x] clear-pages: the f. 163r margin decipherment used as the crib; no clear copy found among ff. 162-173
- [x] known-keys: Tomokiyo's Malycorne table applied and corrected
- [x] print: Tomokiyo gives the key table only; no edition found by Brackx's web search
- [ ] key-rebuild: aligned decodes of all six pages and the 195-label shape legend received (23 Oct 2026); the per-token shape checks of the merged labels are not yet done
- [ ] retry: after the four pages arrive
