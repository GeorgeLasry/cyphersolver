# JQA at St Petersburg: the despatches are NOT in the Armstrong code; his own code rebuilt, and Ford's
# "not decyphered" passage of No. 88 (25 June 1812) read

Page split, 14 Oct 2026 (one key, one entry): this entry was shown on the combined page `legation.html` with Erving's
24 March 1807 letter, which is in a different code (Pinckney's legation code, the = 1651). The two now have their own
pages: this one is `docs/jqa.html`; Erving's letter, a different cipher with its own page, is `docs/erving1807.html`
(folder `../erving1807/`). `legation.html` is a stub pointing to both.

Status: read (22 Sept 2026, third pass). No. 88, measured with `measure.py`: **380 of 390 code groups read as sense
(0.974)**; the nine lines Ford left out 133/133 (1.000), the remainder 247/257 (0.961). 382/390 groups have a value;
362/390 (0.928) without the grade-I values. Still open: 7 groups cut by the microfilm gutter (needs the original)
and 3 single code groups (1508, 1185, 570).
The second pass (earlier on 22 Sept) stood at 0.910; see section 5.

## 1. The premise, checked

- Madison editors on Armstrong's letters (Founders Madison/02-10-02-0369, 02-12-02-0197): code "also used by John
  Quincy Adams at St. Petersburg and by Jacob Lewis at Saint-Domingue; key not found but substantially reconstructed by
  the editors". On JQA to Madison, 7 Jan 1811 (Founders 03-03-02-0121): "a code provided by the State Department to
  John Armstrong in France and to both William Short and Adams" (citing Ford, Writings of JQA 3:328).
- Ford 3:327-28 (Smith's instructions, 1809) says JQA's own cypher was **the London minister's** (Pinkney's), and JQA
  was to *obtain a copy of Armstrong's* at Paris to correspond with him. JQA acknowledges receiving "the copy of General
  Armstrong's cypher" (Ford 3:~370). So JQA held both; the despatches to Washington use the other one.
- NARA M35 reel 3 (naId 188725601): every coded despatch checked uses a code with **the = 1385, of = 1576, that = 1384,
  and = 668, I = 1401**. THE=972 (Armstrong) has the = 972, of = 1354. The 592-entry Armstrong table renders these
  pages as noise (`../armstrong/decode972.py`). Reel 2 frame 0155 (1810) is in the same JQA code. The Founders note on
  the 7 Jan 1811 letter to Madison (a private letter, not a despatch) was not checked against its manuscript (Forbes
  collection, not online).

## 2. JQA's code rebuilt

Frames: NARA M35 reel 3, downloaded by `dl.py` from the catalogue manifest (`objects_M35_03.json` in the main
checkout's `targets/jqa/`; images `img03/`, git-ignored, not in the repo). `strip.py` and `crop.py` cut crops for reading.

**Structure.** A numbered syllabary: syllables, word-parts and common words, about 1,600 numbers; 1-100 mostly whole
words (13 observation, 16 Emperor, 29 United States, 37 together, 44 negotiation, 71 commerce, 78 President). Values
climb alphabetically only inside short runs (1384 that, 1385 the, 1388 then, 1391 there, 1392 these, 1393 they,
1394 think, 1399 this; 1592 on, 1594 one, 1595 ong, 1597 only), then the run breaks, so the alphabetical slot brackets
a value only where the neighbours are in order (`slots.py`). A superscript o after a group adds -s; a mark under a
group changes it (doubled letter, -ed, or a different word: 1107 paper, 1107+ well). A few groups carry two values in
the sources (508 rect and ear; 1570 of and occurr; 1173 when and would).

**Sources of the table** (all merged by `consolidate.py` into `code_table.tsv`, 1,166 numbers after the third pass: 431 H, 393 C, 324 M,
18 I; disagreements in `code_conflicts.txt`, hand decisions in `overrides.tsv`):

| File | What | Pairs |
|---|---|---|
| `pairs_jqa.txt` | clerk's interlinear decode, frames 0206 (No. 88) and 0189 (18 Sept) | ~400 lines, 262 H |
| `clerk_0182.tsv` | No. 80, 29 Feb 1812, interlinear decode, single leaf | 91 H, 19 M |
| `clerk_0184_0185.tsv` | frames 0184 (left, right top) and 0185 (both leaves), 1812, interlinear | 582 H, 518 M |
| `clerk_0190_etc.tsv` | 0190 (both leaves, continues 0189), 0183 right, 0194 right, 0198 right | 614 H, 327 M |
| `clerk_0048.tsv` | 0048 left, top block (1811), interlinear | 9 H, 5 M |
| `ford_pairs.tsv`, `_A`, `_B` | 1811 coded blocks transcribed from the film (`codes_ford*.txt`, 39 blocks: frames 0005, 0010, 0014, 0036, 0063, 0066, 0071, 0084-85, 0090-93, 0103, 0112, 0126, 0132) aligned with the plaintext Ford printed from the Department's decipherments (Writings vol. 4, OCR `ford_writingsofjohnqu04wort.txt`) by `align.py` and checked by eye | 589 C, 270 M |
| `slot_inferences.tsv` | values for No. 88 groups from slot + sense only | 9 I |

Grades: H the clerk's decode over the group; C fixed by Ford's printed plaintext between known neighbours; M the split
or the digit is a judgement; I slot and sense only. Transcription note: in this hand 5 and 6, 7 and 9, 0/6/8 are easily
confused; three No. 88 readings were corrected on 22 Sept from zoomed crops (gap line 1 168 not 158, line 2 1426 not
1425, line 4 302 not 502), and the underlined 1102 at the foot of frame 0206 left is a catchword, not a group.

## 3. No. 88, 25 June 1812 (the day after Napoleon crossed the Niemen): Ford 4:357 "[Nine lines of this paragraph
## not decyphered.]"

Triplicate, M35 reel 3 frame 0206 (the clerk's decode stops exactly where Ford's gap starts). Groups: `gap88.txt`
(133 groups). `python render.py gap88.txt` gives every group a value; 129 read as sense. Reading ([ ] = grade I,
{ } = valued but not sense):

> ... and expectation. But the [journ-ey] itself of the Emperor Alexander to Wilna was in opposition to the
> Chan-ce-ll-or and adv-ice, and if his active influence had not been im-pa-ir-ed before it, it can scarcely
> fail to have been affected by his illness immediately after his arrival [thither], which was undoubtedly an
> apo-ple-ct-ic stroke. Since then he has had a second and a more severe one. In the German Gazettes even his
> death has been announced; but that was a mistake. At all events it is scarcely possible that he should remain much
> longer in the department of foreign affairs.

"He" is Count Rumyantsev (Romanzoff), Chancellor and foreign minister, who had gone to Wilna with Alexander. The
passage reports that the journey to Wilna went against the Chancellor's advice (83 opposition, now grade C from
No. 73), his apoplectic stroke soon after arriving, a second and worse one since, a false report of his death in the
German papers, and JQA's judgment that he cannot long stay at the foreign ministry. That fits the known history (a
stroke in 1812 that cost him his hearing; retired 1814). It differs on timing from standard accounts (Britannica,
Wikipedia), which tie the stroke to the news of the Niemen crossing on 24 June: JQA, writing on 25 June before that
news could reach St Petersburg, places the first stroke soon after Rumyantsev reached Wilna and a second before
25 June. Ford printed none of this. JQA's diary for September 1812 records Romanzoff speaking of two strokes of
apoplexy suffered with the Emperor at Wilna.

im-pa-ir-ed: the groups on the page are 1424 [1102] 1112 1433 520. JQA's catchword at the foot of the left leaf is
1102 (pa, C 9x), the group he meant to begin the next page with, and in No. 83 (0190L5) he writes un-im-pa-ir-ed as
1477 1424 1102 1435 520 (1435 ir, C 3x). The 1112 1433 at the top of the right leaf are his own copying slips
(one digit each) for 1102 1435; read as intended, *impaired* (grade C by the No. 83 parallel).

## 4. The "remainder of letter ... undecyphered" (Ford 4:358)

Frame **0207** (left leaf): 13 lines of code, then clear sentences (Manifestos of both parties expected; Peace with
Turkey signed a third time; "It is not General Kutuzoff but Count Rostopchin who is appointed Governor, civil and
Military, of Moscow"), then 5 more lines. Groups: `rem88.txt` (257 groups, 7 with digits lost in the gutter).
249 valued, 247 read as sense:

> If this proposition has in any form been disclosed to the Russian government, it was certainly neither unreasonable
> nor im-[mod(erate)] nor inconsistent with a system rigorously and [in]-[fl]-ex-[ib]-ly de-fen-sive (underlined), to
> meet it with a proposition for the e-va-cu-ation of Prussia by the French troops as {1508} [pre]-liminary to
> negotiation. But the very point upon which the ambassador manifested the most sensibility in speaking of Prince
> Kurakin's last note was that it held out a proposition with which it would be dishonourable in France to comply. He
> {1185} it as a demonstration that the Emperor Alexander had determined not to [negotiate] at all - it {tol} he
> [sa]-id - such a proposal as France had never thought of making to Russia even after the [bat]-tle of Fri-ed-la-nd.
> [clear text] ... an army of reserve is forming there, and it is [...] probab-le that if great success on the, on the
> side of the French should mark the commencement of the war, the Emperor Napoleon will at-[tem]-p-t to pene-t-rate
> directly to that centre of the em-[pire] than [along] the sho-res of the Baltic.

The ambassador is Lauriston, the French ambassador; Kurakin's note is the Russian ambassador's demand at Paris for the
evacuation of Prussia (April 1812), which Napoleon treated as a declaration of war. "Even after the battle of
Friedland" (June 1807, before Tilsit): France had never proposed evacuating Prussia even when Russia was beaten.

## 5. Third pass (22 Sept 2026): 0.910 -> 0.974

New sources: the clerk's interlinear decodes on 0047, 0048 (rest), 0210-0211 and 0247 (`clerk_0047.tsv`,
`clerk_0048b.tsv`, `clerk_0210_0211.tsv`, `clerk_0247.tsv`, 560 pairs; `clerk_notes_pages2.md`), and coded blocks of
eight 1811-1812 despatches aligned with Ford vol. 4 (`codes_ford1812*.txt`, `ford1812_pairs*.tsv`, 1,926 pairs;
No. 95 against the Department's clear copy on 0230-0232; `ford1812_notes.md`). `consolidate.py` now reads them; the
table has 1,166 numbers (with `ford1812_pairs_b.tsv`: Nos. 71, 72, 74, 75, 81; `ford1812b_notes.md`).

What moved, with evidence:

| No. 88 | was | now | evidence |
|---|---|---|---|
| gap88 l.3-4 `1424 [cw 1102] 1112 1433 520` | {im-pas-sion-ed} | im-pa-ir-ed, *impaired* (C) | catchword 1102 pa; No. 83 un-im-pa-ir-ed = 1477 1424 1102 1435 520 (0190L5): 1112 1433 are JQA's slips for 1102 1435 |
| gap88 l.2 `1025 1016 1457 908` | Chan-ce-{last}-or | Chan-ce-ll-or (C) | No. 73 (0165, Ford 4:256) writes the same four groups, 1457 with the doubling mark = ll |
| gap88 l.5 first group | 492 use | **792** by (H) | re-read on 0206R: an open hook, not this hand's looped 4 |
| rem88 l.4 `142x 350 289 1403 897` | few-ex-table-ly | [in]-[fl]-ex-[ib]-ly, *inflexibly* (I) | slots 1401 I < 1403 < 1404 ic and 347 fit < 350 < 352; 350 has a hook under the 0; the single Ford alignments (few, fi, table, cal) disagree with each other, and the 0194 "1403" (cal-cu-late) has a blotted 4, probably 1003 cal |
| rem88 l.5 | e-va-{1081}-ation | **1061** cu (C): e-va-cu-ation | the blurred digit is a 6 (as in 864, 1576); 1061 cu in Ford 0005 and cal-cu-late (0194); slot 1060 ct < 1061 < 1062 cur |
| rem88 l.11 `426 699 1535+` | ne-{at}-{al} | [negotiate] at all | 1535 with the doubling mark = all; 426 slot 423 need < 426 < 428 nei (I) |
| rem88 l.13 `1309 888 1576 996 520 1453 416` | {...} long of {...}-ed la-nd | [bat]-**588** tle(d) of Fri-ed-la-nd | 996 = fri (C, No. 95 fri-end-ship x2, a fri-end x2); 1453 la, 416 nd (Fin-la-nd); the second group is 588 (the 5 has its top bar), 588 = tled (set-tled, C); 1309 slot 1308 bas < 1309 < 1310 be (I) |
| rem88 l.16 `220 586 1384 1416` | {proper le the if} | probab-le that if | 220 = probab (clerk 0047R19 'it is probab-le that', 0190L6, 0190R26; the lone 0184R11 'proper' is the outlier); the third group is 1384 (4 over 5) |
| rem88 l.18-19 `539 927 1383 1540 1385 1097 748` | em-{927} the {ambass} the side-{res} | em-[pire] than [along] the sho-res of the Baltic | 927 context only (I); 1540 slot 1537 alliance < 1538 ally < 1540 (I); 1383 than and 1097 sho are digits JQA overwrote (5/3, 9->7; M); 748 res (M) |

## Verification 5, 23 Oct 2026

Plain-bar check (English 1812; the gap entry had been listed as French): both No. 88 entries were scored on decryption
files with hyphenated syllables and group tables. Readings written out with words joined and grade-I words marked:
`texts/no88_gap_reading.md` (plain 0.9, explicit 1.0) and `texts/no88_remainder_reading.md` (plain 0.688, explicit
0.812). Both keep read.

## Remaining gaps

- rem88 seven groups with lost digits (142x, 21x, 15xx, 11xx, 10xx, 55x, 13xx) - blocker: needs-physical-access; cut by the binding gutter on the microfilm of frame 0207 (every line end); the original and duplicate of No. 88 are not on reel 3, and JQA's letterbook copy (MHS) is not online. Context fixes most of them (in-, pre-, sa-id, tem-p-t) but they are counted unread
- rem88 l.5 1508 before [pre]-liminary - blocker: no-key-material; 1508 (le/bable, M) does not fit 'as a pre-'; no other occurrence in the decoded pairs
- rem88 l.9 1185 ('He [took?] it as a demonstration') - blocker: no-key-material; no occurrence in any decoded frame or Ford block read
- rem88 l.11 570 ('it tol he said'): valued (tol, C) but does not read; the image shows 570, not 500 (was) - blocker: no-key-material

## Escalation

- [x] siblings: clerk interlinear decodes on 0047, 0048, 0182-0185, 0189, 0190, 0194R, 0198R, 0206, 0210-0211, 0247 (`clerk_*.tsv`); 0056-57 are a clear decyphered copy, 0228-0233 No. 95 code only
- [x] clear-pages: Ford vol. 4 decipherments aligned for 39 coded 1811 blocks and 8 despatches of Oct 1811-Sept 1812, No. 95 against the Department's clear copy on 0230-0232 (`ford_pairs*.tsv`, `ford1812_pairs*.tsv`)
- [x] known-keys: Armstrong's THE=972 table tested and ruled out (18 Sept); Pinkney's London code not found in print or online
- [x] print: Ford 4:357-358 prints both passages as not decyphered; no other printed reading found; JQA's diary (Primary Source Cooperative) confirms the two strokes at Wilna
- [x] key-rebuild: table rebuilt to 1,166 numbers (`consolidate.py` + `overrides.tsv`, every override with its reason); alphabetical-slot bracketing (`slots.py`, `slot_inferences.tsv`, grade I)
- [x] retry: No. 88 re-read against the image a third time: 792 (not 492), 1061 (not 1081), 588 (not 888), 1384 (not 1385) corrected; 570 confirmed; 1097 and 1383 read as JQA's own overwritten digits

## Next

- The original or duplicate of No. 88 (not on M35 reel 3) or JQA's letterbook copy at the MHS would restore the seven
  gutter-cut groups; with them the letter would be at about 98%.
- 1185, 1508, 748 each need one more occurrence: the 1812 blocks of Nos. 77, 78, 81 and the remaining lines of No. 85
  (0196L 12-23) are not yet aligned.

## Contribution by WAINUT (27 Oct 2026)

Contributed by WAINUT (https://github.com/WAINUTAI), a Dutch AI company; the work was done with AI language-model
agents, and every group was checked by eye against the NARA frames, twice, the second time independently. This
section adds two later texts in the same code: catalogue 637 (Appleton, Cadiz 1823) and 638 (Everett, Madrid 1825).
They are filed here because the repository keeps one key per entry, and both use this folder's code (the = 1385,
of = 1576, that = 1384, and = 668, I = 1401). The text above, `code_table.tsv` and the other files are unchanged;
the new files are in `wainut/`, and `profile.json` gains two documents, their two `outcome.texts` entries, a credit
and dated solution steps (existing entries untouched). The code was evidently still in use at the Madrid legation
in 1823-1825, when Adams was Secretary of State.

### Catalogue 637: John J. Appleton to John Quincy Adams, Cadiz, 6 Aug 1823 (closed 8 Aug)

- **Source.** NARA RG 59, Despatches from US Ministers to Spain vol. 22, microfilm M31 reel 24
  ([naId 188609418](https://catalog.archives.gov/id/188609418)), frame 0134, foot of the left page
  ([frame](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-024/M31-024-0134.jpg)).
  Manning, *Diplomatic Correspondence of the United States concerning the Independence of the Latin-American Nations*
  III (1925), doc. 1124, p. 2041, prints the 18 groups (with OCR noise) and "[no decodification]".
- **Context.** The finance minister Yandiola tells Appleton that the constitutional government has sent two
  commissioners to England to liquidate an account; "the success of their mission depended upon its remaining
  secret -- that if this liquidation was effected it would produce" [code]. The two blanks in the clear sentence
  before ("an account which they had with ---- amounting to ----") are plain dashes in the MS, not code.
- **Transcription** (`wainut/appleton1823_transcription.txt`): `1088 648<> 1576 794<> 1384 1453 347 1372 500 /
  192: 668 1384 169 1244 1501 1110 1426 1290`. All 18 numbers agree with Manning. Diamonds after 648 and 794
  (plural); a small raised double dot after 192, meaning unclear.
- **Decryption** (`wainut/appleton1823_decryption.txt`, `python wainut/decode.py appleton1823_transcription.txt`):
  16 of 18 groups have a table value; 14 of them give the English directly: "... of [794] that La-fit-te was [192]
  and that he had a part in England".
- **Groups read from the slot.** The table's numbers run alphabetically in short stretches: among H-graded entries
  3 or fewer apart, 226 of 261 neighbouring pairs are in order. So a slot is evidence, not proof.
  - 648 = **millions**. The table has April (M, 1x), but `code_conflicts.txt` (line 177) records a clerk decode of
    648 as "millions"/"million" on 0210R3, and the slot is 646 might < 648 < 649 min. April fits neither slot nor
    sense.
  - 1088 = **seven [?]**. The table has sa (H, but a single clerk reading, in con-ver-sa-tions), which does not fit
    the slot 1087 set < 1088 < 1091 sever. Seven fits; so do settle, seventh and seventy.
  - 794 = **dollars [?]**. No value in the table; the slot 792 by < 794 < 796 don and the sense fit.
  - 192: **open**. Slot 191 hon < 192 < 193 hon/honor, 194 hood: a hon- word (honest, honour, honourable ...).
- **Reading** (`wainut/appleton1823_reading.md`): "(... it would produce) [?seven] millions of [?dollars]; that
  Lafitte was [192], and that he had a part in England." Lafitte is probably the Paris banker Jacques Laffitte; that
  identification is an interpretation and was not checked.
- **Controls** (`python wainut/decode.py appleton1823_transcription.txt --controls`): the true decode has a
  function-word rate of 0.50; every group shifted by 1, 2, 3, 7, 50 or 100 either way gives 0.00-0.17 and syllable
  salad ("9th min offer ? the ri ? ted e hon to the"); three random permutations of the table give 0.00-0.06. Hits
  alone prove little: 18 random numbers in 1-1600 hit a table value 9.2 times on average, because the table is
  dense. What separates the true reading is the grammar and the syllable chain la-fit-te.
- **Second coded leaf, not transcribed.** Frame 0150 of the same reel is a separate leaf headed "with Mr Appleton's
  Despatch of 6 & 8th Aug. 1823": about 10 lines of numbers in the same code (1385, 1576 and 1290 occur), then plain
  text signed by Appleton; frames 0140 and 0143 are its dockets. Manning does not print it. The film is badly
  degraded by bleed-through.
- **Prior work.** Manning prints the passage undecoded. One web search found no decipherment.

### Catalogue 638: Alexander H. Everett to Henry Clay, Madrid, 25 Sep 1825

- **Source.** NARA RG 59, Despatches from US Ministers to Spain vol. 25, microfilm M31 reel 27
  ([naId 188610348](https://catalog.archives.gov/id/188610348)), enclosure "Notes of a Conversation of Mr. Everett
  with Mr. Zea" (Francisco Zea Bermúdez, the foreign minister). The cipher is on frames 0119 (MS pp. 14-15,
  [frame](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-027/M31-027-0119.jpg)), 0120 (right
  page, MS p. 17, after "End",
  [frame](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-027/M31-027-0120.jpg)) and 0121 (left
  page, MS p. 18, [frame](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M31/M31-027/M31-027-0121.jpg)).
- **What Manning has.** Manning III doc. 1134, p. 2062 (the OCR of the page header reads "2002"), is headed
  "[extract]" and prints only passage A, as "[Here follow six lines in cipher, without decodification.]", after
  "...an interference of Providence." His extract ends at "in reply to his remarks."; passages B and C, after "End",
  are neither printed nor mentioned.
- **Transcription** (`wainut/everett1825_transcription.txt`): **355 groups** in three passages (A 8 lines, B 14,
  C 12). The catalogue estimate of "about 445 groups" is too high. There is no interlinear decipherment on these
  pages. Marks: a lozenge after a group = -s (plural or possessive), like the folder's superscript o; a caret after
  it = -ed; a cross under 1535 = all (al, all, als by the next letter, as in this folder) and under 1167 = well; a
  tick under a group truncates it (108 comply -> compl in ac-compl-ish; 563 time -> tim in le-gi-tim-).
- **Decryption** (`wainut/everett1825_decryption.txt`): 347 of 355 groups have a value in `code_table.tsv`, applied
  without any change. The raw output already reads as English with syllables to join.
- **Reading** (`wainut/everett1825_reading.md`). Everett did not argue at length with Zea, being satisfied that his
  remarks did not express his real sentiments but were "merely a language imposed upon him at present by particular
  circumstances" (A). The foreign ministers at Madrid agree: they think Zea privately well disposed to recognition of
  the new American states, so "there is a strong power somewhere acting in a [125] direction". Zea dare not risk his
  place, since a declaration for recognition would give his rivals the means to overthrow him, and he may think it
  good policy to dissemble (B-C). The influence of the Emperor Alexander is said to be directed against recognition.
  Everett has not yet spoken with the Russian minister, d'Oubril. Some ministers ascribe Russia's policy to a [258]
  of opposition to England rather than to the regard for legitimacy that the Emperor gives as his ostensible motive
  (C). The rivals are not named in the cipher. Pierre d'Oubril was the Russian minister at Madrid in 1825.
- **Values read against the table or from context** (marked [?] in the reading unless said otherwise):
  - 666 = Zea [?] (twice, "Mr. Z[ea]" and "Mr. Z[ea]'s"). The table has March (M, 1x). With the tick, March cannot
    give Zea, so either the table value or the reading is wrong.
  - 601 = Mr. (three times, each before a name). The table has (sympt)oms (M, 1x). Not marked, since it holds at
    every occurrence.
  - 70: necessary in A (the table's second value). In B, "well [850^] to the [70] of recognition" fits neither
    commerce nor necessary: read [?cause].
  - 1072 = satis- (twice: "well satisfied", "if he is satisfied") against the table's see (M, 1x). Not marked.
  - Context words: [?enter] (1293 tent), [?pretty] (211, no value, + 776 ty), [?tenor] (only 908 or is written),
    [?language] (1501 a 1454 ri 1238 gu 1524 age), [?imposed] (1424 im 1155^ port), [?expressed] (297 ex 520 ed,
    followed by 1504 observed), [?disposed] (850^, no value), [?shewing] (1094 she 1184 wi 483 new),
    [?liberality] (880 li 1325 bers 1543 against), [?head] (171 hea), [?enable] (only 545 en before "them"),
    [?overthrow] (929 over 557 those/ough), [?dissemble] (845 dis 541 insure), [?sacred] (1068 sa 1055 policy),
    [?d'Oubril] (809 de 926 ou 1354 1421 ill), [?legitimacy] (1512, no value), [?ostensible] (917, no value).
  - Second values of the table confirmed here: 257 = speci (more e-speci-ally), 1525 = al (person-al), 1599 = ood
    (under-st-ood), 727 = rather (rather than), 1201 = g (re-co-g-ni-tion); 1479 riv (grade I) fits riv-al-s.
  - 450 (ink, M) follows "think" both times and is left out of the reading as redundant.
  - Line C10 "1290 727 1383" is written over; legible as read, but heavier.
- **Open groups:** 125, 126, 211, 258, 850, 917, 1354, 1512 (no value in the table). The reading suggests contrary,
  express, pret-, spirit, dispos-, os-, br, acy, all from context only.
- **Controls** (`python wainut/decode.py everett1825_transcription.txt --controls`): the true decode has a
  function-word rate of 0.37; every group shifted by 1, 2, 3, 7, 50 or 100 either way gives 0.02-0.12, three random
  table permutations 0.03-0.05. Shuffling the order keeps the same words, so it needs a word-order model: an
  independent check with a character-trigram model trained on the English of Manning vol. III (doc. 1134 left out)
  scored the true decode -2.129, wrong keys -2.50 to -2.70, and 200 shuffled orders mean -2.399, best -2.351. That
  check needs Manning's text from archive.org and is not included.
- **Prior work.** Manning prints passage A undecoded and omits B and C. The plaintext phrases do not occur in
  Manning vol. III. One web search found no decipherment. Not checked: a decipherment on another copy, in a separate
  State Department file, or in the Clay Papers.

### Proposed table changes (not applied)

`code_table.tsv` was used as it is. Proposals, with the evidence above: 648 millions (clerk 0210R3, slot) instead of
April; 1088 seven [?] (slot) instead of sa; 794 dollar(s) [?] (slot; no value now); 601 Mr. (3x) instead of
(sympt)oms; 666 Zea [?] instead of March; 1072 satis (2x) instead of see. Second values confirmed in 1825: 70
necessary, 257 speci, 1525 al, 1599 ood, 727 rather.

### Remaining gaps (catalogue 637 and 638)

- 637: group 192 (hon-) and the slot-only values of 1088 and 794 - blocker: no-key-material; each occurs once in
  these texts and has no clerk decode.
- 637: the second coded leaf on frame 0150 - blocker: illegible; bleed-through on the microfilm, the original volume
  would allow a transcription.
- 638: groups 125, 126, 211, 258, 850, 917, 1354, 1512 and the context-only words listed above - blocker:
  no-key-material; Everett's other cipher despatches of 1825-1826 on reel 27 are the next source of occurrences.

### Escalation (catalogue 637 and 638)

- [x] siblings: both texts read with this folder's table; Appleton's second leaf (frame 0150) found
- [x] clear-pages: the clear text around each passage used for the sense; Manning's extracts checked
- [x] known-keys: this folder's table applies directly to both texts (the = 1385, of = 1576)
- [x] print: Manning III docs. 1124 and 1134 print the code undecoded
- [x] key-rebuild: slot inferences for 648, 1088, 794, 192 with the alphabetical-run check
- [ ] retry: other Appleton and Everett despatches on M31 reels 24-27 may repeat the open groups

### Files (in `wainut/`)

- `appleton1823_transcription.txt`, `appleton1823_decryption.txt`, `appleton1823_reading.md`
- `everett1825_transcription.txt`, `everett1825_decryption.txt`, `everett1825_reading.md`
- `decode.py`: applies `../code_table.tsv`; `--controls` runs the wrong-key controls (standard library)
