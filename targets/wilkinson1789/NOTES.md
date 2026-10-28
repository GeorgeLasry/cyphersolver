# Wilkinson ('Agent 13') ↔ Spanish governors of Louisiana, c. 1789-1806 (catalogue 761)

Status: in progress
Outcome so far: attempted, open: dictionaries unidentified, decoder 58.6% on the held-out excerpt; blocked on the LoC/AGI scans of leg. 2374.

## Document

James Wilkinson's cipher correspondence with the Spanish governors of Louisiana (Miró, Carondelet,
Gayoso) and their replies. Library of Congress, Manuscript Division, reproductions of AGI Papeles
procedentes de Cuba, legajo 2374 (LoC pp. 1524-1652, 2874-3072; 'File 1', 'File A', 'File B').
The originals are at AGI Cuba leg. 2374.

## Prior work

Chu, Valenti and Knight, "Solving historical dictionary codes with a neural language model",
EMNLP Findings 2020 (arXiv 2010.04746). Data at https://github.com/c2huc2hu/wilkinson (commit
5ecdb089, Oct 2020; no licence file, so their transcriptions are linked here, not copied).
They recovered 75.1% of word tokens on the held-out excerpt LoC 3044-3045. They did not identify
the dictionary and did not attack the 1096 system. Their inventory (`data.txt`) lists about 73
unsolved pages and 28 pages with decipherments that they had not banked yet.

Checked 28 Oct 2026: the arXiv paper, the GitHub repo and this repo (no earlier target). No later
full reading was found.

## System

Two systems, both a numbered word table plus dictionary references:

- `[n]^`: an entry in a numbered table of about 1,240 words. It is shared by both systems: [1078]^,
  [1096]^ and [794]^ recur in both.
- `p.[r]-` / `p.[r]=`: page and row in a printed dictionary. The bar marks the column (one bar for
  col. 1, two bars for col. 2). Suffixes follow as clear letters (`+ing`, `+y`).

**Finding (28 Oct 2026): the two systems use different dictionaries.** `dict_refs_from_wordbank.tsv`
holds the 233 page.row → word pairs pulled from Chu et al.'s wordbanks:

- 1078 system: pages run to about 764 (`764.[14]- you`, `762.[11]= write`), rows ≤ 29, alphabetical
  over about 780 pages (`486 paper`, `556 receive`, `652 subject`).
- 1096 system: pages run to about 432 (`430.[8]- world`, `432.[17]- weak`), rows up to 40, alphabetical
  over about 430 pages (`163 glory`, `303 receive`, `376 this`).

Chu et al. pooled the two into one wordbank, so the 1096 pages were scored against references from
the wrong book. The 1096 dictionary (about 430 pp, two columns of about 40 lines) is about the size of Entick's
*New Spelling Dictionary*. Entick is the book of the 1806 Burr-Wilkinson cipher letter, so it is the
first candidate. The 1078 book (about 780 pp × 2 × 29) is larger: a Johnson abridgement or a Bailey.

### Edition tests (28 Oct 2026)

`alpha_fit.py` places each scanned leaf alphabetically from its headword-like OCR tokens. It then predicts
the page for each anchor word and counts the anchors that land within ±1 page at the best offset
(`test_editions.py` is the cruder test of the word on the page):

- **1096 → Entick's *New Spelling Dictionary*.** The editions of 1772, 1787, 1788, 1791 and 1795 place
  40-46 anchors within a page, all of them in the 1096 range (p. 133-430). The editions of 1766, 1773,
  1776, 1782 and 1790 (bim) and 1791_0 place at most 15. The OCR is too poor to fix the edition at the
  page level. The next step is to read the scans of the best-fitting editions by eye at a few anchors
  (e.g. 163.[28]- glory, 303.[19]= receive, 430.[8]- world), checking the row count too.
- **Page images overturn the edition fit.** The test anchor is 163.[26]- glorious / 163.[28]- glory:
  two rows apart in column 1. The scans place it as follows:
  - 1772: p. 157, col. 2, rows 15/17.
  - 1788 and 1795: p. 167, col. 2, rows 3/5.
  - 1800: p. 167, col. 2, rows 4/6.

  Every one of these editions has 38 lines per column, while the cipher's rows reach 40. The scanned Entick
  editions 1772-1800 are therefore ruled out. The 1096 book is an Entick-sized spelling dictionary
  with 40-line columns. Next candidates: Entick editions after 1800 (reset), Perry's *Royal Standard* (OCR
  test inconclusive), Walker's and Sheridan's abridgements, and the American spelling dictionaries (Alexander,
  Webster's *Compendious* 1806). Check each by eye at glory (p. 163) before any OCR scoring.
- **Second round (same day).** Webster's *Compendious* 1806 (F at p. 117, about 60 small lines) and Perry's *Royal
  Standard* 1806 (J-K at p. 256) are ruled out. Entick 1812 has the cipher's 40-line columns, but
  p. 161 is already HIG-HIS, so glory falls at about p. 150. The cipher's p. 163 sits between the 1800
  printing (p. 167, 38 lines) and the 1812 printing. The 1096 book is most likely an Entick printing of c.
  1801-1811 reset to 40 lines; none is scanned on archive.org. Google Books has none in full view for 1801-1811; it lists an
  1803 Crakelt edition with no preview. HathiTrust's catalogue needs a human past its bot check. Next: search HathiTrust by
  hand, NCCO/ECCO, or a library copy of the 1803-1810 printings (check p. 163 for glory, col. 1, row 28).
- **Third round: Murray's New York Entick of 1804 (HathiTrust nyp.33433070243435) ruled out.** Its pages
  are glory p. 151 (col. 2 row 3), happy p. 157, home p. 162 and receive pp. 262-263. The cipher's pages are
  163, 171, 178 and 303. The lead grows from 12 to 40 pages, so this is a different and less dense book, not
  the same book with an offset. The 1812 scan is the same Murray edition, so the "1801-1811 between the two lines"
  inference is withdrawn. **The 1096 dictionary is unidentified.** Fitting all the 1096 anchors suggests
  about 430 pp with 40-line columns, with the alphabet spread more towards R-W than in Entick. Next
  candidates: Alexander's *Columbian Dictionary* (Boston 1800), Johnson's Dictionary in miniature
  (larger editions), Sheridan's or Walker's school abridgements, Fenning, Dyche.
- **1078: still unidentified.** These tests were negative: Johnson abridgement 1786 vol. 1, Johnson 1792
  vol. 1, the Johnson abstract of 1802, and a 785-leaf 1805 dictionary (BSB 11223846). Still to try:
  Johnson abridgement vol. 2 editions, Bailey, Sheridan, Walker, Perry, Ash.

### Decoding without the book (28 Oct 2026)

The numbered table is alphabetical too: [160] a, [172] and, [664] I, [1078] the, [1216] you, with names and
corrections appended after about 1221. `decode.py` therefore treats both parts as positions in the alphabet. Each
unknown code gets the corpus words that fall between its two nearest known codes, weighted by the linearly
interpolated rank, and a word-trigram beam search picks the text. On Chu et al.'s held-out excerpt (LoC 3044-3045,
485 tokens) it scores **58.6%**, below their 75.1%. GPT-2 rescoring (`rescore.py`) gives 57.9%. The ceiling is the
number of known values (about 110 table and 160 dictionary codes), not the language model. More of them are on
pages we cannot reach: Chu et al.'s Drive scans and spreadsheets are deleted, and the LoC reproductions are not online.

## Remaining gaps

Everything is open. No page has been read here yet.

- Dictionary identification for both books: workable. Test dated editions on archive.org by checking
  each anchor word's page and row.
- 27 pages with decipherments are not banked yet (LoC 2920-2923, 2958-2961, 2998-3006, 3063-3072): workable. Needs the LoC scans.
- Decipherments LoC 2975-2989 and 3014-3018 (for 1614-1624 and 1635-1637): needs the LoC scans.
- About 60 untranscribed cipher pages: needs the LoC/AGI scans.

## Escalation

0a steps: siblings with decipherment are in the same legajo (bank them first); the dictionary is a
printed book (identify it, then every page.row reads directly); the numbered table can be rebuilt from
the banked pages. Not yet run: scans not obtained, editions not tested.
