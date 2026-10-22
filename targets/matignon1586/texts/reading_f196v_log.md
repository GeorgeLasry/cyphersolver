# f. 196v: reading log (22 Oct 2026)

Brief: `READING_BRIEF.md`; the recto and f. 201: `reading_f196_201.md`, `reading_f196_201_log.md`. Scratch scripts
(line cutting, crops, decode wrapper) were kept in the session scratchpad, not in the repository; what they
established is recorded here.

## Image

fr. 15572, ark `btv1b9061879d`, canvas 204 left (8,563 × 6,365). gallica.bnf.fr/iiif answers 403; openapi.bnf.fr
IIIF serves the page at full size. The cipher block (region 1200,1130,3100,4450) was fetched at full resolution,
deskewed by 0.68°, and cut into 36 line bands by an ink projection (line pitch about 120 px); each line was viewed
in two overlapping halves at 1:1, and doubtful figures re-cropped at 1.2–2× side by side. The page has **36 cipher
lines**, not the ~45 estimated from the recto, then the clear close and dateline. The first crop cut the right end of
several lines (ll. 4, 6, 7, 8, 9: a figure or two); a wider crop recovered them. Crops in the scratchpad
(`matignon_img/f196v/`), not in the repo.

## Pass 1: transcription in Brackx's label set (worked)

Same scribe as f. 196r. The label shapes were calibrated first on f. 196r ll. 1–4 (canvas 203 right) against
`corrections/f196_201_cipher.txt`: ϖ = w, the yogh-like figure = h, ε = ei, ∂ = dd, Ƶe = Ze, 4-shape = pl, ơ = o,
·v· = v, £ = L, the 9-with-tail = y/q, and so on. Then all 36 lines were labelled figure by figure:
`brackx2026/corrections/f196v_cipher.txt`, **1,236 figures** (4 struck through by the writer, 4 the exit marker).

The first mechanical decode (this project's beam and 6-gram, `measure.beam_aligned`, `key_cipher1_f196_201.json`,
line by line) already ran as French over most of the page: *tranch…s en plusieurs endroicts et est | ans mal garnis
de …oniers la besongne en a | esté plus longue ie croi que + de[main] l'on com|mencera a battre en batterie de quinze
canons do|nt il i a apparence qu'ils s'esto…ront* …, so the label set and the key fit this page.

## Pass 2: the crib, and the breaks checked on the image (worked)

**Crib.** f. 201's clear tail (*… tranchées en plusieurs endroicts; et estans mal garnis de pionniers, la besongne
en a esté … Je croy qu'après demain l'on commencera la batterye de quinze canons, dont il y a apparence qu'ils
s'estonneront, n'ayans pas accoustumé à bien assiéger les places et faire avec cest équipaige. Toutesfoys jusques icy
ils sont toutte à Monsieur …*) runs with ll. 1–8 of the verso. The cipher is not word for word the clear: it has
*commencera à battre en batterie*, *de veoir assiéger les places en ce pais*, *ils font toute demonstrance*. Where
they agree the crib fixed **code 63 = après** (*que 63 demain*, l. 3; the figures are plainly "63" on the crop).

**Figures re-cropped and what they showed** (each against the word the sentence needs):

| line | figure | what the crop shows | value |
|---|---|---|---|
| 4, 11, 29, 31 | small double cross with a curl below | not Brackx's large plain # (Hc, which is c in *avec cest*, l. 7) | **tt** (new label `tt` = t/tt): *abattre*, *batterie*, *mettre*, *attendons*, *l'attente* |
| 27 (×2), 29 | Ƶe with an f-ascender and a bar | one shape, three places | **r/rr** (new label `fZ`): *arrivées*, *pourvoira*, *irreparables* |
| 14 | x with a loop (Brackx #77's ꝭ) | | **x** (`xl`): *Xaintonge* |
| 4, 11 | γ-like y with a looped tail | distinct from the g-like y of *garnis*, *charge* | **z** (`yz`): *quinze*, *Bazeille* |
| 1, 3, 10, 30 … | short hooked long-s without descender | Tomokiyo's long s = c | `dl` (c): *tranches*, *endroicts*, *croi*, *celui*, *depesche* |
| 9 | two o-figures with a rising flourish | the σ of f. 110 | `sg` sg = **ff**: *deffendre* |
| 9 | n with a long lead-in stroke | the same figure as *faict* (ll. 11, 35), *faire* (ll. 13, 33) | **M** (f), not n: *que le roi de Navarre a faict recevoir* |
| 13, 20 | in *doi?t*, read as X at first | a λ | **lam** (b): *doibt* |
| 13 | c with a bar | `ca` of corrections/f196_201.tsv | **a**: *advis* |
| 14 | "99" | two 9-figures written as a numeral pair, underlined like the codes | **code 99**, not *yy* |
| 17 | four figures (*o 4 o q*) | a line struck through them by the writer | deleted: a dittography of *amis* from l. 16; *au devant de ses reistres* |
| 21 | f-like figure with two cross-bars | not Hc | **th** (m/s): *l'absence* |
| 22 | in *encores* | a 6, not o | n |
| 24 | "65" at the line end | the 5 written like a long s, as in code 35 on f. 196r | **code 65** |
| 33 | last figure | ϖ, not σ | **w** (d): *entendre* |
| 35 | in *faicte* | 6, not B | i |

After these, the decode (scratchpad, `v2`) reads the whole page as French except at the open points below.

## Pass 3: reading against the letter sets

Read sentence by sentence (`reading_f196v.md`), every word checked against its figures; English in
`reading_f196v_en.md`. Codes resolved by the key: 12 il, 13 qui, 14 que, 15 quoy, 17 car, 25 nous, 26 vous, 33
vostre, 35 parce que, 36 toutesfois, 40 bien, 43 point, 47 tous, 48 aussi, 49 comme, 51 pas, 54 aussi, 59 argent, 62
peu(t), 68 Vostre Majesté, 76 roi de Navarre, 84 le viconte de Turenne. The content: the siege of Monségur (trenches,
too few pioneers, a fifteen-gun battery the day after tomorrow; the defenders mean to hold out so as not to suffer
the shame Navarre inflicted on the commander of Sainte-Bazeille, whom he imprisoned); Navarre to leave [99] for
Saintonge to gather friends and meet his reiters, Turenne at Nérac to keep the province; the army's want of money and
[65]; the third month's pay awaited; a proposal to come by [?Seval] on what to do after the siege; clear close
*Du camp devant Monségur ce … jour de May 1586*.

## What stays open

- **On the figures, not the image** (legible, value not found): l. 1 *tranch[?e]s* (the figure is R, p); l. 12–13 *et
  si il se parle qu'il luy veult faire pas […]* (the sentence has no object; *pas* may begin *passer*, not adopted);
  l. 16 *recueilir [B o] de ses amis* (two figures, no word); l. 23 *[?p]articulierement* (the figure is the f-figure
  M); *de [?Senegal]* (q x B t y o n: a name, not identified); l. 25 *tous* written 47 + ∂; *que les ne se sent*
  (the cipher has *les* where *elles* is wanted); l. 28 *ce [?n'a] peu[t]* (a crossed ß-figure, then 62 + t);
  l. 31 *troisies[?m]e* (an o-figure where m is needed); l. 35 *faict[?e]* (e-figure = r/i); *[?Seval]*
  (ps t y o n; perhaps Bosseval of the recto's clear opening); l. 36 *si[?e]ge* (four figures for *siège*).
- **Codes** 65 (a supply beside money) and 99 (the place Navarre leaves from) not identified; 63 = *après* from the
  crib, its second use (l. 29, *qui sont [?après] irreparables*) fits less well.
- **The dateline day** in clear is not read (*ce [Dmit?] jour*); the signature is not on the page.
- New labels (`tt`, `fZ`, `xl`, `yz`) and codes 63/65/99 were used in a scratchpad copy of the key only; the shared
  `key_cipher1_f196_201.json` was not changed (this pass was told to edit only its own files).
- No second reader has checked the labels.

## Check results

`python docs/_check_reading.py --file targets/matignon1586/texts/reading_f196v.md`:

| pass | file | sentences | clean | share | hole rate |
|---|---|---|---|---|---|
| beam decode (scratch, unspaced) | — | 36 | 36 | 1.0 | 0.014 |
| first draft (markers inside words) | `reading_f196v.md` | 52 | 32 | 0.615 | 0.143 |
| final, whole file | `reading_f196v.md` | 53 | 35 | **0.660** | 0.123 |
| final, reading only (from "## The siege") | same | 34 | 24 | **0.706** | — |

The unspaced beam decode scores 1.0 only because the checker cuts an unspaced run into whatever words fit (it took
it for Italian); it is not a reading. The whole-file figure includes the English header, which the checker scores as
French. The first draft's line markers split words across line breaks (*e[l. 3]sté*); moving each marker before the
word in which the line begins removed those false holes. The remaining failed sentences each carry one or two marked
holes from the list above (a `[?x]` inside a word counts twice).
