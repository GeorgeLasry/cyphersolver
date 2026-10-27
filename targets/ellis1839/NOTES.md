# Powhatan Ellis to John Forsyth, No. 9, Mexico, 16 Nov 1839: a coded despatch in the JQA code, with its 1839 clear copy

Status: contributed by WAINUT (27 Oct 2026). Already solved: the Department's contemporary clear copy of the whole
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

## Remaining gaps

- the two groups not legible on the film (0303.02, 0303.03) - blocker: illegible; the words rest on the clear copy.

## Escalation

- [x] siblings: read with the JQA table (`../jqa`); the values found here used for `../crawford1813`
- [x] clear-pages: the Department's clear copy of the whole passage used to fill and check the reading
- [x] known-keys: the JQA table applies directly (the = 1385, of = 1576)
- [ ] print: Manning vol. 8 (1937) not checked
- [x] key-rebuild: about 40 values from the alignment with the clear copy
- [ ] retry: Ellis's 1836-1837 despatches (M97 rolls 8-9) not tried

## Files

- `ellis1839_transcription.txt`, `ellis1839_decryption.txt`, `ellis1839_reading.md`, `ellis1839_clearcopy.txt`
  (the 1839 clear copy), `ellis1839_pairs.tsv` (values from the alignment)
- `decode.py`: runs `../appleton1823/decode.py` (which applies `../jqa/code_table.tsv`) on this folder's files;
  `--controls` runs the wrong-key controls (standard library)
