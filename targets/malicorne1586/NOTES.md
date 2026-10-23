# Malicorne to Henri III, Niort, 21 April 1586: cipher letter in BnF fr. 15572 ff. 162–164 (Malicorne's cipher)

Status: in progress (four of the six cipher pages await the contributor's aligned decode and sign-shape legend).

**Read in part, 24 Oct 2026.** Contributed by Michael Brackx (@brackxm, issue #92, 22–23 Oct 2026), with Claude Code
(Claude Opus 5.5). Method: **read with known key**: Tomokiyo's key table ("Malycorne's Cipher", Cryptiana henryiii
page), corrected by Brackx and checked against the contemporary margin decipherment on f. 163r. f. 163r stretch A
reads as one sentence confirmed by the margin (read_share 0.727, read in part); f. 162r (0.622) and f. 163r stretch B
(0.694) are *decoded, not read*; the other four pages are not yet given.

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
- `brackx2026/transcription_issue.txt`: the transcriptions as posted in the issue body (pages not headed before f. 163r).
- `texts/`: per text the transcription, the raw decryption, the reading in the decode's spelling and the English.

## Measured (v10_relabel.measure; in-word bracket expansions count as holes)

| text | words | holes | read_share | state |
|---|---|---|---|---|
| f. 162r | 107 | 65 | 0.622 | decoded, not read |
| f. 163r A | 8 | 3 | 0.727 | read in part |
| f. 163r B | 34 | 15 | 0.694 | decoded, not read |

Reviewed as sentences, grade B, Claude Opus 5.5, 24 Oct 2026.

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

- f. 162v and canvases 171-172 (four pages): aligned decode not yet given - blocker: not-attempted; the aligned decode (about 450 lines) and a legend tying each label to its sign shape were requested from the contributor
- f. 162r and f. 163r B: decoded, not read (0.622, 0.694) - blocker: no-key-material; 13 labels still carry two values with shapes not split at this resolution, and the B margin is mostly illegible between 'argent' and 'descouvertes'
- f. 163r A: the opening group, the word before 'porteur', the supplied l of lesdicts - blocker: too-short; single groups at the edges of a two-line stretch with no margin word

## Escalation

- [x] siblings: all six pages of the letter transcribed by Brackx; Camus's and Matignon's ciphers in the same volume are other keys
- [x] clear-pages: the f. 163r margin decipherment used as the crib; no clear copy found among ff. 162-173
- [x] known-keys: Tomokiyo's Malycorne table applied and corrected
- [x] print: Tomokiyo gives the key table only; no edition found by Brackx's web search
- [ ] key-rebuild: the four remaining pages' aligned decode and the sign-shape legend are needed before the merged labels can be split
- [ ] retry: after the four pages arrive
