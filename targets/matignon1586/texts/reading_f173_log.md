# f. 173: reading log (22 Oct 2026)

Brief: `READING_BRIEF.md`. Image: Gallica canvas 180 right (fr. 15572, ark `btv1b9061879d`), fetched full size
(8553 × 6358) from openapi.bnf.fr IIIF (gallica.bnf.fr/iiif answers 403); line and word crops kept in the
session scratchpad, not in the repo. Decoder: this project's beam and period-French 6-gram (`measure.beam_aligned`,
via `brackx_validate.prep_key`), run on the whole leaf as one stream.

## Pass 0: the published decode

`texts/f173.txt` (Brackx's figures, `key_cipher1.json`). `_check_reading.py --file texts/f173.txt`: 19 sentences,
3 clean, **clean share 0.158**, hole rate 0.229. Not a reading.

## Pass 1: what the opening says

The leaf opens in clear: *Sire, Vostre Majesté a esté suffisamment advertie par les deux dernières depesches de
Monsieur du Mayne*, and the cipher starts on the same line. That gives the frame (*advertie … de l'extrême
nécessité*) and the addressee (the King: code 68 = *Vostre Majesté* appears twice).

## Pass 2: reading against the letter sets

The decode was read sentence by sentence against each figure's letter set rather than against the beam's choice.
Most of the text forms once the set is used in context, with no change to the figures: *se voyant frustré de la
venue de troisiesme mois, qu'il y a plus de six sepmaines qu'il estimoit estre par les chemins* (8 = e, not g, as
Brackx's #69 said); *aucun moyen de faire payer les gens de guerre*; *à quoy il n'a trouvé autre remède que de me
renvoyer pour la seconde fois*; *de l'argent soubs ses obligations, à quelque interest que ce peust estre*; *en leur
excuse des lettres qu'ils dient avoir de Vostre Majesté*; *qu'ils ne seront tenus à aucune contribution*; *il ne
s'est peu trouver un seul escu soubs les obligations de Monsieur du Mayne*; *qui avoient de l'argent à recouvrer
audict Paris*; *de le me bailler*. One reading the beam missed and the sets give: l. 12 *que pour essayer* (x B ao
ei t e = e-ss-a-i-e-r, B = ss).

## Pass 3: the breaks, checked on the image

Each break was cropped (full resolution, 2–3× enlarged) and the figures compared with Brackx's labels. Fourteen
label changes (`brackx2026/corrections/f173.tsv`; corrected file `brackx2026/corrections/f173_cipher.txt`):

| line | what the image shows | what it fixes |
|---|---|---|
| 1 | δ, δδ, B where the file has 0, ∞, ao | *nécessité en la* (was *…oteoo…*) |
| 6 | an e between Ze and t, left out of the file | *monstres* |
| 7 | small s (= u), not tall S | *avec* |
| 12, 17 | two o joined by a bar: one figure | *affaire*, *[?fortiffier]*: the barred double o = ff (new label `oob`) |
| 19 | crossed A (= l), not z | *elle leur promet* |
| 23 | long-tailed y (= g), not 3 | *du général* |
| 24 | plain cross (pl), crossed q (= o) | *moins refroidis* |
| 33 | two plain crosses (pl) and c (= p) | *sur ma simple* |

Key additions for this leaf only, in `key_cipher1_f173.json` (the shared key is unchanged): `oob` = ff/f (above);
`fe` = r/rr (*irreverences* l. 8 needs rr; the same figure ends *guer…* at l. 5); `zu` = u/uu (*recou(u)rer* l. 12
and l. 31, the period spelling *recouurer*).

`_check_reading.py` on the reading after pass 3: 45 sentences, 33 clean, **clean share 0.733**, hole rate 0.106
(whole file, English header included); the cipher text alone 28 sentences, 20 clean, **0.714**, hole rate 0.093.

## What failed or stays open

- Re-decoding the corrected figures with the beam still did not produce the sentences (l. 2 *retuoue*, l. 8
  *siniioustum*, l. 33 *iouriamais*): the 6-gram picks short words over the right ones where sets are wide. The
  reading was made by hand from the sets; the beam is a first draft only.
- **On the image (outer edge damaged or cut):** l. 1 *en la[…]le* (the *que* of *laquelle* is not on the line;
  the line ends at a damaged edge); l. 5 *guerr[e]* (last letter at the edge); l. 11 *seco[u]rir* (a stroke at the
  edge); l. 25 *l[e]s* (edge). These are the image's holes, not the key's.
- **Figures that do not make the word:** l. 1 the two figures before the stop 44 (*c v*; on the image the first is
  T-shaped); l. 2 *[?retrouve]* (r e t ? o u e, the figure after t is an f-shaped sign Brackx labels zu);
  l. 3 *de troisiesme* (B = e; *du* would need u); l. 6–7 *de l[e]ur* (n s e = l u r); l. 8 the underlined q
  before *rigueurs* (underlined q = s elsewhere: *des* l. 6, *trouvés* l. 24) and *[?inaccoustumées]*
  (i n a + o u s t u + ss δ: the end does not give *-ées*); l. 9–10 the two figures after *renvoyer* (ε B);
  l. 11 *[?corps]* (the first figure is the barred δ = u/s/m, not c) and the two figures before *vouloir* (ε h);
  l. 15 *servis […]* (q + x) and *[?l']autre* (z = u/s/m); l. 16 *qui [?n'ont]* (dd v 7 6 m) and *[?opposer]*
  (7 L q z x e: one figure short); l. 16–17 *[?nécessité]* (6 for e); l. 21 *[?armée]* (a r m + ss);
  *[?sur]* (S e); l. 22–23 the word before *l'exemple* (w ao he o L dd yy: not *d'ailleurs*);
  l. 23–24 *[?particuliers]* (ao for e); l. 30 *[?marchans]* (no n: marcha + underlined q); l. 31–32
  *[?prendre]* (pre / dre, no n; perhaps a line-end abbreviation).
- The sentence runs on past l. 33 (*sur ma simple …*); the continuation was not looked for (f. 173v or the next
  leaf).
- No second reader has checked Brackx's labels outside the lines cropped here.
