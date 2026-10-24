# Riksarkivet sweep (first pass, 24 Oct 2026)

A search of the Swedish National Archives catalogue (NAD / Sök i arkiven) for cipher words, cross-checked against
the project ledgers and the DECODE harvest. No new target came out of it: **0 candidates**.

## Method

- **API.** `https://data.riksarkivet.se/api/records?text=<term>&max=100&offset=<n>` returns JSON hits for records,
  dossiers, series and fonds (reference code, date, hierarchy, `onlyDigitisedMaterials`). It returns **403 to the
  default Python user agent**, so send `User-Agent: curl/8.0`. The search also matches each record's descriptive note,
  so many hits have no title (`caption: null`).
- **Detail.** `https://data.riksarkivet.se/archive/<id>.jsonld` gives the note (`skos:note`) and, if the record is
  scanned, `schema:image` → a IIIF manifest `https://lbiiif.riksarkivet.se/arkis!<bildid>/manifest`. Images:
  `https://lbiiif.riksarkivet.se/arkis!<bildid>_<00001>/full/1000,/0/default.jpg`. Viewer:
  `https://sok.riksarkivet.se/bildvisning/<bildid>_<page>`. The plain `/archive/<id>` URL returns 403 with JSON Accept.
  The OAI-PMH EAD route works too: `https://oai-pmh.riksarkivet.se/OAI/?verb=GetRecord&identifier=<refcode>&metadataPrefix=oai_ra_ead`.
- **Terms** (`harvest.py`): chiffer, chiffer*, chiffrerad(e), chifferbrev, chiffernyckel, chiffernycklar,
  dechiffrering, dechiffrerade, dechiffr*, chiffre(s), chiffrer, chifferskrift, cifra, geheimschrift, nomenklator,
  nomenclator, ziffer, cipher, déchiffré. Only chiffer*, chiffernycklar, dechiffr* and the related forms returned anything.
  `details.py` adds the note to every hit before 1950 that is not a flag drawing.
- **Output.** `hits.json`: 326 unique hits, 240 dated before 1950. Of these, about 30 are flag drawings ("chiffersida" =
  the royal monogram side of a regimental colour, Krigsarkivet 0418), and about 150 are 1888-1949 Foreign Ministry
  telegram volumes ("Telegram i chiffer", "Chiffertelegram"). That leaves about 45 early items, below.

## Items checked

| Ref. code | Date | What | Scanned | Result |
|---|---|---|---|---|
| SE/RA/720795/I/01/001 In quarto E 8925, E 8917 | 1592-1607 | Erik Brahe's "chifferkalendarium", diary notes in his own cipher alphabet (manifests R0000801, R0000800) | yes | **Closed: already read.** Sven Tunberg found the key and summarised the diary, Personhistorisk tidskrift 20 (1918-19) 37-65, 23 (1922) 31-38. Readings are cited by Peter Andersen, *Sensus Historiae* 2022 ("Erik Brahé … raconte sa mission à Prague") and Vinilandicus, *Kunstværket* (with the key reproduced) |
| SE/RA/202 (Chifferklaver), vols 1-14, 20-21 | 1500-1894 | Sweden's key collection, positive and resolutive keys; card index by H. Stålhane (1934) in vols 20-21 | no | Keys, not ciphertext. DECODE R4282-R4341 come from this collection (cat. 207). Key source for open targets (Görtz 1717, Rusdorff 1628, R4284) |
| SE/RA/757/36/II/48 | 24 Mar 1631 | Johan Casimir to the King, on finance, "duplett, delvis chiffrerad" | no | Duplicate, possibly clear twin. Not scanned. Lead only |
| SE/RA/25.3/4/II/7/B | 1677 | Charles XI's full powers for the commissioners, Nääs 6 May 1677, Latin, partly in cipher | no | Not scanned. Lead only |
| SE/RA/2404/I A 1/28, I A 2/149 | 1710-14 | Pomeranian government / Gov.-Gen. Meyerfeldt to the King, "åtskilliga chiffrerade" | no | Not scanned. Contemporary decipherments likely in the chancery |
| SE/RA/1411/E/E VI/1 | 1714 | Reports from Hamburg by the ex-governor of Bremen-Verden, partly in cipher | no | Not scanned |
| SE/RA/2102/I/36/438 | 1764-91 | Envoy G.A. Nolcken (London): "Tolkade chifferbrev" (deciphered) | no | Deciphered at the time |
| SE/RA/2113/…/73/408-443 | 1774-88 | J.F. von Nolcken (Petersburg): incoming letters, "Dechiffrerade brev" | no | Deciphered at the time |
| SE/RA/720266/02/04/B/B 1/12, B 1/14 | 1773-1800 | Hedvig Elisabeth Charlotta to Sophia Albertina: sympathetic ink, "chiffertext förekommer"; B 1/14 with keys | B 1/14 flagged scanned, but no manifest on the record | Not a candidate: correspondence used in print (Bonde edition of the diary; Hellsing 2015); keys present; no ciphertext checked |
| SE/RA/710003/02/008/b/K 259, SE/RA/720266/02/05/A/III/12 | 1700s; 1809-17 | Lovisa Ulrika papers with keys (A0073297, 223 images); Hedvig Elisabeth Charlotta almanacs with keys | yes | Keys, not ciphertext |
| SE/RA/720791/01/IV/06/3 | 1653 | Bourbon-Clermont autographs: Pierre Lenet to Condé, 13 Mar 1653, "code déchiffré dans l'interligne" | yes | Deciphered at the time (interlinear). Ormée/Bordeaux family, compare our bordeaux1653 target |
| SE/RA/2109/I/12/106; SE/RA/720928/I/E 4895 (24); SE/RA/721512/II and IV (Celsing); SE/KrA/0391/0/6; SE/RA/720725 E 4698 (Stenbock-Malmberg); SE/RA/2411 1:1 (St Barthélemy 1819); SE/RA/230/230019.1 D/170 (London 1824, 1848); SE/RA/230/230015 F 1 A/28 | 1659-1876 | Key sheets filed with envoy papers | mostly no | Keys only |
| SE/RA/221/2211.01/E/E 1/9 | 1813-14 | Copies and "chifferlösningar" of Hegardt's despatches | no | Deciphered at the time |
| SE/KrA/0035:0715/1 | 1942-45 | Stig Roth's diary in cipher | no | Roth made a clear fair copy after the armistice (per the catalogue). Not a candidate |
| Foreign Ministry C 3 A/B "Telegram i chiffer"; legation "Chiffertelegram" | 1888-1949 | Telegram volumes | no | Codebook telegrams, unscanned; out of scope for this pass |

## Best leads (all physical only)

1. Johan Casimir 1631 (757/36/II/48) and the Nääs 1677 full powers (25.3/4/II/7/B): small, partly ciphered, early.
   Would need scans on demand. Keys are probably in Chifferklaver vol. 1 or 3.
2. Meyerfeldt 1712-14 (2404/I A 2/149): Pomeranian reports in cipher, Great Northern War.
3. The Chifferklaver card index (202/20-21) as a key finder for the open Riksarkivet targets.

## Closed leads

- Erik Brahe's cipher calendars, 1592-1607: key found by Tunberg 1918, now in use (Andersen 2022).
- Flag "chiffersida" drawings: royal monograms, not ciphers.
- Nolcken, Hegardt, Lenet: deciphered at the time.

## Limits

- The search matches titles and notes only. Envoy letters described just as "Brev" never mention cipher.
- Almost nothing that matched is scanned. Scanned material sits mainly in the personal collections (Skokloster, royal
  collections). Arkiv Digital's private image service was not searched.
- DECODE (`research/catalogue_harvest/decode/batch_6.json`) has 14 Riksarkivet records, all from the
  Chifferklaver/Oxenstierna/Bremen group (cat. 207), and one National Library of Sweden record (R4350, Görtz).
  None of the hits above is on DECODE.
