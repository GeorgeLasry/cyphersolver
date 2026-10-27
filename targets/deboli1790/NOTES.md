# Deboli → Stanisław August, St Petersburg cipher despatches, 1790 (catalogue 419) — NOTES

Status: no write-up

**Verdict: closed, deciphered at the time.** Sessions 2026-10-26/27. Each of the 109 cipher despatches in
AGAD, Zbiór Popielów 4 has its contemporary decipherment, made in the King's cabinet. They are filed apart from the
ciphers: 2 Jan–2 Feb 1790 at the end of **ZbPop 417** (k. 353–386) and 5 Feb–31 Dec 1790 in **ZbPop 420**. The
catalogue entry took these Polish texts for "the open despatch of the same day". They are the decipherments.
Nothing in the volume is unread.

## The document

- AGAD Warszawa, Zbiór Popielów (zesp. 12), sygn. 4 ("Deboli. 1790 (cyfry)", old sygn. 302), 350 leaves, 109
  despatches dated 2 Jan–31 Dec 1790, all to the King per AGAD's list. Scans: agadd2 album 4 (469 images); letter
  list with image links: https://www.agad.gov.pl/inwentarze/ZbPop4.xml.
- Form: the heading is in clear French ("St Petersbourg ce 2 Janvier 1790 / reçu le 13", "Sire!"). The body is
  a page of numeric code groups, 1 to 4 digits (0 to about 2160), some with a subscript a, b or c, separated by points.
  The text starts low on the first page. The signature flourish is in clear. No interlinear decipherment.
- Plaintext language: **Polish** (the decipherments). The French heading is the house form of these despatches.

## The decipherments

- ZbPop 420 ("Korespondencja ... z Debolim", 1790, paginated) and ZbPop 417 (1787 XII–1790 II, foliated). AGAD
  lists them as "język: pol.". Each copy repeats the cipher's clear heading, the date and the "reçu le" date.
  Most add "rep:".
- `pairs.tsv` pairs all 109 cipher despatches with their copies by date: 99 in ZbPop 420, 10 in ZbPop 417. Image
  counts per despatch correlate (r = 0.69 over the 92 pairs where AGAD names the King on both sides; 409 cipher
  images against 400 clear).
- AGAD's list gives 17 of the matching ZbPop 420 items as Deboli to **Kiciński**. The one checked (16 July 1790,
  ZbPop 420 pp. 377ff.) is headed "Sire!" with the cipher's "reçu le 27", so it is the King's despatch. The
  inventory's addressee is wrong there and probably for the other 16.
- That the cabinet kept decipherments of Deboli's despatches is known for 1780–1783: Zielińska & Danilczyk print
  Deboli 1780–1782 from "deszyfry" in Archiwum Królestwa Polskiego 265 (introduction to the 1782 volume, IH PAN
  2017, RCIN). Rolnik 2025 (*Rocznik Filozoficzny Ignatianum* 31/3) quotes the 1790–92 despatches from ZbPop
  415/420/421 and notes that this correspondence was in cipher. So historians already use the decipherments. Only the
  link between them and the cipher originals in ZbPop 4 was missing from the catalogue.

## Verification (code groups against the decipherment)

Opening lines transcribed in `transcription_sample.md`. Three code equivalences hold at matching word positions in
two independent pairs:

| group | value | 2 Jan (ZbPop 4 k. 2r / 417 k. 353) | 9 Feb (ZbPop 4 k. 34r / 420 p. 13) |
|---|---|---|---|
| 1559 | w | group 1 = "W oświadczoney", group 13 = "w samey" | group 1 = "W poważeniu", group 21 = "w Warszawie" |
| 1092 | po- | opens "pomiędzy" (group 26) | opens "poważeniu" (group 2) |
| 606 | z | — | group 10 = "z okazyi", group 29 = "z strony" |

The code is a Polish syllabic and word code. Ratio is about 1.3 groups per word. That fits the "Cyfra polska
posłana do Petersburga Deboliemu", 8 III 1783 (ZbPop 444), which is not online. The key was not rebuilt. With 109
aligned pairs it could be (key from adjacent plaintext) if the codebook is wanted for other volumes.

## The sibling volumes (dates matched, not aligned)

| catalogue | cipher volume | year | clear volume | same-date matches |
|---|---|---|---|---|
| 417 | ZbPop 428 | 1788 | ZbPop 417 | 108 of 111 |
| 418 | ZbPop 17 | 1789 | ZbPop 419 (+3 in 417) | 103 of 106 |
| 419 | ZbPop 4 | 1790 | ZbPop 420 + 417 | 109 of 109 (checked) |
| 420 | ZbPop 5 | 1791 | ZbPop 421 | 98 of 105 |
| 421 | ZbPop 416 | 1792 | ZbPop 415? | AGAD has no letter list for 416 |

The 1788, 1789 and 1791 entries very likely have the same answer, but each still needs a pair aligned group by group
before its entry is closed. Catalogue 412–416 (1783–1787, ZbPop 9, 10, 11, 2, 3) have no scans online.

## Not reached

ZbPop 444/451/453/454 (keys) and ZbPop 320 (deciphered register 1774–77): no album on agadd2.

## Sources

- AGAD letter lists: ZbPop4.xml, ZbPop420.xml, ZbPop417.xml, ZbPop419.xml, ZbPop421.xml, ZbPop428.xml, ZbPop17.xml,
  ZbPop5.xml (https://www.agad.gov.pl/inwentarze/); fonds inventory ZbPopiel12.xml.
- E. Zielińska, A. Danilczyk (eds.), *Korespondencja polityczna Stanisława Augusta. Augustyn Deboli 1782* (Warszawa:
  IH PAN, 2017), Wstęp pp. 11–17. https://rcin.org.pl/dlibra/publication/275188/edition/238967
- D. Rolnik, "„Przestrogi dla Polski” Augustyna Debolego, posła Rzeczypospolitej w Petersburgu ...", *Rocznik
  Filozoficzny Ignatianum* 31/3 (2025), notes 10–58.
