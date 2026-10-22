# Code signs from the other deciphered letters in this cipher (version 0.2)

19 Oct 2026. Tomokiyo lists these Cipher-2 letters in fr. 15573 with a decipherment of the time: ff. 7–8 (Forget, Aug. 1586), ff. 31–33 (Mayenne, Aug. 1586), f. 97 (Forget), ff. 149–150 (Mayenne, Oct. 1586). Images: the BnF IIIF service, views 18–20, 67–69, 199, 304–306 in full, 2 s apart, each fetch logged with its SHA-256.

## How

- Cipher blocks segmented, then **one reader pass** (Claude Opus 5.5, sheet v3, the settings of pass a). Lines in clear inside the boxes are read as `word`.
- Decoded with key rev 5 untouched. The key reads these letters as French before any change, a check of the key on letters it was never fitted on: "ce sera le plus certain moyen", "je preuoy … pendant lequel … considerera", "Monsieur de la Barge lequel ayant eu nouvelles que sa femme et sa fille sont frapp… de la contagion".
- Every place where a sign without a value occurs was listed, looked at on the straightened line, and aligned by eye with the decipherment of the time: the margin text (ff. 7v, 32v, 33r, 150r), interlinear words (f. 32v l. 13: "aduantage" written over the cipher) or the clear text that follows the cipher (f. 97r).
- The decipherments were read by eye by Claude; they are cursive and often paraphrase, so only places where the word slot is unambiguous count.
- Line numbers are those of the pass, counted from 0 (`s150r l4` = f. 150r, line 4 of the pass).

## Aligned values (key revision 6, `data/key-cipher2.json`)

| sign | value | where (pass line) | cipher, decoded with rev 5 | decipherment of the time | origin |
|---|---|---|---|---|---|
| Qh (an h under a crossed stem) | armée | f. 150r (s150r l4) | "et ceste [Qh] dalieurs si desbauch[N]" | margin: "et ceste armée d'ailleurs si desbauchée" | F |
| | | f. 7v (s007v l10) | "de se par(er) [Qh] ele est si (foible)" | margin: "de separer l'armée elle est si foible" | |
| | | f. 33r (s033r l6) | "faire uiure seulement l[Qh]" | margin: "… seulement l'armée …" | |
| hb (an h with one bar across the stem; new name) | tout | f. 150r (s150r l6) | "re [hb]e neu(f)" | margin: "refaire toute a neuf" | F |
| | | f. 150r (s150r l8) | "que [hb] le seiour" | margin: "que tout le sejour" | |
| N | ée | f. 150r (s150r l5) | "desbauch[N] que" | margin: "desbauchée que" | F |
| | | f. 97r (s097r l15) | "fra(pp)[N]s de la contagion" | clear text below: "frappées de la contagion" | |
| | | f. 32r (s032r l18) | "soyt fort fatigu[N]" | (fits; margin not read) | |
| 17 | tant | f. 97r (s097r l1) | "de se retire(r) [17] est" | margin: "de se retirer, tant il est ennuyé" | F |
| | | f. 150r (s150r l1) | "ie preueoy [17] di(mpossibilite)" | margin: "je prevoy tant d'impossibilité" | |
| 13 | tre | f. 32v (s032v l13) | "se doibt en[13]prendr(e)" | margin: "se doibt entreprendre" | F? (one place) |
| ub (two uprights on a base; new name) | droit | f. 33r (s033r l8) | "la faul[ub] aussi" | margin: "il la faudroit aussi" | F? (one place; f. 97r "faul[ub] souffrir" fits) |

## Seen but not added

- **Φ** (a circle with a stroke through it) on f. 150r reads *vostre majesté* twice ("a [Φ] et a moy", "lequel [Φ] considerera"; margin "a vostre majesté et a moy", "lequel vostre majesté considerera"). Our sheet name `phi` (= *en*, two calibration places) covers a look-alike; f. 385 v l. 7 reads "un' armée [phi] ceste province", where *en* is right. Not changed: no place on f. 385 was shown to be Φ.
- **invT** (an inverted T): its four places on f. 385r (l. 2, 11, 24, 29) all sit where *vostre majesté* fits ("despesche devers [invT]", "ce que [invT] eust peu trouver mauvais", "supplyer [invT] de luy donner congé"). No occurrence was found in the deciphered letters (the reader's "invT" there was the T on its side, *plus*, or `ub`). It stays a conjecture (C?), not in the key.
- 7, 14, 15, 27, 28, 30, x?: no aligned place.

## Relabels on f. 385 (`data/<page>/corrections.json` (`decided_on_the_image`), decided on the image)

The sheet has no row for `hb` or `ub`, so no blind ask could choose them (as round r1's "agent" rows). Qh → hb at f. 385r l. 5, 6, 7 and f. 385v l. 17, 18, 24; invT → ub at f. 385r l. 31 and f. 385v l. 9 (manuscript lines from 1). The Qh places left as Qh show the crossed stem (f. 385r l. 5, 20, 22, 26; f. 385v l. 7).
