# King Carlos I to Queen Amélie, three code telegrams of 1903 (ANTT PT/TT/CAM/M12, catalogue 401)

Status: contributed by WAINUT (27 Oct 2026). Two of the three telegrams are read in full from decodes made at the
time and filed with them; the third (47 items) has no decode and is not read. The code is not rebuilt. The site page
and the ledger rows are left to the maintainer.

Catalogue 401. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents;
the transcriptions were made with a vision-capable language model and checked against the DigitArq images. The
telegram texts and m0058's decode were re-read independently. The second decode (the card m0060) was found later,
while checking the contact sheets; a reviewing agent re-read it against the image once more and agrees.

## 1. The unit

- **Source.** Arquivo Nacional Torre do Tombo, *Documentos de D. Carlos, D. Amélia e D. Manuel II*, maço 12,
  PT/TT/CAM/M12, [DigitArq record](https://digitarq.arquivos.pt/documentDetails/a58a28dda5844d2e8c9f61e2a2567e99),
  61 images. The record says "not accessible", but the images download through DigitArq's JSON backend
  (`/api/rdigital/<docId>` for the file list, `/api/rdigital/dissemination?fileId=<id>` for an image).
- **What is coded.** The letters (m0001-m0053, French, from King Carlos to "Ma chère Amélie", 1904-1905) are in
  clear. Only three telegrams are coded: m0054 (cover m0055), m0056 (back m0057) and m0058 (back m0059). The card
  m0060 is the decode of m0054. The archive description counts 2 telegrams and 1 card.

## 2. The telegrams

| image | route and date | items | decode of the time | state |
|---|---|---|---|---|
| m0054 | Lisbon -> Paris (Hotel Bristol), 12 May 1903 | 14 groups among clear French words | card m0060 (Hotel Bristol, Paris) | read |
| m0056 | Lisbon -> Tlemcen, 4 Mar 1903, to the Queen "bord yacht Amélie, Oran" | 47 (44 groups, three "03") | none found | not read |
| m0058 | undated (spring 1903?), after a letter sent to Malta | 13 (12 groups and "03") | in ink on the same form | read |

- **m0054.** Printed strips. Header `SS PARIS LISBOA 3428 33 12 12/40- HS`. The form itself says that the first
  number after the place of origin is the serial number and the second the taxed words, so the origin is LISBOA
  (no. 3428, 33 words, day 12, 12:40). Stamp `CENTRAL PARIS 12 MAI 03`. The cover strip reads
  "REINE PORTUGAL HOTEL BRISTOL PARIS" (read on a reduced image). The first pass had this as Paris -> Lisbon,
  1903/04: corrected.
- **m0056.** By hand on a French form: "Pour Tlemcen de Lisbonne No 1728 Mots 86 Dépôt le 4/3 1903 à 8h30",
  address "Reine Amélie Portugal bord yacht Amélie Oran Tlemcen", stamp TLEMCEN 5 3 03 ORAN. The sender is not
  named; the telegram is filed with the King's papers.
- **m0058.** Code groups and the decode in ink on a blank French form; no office data.

Transcriptions: `m0054_transcription.txt`, `m0056_transcription.txt`, `m0058_transcription.txt`. The writer of
m0056 and m0058 makes 5 like a long s. In m0056 the fourth group of line 3 was read 19338 in one reading and
59338 in the other; it is marked `59338?`.

## 3. The readings

**m0054** (decode on m0060, `m0054_contemporary.txt`; group by group in `m0054_decryption.txt`). The French words are
in clear on the telegram; the 14 groups carry a Portuguese sentence:

> Merci dépêche. Ici tout et tous très bien. Podes dar, mas só depois de ter combinado com Rosa e ella ter fallado
> com Governo francez. Petits baisent main. T'embrasse. Carlos.

English: "Thanks for your telegram. Here everything and everyone very well. You may give [it], but only after having
arranged it with Rosa and after she has spoken with the French Government. The little ones kiss your hand. I embrace
you. Carlos." The object of "dar" is not said, and "ella" has no clear antecedent. Rosa is probably Tomás de Sousa
Rosa, then Portuguese minister in Paris [our identification, not checked]. Edward VII had visited Paris on 1-4 May
1903; whether the telegram has to do with that is not known.

The card proves the decode: it repeats the telegram's clear words in order and puts the Portuguese sentence where
the groups stand. The two repeated groups fix part of the alignment: 38564 (groups 5 and 11) and 58215 (groups 7 and
13) stand two places apart, as "ter ... com" does twice in the decode ("ter combinado com", "ter fallado com"). So
38564 = ter, 58215 = com, 29955 = combinado, 49452 = fallado [all inferred from the repeat]. The decoder's hyphens
("Po-des", "Ros-a") suggest that the code has syllables as well as words. 38564 < 58215 although "com" comes before
"ter" in the alphabet, so this code is not alphabetical (unlike Sabugosa's, `targets/sabugosa1910`).

**m0058** (decode on the form, `m0058_contemporary.txt`, `m0058_decryption.txt`):

> Ici tous et tout bien. T'ai écrit à Malte. T'embrasse, et les petits salue tous. Carlos.

English: "Here everyone and everything well. [I] have written to you at Malta. [I] embrace you, and the little ones
greet everyone. Carlos." "salue" is singular as written; "[I] embrace you and the little ones; greet everyone [from
me]" is also possible. The 12 groups and "03" do not map one to one onto the 15 words, so the split is not known.
Malta fits the Queen's Mediterranean cruise of spring 1903.

**m0056** is not read. It shares 58215 and 91518 with m0054 and 10734, 43554 and 78341 with m0058; only 58215 (com)
has a value.

## 4. Controls (`python groups.py`, output in `groups_output.txt`)

- Shared groups: random telegrams of 12 and 44 five-digit groups share two or more groups in 0 of 20,000 trials. The
  shared groups mean the three telegrams use one code.
- m0058: the decode has 60 letters and the 12 groups have 60 digits. Letter for digit, the mapping has 37 conflicts;
  1000 shuffled digit orders give 38.1 on average (minimum 32). No better than chance, so the 60 = 60 is a
  coincidence and the system is a code, not a letter cipher.

## 5. Prior work

- No printed decipherment of these telegrams was found (one web search). The decodes themselves are in the archive,
  so the readings are not new; what is new here is the transcription, the dates and directions, and the link
  between m0054 and m0060.
- Related pointer only: A. H. Norris, "A letter from Queen Amelia to her son King Manuel II", BHS Portugal Report 4
  (1977) p. 56 (https://www.bhsportugal.org/library/articles/a-letter-from-queen-amelia-to-her-son-king-manuel-ii):
  the Queen put certain words of a letter in cipher. A different document.

## Corrections to catalogue entry 401

- Date "1903-1906": the coded telegrams are of 1903 (4 Mar, 12 May, and one undated); the clear letters run to 1905.
- Language "Portuguese": the letters and two telegrams are in French; the coded sentence of m0054 is Portuguese.
- Status: two decodes of the time are in the unit (m0058 and the card m0060); one telegram (m0056) is without one.
- The DigitArq record's "not accessible" does not stop the images from downloading.

## Remaining gaps

- m0056, all 47 items (Lisbon -> Tlemcen, 4 Mar 1903) - blocker: no-key-material. No decode in M12; the code is
  not alphabetical, so the few values from m0054 predict nothing; the codebook was not found.
- The word-by-word split of m0054 groups 1-4 and 8-10, and of m0058 - blocker: too-short. The decodes give the
  words but not which group carries which.

## Escalation

- [x] siblings: the three telegrams share groups; m0054's decode is on the card m0060; the other M12 images are clear
  letters. Other CAM units and the Arquivo da Casa Real were not searched: they may hold a decode of m0056 or the codebook
- [x] clear-pages: m0054's clear French frames the coded sentence; m0058's decode is on the form
- [x] known-keys: Sabugosa's code of the same weeks (targets/sabugosa1910) is a different, alphabetical code; not this one
- [x] print: one web search; no edition of these telegrams found
- [x] key-rebuild: only four positions fixed (repeats in m0054); m0058 does not align one to one
- [x] retry: the four values fixed by m0054's repeats (ter, com, combinado, fallado) looked up in m0056 and m0058;
  only 58215 (com) recurs, once in m0056, and that alone reads nothing

## Files

- `m0054_transcription.txt`, `m0054_contemporary.txt` (card m0060), `m0054_decryption.txt`, `m0054_reading.md`, `m0054_en.md`
- `m0056_transcription.txt`, `m0056_decryption.txt` (no values)
- `m0058_transcription.txt`, `m0058_contemporary.txt`, `m0058_decryption.txt`, `m0058_reading.md`, `m0058_en.md`
- `groups.py`, `groups_output.txt`: counts, repeats, shared groups, controls (standard library)
