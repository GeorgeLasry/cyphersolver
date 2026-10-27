# William Vans Murray to James Madison, Paris, 26 June 1801: the coded postscript


Unsolved Catalogue no. 481 (`research/founders_emlo/candidates.json`, Founders row). Prior state: the Madison Papers
abstract (PJM-SS 1:353, Founders [Madison/02-01-02-0456](https://founders.archives.gov/documents/Madison/02-01-02-0456))
says the "partially encoded postscript—beginning 'As to' and concluding 'not a Word has yet been said'—not deciphered
(key not found)".

## The document

- **NARA RG 59, Diplomatic Despatches, Netherlands, vol. 4** = microfilm **M42 reel 5**, catalogue naId 188770447
  (26 June 1798–2 Sept 1801, 433 frames; manifest `objects_m42_vol4.json`, downloader `dl.py`). The letter is
  frames **0397** (No. 5, "Paris 26th June 1801", body in a clerk's hand) and **0398 left** (end of the text,
  Murray's signature and the postscript in his hand). Marked duplicate; "Via Bordeaux / Sent 27 june 1801".
- The catalogue row says "The Hague"; the letter is dated **Paris**. Murray was in Paris (from 22 May 1801) to exchange
  the ratifications of the Convention of Mortefontaine (30 Sept 1800), which the Senate had ratified on condition that
  Article 2 (treaties and indemnities) be struck out. The letter reports that the French ministers refuse that
  suppression.
- Only one copy is in vol. 4 (frame 0394 is the 24 June letter). The original went via Le Havre (Capt. Rodgers);
  it is not in DD France (M34 reel 9, naId 188669701, which is the 1800 envoys' letter-book) and was not found.

## The cipher

The whole coded part is six number groups, in Murray's own hand (`transcription.txt`):

    P.S. As to 536 . 406 . 1004 . 264 . 1136 . 1175 . not a Word has yet been said —

The last group was first read 1075; at 4x it is 1175 (the same "11" as in 1136 on that line).

**System.** Murray's legation code of 1797-1801: a one-part numbered code of about 1-1600 groups, whole words and
syllables, syllables joined by dots (e.g. 712.621.1161 = Tribunate, 279.1136.1175 = majority), with some homophones
(revolution = 1194.1093.1224.1365 and 1194.738.13). Not the Pinckney, Armstrong or JQA codes in this repository
(the = 1651, 972, 1385 there; here the = 536).

## Key material

The code was never printed and no key sheet is known. Its values come from Murray's other coded despatches in the
same series, decoded between the lines at the State Department:

- the decoded sibling named in the catalogue row: P.S. of 18 May 1801 to No. 132 (vol. 4, frame 0372 left), decoded
  by Wagner: 1285.1181 Gaudin, 712.621.1161 Tribunate, **536 the**, 247 Consuls;
- Murray's 1797-98 despatches to Pickering, DD Netherlands vol. 3 = M42 reel 4 (naId 188770022, `objects_m42_vol3.json`),
  which carry long coded passages with a clerk's interlinear decode (frames 0018-0199; No. 13 of 10 Oct 1797,
  No. 25 of Dec 1797 and others). About 150 pairs were transcribed from them (scratch notes summarised in `pairs.tsv`
  for the groups that matter here).

## Reading

| group | value | evidence (contemporary decodes) | grade |
|---|---|---|---|
| 536 | the | vol. 4 f.0372 (Wagner, 1801); vol. 3 decoded passim | C |
| 406 | arm | vol. 3 f.0224R 406.1503s *armies*, 1086.406.1004 *alarmed*; f.0257L 406.517 *arming* | C |
| 1004 | -ed | vol. 3 f.0167R 948.164.1004 *intended*; f.0170L 1369.1004 *worked* | C |
| 264 | neutral | vol. 3 f.0039R 264.88 *neutral ministers* | C |
| 1136 | -i- | vol. 3 f.0093L, f.0167R 279.1136.1175 *majority*; f.0170L 1167.1136.834 *written* | C |
| 1175 | -ty | vol. 3 f.0093L, f.0167R *majority*; f.0134R *apology*; f.0167R *speedy* | C |

    P.S. As to the armed neutrality not a Word has yet been said —

The armed neutrality is the League of Armed Neutrality of the northern powers (Russia, Sweden, Denmark, Prussia,
December 1800), which had collapsed after Paul I's death (March 1801) and Copenhagen (April 1801); Murray's 7 May
despatch is about its weaknesses. Murray reports that in the Paris conferences on the Convention the subject has not come up.

All six values are attested in the contemporary decodes and were checked on the frames: 264.88 on f.0039R;
279.1136.1175 and 948.164.1004 on f.0167R; 1086.406.1004 *alarmed* on f.0224R (crop `crop_0224R_alarmed.png`, which
also gives -ed = 1004 a third time); 406.517 *arming* on f.0257L (`crop_0257L_arming.png`); 536 on f.0372. Murray
also wrote 406.1004 for *armed* in No. 44 of 28 May 1798 (f.0365R, "those ships to be armed", undecoded but clear from
the plain text on the page). Reading file: `reading.txt` (6 of 6 cipher tokens read, all grade C).

*Armed* was first inferred from context and confirmed afterwards. The order of the work was: transcription, match of
1004/264/1136/1175 against the vol. 3 decodes, the hypothesis *armed*, then a search of the remaining vol. 3 frames
for 406, which found it decoded three times.

## Remaining gaps

None. Every token is read from an attested value.

## Escalation

Not needed for the reading. Done anyway: siblings (the 18 May 1801 P.S.; vol. 3 frames 0018-0421), the original
copy (sought in DD France M34 reel 9; not there), and a re-read of the last group (1175, not 1075).

## Scan notes

`scan/vol3_codes.md` (pairs from vol. 3 frames 0018-0211, ~150, with frame references) and `scan/found406.md` (the 406
search, frames 0212-0421) are the subagents' working transcriptions. Only the pairs in `pairs.tsv` were checked on
the images; the rest are unverified and would need checking before reuse as a key.
