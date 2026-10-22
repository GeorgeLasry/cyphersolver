# Forget / Mayenne, BnF fr. 15572 (+ fr. 15571 f. 177), 1585–86 — Mayenne–Forget Cipher-1

Status: read in part, written up 22 Oct 2026 ([`docs/matignon1586.html`](../../docs/matignon1586.html)). Measured
with the **merged Cipher-1 key** (`key_cipher1.json`, section "One key, 22 Oct 2026" below) on Michael Brackx's
complete re-transcription (issues #73, #77, #78, #79, #83): **63.7% of the target's cipher tokens read as sense
(10,616 of 16,677; 58.7% after a scrambled-key control)**, every Cipher-1 leaf transcribed in full. Where a contemporary
clear copy exists the decode agrees with it on 85-93% of letters. Before: 61.8% with his per-leaf keys, 39%
(`key_contrib.json`, 21 Oct), 31% (`key.json`, 22 Sept). **ff. 143r-v, 149v-150 and 154r-v were deciphered at the
time**: ff. 155-157 are contemporary clear copies of them (found by Brackx, #70). The read bar (95%) is not met; ten
code groups and the residue of each leaf stay open (Remaining gaps). Full decryptions per document: `texts/`.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). This folder keeps **Mayenne–Forget's
Cipher-1** only. Matignon's **Cipher-3** leaves (fr. 15572 f. 276 and fr. 15571 f. 179, read by alejandrozarco in
PR #25) are a different cipher with their own entry and page: [`targets/matignon1586c3/`](../matignon1586c3/NOTES.md)
(`f276/` and `f179/` moved there). f. 79r is Cipher-1 (see below). The genuine Cipher-2 leaves, fr. 15572 ff. 218–219,
were not attempted here; Harumi-Matsuba read them (issue #49) and they are now the entry
[`targets/mayenne1586c2/`](../mayenne1586c2/NOTES.md), with two more Cipher-2 letters of fr. 15573 (ff. 120, 385).
fr. 15572 f. 43, solved by George
Lasry in 2022, is not a document of this entry and carries no credit here.

Catalogue item 12 (`CATALOGUE.md`), class B, solvability 5. Ten leaves that S. Tomokiyo
(`cryptiana`, *Henry III's Cipher with Ambassadors*) marks **undeciphered** although he publishes
partial tables for the two keys involved.

## What the target actually is

Tomokiyo's list, checked against the live page on 17 Sept 2026:

* **Mayenne–Forget's Cipher-1** (used among Mayenne, Forget de Fresnes, Villeroy and Henri III).
  Deciphered siblings in the same volume: **f. 14** (deciphered in f. 15), **ff. 18-21**
  (deciphered in f. 19), **ff. 78-79** and **ff. 91-92** (deciphered in the margin).
  Undeciphered: **ff. 110, 123-124, 143, 150, 154, 173, 196, 201**.
* **Matignon's Cipher-3**: deciphered f. 189 (in f. 190), ff. 277-278 (in ff. 279-280), f. 282
  (margin); undeciphered **f. 276**, and **f. 179 of fr. 15571** (both now read; the entry `matignon1586c3`).
* fr. 15572 **f. 43** is in the catalogue line but is *not* open: George Lasry solved it in 2022.
* The catalogue's "fr. 15571 ff. 218-219" is a slip for **fr. 15572 ff. 218-219** (Matignon in
  Mayenne–Forget's Cipher-2).

Prior art checked: no printed decipherment of these despatches was found (searches on the BnF
catalogue and on the literature, 17 Sept 2026). Tomokiyo publishes short openings for ff. 143,
150, 154 and for "f. 111" (probably a slip for f. 110).

## Access: folio to Gallica canvas

fr. 15572 = ark `btv1b9061879d` (385 canvases); fr. 15571 = ark `btv1b90618802` (226).
**Each canvas is a double-page opening**, so the recto of folio *f* is the *right* page of a
canvas, and the verso of *f* is the *left* page of the next. The leaf carries two foliations,
the older one struck through; **the valid number is the lower of the two**. The offset from
folio to canvas drifts (about +2 at f. 14, +6 from f. 99 to f. 137, +7 by f. 142), so it has to
be read off the leaf. Fixed here:

| folio | canvas (page) | content |
|---|---|---|
| 14r / 14v | 16 right / 17 left | Forget to Villeroy, 24 Jan 1586; 4-line ciphered postscript on 14v |
| 15r | 17 right | the decipherment of that postscript, in clear, 3 lines |
| 78v, 79r | 85 left, 85 right | Mayenne to the King, camp de Tonneins(?), March 1586; cipher blocks with marginal decipherment |
| **110** | **116 right** | one leaf wholly in cipher, c. 48 lines, ending "De Bellebourg … jour de Mars 1586" |
| **123-124** | **129 right – 131 left** | despatch to the King: f. 123r opens in clear, then c. 140 lines of cipher over four pages |
| **143** | **150 right** | Mayenne to the King: clear first half (Marmande, Sainte-Bazeille, Castets, the capitulation), then 22 lines of cipher |
| **150** | **158 left** | a full page of cipher |
| **150** | **157 right – 158 left** | a page and a half wholly in cipher |
| **154** | **161 right** | clear opening, then c. 25 lines of cipher |
| **173** | **180 right** | "Sire" in clear, then c. 30 lines of cipher |
| **196** | **203 right** | clear to *auquel*, then the rest of that line and 30 full lines of cipher to the foot (31 in all; 26 transcribed) |
| **201** | **208 right** | the **same despatch**: clear a line and a half further, cipher, then clear again for the last three lines |

The clear openings identify the despatches: f. 123r "Sire, la dernière que j'ay eu l'honneur est
du huict[iesm]e de ce moys…"; f. 143 Marmande, Sainte-Bazeille, Castets and the capitulation;
f. 154 "Monseigneur, vous avez veu par la despesche du S.r Delorme … qui partit d'icy la veille de
Pasques" (Easter 1586 = 6 April), so f. 154 is to Villeroy, not to the King; f. 173 "Sire, Vostre
Majesté a esté suffisamment advertie par les deux dernières despesches de Monsieur du Mayne";
ff. 196 and 201 both "Sire, Depuis le partement du S.r de Bosseval…".

**ff. 196 and 201 are the same despatch** — see [`f196_f201.md`](f196_f201.md). That pair is now
the most tractable target in the item: it carries two cribs (f. 201 is in clear where f. 196 is in
cipher, at the head and again at the foot) and the two ciphered blocks are the same plaintext
enciphered twice, i.e. in depth.

All eight Mayenne–Forget leaves are now located on the image. f. 143 is the best conditioned:
a large, well-spaced hand, 21 lines. ff. 110 and 123–124 are the same cipher in a small, dense
hand — f. 123r alone runs to 38 lines — and are where the volume of text is.

## Method

1. `fetch.py` / `corners.py` / `folgrid.py` — IIIF fetch of the volume and of the folio-number
   corners, to build the index above.
2. `mklm.py` — a character 6-gram model of period French built from the 10 MB of Berger de
   Xivrey's *Recueil des lettres missives de Henri IV* already in `../bethune/xivrey/`
   (6.4 M characters after normalising: accents stripped, v→u, j→i, as the cipher does not
   distinguish them).
3. `flatten.py` — divides out a Gaussian background (flattens the parchment), then unsharp-masks.
   This is the single biggest gain in legibility of anything tried here and should be the first
   step on any new leaf. `tiles2.py` then cuts the block into per-line tiles for transcription by
   eye; `fitlines.py` + `recenter.py` place the lines.
4. `solve.py` / `dec.py` — a beam search over the token sequence where each glyph token carries a
   *set* of candidate letters, scored by the language model, then a dictionary word-segmenter.
   This is what makes the key usable: several glyphs of this cipher are genuinely confusable
   (Tomokiyo boxes three near-identical "6" shapes standing for **i, n, s**), so a
   one-glyph-one-letter transcription is not achievable by eye and the ambiguity has to be
   carried into the decoder.

## The key, as re-derived from the manuscript

Verified against the complete f. 14v/f. 15r crib ("Vous pouez juger que ceste ouverture n'est pas
toute nouvelle …") and against the cipher of f. 143. Values in **bold** are not in, or not
legible in, Tomokiyo's published table.

| glyph | letter | glyph | letter |
|---|---|---|---|
| ɑ (a with tail), Δ | a | ·v·, **ʄʄ (ff-ligature)** | n |
| ʠ | b, z | 7, H | o |
| ʃ (long s) | c | ᴄ, R | p |
| ϖ (m with overbar), ∞ | d | £, Ɛ, e | r |
| t, ʓ, Ƨ, ʋ | e | ∂, ɟ, **ɣɣ = ss** | s |
| M | f | m, **Ƶe** | t |
| 8, ▽, y | g | ʃ, s, Ɋ, ⊐ (box), **ꝉ (crossed t)** | u / v |
| f | h | θ, **₸ (crossed 4)** | m |
| o, 6, β, ε, 3, **ƀ** | i / j | n, A, **ʰe** | l |

Code groups seen so far: 12 *il*, 13 *qui*, 14 *que*, 47 *tous*, **49 (unidentified, frequent)**,
76 *le roi de Navarre*, 26 *vous/leur*.

## Result so far

**f. 143 (Mayenne to Henri III): 21 lines transcribed, about half read.** See
[`f143_reading.md`](f143_reading.md) for the text, `cipher_f143.txt` for the glyph transcription
and `reading_f143.txt` for the decoder's raw output. Tomokiyo printed
"s'estant laisse entendre 49 il se voulloit de partir du 76 duquel je scai quil est tres
malcontant et ayant considere que je lai tousjours ou y tenir pour le meilleur …". The reading
here agrees and runs on:

> … m'estant laissé entendre [49] il se vouloit départir du **roi de Navarre**, duquel je scai
> qu'il est très malcontant; et ayant considéré que je l'ay tousjours ou y tenir pour le meilleur,
> comme de [49] commandement qu'il ayt, et que ce ne seroit [une] petite faveur pour ses affaires
> que de …

Later stretches read "… le et service; il m'a promis de vous … faire pendant ce temps …",
"… ou à la vérité il s'est résolu … la composition de sa place, laquelle estoit encore …",
"… de séjour qui nous est très … parce qu'il m'eust fallu passer …". Lines 8-9, 14-15 and 19-21
still carry glyph errors and are not offered as a reading.

A practical note for whoever continues: **measure the line positions, do not assume they are
evenly spaced.** Cutting f. 143 on a uniform grid put the bands up to 60 px off by line 15 and
turned the second half of the page into noise; correlating a comb against the row-ink profile,
then refining each line on the local maximum, fixed it.

## Open / next

* Finish f. 143's weak lines (8-9, 14-15, 19-21). Everything there turns on telling apart the
  three "6" shapes (i / n / s) and the two round shapes (a / m); a labelled glyph atlas cut from
  the lines that already read would settle them.
* **ff. 196 / 201 first**: transcribe both blocks, align them, solve jointly against the two
  cribs. This is the one place in the item where the evidence is doubled.
* f. 110 is faded and dense (c. 48 lines); ff. 123-124 is the prize (four pages, c. 140 lines,
  opening in clear: "Sire, la dernière que j'ay eu l'honneur est du huict[iesm]e de ce moys …").
* A word-aware decoder (`wdec.py`, beam over letters *and* word boundaries, unigram word model
  swapped in for the character model over each closed word) was tried against the character
  decoder and does **not** help: on f. 143 the two agree on the lines that read and both fail on
  the same lines. That is the evidence that the residue is transcription, not decoding.
* The f. 18-21 / f. 19 crib has not been used yet and should settle the remaining homophones and
  the value of code 49.


## Where the work actually stops, measured

Two leaves have now been pushed hard enough to measure the cost of this cipher:

* **f. 143** (21 lines, the largest and cleanest hand of the eight) took *three* passes — three
  tiles a line, then five, then eight on the survivors — to reach about two thirds read. Lines
  1-7, 9-14 and 17 are continuous French; 8, 15-16 and 18-21 give clauses only. Line 8 resists
  even at eight tiles a line and flattened: it decodes to "a r o m e ? e [car] l m a l a i c t e
  d e n e p o r t e ..." and no reading of it is French, which most likely means a place or
  person name in it.
* **f. 196** (31 cipher lines counting the part-line after *auquel*; "36" was wrong; small hand) is not yet transcribed: the line fit alone needed a comb, a
  spacing-constrained DP, re-centring on glyph boxes and a manual offset, and still does not place
  every line well enough to tile. That is before a figure is read.

So the cost is roughly three tool-calls per line to get tiles the eye can settle, and about
fifteen per cent of figures resist anyway, to be recovered — or not — by the language model. The
eight Mayenne-Forget leaves are about 300 lines. This is a multi-session job, and the constraint
is the transcription of a 16th-century hand, not the cipher, which is solved.

### The order to do it in

1. **ff. 196 / 201** — the only place where the evidence is doubled (same plaintext twice) and
   where cribs at head and foot let segmented glyph boxes be *labelled*, which is the only thing
   that has actually broken a confusable pair so far.
2. **f. 143's** remaining eight lines.
3. **f. 154, 173** (clear openings, ~25-30 lines each).
4. **f. 110** (48 lines, faded) and **ff. 123-124** (140 lines) last: most text, worst conditions.


## Line placement is the unglamorous blocker

Worth writing down because it cost more than anything else here. Tiling a block into per-line
images needs the line centres to within about a fifth of the line pitch, or the tile clips and the
figures cannot be read. On these leaves the pitch is *not* constant — it wanders by 10-15 % from
line to line — so none of these alone is enough:

* a uniform grid from a comb fit (drifts; this is what silently corrupted the second half of the
  first f. 143 pass);
* local refinement on the ink profile (jumps to a neighbouring line);
* re-centring on the median glyph-box centre (`recenter.py` — returns almost no correction,
  because the boxes are already symmetric about the wrong centre);
* centre of mass of the x-height band (`center2.py` — best of the four, still leaves a systematic
  offset that varies per leaf and has to be found by eye on an overlay).

What works, and what the next pass should just do: draw the fitted lines on the flattened block,
look at the overlay, and set the per-leaf offset by hand — then tile with a band of about half the
pitch. f. 143 and f. 201 both fitted cleanly this way; f. 196 (the smallest hand) still does not,
and that is why its 31 lines were untranscribed at that point while f. 201's fit was ready to use.
(Later on 18 Sept, 26 of the 31 were transcribed: see "Coverage, measured".)


## The f. 18/f. 19 crib and the figures-to-French pipeline

The second half of the 17 Sept 2026 work turned on a crib Tomokiyo mentions in one clause and never
uses: **f. 18 is ciphered and f. 19 is its decipherment in clear**, about 1,650 figures with their
plaintext beside them. Full account in [`f18_f19_crib.md`](f18_f19_crib.md). In short:

* The pairing is verified twice on the leaf — f. 19r opens *"Que sa Majesté fust advertie"* against
  a cipher opening with `14` (*que*), and the cipher carries `52` where the clear reads *plustost*,
  the first check of Tomokiyo's nomenclature against a plaintext.
* It is **one key** across the leaves; an apparent contradiction with the ff. 196/201 crib was my
  own shorthand colliding on near-identical figures, not two ciphers.
* The confusable figures were **measured**: i/n, s/i and e/u sit at 0.91–0.93 correlation on the
  manuscript. They are not separable by shape at any resolution available, so **at the level of
  reading this cipher is polyphonic** — a figure is a small set of letters and only the language
  chooses. That explains every dead end: the shape classifier was always going to fail, and the
  early workaround `"6": ["i","n","s"]` in `key.json` was the right model all along.
* So the crib's output is stored as **labelled images**, not names: `exemplars/` with a manifest.
  103 figures over 18 of 22 letters at the time of writing; missing h, q, x, y, z.
* `readleaf.py` reads a line from figures alone — segment, match against exemplars, beam-decode
  with code groups — and recovers about **70 % of plaintext characters** on the crib leaf, with
  f. 18r line 3 read end to end: *"re et conseil des sembler de castille bour"*.
* Every free parameter is pinned by measurement against known plaintext, not by taste: segmenter
  gap 14, per-character bonus 1.6, code similarity floor 0.93.
* `baseline.py` scores the pipeline so a later pass can tell whether it helped — and its first job
  was to show that three lines is too small a test set to detect anything.

**The variable that remains is letter coverage.** Line 3 reads at 94 % because its letters are
covered; line 4 at 45 % because *instruction* wants p and q. Nothing else in the pipeline is
uncertain.

Two practical findings for whoever continues: **proper names are the densest exemplar source** (they
are spelled out rather than hidden in code groups — *Matignon* on f. 19r line 13 is nine consecutive
certain figures), and **exemplars do not transfer between scribal hands** — the same pipeline run on
f. 143 gives noise, because that is a different secretary.

## Session of 18 Sept 2026: six leaves read, and the target is not one cipher

**Read in substance or in stretches, all in the solved Cipher-1:** f. 143r+v (earlier), **f. 150**
(13 ciphered lines over a clear Forget letter to Villeroy, April 1586), **f. 154** (28 lines, the
army's pay crisis), **f. 173** (33 lines, to the King: no one will lend and no one will go surety),
**f. 196** (26 of its 31 lines transcribed) and **f. 201** (30 lines) — one despatch on two leaves, a siege report naming
**"le mareschal de Matignon"**, and **fr. 15571 f. 177** (28 lines, Mayenne's design for Gascony,
31 Dec 1585). See the `f*_reading.md` files.

**The ff. 196/201 check.** The two leaves were transcribed independently. Aligned figure by figure,
**57% of their figures are identical**, with 8 maximal runs of eight or more (longest 12); shuffling
one side gives 12% and no runs. That validates both transcriptions at once. (An earlier note said
"23 runs of eight" - that counted overlapping windows, not runs.) The 43% that differ are not noise:
a homophonic cipher offers several figures per letter, so f. 201 is a **re-encipherment** of the
same text, not a copy of f. 196.

~~**The target is at least three ciphers**~~ — **retracted** in `ciphers.md`: ff. 123–124, f. 110 and
ff. 78v/79r are all Cipher-1 (scrambled-key control and the f. 78v margin decipherment); the "three
ciphers" came from label drift between transcription sittings. The only other cipher in the item is
Matignon's Cipher-3 (ff. 276 and fr. 15571 f. 179). fr. 15571's ciphered page at canvas 187 left,
called "a fourth hand" here, **is fr. 15571 f. 179** (the slip is bound upside down; its foliation
reads 179 when turned), i.e. the Cipher-3 leaf, not a fourth cipher.

**A crib for the second cipher exists**: f. 79r (canvas 85 right), Mayenne's own letter from the
camp at Tonneins, 5 March 1586, carries a seven-line cipher block **with its decipherment down the
left margin**. "rouergue" matches the block's figures in exactly one place, giving `4+`=r, `6`=o,
`h`=u, `f`=e, `B`=g. **(Withdrawn: f. 79r is Cipher-1 and the solved key reads it; the single
"rouergue" hit was chance. See `ciphers.md`.)**

### Additions to the folio index

| folio | canvas (page) | content |
|---|---|---|
| **79r** | **85 right** | Mayenne to the King, camp de Tonneins 5 March 1586, signed Charles de Lorraine; 7 cipher lines **with marginal decipherment** — the crib for Cipher-2 |
| **125r** | **131 right** | clear letter: Castets besieged, the battery, M. d'Alincourt, Matignon, Mayenne |
| **fr. 15571 177** | **185 right** | Forget, 31 Dec 1585, 29 cipher lines in Cipher-1 (24 transcribed; foliated 190 struck / 177) |
| **fr. 15571 179** | **187 left** | the Cipher-3 slip, bound upside down (was listed here as "178v, fourth hand"); ~25 lines; `img/BnFfr15571f179.jpg` (cryptiana) carries an interlinear decipherment in magenta |
| **fr. 15572 276** | **285 right** | the other Cipher-3 leaf: a small slip, ~27 lines wholly in cipher; siblings ff. 277r-278r (canvases 286 right to 287 right, cipher) are deciphered in ff. 279-280 (clear from 288 right) |
| **fr. 15571 180** | **188 right** | (fixes the foliation: f. 180 recto is canvas 188 right) |

### Tools added

`rowcut.py` cuts rows with **alternate rows tinted**, so a row's left and right halves carry the
same wash and the join never depends on a line number — the fix for a full hour lost on f. 173 to
halves joined one row apart. `fitlines.py` fits and snaps a line grid. `hillclimb.py` is a cold
solver (annealing over figure→letter maps, `FIX=` to hold known values, `SEEDKEY=` to start from a
known key).

### A defect in the language model, found and fixed

Built with `v→u` and `j→i`, the corpus's Roman numerals became runs of `i`, and a page of `iiiiii`
scored **better** than French (−1.53 vs −1.51 per character) — so the cold solver collapsed every
figure onto `i`. Dropping Roman-numeral tokens and requiring a context to be attested 15 times gives
French −1.51, all-`i` −2.16, random −3.99. The old model is kept as `lm_v1.pkl`, the old scorer as
`solve_v1.py`.

## f. 110: identified, transcribed in part, not read

See `f110_status.md`. It is in the same key (decoded with the solved key it beats scrambled keys by
+2.07 per figure), but 18 of its 54 lines are transcribed and none of it reads continuously. The
diagnosis is transcription, not cryptanalysis: a solver seeded with the solved key moves 23 of 27
shared labels away from it, which means my names for this scribe's shapes do not match the figures
the key is keyed on. The fix is an exemplar set for this hand.

## Coverage, measured (22 Sept 2026)

The coverage figures in the `f*_reading.md` files ("about half", "two thirds") were estimates.
`measure.py` replaces them with a count (rule in its docstring; output `measure.json`): a cipher token
is **read** only if `key.json` gives it a value (tokens not in the key, `BOX`, `?` and unidentified
codes count unread) **and** its decoded letters fall inside a run of at least three corpus words
(count >= 20) totalling at least ten letters. Each leaf is decoded as `dec.py` does. Untranscribed
lines count as unread, estimated at the leaf's tokens per line (30 a line for untranscribed leaves).
Control: the same decoder and rule with the key's single-letter values shuffled (3 seeds).

| leaf | lines transcribed / on leaf | tokens | read | read / transcribed | scrambled floor | corrected |
|---|---|---|---|---|---|---|
| f. 110 | 37 / 54 | 1,699 (+781 est.) | 167 | 0.10 | 0.09 | 0.01 |
| f. 123r | 36 / 36 | 1,097 | 228 | 0.21 | 0.13 | 0.10 |
| f. 123v | 41 / 41 | 1,251 | 403 | 0.32 | 0.12 | 0.23 |
| f. 124r | 35 / 35 | 1,203 | 314 | 0.26 | 0.12 | 0.17 |
| f. 124v | 22 / 22 | 727 | 141 | 0.19 | 0.12 | 0.08 |
| f. 143r | 21 / 21 | 724 | 424 | 0.59 | 0.11 | 0.54 |
| f. 143v | 33 / 33 | 1,182 | 654 | 0.55 | 0.08 | 0.51 |
| f. 150 | 13 / 13 | 445 | 189 | 0.42 | 0.04 | 0.40 |
| f. 154 | 28 / 28 | 1,061 | 501 | 0.47 | 0.08 | 0.43 |
| f. 173 | 33 / 33 | 1,082 | 306 | 0.28 | 0.08 | 0.22 |
| f. 196 | 26 / 31 | 840 (+162 est.) | 376 | 0.45 | 0.07 | 0.41 |
| f. 201 | 30 / 30 | 987 | 455 | 0.46 | 0.07 | 0.42 |
| fr. 15571 f. 177 | 24 / 29 | 696 (+145 est.) | 167 | 0.24 | 0.14 | 0.12 |
| **total** | | **12,994 (+1,088 est.)** | **4,325** | **0.33** | | **0.26** |

Of the whole target (~14,082 tokens) **0.31 is read (0.24 chance-corrected)**. (Until 14 Oct 2026 the denominator
also carried ~1,560 estimated tokens for the two Cipher-3 leaves, giving 0.28 / 0.22; those leaves are now
`matignon1586c3`, measured there: f. 276 706/734, fr. 15571 f. 179 473/509.) 90% of transcribed
tokens are keyed; the gap between "keyed" and "read" is the transcription noise the notes describe.
The prose estimates were high on f. 143r ("two thirds": 0.59), f. 173 ("half": 0.28), f. 201 ("two
thirds": 0.46) and f. 177 ("a third": 0.24), and gave no figure for ff. 123-124 (0.19-0.32). f. 110
scores at its scrambled floor: unread, as `f110_status.md` says. Line counts checked on the images:
f. 196 has 31 cipher lines (26 transcribed; untranscribed are the part-line after *auquel*, the first
three full lines and the 13th, "mo£7om…"), fr. 15571 f. 177 has 29 (24 transcribed).

## Contributions of 21 Oct 2026 (Michael Brackx, issues #64, #68-#71)

Michael Brackx (@brackxm), working with Claude Code (Opus 5.5), posted five issues on 21 Oct 2026. They are folded
in here as contributed work, with credit in `profile.json` (provenance `mixed`). He gave no licence and no
repository, so his readings are summarised here, not copied; the issues hold his full text and figure tables.
None of it was checked by a second person against the images; what was checked here is listed at the end.

| issue | leaves | what he did | adopted here |
|---|---|---|---|
| #64 | ff. 196, 201 | joint figure-by-figure alignment of the two encipherments (914 columns, 487 identical), beam decode, f. 201 re-read on the image | all four names: **Sainct-Chamarand, la Barge, Montberault, la Binault**; content (Mayenne's fever, Matignon pressed to come, two trenches, battery of fifteen cannon); q = s (our own f. 196 head crib already implies it), f = h, ss = h; the clear phrase *Le regard dud. siege il s'advance fort* inside the f. 201 cipher block (checked) |
| #68 | f. 143r-v | decode with the corrected key; verso ll. 1-7 checked on the image | the treaty with the captain of **Castets** (12,000 écus in three months, leave to sell his property, a pardon to be registered by the Parlement); T= = r, a = a/m, c = p/l; 62 *peut*, 33 *vostre*, 40 *bien*, 54 *aussi*. **Not adopted:** 44 = *Sire* (he withdrew it himself); code 54's first value was inconsistent until the copy fixed it |
| #69 | f. 173 | decode; nine lines checked on the image | the credit crisis: no means to pay two musters, the town refuses to contribute on the strength of letters from the King, no one will stand surety, only merchants of Paris lend on the writer's word; 4+ = m/n, 8 = g/e. **Not adopted:** 79 = *pour* (one context). His notation block is pasted twice in the issue |
| #70 | ff. 154r-v, 155-157 | **found that ff. 155-157 are contemporary clear copies** of f. 143r-v (f. 155r-v), the ff. 149v-150 cipher (ff. 155v-156r) and f. 154r-v (f. 157r); read the copies by eye and aligned them with the decodes; found the f. 154v cipher (two blocks of about 11 lines) | the copies as the text of those leaves; codes 33 *vostre*, 36 *toutesfois* (not *avant*), 40 *bien*, 49 *comme* (not a null), 53 *affin*, 54 *aussi*, 62 *peut*, 76 *roi de Navarre*, 88 *Monsieur du Mayne*, 104 *mil*, `hash` *coustume* |
| #71 | ff. 123-124 | U = u/e/a, d = s/c, q = s/o/a (merged figure classes in our transcription); canvases 128-139 checked, no clear copy | the letter sets and the outline (no contributions without garrisons, the troops cannot be kept, the bearer sent for the King's intention, relief of places); partial, as he says: f. 123r still does not read |

**Key.** `key_contrib.json` (built by `mk_key_contrib.py`) is `key.json` plus his letter sets and the copy codes.
Not taken: `BOX` = u (in this transcription `BOX` also marks figures that could not be read), 44 = *Sire*,
79 = *pour*, and his figure names that have no token in our transcription (δ, ω, λ, ʒ as he names them).

**Re-measured (21 Oct 2026).** `measure.py --key key_contrib.json --control`, same rule as 22 Sept:

| leaf | read / transcribed, key.json | with key_contrib.json | scrambled floor | corrected |
|---|---|---|---|---|
| f. 110 | 0.10 | 0.09 | 0.09 | 0.01 |
| f. 123r | 0.21 | 0.27 | 0.15 | 0.14 |
| f. 123v | 0.32 | 0.39 | 0.15 | 0.28 |
| f. 124r | 0.26 | 0.35 | 0.10 | 0.28 |
| f. 124v | 0.19 | 0.38 | 0.12 | 0.29 |
| f. 143r | 0.59 | 0.63 | 0.09 | 0.59 |
| f. 143v | 0.55 | 0.66 | 0.07 | 0.64 |
| f. 150 | 0.42 | 0.48 | 0.08 | 0.43 |
| f. 154 | 0.47 | 0.56 | 0.08 | 0.53 |
| f. 173 | 0.28 | 0.49 | 0.09 | 0.44 |
| f. 196 | 0.45 | 0.54 | 0.07 | 0.50 |
| f. 201 | 0.46 | 0.62 | 0.10 | 0.58 |
| fr. 15571 f. 177 | 0.24 | 0.30 | 0.17 | 0.16 |
| **total** | 4,325 (0.333) | **5,480 (0.422)** | | 0.351 |

Of the whole target (~14,082 tokens) 0.389 (0.324 corrected). The floors rose by up to 3 points: part of the gain is the
wider letter sets, the rest is the code values and the corrected letters. The measure counts what the key decodes;
it does not credit ff. 143, 150 and 154 with their clear copies.

**Checked here on the images (21 Oct 2026, openapi.bnf.fr IIIF; gallica.bnf.fr/iiif answers 403).**
- Canvas 162 right (f. 155r): a clear page in a secretary's hand, opening *S'estant laissé entendre comme il se
  vouloit départir du Roy de Nav[arre] duquel je sçay qu'il est tres mal contant*; *soubz vostre bon plaisir
  toutesfois que je ne me fusse pas tant advancé* and *Et aussi qu'il n'y avoit plus de hasard* are legible. That is
  the f. 143 cipher, with 49 = *comme*, 33 = *vostre*, 36 = *toutesfois*, 54 = *aussi*.
- Canvas 163: f. 155v ends with the endorsement *Mr du Mayne de ... avril 1586*, then *Comme il estoit bien besoing
  ... Castetz*; f. 156r ends *Mr Forget de ... avril 1586*.
- Canvas 164 right (f. 157r): *En quelle peine nous estions lors pour le payement des deux monstres ...*, *quarante
  mil escus*: the f. 154 cipher. The left page (f. 156v) is blank but for an endorsement.
- Canvas 162 left (f. 154v): two cipher blocks with clear text between and after, signed Forget at Bordeaux.
- Canvas 208 (f. 201): the clear words *Le regard dud. siege il s'advance fort* followed by the code 36 inside the
  cipher block, as #64 reports.
- Not checked here: the names in ff. 196/201 figure by figure, the f. 173 and ff. 123-124 decodes, and Brackx's
  transcription of the copies beyond the lines quoted above.

## Contributions of 22 Oct 2026 (Michael Brackx, issues #73, #77, #78, #79, #83)

Brackx re-transcribed every Cipher-1 leaf from full-size, deskewed line crops (openapi.bnf.fr IIIF) in a new label set
that keeps apart figures Tomokiyo's table separates and our transcriptions had merged, and decoded each with a per-leaf
key (beam search under his own French 5-gram from Montaigne). His figures and keys are in `brackx2026/` (copied from the
issues; his readings are summarised here). Credit in `profile.json` (provenance `mixed`).

| issue | leaves | what it adds |
|---|---|---|
| #73 | fr. 15571 f. 177r (29 lines) and **f. 177v (11 lines, new)** | the Pons–Taillebourg plan (Taillebourg's toll on the Charente, *trente mil escus* from the country) given up when **[84] = le vicomte de Turenne** took the field with guns; matches the archivist's summary on the leaf; 24 = *mais*, 27 = *nostre* |
| #77 | **f. 154v, two blocks of 10 and 11 lines (new)** | the first figure-by-figure test of the key against a contemporary copy (f. 157r); figure splits δ = c / ∂ = s, θ = m / ɟ = s, ꝭ = x, ⊔ = q; 51 = *pas*, 47 = *tous/tout* |
| #78 | the f. 18/19 crib completed: ff. 18r (22 lines), **18v (34), 20r (17)**; ff. 123-124 re-transcribed (36/41/41/38 lines, f. 124r-v completed) | codes **15 = quoy, 73 = oi** (syllable), **78 = le roy de Navarre**, **82 = le gouverneur de Coul[…]**, 84 = le viconte de Turenne, 44 = a stop or null (not *Sire*); code groups split into two figures in the old files (`4 9` = 49, `t 8` = 48, `8 t` = 84); ff. 123-124: Mayenne at Marmande, March 1586, no money, contributions only by garrisons, Turenne back over the Garonne |
| #79 | f. 110 (38 lines, all) | the leaf has 38 cipher lines, not 54 (checked on canvas 116 here); it reads: Mayenne to Villeroy, Bellebourg, March 1586, on war without money and his reputation |
| #83 | ff. 143r-v, **150r (32 lines, new)**, 150v, 154r, 173, 196 (31/31), 201 | the repo's `f150_cipher.txt` is the **verso**, f. 150v; f. 150r (canvas 157 right, checked here) was never transcribed; splits θ = m / ϑ = s, ꝺ̄ = u, ɛ = i; codes **46 = rien, 61 = beaucoup**, 34 = *ainsi*; eleven code groups the old files had split into two figures; five misreadings of the copies f. 155r and f. 157r and seven of f. 156r corrected |

**Validated here (22 Oct 2026), `brackx_validate.py` -> `brackx_validate.json`.** His transcriptions and keys, decoded
with this project's beam and period-French 6-gram (`lm.pkl`), not his decoder. Control: each key's letter sets
permuted among its figures, set sizes kept (so the decoder keeps its freedom), 3 seeds.

| leaf | tokens | read as sense (floor) | clear copy, letters matched (floor) | his figure |
|---|---|---|---|---|
| fr. 15571 f. 177r / 177v | 863 / 301 | 0.60 (0.11) / 0.62 (0.18) | none | — |
| f. 154v block A / B | 360 / 350 | 0.61 (0.15) / 0.74 (0.12) | f. 157r: 0.90 (0.37) / 0.94 (0.38) | 95.7 / 96.4% |
| f. 18r / 18v | 722 / 1,163 | 0.50 (0.06) / 0.61 (0.06) | f. 19 (his reading): 0.86 (0.27) / 0.74 (0.23) | 85.9 / 80.8% |
| f. 20r | 575 | 0.60 (0.07) | its copy (end of f. 19v) is not in the issue | 86.7% |
| ff. 123r / 123v / 124r / 124v | 1,113 / 1,374 / 1,405 / 1,183 | 0.47 / 0.56 / 0.61 / 0.68 (0.06-0.11) | none | — |
| f. 110 | 2,164 | 0.61 (0.14) | none | — |
| f. 143r | 704 | 0.70 (0.14) | f. 155r: 0.94 (0.31); with his corrections 0.95 | 94.4% |
| f. 143v | 1,212 | 0.71 (0.08) | f. 155r, the 25 lines it covers: 0.88 (0.31); corrected 0.90 | 88.8% |
| f. 150r | 1,132 | 0.66 (0.06) | f. 155v: 0.84 (0.25) | 87.0% |
| f. 150v | 441 | 0.63 (0.10) | f. 156r as read in #70: 0.83 (0.36); corrected 0.91 | 90.2% |
| f. 154r | 1,056 | 0.63 (0.04) | f. 157r: 0.90 (0.28); corrected 0.91 | 89.8% |
| f. 173 | 1,072 | 0.50 (0.14) | none | — |
| ff. 196 / 201 | 975 / 972 | 0.59 (0.10) / 0.71 (0.07) | each other: 0.78 (0.50-0.52) | 79.5% |

His copy percentages reproduce within 1-5 points with a different decoder and language model; the f. 18v gap (74 against
81%) is the largest. The copy readings marked "corrected" were re-read by him with the cipher beside them, so they are
not independent; the uncorrected readings (#70) give 0.83-0.94 on their own. Every leaf stands far above its control.
Image checks here: canvas 157 right is f. 150 (159 struck), a clear opening then about 32 cipher lines; canvas 116 right
(f. 110) has about 38 lines. Not checked here: his figure labels line by line (no second reader has done so) and his
reading of the copies of f. 19 and f. 19v.

**Taken in:** the transcriptions (`brackx2026/*_cipher.txt`; for measuring they supersede `f110_cipher.txt`, `f123*`,
`f124*`, `cipher_f143.txt`, `f143v_cipher.txt`, `f150_cipher.txt` (= f. 150v), `f154_cipher.txt`, `f173_cipher.txt`,
`f196_cipher.txt`, `f201_cipher.txt` and `f177_cipher.txt`, which are kept), the per-leaf keys, the code values above
and the figure separations. **Not taken:** 64 = *un* and `me` = *mesme* (open, as he says); the f. 20r copy agreement,
which cannot be checked without its copy text. The keys differ from leaf to leaf (θ = m on ff. 143, 150, 154r but m/s on
ff. 173, 196, 201): a merged key for the whole target is still to be made.

## One key, 22 Oct 2026

`merge_keys.py` -> `key_merged_union.json`, `merge_keys.json`. Brackx's eleven per-leaf keys were merged by union: each
figure takes every letter any leaf gives it, each code every value (a word in one leaf beats `+` in another). Decoded
with this project's beam and 6-gram and scored as `brackx_validate.py`, the union key reads **every leaf as well as or
better than its own key**: 9,855 of 15,705 document tokens against 9,609, copy agreement unchanged within a point
(f. 143r 0.93, f. 154r 0.89, f. 154v 0.89/0.93, f. 150r 0.85, f. 150v 0.90 on the corrected copy), scrambled floor 0.121
against 0.100. So the differences between the per-leaf keys (θ = m or m/s, e/ɛ) are differences of hand and reading,
not of key, and the target has one key. Pruning the union (dropping letters a figure took in under 5% of its
occurrences) lowered the score (0.628 -> 0.610; f. 110 0.62 -> 0.57) and was dropped.

Open codes, retried (`code_lm_test.py`, `code_lm_test.json`, and the copies):
- **59 = argent**, adopted: f. 154r "nous prester icy de l'[59] a rendre a Paris" is "de l'argent à rendre à Paris" in the
  copy f. 157r; the other four contexts fit (f. 124r "pour faire [59] pour l'employer", f. 154r "leur [59] leur seroit
  rendu a Paris", f. 173 "recouvrer de l'[59] soubs ses obligations", "qui avoient de l'[59]").
- 44: at a sentence end both times it meets the f. 156r copy (f. 150v); a stop, as Brackx said (already read as nothing).
- 9: "Comme il estoit" in one copy context (f. 150r), "Mais s'il y avoit" in the other: not one word; open.
- 103 (f. 18v): the f. 19 copy itself has an unread word there, before "chevaulx légers"; open.
- me = *mesme* ("a eu mesme advis de Bourdeaux") and 64 = *un* ("avec un peu de forces") fit, no copy covers them; not adopted.
- Ranking candidate words by the 6-gram over 30-letter contexts does not work: the model picks two-letter function
  words everywhere (it would make 59 *es*). Recorded as a failed step.

`final_texts.py` -> `key_cipher1.json` (union + 59), `final_texts.json`, `texts/<doc>.txt` (per line: figures, then the
decode cut into words, upper case inside a sense run, `|...|` outside one, `[nn]` open codes; the clear copy appended
where there is one). Per document 0.51 (f. 123r) to 0.77 (f. 201).

## Remaining gaps

- unread share of every leaf (23-49% of tokens outside sense runs; ff. 123r and 173 lowest) - blocker: open-codes; with the merged key the decode agrees with the clear copies on 85-93% of letters, so most of the residue is spelling the corpus does not know, single-figure slips and the open codes below; a second reading of the figure labels is still workable
- code groups 16, 19, 23, 45, 64, 101, 102, 103, `me`, 9, and the name code 98 - blocker: open-codes; one to three contexts each, none in a clear copy (64 = *un* and `me` = *mesme* fit, not adopted; 9 is two different words against the copies)
- the copy of f. 20r (rest of f. 19v, about 11 lines) - blocker: open-codes; read by Brackx but not given in #78, so his 86.7% for f. 20r is unchecked here

## Escalation

- [x] siblings: ff. 14/15 and 18/19 cribs used to re-derive and verify the key; f. 78v margin decipherment used as a control (`cribem.py`); ff. 196/201 aligned (57% identical figures; Brackx's joint alignment, #64); f. 125r clear letter read for context; canvases 128-139 round ff. 123-124 checked for a copy, none (Brackx, #71). The f. 18/19 crib completed through f. 20r (Brackx, #78). Not yet: ff. 91-92
- [x] clear-pages: **ff. 155-157 are the contemporary clear copies of ff. 143, 149v-150 and 154r-v** (Brackx, #70; checked here). f. 144 is a separate letter; f. 19 is the decipherment of f. 18; f. 125r is a clear letter
- [x] known-keys: Cipher-1 done (Tomokiyo's table, re-derived and verified on every Cipher-1 leaf); the Cipher-3 leaves and their key are matignon1586c3; the Cipher-2 leaves (ff. 218-219, fr. 15573 ff. 120, 385) are mayenne1586c2
- [x] print: BnF catalogue and literature searched 17 Sept 2026, no printed decipherment; Tomokiyo's cryptiana openings for ff. 143, 150, 154, "111" used as checks
- [x] key-rebuild: key re-derived from the ff. 14/15 and 18/19 cribs, confusable figures modelled as letter sets, code values such as 17 *car*, 25 *nous* and 52 *plustost* added from context and the crib; Brackx's letter sets and eleven code values from the clear copies (`key_contrib.json`); his per-leaf keys and codes 15, 34, 46, 51, 61, 73, 78, 82, 84 (`brackx2026/`, 22 Oct), merged here into one key (`key_cipher1.json`, union; pruning tried and dropped); 59 = argent from the f. 157r copy
- [x] retry: every Cipher-1 leaf re-transcribed in full and re-decoded by Brackx (issues #73, #77-#79, #83, 22 Oct 2026) and re-scored here with this project's decoder and a control (`brackx_validate.py`); every open code retried against the copies and by LM ranking (`code_lm_test.py`), 59 recovered

## Assumptions for George's review

- Your 2022 solution of fr. 15572 f. 43, which stood on this entry as a "prior solution" credit, is removed: f. 43 is
  not one of this entry's documents and its cipher was not identified here as Cipher-1. It is credited nowhere until
  its key is shown.
- f. 79r is treated as Cipher-1 (the solved key reads it); the earlier "Cipher-2 crib" values from it stay withdrawn.
- ff. 143r-v, 149v-150 and 154r-v now count as read from an existing decipherment (the clear copies ff. 155-157, outcome.parts), while the key decode of the same leaves stays in the measure. Is that the right split, or should those leaves leave the key-read part altogether?
