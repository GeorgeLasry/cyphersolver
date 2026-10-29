# Pietro Pusterla → Francesco Sforza, Gualdo, Ferrara and Milan, 21 Jan - 10 Mar 1447 (BnF italien 1584)

Status: no write-up (lead 1313 closed 28 Oct 2026: every cipher leaf has a decipherment filed with it; the brief says
stop and report where it is. Clear copies not transcribed except the passages used for the code signs below.)

Lead 1313 (research/leads.json, sweep venice_milan_print). BnF italien 1584, Gallica microfilm ark
`btv1b100373864`; folio numbers are the stamped ones (Mazzatinti's). Pusterla, the Duke of Milan's procurator, uses the
key of DECODE R1857 image P11, headed "Marcolinus de Barbavara et Symon Arrigonus — Petrus de Pusterla". The sibling
target is `targets/barbavara1447/` (lead 1314), closed the same day for the same reason.

## Result: each cipher leaf already has a decipherment

The same late italic hand that copied Barbavara's letters (the script looks eighteenth century; not dated) wrote a
clear copy for each Pusterla cipher letter. f. 42 also has the decipherment Mazzatinti lists, a fifteenth-century
"Lettera di Pusterla" on f. 43.

| cipher leaf | date, place | decipherment | Gallica canvas |
| --- | --- | --- | --- |
| f. 13 (slip) | 21 Jan 1447, Gualdo | f. 14, clear copy | 15-16 |
| (not located; Mazzatinti f. 27) | 6 Feb 1447, Ferrara | f. 27 is itself the clear copy | 27 |
| f. 32 (slip) | 10 Feb 1447, Ferrara | f. 33, clear copy | 30-31 |
| f. 42 | 16 Feb 1447, Milan | f. 41r-v, clear copy; f. 43, 15th-c. decipherment | 39-40 |
| f. 67 | 6 Mar 1447, Ferrara | f. 66r-v, clear copy | 63-64 |
| f. 71 | 7 Mar 1447, Ferrara | f. 70r-v, clear copy | 67-68 |
| f. 77 | 8 Mar 1447, Ferrara | f. 76r-v, clear copy | 73-74 |
| f. 81 | 10 Mar 1447, Ferrara | f. 80, clear copy | 77-78 |

The lead's shelfmark also lists f. 47 (Reggio, 24 Feb). Mazzatinti does not mark it as in cipher, and its leaf
(canvas 44) is in the late hand. Not examined.

## Code signs settled from the copies' blanks

Where the late copyist could not read a code sign, he left a blank and drew the sign in the margin. The Barbavara and
Pusterla copies together give these blanks:

| sign | blanks | context | value |
| --- | --- | --- | --- |
| ꝺ+÷ | f. 27 ×2; Barbavara ff. 55v ×2, 74v ×1 | "Ista mane giunsi quà, e subito fui col ___"; "utile ad eso ___"; "se includano li xx m del ___: ma lui [the King] prende el caricho de fare che li pagli"; "el manda dal Signore ___ per quelli vinti millia ducati" | **lord (Marquis) of Ferrara, Leonello d'Este [?]**, from context. R1857's crowded labels read "Ducati Ferrara" over this sign and the next. |
| ꝺ.7 | f. 80 ×2 | "che havevano facto ___ a Cremona ... son andati a Sonzino"; "in strecta pratica pur ___" | Veneziani: R1857 labels it so, and the context fits |
| 9+o | f. 80 ×1 | "Andrea Dandulo nel andare suo per ___ a ha hauto a dire" | qui: R1857 label, fits |
| ∠ | f. 27 ×2, f. 80 ×1 | "venire a le conclusione cum ___ presto"; "provedeva a dicto ___"; "uno capo di squadra del ___ quale è suo parente" | open: R1857 draws it unlabelled |

Sources of these passages: f. 27 copy (canvas 27) and f. 80 copy (canvas 77), read 28 Oct 2026.

## Remaining gaps

- ∠ is unlabelled on R1857 and occurs three times. Blocker: open-codes. A value fitting all three was not found.
- ꝺ+÷ = Ferrara rests on context in five places, not on a written decipherment. Blocker: open-codes. The 15th-c.
  decipherment on f. 43, or Barbavara's glossed ff. 135 and 143, would settle it if the sign occurs there; not searched.
- The cipher original of the 6 Feb letter was not located on the film. Not examined: canvas 28 shows a slip edge.
- The clear copies are not transcribed (only the passages quoted above).

## Escalation

- f. 43 (15th-c.) and the glosses on Barbavara's ff. 135/143 are the places to look for ꝺ+÷ and ∠ written out in a
  contemporary hand.
- A sign-level transcription of the cipher leaves against the copies would rebuild the R1857 key in full, including
  its blotted cells. Not done. The brief says to stop at an existing decipherment.

## Sources

- Gallica BnF italien 1584: https://gallica.bnf.fr/ark:/12148/btv1b100373864
- DECODE R1857 image P11 (key, ASMi; login needed): https://de-crypt.org/decrypt-web/RecordsView/1857
- G. Mazzatinti, *Inventario dei manoscritti italiani delle biblioteche di Francia* t. II (1887).
- Images are not committed; the crops were made with `targets/barbavara1447/crop.py`.
