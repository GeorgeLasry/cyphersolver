# Scandinavia sweep (Oct 2026): Riksarkivet, Rigsarkivet, Alvin

Part of the archive sweep in `research/archive_sweep_2026-10/BRIEF.md`. 31 rows in `candidates.json` (18 Swedish,
13 Danish). Each row was checked with `known.py` and against the DECODE list dump: none is on DECODE or in the
repo, except where a row says so.

## Method

| Archive | Endpoint | Terms | Hits | Kept |
|---|---|---|---|---|
| Riksarkivet (SE), NAD | `https://data.riksarkivet.se/api/records?text=` (JSON; `sok.riksarkivet.se/api` is blocked by a WAF) + `/archive/<id>.jsonld` for notes and IIIF | chiffer, chiff\*, \*chiffer\*, chiffrerad(e/t), dechiffr\*, chifferbrev, chiffernyckel/-nycklar, ziffer\*, ciffer\*, cipher\*, chiffré\*, hemlig skrift, sympatetiskt, klartext, apostill\*, tolkad(e)\*, krypterad\*, Geheim\*, uttydning\*, osynlig\* | 1,074 records, 811 enriched (start year up to 1925) | 18 |
| Rigsarkivet (DK), Daisy | `https://daisy.rigsarkivet.dk/arkivskaber_eller_arkivserie_liste?c=` + `arkivserie_detaljer?heid=` (title search only) | chiffer, chiffre, chifre, chiffernøgle(r), chifferbrev(e), ziffer, cifre, opsnappede/opsnappet, intercipierte, kodebog, kodetelegrammer and ~50 variants | 55 series | see next row |
| Rigsarkivet (DK), new search | `POST https://soeg.rigsarkivet.dk/api/v1/Search/arkivalier` with `{"searchQuery":..,"pageNumber":0,"resultsPerPage":100}` (searches the series descriptions in full text) | same terms + ciffre, cifferskrift, krypteret, geheime, hemmelig skrift, usynligt blæk | 2,494 records (mostly noise from "ciffer/cifre/koder" = digits) | 13 (both DK routes together) |
| Uppsala UB etc., Alvin | `alvin-portal.org/alvin/resultList.jsf?...&noOfRows=250` in the built-in browser (Anubis bot wall stops scripts) | chiffer, chiffre, chiffré(e), chiffrerad(e), ziffer | 18 + 10 + 6 + 1 + 1 | 0 (see leads) |

Scripts: `harvest_ra.py`, `enrich_ra.py`, `harvest_daisy.py`, `harvest_soeg.py`, `build_candidates.py` (the rows).
Raw hits: `ra_hits.jsonl`, `ra_enriched.jsonl`, `daisy_hits.jsonl`, `soeg_hits.jsonl`. Reading lists:
`ra_view.txt`, `ra_view2.txt`, `soeg_view.txt`. `decode_nordic.txt` lists every DECODE record held in
Stockholm, Uppsala or Copenhagen, for dedup.

Images checked (a few each, kept in the session scratchpad, not in the repo): Lovisa Ulrika K 259 (two contact
sheets and image 107); Biermann copybook (four openings, incl. image 109).

## Best leads

1. **Lovisa Ulrika's secret correspondence, 1764-66** (Riksarkivet, Kungliga arkiv, K 259). 223 images online.
   Image 107 is a full page of 3-digit numeric cipher facing French clear text about the Empress and Saldern.
   The same volume ends with a "Chiffernycklar" folder and three key tables. Class A, likely quick to read.
2. **Conrad Biermann's copybook, 1675** (Rigsarkivet, TKUA, outgoing letters to Danish ministers abroad,
   "a large part in cipher"). 255 images online. Image 109 shows a numeric and symbol nomenclator inside a
   French letter about France, Gottorp and Niels Brahe. TKUA "Chiffer" 1670-1709, scanned, holds "many
   different keys".
3. **Lagau → La Marck, intercepted cipher letters** (Rigsarkivet, TKUA). Catalogued as 1712. La Marck was in
   Stockholm 1717-20, so the date needs checking.
4. **Duke Frederik (I) and Lübeck, 1523, partly in cipher** (Sønderjyske Fyrstearkiver). The series is online;
   the item's pages are not located yet.
5. **Meyerfeldt → Charles XII, 1712-14, "several in cipher"** (Pommeranica). Also Vellingk from Hamburg 1714,
   Johan Casimir 1631, and Charles XI's 1677 full power partly in cipher.

Also strong but not viewed: Stenbock ↔ Malmberg captivity letters, whose key is in Malmberg's archive (E 4698);
Hedvig Elisabeth Charlotta → Sophia Albertina, cipher plus sympathetic ink, with keys in the next volume; the
French intercepts held in Copenhagen (Feuquières 1675-78, Avaugour 1644, Terlon 1676).

## Key leads (bare keys, no ciphertext)

- Riksarkivet **SE/RA/202 Chifferklaver**, 16 volumes from 1500 to 1894 ("positiva och resolutiva"; 202/1
  includes the 1620-1650 "Kanslichiffer" and an Axel Oxenstierna key; 202/15 is a grille ("Rutchiffer")).
  DECODE has 150+ of these as "Chifferklaver låda II" (record type 2, N/A).
- Riksarkivet: von Nolcken keys for the chancery president's correspondence with ministers, 1730s-40s
  (SE/RA/720928/I/E 4898); Erik von Nolcken 1741 cipher with N. Palmstierna (E 4895); Horn's expedition to
  Prussia 1678-79 keys (SE/RA/754/2/XX/4); S:t Barthélemy key 1819 with clear copy (SE/RA/2411/#/1:1, digitised
  A0060184); Pomeranian war 1757 "Clavis resolutiva" (KrA 0391/0/6); Celsing Constantinople keys (721512);
  Löwenhielm keys and stencils (230015/F 1 A/28); Lovisa Ulrika keys (in K 259); Hedvig Elisabeth Charlotta
  almanacs with keys 1809-17 (720266/02/05/A/III/12); Reuterholm keys (720741/~/28); the Falkenberg key
  (VALA 02038); a key "nyckel till ett schiffer" from the early 19th century (GLA 10131/J/86); the Louis de Geer
  1644 key (ULA 13506 Leufsta I/45); Herslow's WWI Russian code negatives (SE/RA/721594/1).
- Rigsarkivet: TKUA **Chiffernøgler 1539-1693** (Caspar Fuchs to the Netherlands 1539; Cleves, Prussia,
  Saxony, Lüneburg, Hesse 1543-49), TKUA Chiffernøgler 1650-1848, TKUA **Chiffer 1670-1709 (scanned)**,
  Frankrig: Chifre 1541, Christoffer Sehested keys 1650-70, Feltmarskal Arnoldt 1730-55, Wien Chiffres
  1700-1800, Warszawa 1777, Braunschweig congress 1714, Naples 1785, Bernstorff estate keys, East India keys
  (Frederiksnagore, Tranquebar, and earlier keys for Dreyer at St Petersburg 1772, Warsaw 1773 and J.O. Schack
  at Stockholm 1764; scanned), West Indies governor keys 1760-1816 (scanned), Asiatic Company key 1787-94,
  DUA Chifferprotokol 1817-61, DUA "Chifre: chifreringsproblemer" 1777-1843, war ciphers 1807-14, Stockholm
  legation cipher systems 1873-90.
- Uppsala (DECODE): N 724 (R5169-R5197), R 63 (R5198-R5234), E 457 (R5137-R5154), F 474 (R5156-R5168,
  Gustav III's "green portfolio with chiffre-klaver"). Alvin: F 415 no. 171 "Chiffre från Konungens ungdom".

## Crib leads

- Uppsala F 414 nos. 18 and 21 (Alvin 490037, 490051) are Gustav III's own clear originals of despatches sent in
  cipher to Baron Sinclair (Nov-Dec 1768), on the planned regime change. The ciphered copies would be in the
  Riksarkivet Gallica or Sinclair papers.
- Rigsarkivet: Frederik VI's draft of a cipher letter to Prince Christian August of Augustenborg, 1809
  (heid 8617693). The enciphered letter would be in the Augustenborg papers.

## Dead ends and exclusions

- **Erik Brahe's cipher calendars 1592-1607** (Skokloster E 8925, E 8917; DECODE R8889). Sven Tunberg found
  the alphabet more than a century ago, and Peter Andersen has worked on them since. Left out as read.
- Excluded because already deciphered or decrypted:
  - Nolcken Muscovitica ("Dechiffrerade brev" 1774-88).
  - Nolcken Anglica ("Tolkade chifferbrev").
  - Hegardt 1813-14 ("chifferlösningar").
  - Klingspor 1808 ("Översättning av åtskilliga chifrar").
  - Lenet → Condé 1653 in the Sjöholm Bourbon-Clermont collection (deciphered interlinear).
  - Norwegian C-byrån reports ("i chiffer som lösts").
- Excluded as not ciphers: KrA flag drawings ("chiffersida" means the monogram side of a flag); "namnchiffer"
  (royal monograms); Posse ("names that cannot be deciphered", i.e. illegible); the Danish "zifferbog"
  arithmetic books; the post-1950 cipher-telegram diaries.
- DECODE Nordic records already in the repo:
  - R4282, R4284 and R4306 (riksarkivet1628).
  - R4330-R4331 (Bremen).
  - R4332 and R3816 (Heusner).
  - R4333-R4337 (Rusdorff) and R4338-R4341 (E 708), in catalogue 207.
  - R4349 (C 513).
  - R4350 (Görtz).
  - Uppsala E 379 G (R5037-R5136, set aside).
  - R4101 (Stenbock 1713, decrypted).
  - R7688 and R4342 (decrypted).
- Prior art. Kopal and Waldispühl's Swedish papers (Heusner 1637, Chodkiewicz 1575) and Megyesi's DECODE
  project cover only the DECODE items above. Web searches on 26 Oct 2026 found no edition for any kept row.
  Unchecked: the Feuquières letters may be printed in Gallois 1845-46.

## Not reached

- Riksarkivet Diplomatica (Anglica, Gallica, Germanica, Muscovitica, Polonica, Hollandica), the Oxenstiernska
  samlingen and the Kanslikollegium series are described at volume level. NAD notes almost never say "chiffer",
  so most ciphered envoy despatches cannot be found by text search. They need browsing digitised volumes
  (bildvisning) series by series.
- Rigsarkivet TKUA envoy reports (gesandtskabsrelationer) are likewise not annotated for cipher. Most of the
  intercept series are not scanned and need reading-room orders.
- Alvin is behind an Anubis proof-of-work wall. Five searches were run in the built-in browser; scripted
  harvesting was not attempted.
- Riksarkivet's "Brevsamlingar och korrespondens" letter database is not available through the API.
- The Danish Royal Library (KB) manuscripts and Krigsarkivet item lists beyond the NAD notes were not searched.
