"""Write candidates.json for the Riverbank sweep (Oct 2026). Run: python make_candidates.py"""
import json, pathlib

NOTE = "Scored from the archive description during the Oct 2026 Riverbank sweep (research/chi_riverbank/); not viewed"
ROWS = [
  {
    "year": 1925, "date": "1925",
    "title": "W. H. Conklin's 'C.C. characters' cryptogram of the Declaration of Independence, 1925, in the Riverbank papers",
    "correspondents": "William H. Conklin (author) -> unknown (copy in the Riverbank / Fabyan files)",
    "place": "unknown (USA)", "language": "English", "region": "Americas", "period": "1901-1950",
    "shelfmark": "New York Public Library, Manuscripts and Archives Division, MssCol 176 (Bacon cipher collection), Riverbank Labs boxes 13-21 (box not cited by Schmeh)",
    "folio_note": "One sheet: three title lines plus about 39 columns x 41 rows of invented symbols; footer: '1339 words with the names of its 56 signers (capitalization and punctuation indicated) keyed ... in 1636 C.C. characters', 'Copyright 1925'. A second Conklin copy is in the Louis Kruh collection (National Cryptologic Museum) and his 'The code word' is in the LoC Fabyan collection.",
    "cls": "B",
    "status": "Plaintext stated by the author (the Declaration of Independence, 1,339 words plus the 56 signers' names) but the system was never explained: 1,636 symbols for about 1,400 words means a word/abbreviation code, not a letter cipher. Schmeh (Cipherbrain, 25 Mar 2018) printed the sheet; the 15 comments identify the author (Conklin) but nobody mapped the symbols. Not on DECODE; not in the repo (known.py: Conklin, Vosiklin, Declaration of Independence).",
    "why": "A known-plaintext key recovery of a 1920s amateur code system that reached Riverbank; small historical weight, but a clean test case (full plaintext available).",
    "importance": 1, "solvability": 4, "difficulty": 2,
    "score_note": "Scored from Schmeh's photograph of the sheet (viewed) during the Oct 2026 Riverbank sweep (research/chi_riverbank/)",
    "verify": "Transcribe the symbols from Schmeh's 1010x1500 photo (or order a scan of the NYPL sheet), align with the Declaration text word by word and check whether symbols are words, abbreviations or a shorthand; if it is a shorthand, drop it (brief excludes shorthand).",
    "links": [
      {"label": "Schmeh, Cipherbrain 25 Mar 2018 (photo of the sheet)", "href": "https://scienceblogs.de/klausis-krypto-kolumne/2018/03/25/an-encrypted-message-from-1925/"},
      {"label": "NYPL finding aid, MssCol 176", "href": "https://archives.nypl.org/mss/176"}
    ],
    "seen": "image", "source": "Riverbank sweep",
    "prior_art": "plaintext stated by the author; system unexplained (checked 28 Oct 2026: Cipherbrain post and comments, web search 'Conklin cryptogram')",
    "access": "online"
  },
  {
    "year": 1917, "date": "1917-1918",
    "title": "Riverbank Laboratories 'Mexican codes' and unsorted cryptographic papers (the surviving Riverbank Department of Ciphers files)",
    "correspondents": "Mexican government / agents (intercepted) -> Riverbank Department of Ciphers (W. F. and E. S. Friedman) for the State, War, Navy and Justice Departments",
    "place": "Mexico / USA", "language": "Spanish (presumed)", "region": "Americas", "period": "1901-1950",
    "shelfmark": "New York Public Library, Manuscripts and Archives Division, MssCol 176 (Bacon cipher collection), box 15 'Riverbank Labs -- student exercises and lessons, Mexican codes' and box 16 'Riverbank Labs -- unsorted material concerning cryptography'",
    "folio_note": "Box-level description only (1982 accession sheet, 33 boxes). Not digitised (NYPL Digital Collections shows 10 Baconian items only). Contents unknown: could be worksheets, intercept copies or training exercises built from them.",
    "cls": "B",
    "status": "Friedman's own accounts (NSA Friedman papers, folders 433/513) say Riverbank worked codes and ciphers forwarded by State, War, Navy and Justice in 1916-20; a 1917 Army note quoted in a web search summary says the main work was Mexican messages (source PDF not opened). Friedman wrote in 1948 that the Riverbank cipher records were thought destroyed after Fabyan's death (Cora Tyzzer letter, NSA A69876) and that the LoC Fabyan collection held none of them; the NYPL boxes came via Fabyan's widow to George Curtis (gift 1960), so these two boxes may be the only survivors. MI-8 broke several Mexican government codes in 1917-19 (repo: research/nara_triage_c/e), so many messages will be read; whether any are unread is unknown. Schmeh (2018) saw three boxes, not these. NSA historians (Dave Hatch and a colleague, a November visit, year not given) went through all nine Riverbank boxes and found them 'very duplicative and mixed': page proofs of Riverbank publications, student folders and exercises on graph paper, a few Parker Hitt letters; no cipher intercepts are mentioned (NSA blog 'A great TDY', Doc ID 6919113, released 30 Mar 2026).",
    "why": "The only known surviving working files of the first US government cryptanalytic unit (Riverbank 1917-18); any message they hold unread is WWI German-Mexican traffic.",
    "importance": 2, "solvability": 1, "difficulty": 3,
    "score_note": NOTE,
    "verify": "Request boxes 15 and 16 of MssCol 176 (NYPL Brooke Russell Astor Reading Room, appointment); list each cipher text and whether a solution sheet is with it; compare with the MID 10020 Riverbank monthly 'undeciphered messages' reports (catalogue 674).",
    "links": [
      {"label": "NYPL finding aid, MssCol 176", "href": "https://archives.nypl.org/mss/176"},
      {"label": "Box list (1982 accession sheet, Wayback)", "href": "http://web.archive.org/web/20221013194911/https://nyplorg-data-archives-production.s3.amazonaws.com/uploads/collection/pdf_finding_aid/baconcipher.pdf"},
      {"label": "NSA blog 'A great TDY' (Doc ID 6919113): visit to the 9 Riverbank boxes", "href": "https://media.defense.gov/2026/Jul/14/2003961157/-1/-1/0/NSA%20%20HISTORY%20ROCKS%20%20A%20GREAT%20TDY.PDF"},
      {"label": "NSA Friedman papers: Tyzzer letters 1948 (A69876)", "href": "https://www.nsa.gov/Portals/75/documents/news-features/declassified-documents/friedman-documents/correspondence/FOLDER_367/41732499077173.pdf"}
    ],
    "seen": "catalogue", "source": "Riverbank sweep",
    "prior_art": "unknown; box never described item by item (checked 28 Oct 2026: NYPL finding aid, NYPL Digital Collections, Cipherbrain 2018 visit report, Sheldon Friedman guide)",
    "access": "archive"
  }
]
pathlib.Path(__file__).with_name("candidates.json").write_text(json.dumps(ROWS, ensure_ascii=False, indent=1), encoding="utf8")
print(len(ROWS), "rows")
