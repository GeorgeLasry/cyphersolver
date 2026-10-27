# Document in cipher with an English cover, AGS Patronato Real (Unsolved Catalogue no. 625)

Status: in progress

Blocked on images, for now: PARES (pares.cultura.gob.es) has answered 429 Too Many Requests to every request
from this machine since 26 Oct 2026 21:00 UTC, in curl and in the built-in browser alike, so the record could not
be mapped to its PTR signature and no image was seen. Nothing below rests on a sight of the document. The folder
is named after the printed-catalogue number because the writer, the year and the signature are all unknown.

## The document

- Julián Paz, *Archivo General de Simancas. Catálogo V. Patronato Real (834-1851)* (Madrid, 1912), no. 4715,
  Google Books `V0hQAQAAMAAJ`, page PT4 (unnumbered leaves after p. 540). Entry in full: "Documento en cifra con
  sobre inglés. S. f. Ni descifrado. 2 hoj. fol., en mal estado de conservación." So: a cipher document with an
  English cover (wrapper or address leaf), undated, no decipherment with it, two folio leaves, in poor condition.
- Where it sits in Paz: in the run of undated England pieces (nos. ~4670-4747) that closes the England
  capitulaciones section; the next heading, "Capitulaciones con la Casa de Austria", starts at no. 4748 (PT2).
  The neighbours are: 4682 a minute to Dr Puebla signed by Almazán; 4685 and 4687 Henry VII to the Princess of
  Wales; 4694-4712 the Henry VIII divorce papers (1529-31); 4713 a summary of the France-King of the Romans
  capitulations (late 15th c.); 4714 Dr Angulo on restitution of dowry (late 15th / early 16th c.); **4716 and
  4717 Catherine, Princess of Wales, to Dr Puebla** (4717 dated "Rixamonte [Richmond], hoy jueves en la noche").
  Paz did not keep strict date order in this run, so the neighbours suggest, and do not fix, a date between the
  1490s and 1509. Catherine was Princess of Wales from 1501 to 1509; Puebla was in England 1488-89 and 1495-1508.
- The PTR signature (PTR,LEG,<n>,DOC.<m>) is not given by Paz and could not be looked up (PARES 429). The
  England capitulaciones are PTR legajos 52-54 on PARES.

## Possible coincidence with catalogue rows 615-618

catalogue.json has four Puebla rows from the same sweep: 615 (PTR,LEG,52,DOC.124, undated 1495, Great Roman
Numeral Code), 616 (PTR,LEG,52,DOC.47, undated 1496, same code), 617 (Puebla to Almazán 21 Apr 1506, PARES
2208061) and 618 (Puebla to Ferdinand 15 Apr 1507). 617 and 618 are dated, so Paz's "S. f." rules them out. 615
and 616 are undated and could be no. 4715. Paz's other Puebla cipher pieces are described differently (no. 1274,
Puebla 1498, "cifra y descifrado"), and the sweep's scan of every page of Catálogo V for "cifr" found no other
undated Puebla cipher item, which suggests Paz did not describe DOC.124 and DOC.47 as cipher at all, or that one
of them is no. 4715. This cannot be settled without PARES: compare the leaf count (2 folio leaves), the condition
note and the English cover.

## Key material to try once images are in hand (Tomokiyo, cryptiana `code/spanish.htm`, copy in `targets/esp318/lit/crypt/spanish.htm`)

- Puebla's Great Roman Numeral Code (1495-1507): full 2,400-element key extant, AGS PTR,LEG,52,DOC.33 (copied by
  Bergenroth 1861; a margin note says "another fragment of the original of this copy" exists). First choice if the
  text is in Roman numerals.
- Puebla's First Cipher (letter substitution, used 1496-1507; Tomokiyo's reconstruction and Bergenroth's no. 6).
- Puebla's Second Cipher with Puebla's Letter Code (monosyllables b-/c-/d-/f-/g-/h-/l-, 1496-1505).
- Earlier: the 1488 Roman numeral code, the 1491 Arabic numeral code, the 1494 letter code (Bergenroth nos. 1-4).
- Other England ambassadors' ciphers on the same page (Ayala, Londoño, Fuensalida, Estrada) if the hand or the
  cover points away from Puebla.

## Prior art

None found. Web searches (27 Oct 2026) for the Paz wording and for the PTR leg. 52 signature found nothing.
Bergenroth's 1868 Supplement to CSP Spain i-ii (archive.org `10278826bsb`, `bub_gb_9q8MAQAAIAAJ`) has no undated
cipher piece with an English cover; its only "letter without date ... deciphering" is a Tortosa 1520 piece. CSP
Spain i itself (1862) was not grepped: no full-text copy turned up on archive.org (the `dli.ministry.01111` file is a
fragment). Bergenroth calendared only what he could read, so an item Paz still called "Ni descifrado" in 1912 is
unlikely to be in it, but this is unconfirmed. Not on DECODE; not in the repo before this folder.

## Remaining gaps

- The whole document: needs-physical-access, temporarily. PARES is rate-limiting this IP; the item is very
  likely digitised (PTR England legajos are imaged on PARES), so this is a retry, not an archive order.

## Escalation

- Siblings: map no. 4715 on PARES first, then compare with catalogue 615/616 (PTR 52 DOC.124 and DOC.47).
- Clear pages: the English cover may carry an address or docket naming writer or recipient.
- Known keys: Puebla's Great Roman Numeral Code (PTR 52 DOC.33) and First Cipher, then the other Puebla keys above.
- Print: grep Bergenroth CSP Spain i (BHO or a full archive.org copy) for undated cipher pieces once the hand and
  date are known.
- Next step: when PARES answers, search `catalogo/find?texto=cifra` restricted to Patronato Real (or open
  PTR,LEG,52-54 records whose title has "cifra" and "S. f."), fetch the images with the route in the memory note
  `pares-access-and-search`, transcribe, count signs and try the PTR 52 DOC.33 key before any solver run.
