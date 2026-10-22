# f. 110: reading log (22 Oct 2026)

Brief: `READING_BRIEF.md`. Image: Gallica canvas 116 right (fr. 15572, ark `btv1b9061879d`), the slip cut at full
size (region 4800,300,3400,3100 of 8759 × 6369) from openapi.bnf.fr IIIF (gallica.bnf.fr/iiif answers 403), deskewed
by 1.0°, 38 line bands at 1.8× (line centres found by projection); crops kept in the session scratchpad, not in the
repo. Transcription: Michael Brackx, `brackx2026/f110_cipher.txt` (38 lines, 2,164 tokens).

## Pass 0: the published decode

`texts/f110.txt` (Brackx's figures, `key_cipher1.json`, beam + 6-gram). `_check_reading.py --file texts/f110.txt`:
40 sentences, 9 clean, **clean share 0.225**, hole rate 0.217. Sense runs 62% of tokens, but the beam's words
string together without sentences.

## Pass 1: a word-level second draft

A Viterbi decoder over the letter sets that may only emit dictionary words (word list and word bigrams from Henri IV's
letters, `lang/corpora/fr-henri4.txt`, plus `corpus_words_v1.txt`; one-token skip at a high cost). It finds the
longer words the 6-gram breaks up: *il fault parler clairement* (l. 11), *par la ruine de ma reputation et que de
m'exposer* (l. 13), *d'avoir la paix pour l'avoir* (l. 23), *il seroit necessaire de faire de plus grans* (l. 25),
*cest affront* (l. 34). It still fills wide sets with short words; it is a draft, not the reading. (Scratchpad script,
not kept in the repo.)

## Pass 2: reading against the letter sets

The leaf was read sentence by sentence against each figure's set. What forms with no change to the figures:
*qu'elle estoit un peu de [considération], et que l'on ne s'attendoit pas* (l. 6); *en ce traict qui est dans vostre
dernière [depesche]* (l. 7–8); *qui arrivent à ceux qui entreprennent* (B B = n e) *[la] guerre sans [argent]*
(l. 9); *Si le roi est ennuié de la [guerre]* (l. 12); *qu'il n'i a poinct de … faulte, qu'au contraire qu'il ne se
pouvoit [mieux] faire que de la [conserver], comme i'ai faict* (pi = mm in *comme*) *avecques peu de despence, pour
s'en servir à la [saison] et aux occasions* (l. 17–19); *Quand à la guerre, elle se peult faire, et utillemant*
(l. 20); *se veult tenir promesse d'envoier les deniers qui ont esté destinez* (l. 21); *n'est poinct contraire*
(l. 22); *sa Maiesté* (l. 23, 32–33, U = s); *[à vostre] discretion de faire sçavoir au roi* (l. 28); *il est
inévitable qu'elle périra toute entière avant qu'il soit … sepmaines, ce que ie vouldrois éviter pour le moins*
(l. 30–32); *cest affront, car il … peult asseurer* (l. 34); *de personne que de moi* (l. 35); *ceste resolution*
(l. 36); and the close *vous donne, Monsieur de Villeroy, tout le contantement que vous désirés* (l. 37–38; Villeroy
= box 3 n n B e 7 3).

## Pass 3: the breaks, checked on the image

Lines 1, 2, 3, 7, 11, 14, 22, 24 and 30 were cropped and compared figure by figure with Brackx's labels. Ten label
changes and one omission (`brackx2026/corrections/f110.tsv`; corrected file `brackx2026/corrections/f110_cipher.txt`):

| line | what the image shows | what it fixes |
|---|---|---|
| 1 | a 4-like cross, not q1; a crossed A (= l), not th; the ξ-shaped E2, not y | *[Monsieur]*, *par la lettre*, *que ie* |
| 1 | about seven faint figures at the damaged top-right corner, after *qu*, missing from the file | marked `?`, not labelled |
| 3, 7, 11, 24, 30 | a p-shaped figure with a looped hook, which Brackx writes as S (four times) or pl (twice) | it is **b**: *librement*, *beaucoup*, *bons effects*, *substance*, *[honnorable]*, *inévitable* |
| 30 | a ξ figure written U | it is B (= i): *inévitable* |

Leaf key, `key_cipher1_f110.json` (the shared key is unchanged): new label `Sb` = b (the hooked figure above);
M = f/h (h needed by *[empeschement]* l. 22 and *[honnorable]* l. 24, f by *affront* l. 34; not checked on the image,
so both words stay marked).

`_check_reading.py --file texts/reading_f110.md` after pass 3: 72 sentences, 28 clean, **clean share 0.389**, hole
rate 0.189 (whole file, English header included). The bar (most sentences clean) is **not** reached.

## What failed or stays open

- **Re-decoding** the corrected figures with the beam gains little (`beaucoup de bons effects`, `librement`,
  `substance`, `ineuitable` appear; the rest is unchanged). The reading was made by hand from the sets.
- **The labels of this hand are not consistent**, which is what `f110_status.md` found in September with another
  transcription. Seen here on the image: Brackx's S covers two figures (the long s = p/s and the hooked b); his B
  covers both the 8-shaped figure and a ξ that he also writes y, E2 and U; his Cl stands where *guerre* (l. 12) and
  *faire* (l. 13) need r. Each of these gives a hole wherever the set does not hold the needed letter, and the
  fix is a figure-by-figure re-transcription of the whole leaf against a labelled atlas of this hand, not a few
  corrections. Only nine lines were checked on the image in this pass.
- **On the image:** the end of l. 1 is at the damaged corner (seven faint figures unread); l. 2 has a struck-through
  word after *S box L*, left out by Brackx and rightly so.
- **Not formed, figures checked or not:** l. 1 *vous [verrez] …* (s x e T B Ca S B t 6: *verre* then *a?es*);
  l. 2 almost whole; l. 3–4 *avec quo[u] d'avec ce qu'avait*, *de grande con…*; l. 5 the words before *auoir de ceste
  armée*; l. 7 before *particulièrement*; l. 8 the words after *que le roi*; l. 10 *comme il a faict … [45]ssement*
  (perhaps *esclaircissement*, with 45 for a syllable; not adopted) and *il n'a eu …*; l. 11 before *paroist*;
  l. 14 *S n t h m* after *suivie* (the S is the hooked b on the image: *bleut*, no word); l. 14–15 *que les … soustenir*;
  l. 16 *leur … peult faillir*, *ie suis d…*; l. 23 between *sa Maiesté* and *d'avoir la paix*; l. 24 after
  *advantage*; l. 26 *de plus grans …*; l. 27 *pour [4] donne…*; l. 29 almost whole; l. 33 *ie [ne meritois]*
  (6 h h pl t e 3 m th: one figure extra, no o); l. 36 before *prie à Dieu* and between *ruinée* and *iamais*.
- Codes 45 (twice), 4 (l. 27) and the 47 contexts that do not settle *tous/tout* stay open.
- No second reader has checked Brackx's labels outside the nine lines cropped here.

## Pass 2 (22 Oct 2026): the whole leaf re-transcribed against an exemplar set

**Image.** The same full-size cut of canvas 116 right (openapi.bnf.fr IIIF, region 4800,300,3400,3100, deskewed 1.0°).
Each of the 38 lines was straightened (its centre tracked in eight windows, the band resampled along it), cut into
figures by an ink projection, and shown at 2.4× in four parts with every figure numbered; doubtful figures were
re-cut at 4×. Crops in the session scratchpad (`matignon_img/f110/v2/`), not in the repo.

**Exemplar set.** Built first from the lines pass 1 had checked (1, 2, 3, 7, 11, 12, 14, 22, 24, 30), then grown
label by label as lines were done: one contact sheet per label (every figure given that label, side by side), so a
figure that does not look like its class shows at once. What it settled:

- **B** is two shapes, the 8-like figure and the Ω loop, both i/e/n; the **ξ** figure that Brackx writes U (and
  once x, h) is the same class as B (i/e): *Maiesté y perdra* l. 33, *que toutesfois* l. 33, *que ie prie* l. 36,
  *ie vous donne* l. 37 all need it. Seven U → B.
- **th** in Brackx's file covers two figures: the crossed 8 (th, m/s) and an h with a long foot; fifteen of his th
  are plainly the h of the h exemplars (e/u), in ll. 8, 23 (five: *sa Maiesté iuge meilleur de ne le faire*),
  24, 25, 28, 29, 30, 35, 36 (*qu'il me ruine*).
- **σ** (o with a rising flourish), written o by Brackx, is **f**: it gives *effects* twice (l. 17 *de meilleurs
  effects*, l. 26 *de plus grands effects*) and *s'offrent* (l. 20). Labelled `sg` (already f in the key).
- the long s / hooked b split of pass 1 holds on the whole leaf (two more b: l. 1 *bien*, l. 8);
- **y** (g-like) and **3** (z-like with a tail) are different figures; four of Brackx's y are 3 (l. 1, 4, 5);
- the u with a dot is **w** (d/q), not U: *et qu'il vous donne* (l. 37), *que ie prie* (l. 36);
- the square with ticks is **box**, not H: l. 34 *iamais plus* (S n box U), confirmed by *fidelle* at the start of
  l. 35;
- a cursive H-shaped figure (l. 25, twice) has the value n (*recongnoistre*, *que l'on n[…]*), written as ff.

**Counts.** 2,121 figures (Brackx 2,164, pass 1 2,171 with the seven unread figures of l. 1). 123 changes against
Brackx in `brackx2026/corrections/f110_v2.tsv`, of which 50 are labels of his that have no figure on the crop:
each was checked on a contact sheet of the stretch between its neighbours (doubled letters mostly: *S S*, *n n*,
*e e*, *U U*, *s s*), and one (l. 7, *x h h*) is a ξ and one h. Six faint figures remain unlabelled at the damaged end
of l. 1 (pass 1 counted about seven).

**Key.** No change to `key_cipher1_f110.json` was written (this pass was told to edit only the transcription and the
reading). The re-decode used it with one addition, kept in the scratchpad: **Cl = l/r** (pass 1 saw *guerre* and
*faire* needing r; with r allowed the decode gives *la guerre* l. 12, *faire* l. 13, *a pris* l. 8, and Cl stays l in
*meilleur*, *clairement*, *fidelle*). The leaf key should take it.

**Decode and reading.** Re-decoded with the beam and 6-gram (`measure.beam_aligned`) and read again sentence by
sentence against the sets. New against pass 1, all carried by their figures: *Pour le peu de […] que i'ai veu avoir de
ceste armée* (l. 5); *et que l'on ne s'attendoit pas beaucoup de bons effects* (l. 6-7); *dans vostre dernière
depesche, que le roi a pris […]* (l. 8); *il fault parler clairement* (l. 11, every letter); *ceste armée n'a faict
de meilleurs effects, qu'il n'i a poinct de sa faulte* (l. 16-17); *avecque peu de despence* (l. 19, every letter);
*qui [?s'offrent] maintenant. Quand à la guerre* (l. 20); *à quoi l'empeschement de ceux du clergé n'est poinct
contraire. Mais si sa Maiesté iuge meilleur de ne le faire poinct, et d'avoir la paix, pour l'avoir plus honnorable
et advantageuse* (l. 22-24); *qu'il seroit nécessaire de faire de plus grands effects. Ie recours à vous* (l. 25-26);
*pour me donner en cela vostre advis, ainsi que ie sçai que vous le pouvés, remectant mesmes à vostre discretion de
faire sçavoir au roi* (l. 27-29); *il est inévitable qu'elle périra toute entière avant qu'il soit [?six] sepmaines*
(l. 30-31); *sa Maiesté en perdra plus que moi* (l. 33); *car il se peult asseurer qu'il ne sera iamais plus
fidelle* (l. 34-35); *que ie suis tant confirmé en ceste resolution que ie prie à Dieu qu'il me ruine plustost que
[…] iamais. Et qu'il vous donne, Monsieur de Villeroy* (l. 35-37).

**The dateline** in clear after the last group reads on the crop *De Villeneufve d'Agenoys ce … jour de Mars 1586*,
not "De Bellebourg" (NOTES, profile and page say Bellebourg; not changed here).

`_check_reading.py --file texts/reading_f110.md` after pass 2: 76 sentences, 43 clean, **clean share 0.566**, hole
rate 0.16 (pass 1: 0.389, 0.189; pass 0: 0.225). The bar (0.70) is **not** reached.

## What stays open after pass 2

- l. 1-2: the salutation and the first sentence (*vous [?verrez] … bien par la lettre que ie fais au roi*), then
  *du r…* and line 2 almost whole (*se retenu de l… le plus … que ie suretse…*); figures checked, they do not form.
  Six faint figures at the damaged corner of l. 1 (on the image).
- l. 3-4: *de parl[l]r* (n A T gives *llr*: one figure short of *parler*), *avec quoud*, *[?confidence]* (7 where n
  is needed), *amitié […] recongnu*.
- l. 10: *comme il a faict […] [45]sement, que [47] […] paroles* (45 as a syllable of *esclaircissement* fits
  nothing else; not adopted).
- l. 12, 14-16: *qu'il la [?veuille] [l 3 6 o e]*, *la guerre [?n'est] [?suivie]* (B B m: one figure short), *que les
  [s e c e s e u e t] soustenir*, *de [r o u] moien*, *leur [a i e u m e n t] peult faillir*, *ie suis [d i r e] que
  [m e s e] ceste armée*.
- l. 24-25: *quand il fault [47] [e s a] faire recongnoistre que l'on [n i n t e m e e]*.
- l. 29-30: *au roi la [?presence] [76] où ien que voir selon veult mis en dique sur ceste [ar e sse]*; l. 32 *tant
  qu'elle [s s i a e n t r e m i s s i e s]*; l. 33 *ie [?ne] [?meritois] [?poinct]* (one h fewer than Brackx, the
  crossed 8 where *o* is needed); l. 35 *fidelle [s a n t a u i u e] de personne*; l. 36 *plustost que [l e l a c r
  a i n e]*.
- Codes 45 (twice) and 47 (twice) open where the context does not settle them.
- These breaks are not on the image (the figures are legible); they are either wrong letter sets for this hand or
  figures still misclassed. A third pass would test the leaf key on them (B with a, 3 with o, the crossed 8) and
  re-cut lines 1-2, 14-16 and 29 at 4×.

## Pass 3 (22 Oct 2026): the remaining breaks against the sets and the image

`_check_reading.py --file texts/reading_f110.md` before: 76 sentences, 43 clean, **clean share 0.566**, hole rate
0.161.

**Method.** The pass-2 figures (`f110_v2_cipher.txt`) were re-aligned to the ink segments of the straightened line
bands and every break listed at the end of pass 2 was cut again at 3.2× to 6× (crops in the session scratchpad,
`matignon_img/f110/z*.png`, not in the repo). Each break was read against the letter sets first, then the figures
under it were compared with the exemplars. A small word-level search over the letter sets (word list and bigrams
from `lang/corpora/fr-henri4.txt`; scratchpad `wd.py`, not kept) was used to list candidate words for a span; it
found *dissiper* (l. 29), which was then checked figure by figure.

**Label changes** (`brackx2026/corrections/f110_v3.tsv`; corrected file `brackx2026/corrections/f110_v3_cipher.txt`,
2,121 figures, as pass 2):

| line, token | v2 | v3 | what the image shows | what it gives |
|---|---|---|---|---|
| 1, 27 | Ca | sw | a tilde with a long tail looping down, not the hooked Ca | *vous verres bien* |
| 3, 36 | oo | sw | the same open tilde with a tail, not the closed double loop of oo (l. 4, *et de*) | *avecq vous, avec ce* |
| 10, 0 | n | m | a three-stroke m, like the m at l. 10 tokens 12 and 16 | *sans argent* (l. 9-10) |
| 16, 6 | U | 8 | the g-like 8 of *guerre* (l. 12) | *leur argument peult faillir* |
| 30, 8 | t | pl | the 4 with a tail below, not the plain cross t (token 11) | *ceste armée* |
| 32, 37 | th | h | an h closed at the top with a long foot, not the crossed 8 | *tant qu'elle sera* |
| 32, 48 | S | th | the crossed 8 with its bar, not the long s | *entre mes mains* |
| 33, 43 | th | h | the same closed-top h as l. 32 | *ie merite* |

**Leaf key** (`key_cipher1_f110.json`): new label **sw = s**, the tilde with a looped tail. It occurs twice on the
leaf and both places need s (*verres*, *vous*); no other value fits either. Cl = l/r (proposed in pass 2) was already
in the file. No other key change. The other tests pass 2 proposed were run and failed: B + a, 3 + o and th (the
crossed 8) + o/n were each added to the leaf key and the word search re-run on ten open spans (ll. 2 twice, 8-9,
10, 14, 16, 24-25, 25, 33, 36-37). None turns a span into French: B + a gives *sera tenu de lui* at the start of
l. 2 against *se retenu de lui* (no better; the rest of the line still fails) and nonsense elsewhere (*ait suis
isle*, *craian*); 3 + o and th + o/n change nothing that reads (*une si c* l. 16). None was adopted; the crossed 8
stays m/s. The same search gives *toutes a faire* for l. 24-25 (*[47] 3 6 U* + *faire*), which does not make a
sentence and was not adopted.

**Code values from other leaves.** f. 177's copy gives 73 = *le Roy* and 64 = *quelque*; neither group occurs on
f. 110 (here *roi* is spelt out, *7 3*, and in *Villeroy*). 45 and 47 stay open: 45 at l. 10 (*[45]ssement*) and
l. 15 (*le roi de Navarre [45] [?ses] ennemis*) fits no single word; on the crop at l. 10 the group is written as two
figures like 4 and the h-like 5, so it is a code and not two letters (4 then h would give *ecl m e …*, no word).

**Readings gained, all carried by their figures** (no letter supplied by context):
*vous verres bien par la lettre que ie fais au roi* (l. 1); *avecq vous, avec ce qu'avait tousiour faict* (l. 3;
pass 2 printed *tousiours*, but there is no s figure: corrected); *i'ai [?recongn]u dès le commancement* (l. 4-5);
*la guerre sans argent* (l. 9-10); *Retenue qu'il s'en paroist* (l. 11, every letter); *et qu'il la veuile finir,
il ce peult faire plus [?honnestement]* (l. 12-13; pass 2 printed *le plus*, but there is no *le*; *ce* for *se* as
the figures give it, H = o/c); *puis aider ce moien. Car leur argument peult faillir* (l. 15-16); *Au reste ie puis
dire que […] ceste armée* (l. 16; S = p); *l'empeschemant* (l. 22, every letter with M = h, pl = m, ao = a);
*comme à tous [?en] particulier ami, pour me donner* (l. 26-27); *de faire sçavoir au roi la presense le roi de
Navarre où i'en suis, car si l'on veult ainsi dissiper ceste armée, et qu'elle demeure sans secours* (l. 29-30);
*tant qu'elle sera entre mes mains. Sa Maiesté en perdra plus que moi* (l. 32-33); *Que toutesfois ie merite
[?poinct] de recevoir cest affront* (l. 33-34; no *ne* in the figures, and the figure under *n* of *poinct* is the
5-like s = u); *il ne sera iamais plus fidellemant [?servi] de personne que de moi* (l. 34-35; ao where s is
needed). Two pass-2 words were marked down because their figures do not carry them: *[?estat]* (l. 4, x = e/a where
s is needed) and *[?ses] ennemis* (l. 15).

**Layout.** The salutation (*[?Monsieur] de [?Villeroy],*) now stands on its own line, as in the letter; the header
was shortened (it had file paths inside sentences).

`_check_reading.py --file texts/reading_f110.md` after pass 3: 74 sentences, 52 clean, **clean share 0.703**, hole
rate 0.129 (pass 2: 0.566, 0.161). Of the 22 sentences that fail, 8 are the English header, the files line and the
clear dateline (numbers, the place name and the date are counted as holes); 14 are in the cipher.

## What stays open after pass 3

- l. 1-2: *[?Monsieur]* (the cup-shaped figure ub where s is needed; it occurs only here), *[?Villeroy]* (an x where
  the second l is needed; l. 37 writes it n n), six faint figures at the damaged corner of l. 1 (on the image),
  and l. 2 almost whole (*[?retenu] de […] le plus […] que ie […]*): the figures are legible, the words do not form.
- l. 3-4: *[?parler]* (n A T: the A is a crossed triangle, l, where e is needed), *[?confidence]* (7 where n is
  needed), *[?estat]*.
- l. 8: the words after *a pris* (*a n d e t o l b e l a u e*): not formed.
- l. 10: *Comme il a faict […] [45]ssement, que [47] […] paroles, il n'a eu […]*; the group 45.
- l. 14-15: *la guerre […] [?suive]* (the three figures before *suive* give *n e t* / *e s t* sets, no word), *que
  l'en […] ce peust soustenir*, and 45 again.
- l. 16: *ie puis dire que […] ceste armée* (four figures, *s i s i*, no word).
- l. 24-25: *il fault [47] […] faire*, *que l'on […]*: not formed.
- l. 36: *plustost que […] iamais* (ten figures, *r e l a c f a i n e*): not formed.
- Spelling slips the figures carry and the reading keeps marked: *honnrable*, *aduatageuse*, *offr?t*, *tos se*,
  *gonestement* (8 = g where h is needed; the figure is the same 8 as in *guerre* and *grand*).
- These breaks are not on the image (the figures are legible, except the corner of l. 1); they are wrong sets or
  slips of this hand that no single key change fixes across the leaf. A fourth pass would need a second sibling in
  this hand (none is known) or a clear copy.
