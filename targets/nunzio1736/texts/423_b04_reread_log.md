# Re-reading log, Spagna 423/1-11 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b04)

## Starting point

Reading audit (22 Oct): 423/3 read (one sentence); the ten others "decoded, not read": texts/reading_423-*.txt was
Lasry's running text with 46 nomenclator values from key_extra.txt, with open groups and ??? in almost every sentence.

## 1. Is there a text already?

- DECODE images: all 26 pages of R26 and R179-R188 fetched with the project cookie (research/reading_audit/b04_fetch.py;
  saved in the session scratchpad only). No interlinear, margin or slip decipherment on any page. The clear writing in
  the left margins of R184 f. 388r and R188 f. 510r is the facing leaf of other (clear) letters bound in the volume,
  not a decipherment.
- Neighbouring records: R179-R188 and R26 are the whole series; nothing else in DECODE for Spagna 423.
- Print: a web search for the 1736 ciphers to Guiccioli (Molina, Montemar, the arrolamenti, Trastevere, Velletri)
  found no edition. The Secretariat's minutes would be in the Archivio della Nunziatura di Madrid (ASV), not digitised.
  Blocker for a contemporary text: physical access.
- So the readings rest on the figures and the key.

## 2. Transcription

- Lasry's segmented decipherment (decode/keep/lasry_decipherment_S423.txt, parsed by corpus.py into seq.json) leaves
  out whole runs: 423/5 has 137 of the 177 non-null tokens of the page (the sentence "mai ciò seguisse, dovrà ella
  chieder tempo" and "replicata istanza le sarà duopo" are missing). About 20% of the corpus is missing from it.
- research/reading_audit/b04_seg.py re-segments the DECODE transcriptions themselves (Matt F 2015-16 for R179-R188;
  NiLan 2017 for R26, fetched now as decode/keep/DOC_R26_D1635_1635.txt; its "?" is the figure 2, as the transcriber
  notes) with Lasry's rules: 7 null outside groups, 1xxx nomenclator, otherwise pairs. Per-letter output:
  texts/423-<n>_decode_b04.txt (pairs and labels, then the running decode).
- Fifteen unclear figures resolved (texts/423_b04_corrections.tsv): struck runs on R183 f. 384r and R184 f. 388v
  (with the interlinear correction 44 05 64, "inviato"), the caret-inserted 37 on f. 388v, the 1 of group 1829
  (Regni), a stray 8 on f. 388r, blotted figures on R187 ff. 492r-v and R188 f. 511r (all seen on the images), and three
  in R187 resolved by sense only (noted as such).

## 3. Key

All corrections were tested on every occurrence in the eleven letters (texts/b04_key_additions.txt, with contexts):

- Two-digit: 25 = che (Lasry ";": "non pare che vi sia", "un torrente che minaccia", "an-che"); 30 = ta (Lasry to:
  data, condotta, ostilità, autorità; 64 stays to); 69 = z (Lasry t: violenza, zelo, amarezza, istanze, circostanze);
  93 = nel (Lasry quel: nell'udire, nello stesso Mons. Molina, nella sua lettera, nello scorso ordinario).
- Nomenclator values of key_extra.txt replaced: 1234 = qual (was Ministr/Nunzi: "al quale si erano fatte", "i nostri
  Ministri, i quali possono"); 1205 = com (was che: "e gli comunichi", "come Vescovo", "commercio"); 1241 = tant (was
  molt: "sintanto che", "fratanto", "quel tanto che"); 1210 = esser (was restar: "sicuri di esser egli stato", "per
  essersi giudicato"). 1224 is molt.
- 34 new firm values and about 30 probable ones ([?x] in the readings). Open after the session: about 60 groups,
  mostly single occurrences (date numerals, Molina's title 1513 a 1382, Montemar's 1855/1843, 1449, 1664, 1844 ...).
  No key material exists outside these letters (Lasry's key has no nomenclator).
- Unexplained pairs that recur at sentence ends (27, 37, 47, 67, 97): stop signs; 21, 41, 58, 00, 57, 07 have no value.

## 4. Readings

Built sentence by sentence (texts/423-<n>_reading.md, English _en.md), then aligned word by word with the decode
(research/reading_audit/b04_align.py, a character alignment of each reading against its running decode): every
unbracketed word is carried by figures or by a nomenclator value; the alignment flagged and the readings now bracket
"ed" (e è), "all'" (a l'), "l'ecclesiastica", "[è]" in 423/10 and 423/11, "de'" (di) in 423/9. Supplied endings of
nomenclator stems (Brev[e], qual[e], nomin[a]to) are bracketed; the cipher's "a la" for "della/alla" is printed as written.

_check_reading.py on the reading bodies (abbreviations V.S., N.S., Mons., S. Sede de-dotted so they do not cut
sentences; every [?x] counted as a hole): clean-sentence share and hole rate

| letter | before (audit) | clean share | hole rate | state |
|---|---|---|---|---|
| 423/1 | decoded, not read | 0.31 | 0.175 | decoded, not read (attempt filed) |
| 423/2 | decoded, not read | 0.70 | 0.111 | read (B) |
| 423/4 | decoded, not read | 0.70 | 0.101 | read (B) |
| 423/5 | decoded, not read | 0.20* | 0.191 | read (B) |
| 423/6 | decoded, not read | 0.64 | 0.105 | read (B) |
| 423/7 | decoded, not read | 0.63 | 0.125 | read (B) |
| 423/8 | decoded, not read | 0.71 | 0.121 | read (B) |
| 423/9 | decoded, not read | 0.47 | 0.125 | read (B) |
| 423/10 | decoded, not read | 0.65 | 0.107 | read (B) |
| 423/11 | decoded, not read | 0.47 | 0.156 | read (B) |

*423/5 is four sentences whose holes are all probable values ([?g]iungesse, [?se], [?dovrà], d[?u]opo); every
sentence builds and translates.

## 5. Not done / failures

- 423/1 (R26): NiLan's transcription is weaker; about a dozen runs do not decode ("Vescov[o] [..]", "di esiggere [..]",
  "la f[..]a a Donghi", "si fe' [..] a negar"), clean share 0.31. Not re-transcribed from the five images this
  session: workable, not an outside blocker.
- "[?stra]nieri" (423/6): the figures read da-ranieri; checked on the image, the transcription is right.
- "[..] danno" (423/9), "le la mede [..] consaputi libri" (423/11), "ben [..]giata" (423/11): checked in the decode,
  not on the images.
