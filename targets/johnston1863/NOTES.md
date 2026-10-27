# Johnston to Seddon, Jackson, 16 June 1863: five words in Vigenere, key MANCHESTERBLUFF (catalogue 629)

Status: already solved in 1863 (a "Translation of Cypher" is filed with the telegram) and printed in clear in 1864.
Added here: the key that fits the five cipher words (MANCHESTERBLUFF, the known Confederate key), how it was
applied, the clerk's slips, and two corrections to catalogue entry 629. Contributed by WAINUT
(https://github.com/WAINUTAI), 27 Oct 2026; the work was done with AI language-model agents and every reading was
checked against the NARA images.

## The document

NARA RG 109, War Department Collection of Confederate Records, series "Telegrams Received by the Confederate
Secretary of War" (naId 651917), item **naId 3854726**, "Enciphered Telegram from General J. E. Johnston to Secretary
of War J. A. Seddon": <https://catalog.archives.gov/id/3854726>.

- Image 1: the telegram, "By Telegraph", "Jackson 16th June 1863", to "Hon J A Seddon", signed "J E Johnston Genl".
  Clear text with five cipher words in capitals. Stamp "WAR RECORDS COPIED".
- Image 2: docket "1705. Genl Johnston, Jackson Miss. June 16. 1863", stamps "Telegrams Rec'd War Dep't", "Filed".
- Image 3: **"Translation of Cypher"**, a separate leaf: "Will not this enable us to x invade Kentucky, for this Gen
  Bragg & should extend over East Tennessee", with the note "x words underscored in Cypher". The five underlined words
  are the five cipher words.

Transcription: `transcription.txt` (the telegram as written), `ciphertext.txt` (cipher words only),
`contemporary_leaf3.txt` (image 3).

## The cipher words

`UNIEK  CXNKVNED  JJTRRK  ISLX  KFYHJEER` (5, 8, 6, 4 and 8 letters; 31 in all), read on the native page image of the
NARA PDF (2510 x 2400 px) and re-read independently by a second agent on enlarged crops.

- **ISLX**: the third letter is a script capital L (bottom loop, top stroke running right), not D. The catalogue's
  "ISDX" is a misreading.
- **KFYHJEER**: the second letter is a crossed "7" form, a script F. A script T is possible but less likely; under the
  key T fails and F fits.
- **UNIEK**: the fourth letter is E-like with a top hook. A hastily written C cannot be excluded [?]; C would fit the
  key (27/33 instead of 26/33).

## Key and method

Vigenere on the tabula recta, key **MANCHESTERBLUFF**. Only the cipher words are enciphered; the key runs on from word
to word and advances by the length of each *plaintext* word. Details and table: `key.md`. Script: `check.py`
(output `check_output.txt`, standard library only).

| plaintext | key | expected | written | written, deciphered | slip |
|---|---|---|---|---|---|
| INVADE | MANCHE | UNICKI | UNIEK | INVCD | key C applied as E; last letter not written |
| KENTUCKY | STERBLUF | CXRKVNED | CXNKVNED | KEJTUCKY | plaintext N left in clear |
| EXTEND | FMANCH | JJTRPK | JJTRRK | EXTEPD | key C applied as E |
| EAST | ESTE | ISLX | ISLX | EAST | exact |
| TENNESSEE | RBLUFFMAN | KFYHJXEER | KFYHJEER | TENNEZSR | one S (cipher X) left out |

26 of the 33 plaintext positions match. The two mismatches where the key letter is C were both enciphered with E, so
they are one systematic slip (the clerk's key, or his reading of it, had E for C), not two random errors.

Why the catalogue's quick test of MANCHESTERBLUFF failed: UNIEK has only five letters for the six of INVADE, so a key
that advances by cipher length is one place out of step from the second word on (5/33), and restarting the key for
each word gives 4/33. The catalogue's ISDX also costs one match.

**The key was not assumed.** Cipher minus crib, letter by letter, gives the key stream directly:
`MANEH | STARBLUF | FMANEH | ESTE | RBLUFMAN` (with one S of TENNESSEE dropped). Read in sequence this is
MANCHESTERBLUFF running across the words, with the slips above.

## Controls (`check.py`)

| test | positions matching (of 33) |
|---|---|
| MANCHESTERBLUFF, advancing by plaintext length | **26** |
| COMPLETEVICTORY | 1 |
| COMERETRIBUTION | 3 |
| VICKSBURG / RICHMOND | 0 / 2 |
| MANCHESTER alone / BLUFF alone | 9 / 9 |
| 20,000 random 15-letter keys | mean 1.19, max 11 |
| the 14 wrong start offsets of the key | 0-4 |
| 119 shuffled orders of the cipher words, right key | mean 5.4, max 18 |

Every control decrypts to gibberish (`check_output.txt`). The shuffled-order maximum of 18 comes from orders that
leave some words in place.

## Reading

`reading.md`; the decryption against the transcription is `decryption.txt`.

> General Bragg informs me that a telegram from Louisville of the 10th says that part of the 9th, 23d Corps have been
> sent to reinforce Grant. Will not this enable us to INVADE KENTUCKY? For this General Bragg & should EXTEND over
> EAST TENNESSEE. J. E. Johnston, General.

- "9th, 23d Corps": the leaf has "the 9th / 23d Corps'". The 1864 print has "the ninth and third corps", a
  transcription difference in the print.
- "Bragg &": the leaf has a cross-like sign after "Bragg", repeated on image 3. The 1864 print gives "General Bragg's
  command should". The sign is clear text, not part of the cipher.

Context: Johnston, commanding in Mississippi during the siege of Vicksburg, passes on Bragg's report, from a telegram out of
Louisville, that part of the Union 9th and 23d Corps has been sent to reinforce Grant, and suggests an invasion of Kentucky, with Bragg's
command extended over East Tennessee. Only the operative words were enciphered.

## Earlier solution

- **Contemporary decipherment**: image 3 of the same item, the Confederate War Department's "Translation of Cypher"
  (1863).
- **Printed 1864**: *Correspondence between the President and General Joseph E. Johnston, together with that of the
  Secretary of War and the Adjutant and Inspector General, during the months of May, June and July, 1863* (Richmond:
  R. M. Smith, 1864), <https://archive.org/details/correspondencebe00conf>. It prints the telegram twice ("Jackson,
  June 16, 1863. To Hon. J. A. Seddon ... Will not this enable us to invade Kentucky? For this General Bragg's command
  should extend over east Tennessee."), and Seddon's letter to Bragg of 17 June quotes the same sentence.
- **Official Records**: probably reprinted in OR Ser. I vol. 24 (the Johnston, Davis and Seddon correspondence), but
  no page was confirmed (ehistory.osu.edu refused access on 27 Oct 2026).

So this is not a new decipherment. What is new is the match of the key to this telegram and the account of the
clerk's slips; we found no source that names the key for it.

## Proposed catalogue corrections (entry 629)

- folio_note: the fourth cipher word is **ISLX**, not ISDX.
- status: the item has a decipherment, on image 3 ("Translation of Cypher"), although there is none on the leaf of
  the telegram itself. The clear text is printed in the 1864 Richmond volume above.
- status/prior_art: MANCHESTERBLUFF fits when the key advances by plaintext length (26/33); the earlier test advanced
  it by cipher length.
- Suggested status: already solved (contemporary decipherment and 1864 print); key identified.

## Remaining gaps

- None in the text. The OR page reference is unconfirmed, and UNIEK/UNICK stays open [?] (it does not change the
  reading).

## Escalation

- [x] siblings: not needed; the telegram is complete and its key fits.
- [x] clear-pages: image 3, "Translation of Cypher", used as the crib.
- [x] known-keys: MANCHESTERBLUFF fits; COMPLETEVICTORY and COMERETRIBUTION tested as controls.
- [x] print: 1864 Richmond print found; OR page not confirmed.
- [n/a] key-rebuild: the key is known; cipher minus crib confirms it.
- [n/a] retry: nothing left unread.

## Files

- `transcription.txt`, `ciphertext.txt`: the telegram and its cipher words as written.
- `contemporary_leaf3.txt`: image 3, the decipherment of 1863.
- `decryption.txt`: line-by-line decryption; `reading.md`: the telegram as sentences.
- `key.md`: the key and the slips; `check.py`, `check_output.txt`: decryption, key stream and controls.
- No images are kept here; they are on the NARA catalogue page.
