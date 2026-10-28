# NARA bulk sweep, slice K: the export's collections prefix (27-28 Oct 2026)

A file-by-file check of the AWS export against the scan logs found that every record-group file under
`descriptions/record-groups/` had been scanned (151,122 files in 555 groups) except `coll_Wattenberg` (3 files), and that
the second prefix, `descriptions/collections/`, had never been scanned: 5,192 donated and presidential-library collections,
215,839 files, about 28 GB. `research/nara_reels/bulk_coll.py` ran the bulk_all detectors over all of it (215,842 files,
0 failures) into `out/collections_all.jsonl`: 29,813 hits in 318 collections (frame 18,530, caps 9,830, word 1,201,
phrase 173, letters 47, desc 32). The files come from the AWS Open Data bucket, so no request went to catalog.archives.gov
except one record fetch (naId 519768010, through `reels.py fetch`).

Review: `review_j.py` over the full hit file (`review_coll.txt`): every desc, every phrase, all 47 five-letter-group items,
the 200 strongest word hits, and the top 40 frame and caps items.

## Result: no row (`candidates.json` is empty)

- **Closest lead, read at the time:** FDR Library, PSF Safe Files, Marshall, "Telegram, George Marshall", 19 June 1942
  (naId 519768010). 34 five-letter artificial code groups ("GUMER LUTOG PUFUP ... DOPOL PUDEN") relayed to the President
  via McIntyre, with the meaning typed below: Churchill ("your guest") pessimistic about BOLERO, interested in an August
  GYMNAST and a Norway operation. A code/plaintext pair, not an unsolved text.
- **desc (32):** FDR-Churchill Map Room cable traffic (decoded copies), Truman Cryptographic Security Board files, a 1945 "coded
  telegram" item (incoming, decoded), the coded Japanese surrender message 1945 (MHDC 740, own traffic), ARC 227 transposition
  pamphlet, Clinton/Bush cryptography-policy files, surnames Cypher/Cyphers, colour-coded maps.
- **phrase (173):** Western Union form boilerplate ("errors in cipher or obscure telegrams") in Red Cross nurse files (coll_ANRC),
  SHAEF message forms "sent in cypher if liable to be intercepted", Haskell's 1921 Russia reports "to be sent in cipher" (clear
  drafts), British inward telegrams "received in cypher" (decoded), the MOLINK hotline manual, and "key missing" in policy prose.
- **letters (47) and caps:** Kodak film edge-print in White House photo contact sheets (GB-WHPO), statistical tables, the Universal
  Newsreels subject card catalogue; only the Marshall telegram above is real code.
- **word (1,201):** "decipher" for handwriting, Map Room "to be deciphered by officer" routing notes, Keynes lecture notes, the
  Garrison JFK files (Nagell letters "more or less in code", deciphered by the writer), news clippings.
- **frame (18,530):** Clinton/Nixon/Truman calendars, polls, statistics, budget tables, Potsdam briefing tables, firing tables,
  watch-computation journals.

With this slice every file in the NARA catalogue export (record groups and collections, 367,000 files) has been scanned by the
detectors and every group with hits reviewed (slices A-K).
