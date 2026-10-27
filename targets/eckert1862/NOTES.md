# Eckert ledgers: War Department cipher telegrams, 1862-1867 (catalogue 648)

Status: in progress

Catalogue 648: the telegram ledgers and cipher books of Thomas T. Eckert, head of the War Department telegraph
office, Huntington Library, Thomas T. Eckert Papers (mssEC). Transcribed by volunteers of the Huntington's
"Decoding the Civil War" project on Zooniverse (2016-17); the planned third phase, deciphering with the cipher
books, has not been reported done (searched 27 Oct 2026). This folder holds that third phase as far as it has gone.

## What the ledgers hold

The Huntington Digital Library (CONTENTdm collection `p16003coll11`) has all 67 Eckert items online, and every
ledger page carries the volunteers' transcription in its `transc` field ("Transcription text provided by the
volunteers of Decoding the Civil War (2016-2017)"). `harvest.py` pulls them through the public dmwebservices API
into `data/items/<pointer>.jsonl` (git-ignored, rebuilt by the script); `corpus.py` splits the pages into telegrams
(`data/telegrams.jsonl`) and writes `ledgers.tsv` and `codewords.tsv`.

The ledgers are **not in route cipher**. Sent and Received ledgers alike give each telegram with the route
transposition already undone, in reading order, with the **code words still in place** and the check or padding
words at the end:

> For Andes Gunboats and Cavalry ordered up the Tenn River to destroy bridges ... almost impassable Alden light snow falling
> (mssEC 01, War Dept Ciphers Received, 7 Feb 1862, Halleck to McClellan)

So the open layer is the code vocabulary, a code, not a cipher. Two kinds of ledger:

- **Coded ledgers** (the operator's copy, code words left in): mssEC 15, 20, 22, 23, 24, 25, 35, and others still
  being harvested. Between 5% and 20% of their words are code words of the printed book.
- **Received ledgers already decoded** (mssEC 08, 09, 12, 13, 32): the texts are in clear; only about 1% of words
  match the code list, and those are false hits (Washington, Winchester, White as ordinary words).

## The keys in the Eckert papers

The printed "Cipher for Telegraphic Correspondence" gives route tables (blind words, line indicators, routes for
5 to 10 columns) and pages of printed code words, two per line, with the **meaning written in by hand**. The same
printed words were refilled with new meanings for each issue. What the papers hold:

| item | what it is | fits |
|---|---|---|
| mssEC 41-45 (Cipher Book #1, 5 copies) | one filling: Juno = Lt Gen U. S. Grant, Andes = Fort Donelson, Alden = Indiana, Knox/Knave = Maj Gen B. F. Butler | 1864-65 traffic |
| mssEC 46 (Book #1, 6th copy) | a different 1864 filling (Atlanta campaign places, Rebel generals), pages glued over | Sherman's 1864 traffic (not checked) |
| mssEC 38 (Generals and Places, S. B. Fairchild, New Orleans) | Banks's Department of the Gulf, 1863 (Port Hudson, Brashear, Opelousas) | Gulf 1863 (not checked) |
| mssEC 47-48 (Book #2), 49-66 (Book #5, 16 copies), 67 (Book #9) | not yet looked at | 1865-67 |
| mssEC 37, 39, 40 (handwritten) | post-1866 codes ("Act of Congress of July 1866") | 1866-67 |
| mssEC 36 | Stager's memoranda: who held which key where | index to the keys |

`key_book1_mssEC43.tsv` is copy mssEC 43 transcribed whole (427 vocabulary rows, routes, time code, numerals,
holders: Stager, Eckert, Bruch, G. H. Smith, W. G. Fuller, Beckwith with Grant, Armies of the Cumberland and the
Ohio). Transcribed by a subagent from the page images; readings it marked uncertain carry `?` in the file. Not yet
checked against a second copy line by line.

## Known key applied: Book #1 on the Fort Monroe ledger (mssEC 25)

`decode.py` puts the Book #1 meaning after every code word. On mssEC 25 (Fort Monroe, Ciphers Received and Sent,
3 Feb 1864 - 6 Apr 1865; 924 telegram blocks) it reads:

> for Juno[Lt Gen U. S. Grant] despatches from Flora[Newbern] all quiet at fortune[Newbern] ... poplar[Deserter]
> piloted[Capture +ed] ... whisky[Troops] being forwarded peasant[By the way of] Horace[Weldon] to Galway[Richmond]
> & Welch[Rail Road] seized for that purpose Zebra[Period] ... webster[Signature]
> (Sheldon, Fort Monroe, to Beckwith at Culpeper, 27 Apr 1864)

19.4% of the ledger's words are replaced by the key (14,285 of 73,454). That figure is a count of code words, not
a measure of the reading: it includes false hits on clear words (place names in the headings, ordinary words
that are also code words), and it does not count the code words the book lacks (Harrow, plague, Rowley, Knocks in
the telegrams above). Book #1 also fits mssEC 20 (Sent, Dec 1865-Jul 1867: Galway = Richmond, Frog = New York).
No telegram has yet been measured against the read bar.

## The 1862 telegrams: the key is not in the papers

mssEC 15 (War Dept Ciphers Sent, Feb-Jul 1862), mssEC 01 and mssEC 24 (Fort Monroe 1862) use the same printed
words with other meanings. "For Andes" is McClellan (Lander's telegrams; "Andes plans as to Twinkle have
succeeded"), "Alden" signs Halleck's St Louis telegrams, "Twinkle" is a place on Lander's front (Romney in the
context), "Whistle" the enemy. Book #1 gives Andes = Fort Donelson, Alden = Indiana, Twinkle = organize: the 1862
filling is a different one, and no surviving Eckert book carries it. mssEC 22 (Army of the Potomac, Aug 1862-Apr
1863) is a third filling again (Adam, Abel, Argyle, Austria are frequent, not as states).

Route for these: rebuild the 1862 meanings from the telegrams that the Official Records print in clear (OR series
1 vols 5, 7, 10, 11, 12 for Feb-Jul 1862), word by word against the ledger copy (key from external plaintext), then
from context for the rest. The Received ledgers of the same months may also hold the decoded form of the same
telegrams (adjacent plaintext). Neither has been done: the archive.org and eHistory OR texts did not come through
from this machine on 27 Oct.

## Remaining gaps

- Corpus: harvest of the 67 items still running at the time of writing; telegram counts per ledger in
  `ledgers.tsv` once complete. Blocker: none.
- 1862 coded ledgers (mssEC 15, 01, 24, 22): code meanings not in the papers. Blocker: no key material in the
  papers; workable from the Official Records and the decoded Received ledgers.
- 1864-65 coded ledgers (mssEC 25, 20, 23, 35): Book #1 applies; code words missing from the book, header and
  signature false hits, and a per-telegram reading measure are still to do. Blocker: none.
- Books #2, #5, #9 and mssEC 46/38 fillings not transcribed. Blocker: none.

## Escalation

0a steps tried: sibling and key search in the same papers (done: Book #1 fits 1864-65; the 1862 filling is absent);
clear pages (the decoded Received ledgers, to do); print (Official Records, to do); key rebuild for 1862 (to do).

## Files

- `harvest.py`, `corpus.py`, `decode.py`: harvest, corpus split, key application
- `key_book1_mssEC43.tsv`, `book1_words.txt`: Cipher Book #1 (mssEC 43) transcribed
- `ledgers.tsv`, `codewords.tsv`: per-ledger counts
- `decoded/mssEC25.txt`: Book #1 applied to the Fort Monroe ledger (draft, unchecked)
- `WORKLOG.md`: dated steps

## Contribution by WAINUT (27 Oct 2026)

Contributed by WAINUT (https://github.com/WAINUTAI), a Dutch AI company. The work was done with AI language-model
agents. The ledger pages and the key were checked against the Huntington page images, and a second agent repeated
the decode with its own code from its own reading of the key book. This section adds one more coded ledger and the
key that opens it: **mssEC 19, War Department Ciphers Sent, 27 Jan - 2 Dec 1864, read with Cipher Book No. 9
(mssEC 67)**, pages 1-7 so far. The text above and the files above are unchanged. The new files are in `wainut/`.
`profile.json` gains one document, two `outcome.texts` entries, `outcome.key_file`, credits and dated solution steps;
the existing entries are untouched.

### The ledger and the key

- **Ledger.** Huntington, Eckert Papers, **mssEC 19** (Huntington Digital Library item 9302,
  <https://hdl.huntington.org/digital/collection/p16003coll11/id/9302>), "War D[epartment] Ciphers Sent Jany 27th
  1864 to Dec 2", about 824 telegrams on 400 pages (catalogue note). The volunteers' transcription is in each page
  record, as for the ledgers above; `ledgers.tsv` does not list this item yet. `wainut/mssEC19_p1-7_transcription.txt`
  copies pages 1-7 (14 telegrams, Huntington tel001-tel014). We checked pp. 1, 3 and 4 word for word against the page
  images (IIIF canvases 8893, 8895, 8896) and found no difference. Pages 2 and 5-7 rest on the transcription.
- **What the Sent ledger holds.** As said above for the other ledgers, the words are in reading order with the code
  words in place. On p. 3 the telegram is laid out five words to a row, as a grid ready for the route, so this
  ledger copies the message after the code words were put in and before the route transposition. Only the code
  layer is open.
- **Key.** Cipher Book No. 9, **mssEC 67** (item 1750, 37 canvases; "Cipher for Telegraphic Correspondence ...
  [Cipher Book #9]"): printed code words two to a line, with the meaning written in by hand between them, so the
  left and right word of a line share one meaning. The same key is printed in W. R. Plum, *The Military Telegraph
  during the Civil War* (1882), vol. 1, appendix "Cipher Number Nine Complete" (archive.org `cu31924092908742`). A
  first pass used the Plum OCR. Every code word used in pp. 1-7 was then read on the book images (canvases
  1719-1744). `wainut/cipher9_key_used.tsv` lists them with the canvas, and the time words (canvas 1720).
- **Book #1 does not fit this ledger.** In Book #1 (`key_book1_mssEC43.tsv`) Pagan is Battery, Applause is Big Sandy,
  Vernon is Point and Relay is Evacuate. In No. 9 they are Washington, Halleck, Major General and Cavalry, which is
  what the telegrams need.

### Result: pages 1-7

`python wainut/decode.py` writes `wainut/mssEC19_p1-7_decryption.txt` (T1-T11, line by line) and
`wainut/mssEC19_p1-7_unread_decode.txt` (U1-U3). The sentences are in `wainut/mssEC19_p1-7_reading.md`.

| tel. | page | to (for), from | date | in print |
|---|---|---|---|---|
| T1 | 1 | Sheldon, Fort Monroe (Butler), from D. H. Rucker | 27 Jan 1864 | not found in OR I/32/2 or I/33 |
| T2 | 1 | Smith, St Louis (Grant), Halleck | 28 Jan | OR I/32/2 p. 244 |
| T3 | 2 | Sheldon (Butler), from J. H. Taylor, chief of staff | 30 Jan | not found in OR I/33 |
| T4 | 3 | Willard, Chattanooga (Thomas), Halleck | 30 Jan | OR I/32/2 pp. 263-264 |
| T5 | 3 | Baldwin, Baltimore (Lockwood), Halleck | 1 Feb | OR I/33 p. 488 |
| T6 | 4 | Lt W. B. Kelly (Kelley and Sullivan), Halleck | 1 Feb | OR I/33 p. 489 |
| T7 | 4 | Baldwin (Lt Col Chesebrough), Halleck | 1 Feb | OR I/33 p. 488 |
| T8 | 5 | Baldwin (J. W. Garrett, B&O RR), Halleck | 1 Feb | OR I/33 p. 488 |
| T9 | 5 | Baldwin (Lockwood), Halleck | 2 Feb | OR I/33 p. 497 |
| T10 | 6 | Lawrence, Harpers Ferry (Sullivan), Halleck | 3 Feb | OR I/33 p. 503 |
| T11 | 7 | Sheldon, Fort Monroe (Butler), Halleck | 5 Feb | OR I/33 pp. 518-519 |

- **Eleven telegrams read.** Every code word in T1-T11 has a meaning in No. 9, and each telegram reads as English
  sentences (read_share 1.0 on `research/reading_audit/v2_score.py`).
- **Nine are earlier solutions.** OR Series I prints T2 and T4-T11 in clear (`wainut/or_clear_texts.txt`, from the
  archive.org OCR of vols. 32 pt. 2 and 33). For these the contribution is the pointer and the evidence that No. 9
  is the key of this ledger. T1 (Baker's cavalry on the way to Yorktown) and T3 (Parker's cavalry men and the
  recruits in Maine for Fort Monroe) are staff telegrams that we did not find in print.
- **Where the ledger and the print differ.** Village (= Major) for Brig. Gen. K. Garrard (T4). Vernon/Vermin
  (= Major General) for Kelley and Lockwood, where OR prints "General" (T8, T10); the clerk seems to use them
  loosely. OR adds "and burning" in T4. Antwerp is "Adjutant [General]" in the book and "Assistant Adjutant-General"
  in OR (T2).
- **Controls** (`python wainut/decode.py --controls`, `wainut/controls.txt`). For 64 of the 68 code-word tokens of
  the nine printed telegrams, the meaning appears in the printed text of the same telegram. With the meanings
  shuffled among the same code words (500 runs) the count is 4 to 24 (median 14). The four misses are the rank words
  above. Time words agree with the printed time in 6 of 8: T2 has Martha (1.30 p.m.) where OR has 1.24 p.m., and T7
  has Harriet (1 p.m.) where OR has 1.15 p.m. The second agent's own decoder and control, on its own reading of the
  key images, gave the same readings, and 39 of 42 hits against 2-19 for shuffled keys (a narrower count).
- **Corrections made in review.** T6 has Vermont (Brig. Gen.), not Vernon: checked on the page image. Hammer is Fort
  Monroe: it stands under the hand-written heading "Forts" (canvas 1735). Palate is the left word of the Yorktown
  line. Antwerp was found in the book (canvas 1729); it had first been inferred from OR. Vernon/Vermin is on page
  [22], not [21].

### Not read on pages 1-7

`wainut/mssEC19_p1-7_unread_decode.txt` shows these three telegrams with the No. 9 meanings where they exist. They
are not counted as read.

- **U1, Caldwell to "Nestor", 1 Feb.** No. 9 gives Nestor = Raleigh, Midas = New York, Bermuda = F. Sigel, Biscay =
  Jno. Pope and Peru = Wilmington. The second agent also read Walnut = Army, Salem = Flotilla, Lady = Galveston and
  Jaunts = Port Hudson in the book. Together these make no sense ("opinion of New York that Early ..."), so another
  word list was probably used.
- **U2, to S. H. Beckwith, 5 Feb.** Grapes, Plaster, Emily and Paradise were not found among the No. 9 meanings
  checked. Unity is a code word whose line has no meaning written in (canvas 1742). The rest is clear: "I leave here
  today and will report to you soon as possible. A. Anderson".
- **U3, Baldwin (for Lockwood), 5 Feb, prisoners of war passing through from Cleveland.** Pauline has no meaning
  written in. Quarrel = Pemberton and Ink = Abingdon do not fit, and Rodneyed, Abel and Viola are not in No. 9 as
  checked. Probably another list.

### Remaining gaps (this contribution)

- mssEC 19 pp. 8-400 (about 810 telegrams) are not decoded yet. This includes the McPhail report of 15-16 Feb 1864
  on pp. 9-10, which is heavy with code words. Blocker: not attempted; the method is the same.
- U1-U3: the word list they use is not identified. Blocker: no key material found yet.
- The page images of pp. 2 and 5-7 were not checked against the transcription.
- OR was not searched for T1 and T3 beyond vols. 32 pt. 2 and 33.

### Files (wainut/)

- `mssEC19_p1-7_transcription.txt`: the volunteers' transcription of pp. 1-7, with page and telegram markers.
- `cipher9_key_used.tsv`: the No. 9 code words used, read on the book images, with canvas numbers.
- `decode.py`: applies the key and writes the decodes; `--controls` writes `controls.txt`.
- `mssEC19_p1-7_decryption.txt`, `mssEC19_p1-7_unread_decode.txt`: line-by-line decodes.
- `mssEC19_p1-7_reading.md`: T1-T11 as sentences.
- `or_clear_texts.txt`: the nine printed clear texts (OR I/32/2 and I/33), for comparison.
