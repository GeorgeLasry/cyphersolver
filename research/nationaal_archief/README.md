# Nationaal Archief sweep (first pass, 23 Oct 2026)

A title search of every Nationaal Archief (The Hague) inventory for cipher words, cross-checked against the
279 DECODE records held in Dutch archives. This is a candidate list. No target has been opened from it yet.

## Method

- **API.** `https://zvt.nationaalarchief.nl/api/search/eads?q=` returns archive-level hits.
  `.../search/eads/<archive>?q=` returns item-level hits. `.../api/eads/<archive>/clevels/<unitid>` gives
  availability and the scan list, each scan with a IIIF `info.json` on `service.archief.nl/iip`. The site's own
  search runs on JavaScript, which is how these endpoints were found.
- **Terms** (`harvest.py`): cijfer, gecijferd, ontcijferd/-ing(en), dechiffrement, chiffre(s), cijferschrift,
  geheimschrift, cijfersleutel(s), cifra, nomenclator, plus "secrete brieven", "geheime brieven" and "secreta".
  The last three are tier B, because most secret registers are in clear text. "cijfers" alone returned only
  bank statistics and those rows were dropped.
- **Enrichment** (`enrich.py`) adds the inventory number, availability and scan count. Matching against DECODE uses
  `decode_index.json` (archive + inventory number, built from `../catalogue_harvest/decode/list.json`).
- **Outputs.** `hits.jsonl` (1,611 raw hits), `enriched.json` (1,469 rows). Tier A has 125 items dated before
  1850, of which 37 are scanned and 2 are already on DECODE.

**Limit.** The search matches inventory titles only. Envoy letters described just as "Brieven van X" never mention
cipher in their title, so the real number of cipher items is much larger. Most Staten-Generaal items below are
`PHYSICAL` (not scanned).

## Best leads

| # | Archive / inv. | Date | What | Scans | Note |
|---|---|---|---|---|---|
| 1 | 1.05.01.01 (Oude WIC) inv. 62 | 1646 | Statement by Abraham de Pina Forao giving **the key to the cipher and secret writing** of members of the Alto Segredo Concilio (Dutch Brazil) | 904 (whole volume) | Key plus the volume it sits in. Look for the ciphered letters it unlocks. Top pick |
| 2 | 3.20.66.01 (De Witt-Beijerman) inv. 4 | 1660, 1672 | Johan to Cornelis de Witt letters, with a "solution of part of the cipher, probably from the previous letter" | 0 | Contemporary partial decipherment, so this is a crib. Check Fruin's *Brieven van De Witt* in print |
| 3 | 1.01.50 (Stadhouderlijke Secretarie) inv. 237, 174 | 1791, 1794 | Intercepted letters of French diplomats in The Hague and of Prussian diplomats, "mostly deciphered" | 0 | Dutch black-chamber output. The originals are likely in Paris AE / Berlin GStA |
| 4 | 1.10.110 (other envoys) inv. 2 | 1619 | "Cijfers": envoy cipher keys | 0 | Keys of 1619, around the date of our Haga 1620 key |
| 5 | 3.01.26 (Van de Spiegel) inv. 676 | 1792 | "keys to cipher script" among copied letters | 0 | DECODE already has 14 Van de Spiegel records (inv. 190, 212). Check overlap |
| 6 | 2.21.045 (Croiset) section A | 1789-1810 | Papers of the Secretary of the Cipher of the States General | 0 | Croiset's 1765 key is the one that read De Swart 1782. This is the cipher office's own archive. Key lead for the open Dedem/Roell/Spaen codes |
| 7 | 1.01.02 inv. 12586.29-.94 | 1652-72 | Kaiser (1652-53), the 1656 Copenhagen embassy (32 letters), Slingelandt 1660, Van Wijngaerden 1671-72, all "partly in cipher" | 0 | Biggest single family. Needs ordering scans or an on-demand scan |
| 8 | 1.01.02 inv. 12589.148, .165 | 1672, 1676 | Boreel in London **with duplicates "without cipher"** (5 letters); Van Beuningen 1676 "mostly in cipher" with enclosures | 0 | The cipher/clear duplicate pairs are built-in cribs |
| 9 | 1.01.02 inv. 12585.67-.75 | 1674-78 | Schaep and Rumpf in Stockholm, partly in cipher | 0 | Swedish side may be in Riksarkivet |
| 10 | 1.01.02 inv. 12588.120-.138 | 1686-91 | Battier (Brussels, Madrid) incl. one letter **with translaat**; Schonenbergh 1691 | 0 | Sibling of our `battier1686` target |
| 11 | 1.01.02 inv. 12587.203 | 1686 | Wassenaar Starrenburg, Paris, partly in cipher | 0 | |
| 12 | 1.01.02 inv. 12579.58, 12579.98A | 1654, 1672 | Johan Maurits (Kleve) with a cipher enclosure; field deputies at Maastricht 1672 | 0 | |
| 13 | 3.01.14 (Oldenbarnevelt) inv. 1490, 1769, 2442, 3429 | 1594-1605 | Matched items, scanned (3-21 images each) | 3-21 | Cheap to check. Oldest Dutch leads in the list |
| 14 | 2.05.47 inv. 217 | 1826 | Translations of secret letters sent in cipher to Foreign Affairs | 0 | Clear text for a lost cipher series |
| 15 | 4.VEL inv. 2007B | 1781 | Map sheet: "copy, cipher script translated" | 1 | One image. Quick look |
| 16 | 1.04.02 (VOC), ~28 volumes | 1681-1788 | Volumes of incoming letters under a series heading that matches "cijfer" | 180-1946 each | Find which series heading matched (probably secret letters in cipher) before reading 1,000-page volumes |

Already on DECODE: 1.02.13 inv. 226/228 (Russia legation, R1033/R1035), which covers 2 of the tier-A items.

## Next steps

1. Open lead 1 (WIC inv. 62): find the Pina folios and the ciphered letters in the same volume, through IIIF.
2. Check leads 13 and 15 (scanned and small).
3. Before working any 1.01.02 envoy letter, look for it in print (Delpher, RGP at resources.huygens.knaw.nl,
   Aitzema), following the check-print-first rule.
4. Second pass: walk the 1.01.02 "secrete brieven" and liassen series (12579-12589) item by item instead of by
   title words, and repeat the sweep for the KHA (not in this search) and the regional archives through
   archieven.nl.
