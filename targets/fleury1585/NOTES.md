# Henri Clausse de Fleury, French ambassador to the Swiss, 1584-85: the undeciphered ciphers of BnF fr. 16026 and the deciphered sibling Colbert 427 f. 325

Status: in progress (key rebuild from the f. 325 sibling; fr. 16026 not digitised).

Catalogue no. 364. Reported by Michael Brackx (@brackxm, issue #82, 22 Oct 2026), with Claude Code (Claude Opus 5.5).
Nothing here is read yet.

## The documents

From Rott, *Inventaire sommaire des documents relatifs à l'histoire de Suisse conservés dans les archives et
bibliothèques de Paris* I (1882), pp. 193-197, which notes letter by letter whether a cipher was deciphered. Fleury's
whole embassy (1582-86) was checked by Brackx: only two items are marked *non déchiffré*.

| item | date | Rott | images |
|---|---|---|---|
| **fr. 16026 f. 99**, Fleury to Villeroy, Soleure | 22 Apr 1584 | *Quelques chiffres, non déchiffrés* | not digitised |
| **fr. 16026 pp. 130, 130bis**, Fleury to Villeroy, Soleure, two originals | 8 Dec 1585 | *partie chiffrée, non déchiffrée, partie chiffrée, déchiffrée* | not digitised |
| fr. 16026 f. 120, Fleury to Villeroy | 12 Apr 1585 | *chiffré et déchiffré* | not digitised |
| fr. 16026 f. 126 | 29 Sept 1585 | *quelques chiffres; déchiffrés* | not digitised |
| fr. 16026 p. 129 | 3 Dec 1585 | *partie chiffrée, déchiffrée* | not digitised |
| **Cinq cents de Colbert 427 f. 325r**, Fleury to Henri III, Fribourg | 23 Apr 1585 | *Chiffré et déchiffré* | Gallica btv1b10033949q, view 344 |

- **The targets** are f. 99 and the undeciphered part of pp. 130-130bis. The 1585 letters deciphered at the time sit
  next to them (p. 129 is the leaf before pp. 130-130bis), so they are probably in the same key; the 1584 letter
  may use an earlier one.
- **fr. 16026** is not on Gallica; Biblissima lists it (321 leaves) as *numérisation indisponible*, and the BnF record
  says consultation needs authorisation *sur demande motivée*. A contemporary summary of its contents is cited there:
  **fr. 17020 ff. 134-139** (not checked; Gallica's bot check blocked a search here on 23 Oct 2026).
- **Colbert 427** was scanned by Brackx from view 290 to the end (Feb 1584 on): no cipher apart from f. 325r and the
  two name groups on ff. 325v and 326r. f. 353, an *Examen de la depesche de Mons^r de Fleury* (1585, copy), may quote
  deciphered passages; not yet looked at.

## The f. 325r sibling

Clear text, 12 lines; a cipher block of 8 full lines and 5 signs (`f325r_transcription.txt`, transcribed by Brackx
at 7654 × 5802 px from `openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b10033949q/f343/full/max/0/default.jpg`):
276 tokens as written, 231 after taking out dividers `/`, hairlines `///`, raised `o` and dot groups, 43 kinds.
A contemporary decipherment in another hand runs down the left margin in 18 short lines (`f325r_margin.txt`):

> des Jesuistes en Suisses par les autres gens d'eglise, et leurs adherans, ung personnage premier d'autorite, en ce
> party, mettoit p[eyn]e? de les attirer a son oppinion ... de n'avoir aultre respect que sa conscience ... Dieu et sa
> patrie ... Colonnel de [ce]? party.

The margin was read at 2000 px; about 300 letters against 231 signs, so some signs carry syllables or words.

## The partial key (Brackx)

From the f. 325v name group, 17 signs against *messieurs de surich* (Zurich in a period French spelling), one sign
per letter with consistent repeats (`A@` = s, `6` = u, `M` = i twice each): e = `C`, `Z`, `q+`; s = `A@`, `X`, `TRI`;
i = `M`; u = `6`; r = `9`, `OM`; m = `7`; d = `L`; c = `z`; h = `Yx` (`name_groups.txt`). Homophonic, as expected for a
French embassy cipher of the 1580s.

## What was tried

1. **Rigid slide** of the margin text over the block with the partial key (Brackx, 22 Oct): no better than 200
   shuffled keys. A rigid slide fails at the first null or code group, so this is not evidence against the key.
2. **Frequencies** (here, 22 Oct, on the first transcription): the proposed values fit French: `C`+`Z` (e) 14% of the
   block, `9` (r) 6%, `6` (u) 5%, `M` (i) 5%; `C` is the commonest sign.
3. **Gapped alignment** of the corrected block against the margin, anchored on the partial key (Brackx, 22 Oct):
   all 13 raised `o`, all `///` and the dot groups fall as nulls; the multi-letter "codes" proposed change from run to
   run (artefacts). Controls: with the full partial key 2 of 12 random French passages align as well as the margin;
   with the firm values only (`9` = r dropped) the block beats 47 of 50 random passages (p ≈ 0.06); shuffled keys
   score far lower. The key fits French, but one 17-letter group cannot pin the alignment.
4. **Re-read at 7654 px** (Brackx): about ten signs corrected, the important one both `=` in l. 5 read as `C`.

## Remaining gaps

- The f. 325r block: not aligned with its margin - blocker: not-attempted; a second crib is needed to fix the alignment, and the margin itself was read only at 2000 px (re-read at 7654 px is work in hand)
- f. 326r name group, glossed *de monsieur de [?]* - blocker: illegible; the gloss's second line does not read even at 7654 px (S... or B...)
- fr. 16026 f. 99 and pp. 130-130bis (the targets) and the deciphered siblings f. 120, f. 126, p. 129 - blocker: needs-physical-access; not digitised, consultation by authorisation
- fr. 17020 ff. 134-139 (contemporary summary of fr. 16026) and Colbert 427 f. 353 (*Examen de la depesche*) - blocker: not-attempted; possible cribs for the 1585 letters

## Escalation

- [x] siblings: Colbert 427 scanned from view 290 to the end; f. 325r and the two name groups are the only ciphers; fr. 3376 has no cipher note (Brackx)
- [ ] clear-pages: Colbert 427 f. 353 and fr. 17020 ff. 134-139 not yet read
- [ ] known-keys: no Henri III embassy key compared yet (BnF fr. 15913 Bellièvre keys, catalogue 363; Lasry's keys of the 1580s)
- [x] print: Rott 1882 is the inventory only; no edition of the ciphers known; not on DECODE or Cryptoole (Brackx, 22 Oct 2026)
- [ ] key-rebuild: partial key from one 17-letter group; gapped alignment inconclusive without a second crib
- [ ] retry: after a second crib

## Log

- 22 Oct 2026: issue #82 (Brackx): items identified in Rott; f. 325r transcribed at 2000 px with the margin; partial
  key from the f. 325v name group; rigid slide negative. Catalogue no. 364.
- 22 Oct 2026: frequency check here supports the partial key; reply on the issue.
- 22 Oct 2026: Brackx re-read f. 325r at 7654 px and ran the gapped alignment with controls (p ≈ 0.06); fr. 16026
  access conditions and the fr. 17020 summary found.
- 23 Oct 2026: target folder opened from the issue material.
