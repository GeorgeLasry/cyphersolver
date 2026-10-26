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

## The 1797 pages and R2236 (25 Oct, second pass)

Agents transcribed the 21 deciphered 1797-type pages (scans 195-278: `pairs97_a.txt`, `pairs97_b.txt`, with the
brief `AGENT_BRIEF_1797.md`; CT faithful with marks, PT = the faint text between the lines, AL mostly empty).

- Scans 195-202 (Sept 1796 - Jan 1797) still use the 1795-96 list, with dark-ink decipherments.
- From 20 Jan 1797 the numbers run to about 800 with frequent `0`. Tests (`key_euler.tsv` decoding of groups
  with N <= 249 against the faint text): 1796 lines 82% of decoded groups found in their own line's text vs 21%
  in another line's; 1797 lines 6% vs 4%. So the 1797 numbers are not in the 1795-96 list.
- The 1797 numbers are diffuse: 545 distinct big numbers in 1,585 items (1795-96: 233 in 11,012); the top number
  is 1% of items. Either a large homophonic list or dummy numbers over lemon-juice text. For dummies: on 31 Jan
  1797 the only dark-ink decipherment reads the first groups as "rien que du clair"; on pp. 217/220/278 the faint
  text runs on below the last number line over blank paper; repeated number pairs (5 cases) never sit under
  repeated text. Against: Wilhelmina's precis of 23 Mar 1797 (scans 274-275) is headed "pour autant qu'il m'a ete
  possible de le dechiffrer" and ends "Ou 93 le chiffre n'est pas distinct": she worked from numbers. Settled
  on 25 Oct (see below).
- **Settled: the faint text is not a decipherment.** (1) Capacity: on 243/249/261, 50 of 52 lines carry more
  plaintext letters than their groups can yield under the list's rules even counting each bare entry as a
  10-letter word (243 line 6: 48 letters over six position groups worth at most 11 letters). Plaintext letters per
  item: 1795-96 interlined 3.1 (median), Sept 1796 - Jan 1797 dark ink 4.7, 1797 faint text 6.9. (2) The clear
  words among the numbers ("a moins que l'on ne dicte", "Quant a l'article du", "certain si l'on voudra", "soit
  dans celle ci soit dans", "& c'est pour cette raison que", "est une preuve si non ... dumoins") never occur in
  the faint text; with the numbers they make the frame of a separate cover letter. (3) The faint text runs on past
  the last number line (217, 220, 278). So from 20 Jan 1797 the numbered letters are covers and the message is in
  sympathetic ink (developed, brown), as the June 1796 letters say outright. The 1797 numbers cannot rebuild a
  list. Wilhelmina's "Chiffre de Guillaume" write-ups of 1797 copy the ink text.
- **R2236 Copie No. 2** (20 Mar 1797, scans 264/272) is in this 1797 system (groups to 722, `0`, underlined
  digits). Not transcribed yet.
- **R2236 Copie No. 1** (scans 269-270) is a different code: plain numbers 1-391 among clear Dutch, no marks;
  317 tokens, 154 distinct, small numbers 1-19 the most frequent. Transcribed in `r2236_copie1.txt`. Decoded with
  the 1795-96 list (big number + small positions) it gives nonsense, so it is not that list either. Its clear
  Dutch carries the frame of the argument ("op losse gronden ... Echter schynt het als of ... met een van beiden
  ... tot een bestendig ... De minister ... stellig aan ... zoo deze mogenheid ... zou het gevolg daar van
  natuurlyk zyn ... dat onze ... Het is reeds algemeen bekend dat ... zich niet zullen ... hoegenaamd geene ...
  Dus het eenigste middel om ... Dit is, om door ... brengen: hier toe ... het geen by wyze van ... zoude kunnen
  geschieden"). Repeats: 215 2 6 (twice), 390 217 8 5 2 (twice), 149 332 61, 55 319 250, 223 65 226, 220 43 19 8,
  42 9 7 62 147 300.

## R2236 Copie No. 1: print search and ciphertext-only assessment (25 Oct)

- **Print.** All 1,166 pages of Colenbrander, *Gedenkstukken* II (1795-1798) were downloaded as text from the Huygens
  retroboeken service (`pages.json?source=2` gives each page's `html_url`; kept in `gs2/`, git-ignored) and searched
  for the clear frame: "losse gronden", "stellig aan", "deze mogenheid", "hoegenaamd geen" have no hit; "een van
  beiden", "eenigste middel", "kunnen geschieden", "bestendig" hit only unrelated pages (p. 913 is an anonymous
  memorandum). The letter is not printed there.
- **Code.** 317 numbers, 154 types, 94 singletons, 32 types seen 3+ times; numbers 1-19 are 35% of tokens and
  follow a big number 77 times out of 112. Ten repeated sequences of 3-6 numbers ("155 7 204 3 9 7",
  "42 9 7 62 147 300", "390 217 8 5 2", "209 371 12 76", "220 43 19 8", "55 319 250", "149 332 61", "105 223 323",
  "313 35 17", "249 198 382"). Between clear words a cipher stretch of about ten numbers stands for a clause of
  several words ("zoo deze mogenheid [10] zou het gevolg"), so the unit is a word or syllable, not a letter; the
  small numbers behave like frequent short words or endings placed at the head of the list, so the list is not
  one-part alphabetical. A word/syllable code of about 400 entries seen 317 times, two-thirds of its types once:
  too little for a ciphertext-only solution. Not attempted further; blocker: no key material and too short.

## Wilhelmina to her son, 1801 (KHA A35-178, 26 Oct)

The KHA K9 survey flagged 11 pages of A35-178 (Wilhelmina's letters to the future Willem I, Jan-Jun 1801, London and
Hampton Court). Checked at full size (`letters1801.txt`; images in `img1801/`, git-ignored): 3 pages are clear
letters (131711, 131718, 131739); 8 carry short cipher passages in the **same Euler word list**, with Wilhelmina's own
marks. Glosses agree with `key_euler.tsv`: 62 Guillaume, 66 le ministere, 98 votre, 118 dispositions, 133 on dit,
137 l'Empereur, 185 Pitt, 196 Tollius; new values 230 Pays, 390 230 116 Pays de Nassau, 37 32 Duc d'York,
167.5.3.7 137 38 Wilhelmine Princesse d'Orange. Six passages are glossed in full or in part (131652, 131659, 131677,
131740, 131746, 131771). Wilhelmina writes on 13 Feb 1801 that "vos dechiffremens" took her so long she could not
write at length: her son wrote to her in the same list.

Unglossed: 131704 (Feb/Mar 1801, about 55 groups, the second passage headed "correctif au precedent chiffre") and
131715 (April 1801, about 50 groups). Decoded with `key_euler.tsv` they give fragments ("intentions",
"defavorables", "est ecrit sans", "votre instructions", "troupes", "opinion") between broken groups, and numbers
above the 1795-96 range (360, 700, 906, 1107): the list was extended by 1801, and the agent's mark readings are a
first pass. Not read.

Re-read 26 Oct (`r131704_reread.txt`, first passage of 131704, 21 groups): with the 1795-96 values the cuts do not
fit the entries: 8)169 would drop 8 letters of the 8-letter "haugwitz", 10)151^11 would drop 21 of the 11-letter
"kalitscheff", 2)238^4 6 of the 4-letter "rhin"; the rest gives "lettre ... mi ... ttre ci pres tou inte rreue b len
lamosella". So in 1801 these numbers stand for other, longer entries (or the marks follow other rules); the eight
glossed 1801 passages give too few values to rebuild that list. Left unread.

## Remaining gaps

- R2236 Copie No. 1: not read; its own Dutch word/syllable code; no key, no decipherment in A32-630, not in
  Colenbrander GS II; too short for ciphertext-only (317 tokens, 154 types). Blocker: no key material, too short.
- R2236 Copie No. 2 and scan 89: not transcribed; in the 1797 number system, which has no aligned plaintext
  anywhere in the file (the 1797 faint texts are separate ink letters). Blocker: no key material. Copie No. 2 has no
  clear words and no faint text, unlike the cover letters, so it may be genuine cipher; the 23 Mar 1797 letter
  (266) and Wilhelmina's partial precis (274-275) are the only lead, a paraphrase not a crib.
- About 100 entries of the 1795-96 list are still gapped or below 80% agreement.

- 1801 passages 131704 and 131715 (about 105 groups) - blocker: no-key-material; re-read at full size, the cuts do not fit the 1795-96 entries (8)169, 10)151^11), numbers beyond the list (360, 700, 906, 1105); the 1801 list is a revision not rebuildable from eight short glossed passages

## Escalation

1. Done: 1797 pages transcribed and the faint text shown to be separate ink letters; no 1797 list from them.
   Remaining lead for Copie No. 2: transcribe scan 266 (23 Mar 1797) and align it loosely with the precis 274-275
   for names (Callitschef, Elgin, Peterbourg, Bale, Deux-Ponts, Brandebourg).
2. Done: Copie No. 1 searched in Colenbrander GS II (not printed) and assessed ciphertext-only (too short). A key
   could be in KHA A31 (Willem V) or A35 (Willem I) cipher papers; the Hereditary Prince's Dutch code of 1797 is not
   in the KHA search results so far.
3. Re-read low-agreement 1795-96 entries at full size where a group recurs.

## Log

- 25 Oct 2026: target opened; 387 scans fetched; page index; R2236 found in the file; 65 interlined 1795-96 pages
  transcribed; list rebuilt by vote (key_euler.tsv). Later: 1797 pages transcribed; old list does not apply;
  R2236 Copie No. 1 transcribed, a separate Dutch code; Copie No. 2 in the 1797 system. 1797 faint texts
  shown to be sympathetic ink. Copie No. 1 not in GS II; too short for CT-only; DECODE R2236 queued.
