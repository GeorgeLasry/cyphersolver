# Riverbank Laboratories sweep (Oct 2026)

Part of the Oct 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`), Chicago-area group. Target: material
from George Fabyan's Riverbank Laboratories, Geneva, Illinois (the Friedmans' cipher department 1916-20) and wherever its
papers went. Output: `candidates.json` (2 rows, source "Riverbank sweep", each with `access`), written by
`make_candidates.py`. Source-by-source detail is in `coverage.md`.

## Where the Riverbank papers went

- **NYPL, Bacon cipher collection, MssCol 176** (30 boxes; gift of Josephine C. Curtis 1960; George Curtis had the boxes
  from Fabyan's widow). Riverbank boxes 13-21. Box-level list only (1982 accession sheet, Wayback copy of
  `baconcipher.pdf`; the live archives.nypl.org sits behind an Incapsula bot check). Ten Baconian items digitised.
- **Library of Congress, George Fabyan Collection**: printed cryptography and Baconian books, item-numbered. No
  manuscripts found.
- **Marshall Foundation (Friedman Collection)**: Friedman-Fabyan correspondence, file 734 (~300 items). Already swept
  in `research/us_friedman`.
- **The WWI working files of the Riverbank Department of Ciphers are probably lost.** In Feb 1948 Friedman looked for
  them. He was told they had gone to the LoC, but he found nothing there. Cora Tyzzer (Geneva) replied that Miss Cumming
  had probably destroyed them after Fabyan's death (NSA Friedman papers, correspondence folder 367, A69876). The NYPL
  boxes 15-16 are the only candidate survivors.
- Geneva History Museum, Fabyan Villa Museum and the present Riverbank laboratory have no online catalogue or
  cipher holdings described.

## Candidates (ranked)

1. **Riverbank "Mexican codes" and unsorted cryptographic papers, 1917-18** (NYPL MssCol 176 boxes 15-16). Importance
   2, solvability 1, archive only. Contents unknown. MI-8 read much Mexican traffic, so many items will be solved. A weak
   lead: NSA historians went through all nine Riverbank boxes and reported page proofs, student exercises on graph
   paper and a few Parker Hitt letters, with "not too many gems" (NSA blog "A great TDY", Doc ID 6919113, read in the
   browser from media.defense.gov; curl and WebFetch get 403).
2. **Conklin's 1925 "C.C. characters" cryptogram of the Declaration of Independence** (NYPL MssCol 176, photographed
   by Schmeh 2018). Importance 1, solvability 4, online. The plaintext is stated by the author, but the symbol system
   was never explained. 1,636 symbols for about 1,400 words points to a word/abbreviation code. If it turns out to be
   a shorthand, drop it.

## Not kept (checked)

- Detective Story Magazine personal-column number cipher (c. 1920, in the same NYPL boxes): solved in the Cipherbrain
  comments, 19 Mar 2018.
- Riverbank WWI work already in the repo or solved: Tampico message (catalogue 674), Gulick/Honytre message, Hindu-German
  conspiracy letters (694, `targets/gupta1917`), Burdick ciphers (from us_friedman), Wheatstone test messages, AT&T
  Vernam challenge 1919, Hebern/Brigman 1924, Waberski (Manly).
- "Riverbanks Ripper" (Schmeh Top 50 no. 39): an April Fools' joke (`research/top50/NOTES.md`).
- Baconian biliteral/word cipher material (Gallup, Owen): excluded by the brief.

## Key leads

None (no bare keys found). The LoC Fabyan Collection holds early printed cipher manuals (Trithemius, Porta-era books)
and W. H. Conklin's "The code word", which may explain row 2's symbols.

## Not reached

- The NYPL item level: boxes 13-21 need a reading-room visit (appointment; the catalogue once marked the collection
  restricted).
- loc.gov returns 403 to scripts. Only WebFetch summaries of the search were read.
- The Geneva History Museum PastPerfect site returns 403, and its archive works by request form only.
- The Newberry catalogue was not searched directly.
