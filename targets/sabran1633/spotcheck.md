# Spot-check of the contributed transcription against the Gallica images (21 Oct 2026)

Images: BnF fr. 4134, Gallica btv1b9060193z, f139 (f. 66r) and f140 (f. 66v), fetched full size from the BnF IIIF
service (openapi.bnf.fr, 6060 x 9009 px; the gallica.bnf.fr IIIF route returned a Cloudflare challenge). Lines cut
and enlarged, compared sign by sign by Claude (Opus 5.5) with `contributed/data/transcription.tsv`, using the sign
names of `contributed/data/key.tsv`. This is a model's check, like theirs; no person compared the signs.

## f. 66v (f140): 59 of 59 signs agree

| line | signs | result |
|---|---|---|
| c140_2 `5 S nt g S tt ff 10 dd` | 9 | agree (du soupson) |
| c140_3 `c pl o g S 11 8 z E` | 9 | agree (decouuert) |
| c140_4a `7 o r S? ff` | 5 | agree |
| c140_4b `7 o pl tt 8 S? ? x m 8` | 10 | agree; the `?` is an ink blot on the image |
| c140_5 `5 pl ll 9 dd E pl m ll 9 u 8 dd o 8 5 a dd ff o 8 E 8 E 7 E` | 26 | agree (de l'intelligence dans cet estat) |

## f. 66r (f139): 113 of 116 checked signs agree

Lines checked: c139_20, 21a, 21b, 22, 23, 23b, 23c, 25a, 25b, 28 (116 signs as transcribed). Not checked: 24a,
24b, 29a-c (33 signs).

Disagreements:
1. c139_23 ends `... dd 8 nt` and c139_23b begins `8 nt 7 35 m 7 3i`. On the image there is one `8 nt` before
   `7 35` (line 4 of the cipher block: `8 S x 7 S pl o ll 11 yb ct 7 d pl dd 8 nt 7 35 m 7 3i [cest tems] nt pl o z 8`).
   The pair `8 nt` is counted twice: 2 signs too many, and the reading "amenes | esa<35>la<3i>" should be
   "amenes a <35> la <3i>".
2. c139_23c `nt pl o lh 8`: the fourth sign is the Z-shaped sign (`z` = r) on the image, not `lh`. With `z` the run
   reads *secre[t]* ("c'est tems secret"?), which is the reading their own OPEN.en.md says the AI-agreed correction
   z→lh broke. The correction should be reverted.

Agreements of note: c139_20 `m a 3i 5 8 ff 7 S g dd pl 5 10 11` (la ⟨3i⟩ de Savone dou-) and c139_22 (… pris
prisonniers le [blot] munitionnaire …): the blotted sign at position 15 of c139_22 is a blot on the image too.

Total over the two leaves: 172 of 175 checked signs agree (98.3%); the three disagreements are transcription
choices (one duplication, one reverted-worthy correction), not key problems.
