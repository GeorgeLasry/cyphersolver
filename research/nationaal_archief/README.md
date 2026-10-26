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
| 1 | 1.05.01.01 (Oude WIC) inv. 62 | 1646 | Statement by Abraham de Pina Forao giving **the key to the cipher and secret writing** of members of the Alto Segredo Concilio (Dutch Brazil) | 904 (whole volume) | **Already published:** Dinnissen & Araújo, HistoCrypt 2023 ("A 'Mirror for All Traitors'", ecp.ep.liu.se/index.php/histocrypt/article/view/693): Pina's report, the nomenclator and all four ciphertexts read. Same authors did the 1649 Teles da Silva ciphertexts (article 392). Closed, nothing to add |
| 2 | 3.20.66.01 (De Witt-Beijerman) inv. 4 | 1660, 1672 | Johan to Cornelis de Witt letters, with a "solution of part of the cipher, probably from the previous letter" | 0 | **Checked 23 Oct, closed.** The cipher sheet is inv. 4 item 183, after item 182 = Johan to Cornelis (Brussels), 29 Mar 1672. EMLO lists that letter with "1 printed edition" (Fruin/Japikse) and Johan's own minute in clear, 3.01.17 inv. 26 fol. 14 (minutes to Cornelis Jan-Mar 1672, 59 scans online). The plain text is known; the ciphered original is not scanned. Nothing to read. Other De Witt letters "partly in cipher" can be checked the same way, since the 3.01.17 minute books (inv. 26-27 etc.) are scanned |
| 3 | 1.01.50 (Stadhouderlijke Secretarie) inv. 237, 174 | 1791, 1794 | Intercepted letters of French diplomats in The Hague and of Prussian diplomats, "mostly deciphered" | 0 | Dutch black-chamber output. The originals are likely in Paris AE / Berlin GStA |
| 4 | 1.10.110 (other envoys) inv. 2 | 1619 | "Cijfers": envoy cipher keys | 0 | Keys of 1619, around the date of our Haga 1620 key |
| 5 | 3.01.26 (Van de Spiegel) inv. 676 | 1792 | "keys to cipher script" among copied letters | 0 | DECODE already has 14 Van de Spiegel records (inv. 190, 212). Check overlap |
| 6 | 2.21.045 (Croiset) section A | 1789-1810 | Papers of the Secretary of the Cipher of the States General | 0 | Croiset's 1765 key is the one that read De Swart 1782. This is the cipher office's own archive. Key lead for the open Dedem/Roell/Spaen codes. **Checked 23 Oct:** A.7.b inv. 18 (envoy code correspondence + code tables), 21 (cipher codes), 22 (Röell letter), all physical only; recorded in the three targets' NOTES. Needs scan-on-demand |
| 7 | 1.01.02 inv. 12586.29-.94 | 1652-72 | Kaiser (1652-53), the 1656 Copenhagen embassy (32 letters), Slingelandt 1660, Van Wijngaerden 1671-72, all "partly in cipher" | 0 | Biggest single family. Needs ordering scans or an on-demand scan |
| 8 | 1.01.02 inv. 12589.148, .165 | 1672, 1676 | Boreel in London **with duplicates "without cipher"** (5 letters); Van Beuningen 1676 "mostly in cipher" with enclosures | 0 | The cipher/clear duplicate pairs are built-in cribs |
| 9 | 1.01.02 inv. 12585.67-.75 | 1674-78 | Schaep and Rumpf in Stockholm, partly in cipher | 0 | Swedish side may be in Riksarkivet |
| 10 | 1.01.02 inv. 12588.120-.138 | 1686-91 | Battier (Brussels, Madrid) incl. one letter **with translaat**; Schonenbergh 1691 | 0 | Sibling of our `battier1686` target |
| 11 | 1.01.02 inv. 12587.203 | 1686 | Wassenaar Starrenburg, Paris, partly in cipher | 0 | |
| 12 | 1.01.02 inv. 12579.58, 12579.98A | 1654, 1672 | Johan Maurits (Kleve) with a cipher enclosure; field deputies at Maastricht 1672 | 0 | |
| 13 | 3.01.14 (Oldenbarnevelt) inv. 1490, 1769, 2442, 3429 | 1594-1605 | Matched items, scanned (3-21 images each) | 3-21 | **Checked 23 Oct.** **inv. 2442 is a real target**: Spanish letter, Juan Gara de Senisteros to Juan de la Peña, Alcalá 23 Dec 1605 (early-17th-c. copy, 11 scans): long passages in a letter-and-figure substitution, no decipherment visible. inv. 1490 (Jülich to Oldenbarnevelt 1605, duplicate) is Dutch clear text with 3-digit name/number codes (e.g. 671, 612, 241). inv. 1769 is a clear French minute with underlined words. inv. 3429 is French copies, apparently clear |
| 14 | 2.05.47 inv. 217 | 1826 | Translations of secret letters sent in cipher to Foreign Affairs | 0 | Clear text for a lost cipher series |
| 15 | 4.VEL inv. 2007B | 1781 | Map sheet: "copy, cipher script translated" | 1 | **Checked 23 Oct: not a cipher.** A coloured 1781 Surinam river defence plan; "cijferschrift" is its numbered legend |
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

# Second pass (23 Oct 2026): Staten-Generaal item by item, KHA, archieven.nl

## 1.01.02 Staten-Generaal, Secrete kas envoy letters (section VI.C)

- `dump_ead.py` walks `.../api/eads/1.01.02/clevels?page=N`. Two full passes return the same **18,807** of the
  28,573 catalogued items: the paged listing leaves part of the tree out, including most of the envoy letters. The
  gap was filled with item-level title searches inside the archive (`fill_search.py`: every envoy posting, "brief",
  "gezant", "cijfer" …), which returned **7,212** individual letters in VI.C (`vic_letters.json`).
- Scan status was checked per volume (`vic_inv_status.json`): of **297** volumes holding these letters, **4** are
  digitised (a charter, a ratification, a label, a Bank of England receipt). **The envoy correspondence of the
  Secrete kas is not online.**
- 63 letters are described as (partly) in cipher, in 19 volumes, all `PHYSICAL`. This is the scan-on-demand list:

| Volume | Year | Letters in cipher | Sender |
|---|---|---|---|
| 12586.49 | 1656 | 29 | Van Beuningen embassy, Copenhagen |
| 12589.148 | 1672 | 6 | Johan Boreel, London (with clear duplicates) |
| 12586.41, 12586.29 | 1652-53 | 6 | Nanningh Kaiser, Copenhagen |
| 12585.74, 12585.75 | 1677-78 | 6 | Rumpf, Stockholm |
| 12588.120-125, 12588.138 | 1686-91 | 6 | Battier (Brussels, Madrid), Schonenbergh |
| 12589.165 | 1676 | 2 | Van Beuningen, Westminster |
| 12586.93-94 | 1671-72 | 3 | Van Wijngaerden, Copenhagen |
| 12579.58, 12579.98A | 1654, 1672 | 2 | Johan Maurits; field deputies |
| 12587.144, 12587.203 | 1657, 1686 | 2 | Paris embassy |
| 12586.69 | 1660 | 1 | Slingelandt embassy, Copenhagen |

  Only 12587.144 (1657) is new against the first pass. Most envoy letters are described without any word for
  cipher, so the true number is larger; the senders with the longest runs (L'Hermitage 423, Willem Boreel 330,
  Goes 315, Van der Meer 306, Van Beuningen 211, Moeringh 210, Hamel Bruynincx 156, Van Citters 135, Godard
  Adriaan van Reede 129) are the series to sample first once anything is scanned.

## Koninklijk Huisarchief

The KHA catalogue is not in the Nationaal Archief search. It is served by the Koninklijke Verzamelingen CMS:
`https://cms.koninklijkeverzamelingen.nl/api/archive/?format=json&query=<term>&limit=50&start=<n>` (42,089
records; `harvest_kha.py`, `kha_hits.jsonl`, 474 hits, ~75 before 1850 on cipher words). Scans are viewed on
`koninklijkeverzamelingen.nl/archief/...` (each record's `url`). DECODE already holds the Willem V intercepts
under the old inventory numbers (A31 inv. 192 d'Affry, 196 Hellen, 198 Michell/Frederick II, 201 Kauderbach,
205 Van Reede, 337, 339 keys), A32 inv. 192 (Wolff 1801) and A16 XIII-1 (d'Avaux 1684).

Leads not on DECODE, scanned first:

| # | KHA item | Date | What | Scans |
|---|---|---|---|---|
| K1 | G016-A0204 | 28 Aug 1574 | Philip II to Don Juan of Austria, **letter in cipher** (Collectie Handschriften, 2e serie) | 6 |
| K2 | A23-311 | 1618-1627 | Ernst Casimir of Nassau-Dietz: **keys for cipher used with various correspondents** | 97 |
| K3 | G016-A0572 | 17 Dec 1640 | Philip IV to the marquis of Velleda, in cipher | 7 | **Checked 25 Oct:** signed original (Yo el Rey, countersigned Andrés de Rozas) to Velada, ambassador extraordinary in England, recalling him to Flanders; Malvezzi to follow, Alonso de Cárdenas to keep the embassy. Clear Spanish except two short cipher runs (about 20 and 25 groups: figures 4-171, a few signs and plain-looking syllables), both ending in the same phrase "121 so ta na te 6 Q X", so a repeated place or subject. No interlinear decipherment, nothing on the dorse (address only), no print found. Too short to break without the 1640 Velada/Malvezzi cifra (Simancas, Estado, Inglaterra). Not opened as a target. Scans: KHA image ids 96169-96174; working crops in k3/ (git-ignored). |
| K4 | A32-603, A32-599-604 | 1783-84 | Schöning's secret mission to Berlin: letters with **their decipherment by Van der Hoop**, De Larrey's file with key | 212, 442 |
| K5 | A32-630 | 1795-97 | "Anciens déchiffrements sur les premières années de notre séjour en Angleterre" (Wilhelmina) | 387 | **Surveyed 25 Oct (contact sheets of all 387 scans, k5/ids.txt):** the Hereditary Prince's letters from Berlin to his mother, Oct 1795 to spring 1797, in the same Euler word-list system as target hereditary1796 (groups `N,p,q`, underlined whole entries, `k)N` / `N(k` truncations, e.g. "52,1,2, 128; 147, 48, 1)121, 148,2,3,5 ..." on scan 177508). Three kinds of page: (a) originals with cipher runs between clear French, many with interlinear decipherments in pencil or ink (e.g. 177520-177526, 177541-177550, 177554-177557, 177600-177641); (b) pages of solid numeric cipher (177508, 177537-177540, 177650-177651, 177745, 177751, 177757, 177763-177790); (c) Wilhelmina's clear write-ups headed "Chiffre de Guillaume du ..." (20 and 29 Jan, 19 Feb, 7 Mar, 10 and 16 July, 20 Aug 1796; Mar-Apr 1797; e.g. 177552, 177560, 177566, 177576, 177581, 177650, 177656, 177660, 177677, 177683, 177687, 177691, 177693, 177748, 177760, 177776, 177782, 177788, 179444). Read at the time; value here: dozens of cipher/plaintext pairs to rebuild the full Euler list (hereditary1796 has about 250 entries from one pair) and so read R2236 and other unread A31/A32/A35 letters in this system. Next: open as a target, pair each solid-cipher page with its "Chiffre de Guillaume" copy, extend the list. |
| K6 | A35-488-1 | 19 Jan 1795 | **Key** of the Orange family cipher devised by H.W. van Aylva | 2 | **Checked 25 Oct:** not a cipher alphabet but a two-page jargon list (8 columns x ~28 rows): real names in dark ink (Pitt, Bentinck, Nagell, Fagel, Haugwitz, towns, "Rassemblement", "Regents actuels 1802") with pale-ink cover words (Jean, Mimi, La Cousine...); a note says underlined words carry the opposite sense. Additions to 1802+, so used into the 1800s. Useful as a gloss list for Orange-family letters written in cover names; no number or sign key, so it does not bear on R1892/R2242 open signs. Scans in k6/ (git-ignored). |
| K7 | A32-571 | [1793] | Wilhelmina's notes on the hereditary prince's cipher letters, March-July 1793 | 16 | **Checked 25 Oct:** no cipher in the folder. Two pieces, both in clear French in Wilhelmina's hand: (1) "Projet de réponse aux chiffres de Guillaume du 10 & 14 Mars 1793", a draft answer of 28 March (on the eventual Prussia-France treaty, Elgin, Haugwitz); (2) "Réflexions sur le contenu des chiffres de Guillaume du 14, 15, 22 & 25 Juillet 179[?]", whose last digit is unclear but whose content (Repelaer and Ragay, Fritz banished by sentence, "le rassemblement") puts it in 1796-98, not 1793. Use: clear summaries of lost or unread Hereditary Prince cipher letters, so a crib source if those letters turn up (cf. targets hereditary1796, r1892, r2242). KHA image ids about 174057-174069; working copies in k7/ (git-ignored). |
| K8 | A32-527, -536, -537-541, -542-549, -354, -560, -620 | 1782-1819 | Wilhelmina's correspondence in cipher (Thulemeier, Nagell, Van de Spiegel, A.W. van Reede, Stamford, Hogguer, Van der Hoop) | 71-1,941 each | **Surveyed 25 Oct** (contact sheets of every scanned item, `k89/`; 321 flags in `k89/flags_a32.tsv`): best pairs are (1) A32-544 Van Reede, Berlin 1788: 4-digit despatches beside "Dechiffrement de la lettre de Mr de Reede" (e.g. 170221/170224, 170276-77/170273) and clear "Chiffre No. .. de Mr de Reede" copies (scans 301-337, ids 170451-170487); (2) A32-527 Thulemeier 1787: each number letter followed by "Dechiffre de Mr de Thulemeier du <date>" (157868-71 ... 157965-68); (3) A32-542 Van Reede 1786 with decipherments (170014/170017); (4) A32-536 Nagell, London 1789: digits mixed with symbols, letters written above (163380-82, 178888-94), clear copies 163441, 163482; (5) A32-545-547 Van Reede 1789-92 interlined, plus undeciphered solid 4-digit pages 171282 (Jan 1792), 171359, 171376, 171405, 179084, and A32-548 171596 (1793), 171534/171548/171568 (1795): **lead for target vanreede1787's unread R1893 (24 Mar 1793)**; (6) A32-537 Van de Spiegel 1787 Dutch code glossed (168844, 168849); (7) A32-354 Stamford clear "Chiffre" copies and one interlined letter (126321). Flags judged from thumbnails, mostly not checked at full size. |
| K9 | A35-172-197, A35-511-515, A35-524-532, A35-1448-1458, A35-1232 | 1788-1819 | Letters to the future Willem I in cipher with decipherments (his mother, Bentinck, d'Yvoy, Van Reede) | 165-1,029 | **Surveyed 25 Oct** (`k89/flags_a35.tsv`, 48 flags; only A35-178, -513, -528, -531, -1232, -1450 to -1453 are scanned): best is A35-1450-1452, d'Yvoy despatches London 1797-99, a Dutch 4-digit code (groups to about 1,400) with Dutch glosses above the numbers (checked 147529: 1341 = Zeeland, "101 1216 723" = "in Hamptoncourt men"; also 146903, 147030, 147531), letters both ways; then A35-1232 Van Reede 1796 (144358 interlined; 144361 "Extrait" in solid numbers). A35-178 (London 1801) has 11 number letters, unchecked. |
| K10 | A16-XIII-1 | 9 Jan 1684 | d'Avaux to Louis XIV in cipher (already DECODE, de Mesmes) | 11 |

Unscanned but notable: A31-903/904 chiffre chiffrant/déchiffrant (c. 1775-80); C02-77 keys of 1759; A31-1191-1193
lists of intercepted and deciphered diplomatic letters (De Larrey 1773, Croiset 1773-91, Lyonnet 1752-78); A22-51
and A22-191-198 Willem Lodewijk's secret writing (1583-1609); A15-XIC-8 Jermyn 1649-50 with key.

K1 and K2 are the best next targets (the K1 letter may be printed in Gachard's *Correspondance de Philippe II*;
check first). K4 and K6 pair ciphertext with decipherment or key on the same scans.

## archieven.nl (regional archives)

archieven.nl's search returns inventories, not items, and only in a browser (results load through an obfuscated
proxy). Inventory-level hits for the cipher words were collected and the early-modern ones kept in
`archievennl_hits.json` (39). Item-level hits inside each inventory are not reachable by URL; each has to be opened
by hand. Most promising: Huis Amerongen (Utrecht, 1001; the Van Reede envoys), Tresoar's descriptions of the Frisian
stadholders' archives (7-02 Willem Lodewijk to 7-14 Willem V) and the Saxon dukes' rule in Friesland (1, 2),
Culemborg (0370), the Gelre counts (0001), Bentinck (0613), Van Lynden van Hoevelaken (1030), and the KZGW
manuscripts in Middelburg (6,097 digitised). Newspapers and modern municipal files dominate the raw hits.
