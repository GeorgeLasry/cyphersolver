# f. 143v tail (ll. 26–35): reading log (22 Oct 2026)

Brief: `READING_BRIEF.md`, method as in `reading_f173_log.md`. Image: Gallica canvas 151 left (fr. 15572, ark
`btv1b9061879d`), the left half (4300 × 6346) fetched at full resolution from openapi.bnf.fr IIIF
(`/iiif/image/v3/ark:/12148/btv1b9061879d/f151/0,0,4300,6346/max/0/default.jpg`; gallica.bnf.fr/iiif answers 403).
Line bands were found from the ink profile, and line and figure crops were kept in the session scratchpad, not in
the repo. Canvases 161–163 were fetched at 1600 px to look for the copy's continuation, and the head of canvas 163
was then fetched at full resolution.

## Pass 0: where the copy breaks, and the published decode

The f. 155r copy ends *… pour son party, où il eust*. In `brackx2026/f143v_cipher.txt` this is l. 26:
`c ao L Ze 3 | 7 g | 12 | x g z Ze` = *party, où il eust*, so the tail starts at token 12 (code 62) of l. 26 and runs
to l. 34 of the transcription. The transcription stops at l. 34, but the image has a 35th cipher line.

`_check_reading.py` on the published decode of ll. 26–34 (`texts/f143v.txt`, header plus those lines, extracted to
the scratchpad): 7 sentences, 1 clean, **clean share 0.143**, hole rate 0.21.

## Pass 1: reading against the letter sets

Read by hand from each figure's letter set (`key_cipher1.json`), not from the beam's choice. Without any change to
the figures, most of it forms: *peu nuire pour*; *et si j'ay grande espérance de l'en retirer du tout* (ei ao B =
j-a-y, 3 e = i-r); *et ce faisant de pouvoir* (q = u); *par son moyen et exemple* (q = o, y = x); *retirer
d'aultres … et places de conséquence* (14 = que, 6 = n); *plus volontiers en ce traicté*; *s'il luy plaist entendre
son intention*; *ayant le tout excepté* (h y dd x c Ze t = e-x-c-e-p-t-e); *dont je me suis engaigé de ma parole,
remis sou…*.

## Pass 2: the breaks, checked on the image

| line | image | effect |
|---|---|---|
| 26 | the "6" before *d'…* is 6 + 1, written like 62 on the same line | code 61 = *beaucoup* |
| 27 | Brackx's first token h is a sign in the left margin, outside the text block | dropped |
| 28 | an o after the final g, left out | *servi-ces* |
| 30, 33 | x with a bar over it, a figure of its own | = mm: *hommes*, *somme* (new label `xb`) |
| 30 | crossed 4 (Tm), not the plain cross | *qui m'a meu* |
| 32 | `1 5` (code 15) and `68` written as one group | *Sur quoy Vostre Majesté* |
| 34 | λ (lam = b), as in *de bons* l. 28, not X | *soubz* |
| 35 | a whole cipher line, not transcribed | *le bon plaisir de […]* |

Ten changes in all (`brackx2026/corrections/f143v.tsv`; full corrected file `brackx2026/corrections/f143v_cipher.txt`).
New label `xb` (barred x = mm) and a new figure `fig` on l. 35. No key file was written for this leaf, because the
reading was made by hand from the sets. A leaf key would add `xb` = mm.

## Pass 3: the rest of the copy

f. 155r (canvas 162, right) ends at its foot on *où il eust*. The brief's "f. 155v = canvas 162 left" is f. 154v
(Forget's letter, cipher and clear, signed). **f. 155v is canvas 163 left**. Its first seven lines carry the rest of
the f. 143 copy, *peu nuire pour beaucoup davantage … remis soubz le bon plaisir de Vostre Ma.té*, then the docket
*M.r du Mayne du x(?)me avril 1586*. After that comes the copy of f. 150r (Brackx's `f155v_f150r.txt` begins
there). It was transcribed from full-resolution crops into `brackx2026/copies/f155v_f143_tail.txt`.

The pass 1–2 reading was then compared with it word by word. The copy and the cipher agree on every word except:
the cipher has *et si j'ay* where the copy has *Et j'ay*; the cipher spells *se* for *ce*, *engaigé* and *parole* for
the copy's *engagé* and *parolle*; and the cipher's last figures (`fig o gg T`) do not spell the copy's *Vostre
Ma.té*.

`_check_reading.py` on the reading's cipher section alone (extracted to the scratchpad): 8 sentences, 8 clean,
**clean share 1.0**, hole rate 0.034. On the whole file, including the English notes and the doubtful clear
postscript: 94 sentences, 59 clean, 0.628. That score is pulled down by the label lists in the notes, not by the
reading.

## What failed or stays open

- **The plain cross (pl)**: at the end of l. 26 it stands where the copy has e (*davantag-e*), and in l. 28 where it
  has r (*tire-r*). The key gives pl = m/s/i, and the l. 30 "cross" that would have been m is in fact a crossed 4
  (Tm). The two letters are left as `[?]`. Either the plain cross is a null or line-end sign that the encipherer used
  for a dropped letter, or there are two figures here that look alike. This is not settled.
- **s[q]ervices** (l. 28): one figure too many. q is plainly written on the image, so this is an encipherer's slip
  or a figure not understood.
- **The closing figures** (l. 35, `fig o gg T`, followed by *me.* in ordinary letters): the copy has *Vostre Ma.té*
  here, but the figures do not spell it, and code 68 for it is used two lines above. `fig` (a long stroke looped at
  both ends, crossed by a bar) is not seen elsewhere. Left open.
- The marginal sign at l. 27 (taken for h by Brackx) was not identified; it may be a reader's mark.
- **The clear postscript** (ll. 35–39: the Marshal emptied Castets and is having it razed; Mayenne expects him in
  two days and has begun investing "ceste place" today) was read from the image only, with several doubtful words.
  The copy on f. 155v does not include it, and nothing else carries it. The page ends mid-sentence (*fort b…*). The
  next leaf, f. 144r (canvas 151 right), is a different letter in another hand ("Sire, …"), so the continuation was
  not found.
- No second reader has checked Brackx's labels on ll. 1–25. Only ll. 26–35 were checked here.
