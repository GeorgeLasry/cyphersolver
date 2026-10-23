# ff. 124r–v: reading log (22 Oct 2026)

Brief: `READING_BRIEF.md`. Leaf name f124. Images: Gallica canvases 130 (right half = f. 124r, 4248 × 6368) and 131
(left half = f. 124v, 4248 × 6369) of fr. 15572 (ark `btv1b9061879d`), fetched at full resolution from openapi.bnf.fr
IIIF (gallica.bnf.fr/iiif answers 403). Each manuscript line was cut as two half-line bands at 0.85×, with line
centres found by ink projection. About 40 single-figure crops were made at 1.2–2×. All crops are in the session
scratchpad, not in the repo. Transcription: Michael Brackx, `brackx2026/f124r_cipher.txt` (41 lines) and
`f124v_cipher.txt` (38 lines). Scratch scripts (corrections, forced alignment, the checker's per-sentence view) were
kept outside the repository; what they established is recorded here.

## Pass 0: the published decodes

`_check_reading.py --file` on the mechanical decodes (Brackx's figures, `key_cipher1.json`, beam + 6-gram):

| file | sentences clean | share | hole rate |
|---|---|---|---|
| `texts/f124r.txt` | 8 / 29 | 0.276 | 0.196 |
| `texts/f124v.txt` | 3 / 26 | 0.115 | 0.214 |
| both | 11 / 55 | **0.200** | |

## Pass 1: a word-level draft

The f. 110 pass's word Viterbi (dictionary words only, word bigrams from Henri IV's letters) was run on both pages.
It found most of f. 124v at once (*toutesfois n'en aiant point de plus propre pour traicter*, *ledict sieur de
Gourgues emprunter*, *attacquer saincte basile sitost*, *la pouldre … necessaires comme il*, *le vicomte de Turenne
est venu a Nerac*, *repasser la Garonne*, *seiourner ici ou ie le desirerois mieux que*). On f. 124r it gave
fragments only (*la retenir que en moins d'un*, *preparer … il lui plaira que la dicte ar…*, *de ceux de ceste
armée prendre le peu de secours que l'on nous*, *de ma part ie ne discontinuerai point*, *pour faire argent pour
i employer*). It is a draft, not a reading.

## Pass 2: every line on the image, reading against the letter sets

All 79 lines were looked at in two halves. Each word was built from its figures' letter sets, and each break was
compared figure by figure with Brackx's labels. Then the hypothesised plaintext of each line was forced back onto
the corrected figures (each figure must give a letter of its set; a substitution, null or missing figure costs 1 to
1.2). This was a check that no letter of the reading is supplied from context. After the corrections, 62 conflicts
are left on f. 124r and 40 on f. 124v. Most of them are the holes listed below, or a word split differently at the
line end.

What the images showed (`brackx2026/corrections/f124.tsv`, 65 rows; token indexes are 0-based on Brackx's original
lines; corrected figures in `brackx2026/corrections/f124_cipher.txt`):

- **One label, several figures.**
  - Brackx's `tm` covers three shapes. The crossed d is m/s, as in the key. A filled b with a side stroke is
    **a**: *de la secourir*, *au moins*, and the [..]*aire* of l. 1. In one place the label stands for the
    g-shaped y: *ruinée*.
  - His `q1` covers two shapes. The crossed q is o. An o with a cross above it is **u**: *souvent*, *pouoir*
    (twice), *recou|vrer*, *nouuelles*, *trouue*. He also wrote this second shape as `S` once.
  - His `Cl` and `U` cover a large hooked C, which is l (*mal*, *-bles*, *cela*), and a small curl, which is **s**
    or l (*Sire*, *sont*, *service*, *suis*, *ennemis*, *jurats*, but *elles*).
  - His `ao` / `oo2` for the sigma-shaped o is, in pairs, the barred double o, **ff** (as on f. 173): *deffase*,
    *soffrent*, *deff-*, *deffaveur*, *l'eff[o]rt*.
  - Seven letter values were added for this leaf in `key_cipher1_f124.json`; the shared key is unchanged:

    | label | value | where it is needed |
    |---|---|---|
    | `ba` | a | the filled b |
    | `qx` | u | the o with a cross above |
    | `ls` | s, l | the small curl |
    | `oob` | ff, f | the barred double o |
    | `dc` | c, m | the looped d is m in *Matignon*, *l'armée* (twice) and *Monsieur* |
    | `60` | open code | see the open codes below |
    | `67` | open code | see the open codes below |
- **Code groups read as letters, or letters read as codes.**
  - f. 124r l. 5: `o B` is the numeral **68** (*ou si Vostre Majesté connoist ses moiens*).
  - f. 124v l. 8: `y y` is **59** (*et argent et draps*).
  - f. 124v l. 34: `7 61 t` is **76 14** (*ledict sieur [Roy de Navarre] que de séjourner*).
  - f. 124r l. 5: `47` before *-is* is the 4-shaped m and 7 (*mois*), as Brackx found on f. 196.
  - The heavy "6o" group (f. 124r l. 4; f. 124v l. 9, Brackx `B` and `6 o`) and the "67" group (f. 124v ll. 32 and
    37, Brackx `B y` and `6 7`) are each one code group. Neither has a value.
- **Omissions.**
  - Four figures written above f. 124r l. 26 with a caret: *veoi* (*que je [veoi] la pluspart*).
  - Three figures written between ll. 7 and 8 above a caret, which Brackx read as `U`. Their place in the word is
    not settled.
  - An o in *coura-ge* (l. 29), an o in *sauroit* (l. 4), and a second figure after the crossed q in *nouuelles*
    (f. 124v l. 30).
- **Not figures.** A long pen stroke in the left margin of l. 7 and a separator bar later on that line (both
  Brackx `S`). A flourish at the end of l. 1 (`he`): the word runs on, *d'ore|snavant*.
- **The writer's cancellation.** Two figures struck through on l. 9 (`t 3`).
- **Single misreadings.**
  - `y`/`E2` (*sieur*), `S`/`f` (*marschal*, *ceulx*), `h`/`3` (*monsieur*), `h`/`y` (*Gourgues*), `E`/`E2`
    (*ville*), `X`/`lam` (*bon nombre*), `ff`/`B` (*repassé*), `ao`/`y` (*suivre*).
  - `t`/`c`, `t`/`tm` and `ff`/`w`: *pendant*, *camper*, *m'aura*, *[?mandé]*.
  - `ao`/`w` and `m`/`w` in *pied*; `n`/`m` in *et*.
  - `tm UNK`/`ao E E` in *attendant* (the crossed double stroke is tt, as in *mettre* and *attendant*).
  - `UNK`/`om` in *qu'ils* and *cinq*.

`_check_reading.py --file texts/reading_f124.md` after pass 2, before the second round of image checks:
120 sentences, 70 clean, 0.579.

## Pass 3: the line markers, and a second round of crops on the remaining breaks

Line markers in the middle of a word make the checker split the word, so a divided word was put after the marker
of the line it ends on. More crops then settled three words: l. 32 *attendant* (the crossed double stroke is tt)
and *nouuelles* (a small s figure, u, at the line end, not m), and f. 124v l. 5 *suis* (the small s, not S).
Crops of l. 12 (*Q u e ‡ i*), l. 14 (*A* in *[?délivrance]*), l. 15 (*[?espres]*, and the four figures before
*vostre*), l. 28 (*[?crains]*), l. 33 (*[?vendre]*), ll. 38–40 (*[?parlement]*, *[?exhorter]*) and f. 124v
ll. 2 and 11 (*[?combien]*, *[?je]*) showed the figures as transcribed, so these stay holes.

## The beam on the corrected figures (a control, not the reading)

The project's beam and 6-gram, run on the corrected figures with the leaf key, now gives a fair draft of most lines
(f. 124r l. 32 *rersoiendelentretenirattendantdeuosnouu*, f. 124v l. 21 *cinqcanonsetlapouldre*). It still breaks
where the sets are wide: *ouienesuisuenuqueluisuostreesprercomande*, *estearmeprendre*, *uetoutcequilpourarecomrer*.
As on ff. 173 and 110, the reading was made by hand from the sets.

## Check results

| pass | file | clean sentences | share | hole rate |
|---|---|---|---|---|
| before | `texts/f124r.txt` + `texts/f124v.txt` | 11 / 55 | 0.200 | 0.196 / 0.214 |
| 2 | `texts/reading_f124.md`, whole file | 70 / 121 | 0.579 | 0.141 |
| 3 | `texts/reading_f124.md`, whole file | 72 / 120 | **0.600** | 0.137 |
| 3 | the same, reading only (f. 124r and f. 124v sections) | 37 / 61 | 0.607 | 0.106 |
| 3 | f. 124r section only | 16 / 32 | 0.500 | 0.129 |
| 3 | f. 124v section only | 21 / 29 | 0.724 | 0.078 |
| 3 | `texts/reading_f124_en.md` | 55 / 73 | 0.753 | 0.089 |

The checker counts a `[?word]` as two holes when the word is not in its list, and it also counts period spellings
the figures give: *avoict*, *estoict*, *donnoict*, *soffrent*, *proposicion*, *deffaveur*, *secors*. **f. 124v
reaches the bar and f. 124r does not.**

## What failed or stays open

- **Codes:** 60 (f. 124r l. 4; f. 124v l. 9, *ordre [60] faire monstre*, where *de* or *pour* fits), 67
  (f. 124v l. 32 *avec quelque [67]*, l. 37 *pour nostre [67]*; a noun like *troupe* or *forces* fits both),
  `me` (f. 124v l. 38). No clear copy covers them.
- **Figures checked on the image that do not make the word.** These are not image defects; the figures are clear.
  So each is either a value the key lacks or a writer's slip.
  - On f. 124r:
    - l. 4, the four figures after code 60 (*σ o Ɛ ɗ x b m*, which suggest *-isent*).
    - ll. 7–8, the word after *que le*: *c o n s i | d r i e …* with the three interlinear figures.
    - l. 10, *[?armée]* (no m).
    - l. 11, *[?affin]* (crossed 4, slashed q, dotted cross).
    - l. 12, *[?Quercy]* (q u e ‡ i).
    - l. 13, *[?deffraier]* (*d e ff r a e r*).
    - l. 14, *[?délivrance]* (A gives l, not n), and the figure before *à une autre fois*.
    - l. 15, the four figures before *vostre* (*ȼ g b ʃ*), and *[?espres]* (the last figure is r/i).
    - l. 18, the unknown figure in *qui [¤] avoict*.
    - l. 20, *[?sçai]* (s + barred o + a).
    - l. 21, *[?préjudiciables]* (*p e i u d i c a b l e s*).
    - ll. 22–23, the words after *si elles tant*.
    - l. 25, *leur […]* (*p a r o i c o ¤ e*).
    - ll. 27–28, the verb after *nous a* (*d | o i e*).
    - l. 28, *[?crains]* (the first figure is the crossed d, m/s).
    - l. 29, *[?de] bien servir* (*d a*).
    - l. 33, *[?vendre]*.
    - l. 37, the eleven figures after *pourra recouvrer*.
    - l. 38, *[?ceulx]* and *[?parlement]*.
    - l. 39, *[?ladite]* and *[?exhorter]*.
    - l. 40, *[?exemple]* and *[?Toulouse]* (*t u o | u l o u s e*).
    - l. 41, the words round *province*.
  - On f. 124v:
    - l. 2, *[?combien]* (a hooked f-like figure where b is needed; perhaps the b figure of f. 110, not adopted).
    - l. 6, the verb after *luy en* (*e n o n n e r*).
    - l. 11, *[?je]*.
    - l. 12, *[?uniesme]* (*ung n i e s m e*).
    - l. 13, *[?Thonains]* (*t h o n a i/n s*).
    - l. 14, *[?et]*.
    - l. 17, *[?est]*.
    - l. 18, the place taken (*[?Castels]*, *ʃ a s t e l s*) and the words before *Pasques* (*d i f a i e e*).
    - l. 23, *[?mandé]* (*m a e a n d e*) and *[?seré]*.
    - l. 30, the river (*d o r d ? e*).
    - l. 37, the participle before *audict siège*.
- **The beginning of l. 1** (*[…]aire*) belongs to the last word of f. 123v, which another pass is reading.
- **The clear end** is in a small cursive hand. Two words and the day of the month were not read from the image at
  this resolution.
- No second reader has checked Brackx's labels on these two pages beyond the crops made here. The hand uses at
  least four shapes that one label covers (above), so a figure-by-figure re-transcription against a labelled atlas,
  as recommended for f. 110, would probably resolve more of the breaks on f. 124r.

## Pass 2 on f. 124r (22 Oct 2026): figure-by-figure re-transcription

**Image.** Canvas 130 right at full size (4248 × 6368, openapi.bnf.fr IIIF). Each of the 41 lines was tracked in
nine windows (line centre = a shared page-curve shape plus a per-line slope, fitted robustly) and resampled into a
straight band 124 px high; each band was cut into figures by an ink projection and shown at 1.5× in three parts
with every figure numbered; doubtful stretches were re-cut at 2.2–4×. f. 124v (canvas 131 left) was tracked the
same way for exemplars. Crops in the session scratchpad (`f124v2/`), not in the repo. Lines 18 (right half) and 25
(right half) bend more than the fit; they were read on raw crops of the page instead.

**Exemplar set.** An automatic token-to-figure alignment (width model, splits and merges allowed) was tried to cut
one contact sheet per label from both pages. It drifts: on the lines where the counts agree by chance the sheets
still mix neighbouring figures, so it was not used as evidence. The exemplars actually used were figures read by
hand on lines that read: f. 124v l. 9 (*je veoi qu'il n'y a ordre [60] faire monstre aux gens*), where the o with a
horizontal bar is **a** three times (ao) and the heavy "6o" group is code 60 again; and on f. 124r the sense-checked
words of pass 1 (the small curl s in *Sire*, *sont*, *suis*; the crossed d m/s in *meine*, *remettant*; the
omega-shaped q in *Quercy*, *qu'il*). No full labelled atlas of the hand was finished.

**What the image showed** (`brackx2026/corrections/f124r_v2.tsv`, 10 rows, token indexes 0-based on the lines of
`brackx2026/corrections/f124_cipher.txt`; corrected f. 124r figures in `brackx2026/corrections/f124r_v2_cipher.txt`):

| line | change | gives |
|---|---|---|
| 4 | the o with a rising flourish after code 60 is the sigma of f. 110 (sg = f), not Brackx's double-o d | *[60] [?faisant]* (f a i s a n t); sg = f is not otherwise attested on this leaf, so the word stays marked |
| 10 | a small crossed stroke with a looped foot is the crossed d (m/s), not t | *ladicte a\|rme[e] soit* |
| 17 | a small curl (s) missing between v and the hooked d | *que sans cela* |
| 20 | the barred o is ao (a), the next figure a plain o (i), and an omega q was missing | *je sai qu'el\|les* |
| 22 | the last figure is the pound-shaped r, not E2 | *si elles tant sur* |
| 23 | the small curl (s), not the hooked C (l) | *les lieus* |
| 25 | Brackx's unknown figure is the omega d/q (w) | the word (*p a r o i c o d e*) still does not form |
| 28 | a 6 written over an E2 (the writer's own correction) | *nous a d\|oné* |

**Checked on the image and left as transcribed** (the figures are clear and do not make the word; key gap or
writer's slip): l. 7–8 *con-* + crossed d + o + a small a-shaped figure at the margin, then *d r i e*, with the
interlinear *c ϑ 3* after the caret; l. 11 *[?affin]* (crossed 4, slashed q, dotted cross, E2: *o u ? i n que*);
l. 12 *[?Quercy]* (q u e c y: no r figure); l. 13 *[?deffraier]* (no i); l. 14 *[?délivrance]* (the A is l on every
other line of the page) and the Ω figure before *à une autre fois*; l. 15 the four figures after *que* (a hooked
d with a tall stem among them) and *[?espres]* (the last figure is an e with a stroke below); l. 18 the figure after
code 13 is an ink blot (on the image); l. 21 *[?préjudiciables]* (no r, one i); l. 23 the crossed d after *lieus*
and *[?parlent]* (a crossed figure where n is needed); l. 25 *p a r o i c o d e*; l. 28 *[?crains]* (a tall crossed
d where c is needed); l. 29 *[?de]* (w o) and an extra filled-b figure in *courage*; l. 31 *[?effort]* (two sigmas,
then r: no o); l. 33 *[?vendre]* (a g-shaped figure where d is needed); l. 37 *[?recouvrer]* (a tall crossed figure
for *uv*) and *a e o u r d e a u s c* before *j'ay aussi*. Lines 38–41 were not re-cut in this pass (pass 1 crops).

**Key.** No value was changed in `key_cipher1_f124.json`: every change above is a label (sg, tm, ls, ao, o, om, L,
w and 6 already carry the needed letters), so f. 124v, whose figures were not touched, reads as before.

**Check results** (each section cut to a scratch file and scored alone):

| pass | file | sentences | clean | share | hole rate |
|---|---|---|---|---|---|
| 1 (pass 3 above) | f. 124r section | 32 | 16 | 0.500 | 0.129 |
| 2 | f. 124r section | 32 | 18 | **0.562** | 0.119 |
| 2 | f. 124r section, English | 35 | 26 | 0.743 | 0.085 |
| 2 | f. 124v section (unchanged) | 29 | 21 | 0.724 | 0.078 |
| 2 | `texts/reading_f124.md`, whole file | 120 | 74 | 0.617 | 0.133 |

f. 124r is still below the bar. The remaining breaks were all looked at on the image and the figures are legible,
so they are not image defects (except the blot on l. 18): either this hand uses letter values the merged key does
not give (A for n, a tall crossed d for c or uv, g for d) or the writer slipped. A third pass would need a real
labelled atlas of this hand (hand-mapped f. 124v lines, not the automatic alignment) to test those values across
both pages before adopting them.

## Pass 3 on f. 124r (22 Oct 2026): a per-label atlas of the hand, tested on the open words

`_check_reading.py --file` on the f. 124r section alone (cut to a scratch file), before: 32 sentences, 18 clean,
**clean share 0.562**, hole rate 0.119.

**The atlas** (method in `reading_f123_log.md`, Pass 3): all 5,111 tokens of ff. 123r-124v mapped to their cut figures
by an alignment with width and appearance models per label, checked on overlays, each token given its letter from the
current readings by forced alignment (f. 124r: 1,331 tokens carried, 30 against the reading), and contact sheets made
per label and per family. Crops in the session scratchpad, not in the repo.

**What it shows for this page** (counts over the four pages; split accuracy from a classifier trained on the other leaf):
- **A** is one shape and l in all 20 places, including *[?délivrance]* (l. 14): so the A there is a slip of the
  writer for n, not a second value; A = n is not adopted.
- **tm / th**: the crossed oval (θ) is m and the tall crossed d is s (f. 124: 39 of 45 m, 55 of 60 s; f. 123 about
  the same), with one figure in ten the other way, so the sets stay m/s. On l. 22 the figure after *peult estre* is the
  θ: the run reads *m i e l l + estant*, not *si elles tant*; written **[?mieulx] estant sur les lieus** (m, i, e, l
  carried; u and x not written, the second l where x is wanted). The figure after *lieus* (l. 23) is the tall d, s:
  a doubled s, left […].
- **y** is two shapes: the v-shaped y is g, the g-shaped figure (plain or barred) is u. The long-barred crossed g of
  l. 11 (*[?affin]*), l. 15 (before *vostre*) and l. 41 is the u-figure, as in *fruicts* and *puisqu'ils* on f. 124v;
  with it *[?affin]* gives *o s/u u i n*, still no word; the four figures before *vostre* (l. 15) give *a u* + a
  filled 6 (i/n/s) + a tall-stemmed d (s/c): *auis*, *auns*, no word that fits.
- **B**: the Ω-shaped figure is e and the looped b i/n. The hole after *faveur* (l. 14) is the Ω (e): *faveur e à une
  autre fois*, still not a word; left […].
- The small curl (ls here, U and Cv elsewhere) is s or x, never l (8 of 8 ls are s).
- **Label change** (`brackx2026/corrections/f124r_v3.tsv`, 1 row; corrected file `f124r_v3_cipher.txt`): l. 7 token
  32, y -> th: the figure is the tall crossed d (s), not a y. The reading already had s (*con s i-*).

**Checked and left as they are** (the figures are the ordinary shapes of their classes, so these are slips or words
not recovered): *[?Quercy]* (q u e c i, no r; the last figure is E2, the i the writer also uses for y),
*[?deffraier]* (seven figures for eight letters), *[?espres]* (the last figure is an e with a stroke below,
not the e of the e sheet), *[?préjudiciables]* (no r, one i), *[?parlent]* (the h figure, e/u, where n
is wanted), *[?crains]* (the first figure is the tall crossed d, s, where c is wanted), *[?effort]* (the o figure,
i/a, where o is wanted), *[?vendre]*, *[?recouvrer]*, ll. 7-8 *[?consi…]* (the second figure of l. 8 is the r/f L;
the three interlinear figures are not placed), l. 41.

**Codes from other leaves.** 64 = *quelque*, 62 = *peu*, 73 = *le Roy*, 63 = *après* were tried in the slots of 60
(*l'on ne sauroit [60] [?faisant]*, *ordre [60] faire monstre*) and 67 (*avec quelque [67]*, *pour nostre [67]*). None
fits; not adopted. 60 still wants *de* or *pour*, 67 a noun such as *troupe*.

**Key.** No value adopted; `key_cipher1_f124.json` is unchanged.

| pass | file | sentences | clean | share | hole rate |
|---|---|---|---|---|---|
| 2 | f. 124r section | 32 | 18 | 0.562 | 0.119 |
| 3 | f. 124r section | 32 | 18 | **0.562** | 0.121 |
| 3 | f. 124r section, English | 35 | 26 | 0.743 | 0.088 |
| 3 | `texts/reading_f124.md`, whole file | 136 | 81 | 0.596 | 0.143 |

The share does not move: the one sentence changed (*Ce que je comprens, peult estre, [?mieulx] estant sur les lieus
[…] que ceuls qui en [?parlent] de plus long*) still has more holes than its length allows, now with a sense.

## What stays open on f. 124r after pass 3

The atlas was the escalation step pass 2 asked for. It finds no letter value the merged key lacks: the breaks are on
figures that are the ordinary shapes of their labels, so they are the writer's omissions and slips (A for n, h for n,
the crossed d for c, one figure short in *Quercy*, *deffraier*, *préjudiciables*), words still not recovered from
their sets (l. 4 after code 60, ll. 7-8, l. 15, l. 25, l. 37, l. 41), and the codes 60 and 67. The page stays below
the 0.70 bar; a further pass would need a clear copy of the despatch or another letter in this hand with the same codes.
