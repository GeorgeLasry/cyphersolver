# Schöning's secret mission to Berlin, 1783-84 (KHA A32-603)

Status: in progress (scans fetched and being surveyed)

## Source

Koninklijk Huisarchief, The Hague, A32-603: "Correspondentie van G. von Schöning vanuit Potsdam met prinses
Wilhelmina en advocaat-fiscaal Van der Hoop, met ontcijfering van zijn brieven door Van der Hoop", 1783-1784, 212 scans
via the Koninklijke Verzamelingen rendition API (`scan_ids.json`; `img/` git-ignored). Part of A32-599-604, the file on
Schöning's secret mission to the Prussian court on Princess Wilhelmina's behalf. Found by the Nationaal Archief sweep,
KHA lead K4.

## Survey (25 Oct 2026, `survey.md`, subagent; counts estimated at ~1100 px)

- 43 letters by Schöning, 28 July 1783 - 10 July 1784: 34 to Van der Hoop (French, one Dutch), 9 to Princess
  Wilhelmina (German). Also her note, two notes of Frederick II, Larrey's memoranda.
- The system: running text in a symbol alphabet (hook and stroke signs, one per letter, word gaps), with names and
  titles as 2-3 digit code numbers followed by ":;." (61, 65, 66, 69, 70, 857, 880, 446, 191, 343, 155 ...).
- 24 letters (all to Van der Hoop) contain cipher: 6 partly glossed (No. 4 of 12 Aug 1783 interlined; the 25 Nov 1783
  copy glosses ~45 of 52 codes), 18 unglossed with about 400 code numbers (26 Jan 1784 alone ~100).
- 10 clear copies by the decipherer (No. 4, No. 5, 23/25/28 Nov, 13 Dec 1783, 3/6/19 Jan 1784, fragment 19-20 Dec):
  they write out the symbol text but leave the code numbers as numbers, except the 25 Nov copy.
- Larrey's memorandum (s180) lists a "Lettre déchiffrée de S. à Mr van der Hoop"; on 26 Jan 1784 Schöning says
  Van der Hoop could not read his last letter for numbers missing from his alphabet.
- Code values from context and glosses: 857 = S.M., 446 = Hertzberg, 914 = Thulemeier, 66/70 = Altesse / Altesse
  Sérénissime, 862 = Schöning; 450, 106 uncertain.

## Plan

1. Symbol alphabet from the copy/original pairs (10 pairs): label the signs in ASCII (the output filter stops long
   runs of unusual characters), align, and fix the letter table.
2. Code table from the 25 Nov 1783 glosses plus context across all letters.
3. Read the 14 letters with no clear copy and the unglossed codes; measure. Related keys to try on unglossed numbers: R1024 "Grand Chiffre" (Van Reede, Berlin
1787, `../vanreede1787/`).

## Prior work

No edition of these letters found on the web (25 Oct 2026); not on DECODE.

## Step 1, letter table (25 Oct 2026, partial)

From the 6 Jan 1784 pair (original s138, copy s140), by subagents, ASCII sign labels G01-G21
(`signs_alphabet.md`, `letter_table.tsv`, `align_samples.md`):
- confirmed (3+ times): a c d e f i l m n o p q r s t u v; single sightings: g (G19), z (G20), doubled l (G16);
  possible second s (G21); G18 also for c-cedilla (*soupsonne*); a tick above the line marks run-together word breaks;
  plain punctuation inside the cipher.
- not yet seen: b h j k x y. The rest of s138 (lines 6-12) holds x, y, h, j per the copy; code numbers in the block
  follow the copy's order (884, 881, 860, 858, 582, 65, 914), which anchors the alignment.
- not yet verified on a second pair (25 Nov 1783 s091/s093-095; 13 Dec 1783 s112/s115-117).
Lesson: the glyphs need 3x crops segment by segment; two agent passes covered ~200 signs.

## Step 1 result (25 Oct 2026)

- 6 Jan 1784 (s138/s140) aligned in full: a c d e f g h i(=j) l m n o p q r s t u v x z; h = G23 (small cross); j written
  as i (G17); second s G21 (medium); a dot above a sign doubles it (ll nn rr tt ss ff); a short reversed hook between
  words is a divider. No y in this letter (copy spells "moiens").
- Verified on 25 Nov 1783 (s091 against copy s093, `verify.md`): 142 of 143 known signs agree with the copy (99.3%);
  new: b = short mid-height dash (G24, 3x), h also as an L with a cross above; one doubt, G11 (c) read s once.
- Still to find: y, k (rare in French). Step 1 is done; the table is in `letter_table.tsv` / `signs_alphabet.md`.

## Step 2, code table (25 Oct 2026)

`code_glosses.tsv` (25 Nov 1783 copy: 42 occurrences, 38 numbers glossed, 5 not) and `code_context.tsv` (clear copies:
164 occurrences, 78 numbers, with context) merged into `code_table.tsv`. The code is **one-part alphabetical with blocks
of homophones**: Berlin 106, Cabale 157, Cour 191, Hertzberg 446-450, Prince 725-733, Republique 805, Roi 810-818,
Sa Majeste 857-861, Schoning 862, Son Altesse Royale 880-884, Stadhouder 888, Thulemeier 914-918, Versailles 975-977.
Context values checked against the order: France 343, Empereur 250-255, Angleterre 81-85, Hollande 451, lettre 582.
Open: 435/439 "Heidm..." (a name), 661, 724, 763, 809 ("pour moi 809"), 950, 978 (after "de Goltz"), the 8x/25x
alliance numbers; 449 vs 446, 859 vs 858, 881 vs 884 need 3x crops. The 12 Aug 1783 (No. 4) glosses not yet read.
Next (step 3): decode the 14 letters with no clear copy with letter_table.tsv + code_table.tsv, bracket every unknown
number alphabetically, and measure.

## Step 3, first pass (25-26 Oct 2026)

Two subagents deciphered the 11 cipher letters with no clear copy (`dec_*.tsv`, one token per line: sign label or code
number, then its reading; running readings in `# line reading:` lines). `measure.py` (`measure.log`):
**3,447 tokens, 3,198 given a value (92.8%), 80 code numbers bracketed alphabetically, 169 unread; 110 of 192 code
numbers known.**

Caveats before this counts toward the read bar:
- The measure counts signs given a letter, not words that read as sense. Most of the 26-27 Jan 1784 letter reads as
  French (de Verac futur ambassadeur de France; an alliance of France, Spain and Prussia against the Emperor and
  England; Schöning's role and "ma tres chere princesse"), but some lines are garbled ("leur jamble ratbbdn", "es ue des
  honoronrant") and need re-reading at 3x.
- No. 1 (s001) is only its first three lines; lines 4-20 are not transcribed.
- The early letters (Nos. 1-3, Aug 1783) use a variant alphabet: one inverted-T sign serves o and d. Their word breaks
  were set by the agent, not by the scribe's ticks.
- Numeric signatures (a separate digit script) and the address panel on s029 are not read.
- Proposed from brackets: 500 between Hollande and lettre, opening "[j'ai] l'honneur" (j); 750 between Son Altesse
  (733) and Republique (801).
Next: a sense check per line with the fr-1600-letters model, re-read the garbled lines and No. 1 at 3x, then grade.

## Step 3 update (26 Oct 2026)

- s172 re-read along the slant (the first pass paired wrong line halves): unread on that page 40 -> 11; it now reads
  as Schöning's plan: assure Vérac the Orangists are not "anglomaniens", and make a defensive and offensive alliance
  with France, Spain and Prussia against England and the Emperor.
- s173-s174 re-transcribed with every code as a token ("de ma mission", "le prejuge de monsieur Lare[y]" added).
- Batch B also wrote `combined_172_firstpass.tsv` (an older merge of s172-s176), kept out of the measure.
- s176 is dated "P. ce 26 fevrier 1784" in its margin: probably a separate February letter (VdH's letter of the 15th
  arrived on the 26th and could not be deciphered), still inside `dec_175_pages.tsv`.
- 24 Dec 1783: warn the privy council so that 70 does not thwart Berenger's money negotiation, nor his intrigues to make
  a party against the Emperor "par ordre de 857". 15 Jan 1784: "Monsieur Larré n'est point instruit de mes secrets".
  10 July 1784: the Gazette's Petersburg revolt was really at Constantinople, stirred by "notre" Gaffron; 861 recalled
  him, and he will be put in Spandau.
- The cup sign G11 (c) also stands for s (twice) and g (Espagne, espagnols, derangement): a polyvalent sign, or two
  cup shapes not yet told apart.
