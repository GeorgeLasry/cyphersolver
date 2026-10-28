# Powhatan Ellis to John Forsyth, Mexico, 1836-1839: coded despatches in the JQA code, deciphered at the time

Catalogue 653. This is the one Ellis folder for the whole entry: the 1836-37 despatches (M97 rolls 8-9, surveyed and
transcribed by Michael Brackx, issue #120) and No. 9 of 16 Nov 1839 (M97 roll 10, WAINUT, PR #107). The folder keeps
its first name, `ellis1839`, so that links from the sibling JQA-code folders keep working.

## 27 Oct 2026: the whole correspondence, merged (maintainer)

**Outcome: read from existing decipherment.** Every coded passage Ellis sent in 1836-39 was deciphered in the
Department at the time, and the decipherments are filmed with the despatches, except 26 Oct 1836, whose text is in
print (Bosch García 1984). The work here: transcription of the groups, their decode with the JQA table, the check of
each decipherment against them, and three corrections (below).

### The despatches

From Brackx's survey (issue #120; frames are M97 roll 8 = vol. 7 unless marked). Coded pages by despatch, as his
files group them (the date is the printed passage he measured each against):

| despatch | coded frames |
|---|---|
| 19 May 1836 | 0015-0019 (0014 is a mirror-image exposure) |
| 28 May 1836 | 0025-0027 |
| 25 June 1836 | 0071 (and 0066-0067, not assigned in his list) |
| 3 Aug 1836 | 0123-0124 |
| 7 Sept 1836 | 0200 (clear pencilled over the first four code lines) |
| 24 Sept 1836 | 0203-0204 |
| 26 Oct 1836 | 0323 and the top line of 0324 |
| 30 Nov 1836 | vol. 8 0099 (and 0098) |
| 14 Dec 1836 | vol. 8 0208-0209 |
| 21 Dec 1836 | vol. 8 0211 |
| No. 9, 16 Nov 1839 | vol. 9 0298, 0299, 0302, 0303 (sections 1-4 below) |

Also frame 0311, a coded page whose *Cypher* slip is pasted on the same page as filmed on 0310. The decipherments, as
he lists them: clean copies headed *(Deciphered)* or *Cypher*, clear copies, or clear text written between the code
lines, on vol. 7 frames 0020-0023 (19 May), 0027-0028, 0068, 0073, 0115, 0124, 0200, 0310; vol. 8 frames 0099, 0100,
0209, 0211; vol. 9 frames 0300-0301 (1839). 26 Oct 1836 is the one passage with none on the film. Which decipherment
frame goes with which despatch, beyond 19 May and 1839, has not been checked here.

Brackx's transcriptions of all 36 coded pages (about 4,100 groups), his reading of 19 May, his values for Ellis and
his scripts are in his gist (https://gist.github.com/brackxm/541493ba267c2a224b8ff5006215bc38, revision of
27 Oct 2026). They are not copied here until he agrees to the project licence (asked on issue #120, 27 Oct).

### What the decode gives (measured)

- **19 May 1836** (1,383 groups, clerk's clean copy): with the table as it stands 0.826 of words read, 0.912 with
  Brackx's firm values, 0.942 with his tentative ones (his `readmeasure.py`, word by word against the copy). The
  maintainer reproduced frames 15L-15R with our own script: 266/289 groups valued by the table, 289/289 with his values.
- **The other 1836 passages** against the printed text: 0.815 table alone, 0.833 with his values. The values are
  largely fitted on 19 May, so the out-of-sample gain is small.
- **26 Oct 1836** (`ellis1836oct26_*`, transcribed here independently of Brackx): 85 of 90 groups valued by the table;
  89/90 give sense in the reading (0.989), group 285 open. Function-word rate 0.26 against 0.01-0.07 for controls.
- **16 Nov 1839** (sections 1-4): 473 of 519 groups valued by the table after the settlement below; read in full with
  the clear copy.

So the decode alone stays short of the read bar on the long 1836 passages; the texts are read from the 1836
decipherments, and the decode is the check that they belong to these groups.

### Corrections found

1. **7 Sept 1836** (Brackx): Bosch García notes that the last three lines of the coded passage "no están descifradas".
   On frame 0200 the clerk pencilled the clear text over the first four code lines only. The bare lines
   `318 # 1576 1549 929 557 / 496 1576 1385 210 1044 / 249 880 802 1373 983 / 1576 1229 637 1264` decode with the table
   as the second half of the sentence: "favor of an over-thr-ow of the present con-so-li-da-ted form of govern-ment."
   (reproduced by the maintainer). Nothing is missing.
2. **26 Oct 1836 runs onto frame 0324.** The catalogue and Brackx's file stop at the foot of frame 0323 with
   `385 1053` (suc-cour). The top line of frame 0324 has three more groups, `999 1384 205` = "from that power", before
   the clear "So far as I can ascertain perfect tranquility reigns throughout the Republic." This matches the print's
   ending "succor from that power".
3. **1839 transcription settled.** The 14 single groups where Brackx's and WAINUT's independent transcriptions of
   No. 9 differed were read on full-resolution crops of frames 0298-0303:

| group | line | Brackx | WAINUT | frame | value and context |
|---|---|---|---|---|---|
| 41 | 0298.07 | 1551 | 1557 | **1557** (closing stroke with a top bar, as in 7) | context needs 1551 *o* (t-ro-o-p-s); probably Ellis's slip; the clerk wrote "Toops" |
| 54 | 0298.09 | 668 | 1068 | **668** | *and*: "and has been joined" |
| 130 | 0299.04 | 145 | 45 | **45** (no leading 1) | *principal*-ly |
| 144 | 0299.06 | 1450 | 1430 | **1450** (the flagged 5) | *king*: ta-king |
| 146 | 0299.07 | 438 | 1438 | **438** | *ng*: st-(ro)ng |
| 150 | 0299.07 | 1361 | 1261 | **1261** (2, set beside 1361 on the next line) | comma |
| 198 | 0299.16 | 1570 | 1510 | **1510** | *act*: "to act as circumstances" |
| 210 | 0299.18 | 451 | 457 | **457** (7, compared with 451 on 0302.04) | vo-*ou*-ch |
| 232 | 0299.22 | 451 | 457 | **457** | thr-*ou*-gh |
| 292 | 0302.04 | 1001 | 1501 | **1501** | *a*: "with a large portion" |
| 374 | 0302.18 | 1070 | 1075 | **1075** (the flagged 5) | *se*: dis-per-se-d |
| 434 | 0303.02 | 833 | ?03 | **833?** (first digit under the blot; 33 visible) | *di*: un-di-vi-ded |
| 454 | 0303.06 | 1216 | 416 | **416** | *nd*: under-sta-nd |
| 468 | 0303.09 | 731 | 721 | **731?** (middle digit 3 or 2) | *re*: re-lations |

   Nine stand as WAINUT read them, five follow Brackx. Both decodes are applied to `ellis1839_transcription.txt` and
   `ellis1839_decryption.txt`.

4. **401 = n.** The two contributors disagreed (Brackx *n*, WAINUT *ican*; the table has *sian*). In 1839 it stands in
   fron-[401]-ti-er and know-[401] ("known"), and after 65 (*amer*, also *america* in the table) in "Spanish
   America-[401] States"; in 1836 in campai-g-[401] (26 Oct) and Brackx's an-nou-[401]-cing, Sa-[401]-ta. *n* fits
   every case; *ican* fits one only with 65 = *amer*. Settled as *n*.
5. **614 = manifest stays.** 26 Oct has "manifest-ed" (print: "manifested") with the table's 614. Brackx's tentative
   *know* for 614 (one context, ac-know-ledge) is at most a second value.

### Prior work

- The Department's decipherments of 1836-39, filmed with the despatches (above).
- Bosch García, *Documentos de la relación de México con los Estados Unidos* III (UNAM, 1984; free online at
  historicas.unam.mx) prints most of the 1836 despatches from 28 May with the coded passages in clear, 26 Oct
  included (found by Brackx, 27 Oct 2026). So the texts were in print before this project.
- Manning, *Diplomatic Correspondence of the United States: Inter-American Affairs* vol. 8 (1937) is still not checked
  (HathiTrust behind a bot check). It is not needed for the outcome.

## No. 9 of 16 Nov 1839 (WAINUT, PR #107)

Contributed by WAINUT (27 Oct 2026). Already solved: the Department's contemporary clear copy of the whole
coded passage is in the same file, so the method is "read from existing decipherment". The groups were transcribed,
decoded with the JQA code table (`../jqa/code_table.tsv`, applied unchanged) and aligned with that copy: the table
alone gives a value to 471 of 519 groups; the rest (about 48) are filled from the clear copy. The site page and the ledger rows are left to the
maintainer.

Catalogue 653. Contributed by WAINUT (https://github.com/WAINUTAI), a Dutch AI company; the work was done with AI
language-model agents.

## 1. The document

- **Source.** NARA RG 59, Despatches from US Ministers to Mexico vol. 9, microfilm M97 roll 10
  ([naId 189102194](https://catalog.archives.gov/id/189102194)). Code on frames 0298 (after the heading "No. 9 ...
  Sir,"), 0299, 0302 and 0303 (before the clear closing, signed Powhatan Ellis), e.g.
  [frame 0302](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M97/M97-010/M97-010-0302.jpg).
- **Contemporary decipherment in the same file.** Frames 0300-0301
  ([0300](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M97/M97-010/M97-010-0300.jpg),
  [0301](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M97/M97-010/M97-010-0301.jpg)), filmed between
  the code leaves, are the Department's clear copy of the whole coded passage, in words only. It shows the decipherer
  at work: "Cado" corrected to Cañedo, "sp" struck and "not" written above, "we" and "learn" above the line, and the
  misspelling "Toops". So the text was read in 1839. This contribution adds the group transcription, the decode with
  the JQA table and the alignment of the two. The clear copy is transcribed in `ellis1839_clearcopy.txt`.
  The catalogue's "no words" for frames 0298-0303 missed these two frames.

## 2. The code and the key

The despatch is in John Quincy Adams's St Petersburg code of 1811-1812 (the = 1385, of = 1576, that = 1384,
and = 668, I = 1401), whose table was rebuilt in [`../jqa`](../jqa/NOTES.md). This folder has no key of its own:
`profile.json` names `../jqa/code_table.tsv` as its key file, as other entries use a sibling folder's key
(`../feuquieres/grand_chiffre_1691.tsv`, `../balbases1677/key.json`). Nothing in `../jqa` is changed. Three more
letters in the same code have their own folders: [`../crawford1813`](../crawford1813/NOTES.md) (Paris 1813,
catalogue 652), [`../appleton1823`](../appleton1823/NOTES.md) (Cadiz 1823, catalogue 637) and
[`../everett1825`](../everett1825/NOTES.md) (Madrid 1825, catalogue 638). With them, the code is seen in State
Department use from 1811 to 1839, at St Petersburg, Paris, Madrid and Mexico.

`decode.py` here calls the shared script `../appleton1823/decode.py` with this folder's files.

## 3. Transcription and decryption

- **Transcription** (`ellis1839_transcription.txt`): **519 groups** in 88 lines, counting the commas, the
  stops and the groups inserted above the line (the catalogue's "about 500" was right; a first count of 711 was
  wrong). Every line was checked a second time, independently, on full-frame views, and about 15 lines on enlarged
  crops, with no disagreement. Two groups are not legible on the film: one under an ink blot in 0303.02 (di) and the
  last group of 0303.03 (560 or 500, "enemy").
- **Decryption** (`ellis1839_decryption.txt`): `../jqa/code_table.tsv` alone gives a value to 471 of 519 groups, and
  the raw output already reads, e.g. "who were late ly in arm say against this govern ment have either ca pit u la
  ted". Joined into letters and aligned with the clear copy (difflib), the table-only decode recovers 1,228 of the
  copy's 1,394 letters (88%, ratio 0.868); three shuffled tables give 0.12-0.22 and three shuffled group orders
  0.20-0.22 (independent check; script not included). Each line of the file also gives the syllables as read; {x}
  marks a value taken from the clear copy.

## 4. The reading

`ellis1839_reading.md`, read: a body of Texian troops, joined by disaffected Mexicans, has crossed the line, it is
thought to attack Matamoros; the government will send General Arista to the frontier with 4,000 men; a war with
Texas would be popular, and Ellis expects all parties to set aside their animosities against the common enemy; the
foreign minister Cañedo wants a general congress of the Spanish American states, which Ellis thinks unlikely to
succeed. Where the groups differ from the clear copy, the reading follows the groups: "a most respectable source"
(153 = most, H), where the copy has "very respectable sources"; "the 14th instant", where it has "the 14th of
instant". T. M. Nance (*After San Jacinto*) has Arista sent north from Mexico City on 17 Nov 1839, the day after the
despatch.

**New values** (`ellis1839_pairs.tsv`, about 40 pairs from the alignment): above all 1261 = comma (27x, no value in
the table) and 1264 = full stop (11x; the table has gar, H, 1x: a conflict), 1067 = s (table: say, M),
651 = x (Te-x-as, Me-x-i-cans), 1366 = tal, 1003 = able, 336 fifteen, 43 hundred, 987 four, 553 thousand,
601 713 = Mr. The table column was checked against `../jqa/code_table.tsv`; a first draft had some entries wrong (for
example the new value su belongs to 383, not 1123, which is per in the table and in 1839).

## 5. Controls (`python decode.py ellis1839_transcription.txt --controls`)

Function-word rate 0.28 for the true table; every group shifted by 1, 2, 3, 7, 50 or 100 either way gives 0.02-0.12,
three random permutations of the table 0.03. The alignment with the clear copy (section 3) is the stronger check.

## 6. Prior work

The clear copy above. Manning, *Diplomatic Correspondence of the United States: Inter-American Affairs 1831-1860*,
vol. 8 (Mexico, 1937) may print the despatch from that copy: **not checked** (HathiTrust full text answered with a
bot check, which we did not try to get past; the Internet Archive has no copy). Two web searches for phrases found no
printed text.

## Proposed table changes (for `../jqa/code_table.tsv`, not applied)

`../jqa/code_table.tsv` was used as it is. Proposals, with the evidence above: 1261 comma (1839 clear copy); 1264
full stop instead of gar (1839 clear copy, 11x; Crawford 1813, 30x); 713 r (here, and Sir / Mr. in 1813) instead of
port; 1067 s instead of say; 1366 tal instead of take; 1003 able beside cal; and the other clear-copy pairs in
`ellis1839_pairs.tsv`.

Queued as a `jqa` follow-up for the maintainer (not applied here). The most important is 1264 = full stop, attested
41 times (Crawford 1813 30x, Ellis 1839 11x, fixed by Ellis's clear copy), which conflicts with the table's grade-H
"gar".

## Cross-check with Brackx's transcription (issue #120, 27 Oct 2026)

**Settled the same day on the frames: see "Corrections found", point 3, at the top of this file. 401 settled as *n* (point 4).**

Michael Brackx (issue #120) transcribed all of Ellis's coded pages of 1836-40 (36 pages, 4,117 groups; M97 rolls 8-10)
and found the Department's decipherments filmed with them (all but 26 Oct 1836). His four pages of No. 9 (vol. 9 frames
298, 299, 302, 303) and `ellis1839_transcription.txt` both have 519 groups and agree on 505. The 14 single-group
differences, to be settled on the frames when the two are merged (group number in this file, line label, Brackx /
this file):

| group | line | Brackx | here |
|---|---|---|---|
| 41 | 0298.07 | 1551 | 1557 |
| 54 | 0298.09 | 668 | 1068 |
| 130 | 0299.04 | 145 | 45 |
| 144 | 0299.06 | 1450 | 1430 |
| 146 | 0299.07 | 438 | 1438 |
| 150 | 0299.07 | 1361 | 1261 |
| 198 | 0299.16 | 1570 | 1510 |
| 210 | 0299.18 | 451 | 457 |
| 232 | 0299.22 | 451 | 457 |
| 292 | 0302.04 | 1001 | 1501 |
| 374 | 0302.18 | 1070 | 1075 |
| 434 | 0303.02 | 833 | 03 |
| 454 | 0303.06 | 1216 | 416 |
| 468 | 0303.09 | 731 | 721 |

Values: of the 11 numbers both propose, 10 agree (116 Congress, 383 su, 647 mil, 987 four, 1067 s, 1152 por, 1261
comma, 1264 full stop, 1485 rn, 713 r/ro). One disagrees and is unresolved: **401** = *n* (Brackx) against *ican* here
(`ellis1839_pairs.tsv`; the jqa table has *sian*). Compared by the maintainer's own script on the gist's data files
(27 Oct 2026); the contributor's scripts were not run.

## Remaining gaps

Whole entry, as of 27 Oct 2026:

- 1839, the last group of 0303.03 (560 or 500, "enemy") - blocker: illegible on the film; the word rests on the clear
  copy. (0303.02 is now read as 833, *di*, with the first digit under the blot.)
- 26 Oct 1836, group 285 (no value; probably a null, as Brackx proposes for 19 May) - blocker: too short (one
  further context).
- Brackx's 1836 transcriptions and reading are in his gist, not in the repository - blocker: contributor's permission
  to copy under the project licence (asked on issue #120).
- The decode of the long 1836 passages without the decipherments is 0.83-0.94 of words: not a gap in the text, which
  is read from the decipherments; it measures how far the JQA table plus Ellis's values reach on their own.

## Escalation

- [x] siblings: read with the JQA table (`../jqa`); the values found here used for `../crawford1813`
- [x] clear-pages: the Department's clear copy of 1839 and the 1836 decipherments filmed with the despatches
- [x] known-keys: the JQA table applies directly (the = 1385, of = 1576)
- [x] print: Bosch García III (1984) prints the 1836 coded passages in clear (Brackx); Manning vol. 8 (1937) not
  checked, behind a bot check, not needed for the outcome
- [x] key-rebuild: about 40 values from the 1839 clear copy; Brackx's 97 values from 19 May 1836
- [x] retry: the 1836-37 despatches (M97 rolls 8-9) done by Brackx; the 14 disputed 1839 groups and 401 settled on
  the frames; 26 Oct 1836 transcribed and decoded here, with three groups found on frame 0324

## Files

- `ellis1836oct26_transcription.txt`, `ellis1836oct26_reading.md`: 26 Oct 1836 (frames 0323-0324), the passage with
  no decipherment on the film
- `ellis1839_transcription.txt`, `ellis1839_decryption.txt`, `ellis1839_reading.md`, `ellis1839_clearcopy.txt`
  (the 1839 clear copy), `ellis1839_pairs.tsv` (values from the alignment)
- `decode.py`: runs `../appleton1823/decode.py` (which applies `../jqa/code_table.tsv`) on this folder's files;
  `--controls` runs the wrong-key controls (standard library)
