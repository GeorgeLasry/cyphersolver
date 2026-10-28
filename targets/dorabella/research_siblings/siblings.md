# Dorabella: sibling texts and Elgar's key table (research, 28 Oct 2026)

Images are in `downloads/` (sources listed at the end). Token notation is the one in `../ct.txt`.

## Orientation mapping (ct.txt letters)

The token letter gives the direction the arcs **open** (image up = north). The letters run clockwise from "opens right":

| ct | opens | back of arc points to | 1 / 2 / 3 arcs look like |
|----|-------|----------------------|--------------------------|
| A | E (right) | 180° | c, ε, Ɛ |
| B | SE | 135° | tilted ε, back to the upper left |
| C | S (down) | 90° | ∩, m |
| D | SW | 45° | tilted 3, back to the upper right |
| E | W (left) | 0° | ɔ, 3 |
| F | NW | 315° | tilted ω, back to the lower right |
| G | N (up) | 270° | u, w |
| H | NE | 225° | tilted ε, back to the lower left |

How it was checked:
- Task anchors: A2 = ε (opens right) and E3 = 3 (opens left).
- `histocrypt159.txt` ll. 107-112: the most common orientation has its back at 315° (that is F, 23 tokens). The rarest has its back at 0°, to the right (that is E, 4 tokens: E3 ×4 in ct.txt).
- Visual check on Schmeh's redrawn note (`downloads/schmeh_Dorabella-Hires.png`). Tokens 1-9, A2 E3 B2 A3 A1 C2 G1 A3 D1, read as ε 3 (tilted ε) Ɛ c m u Ɛ (tilted ɔ). C2 is an "m" opening down and G1 a "u" opening up.

## Elgar's notebook key table (Elgar Birthplace Museum notebook)

**Source.** Two facing pages of an exercise book at the Elgar Birthplace Museum (Lower Broadheath).
- Photograph: R. W. Padgett, https://enigmathemeunmasked.blogspot.com/2021/12/decoding-elgars-liszt-fragment-ciphers.html (`downloads/padgett_elgar_notebook_2pp.png`, 1682×1025).
- Tracing: Eric Sams, "Elgar's cipher table", Appendix (d), https://www.ericsams.org/index.php/on-music/essays/on-elgar/111-elgar-s-cipher-table (`downloads/sams_ciphertable3.jpg`, 714×519).

**Date and attribution.**
- Bauer, *Unsolved!* (2017) p. 127, dates the notebook to the 1920s.
- One of its messages is MARCO ELGAR. Marco was Elgar's spaniel, so the page is no earlier than his ownership of Marco (c. 1922-24).
- Thomas Ernst (comment 3 on Schmeh 2018) argues the pages are not by Elgar. That attribution is not settled.

**Layout.** Eight groups, ABC DEF GHIJ KLM NOP QRS TUVW XYZ. Within a group the letters take 1, 2 and 3 arcs. The groups take the eight orientations in the clockwise order above. I/J and U/V share a symbol.

| letter | A | B | C | D | E | F | G | H | I/J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| token | A1 | A2 | A3 | B1 | B2 | B3 | C1 | C2 | C3 | D1 | D2 | D3 |

| letter | N | O | P | Q | R | S | T | U/V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| token | E1 | E2 | E3 | F1 | F2 | F3 | G1 | G2 | G3 | H1 | H2 | H3 |

I checked this group by group on the photograph:
- ABC: c ε Ɛ.
- DEF: tilted, back to the upper left.
- GHI: ∩ m and a three-humped m.
- KLM: tilted 3, back to the upper right.
- NOP: ɔ 3 Ʒ.
- QRS: tilted ω, back to the lower right.
- TUW: u w ш.
- XYZ: tilted, back to the lower left.

Every enciphered line on the left page decrypts with this table (below), which confirms it. This is the same key `../elgar_layout.py` covers (the "notebook alphabet family"); Dorabella does not read with it.

## Sibling texts in the semicircle system

### 1. Notebook messages (key known, plaintext known)

These are encipherment exercises. I transcribed them by reading the shapes on the photograph and then checking them against the plaintext; every symbol agrees.

- Left page, line 4. MARCO ELGAR (10):
  `D3 A1 F2 A3 E2 | B2 D2 C1 A1 F2`
- Left page, line 5. A VERY OLD CYPHER (14):
  `A1 | G2 B2 F2 H2 | E2 D2 B1 | A3 H2 E3 C2 B2 F2`
- Left page, line 6. The same message in an angular, box-letter variant of the same 24 signs (14 tokens, same as line 5).
- Left page, line 7. DO YOU GO TO LONDON? (17):
  `B1 E2 | H2 E2 G2 | C1 E2 | G1 E2 | D2 E2 E1 B1 E2 E1 ?`
- Right page:
  - Three lines of the key alphabet written out in order. Line 3 is the complete A…Z run of 24 signs; lines 1-2 are shorter runs.
  - DO YOU GO TO LONDON TOMORROW? in plain capitals with tick marks, plus "90", "1234 4".
  - Clock-face/compass diagrams on the left page.

They are useful only as a key check. They are too short to serve as a test text, and they have no unknown plaintext.

### 2. The "Liszt fragment" (1886): 18 signs, unread

**Source.** Pencil marginalia beside music example No. 5 (Liszt, *Les Préludes*), p. 546 of the Crystal Palace "Nineteenth Saturday Concert" programme, 10 April 1886. A copy is at the Elgar Birthplace Museum (Kevin Jones, quoted by Pelling 2008).

**Images.**
- `downloads/padgett_liszt_programme_p546.png` (5974×9319, whole page).
- `downloads/padgett_liszt_fragment_strip.png` (7033×734, the line itself).
- Schmeh 2018 crops: `schmeh_Elgar-Liszt-fragment-1.jpg`, `schmeh_Elgar-Liszt-Fragment-2.jpg`.

**Length.** 18 signs followed by a long dash.

**Reading through the notebook key.** Padgett's table (`downloads/padgett_liszt_raw_reading_table.png`) reads the signs as `f h s t r s g e h i e t s h m u q x`. In tokens:

`B3 C2 F3 G1 F2 F3 C1 B2 C2 C3 B2 G1 F3 C2 D3 G2 F1 H1`

**My check against the 7033-px strip.**
- Agrees: tokens 2-6, 10, 12-14 and 16.
- Token 15 looks to me like an upright Ʒ, that is E3 (P), not D3 (M).
- Tokens 1, 7, 8, 9, 11, 17 and 18 are smudged: 7 is a blob, 8 a tall hook, 11 a hooked ɾ. They are uncertain in any reading.

**Claimed solutions.** Neither is accepted.
- Thorley (1977): "GETS YOU TO JOY, AND HYSTERIOUS". It has 26 letters for 18 signs, and Bauer rejects it.
- Packwood (*Musical Opinion*, July 2020, per Padgett): "STRING QUARTET IS WRY". It applies 13 different, unexplained Caesar shifts per letter.

The direct key reading is gibberish.

### 3. The "Cryptogram" card: about 18 signs, unread

**Source.** An undated card at the Elgar Birthplace Museum. Bauer (*Unsolved!* p. 127) says it is one of a series of cards giving Elgar's solution to the 1896 Pall Mall "Secrets in Cipher" challenge.

**Image.** Schmeh 2018, `downloads/schmeh_Elgar-card.png` (614×336). Only this low-resolution image is online.

**Contents.** The word "Cryptogram" in clear, about 18 semicircle signs in three short lines (2, 10 and 6), and above the middle line the row `1 4 -8, 5 ; · : x`.

**My tentative tokens (low confidence, from a 614-px image).**
- top: `A3 A1?`
- middle: `A3 B2 C2 D2? E3 F2 G2 H2 A2 A1`
- bottom: `A3 A3? ?(o-shape) B2? A2? A1?`

The middle line appears to step through the eight orientations in order (A…H, then A again). If so, it is a key or alphabet exercise, not a message. This needs a better image to confirm.

No solution has been claimed.

### 4. Other leads

- **Pall Mall "Secrets in Cipher" (1896).**
  - The Birthplace holds the four articles, the card series (item 3) and a wooden box painted with Elgar's solution.
  - The challenge was a Nihilist/Polybius-type cipher by J. Holt Schooling, according to Padgett's blog. It is not in the semicircle system.
  - No transcription of the cards is online.
- **Letters to Jaeger, and the Enigma.** I found no semicircle-cipher text. The Enigma "ciphers" online (Padgett's blog and others) are interpretive readings of the music, not ciphertexts.

## Image sources for the Dorabella note itself (part B)

- `downloads/schmeh_Dorabella-Hires.png` (614×138), from https://scienceblogs.de/klausis-krypto-kolumne/files/2018/07/Dorabella-Hires.png. This is a clean redrawing (vector-like strokes), not a scan, so do not use it for disputed strokes.
- No Elgar Birthplace / elgarfoundation image of the note was found online.
- Pelling's image (`ciphermysteries.com/wp-content/uploads/sites/6/2009/02/dorabella-cipher-image.gif`) is the same 433×161 image as Wikimedia's.
- I found no online report of a "dot on line 2" difference between editions.
  - Pelling (2013) bought the 1946 2nd edition. He reports more Enigma material in it, but no difference in the plate.
  - Commonly cited: a small dot after the 5th sign of line 3.
  - The 1949 3rd edition adds Appendix B. Whether the plate changed between editions is unverified.

## Download list

| file | px | source |
|---|---|---|
| padgett_elgar_notebook_2pp.png | 1682×1025 | enigmathemeunmasked.blogspot.com 2021/12 (photo of Birthplace notebook) |
| padgett_liszt_fragment_strip.png | 7033×734 | same post |
| padgett_liszt_programme_p546.png | 5974×9319 | same post |
| padgett_liszt_raw_reading_table.png | 1986×499 | same post (Ex. 5) |
| sams_ciphertable3.jpg | 714×519 | ericsams.org /images/ciphertable3.jpg (Appendix d tracing) |
| sams_ciphertable2.jpg | 471×333 | ericsams.org /images/ciphertable2.jpg (Sams's reconstructed table, Ex. 3) |
| schmeh_Elgar-card.png | 614×336 | scienceblogs.de/klausis-krypto-kolumne/files/2018/07/ |
| schmeh_Elgar-Liszt-fragment-1.jpg | 450×682 | same |
| schmeh_Elgar-Liszt-Fragment-2.jpg | 600×234 | same |
| schmeh_Dorabella-Hires.png | 614×138 | same (redrawn note) |
