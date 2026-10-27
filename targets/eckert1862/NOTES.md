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
