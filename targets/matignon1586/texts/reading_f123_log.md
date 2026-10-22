# ff. 123r-v: reading log (22 Oct 2026)

Brief: `READING_BRIEF.md`. Leaf name f123, one reading for both pages. Images: Gallica canvas 129 right (f. 123r) and
130 left (f. 123v), fetched full size (8500 x 6370) from openapi.bnf.fr IIIF (gallica.bnf.fr/iiif answers 403). Line
and figure crops were kept in the session scratchpad, not in the repo. The work was split three ways: f. 123r ll. 1-18,
f. 123r ll. 19-37 and f. 123v were each read by one pass, with the figure findings passed between them. The scratch
tools (letter sets per line, a forced aligner of a French hypothesis onto the figures, a word-level beam over the
Henri IV letters) stayed outside the repo; what they established is recorded here.

## Before

`python docs/_check_reading.py --file` on the mechanical decodes (merged key, `final_texts.py`):

| file | sentences clean | share | hole rate |
|---|---|---|---|
| `texts/f123r.txt` | 1 / 21 | 0.048 | 0.283 |
| `texts/f123v.txt` | 5 / 27 | 0.185 | 0.225 |

## Pass 1: the letter sets read by hand (worked)

Each line was printed as the letter sets of its figures and read word by word; the beam decode was used only as a
first draft. Most of f. 123v and much of f. 123r form with no change of figure: *plus grande que je ne l'avois*,
*commançant à sortir les*, *de tous les gens de*, *nous serions*, *à quoy je suis si mal préparé que de plus de cent
mile escus qu'il faudroict*, *non pas pour les paier d'un mois*, *Monsieur [le …] de Matignon me mande qu'il a esté
contrains d'emprunter plus de vingt mil escus pour l'entretenement des …*, *il faict estat que je face rembourcer à
mon arrivée*, *je me voi en tele peine que je ne sai aucun moien*, *de fatigues et de maladie*, *que les mestres de
camp*, *les compaignies*, *sans faire monstre*; on the verso *utile pour vostre service*, *de vostre conseil*,
*après avoir faict tant de despense de conserver ceste*, *de la province où*, *du Daulphiné quand j'y estois*,
*aucun secours, je suis contraint de recourir*, *ce porteur*, *pour vous supplier*.

## Pass 2: the breaks on the image (worked)

126 rows in `brackx2026/corrections/f123.tsv` (47 on f. 123r ll. 1-18, 21 on ll. 19-37, 58 on f. 123v; 36 carry
` ?`: read from context or not enlarged). Corrected figures in `brackx2026/corrections/f123_cipher.txt`.

- **Brackx's U is two figures.** A V with an underbar (`Uv`, e/u: *nécessité*, *remis*, *cent*, *Monsieur*) and a C
  with a small v on its top right (`Cv`, s/x: *tousiours*, *ie suis*, *escus*). The same Cv also stands where Brackx
  writes Cl (*armées*, *demandes*, *mois*, *ès mains*, *Monsieur*, *qu'ils*); the Cl proper (a C with a loop inside)
  is l (*13 Cl* = *qu'il*, *que l'on*, *clameurs*).
- **Looped double s = ée/é** (`ssl`): *armées* (f. 123r l. 2), *armée* (l. 14; f. 123v ll. 1, 8, 41), *employée*,
  *arrivée*, *demourés*. Brackx labels it ff, B or yy.
- **dc = m on this leaf** (key: c): *clameurs* (l. 5, Brackx oo), *Monsieur* (l. 14), *me mande* (l. 15), *à mon
  arrivée*, *maladie*, *impossible*, *monstre*, *moiens*.
- **ff = o as well as n** (leaf value; ff = n stays in *non*, *contrains*, *maintenant*, *ne*): *retrouverions*
  (l. 2), *tous ensemble* (l. 8), *comptant* (l. 10), *fournir* (l. 35) — four independent words.
- **The figure "6i" is code 61** (*beaucoup*, l. 4), not B + o: *maintenant beaucoup plus grande*.
- **Code 25 twice** (l. 1, *nous nous*): Brackx's extra *s* is the s-shaped 5 of the first 25.
- **Struck figures** read as nothing (`del`): an ink-blotted figure in *demandes* (l. 6), a struck c-with-bar after
  *ensemble* (l. 8), a crossed q (l. 26), a struck M (l. 28). **A slash** after *ensemble* (l. 8) and in l. 4 is a
  virgule (`virg`), as after *Sire* in the clear text.
- **The d with a crossed stem is u** (`ub`): *trou[v]e* (l. 3), *pou|voir* (l. 24), *peuuent*, *pouant* (verso).
- **Other relabels:** a flat-topped 3 for y in *mains* (l. 13); a small hooked c as r in *pour* (l. 11); Ze for Cl in
  *estreme* (l. 32); 3 for h (l. 21); on the verso the barred double o = ff (`oob`), the open ß = ss (`szl`), the
  L with a curved foot = pp (`brace`: *supplier*, *approués*), `6 8` = code 68, `3` = code 33, X = λ (b).
- **A figure for Vostre Majesté** (`VMf`, verso ll. 11 and 38: a barred o crossed by a looped stroke): value from
  the two contexts only, written *[?Vostre Majesté]*.
- **Omissions in Brackx's file:** the whole last line of f. 123r (l. 37, 30 figures: *[?deffaillent] d'i pourveoir,
  et lors que ceste*, which joins the verso's *armée devoist estre …*), and figures at line starts and ends on the
  verso (ll. 10, 12, 17, 18, 26, 27, 33, 38, 41).

Leaf key `key_cipher1_f123.json` (the shared key is unchanged): Uv, Cv, ssl, szl, oob, ub, dc = m, ff = n/o,
VMf, qt (q with a barred foot, t: two contexts on l. 35-36, both left [?]), cr (plain cross, c/e), 8 = g/e,
fe = r/rr, brace = p/i/pp, q4 (crossed 4, unidentified), del, virg.

## What failed

- The beam decode and a word-level beam over the Henri IV letters (word bigrams) did not give the sentences (*la
  neces iti que ie preu o in uos*); both were used for word candidates only.
- f. 123r l. 7-8, the twelve figures after *tousiours remis*: with oo2 as d (*au … d'aire … attendre*) and as the
  barred-double-o ff (*… affaire*) neither forms; left […]. Same for *que l'on a* + four figures (*a u o s t*:
  *aoust* has the letters in another order) and the six figures after *l'avois* (*a reuni*, *a ieune*: not French
  in context).
- l. 12: *pacience* needs c where a large 3-shaped figure stands; *vivre* follows a figure (ε) that is not read.
- *tresorier*, *mareschal* (*mar c a l*), *forces*, *lesquels*, *proteste* (*protesue*): one figure short or wrong
  each; the image shows the figures as transcribed, so they stay [?].
- On the verso: *a ma charge* and *aussi* for the V.M. figure (l. 11): neither fits; U as e on l. 14 (two figures,
  not a V).
- Code 16 fits *quand* in all three places (ll. 2, 8, 36) but no clear copy confirms it; not adopted.

## After

| file | sentences clean | share | hole rate |
|---|---|---|---|
| `texts/reading_f123.md`, whole file (header and notes included) | 83 / 153 | 0.542 | 0.153 |
| the cipher sections only (both pages) | 31 / 59 | 0.525 | 0.129 |
| f. 123r cipher only | 10 / 27 | 0.37 | 0.156 |
| f. 123v cipher only | 21 / 32 | 0.656 | 0.105 |
| `texts/reading_f123_en.md` | 56 / 76 | 0.737 | 0.079 |

Below the 0.70 bar on the recto. About a third of the failing sentences fail on period spellings the word list does
not know (*laquele*, *demourés*, *douse*, *harasée*, *desnu*, *estreme*, *deuoist*, *meritoist*, *ocupés*,
*enemis*), kept as the figures give them; the rest carry two [?] words each.

## What stays open, and why

No break on these two pages is an image defect, except the verso gutter, which half-hides the last figure of ll. 10
and 18. Everything below is figures that do not make the word, so the escalation is not exhausted: a second reader on
the shapes of B, the 3/ȝ/y family and the C-shapes, and the ff. 124r-v reading (the same despatch) for the code
values 16, 101, 102 and the unread runs.

- f. 123r: l. 1 [UNK] (the first figure, a cross with an o at each end), *[?nécessité]*, *[?prévois]* (a long cross
  with a curled foot before the s); l. 3 *[?reiondroient]*; l. 4 six figures after *l'avois*; ll. 6-8 the two runs
  above; l. 12 *[?pacience] […]*; l. 13 *[?proteste]*; l. 14 *[?tresorier]*; l. 15 *[?mareschal]*; l. 18
  *[?forces]*, *[?lesquels]*; ll. 21-37 *[?sortir]*, *l'[…]*, *[?harasée]*, *[…] mal vestue*, *m'[?ont] [?tous]*,
  *[?monstres]*, *[?protestent]*, *qu'il n'i […] point*, *[?gendarmes]*, *[?veulent]*, *[?importuns]*, *[?est]*,
  *[?peult]*, *n'[?en]*, *qu'[…] comptant*, *[?incommodités] [?m'arrivent] [?ensemble]*, *[?deffaillent]*; codes 16,
  101, 102.
- f. 123v: *[?messieurs]*, *[?moindres]*, *non [?plus]*, *[?deperir]*, *[?entretenement]*, two words after *et que*
  (ll. 13-14), *[?quelques]*, *[?rapporter]*, *comme [?je] croi*, *[?recouvrement]*, *[?difficile]*, *[?promises]*,
  *[?ne]*, *[?du]*, *[?dire]*, *Vostre [?costé]*, *[?humblement]*, and a large curled figure in *et si […] desire*
  (l. 41), perhaps a code for the King; the V.M. figure (`VMf`) from context.
- The clear opening was read from the image for context; its last words before the cipher are not read.

## Pass 2 (22 Oct 2026): f. 123r ll. 1-37 re-checked figure by figure

`_check_reading.py --file` on the f. 123r cipher section alone (cut to a scratch file), before: 27 sentences, 10 clean,
**clean share 0.37**, hole rate 0.156.

**Image and exemplar set.** The right page of canvas 129 (full size, region 4750,1000,8250,6100) was deskewed by
2.25°, the 42 text lines found by projection (five clear, 37 cipher), each line's centre tracked in eight windows and
the band straightened, then cut into figures by connected ink with every figure numbered (two halves per line at full
resolution, doubtful stretches at 2-2.5×). Crops in the session scratchpad, not in the repo. The exemplar set was cut
as contact sheets per confusable class, from figures whose value a read word fixes on this page and on f. 123v: the
C-shapes (Cl in *clameurs*, *qu'il*; Cv in *prévois*, *armées*, *tousiours*), the double crosses (Hc in
*nécessité*, *clameurs*, *pacience*, *aucun*, *recevront*, *encores*, *ici*, *dict*) against the slanted ff (*vos*,
*maintenant*, *non*, *monstres*), the q-family (crossed q in *tous*, *mois*, *pour*, *moien*, *d'i pourveoir*
against the looped 4 of *harasée*), the a-figure (ao) against the t-cross, and the t-cross against the closed 4 (pl).
The barred double o was taken from f. 123v (*affaires*, *deffaillent*) and l. 37 here. Lines 1-8, 12-15, 21-28, 30-33
and 36-37 were compared figure by figure; the other lines read word for word with every figure carried and were
only checked for figure counts.

**Label changes** (`brackx2026/corrections/f123r_v2.tsv`, 12 rows; corrected file
`brackx2026/corrections/f123r_v2_cipher.txt`, 1,138 figures against 1,140 in pass 1, two pairs merged into code
groups):

| line, token | pass 1 | pass 2 | what the image shows | what it gives |
|---|---|---|---|---|
| 1, 20 | Hc | Hl | a double upright with a looped foot, not the plain double cross | the s of *[?prévois]* follows an unknown sign (value not known) |
| 3, 2 | Hc | ff | the slanted ff, not the straight double cross | o of *reiondroient* |
| 4, 24 | virg | S | a long s with a curved head running below the line, as the S of *plus* | *a p r e u n e* after *l'avois* (no word yet) |
| 7, 21; 8, 1 | oo2 | oob | two o joined by a long bar, the ff of *affaires*, *deffaillent* | the run after *remis* still does not form |
| 21, 25-26 | 6 B | 66 | two 6 written together, one group | *Toute l'[66] a esté*, every other figure read |
| 22, 29; 23, 2 | Cl | Cv | the heavy curled C, not the open C with an r inside | *[…] si mal vestue* |
| 25, 0 | Hc | ff | the slanted ff | *s'en pouoir servir* (pouvoir) |
| 28, 0 | t | ao | an open a-bowl, not the t-cross | *gend a mes* (still one r short) |
| 33, 23-24 | s y | 59 | the s-shaped 5 and a 9, one group: code 59 = *argent* | *qu'à l'argent comptant* |
| 36, 16 | pl | t | the t-cross with a curled foot, not the closed 4 | *ensemble* |

**Leaf key** (`key_cipher1_f123.json`): two labels added, both with no value (`+`): `Hl` and the code `66`. Neither
occurs on f. 123v, so the verso reading is unchanged (its section still scores 0.656). No letter value was changed:
the page confirms Hc = c wherever the plain double cross stands (eight words), but Hc keeps c/n/o in the leaf key
because f. 123v was not re-checked for it in this pass.

**Readings gained, all carried by their figures:** *qu'à l'argent comptant* (l. 33, was *qu'[…] comptant*);
*ensemble* (l. 36, was *[?ensemble]*); *Toute l'[66] a esté* (l. 21, was *l'[…]*); *[…] si mal vestue* (l. 23);
*[?pacience], i vivre* (l. 12: the figure after *pacience* is the ε-figure, i; the double cross before it is c, so
the word is *paciece*, the n missing); *qu'il n'[…] [?recevront] point* (l. 26: *r e c e r o n t*, one u/v figure
short); *pouoir* (l. 24-25) now carried by its figures.

**Tried and failed.** The run after *remis* (ll. 7-8) re-read with oob = ff and the hooked figure (Brackx qs) as s,
as in *mains* l. 14: *a s a t ff a i r e e s a t ff r e a*; the word search over the Henri IV word list finds no
French through it (*affaire* needs an a where E, t, stands). *que l'on a* + *a u o s t* (l. 6-7) still has the
letters of *aoust* in another order. l. 4 after *l'avois*: with S for the virgule, *a p r e u n e*, no word.
*[?tresorier]* (l. 14): the figure before *er* is the r-like open C (l), as in *qu'à l'argent* (l. 33), not a figure
for i; no relabel. *m'[?ont] [?tous]* (l. 23-24): the four figures (E, m, crossed q, dd) checked, n and u are not
written. l. 25 *deu[l] [s] monstr[s] et*: the C after *deu-* is the open C (l), not Cv; one figure too many and one e
short. The first figure of l. 23 is the library stamp, not a figure.

**The clear opening** ends *j'ay tousjours [?dépeint]* (d, a dot for e, a p with a stroke, a dot, two minims and a
hooked final stroke; *depuis* on the same line is written without the dot after the p), then a filler stroke and four
signs not in Brackx's file: a *tt* joined to a C, a triple bar and a crossed loop. They stand where the sense wants *à
Vostre Majesté* before l. 1 *[UNK] la nécessité*, but no value is read from them; not added to the cipher file. The
clear opening has five lines, not six.

`_check_reading.py --file` on the f. 123r cipher section after pass 2: 27 sentences, 11 clean, **clean share 0.407**,
hole rate 0.152 (pass 1: 0.37, 0.156). Of the 16 failing sentences, **4 fail only on period spellings** the word list
lacks (*commançant*, *douse* and *ès*, *desnu*, *estreme*; the marked holes in them are within the one-in-ten
allowance); counted as words they would give 15 / 27 = 0.556. English f. 123r section: 29 sentences, 15 clean, 0.517,
hole rate 0.116. Whole file `reading_f123.md`: 191 sentences, 103 clean, 0.539, hole rate 0.159. The recto is still
below the 0.70 bar.

## What stays open on f. 123r after pass 2

The breaks below were checked on the image; the figures are legible (except the stamp at the start of l. 23, which
covers no figure). They are writer's omissions (one letter short: *retrouerions*, *reiondroiet*, *troue*, *optnir*,
*paciece*, *protesse*, *forcs*, *lesquls*, *gendames*, *velent*, *impotus*, *quiet*, *pelt*, *dffailent*) or runs
that do not form:
- l. 1 [UNK] and the `Hl` sign in *[?prévois]*; the four signs after the clear text.
- l. 4 *l'avois [a p r e u n e]*; l. 6-8 *que l'on a [a u o s t] tousiours remis [a s a t ff a i r e e s a t ff r e a]
  [16] nous serions tous ensemble*.
- l. 22-23 *maladie, [s e t s t] si mal vestue*; l. 26 *n'[i/n/s n/o]*.
- Codes 16 (three times, fits *quand*), 66, 101, 102 open: no clear copy or sibling gives them; ff. 124r-v (the same
  despatch) are the next place to look.
