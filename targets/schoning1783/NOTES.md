# Schöning's secret mission to Berlin, 1783-84 (KHA A32-603)

Status: read (26 Oct 2026): 3,988 of 4,088 tokens given a value (97.6%), 95.9% of letter signs on lines that read as
French; 188 of 226 code numbers known; open: 38 scattered code numbers, 62 scattered signs, the signature formula
and the s029 address (too short, no crib)

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

## Sense check and grading (26 Oct 2026)

- `sense.py` scores each deciphered line with fr-1600-letters (calibration: good French about -2.1, the known garbled
  lines -2.8 to -3.1, shuffled letters -4.1 to -5.3; threshold -2.6). Seven lines flagged and re-read at 3x; the cup
  sign G11 settled as c only (the "g" readings were G19, the open C; the "s" readings are the writer's spelling by
  sound: ce meler, cera).
- No. 1 (s001) transcribed in full (lines 4-16): 752 tokens, 81.4% given a value, 135 unread; the low-resolution
  lines 4, 9, 12, 13, 15 are weak; NEW2-NEW4 unresolved.
- **Measure (`measure.log`): 4,100 tokens, 3,779 given a value (92.2%), 90 codes bracketed, 231 unread; 136 of 228
  code numbers known. Without No. 1: 3,167 / 3,348 (94.6%). Sense (`sense.log`): 93.1% of letter signs on lines that
  read as French.**
- Grade: below the read bar (95% as sense) overall and for No. 1; the other ten letters are just under it. The open
  pieces are the weak No. 1 lines, ~90 bracketed code numbers and a few unresolved runs (s175 line 11 middle).

## Escalation pass, 26 Oct 2026 (to the read bar)

- **No. 1 lines 3, 4, 6, 15** re-read at 6x sign by sign (dec_001.tsv notes "6x pass"): line 3 "(Holl)andois entre
  lesquel il y en a des foux patriotes :: 500 parler monsieur ... aumeur du courrier"; line 4 "lui ai dit de donner
  une louenge bien merite aux bourguemetres regnant d'Amsterdam"; line 6 "ce veut dire l'aumeur dont il me parle ::
  contre monsieur Thulemeier"; line 15 "... t mal 880. 475: serenissime et la malheureuse 801. cet idie ... a(v)ec
  zele". The inverted T (G15) is o as well as d in the early letters; the writer spells humeur "aumeur".
- **Nos. 2 and 3 (dec_003, dec_005)** re-read: every unread sign resolved ("je croi bien que 750 aurat prit les
  arangemans necessaire d'etre averti du moment de mon arrivee"; "914 est un infame. 446 sera envoyer. 818 hait et
  meprise de bon coeur 724, mais en revanche il aime tendrement 734 ... Potsdam ce huit d'aou mile sept cag quatre
  vintt troi"); several old tokens were double counts or a code-table bracket split into tokens.
- **s175 line 11** re-read: "du 733. ici, qu'il faut aussi etre une communication reguliere de lettres". **s174
  line 1** checked at 5x: "si par hasar elle reucisoit" (spelling by sound; still scores low).
- **Code values from the sibling files** (`code_values_new.tsv`, subagent survey of A32-599, 601, 602 and the No. 4
  glosses): A32-599 175309-175313 is Van der Hoop's own "Dechiffrement de Lettres de S., communique a LL.AA.S.&R. le
  14 Dec 1783" for the letters of 23 and 25 Nov 1783. New values include 435/439 Heiden, 978 Versailles, 163/155/164
  Cabale, 968/972 Vauguyon, 724 Prince, 734 Princesse, 750 Prince de Prusse, 784 Reede, 809 le Roi, 895 Stadhouder,
  61/63 S.A.R., 67-69/90 S.A.S., 107 Berlin, 461 Van der Hoop, 573 Larrey. `apply_values.py` gave 43 bracketed tokens
  their value (marked {sib}).
- **Signatures and the s029 address** (`signatures.md`): one fixed 30-31 sign formula in a digit script after the
  closing, and a third set of cursive signs on the address panel. Neither is a letter substitution of Schoning's
  name; no clear form survives.
- Measure (`measure.log`): 4,088 tokens, 3,988 given a value (97.6%), 38 bracketed, 62 unread; 188 of 226 code
  numbers known. Sense (`sense.log`): 3,608 of 3,763 letter signs (95.9%) on lines scoring >= -2.6; the three flagged
  lines are sound-spelled (s174 line 1, dec_005 line 3) or a list of names (dec_204).

## Remaining gaps

- 38 code numbers without a value (e.g. 475, 499, 500, 661, 950, 1066), scattered across the letters - blocker: open-codes; no gloss in A32-599/601/602/603/604, values from alphabetical position only
- 62 scattered unread signs (No. 1 33, s172 11, s175 16, 27 Jan 2) - blocker: illegible; blots, overwriting by a later hand and damaged ink, re-read at 5-6x
- the signature formula (30-31 signs) and the s029 address panel (about 33 signs) - blocker: too-short; one fixed short string each, no clear form anywhere in the file

## Escalation

- [x] clear-pages: the decipherer's 10 clear copies used for the tables; Van der Hoop's "Dechiffrement" of 14 Dec 1783 (A32-599) found and used
- [x] siblings: A32-599, A32-601, A32-602 surveyed for code values (code_values_new.tsv); A32-604 De Larrey's dossier searched in full
- [x] known-keys: the A32-604 Byland key list (scan 6) applied; R1024 Grand Chiffre not the code (different system)
- [x] print: no edition found
- [x] key-rebuild: letter table from the copies; code table from glosses, the 14 Dec 1783 decipherment, context and alphabetical bracketing (188 of 226 numbers)
- [x] retry: every flagged line and unread sign re-read at 5-6x (No. 1, Nos. 2-3, s174, s175); values from the siblings applied

## No. 1 re-read at 5x (26 Oct 2026)

Lines 3 (tail), 4, 9, 12, 13, 15 re-read at 5-6x (the slant on s001 is about 0.01, not 0.04). Now reading: line 9 "il
soupsonna monsieur votre frere le general d'etre du parti du cal(?): 499 de le desabuser"; line 13 "avent qu'onne soit
tout a fait sur de la bonne reussite"; line 15 "... la malheureuse 801. cet idie ... ave(c) zele". NEW4 = G21 (second
s); NEW3 = ink blots read from context; NEW2 probably G22 x ("teriteaux"); new NEW5 (blotted), NEW6 (squared bracket,
read v). Still weak: line 4 (three signs under a gloss), line 12 "ssanur", the name after "monsieur" on line 3.
Measure: No. 1 676/754 (89.7%, was 81.4%); all letters 3,852/4,102 (93.9%). Sense: 90.7% of letter signs on lines
scoring >= -2.6 (was 93.1%: the re-read added more doubtful words, and the writer's spelling by sound lowers scores).
- 26 Oct 2026 (later): escalation pass to the read bar (No. 1, Nos. 2-3, s174, s175 re-read; sibling code values from A32-599/601/602); 97.6% of tokens, 95.9% as French, validation pass; written up (docs/schoning1783.html).
