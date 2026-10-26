# The Hereditary Prince's cipher letters to Wilhelmina, Berlin 1795-97 (KHA A32-630)

Status: in progress

Koninklijk Huisarchief, The Hague, A32 Wilhelmina van Pruisen, inv. A32-630, "Anciens déchiffrements sur les
premières années de notre séjour en Angleterre", 1795-1797, 1 pak, 387 scans on the Koninklijke Verzamelingen site
(image ids in `ids.txt`, scan number = line number; images in `img/`, git-ignored, fetched from
`https://cms.koninklijkeverzamelingen.nl/api/images/rendition/<id>/width-1600/`).

Found in the Nationaal Archief / KHA sweep (research/nationaal_archief/README.md, lead K5), 25 Oct 2026.

## What the file is

Letters of Willem Frederik, the Hereditary Prince (later King William I), from Berlin to his mother Wilhelmina in
England, October 1795 to 1797, in French. The cipher passages use the Euler word-list code already rebuilt in part
for target hereditary1796 (DECODE R2237/R2239): a numbered list of words; a group is a whole entry (underlined),
letters p, q... of entry N (`N,p,q`), entry N without its first k letters (`k)N`) or without its last k (`N^k`).

Three kinds of page (survey of 25 Oct): originals with cipher runs among clear French, often with an interlinear
decipherment; pages of solid cipher; and Wilhelmina's clear write-ups headed "Chiffre de Guillaume du <date>".
These were read at the time. The aim here is the code itself: pair each cipher page with its write-up, rebuild the
full list, and use it on unread letters in the same system (first R2236, hereditary1796).

## Prior work

- Contemporary decipherments in the file itself (interlinear and Wilhelmina's copies).
- Colenbrander, *Gedenkstukken* II (1906) prints Hereditary Prince letters of 1795-96 from the Huisarchief
  (hereditary1796 found no. 752 there). Some of these letters may be printed; to check.
- Karl de Leeuw, "Johann Friedrich Euler ...", *Cryptologia* 25 (2001), 256-274, describes the cipher (not seen).

## Page index (25 Oct)

`index_a.tsv` (scans 1-194) and `index_b.tsv` (195-387): kind, decipherment present, date, first words.
- 1795-96 (scans 1-194): 65 interlined pages (contemporary decipherment above each run), 47 write-ups, genuine
  solid cipher with facing write-up for 7 Mar 1796 (80-82), 12 Mar 1796 (87-88 = R2239's letter), 18 Mar 1796
  (94), 26 Jul 1796 (166-167), and the memoir notes (31-32 / 34-35, = R2237's observations).
- From 7 June 1796 most letters carry **dummy number pages over lemon-juice text** ("les chiffres qui suivent ne
  disent rien et ne servent qu'a masquer"): scans 128, 130, 134, 138, 140, 148, 149, 156, 183. Leave them out.
- 1797 (scans 195-387): 21 interlined, 37 mixed, 58 write-ups. A larger list (entries to about 720, '0' as
  separator; 4-digit groups from 29 Apr 1797) and an older "chiffre ordinaire" in short passages.
- Undeciphered: 264, 266, 272, 328, 333, 365; partly: 324, 372, 374.

## R2236 is in this file

DECODE R2236 (catalogued under Prins Willem V inv. 337, "Non-decrypted") is the same text as A32-630 "Copie No. 1"
(scans 269-270; same line breaks, Dutch with numbers to about 391), "Copia No. 2 (a) 20 Mars 1797" and "(b)"
(264, 272), and the "Copia" page of numbers to about 2800 (89). No decipherment of them was found in the file;
Wilhelmina's precis of the 23 Mar 1797 letter (274-275) is headed "pour autant qu'il m'a ete possible de le
dechiffrer". The numbers run past the 1795-96 list, so R2236 belongs with the 1797 system.

## The 1795-96 list (25 Oct)

Agents transcribed the 65 interlined pages as runs (`pairs_a.txt`, `pairs_b.txt`: PT, CT, AL lines). The groups
were struck through after deciphering, and the agents' alignments often dropped the marks; a strict table build
(`merge.py` -> `all_assign.txt`) gives thousands of conflicts. `vote.py` takes a majority vote per letter position
instead: 245 entries (1-249; 112, 134, 153, 164 never seen), 145 with no gap and at least 80% agreement. It is the
same list as R2237's (10 angleterre, 11 berlin, 15 france, 23 prusse, 162 elgin, 169 haugwitz), now with the names:
151 kalitscheff, 155 bourdeaux, 157 caillard, 163 finckenstein, 168 hardenberg, 171 hohenlohe, 177 lucchesini,
183 dompteda, 184 pichegru, 185 pitt, 189 rietveld, 196 tollius, 223 ligne de demarcation, 248 westphalie.
`key_euler.tsv` is the working list (vote, with hand choices marked). Entries 1-9 look like single letters.

## Remaining gaps

- R2236 (Copie No. 1, No. 2, scan 89): not read; blocker none yet: needs the 1797 list.
- The 1797 list: not rebuilt; the 21 interlined and the deciphered mixed 1797 pages are the source.
- About 100 entries of the 1795-96 list are still gapped or below 80% agreement.

## Escalation

1. Transcribe the 1797 interlined and mixed pages (index_b.tsv) with the same brief, asking the agents to copy
   the full group form in AL; rebuild the 1797 list by vote.
2. Decode R2236 Copie No. 1/No. 2 with it (Dutch; check with nl-modern / nl-1600); then the undeciphered 1797
   letters (264, 266, 272, 328, 333, 365).
3. Re-read low-agreement 1795-96 entries at full size where a group recurs.

## Log

- 25 Oct 2026: target opened; 387 scans fetched; page index; R2236 found in the file; 65 interlined 1795-96 pages
  transcribed; list rebuilt by vote (key_euler.tsv). Next: the 1797 list.
