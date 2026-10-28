# Union Army cipher telegram books, 1864-1868 (Unsolved Catalogue no. 632)

Status: no write-up. Blocked on access: four of the five NARA series are not digitised; the one online item (Butler to Biggs, 24 July 1864, naId 3854723) was deciphered at the time and is printed in OR I.40.3 p. 432.

Blocked on access for four of the five series; the one digitised item was read at the time and printed.
Overlaps catalogue 680 (`targets/army1865`): the three RG 393 series are the same naIds. Dedup at merge.

## The document

Five NARA series (catalogue checked through the NARA proxy API, 27 Oct 2026):

| Series | naId | Online | What the catalogue says |
|---|---|---|---|
| RG 107 Telegrams in Cipher, 1864 (A1 37, boxes 1-3, 1 ft 4 in) | 628803 | 1 item | Telegrams in cipher from Union officers with surnames in B; "accompanying most of the telegrams are worksheets that were used in deciphering the telegrams in the War Department Central Telegraph Office". A fragment of a larger series. |
| RG 108 Telegrams Received in Cipher by Grant, Halleck and Others, Aug 1864-Dec 1865 (I1 30, vols. 177A-C) | 604437 | no | "Fair copies of telegrams"; name index in each volume. |
| RG 393 Middle Dept, Press Copies of Cipher Telegrams Sent, 1865 (0.5 in.) | 4486363 | no | no scope note |
| RG 393 Dept of the Gulf / Fifth Military District, Telegrams Sent in Cipher, 1866-67 (2 in.) | 5081118 | no | "These records are in cipher." |
| RG 393 Fifth Military District, Office of Civil Affairs, Cipher Telegrams Sent and Received, 1868 (1 in.) | 5131597 | no | no scope note |

All at National Archives at Washington, DC, Textual Reference (archives1reference@nara.gov).

## The digitised item: Butler to Biggs, 24 July 1864 (naId 3854723)

Three images (catalog.archives.gov/id/3854723; PDF 18863.pdf at 2094x3150 px; not committed):
1. U.S. Military Telegraph form, "By Telegraph from Butler['s] Hdqrs, July 24 1864, To [?] Sheldon(?)", operator
   signature R. O'Brien, 59 words, 7.50 p.m. Stamped **"Deciphered"** and **"Printed in War Records"**, pencilled
   "Vol 40 / Pt 3 / p 432" (the stamp's reference; not checked in the Official Records).
2. Verso: docket "R. O'Brien / Sheldon / July 24/64".
3. The Central Telegraph Office route worksheet: a 7-column grid with the plain text written in.

System: Union Army route cipher (word transposition by columns, with code words for names, times and dates, and
blind words). Transcription and route are in `transcription.md`. The route is up column 1, down 6, up 4, down 2,
up 3, down 5, up 7 (the worksheet's own column numbers), with a blind word after each column. It reproduces the
worksheet grid word for word except two cells (see transcription).

Plain text, from the worksheet: "Hdqrs. 9 a.m. July 24 ... Col. Biggs: Send me a list of all the boats in the dept.
capable of going through the canal and the Sound [?], their capacity in men and rations, and where they are. ...
Butler" (last row partly code, not read). The canal is presumably Dutch Gap; Biggs = Lt. Col. Herman Biggs, chief
quartermaster, Army of the James [?].

Printed text (checked 27 Oct 2026, OR Ser. I vol. 40 pt. 3, p. 432; archive.org `warofrebellion014003rootrich`;
index "Biggs, Herman - 432"), headed "SUNDAY, July 24, 1864. Lieutenant-Colonel BIGGS, Chief Quartermaster":

> Send me a list of all the boats in the department capable of going through the canal and the sound: also their
> capacity in men and rations and where they are. This is to be confidential. BENJ. F. BUTLER, Major-General,
> Commanding.

This matches the worksheet reading word for word and settles three open cells: the last grid row "to he confide"
= "[this is] to be confidential" (cipher "be" written "he"; "confide" a stem for "confidential"); "Sound" confirmed;
"pedlar" falls where the print has "also" [?] (a code word, or a blind word with "also" supplied by the clerk).
Still unread: "dont shall walrus knox" at the end of the last row (blind words and/or a signature code for
Butler [?]), the "unity i" cell, and the opening "Forward gam gobble" (route indicator [?]). The print omits the
"Hdqrs. 9 a.m." heading and "Col." for Biggs.

Method for this item: read from existing decipherment (contemporary worksheet; printed in the Official Records).

## Prior art (checked 27 Oct 2026)

- The RG 107 item is stamped "Printed in War Records": the War Records Office printed these telegrams in the
  *Official Records* (1880-1901). Most of RG 107 should be in print the same way.
- RG 108 holds fair copies (deciphered texts) of telegrams received; Grant's and Halleck's are largely printed in
  the *Official Records* and in *The Papers of Ulysses S. Grant* (Simon ed.). Not checked volume by volume.
- The Huntington Library's Thomas T. Eckert Papers hold the War Department telegraph-office ledgers and cipher books
  (received telegrams mostly decoded), transcribed by the "Decoding the Civil War" Zooniverse project. These hold
  the route books needed for anything still in cipher.
- Union route ciphers: Plum, *The Military Telegraph during the Civil War* (1882); Bates, *Lincoln in the Telegraph
  Office* (1907). Not on DECODE.

So, of the five series, RG 107 and RG 108 were read at the time and are largely in print; only the post-war RG 393
books may hold ciphertext without plain text (as 680 already records).

## Remaining gaps

- RG 107 628803 apart from the Butler item, RG 108 604437, RG 393 4486363/5081118/5131597: needs-physical-access
  (not digitised).
- Butler item: "dont shall walrus knox" (end of last row), "unity i", "dead", "pedlar" and the opening
  "Forward gam gobble": code, blind or indicator words, not read [?]; the rest of the row read from the OR print. Key material: the War Department route book in use in July 1864
  (Eckert papers, Huntington). Not checked.

## Escalation

- Siblings: Eckert ledgers at the Huntington (digitised on the Huntington digital library), the source of any route
  book; RG 107 M473/M504 telegram microfilm (plain copies) as cribs. Not checked.
- Print: OR Ser. I vol. 40 pt. 3 p. 432 checked 27 Oct 2026 (Butler text printed, matches); still to check: Simon's Grant Papers for RG 108.
- Access: ask NARA Textual Reference (DC) whether the RG 393 books carry plain text; order scans of 5081118
  (stated to be in cipher). Blocker is outside the project.
