# NARA bulk-scan triage, slice D: five-letter code pass and RG 109 (27 Oct 2026)

Brief: `research/nara_reels/TRIAGE_BRIEF.md` and `research/archive_sweep_2026-10/BRIEF.md`. Inputs:
`research/nara_reels/out/rg_<n>_letters.jsonl` (frames where most words have exactly five letters) and the RG 109
numeric pass `out/rg_109.jsonl` / `agg_rg_109.tsv`. Dedup against catalogue.json 628-680 and the candidates of
`nara_triage_a/b/c`, `nara_military`, `nara_state` and `nara_catalog`. Checked with `known.py`.

Output: `candidates.json` (1 row, from `rows.py`). No bulk_scan.py process was started or restarted.

Scripts here:
- `filter109.py`: streams rg_109.jsonl and drops the compiled service records → `slice109.jsonl` (regenerable, git-ignore)
- `show.py <naId> <frame> [before after chars]`: prints cached OCR around a frame
- `vig.py` / `vigword.py`: test a cipher run or single words against MANCHESTER BLUFF, COMPLETE VICTORY and COME
  RETRIBUTION (Vigenère, Beaufort, variant; every key offset; `lang` en-modern score or the `en` lexicon)
- `capruns.py <naId> ...`: finds runs of capital cipher words in a cached volume's OCR and key-tests each run
  (output: `capruns1.txt`, `capruns2.txt`)
- `rb_items.txt`, `solid_corr.txt`, `phrases109.txt`: the RG 109 item lists and phrase hits as read

## The row

**Richard Taylor's telegram letter-books, Dept. of Alabama, Mississippi and East Louisiana, 1864-65** (RG 109 ch. II
vols. 10, 11, 196). The clerk copied the cipher words as sent (capitals, word lengths kept), not the clear. One frame
viewed and transcribed (vol. 196 p. 117, Taylor → Maury, 12 Mar 1865). It reads with **COME RETRIBUTION**. On the OCR,
other runs read with COME RETRIBUTION in vols. 11/196 and with **COMPLETE VICTORY** in vol. 10. The keys are known, so
these copies are not unsolved. The row is kept because the deciphered text may never have been printed: the
volumes carry the "War Records COPIED" stamp, and whether the Official Records gives the cipher words in clear was not
checked. Class A, solvability 5, difficulty 1.

## Coverage per input file

| file | hits | what they are | kept |
|---|---|---|---|
| rg_59_letters.jsonl (400/400 done) | 68 lines (some repeated) | M862/M1442, 29 frames in 20 items: OCR noise (dotted or faint pages read as "sasaa essea"), name lists, tables, Spanish column heads, a ship-code list. M367 roll 192 (27202251), 9 frames: a 1915 Bryan→Page "special cipher" code-word letter with the decode written between the lines. Other M367, 8 frames: WWI tables and inventories, plus a 1918 Christiania form decoded in the Green code. 13 frames in 11 items: 1875-1900 State Department cipher telegrams copied into despatches (see below), all decoded. The rest: sealing tables (M50), Venezuela and Belgian statistics, irrigation tables (M179), a Baghdad estate inventory. | 0 |
| rg_84_letters.jsonl (400/400) | 7 | Jerusalem consulate OCR noise (4), Djakarta 1965 telegrams (post-1950) | 0 |
| rg_45_letters.jsonl (400/400) | 3 | Confederate Navy enlistment name index (M1091) | 0 |
| rg_38_letters.jsonl (finished during this pass: 308 files in the second scan) | 63 | WWII war diaries and action reports: route and beach code names, spotting logs, cargo manifests, statistics; Okinawa gazetteer index | 0 |
| rg_165_letters.jsonl (249 files done at 09:36, scan still running) | 18 lines (9 distinct frames) | M1024 War College Division tables (anti-aircraft annex, camp facilities, division strength charts, statistics) and an M1513 China newspaper index | 0 |
| rg_107, 393, 76, 11, 457, 65, 360, 109, 242, 94 letters | not yet written | still queued in the running scan when this pass ended | n/a |
| rg_109.jsonl (1,261,830 frames, 257 phrase, 24 desc) | 1,249,731 frames + 23 phrase + 19 desc in compiled service records, skipped | Kept 12,099 frames: Record Books 5,819, enslaved-labour payrolls 4,100, personnel papers M347 1,794, citizens M345 287, casualty lists 91, manuscripts 8. 141 items in correspondence volumes have "solid" numeric frames, all read by snippet: indexes to letter/telegram registers, accounts, rosters, Lee's telegram account book, receipt books. No numeric code. | see below |
| rg_109 phrase/desc (234 outside the CSRs) | 234 | About 190 are telegraph-blank boilerplate ("errors in cipher or obscure messages") and Fayetteville oath forms. The rest are "in cipher" notes in Confederate letter-books. 28 volumes fetched (`reels.py fetch`, 4 s apart) and run through `capruns.py`. | 1 row |

### RG 109 volumes fetched and what they hold

- Cipher words copied as sent, readable with a known key: vol. 196 (45485022), vol. 11 (12127054) and vol. 10
  (16878212) → the row.
- Clear copies only, with notes such as "sent in cipher", "could not decipher your despatch" or "(start in cypher)":
  Pemberton vols. 57 and 60 (18220719, 19082026); Trans-Mississippi "Confidential" vol. 71-5 (18221598); Trans-Miss.
  vol. 71 (18221563); Longstreet confidential vol. 269 (29905738); Beauregard/Dept. SC, GA & FL telegrams vols. 45, 48
  and 50 (26280904, 18255161, 18219820); Polk telegrams vol. 222 (24467075); Bragg vol. 359 (99292770); Charleston
  telegraphic dispatches vol. 47 (19080962, 799 frames).
- Signal Office letter-books, Charleston and Savannah (7821309, 7557411): Capt. Frank Markoe, 20 Sept 1863, says
  Gilmore and Dahlgren went over to cipher after the Confederates were found reading Union flag signals, and that he
  "can make no sense of anything they send". No Union ciphertext is copied in the book. **Lead:** intercepted Union
  signal-cipher messages off Charleston, Sept-Oct 1863, may survive elsewhere (Markoe's reports, RG 109 ch. VIII
  vol. 30), not found here.
- Perry, Benjamin F. (28003751, citizens file, Hilton Head, 5 July 1865): a Union dispatch "came in cipher and the
  signature is unintelligible". It is given in clear, so nothing to read.

## State Department cipher telegrams 1875-1885 (dropped, crib material)

Fetched and read: Spain 1875 (M31 v.80, 188635309), France 1875/1876 (M34, 188698202, 188699484), Turkey 1877 (M46 v.32,
188891066), China 1878/1884/1885 (M92 v.49/71/72/75, 189044391, 189055581, 189056176, 189057696), Austria 1880 (T157
v.28, 189217744), Chefoo 1900 (M102 v.6, 210929063), Schenck London cable 1876 (M179, 153211894). In every case the
clear text or "Translation" sits on the same or the next frame, or the decode is interlined. The only exception is
the Fish → Washburne cipher of 4 May 1875 (M34 v.80 fr. 0026), which is only summarised. It is an outgoing
Department instruction, so the clear should be in M77 (Instructions, France).

These are paired cipher and clear texts in the Department's 1870s-80s five-letter cipher. They are useful as cribs if
entry 634 (Vienna 1868, "never deciphered") or a related 1867-code telegram is ever attacked. Spain 1875 fr. 0080/0081
mixes clear syllables into the groups ("REMON STRAN CE", "INSTA NCESB UTCON"), which is the 1867-code style that
entry 634 describes.

## Not reached

- The letter-scan files for RG 165, 107, 393, 76, 11, 457, 65, 360, 109, 242 and 94 had not been written (RG 165
  had just started, with 0 hits) when this pass ended.
- RG 109 telegram volumes that had no numeric or phrase hit were not fetched. Confederate letter ciphers do not trip
  the numeric filter, so the RG 109 letter pass, once written, should be run through `capruns.py`.
- The OR check for the row.
