# Marshall Foundation William F. Friedman Collection sweep (Oct 2026)

Part of the Oct 2026 US archive sweep (`research/archive_sweep_2026-10/BRIEF.md`). Output: `candidates.json`
(12 rows, source "Marshall Foundation Friedman Collection sweep"). Coverage counts are in `coverage.md`.

## Method

1. **Item guide.** Sheldon, *The Friedman Collection: An Analytical Guide* (Marshall Foundation 2014, 646 pp.),
   recovered from the Wayback Machine because the Marshall site no longer hosts it. `parse_guide.py` splits it into
   2,655 items and runs keyword passes; promising items were read in full (see coverage.md).
2. **Marshall library portal** (Soutron, `library.marshallfoundation.org`): the William F. and Elizebeth S. Friedman
   saved searches paged in the built-in browser (850 photo records); `soutron_records.py` fetches record metadata by
   CID (3 s spacing). Thumbnails of ~25 cipher photographs viewed.
3. **NSA Friedman Collection of Official Papers** (nsa.gov, browser only; scripts get 403): 7,936 document titles
   and 665 folder titles harvested, filtered, 17 PDFs read in-page.
4. Dedupe with `known.py` (Friedman, Clinton, Cornwallis, Rochambeau, Luzerne, Arnold, Jefferson, Wharton, Lovell,
   Winterhalter, Burdick, Dee); prior-art web searches for the importance 3-4 rows.

`make_candidates.py` writes `candidates.json`. `cache/` (guide PDF and text, record JSON) is git-ignored.

## Best leads

1. **Cornwallis ↔ Clinton undeciphered letters** (Item 796.6, photostats of Clements Library Clinton Papers, with
   WFF worksheets). Key family known (Lovell broke it; `targets/balfour1781` rebuilt the southern Common cipher).
2. **Rochambeau → La Luzerne intercepted letter** (Willcox 1945, Item 796.7): British New York could not read it and
   sent it to London; the cipher sits in the Clinton Papers; no decipherment found. Try the Rochambeau army codes in
   Beinecke GEN MSS 146 box 5 (see `research/us_beinecke_folger`).
3. **Wharton vols. 4-5 cipher passages undeciphered in 1956** (Item 14): Continental Congress diplomatic letters; a
   sibling of `targets/dana1783`. High solvability: text in print, originals in PCC (M247).
4. **Three categories of Revolutionary syllabaries Friedman could not solve** (Item 796.1) and **ESF's unfinished
   1952 work on British systems in the Clinton Papers** (Item 796.8).
5. **Arnold's "treasonable cow letter"** (Item 611; NSA A62872 slide), open code, Sept 1780.

Lower: Winterhalter painting cipher texts (Item 1040, Tiltman's photo; WFF failed), "Burdick ciphers" WWI
German-Mexican conspiracy (Item 1931), challenge ciphers (Items 1956 K, 212; NSA A273674), Rhea Smith's
unidentified 16th-century "cipher" book (NSA A67868).

## Key leads (keys / key material, no ciphertext)

- Item 796.4/796.5: Force Book of Cyphers photostats (LoC), Dumas cypher, UVA code list A1-I14, "Robert Patterson's
  cipher", Monroe cipher original (WFF thinks), Pendleton cipher: keys for Continental Congress and Jefferson-era
  letters (cf. catalogue 483/484).
- Item 796.3: partly reconstructed code C6 (Burnett Papers, LoC) and an unattributed syllabary in PCC no. 59 vol. 1.
- Item 675-675.3: Burr-Wilkinson cipher keys and decipherments; 675.2 index of Wilkinson cipher passages in AGI
  Papeles de Cuba (LoC photofilm 1930).
- Item 187: Federal Army cipher books (seven of eleven) and W.R. Plum's worksheet book (Civil War, Union route
  ciphers).
- Item 1956 G: an actual message in Gregory's 1885 War Department telegraphic code.

## Dead ends (checked, not kept)

- Item 42: Jefferson to Madison 14 Feb 1783 and to the Governor of Virginia 18 Mar 1784, "code groups never decoded"
  (Ford's edition); Madison decoded the 1783 letters with Code No. 1 and the Boyd/Hutchinson editions print them.
  Not kept; worth a check only if Founders Online shows gaps.
- Item 677 (Greene-Rochambeau), 796.9 (British diplomatic messages 1794), 796.10 (Jefferson code letter for
  Butterfield), 951, 835 (Wren), 1719 (TR-Dewey 1898), 1064 (Hindu ciphers), 660-669 / NSA A4148934 (AT&T Vernam
  challenge messages 1918): all solved by the Friedmans.
- Item 694 (Winthrop), 956 (Pamba Berinda, two words, read in the article), 1885 (Lafayette Baker cipher, Neff's
  disputed 1961 "solution"), 822 (1931 treasure hunt: a map, no cryptogram), 941 (Dee's Enochian tables, not a
  cipher letter), 1026.1 (Dorabella, famous), 1405.1 (Chaocipher, solved 2010).
- Portal photographs: lecture illustrations of famous solved items (see coverage.md).
- NSA folder 532 (1931-32 cipher machine tests) and 545 (AT&T printing telegraph): machine ciphers, solved.
- NSA A67090 (1952 garbled telegram), A70100 (Jefferson "medallion" = Réaumur-Fahrenheit table), A64707 (Gallup
  biliteral inquiry), A4148659 (1944 German clandestine decrypt), A4148613 (1942 alleged Axis decipherment).

## Not reached

Physical folders are not digitised; every guide row needs a scan request to the Marshall Library or the original
holder (Clements Library). The ESF manuscript box list and old Marshall collection pages had no Wayback copy.
Internet Archive was down on 27 Oct, so its mirrors of the NSA PDFs were not used.
