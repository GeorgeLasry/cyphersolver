# Deboli → Stanisław August, cipher despatches from St Petersburg, 1791 (AGAD Zbiór Popielów 5; catalogue 420)

The 105 cipher despatches of 1791 were deciphered at the time. The decipherments are the items the AGAD inventory lists
as Deboli's clear Polish despatches of the same dates: a separate unit, **Zbiór Popielów 421** ("Korespondencja króla
z Debolim 1791"), which holds the cabinet's fair copies, each docketed "reçu le …". A sample of five despatches
(002, 032, 037, 039, 045; 3,082 cipher groups) was transcribed and aligned group by group against those decipherments.
The decipherment gives a value to 3,048 of the 3,082 groups (98.9%). The pairing was checked for the other years of
the series (catalogue 417–421): 1792 is confirmed, 1789–1790 are in the same code, and 1788 is in another code.

Outcome method: **read from existing decipherment** (the contemporary decipherment in ZbPop 421, transcribed and
checked against the cipher). The code tables in `align/` are rebuilt from the alignment and are partial.

## Sources

- **Cipher:** AGAD Warszawa, Zbiór Popielów (zesp. 12), sygn. 5 (old sygn. 303), "Deboli. 1791 (cyfry)". 105 items,
  4 Jan – 30 Dec 1791, k. 369. Letter list with image links: https://www.agad.gov.pl/inwentarze/ZbPop5.xml. Images:
  `http://agadd2.home.net.pl/metrykalia/12/album/5/slides/1_12_0_0_5_NNNN.jpg` (2480×3500; 463 images). Not
  committed. Every item is listed as "język: szyfr" with no note of a decipherment.
- **Decipherments:** AGAD Zbiór Popielów 421 (old sygn. 308), 115 items. List: https://www.agad.gov.pl/inwentarze/ZbPop421.xml.
  Images: `.../album/421/slides/1_12_0_0_421_NNNN.jpg`. The inventory calls them Deboli's letters, language Polish. Each
  is a fair copy headed "St Petersbourg ce … / reçu le …", with the despatch number, "Sire!", the text and "Deboli."
  The page layout copies the cipher original: half a page is left blank under "Sire!".
- **Keys** (not online): ZbPop 444 "Cyfra polska posłana do Petersburga Deboliemu" (8 III 1783); 451 "Chiffre François
  Nouveau envoyé a Monsieur Deboli" (1780); 453–454 the Cabinet's numbered keys 1772–1795. None has an album on agadd2
  or a letter list; the deciphered registers ZbPop 317/320 are not online either.

## Pairing of the two series (1791)

From 18 March both series carry the same despatch numbers (Nr 1, 2, 3, 3, 4 …, the duplicate "Nr 3" included). By
date, 99 of the 105 cipher items have a ZbPop 421 item of the same day. Four more pair by despatch number where one of
the two lists has a date slip:

| cipher item | ZbPop 421 item |
|---|---|
| 030 (Nr 8) | 010, dated 15 Apr |
| 091 (Nr 67) | 073, dated 9 Nov |
| 035, listed "05.29" (Nr 13) | 015, 29 Apr |
| 072 (Nr 49) | 054, listed under 2 Aug |

Only 014 (18 Feb) and 019 (8 Mar) have no partner found. The image counts of the pairs track each other: 443 cipher
images, 416 clear.

## The sample

| despatch | date | cipher (ZbPop 5) | decipherment (ZbPop 421) | code | groups | given a value by the decipherment |
|---|---|---|---|---|---|---|
| 002 | 7 Jan 1791 | k. 6–7, img 0008–0009 | item 090, k. 302–303, img 0380–0381 | A | 724 | 721 |
| 032 (Nr 10) | 22 Apr | k. 111–112, img 0158–0159 | k. 30–31, img 0040–0041 | A | 732 | 726 |
| 037 (Nr 15) | 6 May | k. 126, img 0178–0179 | k. 48, img 0060–0061 | B | 567 | 566 |
| 039 (Nr 17) | 13 May | k. 129, img 0182–0183 | k. 52, img 0065–0066 | B, then A | 417 | 409 + 2 indicators |
| 045 (Nr 23) | 31 May | k. 147, img 0206–0207 | k. 77–78, img 0098–0099 | A, then B | 642 | 622 + 2 indicators |
| total | | | | | 3,082 | 3,048 (98.9%) |

Files:
- `transcription/zbpop5_NNN.txt` (cipher) and `transcription/zbpop421_NNN_clear.txt` (decipherment). For 002 they are
  `zbpop5_001-003.txt` and `zbpop421_090_clear_1791-01-07.txt`.
- `transcription/groups_NNN.txt`: the bare groups, used for the counts above.
- `align/NNN.tsv`: one cipher group per line with its value.
- `align/pairs_all.tsv`: all five merged, with the code marked.
- `texts/NNN_en.md`: English translations.

Of the 3,082 groups, 34 have no place in the decipherment. About 660 values are syllable splits inside a spelled word
that the alignment could not fix exactly; they are marked [?]. In `scripts/consistency.py`, groups that occur more than
once carry their most common value in 83.3% of occurrences in code A (1,757 occurrences) and 84.4% in code B (762).
Most of the rest are split guesses and related forms (ie/nie, iak/jak, te/ta).

What the sample covers: the King's quarrel with the Sejm over the oath (Jan); Deboli's dislike of his office and
Spain's offer of a diversion in favour of Russia (Apr); Gálvez, Nassau and Ochakov (May); the Petersburg reaction to the
Constitution of 3 May 1791 and the Saxon succession (13 and 31 May). Summaries are in the profile, translations in `texts/`.

### Where the cipher and the decipherment differ

- 032: the cipher has "przyiechał" (1117 360 2107 1886) after "ze Srody na Czwartek"; the decipherment leaves it out.
- 037: the cipher has "na Morze Czarnym" (213 183 …); the decipherment has "się Czarnym".
- 039 A: the word order is "Niech będzie Bogu" in the cipher, "Niech Bogu będzie" in the decipherment. "cyfrowana cyfrą"
  is enciphered as "cy-cyfrowana" with no separate "cyfrą". In 039 B the decipherment adds "dałem" to "Ja tu się".
- 002: the decipherment adds "się" after "niedałbym", and the cipher's first "ani" in "ani smierdzi" is 1444, which is
  "tak" elsewhere.
- 002: the first transcription dropped a whole cipher line, 0009 right L09 ("skarżył na Komorę Połangowską, ktora
  wszystk-"). The alignment found the gap because the decipherment had text with no groups against it, and the line is
  now restored. Two clear-text misreadings in 002 were also corrected ("nareszcie", "żesmy").

## The system: two codes

Both are Polish syllabic codes (nomenclators) of about 2,200 groups and above. They have whole-word groups for common
words, titles and some names, syllables and single letters for the rest, and groups for punctuation. The clear frame
of every despatch is French: "Sire!" at the head, "Je suis avec le plus profond Respect … Deboli" with place and date
at the foot. The coded body is Polish.

**Code A** (January 1791; 001–003, 002, 032; 039 second paragraph; 045 to "dalsze rozkazy").
- Punctuation: 1786 = comma (the most frequent group), 1785 = semicolon, 1775 and 1782 = full stop, 1780/1781 = "/: :/".
- Words: 1944 = ani, 951 = od, 1578 = WKrM-, 21a 2152 = Deputacyi, 1353 = się, 1657 = y, 895 = nie, 1559 = w,
  782 = na, 948 = o, 1601 = że, 1433 = tu, 1654 = Xcia, 2148 = currentis, 1490 = by.
- Names spelled out: przysięgi = 1117 1353 212 (przy-się-gi; 1775 after it is the full stop); Stahremberg = 1307b 277 1258 686 1405 1255 207 (1307 = sta,
  also in przystaną and zastanie); Graff = 221 157; Helbig = 280 616 1907; Goltz = 213 616 1490.
- One-digit groups (8 = do, 5 = de, 3, 1, 9) are frequent.

**Code B** (037 throughout; 039 first paragraph; 045 last paragraph): the code of Deboli's 1792 Danzig letters (ZbPop 415
items 084, 086, transcribed with their clear copies in `transcription/zbpop415_1792_mixed.txt`).
- Each code-B run opens with a group above 3,000 (3283, 3285; 037 opens 3381z 3285; the Danzig runs open 3285). In 045
  the switch back reads "4000 1775 3285 1269", and in 039 the code-A paragraph opens with 4000. These look like
  code-change indicators.
- Punctuation: 1280 = comma, 1269/1276 = full stop, 1279 = semicolon, 1272 = colon.
- Words: 756 = się, 1053 = w, 1682 = do, 1072 = WKrM-, 1151 = y, 213 = na, 281 = nie, 1172 = z, 1175 = że,
  1500 = będzie, 2191 = ktory, 1694 1646 = Deputacyi (4×), 1879 40 1134 720 = Galwez (5×).
- 144 of the 279 group types in 037 also occur in the Danzig letters; only 39 also occur in 032.

The same number means different things in the two codes (893 = nic in A, tu in B). Code tables:
`align/code_table.tsv` (A, from 002 and 032), `align/code_table_037.tsv` (B, from 037) and
`align/code_table_039_045.tsv` (both, keyed by code). Flags mark conflicts. Small a/b/c marks under groups occur in
both codes. They may distinguish values: 1307a and 1307b both align to "sta", but bare 1307 aligns once to "stro" and
once to "Rossyi". Their purpose is not established.

An earlier note here said the Danzig code does not occur in 1791. That was drawn from January only and is wrong: code B
is in use by May 1791.

## Scribe and digits

The looped θ = 8; an open o = 0; b-shape = 6; s-shape = 5; q-shape = 9. From 002 on the 4 is often closed like a q:
"1990" in 032 is 1490 (= by), as the decipherment shows. Doubtful readings are listed in the `{notes}` lines of each
transcription, and the decipherment settled several of them (1884 → 1084, 2418 → 2 418, 2039 → 2059, 1079 → 1879).

## Other years of the series (catalogue 417–421)

The cipher unit and the scanned "clear" unit of each year were paired by date (`pairings_1788-1792.txt`), and one pair
per year was looked at side by side:

| year | cipher unit | clear unit | same-date pairs | spot check |
|---|---|---|---|---|
| 1788 (cat. 417) | ZbPop 428, 112 items | ZbPop 417 | 98 + 12 within 3 days | 4 Jan: a different code (1970 981 2345 992 211 …); clear copy docketed "reçu le 15". Pairing by date only |
| 1789 (cat. 418) | ZbPop 17, 109 | ZbPop 419 | 100 + 3 | 6 Jan: same code family as code A (1559 1681 1353 1775 686 948); clear copy "reçu le 17". Not matched word by word |
| 1790 (cat. 419) | ZbPop 4, 109 | ZbPop 420 | 98 + 2 | 1 Jun: "do Deputacyi" twice in the clear text, 21a 2152 (code A Deputacyi) twice on the cipher page at matching places. Likely |
| 1792 (cat. 421) | ZbPop 416, 80 | ZbPop 415 | 74 + 4 by number | No. 114, 20 Apr: cipher 951 1145a 1520 782 637 1578 = "Odpisuiąc na list WKrMości" (951 = od, 1578 = WKrM-, as in code A). Confirmed |

The January 1790 cipher items (001–009) have no partner in ZbPop 420. The 1783–1787 units (ZbPop 9, 10, 11, 2, 3) are
not scanned.

A parallel session worked on the same series as target `deboli1790` (catalogue 419, landed on main 27 Oct 2026), and
reached the same pairing independently. Its `targets/deboli1790/NOTES.md` adds four things:
- **1790:** the January 1790 decipherments are in ZbPop 417 (k. 353–386), which accounts for the unpaired January items.
- **1788:** an older code runs until spring, and the code of 1789–91 then starts with a leading group 4000. 4000 marks
  a change of code, as it does in the 1791 despatches here.
- **1792:** No. 95 (17 Feb) does not fit on its opening lines, so catalogue 421 stays open there. No. 114 (20 Apr)
  does fit (above).
- **WKrMci:** it reads the group as **1570**, where the transcription here has **1578**. The scribe writes two round
  figures, a small open o (as in 2107) and a barred loop (θ). This project reads the barred loop as 8 and the open o as
  0; that session reads the barred loop as 0. Both read the same repeat at the same place, so the pairing stands
  either way. Which figure is 0 is not settled; a key sheet (ZbPop 444, 453–454) would settle it.

## Remaining gaps

- Despatches other than the five of the sample (100 items, about 440 cipher images) - blocker: not-attempted; their
  decipherments exist in ZbPop 421 and the pairing is established, but the cipher was not transcribed or checked
  against them in this session.
- Despatch 001 (4 Jan, 2,202 groups transcribed) and 003 (first page transcribed) - blocker: not-attempted; the ZbPop
  421 item for 4 Jan (088, k. 297, 301) is short for 2,202 groups and was not checked.
- Despatches 014 (18 Feb) and 019 (8 Mar) - blocker: not-attempted; no ZbPop 421 partner found; items 003 and 039 of
  ZbPop 421 are undated and may be them.
- 34 groups of the sample have no place in the decipherment - blocker: open-codes; listed as "?" in `align/`.

## Escalation

- [x] siblings: the 1792 Danzig letters (ZbPop 415) have clear copies filed with them; their code is code B, which 1791 also uses.
- [x] clear-pages: done. This is how the decipherments were found (ZbPop 421).
- [x] known-keys: ZbPop 444/451/453/454 not online; not needed with the decipherments in hand.
- [x] print: Zielińska & Danilczyk edit only 1780–1782; Szczygielski 2014 cites only the King's clear letters (ZbPop 420); nothing for 1791 in print.
- [n/a] key-rebuild: the text comes from the contemporary decipherment; the partial code tables are a by-product.
- [n/a] retry: the doubtful cipher readings of the sample were resolved against the decipherment.

## Prior work

No decipherment of the 1791 cipher despatches is printed. The ZbPop 421 texts were already in historians' use, though:
- Rolnik 2025 (*Rocznik Filozoficzny Ignatianum* 31/3) quotes Deboli's 1790–92 despatches from ZbPop 415/420/421 and
  notes that this correspondence was in cipher. This comes from the deboli1790 notes; the article was not read here
  because the server refused the connection.
- Zielińska & Danilczyk print 1780–1782 from the cabinet's "deszyfry" (Archiwum Królestwa Polskiego 265).

What was missing was the link between these Polish texts and the cipher originals in ZbPop 5. The AGAD inventory lists
the originals as unread cipher and the decipherments as ordinary letters. The decipherments are contemporary (the
King's cabinet, 1791). This project found the link on 26 Oct 2026 while attempting the cipher; deboli1790 found it
independently on 27 Oct. The sample text comes from the decipherments.
