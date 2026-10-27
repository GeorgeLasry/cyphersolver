# Poinsett → Monroe, Santiago de Chile, 20 Feb 1813 (Unsolved Catalogue no. 639)

Status: in progress

Catalogue 639. Joel Roberts Poinsett, US special agent for Buenos Aires, Chile and Peru, to James Monroe, Secretary
of State. Manning, *Diplomatic Correspondence ... concerning the Independence of the Latin-American Nations* vol. 2
(1925), doc. 442, pp. 896-898, prints the clear text with "(undeciphered cipher)" at ten places.

## 1. The document

- NARA RG 59, Despatches from Special Agents, vol. 3 = microfilm **M37 roll 2** (catalogue naId 213803757),
  **frames 0092-0094** (folios 37, 37v-38, 38v; old foliation 41 on 0093). Images are the catalogue JPEGs
  `https://catalog.archives.gov/medialz/dc-metro/rg-059/876974/M37-02/M37-02-NNNN.jpg` (not committed).
- Frame 0092 (f. 37r, the opening) is filmed almost black with heavy show-through; even after background
  flattening only the clear words can be made out, not the code groups of passage P0 ("You will have seen a series
  of ..."). Frames 0093-0094 are good.
- Passages P1-P9 (`transcription.tsv`, one row per written line, with the clear context from Manning): **437 code
  groups, 256 distinct** (`ciphertext_1813.txt`, measured with `docs/_check_profile.py --measure --digits`).
  Manning's ten "(undeciphered cipher)" places = P0 + P1-P9 (Manning splits P2/P3 around "and dictated by the first").

## 2. The system

A numbered code of about 1,600 groups (highest group read 1589; one doubtful 1800), comma-separated. Common words
are single groups (1355 the, 1397 of, 522 and, 1348 in, 1215 / 1315 a, 1554 to), longer words are spelled from
syllable groups (409 1175 1179 765 pro-te-ti-on; 1314 413 1166 per-ma-nent). Values are not in alphabetical order
(1348 in, 1355 the, 1385 pre, 1397 of, 1399 foot, 1407 po, 1413 at): a two-part code. A small circle over a group
adds -s (971 country, 971° countries; 1116° in "sloops"); a cross under a group and a caret also occur (1115+,
694+, 264^, 961^), meaning not yet established.

It is **not** any US code table in the repo: the Department code of 1803-40 (`targets/jqa`, the = 1385), Armstrong's
THE=972, Pinckney's legation code, the 1788 legation code, Jefferson 1787, Mountflorence 1801, nor Sumter's Rio code
of 1813 (M121 vol. 1A frames 0035-0039: the = 798, of = 1399, and = 1242). `shift_test.py` also tried every constant
shift (and mod 1600/1700) of the first five against the 1813 groups: best z = 4.3 among ~9,000 settings for the JQA
table, decodes are junk; no signal. Gallatin to Madison, 15 Aug 1810 (Founders, Madison 03-02-02-0600), says
Sumter "ought to have Mr Poinsett's cypher", so a Sumter-Poinsett copy may have existed, but Sumter's despatches to
Washington are in his own code.

## 3. The key so far: the 14 June 1814 sibling

Poinsett → Monroe, Buenos Aires 14 June 1814 (M37 roll 2 **frame 0098**, ff. 38v-39; duplicate at frames 0099-0100,
f. 40-41) is in the same code (the = 1355, of = 1397, "of this country" = 1397 891 971 in both letters) and has a
**clerk's decode written over the groups** for its two coded passages:

- A (after "a mission which has originated from the"): "prevailing opinion of a rupture between G. Britain & Spain
  [in] the present Government of this Country will endeavour to obtain the protection of the latter at any price
  such is however the disposition of the people that the English never can gain a permanent footing in these
  countries".
- B (after "sent a prize to Rio de Janeiro"): "their trade is exposed to a just retaliation of this prince with
  seldom more than a single frigate to protect ... eighteen feet ... it two sloops of war better than a frigate
  being the utmost a ship should draw".

`key_1814.tsv` holds the 88 values aligned from these (D = word written over the group, S = syllable split of a
decoded word, ours). Group readings were checked against the duplicate (it gives 80 for "such", 618 for "ju-", and
the four groups of "endeavour"). The right ends of some lines on 0098 run into the gutter; the duplicate fills them
for passage A, not yet for the last lines of B.

## 4. The 1813 letter with that key

`decode.py` → `decode_1813.txt`: **158 of 437 groups (0.362) have a value**. The decode is fragments, not yet
sentences, e.g. P1 "No dependance can be placed on the [1436] of the people the [486][1095] and li[218][1095] of
this country ..."; P4 "... of this govern-ment [901] the ..."; P6 "... re-[12]-pro-te-ti-on ..."; P7 "... in the
[428] of ... the govern-ment". No sentence reads yet, so nothing is claimed as read.

## Remaining gaps
- P0, f. 37r (frame 0092), about three lines of groups - blocker: illegible; the microfilm frame is nearly black;
  needs a new scan of the original (NARA RG 59) or the 1813 duplicate if one survives
- 279 of 437 groups in P1-P9 (211 of 256 distinct values) - blocker: no-key-material for most; the only decoded
  sibling found covers 88 values (45 of the 256 distinct 1813 groups); Poinsett's own papers with his other ciphered reports (HSP, Poinsett Papers
  vol. 4, Gilpin collection) are not online
- the same groups - blocker: open-codes until the context pass below has been made

## Escalation
- [x] siblings: M37 roll 2 frames 0091-0102 opened; 14 June 1814 (0098, duplicate 0100) is in the same code with a
  clerk's decode, used for the key; 0462 (Jacob Lewis) is another code; Sumter's Rio code (M121) is not this one
- [x] clear-pages: Manning prints the clear text only; no clear copy of the cipher passages found
- [x] known-keys: JQA/Department 1803-40, Armstrong THE=972, Pinckney, 1788 legation, Jefferson 1787,
  Mountflorence 1801, Sumter 1813 tried directly and under shifts; none fits
- [ ] print: Manning checked (no decode); Weber 1979 not online; HSP calendar (1941) full view on HathiTrust
  mdp.39015034759822 but behind a bot check, to be searched by hand for 'cipher'
- [x] key-rebuild: context pass made 27 Oct; only 'Lima' (249 413, twice in P4) cross-checks; no new values, the
  unknown groups occur once or twice in contexts that do not fix them
- [ ] siblings (2): Lowry, La Guaira 1810-12 (M84 roll 1, frames ~0019-0079), had a cypher for Shaler and Gelston and
  sent the Department one ciphered letter (Manning vol. 2, Lowry to Graham 30 Nov 1816); if it is the 1810 agents'
  code with a decode it adds key; sampled at thumbnail scale only
- [ ] retry: after the context pass

## 5. Next steps

1. Context pass: fill recurring groups only where two or more occurrences agree; grade them I.
2. Find more decoded material in this code: Weber, *United States Diplomatic Codes and Ciphers* (1979); HSP Poinsett
   Papers vol. 4 (1811-14 reports "parts in cipher", per the HSP list filmed at M37 roll 2 frames 20-22); the
   Department's Buenos Aires consular file (M70) for any of his letters that were not returned in 1818.
3. A better image of f. 37r (frame 0092).

Prior art (27 Oct 2026): Manning 1925 has no decode; web search found none; not in the repo before this folder.
