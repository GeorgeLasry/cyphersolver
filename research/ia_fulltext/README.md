# Internet Archive full-text sweep, 28 Oct 2026

Brief: `research/archive_sweep_2026-10/BRIEF.md`. Output: `candidates.json` (85 rows). No edits to catalogue.json or docs/.

## Method

* Full-text endpoint that works from a script, no login:
  `https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=<query>&hits_per_page=50&page=N`
  (`fts.py`). Returns page-level hits with `identifier`, `page_num` and a `highlight.text` snippet. Exact phrases in
  double quotes work. A volume's OCR is at `https://archive.org/download/<id>/<id>_djvu.txt`.
* `harvest.py`: 60 phrase queries in English ("cipher not deciphered", "cipher undeciphered", "in cypher, not
  decyphered", "unintelligible cipher" ...), French (chiffre non déchiffré, indéchiffré), German (Chiffren nicht
  entziffert, Geheimschrift nicht entziffert), Italian (cifra non decifrata), Spanish (cifra sin descifrar),
  Dutch (cijfer niet ontcijferd), up to 4 pages of 50. 470 page hits, about 400 volumes (`hits_raw.json`).
* `dl.py`: downloaded the OCR of every hit volume (about 270 succeeded; many hits are modern books, DTIC, fiction).
* `extract.py`: regex over the whole OCR (cipher-word within 40 characters of an "undeciphered"-type phrase),
  about 1,000 context windows (`matches.json`), then hand reading with `show.py`, `ctx.py`, `head.py` (nearest
  calendar entry number). Entry numbers, sender and date come from the printed calendar; where the heading could
  not be read the row says "to confirm" or "verify".
* `build.py` + `rows.py` write `candidates.json`. Every row carries the archive.org volume link with `?q=` search
  and the plain-text OCR link. All rows are `seen: catalogue` (the printed text), none viewed against an original.

## Counts

470 page hits; about 400 volumes; about 1,000 regex matches; about 250 reviewed by hand; 85 rows kept
(class A 17, B 40, C 28). Dropped: matches where a decipher follows in the same edition ("Decyphered on following
paper", "deciphered by Ormond", Phelippes decipher printed), modern books, novels, numismatic "unintelligible cypher",
and bare mentions with no document identified.

## Best leads (ranked)

1. **Heathcote / Fanshawe 1664, Bennet to Fanshawe, 6 Oct 1664**: eight pages of cipher, HMC says the key is among
   the papers and the plaintext is the letter of 25 Aug 1664 printed on p. 283 of Fanshawe's Letters. Crib plus
   key: solvability 5. Also the 13 Jun 1664 six-page companion.
2. **Charles I to Ormond ciphers in the Clarendon calendar vol. I** (nos. 1815, 2312, 2401) and Hyde to Nicholas
   no. 2505 (29 Apr 1648, "nearly all in cypher"): siblings are decyphered in the same volume, so the royalist
   key can be rebuilt.
3. **Ghinucci (Bishop of Worcester) 1530, Cotton Vitellius B. xiii**: six "Cipher, undeciphered; mutilated" letters
   to Henry VIII (LP IV pt 3 nos. 6140-6191) plus the Spanish pair of 12/15 Feb 1529 in Planta. The Lee-Worcester
   key family is already in this repo.
4. **Spinelly to Wolsey 1518** (mostly cipher: 2 Apr, 30 Jun, 16 Aug): three long letters, LP II pt 2.
5. **Condé to Elizabeth, 6 Dec 1562** (CSP Foreign 1562 no. 1195): repo holds the Condé key R335.
6. Holt to Allen 1588 (Phelippes partial decipher gives a crib), Sir Henry Norris 1569 (no. 285, entirely cipher;
   Cecil-Norris table), the Marsh-cipher letter no. 812 (plain copy precedes it).

## Key leads (bare keys, not rows)

* Calendar of the Stuart Papers vol. III preface, pp. 97-98: name lists for Sir P. Lawless's cipher names,
  "not deciphered in the originals" (Bloiin, Brignon, Burin, Chaunin, Despeches, Normand, Renaud's, Vallin).
* Preface of CSP Domestic Commonwealth 1655-56 (cu31924091770432 p. 8): the Nicholas-Jane figure cipher key was
  rebuilt from Jane's interlineations; no key survives for the Ross series.
* Planta (Cottonian catalogue) item 113: "paper chiefly in cypher, not decyphered", 22 Jul 1529 duplicate of a
  Worcester letter.

## Dead ends / not kept

* Calendar of the Correspondence of James Madison: 1785 Jefferson-Madison letters "in cipher not deciphered":
  Madison's own decipherment is in the published Papers of Madison/Jefferson, so these are not open.
* Négociations diplomatiques de la France avec la Toscane (vols 3, 5): footnotes "chiffre non déchiffré" cover a
  single name or sign, no identifiable cipher document.
* "Cipher not deciphered" hits in modern (1960s+) guides to the Public Record Office are generic descriptions of
  the SP series, not items.
* Archivio storico italiano 1842, Giovanni delle Bande Nere: "Segue un pezzo in cifra non decifrata" inside a
  papal ordinance: too short, no folio.

## Not reached / blockers

* The fts search returns page hits capped by relevance, so only about 400 volumes were seen. Volumes of CSP Foreign
  (Elizabeth 1558-59, 1563-66, 1566-68, 1575-77), CSP Spanish, Venetian, Clarendon vol. II-III, HMC reports other
  than Heathcote, and the State Papers Domestic of Charles I did not surface and should be searched next with
  volume-specific queries (`user_query` plus the volume identifier is not supported; download the OCR instead).
* German, Italian, Spanish and Dutch queries returned few usable hits (the OCR of non-English editions is poor
  and the phrases vary: "nicht aufgelöst", "in Ziffern", "chiffrirt").
* Web checks (cryptiana, HistoCrypt, Lasry) were not run for the importance 3-4 rows; `prior_art` says so. The
  DECODE list was not cross-checked item by item; `known.py` was run on names only (Wotton, Throckmorton, Ghinucci,
  Condé, Norris, Lethington, Nicholas ... ), which turned up only the sibling letters named in `status`.
* Calendar dates and entry numbers for items marked "to confirm" or "year inferred" must be checked in the volume
  before the rows go into catalogue.json. Original shelfmarks (TNA SP, BL Cotton, Bodleian Clarendon) are cited
  from the calendar, not from the archive catalogue.
* No Gallica/Google Books full-text route was tried; the IA OCR is page-level only.

## Files

`fts.py` search helper, `harvest.py` query runner, `dl.py` OCR downloader (writes to the session scratchpad, not the
repo), `extract.py`, `show.py`, `ctx.py`, `head.py` readers, `build.py` + `rows.py` row builder, `hits_raw.json` and
`matches.json` raw results, `candidates.json` the output.
