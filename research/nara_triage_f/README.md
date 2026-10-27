# NARA bulk-scan triage, slice F: capital-letter (Vigenère-likeness) pass, RG 109 / 45 / 107 (27 Oct 2026)

Brief: `research/nara_reels/TRIAGE_BRIEF.md` and `research/archive_sweep_2026-10/BRIEF.md`. Input:
`research/nara_reels/out/rg_109_caps.jsonl` (388 lines), `rg_45_caps.jsonl` (43), `rg_107_caps.jsonl` (4): frames with
>= 15 all-capital tokens, a run of >= 6, >= 80 capital letters and letter IC < 0.055 (`caps_score` in `reels.py`).

**Result: 0 candidates** (`candidates.json` is `[]`). Every hit is clear text: printed form headings, Navy telegrams
copied in capitals, telegraph-blank boilerplate. No capital run reads under MANCHESTERBLUFF, COMPLETEVICTORY or
COMERETRIBUTION, and none looks like cipher. The extension pass over 24 more Confederate telegram and letter books
(below) found no cipher copied as sent, only clear copies with "in cypher" notes. No bulk_scan.py process was started,
restarted or stopped.

## Method

- `capscan.py hits <jsonl>`: for each hit, takes the frame's full OCR from `nara_reels/cache` when cached (otherwise the
  400-character snippet), extracts runs of >= 3 capital words, and gives each run of >= 15 letters its IC, its score as
  plain English (`en-modern`) and its best score under the three Confederate keys (Vigenère, Beaufort and variant at
  every offset, through slice D's `vig.py`). Output: `hits_scan.txt`. For calibration, the runs slice D read in Taylor's
  books score -1.9 to -2.8 under COME RETRIBUTION. Here the best key score on any real run is -3.7 or lower, and the
  runs with a low plain score are abbreviations and Roman numerals ("XLVA FLA MOH XXVITH HON SECY").
- 44 hits (in 44 items) had no qualifying run in the snippet. Their items were fetched with `reels.py fetch` (4 s
  spacing; list in `snippet_miss.json`) and rescanned on the full frame OCR. All of them are form headings ("SUBSCRIBED
  BEFORE ME THIS DAY", "DESCRIPTION AGE HEIGHT HAIR EYES COMPLEXION", printers' imprints).
- `capscan.py item <naId>`: every frame of a cached item, runs with IC < 0.055, key-tested (`items_rg107.txt`).
- Union route-transposition and code-word telegrams keep English letter frequencies (IC about 0.066), so the IC < 0.055
  filter cannot catch them. For RG 107 they were looked for directly: runs of 5+ capital words with the boilerplate
  removed, plus every "cipher/cypher" mention outside the Western Union terms (`rg107_items_notes.txt`). None found.

## Coverage per input file

| file | lines | items | what they are | kept |
|---|---|---|---|---|
| rg_109_caps.jsonl | 388 | 382 | Papers Relating to Citizens (M345) 259 and Military and Civilian Personnel (M347) 117: Union provost-marshal amnesty and loyalty oaths ("PROVOST MARSHAL'S OFFICE", "SUBSCRIBED BEFORE ME THIS DAY", descriptive blocks) 351, Confederate pay accounts, clothing lists, forage requisitions and vouchers 25. Slave payrolls 5, Macon Arsenal foreman's time book, Abingdon post-guard clothing book, 12th N.C. account book, Contract Bureau staff list (ch. VIII vol. 310), A&IGO special orders 1865 (hire schedules), Mississippi House accounts 1863 (deaf institute): form headings. | 0 |
| rg_45_caps.jsonl | 43 | about 36 | Navy Department letters received 1855-1884 (Key West, New York, Boston station telegrams copied in capitals with Roman-numeral dates and word counts, e.g. "KEARSARGE COMDR PICKING ARRIVED"), pay-officer abstracts, Nagasaki public bills, Brooklyn tax bill; Confederate Navy subject file AC (J. C. McGuyre blacksmith bills, Mobile 1862). All clear. | 0 |
| rg_107_caps.jsonl | 4 | 4 | M473 vols. 195-196 (1872-74) and 199-200 (1878-81), Secretary of War telegrams sent: Western Union blank headings and clear postwar telegrams. M504-179B (1863 field telegrams, Army of the Potomac QM): handwritten, OCR noise, clear. M492 roll 25: a medical letter of 1863. The four items were fetched and scanned whole (939 + 920 + 1481 + M492 frames). | 0 |

## Extension: Confederate telegram books not reached by slice D

The caps filter has low recall on the cipher it was calibrated for. On the cached OCR of Taylor's volumes it flags 1 of
82 frames (vol. 11, 12127054), 1 of 72 (vol. 10, 16878212) and 0 of 83 (vol. 196, 45485022), and none of the three is
in `rg_109_caps.jsonl`. The cipher runs in those books are three to five words embedded in clear text, below the
>= 6-word run threshold. So the RG 109 telegram books were searched directly: one catalogue search ("Military
Departments Telegrams Sent", the top 100 hits saved as `rg109_telegram_books.tsv`), then 24 books not fetched by
slice D were fetched and run through slice D's `capruns.py` (`capruns_f.txt`) and a "cipher/cypher" mention search
(`cipher_mentions.txt`):

12497590 (Telegrams Sent, Dept. Ala., Miss. & E. La. 1864, ch. II vol. 6), 18253595 (same, 1865), 28470698 (same,
Jan-Feb 1864), 28470762 (J. E. Johnston telegrams June-Dec 1863, vol. 236 ¾), 23830039 and 19082623 (Army of Northern
Virginia letters and telegrams sent, 1862-64), 18562622 (Lee letters sent, Richmond 1862), 26282311 (Longstreet
confidential, second copy), 75810542, 19085416, 19085507 and 28470211 (District of Texas, New Mexico and Arizona,
1863-65, including the confidential book), 99292654 (N.C. Reserves 1864-65), 24621771 (E. Tennessee/W. Virginia
1863-64), 29906489 and 166044721 (Chalmers, received), 166045337 (Hébert received, Jan 1865), 16615916 (S.C. military
districts, 1864-65), 28472472 (Whiting 1864), 18561772 (Trans-Mississippi letters sent 1864), 23833280 (District of
Arkansas 1864-65), 28471840 (Breckinridge 1861-63), 24467018 (Army of the Mississippi 1864), 166044584 (Wayt, ACS).

What they hold: no cipher words copied as sent. The capital runs are archival stamps ("WAR RECORDS COPIED", "REPAIRED
... NATIONAL ARCHIVES"), printers' imprints and headings. There are 40 "in cypher" mentions, all on clear copies:
"answer in cypher", "(in cypher)" marked on Trans-Mississippi letters of April 1864, Johnston's June 1863 books
("your despatch imperfectly deciphered", "in putting the President's telegram in cypher I think the process was
reversed", "the deciphering clerk" C. H. Smith), and Lee's 1862 note on an intercepted cipher telegram at Huntsville.
These are clear-text copies of cipher traffic, so there is nothing to read. Caveat: these books are handwritten and
the OCR is poor. Lowercase cipher words would be garbled into noise that no filter separates, so "no cipher" means "no
cipher legible in the OCR". The Taylor books worked only because the clerk wrote the cipher words in capitals.

## Leads (no rows)

- J. E. Johnston's Jackson telegram book, June 1863 (28470762, ch. II vol. 236 ¾): complaints about garbled cipher
  between Johnston, Pemberton and Richmond. These are the well-known Vicksburg-campaign cipher failures, printed in
  the OR (ser. I vol. 24), so they are not a candidate. They could serve as crib context if a Pemberton/Johnston
  ciphertext turns up.
- Lee, Richmond, 1862 (18562622, vol. 83 ½, frame 0075): a Union (?) telegram "received here was in cypher" and
  intercepted at Huntsville, forwarded to the Secretary of War. The ciphertext is not copied in the book.
- Slice D's lead stands: Union signal-cipher intercepts off Charleston, Sept-Oct 1863 (Markoe), not in these books.

## Not reached

- The other ~76 of the 100 search hits and the remaining RG 109 ch. II telegram books (the search reported 32,408
  loose matches; only the first 100 were listed).
- Viewing frame images of the handwritten books to look for lowercase cipher words the OCR destroyed. No images were
  viewed in this pass.
- `rg_393_caps.jsonl` exists in `out/` but was not in this slice.

## Files

`capscan.py` (scanner), `hits_scan.txt`, `items_rg107.txt`, `rg107_items_notes.txt`, `snippet_miss.json`,
`capruns_f.txt`, `cipher_mentions.txt`, `rg109_telegram_books.tsv`, `fetch1.log`.
