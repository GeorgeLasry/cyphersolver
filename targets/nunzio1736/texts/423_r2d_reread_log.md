# Re-reading log r2d, Spagna 423 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, VERIFY3_BRIEF)

## Starting point

423/1 decoded, not read (not attempted on the images); 423/5, 9, 11 decoded, not read (0.20-0.47 on the 22 Oct
measure); about 60 nomenclator groups open; escalation step "retry" not done.

## 1. Is there a text already? Yes, on the DECODE records

- research/reading_audit/r2d_fetch_docs.py fetched every DOC_ and IMG_ file of R26 and R179-R188 (images in the session
  scratchpad only). The b04 re-read had opened only the IMG_ page images. The DOC_*.png documents, listed on the records
  as "284r.jpg [cleartext]" etc., are other folios of the volume, and among them are the contemporary clear copies
  ("Copia", same date, same addressee) of the ciphered letters:
  423/1 = R26 D963-D967 (ff. 284r-286r); 423/4 = R181 D1438 (f. 301r); 423/5 = R182 D1442 (f. 375r);
  423/6 = R183 D1387 (f. 386r); 423/9 = R186 D1394-D1395 (ff. 416r-v); 423/10 = R187 D1444-D1446 (ff. 493r-494r);
  423/11 = R188 D1396-D1397 (ff. 509r-v). R179's seven pngs are other clear letters (21 July); R180's two were not
  checked against 423/3 (already read); R184 and R185 have no png attachments.
- Transcribed in full: texts/423-1_copy.txt, 423-5_copy.txt, 423-9_copy.txt, 423-11_copy.txt. For 423/4, 6, 10 only the
  places of open groups were read on the copy (values below).

## 2. Alignment and transcription

- research/reading_audit/r2d_align.py aligns the copy (normalised letters) with the decode tokens (banded DP; a pair
  costs its edit distance, a valued group its distance to the value, an open group a small cost per letter);
  output texts/423-<n>_r2d_align.tsv. research/reading_audit/r2d_kwic.py lists a group's contexts in all letters;
  r2d_locate.py / r2d_lines.py / r2d_strip.py find a token's line on the page image and crop it at native resolution.
- R26 (NiLan 2017): six corrections, each seen on the image (texts/423_b04_corrections.tsv, item 1): a dropped 5 in
  "Regolare" and in "orecquo"; 8 -> 7 before "di altre"; an ink blot read as 8 before "condotta"; 2 -> 1 in group
  1858 (sempre); "1 1" -> 4 in "fecero". (Tokens 1953 seen on both pages: the group is the same both times.)
- 423/9 "io te danno" (f. 415v l. 3) and 423/11 "le la mede" (f. 510r l. 11) and "ben 3 ma ne ggiata" (f. 511r l. 4):
  the transcription matches the image; slips of the cipherer, the copies give the words.
- A segmentation bug found: values with spaces ("con tutto cio") dropped rows in the token parser; values now written
  without spaces (con_tutto_cio, S.M.Cesarea, Mons.Vescovo).

## 3. Key

Every value checked at every occurrence in the eleven letters (texts/b04_key_additions.txt, r2d block):
- pairs: 26 = del (60+ occurrences, Lasry "a"), 80 = dal (7/7, Lasry "nel"). b04_seg.py now reads two-digit lines of
  the additions file as key corrections.
- replaced nomenclator values: 1219 ancora -> ora; 1239 ecclesiastic -> quell; 1449 open -> ecclesiastic; 1608 maggior
  -> necessari; 1229 affinche -> perch(e); 1231 anch -> pero; 1818 inform -> ragguagli; 1699 aggrav -> pregiudizi; 1865
  grazi -> sodisfazion; 1218 ?sempre -> avut; 1223 ?pero -> mentre; 1260 ?inviat -> Ambasciator; 1368 ?occasion ->
  congiuntur; 1510 ?religion -> giustizi; 1525 ?Infante -> Imperator; 1819 ?rimostra -> rappresent.
- new: 1201 ancora, 1236 quando, 1204 benche, 1206 con tutto cio, 1213 final, 1235 qualsivoglia, 1244 ultima, 1248
  accennat, 1252 alcun, 1322 camera, 1389 costi, 1405 diligenz, 1426 dovut, 1482 Fiorenz, 1499 General, 1502
  giurisdizion, 1513 Governator, 1535 impression, 1544 Inquisitor, 1555 istruzion, 1580 maggior, 1582 Marches, 1601
  Mons. Vescovo, 1646 opportun, 1664 particolar, 1668 pendenz, 1695 possibil, 1696 potre, 1808 Promozion, 1811 propri,
  1840 riflession, 1843 riscontr, 1844 risoluzion, 1845 ?rispond, 1855 second, 1858 sempr, 1862 sentiment, 1864
  signific, 1894 S.M. Cesarea, 1916 Trupp, 1952 = 7, 1953 = 8 (otto), 1957 = 12, 1964 = 19; probable values confirmed.
- Open: 12 tokens (1268, 1765, 1847 in 423/1, words carried by the copy; 1200, 1335, 1960, 1985 in 423/2; 1232, 1469,
  1698, 1942 in 423/7; 1636 in 423/8).

## 4. Readings and scores (research/reading_audit/r2d_score.py: body only, abbreviations de-dotted, v2 holes)

| letter | 22 Oct state, score | 23 Oct plain / explicit | state |
|---|---|---|---|
| 423/1 | decoded, not read, 0.41 / 0.53 | 0.92 / 1.0 | read (A, copy) |
| 423/5 | decoded, not read, 0.60 / 0.80 | 1.0 / 1.0 | read (A, copy) |
| 423/9 | decoded, not read, 0.72 / 0.83 | 0.94 / 1.0 | read (A, copy) |
| 423/11 | decoded, not read, 0.56 / 0.68 | 0.94 / 1.0 | read (A, copy) |
| 423/2 | read, 0.75 / 0.85 | 0.85 / 0.95 | read |
| 423/4 | read, 0.82 / 0.91 | 0.91 / 1.0 | read |
| 423/6 | read, 0.73 / 0.91 | 1.0 / 1.0 | read |
| 423/7 | read, 0.58 / 0.79 | 0.61 / 0.87 | read |
| 423/8 | read, 0.57 / 0.86 | 0.71 / 0.86 | read |
| 423/10 | read, 0.70 / 0.83 | 0.76 / 0.90 | read |

(The 22 Oct figures here are the same body measure, re-run 23 Oct before the changes.) Readings follow the figures
where they carry other words than the copy, and the copy where a single figure is a slip; each reading's notes list
both. The readings of 2, 4, 6, 7, 8, 10 were corrected by exact replacements (research/reading_audit/r2d_fix_read.py,
r2d_fix_read_en.py) and re-aligned with verify2_nunzio_align.py: every word carried.

## 5. Not done

- The copies of 423/4, 6, 10 were read only at the places of open groups and the corrections; a full alignment of
  those letters with their copies would refine word choices but no group there is open.
- 423/2, 7, 8: no copy among the attachments; their 9 open groups wait for the volume itself.
