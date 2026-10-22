# Earlier readings: has this letter been read before?

[日本語](PRIOR_CHECK.md)

This check has two parts.
1. **A search made in order to refute**: a reader (an AI) who had not seen the decipherment work (transcription, key, intermediate readings) received the plaintext, the ciphertext and the record of earlier searches, and looked for any earlier reading (20 Oct 2026; "Search made in order to refute" below).
2. **Our own search**, made earlier the same day by those who made the reading ("Our search" below). It is not independent and only supplements part 1.

Date: 20 Oct 2026 (Japan time); 19 Oct 2026, 15:00–17:59 UTC.

## Verdict
| object | class | evidence |
|---|---|---|
| the plaintext of f. 50 as a whole (the joined reading) | **not found** | no period decipherment in the volume (NoAutopilot: f. 49v, f. 51, f. 52 carry only the address and slips; we have not looked at them). No plaintext of this letter found in print, papers or repositories (table below) |
| some words (conseil, que ledit, descouvert, surtou[t] …) | **already read (partly)** | in NoAutopilot/cipher-lab reading.txt (commit f3dcded, 13 Oct 2026) as strings from Tomokiyo's table, not as connected text ("Status: partial", "Verdict: parked") |
| plaintext exists but no alignment | none | no plaintext of this letter has been found |

Not finding a reading does not prove that none exists. The README does not call this reading the first.

## Search made in order to refute (20 Oct 2026)
| where | result |
|---|---|
| DECODE R2742 (public record page) | "Status: Decrypted", "Inline Plaintext: No", "Available Documents: Key, Paper", by tomokiyo; documents need a login; NoAutopilot logged in and records only the images and Tomokiyo's table (5 Oct 2026) |
| NoAutopilot/cipher-lab baluze103-letellier-marca-1644 | last commit f3dcded (13 Oct 2026 07:56 UTC), Verdict: parked; no later commit |
| GitHub code search "\"Baluze 103\"" (18 hits) | all NoAutopilot files |
| cyphersolver (origin/main 0258b8ab) full text; all 47 issues and PRs (latest #49) | no reading of f. 50 |
| Cryptiana (unsolved 2026-10-13, GL 2026-10-15, ai 2026-10-19, verification 2026-10-15) | only louisxiv0.htm's « undeciphered » |
| Cryptoole API (854 entries) | nothing |
| DECODE catalogue copy (aaymeloglu/unsolved-ciphers, c2436b0, 18 Sep 2026, 10,106 records) | nothing beyond R2742 |
| BravoBravoIX (6 repositories), pangoleen/cipher-readings, el-descifrador/cabinet-noir | no file names with Baluze, Marca, Tellier |
| web search (French): "conseillers de la ville de Barcelone", Marca, La Motte | nothing |
| not searched | Gallica, Google Books, HathiTrust full text (at that time); DECODE documents; Spanish printed works such as Sanabre |

## Our search: searched
| where | how | result |
|---|---|---|
| web search (French, Spanish, English; 5 queries) | the letter's subjects (lodging, opened packets) with Le Tellier, Marca, La Motte, Barcelona, 1644; and the names Torreilles, Sanabre, Aznar | nothing on this letter's content |
| T. Issartel, "Pierre de Marca (1594-1662), l'absolutisme et la frontière" (ddd.uab.cat, 2010) | full text of the PDF | cites the studies of the Le Tellier–Marca correspondence (Dubarat 1901, 1927–28; Torreilles 1901; Sanabre 1956); nothing on f. 50 |
| a HistoCrypt paper found by the search (ecp.ep.liu.se) | PDF | about a Portuguese spy in Dutch Brazil (1646); unrelated |
| GitHub code search | "\"paquets que les Catalans\"", "\"conseillers de la ville de Barcelonne\"", "Marca \"La Motte\" \"Le Tellier\" 1644", "baluze103 letellier marca" | 0, 0, unrelated text data, only NoAutopilot/cipher-lab |
| NoAutopilot/cipher-lab | last commit of the folder and reading.txt | still f3dcded (13 Oct 2026); reading.txt has none of the words paquet, catalan, motte, maison |
| D. Bourdeau, cyphersolver | origin/main 0258b8ab (18 Oct 2026), full-text search; latest issues #45–#49 | nothing |
| Cryptiana | louisxiv0.htm (2025-12-06), unsolved.htm (2026-10-13) | louisxiv0.htm still says « f.50 (undeciphered) » |
| Cryptoole | same-day search (idx.json, 854 entries) | nothing |
| HathiTrust full-text (phrase search, all items) | after a person passed the check in the browser, 12 phrases from the same tab, 4 s apart (the letter's own phrases; general ones such as "ouvre tous les paquets", "preparer un logis", "Le Tellier a Marca"; and a phrase of the f. 189 period decipherment) | the seven phrases specific to f. 50: 0 hits. "conseillers de la ville de Barcelonne" hits Sourdis's correspondence and the 1641 treaty text (Collection de documents inédits, uc1.c2811166, pp. 492, 564 seen): unrelated. General phrases: many unrelated books (titles only). The f. 189 phrase: 0, so the sister letters' plaintext is not in print either, as far as this search goes |

## Our search: not searched or blocked
| where | why |
|---|---|
| Google Books full-text (API) | HTTP 429 on all seven queries; stopped |
| Gallica full-text (SRU) | 403 with curl; a security check page in Chrome, twice (also after a person passed the HathiTrust check); not pressed, stopped |
| DECODE (de-crypt.org) R2742 | login needed; NoAutopilot records "images and Tomokiyo's table only" |
| printed works: Sanabre (1956), Dubarat (1927–28), Torreilles (1901), Chéruel's Mazarin letters | not read in full (NoAutopilot searched Chéruel vol. 1 for "Marca" and found no such letter) |
| Persée, Cairn, Dialnet | not searched separately (only through web search) |

## Re-check (from 19 Oct 2026 19:47 UTC = 20 Oct 04:47 Japan time)
| where | result |
|---|---|
| NoAutopilot/cipher-lab | last commit of the folder still f3dcded (13 Oct 2026); no commit title since 13 Oct (about 2,000 commits) mentions Baluze 103, Marca or Tellier (only other work on Baluze 167 and 169); nothing in the issues |
| cyphersolver | origin/main still 0258b8ab (18 Oct 2026); latest issue #49 (19 Oct 2026); nothing |
| GitHub code search | "\"Baluze 103\"": only NoAutopilot/cipher-lab; "Marca \"La Motte\" Barcelone paquets": one unrelated hit |
| Cryptiana | louisxiv0.htm 2025-12-06, unsolved.htm 2026-10-13, ai.htm 2026-10-19, recent blog posts: nothing |
| Internet Archive full text | the letter's own phrases: 0 hits; "conseillers de la ville de Barcelonne": 8 hits, all the 1641 treaty text; word-combination searches (Le Tellier, Marca, paquets, 1644 …) give catalogues, biographies and editions of Marca's letters (Revue de Gascogne 1910), not this letter's plaintext |
| Catalogue des manuscrits de la Collection Baluze (1921; Internet Archive full text) | for Baluze 103: « Correspondance de Marca avec Le Tellier (4 avril-29 décembre 1644) … dont quelques-unes chiffrées, avec traductions (fol. 50, 171, 189, 200, 230) », which reads as if f. 50 also had a translation. We looked at the leaves around f. 50 (about ff. 47–57, Gallica views 104–124): no translation; f. 51 is blank and the address side (« receue le 3 may, resp. le 4 may »); f. 52 carries two filing slips. The other four letters have their translation on the next leaves (ff. 172, 190, 205, 232). Whether a translation of f. 50 is elsewhere in the volume has not been checked |
| Marca's reply (view 121, « A M. le Tellier, du 4 May 1644 ») | reports his arrival and the handover from La Berchère; nothing on the lodging or the packets |
| Google Books API | daily quota, 429 (4 tries) |
| Gallica full text | still a bot check page |

## The catalogue's "avec traductions" (20 Oct 2026)
The 1921 catalogue of the Baluze collection describes Baluze 103 fol. 41ff. (Le Tellier–Marca letters) as "dont quelques-unes chiffrées, avec traductions (fol. 50, 171, 189, 200, 230)". We looked at all 743 views of the volume (Gallica btv1b9001389d, BnF IIIF, views 1–743). Period decipherments are present for f. 171 (f. 172), f. 189 (f. 190), f. 200 (f. 205–206) and f. 230 (f. 232), each right after its cipher letter. **No decipherment of f. 50 was found anywhere in the volume**, so the reading of f. 50 cannot be checked against a period decipherment. The catalogue's "avec traductions" applies to four of the five letters.
