# Motion in Congress, 10 Aug 1781, partly in Lovell's cipher (PCC item 59 vol. 1 p. 133; part of catalogue 631, closed in `targets/pcc1780`)

Status: no write-up. Contributed by WAINUT (27 Oct 2026); the site page and the ledger rows are left to the
maintainer. Already solved: the plaintext is printed from the journal in JCC 21:853-854 (1912). Added here: the
match of Lovell's "Jay" key, filed in the same volume, to the cipher words, and the nulls.

This folder is a sub-target of `targets/pcc1780`, which closes catalogue 631 as a whole and inventories the volume.
It holds only the decipherment of one piece of that volume (pcc1780's row "Report on instructions to Jay ...,
10 Aug 1781", images 105-106 there, PCC pp. 133-134).

Catalogue 631. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents;
the transcriptions were made with a vision-capable language model. The numbers and the key were read twice from the
NARA scans, the second time independently, and the decryption was checked against the images.

## 1. The volume

NARA RG 360, Papers of the Continental Congress, item 59 vol. 1, "Miscellaneous Papers, 1770-89" (M247 roll 72),
[naId 475671573](https://catalog.archives.gov/id/475671573), 422 images. Image n below is the n-th digital object;
its scan is `https://catalog.archives.gov/medialz/partners/dc-metro/rg-360/M247/pcc_172591_0001/<Fold3 file>.jp2`.
The per-image descriptions (from Fold3) are in the NARA record. All the cipher material sits in objects 96-136
(MS pp. 115-175) and 318-325 (pp. 329-336). The catalogue entry links the file unit (naId 2124632), the item
"Cipher With Keywords" ([naId 631635424](https://catalog.archives.gov/id/631635424), PCC 59 vol. 1 pp. 141-142) and
the exhibit item [naId 2450021](https://catalog.archives.gov/id/2450021). A second exhibit item,
[naId 2440605](https://catalog.archives.gov/id/2440605), was found here for the fisheries resolve. Both exhibit items
are colour photographs of leaves of this volume (2450021 = the key sheet of pp. 144-146; 2440605 = the fisheries
resolve of 22 Jan 1782, pp. 155-156). Object numbers here are 1-based; pcc1780 counts the same images from 0.

## 2. The document read here

- **Source.** MS p. 133, object 106 (Fold3 172698,
  [scan](https://catalog.archives.gov/medialz/partners/dc-metro/rg-360/M247/pcc_172591_0001/172698.jp2)); verso
  p. 134, object 107 (Fold3 172699), endorsed "Aug. 10. Negative / J. Jay".
- **What it is.** "By the United States in Congress assembled, Augt 10 1781": the report of the committee on a letter
  of the 9th from the Superintendent of Finance is considered, and a proposition is put that "the said minister" (Jay,
  at Madrid) be empowered to make further cessions of the right to navigate the Mississippi. Every member present
  votes no; twelve states vote no, and North Carolina, with one member, is not counted. "Extract from the minutes",
  signed James Lovell. Two stretches of the proposition are in cipher.
- **Transcription.** `transcription.txt` (whole page, line by line), `ciphertext.txt` (the 57 cipher numbers only).
  "1119" is written without a point; it decodes only as 11, 19 (h, t), so it is two numbers. The "13" in the fourth
  cipher line is written over another figure and reads 13.

## 3. The system and the key

James Lovell's column cipher. The alphabet has 27 signs, a..z and &. Each key letter heads a column that runs
through the alphabet from that letter, so row 1 is the key letter itself. A letter is written as its row number;
the columns are used in turn, letter by letter. This is the same convention as Dana's WIN table (targets/dana1783).

The key is in the same volume: Lovell's key-letter sheet, p. 144, object 115 (Fold3 172707,
[scan](https://catalog.archives.gov/medialz/partners/dc-metro/rg-360/M247/pcc_172591_0001/172707.jp2)), endorsed on
p. 146 "Cyphers / Adams / H Laurens / Franklin / Palfrey / Jay". Under "Jay" stand two columns: B (1 = b ... 27 = a)
and Y (1 = y, 2 = z, 3 = &, 4 = a ... 27 = x). Rows 28, 29 and 30 are numbered but carry no letters; the Adams and
H. Laurens columns on the same page have the same blank rows. Transcribed in `key.txt`.

**Nulls.** The first stretch opens with 30 and 28. A first pass wrapped them onto rows 3 and 1 ("dy") and left a
two-letter hole. The verifier's correction is adopted: these rows are blank on the key, so 30 and 28 are nulls. They
give no letter and do not move the alternation. Nothing is missing ("to make such further cessions"), and the 1912
print confirms it.

**Phase.** With the nulls left out, the first stretch has 25 letters, B to B. The alternation runs on through the
clear words, so the second stretch starts on Y. Restarting at B gives gibberish there.

## 4. The reading

Line by line in `decryption.txt` (output of `python decrypt.py`), as sentences in `reading.md`:

    A: 30 28 | 5 24 17 23 7 8 17 6 4 22 18 12 14 17 18 18 5 23 7 8 17 12 6 11 19
       nulls | f  u  r  t  h e r  c e s  s  i  o  n  s  o  f  t  h e r  i  g  h  t
    B: 17 27 25 8 10 27 23 8 18 13 18 5 23 7 8 17 12 21 8 17 16 8 22 18 12 18 22 8 19 8
       n  a  v  i g  a  t  i o  n  o  f t  h e r  i  v  e r  m  i s  s  i  s  s  i p  i

> "That the said minister be & he is hereby authorised and empowered to make such FURTHER CESSIONS OF THE RIGHT of
> these United States to the NAVIGATION OF THE RIVER MISSISSIPI as he may think proper and on such terms &
> conditions as he may think most for the honor & interest of these United States."

The yeas and nays were called for by Roger Sherman; every member present voted no. Twelve states voted no; North
Carolina had one member present and is marked "x" (not counted). The roll call is written out in `reading.md`.
All 57 numbers are accounted for (55 letters, 2 nulls). The text is English; no translation is needed.

Context: in 1781 Congress weighed giving up the claim to navigate the Mississippi to win Spain's alliance and aid.
Earlier in 1781 it had already allowed Jay to give up navigation below 31 degrees (general history; that resolve
was not opened here). This motion, to let him cede further rights on terms he thought proper, was rejected. The
extract was made with the key letters assigned to Jay, and the verso is endorsed "J. Jay".

## 5. Controls (`python decrypt.py --controls`, output in `controls_output.txt`)

Scores are mean letter-bigram log-probabilities, with bigrams counted from the repository's English word list
(`lang/lexicons/en.json.gz`).

- B/Y with the nulls and the running alternation: **-2.873**.
- All 702 ordered pairs of two different key letters: B/Y ranks first. The next best, N/Y, scores -3.778 and is
  gibberish ("ructteccqsdi&ndor..."). The median is -6.177.
- The other columns on the same sheet give gibberish: Adams C/R -6.272, H. Laurens Y/O -6.312, all six Franklin
  orders of C, O, R and all six Palfrey orders of U, N, T between -5.16 and -6.63, and Jay swapped (Y/B) -5.094.
- B/Y with the alternation restarted at B for the second stretch: the first stretch reads, the second is gibberish.
- 200 shuffles of the 55 letter numbers under B/Y: best -3.636, mean -4.754.

The verifier's own script (different code, a word-coverage score) gave the same result: only B/Y of the 702 pairs
reads (coverage 1.0, next best 0.31).

## 6. Earlier solution

Journals of the Continental Congress, vol. 21, ed. Gaillard Hunt (Washington 1912), pp. 853-854, Friday 10 Aug 1781
(archive.org `journalsofcontin21unit`, opened by the verifier):

> "That the minister be empowered to make such further cession of the right of these United States to the navigation
> of the river Mississippi as he may think proper, and on such terms and conditions as he may think most for the
> honour and interest of these United States -- The yeas and nays being required by Mr. [Roger] Sherman --"

The footnote on p. 854 reads: "This resolution (partly in cipher) and vote, as an extract from
the minutes, by James Lovell, are in the Papers of the Continental Congress, No. 59, I, folio 133." So the print
names this very copy, and the plaintext has been known since 1912. It comes from the journal, not from a
decipherment. The decryption agrees word for word, apart from "cessions" (cipher) against "cession" (print), and the
copy's "Mississipi" and "authorised and empowered" against the print's "Mississippi" and "empowered". The NARA/Fold3
description of the item cites the print ("Printed in Journals, 1781, p. 853-854"). The print was opened only after
the decryption was made.

So this is not a new decipherment. What is new: the match of Lovell's Jay columns to this copy and the nulls. We
found no source that applies the key to this copy; Weber, *United States Diplomatic Codes and Ciphers 1775-1938*
(1979), which treats Lovell's systems, was not checked.

## 7. The other cipher pieces in the volume

See `targets/pcc1780/NOTES.md`, which inventories the cipher pieces and key sheets of PCC item 59 vol. 1 and gives
the plaintext source of each (the Livingston letter to Franklin of 26 Nov 1781, the "Letter to Dr Franklin in
Cypher"; Thomson's dictionary-code note of 19 May 1780; the Committee for Foreign Affairs letter to Jay of 16 June
1780; the resolves of 22 Jan, 8 Feb and 7 Aug 1782). Two readings here bear on that inventory:

- The fifth name on Lovell's key-letter sheet (p. 144, docket p. 146) reads "Palfrey" (columns U, N, T), presumably
  William Palfrey, named consul to France in 1780; pcc1780 had "Dalgey(?)" and is corrected in this branch.
- Lovell's note on his use of the Dumas numbers (pp. 142-143), with words written in Dumas numbers, is a note on
  key use, not a message; it was not decoded here.

## Remaining gaps

- None in the motion of 10 Aug 1781: every number is accounted for. The rest of catalogue 631 is in `targets/pcc1780`.
- Weber (1979) was not checked for an earlier application of the Jay columns to this copy.

## Escalation

- [x] siblings: the other cipher pieces of the volume are in `targets/pcc1780`; none shares the Jay columns.
- [x] clear-pages: the clear text of the motion frames the two stretches.
- [x] known-keys: Lovell's key sheet in the same volume; the Jay columns fit, the other columns are controls.
- [x] print: JCC 21:853-854 opened and compared.
- [n/a] key-rebuild: the key is on the sheet; only rows 28-30 needed a reading (blank, so nulls).
- [n/a] retry: the motion is read in full; the rest of the volume is in `targets/pcc1780`.

## Files

- `transcription.txt`: p. 133 line by line, with the endorsement of p. 134
- `ciphertext.txt`: the 57 cipher numbers
- `key.txt`: the Jay columns of p. 144, and the start letters of the other columns
- `decrypt.py`: decryption and controls (standard library; reads `transcription.txt`)
- `decryption.txt`, `controls_output.txt`: output of `python decrypt.py` and `python decrypt.py --controls`
- `reading.md`: the extract as sentences, with the roll call
- No images are kept here; they are on the NARA catalogue pages.
