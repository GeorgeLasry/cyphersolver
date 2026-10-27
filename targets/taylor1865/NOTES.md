# Richard Taylor's telegram letter-books, Meridian 1865: Confederate Vigenere, key COME RETRIBUTION (catalogue 681)

Status: in progress. Four telegrams of March-April 1865 are read from the NARA images with the known Confederate
key COME RETRIBUTION; the 6 April telegram needed 11 of its 57 letters corrected and is settled only with the clear
text printed in the Official Records. Two of them (6 and 8 April) are printed in clear in the Official Records, so for
those this is an earlier solution; for the other two (12 and 30 March) we found no printed text. The other cipher
passages in the three volumes are not read yet. Contributed by WAINUT (https://github.com/WAINUTAI), 27 Oct 2026;
the work was done with AI language-model agents. Every cipher word was read on the NARA images, and a second agent
read all four telegrams again on its own crops and decrypted them with its own code.

## The documents

NARA RG 109, War Department Collection of Confederate Records, Chapter II, letter-books of telegrams sent by the
Department of Alabama, Mississippi and East Louisiana (Lt. Gen. Richard Taylor), Meridian, Mississippi:

- vol. 196, Feb-Mar 1865: <https://catalog.archives.gov/id/45485022>
- vol. 11, 1865: <https://catalog.archives.gov/id/12127054>
- vol. 10, 1864-65: <https://catalog.archives.gov/id/16878212> (not read here)

The clerks copied each telegram in clear, but the passages that went by cipher were copied in cipher only, in
capitals, with dashes between the words. The volumes carry the "War Records COPIED" stamp.

| doc | frame, MS page | date | from, to | cipher letters | prior print |
|---|---|---|---|---|---|
| v196-0061 | vol. 196 fr. 0061, p. 117 | 12 Mar 1865 | Taylor (W. F. Bullock Jr., AAG) to Maj. Gen. D. H. Maury, Mobile | 180 | none found |
| v11-0022 | vol. 11 fr. 0022, pp. 40-41 | 30 Mar 1865 | E. Surget, AAG, to Lt. Gen. Taylor, Selma | 52 | none found |
| v11-0036 | vol. 11 fr. 0036, p. 69 | 6 Apr 1865 | Surget to Lt. Col. Wm. M. Levy, Mobile | 57 | OR I/49/2 p. 1209 |
| v11-0039 | vol. 11 fr. 0039, p. 75 | 8 Apr 1865 | Surget to Lt. Gen. R. Taylor, Demopolis | 61 | OR I/49/2 p. 1216 |

Image links are on each catalogue page above (frame numbers as in the NARA file names, e.g.
`chapter-2-volume-196-0061.jpg`). No images are kept here.

## Key and method

Vigenere with the key COMERETRIBUTION, running over the cipher letters only, starting at offset 0 with the first
cipher letter of each telegram (`key.md`). The key was already known for this correspondence: catalogue entry 681
had read frame 0061 and the vol. 11 OCR runs with it, and it is the known key of Confederate telegraph traffic in
1864-65. Applied to the vol. 11 passages, it fits each from its first letter.
The 12 March telegram has 180 cipher letters, exactly 12 turns of the key.

`python decrypt.py` checks every word of `alignment.tsv` and writes `<doc>_cipher.txt` and `<doc>_decryption.txt`.

## The clerk's capitals

The cipher capitals are written in a looped copperplate. A few letter forms mislead, and the same confusions recur.
The letters as read give the plaintext directly at 171 of 180 places (12 Mar), 50 of 52 (30 Mar), 46 of 57 (6 Apr)
and 59 of 61 (8 Apr). Every other place is explained by one glyph:

- the barred capital that looks like E is often F (EVEQRXXA = strength, BEVOZX = -nstant, TSNIQEL = courier, ME =
  to, IRUBEE = advanta-);
- T for F (ITQON = point, HCHTKRQ = outside), R for J (IIRX = west), N for G (CNAH, EQXLVNI), Y for V (PBYBBG),
  X for W (WXGF), Z for E (PCDXYIKZ), U for M (KUILM), C for B (CH = of);
- in IRUBEE (6 April) a U-like or II-like glyph stands for IC, so the word has 7 letters, not 6.

No correction needs more than one glyph per place. Corrections that were not checked again on a fresh crop are
marked [?] in `alignment.tsv` and the decryptions. The 6 April telegram is the weakest by itself (EQXLVNI needs three
fixes to give "returns"), but the Official Records print it in clear, word for word, which settles it.

## Reading

The four telegrams as sentences: `v196-0061_reading.md`, `v11-0022_reading.md`, `v11-0036_reading.md`,
`v11-0039_reading.md` (cipher words in capitals). Line-by-line decryptions: `<doc>_decryption.txt`.

- **12 March 1865, Taylor to Maury, Mobile.** "Telegraph in cipher what CAVALRY YOU HAVE ON EACH SIDE OF BAY, its
  STRENGTH AND NAME OF COMMANDER. Direct CAVALRY SO KEEP CLOSE as possible TO ENEMY, and to arrange to KEEP IN
  CONSTANT TELEGRAPHIC COMMUNICATION WITH Genl D. W. Adams and with these Head Quarters. Also indicate in cipher
  [?west] POINT you have decided upon OUTSIDE THROUGH WHICH TO COMMUNICATE WITH these Head Quarters, SO COURIER
  LINE may be established. Answer." Canby's advance on Mobile was beginning; Taylor wants Maury's cavalry kept in
  touch with the enemy and a courier point outside the city. The cipher gives WEST POINT where "what point" would
  fit the sense; Taylor had just returned from West Point, Mississippi (facing page), so the clerk may have
  enciphered the wrong word. One hole, read_share 0.989.
- **30 March 1865, Surget to Taylor, Selma.** After clear news (Lee's and Pillow's despatches; Dana's report at
  Vicksburg that Sherman had been wounded; Federal ambulances allowed between Big Black and Jackson): "War Dept
  ought to be again recommended to RELIEVE COL WATTS. Have no official CHARGES AGAINST HIM BUT HIS HABITS UNFIT HIM
  entirely for the position." Watts is probably Lt. Col. N. G. Watts, the agent for the exchange of prisoners (the
  telegram above it on p. 40 is about prisoner shipments and names Col. Watts).
- **6 April 1865, Surget to Levy, Mobile.** "SEE THAT SAM DUNCAN RETURNS PROMPTLY ON TIME. You will understand it is
  TO HIS ADVANTAGE TO DO SO. Think the enemy have crossed river at Selma and going East but have nothing definite."
  (Wilson's raid had taken Selma on 2 April.)
- **8 April 1865, Surget to Taylor, Demopolis.** "NORTHERN PAPERS JUST RECEIVED by General Hodge SAY RICHMOND FELL BY
  ASSAULT ON THIRD INST. He will send them here." The news of the fall of Richmond reaching Taylor's headquarters.

## Controls (`python decrypt.py --controls`, `controls.txt`)

Run on the letters as read, with no corrections:

| telegram | COME RETRIBUTION, offset 0: chi2 / letters agreeing | best other offset, chi2 | COMPLETE VICTORY chi2 | MANCHESTER BLUFF chi2 | 200 random keys, chi2 min / median | shuffled words, letters agreeing, mean / max |
|---|---|---|---|---|---|---|
| 12 Mar | 37 / 171 of 180 | 676 | 381 | 1072 | 402 / 1110 | 10.3 / 21 |
| 30 Mar | 19 / 50 of 52 | 156 | 184 | 323 | 75 / 434 | 3.0 / 10 |
| 6 Apr | 33 / 46 of 50 | 130 | 242 | 133 | 95 / 422 | 3.8 / 12 |
| 8 Apr | 22 / 59 of 61 | 92 | 132 | 273 | 117 / 456 | 5.2 / 25 |

COMPLETE VICTORY agrees in part (71 of 180 letters on 12 Mar) because it shares the key letters C, O, M, E and T in
6 of its 15 places with COME RETRIBUTION; it does not give English. The 6 April control leaves out IRUBEE (read with
6 letters for 7). The second agent ran its own controls on its own readings and got the same result for 12 March,
30 March and 8 April; its 6 April control, which kept IRUBEE, went out of step after that word.

## Earlier solutions and prior print

War of the Rebellion: Official Records, Ser. I vol. 49 pt. 2 (Washington 1897), archive.org
`warofrebellion014902rootrich`, and pt. 1, `warofrebellion014901rootrich` (correspondence to 15 March 1865).
Searched in the OCR full text with the whitespace normalised:

- **6 April, to Levy: printed**, OR I/49/2 p. 1209, word for word with the reading (page checked again on the OCR
  page headers and in the index, "Duncan, Sam. Mentioned 1209").
- **8 April, to Taylor: printed**, OR I/49/2 p. 1216, word for word ("on 3d instant" for THIRD INST; page checked again on the OCR page headers). A first search
  missed this one because the OCR text has double spaces between words; the second agent found it.
- **12 March, to Maury: not found** in OR I/49/1 (which prints the other Meridian telegrams of 12 March, to S. D.
  Lee, Gov. Watts, Forrest and D. W. Adams, about pp. 1050-1051) or pt. 2. Searches: "each side of bay", "courier
  line", "Adams and with", "what cavalry", "cavalry you have", Meridian 12-13 March followed by Maury.
- **30 March, on Col. Watts: not found** in OR I/49/2 ("relieve Col. Watts", "habits unfit", "official charges",
  "Sherman had been wounded", "Federal ambulances", "Big Black and Jackson").

An OCR search can miss a page, so "not found" means not found by that search. OR vols. 45 pt. 2 and 39 pt. 3 were
not checked. We know of no modern decipherment of these letter-book passages; the catalogue entry's own check
(known.py, web search) found none.

## Proposed catalogue changes (entry 681)

- status: four telegrams read in full from the images with COME RETRIBUTION (key over cipher letters only, offset 0
  at each telegram): vol. 196 fr. 0061 (12 Mar 1865), vol. 11 frs. 0022 (30 Mar), 0036 (6 Apr), 0039 (8 Apr). The
  6 and 8 April telegrams are printed in clear in OR I/49/2 pp. 1209 and 1216; the 12 and 30 March telegrams were
  not found in OR I/49 pts. 1-2.
- status: the quoted reading of frame 0061 should read "on each side of bay" (not "which side") and "[?west] point"
  (the cipher gives west; the catalogue's "[what]" is the sense, not the cipher). 180 cipher letters.
- prior_art: OR I/49 pts. 1-2 checked (27 Oct 2026); two of four telegrams printed in clear there.
- Suggested status: read in part (4 telegrams); vol. 10 and the other passages of vols. 11 and 196 open.

## Remaining gaps

- Vol. 196: only frame 0061 read - blocker: not-attempted; the catalogue's OCR run list (about 40 runs) is noisy
  (frame 0027, checked on the image, has no cipher words), so the frames need a visual screen first.
- Vol. 11: frames 0041-0046 and 0076-0081 not read - blocker: not-attempted; mechanical with the known key.
- Vol. 10 (about 8 runs; the OCR suggests COMPLETE VICTORY): not read - blocker: not-attempted; the date of the key
  change is therefore open.
- OR vols. 45 pt. 2 and 39 pt. 3 not searched for the remaining passages - blocker: not-attempted.

None of these has an outside blocker, so this is not a stopping point: the folder stays "in progress" until the
remaining passages are read (mechanical with the known key; vol. 10 probably COMPLETE VICTORY).

## Escalation

- [x] siblings: the three volumes are the sibling set; four telegrams read, the rest listed above.
- [x] clear-pages: the clear text around each cipher passage was used to check the sense.
- [x] known-keys: COME RETRIBUTION fits all four; COMPLETE VICTORY and MANCHESTER BLUFF tested as controls.
- [x] print: OR I/49 pts. 1-2 searched; two telegrams printed, two not found.
- [n/a] key-rebuild: the key is known.
- [ ] retry: the remaining passages of vols. 10, 11 and 196.

## Files

- `<doc>_transcription.txt`: each telegram as written, cipher words as read.
- `<doc>_cipher.txt`: cipher words only (written by `decrypt.py`).
- `alignment.tsv`: each cipher word as read, corrected, and its plaintext, with the glyph notes.
- `<doc>_decryption.txt`: line by line; `<doc>_reading.md`: the telegram as sentences.
- `key.md`; `decrypt.py`; `controls.txt`.
