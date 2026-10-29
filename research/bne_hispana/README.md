# BNE / Hispana sweep (28 Oct 2026)

Search of the Spanish digital-library portals for manuscripts described as ciphered. 13 candidates written to
`candidates.json` (none on DECODE, none in the repo per `known.py`). All scored from catalogue descriptions; nothing viewed.

## What could and could not be reached

| Portal | Result |
|---|---|
| BDH (bdh.bne.es, bdh-rd.bne.es, now bnedigital.bne.es) | **Blocked.** 403 to scripts (WAF page); the built-in browser got a Cloudflare "Just a moment" challenge. Not bypassed. |
| Hispana (hispana.mcu.es, OAI-PMH, lod) | **Blocked.** HTTP 429 to every request from this IP, script and browser alike, also on bvpb.mcu.es. |
| Real Academia de la Historia digital library | Anubis bot check ("Making sure you're not a bot"). Reached only through Europeana records. |
| Biblioteca Digital de Castilla y León | Search form loads (200) but the results endpoint timed out; not pursued. |
| **Europeana Record API** (`api2demo`) | Works, and carries the BNE, RAH, Catalonica, Galiciana, PARES (Archivo Histórico de la Nobleza) and BVPB/Madrid records that Hispana aggregates (`hispana_mcu_es_lod` ids). This was the working route. |

## Method

- `eu.py` / `terms.py`: cursor-paged Europeana queries with `qf=DATA_PROVIDER:"National Library of Spain"` and
  `qf=COUNTRY:spain` for 30 Spanish, Catalan and Latin cipher terms (cifrada, cifrado, cifra, "parcialmente cifrada",
  "en cifra", "con cifra", descifrado, contracifra, criptografia, xifrat, nomenclator, clave AND carta, jeroglifico ...).
  2,406 distinct records; 192 survived a regex that drops music ("cifra de arpa", guitar), photographs, theses, museum objects.
- `allmss.py`: the key step. `qf=proxy_dc_type:Manuscritos` on the BNE gives **all 21,795 BNE manuscript records**
  (the whole Europeana-visible BDH manuscript set). Every title and description was grepped for cifr-, clave,
  contracifra, criptogr-, jerogl-, abecedario, nomenclat-, enigm-, code. 95 hits, of which only 17 are cipher letters
  or cipher volumes (`bne_mss_cipherish.json`); the rest are conclave papers, riddles, hieroglyph poems, laws ("código").
  So BNE manuscript records that name a cipher are exhausted: the list below is complete for what the catalogue says.
- Dedup with `research/archive_sweep_2026-10/known.py` on bdh ids and names. The five Europeana-sweep ids
  (bdh0000172729, 172763, 173169, 186643, 172697) and 186675 (Lachaulx, repo `poupet1522`) were kept out.

## Candidates (13)

BNE (all Gayangos or Osuna manuscripts; the catalogue gives only the note, no folio counts):
Sessa 1524-29 (bdh0000172732, importance 4), Hurtado de Mendoza 1548-51 (172694, 4), Juan Manuel 1496-1522 (186690, 4,
Tomokiyo covered the 1521-22 part), Carpi 1548-50 (172678), Mary of Hungary 1544-48 (173419), Mirabel→Gondomar 1621-24
(141369), Olivares→Alba (042230), Leyva 1512-27 (186678, class A), Abbot of Nájera 1522 with contracifra (186680, class A),
Dormer vol. VI 1679-97 (064262). RAH: Chacón→Morillo 1818 (id 5894), Isabel II / Xiquena 1868-69 (ids 14495, 15711).
Barcelona UB: Receptari xifrat 1687.

## Best leads, ranked

1. **Duke of Sessa, Rome, 1524-29** (bdh0000172732): sibling of the repo's sessa1523/sessa1524; the existing key may read it.
2. **Abbot of Nájera 1522** (186680) and **Leyva** (186678): decipherment or key copy bound in, so a crib exists.
3. **Juan Manuel 1496-1522** (186690): any ciphered letter before 1500 would matter for the oldest-cipher search.
4. **Hurtado de Mendoza 1548-51** (172694) and **Carpi 1548-50** (172678): named, dated, Granvelle papers.
5. Mirabel→Gondomar 1621-24 (141369).

## Key leads and excluded (not candidates)

- **bdh0000037730 "Cifre de diversi Prencipi"** (Biblioteca Real 12-2): a book of princes' ciphers, a key collection, no ciphertext. Worth viewing as a key source for 16th-17th-century Italian/Spanish ciphers.
- **bdh0000077600 "Cifra, contracifra, antigua y moderna"** (Tamayo de Vargas, 1612): a treatise on cipher and shorthand, not a ciphertext.
- **bdh0000172704 Cardinal of Jaén → Granvelle 1551-54**: the last two letters have "texto descifrado al margen", so read at the time; useful as a crib for the Granvelle family. Neighbour of the Sigüenza and Gonzaga items already catalogued.
- bdh0000172697 (Gonzaga, "acompaña texto descifrado"), 186675 (Lachaulx): already handled.
- RAH Morillo 1817-20 (Enrile 2242, Eguía 1306, Herrera 5186): printed by Rodríguez Villa (RAH note says so); Alós 1487 not cipher.
- Printed items: Felipe IV "Letra de confianza escrita en cifra", Bonsoms collection (a pamphlet with signatures A-C4); Granvelle printed books; De furtivis literarum notis (Porta) copies; guitar/harp "cifra" tablature.
- Galician Civil War telegrams (1937, Galiciana): each carries a transcription ("corre unida transcrición").
- PARES Archivo Histórico de la Nobleza (Cifuentes, Silva family, ids 4021441-4021452): fonds-level boilerplate "correspondencia, en muchos casos cifrada"; not item-level cipher.
- Biblioteca Virtual de Madrid, Disertación dialogística 1777: a poem signed with a riddle "cifra", not a cipher text.

## Neighbouring volumes of the Europeana leads

The BNE records for the Gayangos Granvelle series (Mss/7913, 7919 ...) are single-letter or small-volume entries. Only those whose
catalogue note says "cifrada" are findable from metadata; the 70+ other Granvelle-addressed BNE records (e.g.
bdh0000198447 Alba 1548, 194097 Sarriá 1554, 198446 Vaca de Castro 1542, 199648 Chapuys correspondence 1529-45) carry no cipher note and are
not claimed. A visual check on BDH could still find unflagged cipher passages in them.

## Not reached / blockers

- BDH full-text and the "Parcialmente cifrada" physical-description field search, and Hispana OAI/search: blocked (see above). The Europeana metadata is a
  mirror of the BDH catalogue, which is why the 21,795-record enumeration is complete for BNE manuscripts, but it misses cipher mentions that exist only in
  BDH fields not exported to Europeana (note fields beyond the first, OCR).
- Archivo Histórico Nacional / Archivo de la Corona de Aragón finding aids: PARES via Europeana has only a few fonds-level records; PARES itself was not queried (covered by `research/pares_ags/`).
- Biblioteca de Catalunya, BVPB, BDCyL: only what Europeana exposed; BDCyL native search timed out.
- Prior-art web search was thin (one query); cryptiana pages on the Granvelle ciphers (Pich-Ponce 2023 on Granvelle-Renard 1553) and Tomokiyo's May 2026 "yet more ciphers from Emperor Charles" were not read and should be checked before work on any 1540s-50s Granvelle item.
- Retry BDH/Hispana from another network or later (429 is probably a rate block).

## Files

`eu.py`, `terms.py`, `allmss.py`, `leads.py`, `jcyl.py` (unused, timed out), `make_candidates.py` (writes `candidates.json`), `bne_mss_cipherish.json`
(the 95 keyword hits among all BNE manuscripts), `filtered.json`, `review.txt`, `terms.log`, `raw/` (lead record details).
