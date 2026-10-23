# fr. 3315 ff. 15r-16r re-read log, 22 Oct 2026 (Claude Opus 5.5)

Task: replace the stub reading (opening line + clear ending only) with a continuous reading built from the
interlinear gloss and a mechanical decode of the cipher signs.

## Images and method

* Gallica native scans via openapi.bnf.fr IIIF (f17 = opening with f.15r; f18 = f.15v left, f.16r right; the
  f.16r half was fetched separately from f18 x>=4250). Cut into line-pair strips (gloss + cipher) at 1.05-2.2x
  with autocontrast; hard words re-cut at 1.7-3x.
* Per line: transcribe the cipher signs (f15_signs.tsv), read the gloss above (f15_gloss.md), decode the signs
  with the table being built (f15_key.md), reconcile. A key value was kept only when it held in several words.
* No sub-agent was used; everything was read directly.

## f. 15r (26 cipher lines)

* Worked. The gloss is legible enough on almost every line, and the signs are large and clean; the two agree word
  for word. Sentences hold from "je ne veulx faillir" to "qu'apres avoir servi".
* Key emerged from lines 1-6: a=1, d=b-shape, e=F, i/j=7, l=3, m=+, n=2, o=8, p=G/(9, q=9, r=T, s=9, t=4,
  u/v=6, x=Z, y=y; then f=crossed +, g=0 (gouvernement), h=h, b=±, c=C, doubling sign ʒ (fisse, elle).
* Name signs: boxed group "Royne mere" (l.4), boxed "Royne" (l.5), `SS` = Roy (l.25).
* Left doubtful: end of l.12 ("et recevoir une conte…"), "tiens" (l.17, struck group), "veid" (l.21).

## f. 15v (25 cipher lines + one gloss-only line at the head)

* Harder. The decipherer wrote small letters on top of many signs, some signs are overwritten or struck, and the
  gloss is fainter. Lines 1 and 6-25 were decoded from the signs with the gloss as check; most of them hold
  (ligue de quatre ou cinq; Picardie et Languedoc; "le Roy ne luy en a point parlé aucunement").
* Failed: lines 2-5 (after "25 ans ceste couronne si fidellement et"): overwritten cipher, gloss mostly lost; only
  "ayant tant", "aviez", "la moitié", "elle a", "recompense", "France" carried. Line 0 (gloss without cipher) unread.
* Unresolved groups: `T1b879` (l.7), `XX` before "une ligue" (l.10), parts of ll.12-16 and 20-23.

## f. 16r (19 cipher lines, then 8 clear lines)

* The earlier notes called f.16r a clear closing. In fact its first 19 lines continue the cipher with a full
  gloss, from "respondu que c'estoit chose ..." (continuing "Je luy ay" at the foot of 15v) to "de peur qu'ilz ne le
  prennent de mauvaise part". All but two groups read (l.1 `21 CF(99F`, l.14 `C824F2bTF`).
* The clear ending was re-read: "Je vous supplie m'excuser si je ne vous escris davantage car il est minuit ...
  je vouldrois estre au paradis. Je supplie Dieu, mon bon frere, qu'il vous donne patience. De Lion ce 16
  septembre." One word after "je ne vous" and "nous [?mene]" stay doubtful.

## Counts

| | cipher lines | tokens in reading | [?word] partly carried | […] holes |
|---|---|---|---|---|
| f. 15r | 26 | 249 | 3 | 1 |
| f. 15v | 25 (+1 gloss-only) | 224 | 7 | 50 |
| f. 16r cipher | 19 | 153 | 0 | 3 |
| f. 16r clear | (8 clear lines) | 84 | 1 | 1 |
| total | 70 | 710 | 11 | 55 |

`docs/_check_reading.py --file` on the reading body alone (notes and header removed): 57 sentences, 46 clean,
clean share 0.807, hole rate 0.065, lang fr, coverage 0.966. The whole file (notes included) gives 0.688; the old
stub gave 0.677, but that was English prose around a two-line French quotation.

## What stays open and why

* 15v ll.2-5 and line 0: overwritten cipher and faded gloss (illegible on the best image; a specialist look at the
  original or a multispectral image might recover them).
* A dozen single groups on 15v and 16r that neither the signs nor the gloss settle.
