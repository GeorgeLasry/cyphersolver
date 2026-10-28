# Schooling, "Secrets in Cipher" (Pall Mall Magazine 1896): the systems

Source: John Holt Schooling, "Secrets in Cipher", *The Pall Mall Magazine* vol. 8 (1896), four parts:

| Part | Issue | Pages | archive.org item | text |
|---|---|---|---|---|
| I "From ancient times to late Elizabethan days" | no. 33, Jan 1896 | 119-129 | sim_pall-mall-magazine_1896-01_8_33 | part1.txt |
| II "From late-Elizabethan days to mid-Stuart times" | no. 34, Feb 1896 | 245-256 | sim_pall-mall-magazine_1896-02_8_34 | part2.txt |
| III "From the times of Charles II to the second George" | no. 35, Mar 1896 | 453-462 | sim_pall-mall-magazine_1896-03_8_35 | part3.txt |
| IV "From the time of George II to the present day" | no. 36, Apr 1896 | 607-618 | sim_pall-mall-magazine_1896-04_8_36 | part4.txt |

The partN.txt files are archive.org's uncorrected OCR (figures garbled). Full-size page scans of every article page are in
`downloads/img/pN_p<page>.jpg` (with `_s.jpg` reductions); the full-issue OCR is in `downloads/`. Figures numbered
No. 1-58 run continuously through the four parts. Each of Parts I-III ends with a challenge cipher that the next
part explains; Part IV ends with the "insoluble" Nihilist challenge (Elgar's solve).

Verified from the page images where marked [img]; otherwise from the OCR text.

---

## Part I (Jan 1896)

1. **Wooden Roller (scytale)**, Nos. 1-2. Parchment strip wound spirally on a roller, written along the roller,
   unwound. Transposition; period = number of turns. Example plaintext "This is an illustration of the most ancient
   form of secret writing".
2. **Pass-word cipher** (Vigenère/Caesar-family), Nos. 3-4. Keyword PRUDENTIA; nine shifted standard alphabets, one
   per keyword letter (row P = A→P shift etc.), but applied **one alphabet per WORD**, not per letter: word 1 uses
   the P alphabet, word 2 the R alphabet, ... word 10 back to P. Ciphertext begins "JXU KGDVAWJK ..." = "the
   soldiers ..." (J→t, X→h, U→e under row P, i.e. Caesar shift +16; KGDVAWJK under row R). Plaintext: "...the
   soldiers ... mutiny for want of Victuals; supply us, or they will Revolt to the enemy" (OCR partial). Mentions
   Caesar's shift by 3.
3. **Elizabethan State cipher for Spain**, No. 5. Homophonic: 24-letter alphabet (j and u/v omitted from the left
   column, w after z), each letter with 12 substitute letters in 12 columns; the writer prefixes a numeral 1-12 to
   each cipher letter to say which column. Key irregular (same letter repeated within a column).
4. **Guise (c.1559) and Condé (1562) ciphers**, Nos. 6-7. Homophonic **symbol** substitution: "Underneath each of
   the letters of the alphabet are written three, sometimes four, peculiar marks -- something between modern
   shorthand and ancient hieroglyphics." Plus single-sign nomenclator (e.g. a sign for Roy de France, Pape; Condé:
   Guise = 6, Le Roy = S, Angleterre = W, La Royne d'Angleterre = small a). Key tables are facsimiles only.
5. **Mary Queen of Scots / La Mothe-Fénelon**, No. 8. Simple substitution, 1 to 5 symbols/letters per plain
   letter, plus name symbols.
6. **Mary Stuart (Darnley?) cipher**, No. 9. Symbols for letters, **nulles**, symbols/numerals for common words
   and names.
7. **"English Rebell fled into Flanders" (Prestall), 1571**, No. 11. Numerals and arbitrary symbols; vowels (and
   s) get 3 homophones; name symbols; a personal sign mark.
8. **Mary Stuart / Bishop of Glasgow 1571**, No. 12. Same family (symbol alphabet + nomenclator).
9. **Scottish gentleman / English woman 1574**, No. 13. Plain monoalphabetic letter-for-letter substitution.
10. **Cipher signatures and addresses** (Cecil papers), No. 14: single signs standing for a name; and No. 15, the
    cipher "given to Hugh Floyd" (symbol nomenclator).
11. **Challenge sentence** (end of Part I) = Roe's nine-figure cipher (see Part II no. 27); plaintext: "May you
    receive as much pleasure from reading my account of these ciphers as I received from writing it.--J. H. S."

## Part II (Feb 1896)

12. **Code-name cipher, Scottish Jesuits 1596**, No. 16. Classical names for persons (Solon = Sir Robert Cecil,
    Crassus = Lord Treasurer).
13. **String cipher**, Nos. 17-18. Ink marks on a string; wound on a notched card (key), each mark falls in the
    column of a letter; read left to right down the card. Example "Beware of this bearer, who is sent as a spy over
    you".
14. **Sliding-card cipher (c.1600)**, No. 19. Sheet 24 rows x 10 columns of irregularly placed letters (J and U
    omitted); a card slip with the alphabet in order slides across; a prefixed numeral (1-10) gives the column
    setting; changes of setting mid-message signalled by new numerals. (Columnar polyalphabetic, 10 alphabets.)
15. **Dot, Triangle and Line ciphers ("early Stuart", to 1694)**, Nos. 20-21 [img p. 250]. A ruler key with the
    26 letters A-Z in equal cells, each with an arrow. **Dot**: each plaintext letter is a dot placed under the
    column of its letter; successive letters go on successive lines down the page (so x-position = letter,
    y-order = sequence). **Triangle**: same dots, then joined in arbitrary groups of three into filled triangles
    (leftovers into one polygon); each vertex = a letter; read vertices top to bottom. **Line**: each letter
    marked by the END of a horizontal line (lines start at the box edge or at another line's end). All three
    encode "There is no safety but by flight". Positional, 26 letters.
16. **Carleton's Venice cipher (1610-15)**, Nos. 22-23. Numbers: each vowel 4 homophones, each consonant 2;
    persons as capital letters, then small letters, then numbers from 63 up (King A, Queen B, Prince C,
    Parliament F, Lord Chancellor K, French ambassador T). Example cipher No. 23
    "29.22.45.59.7.2.51.23.12.53.17.24.41.8.25.46.33.9.52.55.37.18.A-" (reader exercise, key only in facsimile).
17. **Two-Word Square cipher (1627)**, Nos. 24-25. A square with OPTIMVS across the top and DOMINVS down the right;
    the alphabet written twice inside (7 x 7 = 49 cells, alphabet x2), so each letter = a 2-letter bigram
    (column letter + row letter), two choices per letter. "TMONPOPVVDTVVVTDMDOVONVOOSIMSOPVMMINMDTSODMS" =
    "Reinforcements on the way" (TM=r, ON=e, PO=i, PV=n, VD=f, TV=o ...).
18. **Buckingham's numerical cipher (1627)**, No. 26. Numbers for letters; nulls 1-8, 19-22, 33-36, 49-52, 67-70,
    83-100; "nulls to be used betwixt every word"; a null placed before/after vowels.
19. **Sir Thomas Roe's Nine-Figure cipher (c.1630)**, Nos. 27-28 [img p. 255]. A 3x3 grid; each cell holds three
    letters and a figure: abc=3, def=7, ghi=2, klm=5, nop=9, qrs=4, tuw=6, xyz=8 (24 letters, no j, no v); the
    ninth cell's figure **1 is a null** "to disguise the more, or to fill up betwene woords". Within a cell: **no
    dot = 1st letter, one dot over the figure = 2nd, two dots = 3rd.** No. 28 "6 2̇ 7̇ 4̈ 6̇ 5̇ 1 6 3 9 ..." = "The
    Sultan has no money to lend". **8 base signs x 3 states = 24 letters: the same arithmetic as Dorabella
    (8 orientations x 1-3 arcs = 24).**
20. **Charles I's diagrammatic cipher** (to Lord Hyde), No. 29. Plaintext written along the lines of a figure
    (verticals from the bottom, top line backwards, diagonals, bottom line backwards, middle vertical): a route
    transposition of words on a drawing. "Take Charles to France ... Write to me in this cipher."
21. **Charles I's shorthand cipher**, No. 30 [img p. 256]. Each letter A-Z (24-letter alphabet with I/J, U/V
    merged) = a short stroke or dot placed above, on or below a horizontal base line, with different slants
    ("dots and dashes, placed above or below a line"). Key facsimile only: strokes of several orientations
    relative to a line -- the closest in look to oriented-mark systems.
22. **Challenge sentence** (end of Part II) = Revolving Dial (see Part III): "AO WB FSORWBU RCQIASBHG CT OBQWSBH
    ROHS HVS GDSZZWBU OBR HVS OPPFSJWOHWCBG 5 NLXW UR MAX PKBMXKL HY MAXF TKX HYMXG VHGYNLBGZ MH MAX FHWXKG KXTWXK"
    = "In reading documents of ancient date, the spelling and the abbreviations used by the writers of them are
    often confusing to the modern reader."

## Part III (Mar 1896)

23. **Rupert-Arlington numerical code (Charles II)**, Nos. 31-32. Each letter 3 numbers (homophones) + a printed
    table of syllables/short words with numbers (two-part nomenclator). No. 32 "478 308 378 464 392" = "Keep the King
    free from ill".
24. **Revolving Dial cipher**, Nos. 34-36. Two concentric 26-letter disks (Alberti-type). Indicator: first two
    letters "AO" = set A (outer) opposite O (inner); a digit in the text = rotate the inner disk n places right to
    left. No. 36: "AO WT MCI KWZZ QCAS CJSF HC IG MCI GVOZZ VOJS O DSBGWCB 5 TGW RHN FTR LMBEE FTDX T LATF 2
    JKKJNDODJI" = "If you will come over to us you shall have a pension, and you may still make a sham
    opposition." (OCR; check image.) Plain Caesar shifts per segment.
25. **Ladder cipher**, No. 37. Same as the dial but linear: slip with the alphabet written twice, ladder of 26
    windows slides over it.
26. **Fractional cipher (George I, Spain)**, Nos. 38-39. Five numbered squares; a fraction numerator = which
    square, denominator = cell(s); each fraction = a whole phrase ("I have reason to commend", "Nothing worth
    Notice has occurred since my last"). Phrase code.
27. **FG / DE Foreign Office codes (1745)**, No. 40. Large numerical codes with grammatical operator numbers (92,
    223, 392, 413 cut syllables/letters). Not illustrated.
28. **Musical cipher (George II)**, No. 41 [img p. 459]. Each letter = a written note (24 letters, notes of two
    durations on different staff positions); "you may chose either of the 3 keys" (three clefs/keys usable);
    "if any thing should be wanting in measure it may be filled up with any of the following marks" (rests as
    nulls to complete bars); a mark for the end of a period. Example: "I have received yours of the Sixteenth".
29. **Grill (Cardan grille)**, Nos. 42-43. Card with 9-10 oblong holes laid on an innocent letter. Positions can be
    sent as vulgar fractions.
30. **Challenge sentence** (end of Part III), No. 44 [img p. 462] = Heraldic cipher (Part IV), with the shield
    (No. 45) as partial key. 3 lines, about 50 signs; plaintext given in Part IV: "You will read this sentence in
    less time than I spent in writing it."

## Part IV (Apr 1896)

31. **Pack of Cards cipher**, No. 46. 32-card piquet pack in a remembered order (rhyme: K 8 J Q A 7 9 10; suits
    clubs, diamonds, hearts, spades), message written one letter per card in invisible ink, round after round
    (32 letters per round), then shuffled. Transposition (period 32).
32. **Consul Davison, Algiers (George III)**, No. 47. Homophonic: five rows of substitute letters, a 2-figure
    indicator (e.g. 58) prefixed to say which row; changed several times per despatch. Plus **arbitrary marks for
    common short words** ("this Mark + may serve for th") and 2-figure codes for words (84 Ships, 67 Governor, 21
    fitted out, 49 Xebecks).
33. **Heraldic cipher (18th century FO papers)**, Nos. 48-50 [img p. 613]. A pigpen (tic-tac-toe) variant disguised
    as a shield: 3x3 grid, 24 letters (J and V omitted) in 9 cells holding 3,2,3 / 3,2,3 / 3,2,3 letters:
    ABC | DE | FGH / IKL | MN | OPQ / RST | UW | XYZ. Each letter = the outline of its cell (corner/U/box shape
    as cut by the grid lines) plus **1, 2 or 3 small ticks** inside for 1st/2nd/3rd letter of the cell. "Plot
    known. Fly." Again: one base sign per cell x 1-3 marks = 24 letters.
34. **Checker-board cipher of Russian prisoners**, Nos. 51-54. Steganographic: the letter's pen-lifts ("breaks")
    divide the text into groups of 1-5 letters; a word's last letter joins the next word unless its last stroke
    points upward; group lengths read in pairs (row, column) on a 5x5 Polybius square. "Plot discovered. Burn the
    Orloff papers in Moscow."
35. **Nihilist numerical cipher**, Nos. 55-58. 5x5 square A B C D E / F G H I K / L M N O P / Q R S T U / V W X Y
    Z (J omitted), 11=A ... 55=Z (TYRANT = 44 54 42 11 33 44 confirms I/J merged). Ciphertext = plain number + key
    number (decimal addition, carries allowed), key word repeated. "Meet me in Paris on Monday" with TYRANT ->
    76 69 57 55 65 59 68 87 77 22 75 68 87 88 75 43 67 77 58 65 96. Same square used for tap code (rows/columns
    as raps, fingers, candle flashes).
36. **Dictionary cipher** (Duke of Portland specimen): numbered dictionary, number per word. Invisible ink noted.
37. **Final challenge** [img p. 618]: Nihilist, unknown key, white disks on black:
    `36 49 97 65 45 43 30 24 76 88 66 / 54 45 26 44 55 59 57 22 36 ? ?`.
    Checked here: key **COURAGE** (13 34 45 42 11 22 15) gives HE WHO FEARS IS HALF DEAD (the two "?" are
    unwritten). Elgar's solution (the "Courage card" set, the black-painted box, Buckley 1905) is this.

---

## Elgar's annotations and the secondary literature

- Elgar's copies of the four parts are said to be at the Elgar Birthplace Museum (Enigma Theme Unmasked blog;
  Bauer, *Unsolved!* 2017 ch. 3, cited via Wikipedia). No source found that transcribes **what he marked** in the
  articles; nothing found online says which pages he annotated. Bauer's chapter (not accessible here) is the place
  to check.
- His solution of No. 37 is documented on a set of nine cards (the "Courage cards", Elgar Birthplace) and painted on
  a wooden box; he mentions it in Buckley's *Sir Edward Elgar* (1905), p. 41 (blog citation). Nautilus says he made
  notes on *Cockaigne* sheet music. Nick Pelling (ciphermysteries.com 2013/10/09) reports that the first Courage
  card carries ten Dorabella-type "rotating 3" letters (eight triple cups, an upward double, an upward single), as
  reconstructed by Christian Schridde, unseen in context; no transcription of the nine cards is online.
- Eric Sams thought the Schooling solve unremarkable ("many readers could do as well in half an hour").
- Mark Pitt (2019) linked the Enigma "dark saying" to "He who fears is half dead".

## Prior discussion linking Pall Mall to Dorabella; what was tested

- ciphermysteries.com (Pelling, "The Dorabella cipher and Elgar's other little ciphertexts", 2013): Schridde
  wondered whether Dorabella uses "some element of the Nihilist cipher"; no test reported. Pelling's own tests:
  rotating-pigpen with a length-10 offset sequence (Excel, C program), nothing plausible.
- Enigma Theme Unmasked blog (Santa): proposes a checkerboard/Polybius ("music box") reading for the Enigma theme,
  not a tested Dorabella decryption.
- Other Dorabella proposals (Sams 1970 phonetic substitution, Roberts, Gaffney clock-face key + backslang,
  Henderson, Packwood, Atance melody; Wase 2023 shows standard solvers fail for English/Latin monoalphabetic) do
  not derive from the Pall Mall systems except that the Elgar alphabet itself (24 letters, 8 orientations x 1-3
  arcs) is structurally Roe-like/Heraldic-like.
- Not found: any published test of Roe's figure-plus-dots structure, the Heraldic cell+tick structure, Charles I's
  line-position shorthand, a Pass-word (per-word Caesar) or Revolving-Dial (indicator + shift digits) system, or a
  Nihilist/Polybius coordinate reading against the 87 Dorabella signs.

## Plausibility for a 24-sign, 87-character note

Direct structural matches (sign = base form x count, 24 letters):
- **Roe nine-figure (No. 27)** and **Heraldic (No. 48)**: 8 (or 9) base signs x 1-3 marks. Elgar's alphabet is the
  same shape (8 orientations x 1-3 arcs). Implementation: the base sign selects a group of three letters, the arc
  count selects within it. Test orders of the 24-letter alphabet (j and v/u dropped) and the mapping
  orientation -> group, including the Heraldic grouping (3,2,3 per row: ABC DE FGH / IKL MN OPQ / RST UW XYZ) and
  Roe's group order (abc def ghi klm nop qrs tuw xyz with figure order 3 7 2 5 9 4 6 8). Note Elgar's own key
  (1920s notebook) is the straightforward version of this; Dorabella failing as a simple substitution means a
  second layer is needed.
- **Pass-word cipher (No. 3)**: a keyword shift applied per word (or per letter) on top of the 24-sign alphabet,
  i.e. rotating the orientations (Pelling's "rotating pigpen" tests are this family, per letter).
- **Revolving Dial (Nos. 34-36)**: shifts changed mid-text by indicator signs; for Dorabella, rotate orientation
  index by a running offset. Dorabella has no visible digits/indicators, so the shifts would have to be implicit.
- **Nihilist (Nos. 55-58)**: Elgar demonstrably mastered it in 1896. Additive key on Polybius coordinates; with
  24 signs one could read sign = (orientation, arcs) as a coordinate pair or treat consecutive signs as
  coordinates. Testable but the 87 signs give ~43 letters if paired.
- Lower: musical cipher (letters as notes; consistent with Atance's melody idea but Dorabella is not on a staff),
  Charles I shorthand (oriented strokes against a line), Dot/Line positional cipher (sign position, not shape),
  scytale/cards/grille transpositions (would need a prior 87-letter plaintext layer). Code/nomenclator systems
  (Carleton, Rupert, FG, fractional, dictionary) are not plausible for 87 signs from a 24-sign set.
