# DECODE sweep: Venice and Milan (Oct 2026)

Sweep of DECODE (de-crypt.org) ciphertext records connected with Venice, Milan, the Sforza/Visconti and Mantua that
DECODE marks Non-decrypted, Partially decrypted or N/A, against what the repo already holds. Output:
`candidates.json` (5 rows, 183 DECODE records). Done 28 Oct 2026.

## Method

- **API.** The bulk JSON API still works with `targets/bordeaux/decode/cookie.txt` plus the page JWT (`api.py`).
  `dump_list.py` re-fetched the full record list (`list_now.json`, git-ignored): 10,106 records, the same as
  the 19 Sept dump, so nothing new has been added since then.
- **Coverage.** `coverage.py`: the local view dumps (`research/catalogue_harvest/decode/views*.jsonl`) already
  hold full metadata for every in-scope ciphertext record (802 Non-decrypted, 385 Partial, 718 N/A, 428 blank). Only
  Decrypted records and keys are missing there, so no new view fetches were needed.
- **Selection.** `filter.py` (keywords: Venice/Milan/Sforza/Visconti/Mantua/Gonzaga/ASVe/Doge, Venetian
  subject towns) found 321 unique records. `filter2.py` (Venetian family names, sforz-, simonett-, ital. 158x) found
  37 more, all of them the Morosini nunciature (already read here) plus R7898. `series.py` (`series.txt`) groups all
  2,333 in-scope records by holder so that series with no keyword in their metadata could be caught by hand. That is
  how BnF ital. 1583 R7899-R7915 turned up: DECODE gives them no names.
- **Dedup.** `known_batch.py` greps the repo ledgers, target notes and profiles for each R-number. It leaves out the
  raw DECODE dumps, which hold every record.

## What the Venice/Milan pool holds, and what was already handled

| DECODE | What | Repo status |
|---|---|---|
| R1862, R1871, R1873-R1875 | ASVe Busta 27/30 | all handled (r1862, R1874/R1875 notes, README rows) |
| R1849/R1850 | Zambon → Dieci (ASVe) | set-aside catalogue 278 |
| R2292-R2295, R1894, R4450 | Ranzo / Venetian superscript ciphers, BnF fr. 2988/3019/3022/20506 | excluded: ranzo1528, vasto1527 |
| R3694, R3697, R4232, R4249, R4230, R4256, R4224 | Langeac, Selve (Venice), Rangone, Galeazzo Visconti, Bizozola | handled (gramont1529, bizozola1529, README rows) |
| R3705, R4176, R4285, R4286, R4289 | Gonzaga-Nevers letters | handled |
| R1084-R1159 | Maffeo da Treviglio, Buda, ASMi | buda1489 |
| R1854 | Mantua | handled |
| R9505-R9770 (c. 60) | Alonso Sánchez, Venice 1522-23, BRAH 9/23-9/28 | sanchez1522, sanchez1523, lopehurtado |
| R9952, R9966, R9967 | Charles V Cremona 1543, Caracciolo Milan 1537, Vargas Venice 1552 | handled |
| R18-R58 | Card. Morosini (Venetian), nuncio in France 1588-89 | morosini1588 |
| R13-R17, R72-R73, R119 | Bergamo/Como/Lodi bishops (papal nuncios) | handled |
| R974-R1001 | Ronquillo (formerly in Venice) 1676-78 | ronquillo1676 |
| R2252 | BNE ms. 994, letter from Venice | ottobon |
| R7898, R7899 | Sforza 1446, ital. 1583 ff. 68/70 | it1583 |
| R7900/R7901 | Simonetta at Venice 30 Sept 1446 in cipher + contemporary clear text | read at the time; key lead (below) |
| **R7902-R7915** | **ital. 1583, 14 more 1446 cipher records** | **not in the repo: rows 1-3** |
| **R5297-R5587 (169)** | **ASMi Carteggio Sforzesco cart. 1591/1597/1598 "ciphertexts"** | **set aside as catalogue 292 pending an image check; checked here: rows 4-5** |

## Best leads, ranked

1. **Filippo Maria Visconti → Francesco Sforza, six parchment cipher letters, Nov-Dec 1446** (R7902, R7903, R7904,
   R7907, R7914, R7915; ital. 1583 ff. 110-158). Class A: Mazzatinti's 1883 inventory (`targets/it1583/asl1883.txt`,
   p. 232) lists f. 131 as "Traduzione della lettera precedente", a contemporary translation of f. 130 (R7904). It is
   not a DECODE record, but it should be on Gallica (ital. 1583, `btv1b10033686w`). Imp 5 / solv 4 / diff 2.
2. **ASMi Carteggio Sforzesco cart. 1597, 59 cipher letters** (R5380-R5474). I viewed R5430 in full: a folded
   letter wholly in graphic signs, with no decipherment on it. The question that got catalogue 292 set aside ("key
   samples or letters?") is now answered for the sample: they are letters. 115 keys from the same box are on DECODE.
3. **Cart. 1598 + 1591, 110 records** (R5297-R5298, R5476-R5587). The same kind of material, with clear leaves mixed
   in. One thumbnail seems to be headed "Da cifra"; that is a guess from a 200-px image.
4. **Nicodemo Tranchedini and Boccaccino Alamanni, Florence → Sforza, Nov 1446** (R7905, R7906, R7908, R7909; Sforza's
   reply R7910). Class B: Lasry's 1452 Tranchedini key (targets/tranchedini1452) and the Sforza key boxes.
5. **Sforza's envoys at Venice → Sforza, 7 Dec 1446** (R7911-R7913; Contucio, Stavoli, Giordani, Amidani). Class B:
   the Simonetta-Vincentius/Stavoli key (cart. 1597 no. 14) and the R7900/R7901 cipher + clear pair.

DECODE gives the R7902-R7915 records no names. I took the identifications from Mazzatinti's folio inventory. Folio
and date line up for R7903, R7905, R7906, R7907, R7908, R7910, R7911, R7913 and R7915. R7909 (f. 143) and R7912
(f. 151) are inferred.

## Key leads (keys and cribs, not ciphertext rows)

- **BnF ital. 1583 f. 131**: contemporary translation of the Duke's cipher letter f. 130 (R7904).
- **BnF ital. 1584 (1447)** (not on DECODE): more Duke → Sforza cipher letters on parchment, each followed by a
  "Traduzione" (ff. 5/6 Abbiategrasso 10 Jan 1447, ff. 8/9 11 Jan 1447), plus further letters in cipher (ff. 15, 23,
  24: the Duke; f. 2: Federico of Urbino, 3 Jan 1447; f. 13: Pietro Pusterla). This is a 1447 follow-on target outside
  DECODE (Mazzatinti pp. 233-234).
- **R7900/R7901**: Angelo Simonetta at Venice, 30 Sept 1446, "Cum cifra Vincentii", with its "Explication du
  chiffre". A complete plaintext-ciphertext pair for the Vincentius cipher.
- **DECODE key records in the Sforzesco boxes**: cart. 1591 (64), cart. 1597 (115), cart. 1598 (29), record_type 2,
  served as PDFs. No. 14 of cart. 1597 is the Simonetta-Vincentius/Stavoli key (it1583 notes).

## Dead ends and exclusions

- Florence Dieci di Balìa R3753-R3789 hit only on the keyword "dieci" (Florence, not Venice). Left out.
- R2960 (Fontana, *Bellicorum instrumentorum liber*, Venice c. 1420): a technical treatise with a known simple
  substitution, not a letter. Left out.
- R2877 (Yale Mellon MS 29, *Lumen luminum*): alchemical, already in CATALOGUE.md.
- R2254 (BNE ms. 994, a cipher by Gerónimo Sertori, Milanese, N/A): from the description it is a cipher system or
  key in Valle de la Cerda's treatise, not a letter. Noted as a key, not a row.
- R7930/R7931 (Visconti 1727, Add MS 32270): handled (visconti1727).

## Not reached

- I did not open R7902-R7915 or the Gallica leaves (f. 131, ital. 1584). Rows 1-3 are scored from the catalogue
  description only.
- Of the 169 Sforzesco records I looked at 13 thumbnails and one full PDF. Sorting all of them into letters, clear
  decipherments and keys is the first job if rows 4-5 are taken up.
- Prior-art checks: a web search, Cipher Mysteries, and the repo's own notes. I did not re-check Cerioni 1970 or
  Tomokiyo for the 1446 letters.

Images fetched to check leads are in `dl/` (git-ignored with `list_now.json` and `inscope.json`).
