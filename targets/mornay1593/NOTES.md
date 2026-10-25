# Duplessis-Mornay circle: undeciphered figures printed in the 1824 *Mémoires et correspondance*

Status: in progress

Opened 25 Oct 2026. Found while checking whether Archives nationales 402AP/13 (catalogue 365, "lettres chiffrées"
of the Mornay family) was already in print. It is not, but the printed edition itself carries unread cipher.

## Source

*Mémoires et correspondance de Duplessis-Mornay* (Paris: Treuttel et Würtz, 1824-25), 12 vols. archive.org
`mmoiresetcorre01morn` … `mmoiresetcorre12morn` (vol. 7 text is short in that copy; use `mmoiresetcorresp07morn`).
Page images: `https://archive.org/download/<id>/page/n<leaf>_w1600.jpg`; leaf from `<id>_page_numbers.json`
(vol. 5: printed p. 471 = leaf 480, p. 487 = leaf 496).

Editors' note, vol. 6 p. 82 n. 1: they kept the figures they had a translation for (printed above them) "afin que le
lecteur puisse y recourir pour traduire les chiffres dont nous n'avons pas la clef". So passages printed as bare
figures were unread in 1824.

## Inventory of cipher in the edition

| Vol./letter | Writer → recipient, date | State |
|---|---|---|
| 5, CCI, pp. 471-475 | Du Maurier → Duplessis, "mardi .. juin 1593" | **bare figures, 6 passages, 72 groups** |
| 5, pp. 487-488 | J. de Serviez → Duplessis, 6 Jul 1593 | **bare figures, 2 passages, 21 groups**, same system |
| 6, LVI, pp. 82-85 | Catherine de Parthenay (Mme de Rohan) → Mme Duplessis, Paris 30 Jul 1594 | figures printed **with** decipherment above; a ready key (syllabic/homophonic, e.g. 158 = re, 162 = Sa, 49 = n) |
| 6, CVII, pp. 179-181 | Loménie → Duplessis, Paris 24 Feb 1595 | bare figures, different system (many groups x10: 610, 810, 910), plus small numbers as name codes (3, 11, 16, 25, 26, 98, 99) |
| 6, CIX | Duplessis → his wife, 1595 | short bare run |
| 7, LXVI-LXVII, CXLI and others | Duplessis, Jan-Oct 1597 | bare figures |
| 8, p. ~507 | Duplessis, 14 Apr 1598 | short run |
| 11, CXCVII | 2 Dec 1611 | name codes only |

Not yet transcribed: everything after vol. 5. The Rohan 1594 key should be tested on the 1595-98 figures first: same
household, and the editors expected readers to do exactly that.

## The 1593 system (vols. 5)

`ciphertext.txt` has all eight passages with their clear context. 93 groups, 62 distinct; repeats 149, 912, 129, 2210,
515 (x4). Groups split into two numbers of 2-24 (2210 = 22|10, 1020 = 10|20, 912 = 9|12), and both halves use the same
set of values (1 and 3 never occur in either half).

Context cribs:
- P5 "la maison de [10 groups]": the house of the vicomte de Pont-du-Château, younger brother of the marquis de
  Canilhac (family Beaufort-Montboissier-Canillac). P1 and P5 both open with 192.
- P1 follows "une particularité … que," and precedes "avec les cérémonies et circonstances": the July 1593 conversion
  of Henri IV is the topic of the letter.
- S2 "le roy est [1014 215 17]".

## Steps

1. Literature: no decipherment found (web search, 25 Oct 2026).
2. Hypothesis A, two letters per group: annealed number→letter onto `fr-1600-letters` with a frequency penalty
   (`anneal_pairs.py`). No French in 10 restarts. Failed.

## Remaining gaps

- All 93 groups of 1593: no key; under 100 groups. Next: test one-unit-per-group (homophonic/syllabic) with the P5
  name crib, and look for more Du Maurier/Serviez letters of 1593 in vol. 5 and in BnF/Institut copies of the Mornay
  papers.
- Loménie 1595 and Duplessis 1597-98 figures: not attempted.

## Escalation

- Siblings: transcribe every bare-figure passage in vols. 5-8 and pool by system.
- Known keys: apply the Rohan 1594 key (vol. 6) to the 1595-98 figures.
- Archive: AN 402AP/13 (Mornay key to Mme du Bourget; requested 25 Oct 2026) and the Mornay papers in the
  Bibliothèque de l'Institut / BnF may hold the 1593 key or the originals with interlinear decipherment.
