# d'Affry (The Hague) to Rouillé / Bernis, 1757-58: intercepted code letters

Status: read in part (5 Oct 2026, rerun 14 Oct 2026: 0.89 of the code groups read as sense by measure_sense.py, 8,282
of 9,306; the 21 Sept figure 0.86 counted groups that merely had a value; write-up affry1757.html, 19 Sept 2026)

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): R1071, d'Affry's letter to Stainville at
Vienna (4/7 Aug 1757), is in a different code (code C below) and is now [`targets/affry1757c/`](../affry1757c/NOTES.md)
(a different cipher, with its own page; `cipher_C.txt` and its DOC file moved there). Codes A and B below are one
code; the profile now lists them as one document. Figures in the sections below dated before 14 Oct include R1071
where they say so.

KHA The Hague, Prins Willem V, inv.nr. 192. DECODE R1052-R1076, R2067 (catalogue: d'Affry, 11 unsolved records).
Images (git-ignored, `img/`) and DECODE digit transcriptions (`decode/DOC_*.txt`) fetched 19 Sept 2026 with the
bordeaux cookie. `parse.py` reads the DOC files; `cipher_A.txt`, `cipher_B.txt`, `cipher_C.txt` hold the groups.

## Prior work

- DECODE marks R1052, R1053, R1062, R1063, R1066, R1069, R1075 "solved by Dutch codebreakers, solution on separate
  sheets". The sheets **are** among the DECODE images, as clear-text pages marked "gelcp[?] D'A. à R." with number
  and date (first missed here: they read like ordinary clear letters). Lyonet's decipherment pages: R1052 5506,
  R1053 5507-08, R1062 (see align/), R1063 (see align/), R1065 5566-68 + 5572 (cipher in numbered paragraphs P:1..),
  R1066 5578 (+5575), R1069 5589 + 5586, R1075 5604-05. Transcribed into `plain/R*.txt`.
- De Leeuw, *Cryptology and statecraft in the Dutch Republic* (thesis, UvA 2000), ch. on the Seven Years' War:
  Lyonet broke d'Affry's first code by June 1756, then "two more French ones, belonging to Bonnac and D'Affry";
  the French code used July 1757 - December 1758 "is not mentioned by Lyonet and Croiset, but was nevertheless
  solved"; d'Affry's code to Choiseul from Dec 1758 broken later.
- The contemporary decipherments survive as Nationaal Archief 1.01.50 (Stadhouderlijke Secretarie) inv. 221
  (d'Affry to R[ouillé], Dec 1755 - Jun 1757) and inv. 223 (d'Affry to B., Jul 1757 - Dec 1758), "grouped by the
  cipher used". Not digitised (empty scan ids, checked 19 Sept 2026).
- Bussemaker (ed.), 'Uittreksels uit de brieven van D'Affry aan de Fransche regeering (Dec 1755 - Mei 1762)',
  BMHG 27 (1906), DBNL `_bij005190601_01_0008`: Fruin's extracts from those decipherments, Dutch summaries with
  verbatim French sentences. Entries for 7 Jan, 1 Feb, 1 Apr, 19 Jul, 22 Jul 1757 match letters here.
  So the content of these letters was read in 1757 and summarised in print in 1906; the full text is not printed.

## Codes (group-frequency cosine between letters)

Revised: the Jan-Feb ("A") and Apr-Jul ("B") letters share their common values (de 219/1018/1138, la 583/382, que 197,
M 196, vous 569, il 1088, me 208, ne 134, faire 847, ma 6, ti 588, n 580...); the cosine split reflects homophone
habits, not two codes. `cipher_U.txt` holds both; `key_U.json` is the joint key. R1071 (C) is different.

Original split:

- **A** (Jan-Feb 1757, to Rouillé): R1052, 1053, 1062-1065, 1072, 1073, 1075, 1076. 5,011 groups, 777 distinct.
- **B** (17 Feb? / Apr 1757 - Jan 1758, to R. then "A à B" = Bernis): R1066, 1067, 1068, 1069, 1054, 1070, 1074
  (+ R2067, no transcription). 3,512 groups, 743 distinct. R1054's "to Bonnac" is DECODE reading "B"; the
  letter is Bussemaker's 19 July 1757 extract.
- **C**: R1071 (to Choiseul, 7 Aug 1757), 761 groups, unlike both.

Groups run 1-~1200; a word-and-syllable nomenclator (two-part or mostly unordered: frequent groups barely
cluster numerically).

## Code B: crib from Bussemaker's 19 July 1757 extract on R1054

The verbatim passage "Zoo het eerste het geval was, il me paroit qu'il seroit essentiel ... de la sagesse de leurs
règles" lies in R1054 positions ~200-370. Anchor: `800 698` (des précautions) at 264 and 277, 12 words apart in
the crib. See `key_B.json` for the growing key.

## Result (19 Sept 2026): key rebuilt from Lyonet's decipherments, the unread letters read

**Key.** Eight letters carry Lyonet's clear copy among the DECODE images (R1052, R1053, R1062, R1063, R1065, R1066,
R1069, R1075). Each clear copy was transcribed from the images (`plain/`) and aligned group by group with its
cipher (`align/*.tsv`, graded H/M/?; sub-agents, one letter each, cross-checked against each other). `merge.py`
votes `key_M.json` (651 groups; 56 left ambiguous in `amb_M.json`; `overrides.json` for corrections found in
reading). One code serves Jan 1757 - Jan 1758 (to Rouillé, then Bernis); only R1071 (to Stainville/Choiseul,
Vienna, 4/7 Aug 1757) is in a different code and stays unread.

**Readings** (`read/R*.md`, inferred values with evidence in `read/R*_new.tsv`, {braces} = inferred, [n] = open):

| Record | Date, no. | Read | Content |
|---|---|---|---|
| R1072 | 6 Jan 1757, 123 | ~65% in sense | "the Italian", a spy, offers to go to England and report on forces, cabinet, campaign plans; wants pay and a pension |
| R1076 | 7 Jan 1757, 124 | ~90% | convoy and escort after the storm; navy without land increase; herring; talk in Amsterdam |
| R1073 | 25 Jan 1757, 133 | ~90% | false rumour of a memorial on the augmentation; talk with the Grand Pensionary |
| R1064 | 1 Feb 1757, 136 | ~95% | States of Holland adjourned to the 20th; taxes for the augmentation; herring favour; spies (Quintin, La Combe) |
| R1067 | 1 Apr 1757, 161 | ~88% | Steyn embarrassed; the Gouvernante: "faut-il que ce soit moi qui favorise les moyens de faire du mal à mon père?"; Maastricht convoy; Wassenaer |
| R1068 | 26 Apr 1757, 172 | 56/60 groups | courier Vienna-London; Colloredo to d'Arenberg |
| R1054 | 19 Jul 1757 (to B.) | ~92% | Gouvernante's journey; ask for a declaration of the States-General; précautions of d'Estrées |
| R1070 | 22 Jul 1757, 210 (to B.) | ~95% | Gouvernante to speak to the States of Holland; Ostend and Nieuport; trade to Amsterdam and Rotterdam |
| R1074 | 17 Jan 1758, 283 | ~90% | French loan attempted in London; Macdonald (Bulkeley regiment) suspected |
| R2067 | 17 Jan 1758, 283 (to B.) | ~91% | cover letter to the loan extract: money operations in England useless; Englishmen and Spaniards passing; transcribed from the images here |
| R1071 | 4/7 Aug 1757 (to Stainville) | not read | different code |

**Checks.** Bussemaker's verbatim sentences recur group for group: 19 Jul (R1054, groups 145-351, four small
differences where Fruin abridged), 22 Jul (R1070), 1 Apr Wassenaer sentence (R1067 piece 7); Coquelle (1904)
quotes the Gouvernante's words to d'Affry from the Paris original, found in R1067. Bussemaker's Dutch summaries
of 7 Jan, 1 Feb, 1 Apr, 19 Jul and 22 Jul agree point by point.

**DECODE transcription slips** found on the way: in two hands a looped 8 was read as 0 (R1072, R1075, also R1064,
R1067: 056=856, 099=899 ...); groups run together (58291 = 582 91) or dropped; superscript corrections (8^578).
`view.py` splits merged groups; the reading agents re-parsed from the DOC files where needed.

**Open:** ~5-12% of groups per letter (listed as [n] in each reading), the weak stretches of R1072, R1071 entirely.

## Push towards 95% (5 Oct 2026): image re-transcription and a sense measure

**The old measure did not count sense.** The 0.86 of 21 Sept counted a group as read when it had any key or inferred
value, '?' values included, whatever the text around it said; by that rule the undeciphered letters now stand at 0.96.
It also ran on `cipher_U.txt`, the DECODE digits parsed by `parse.py`, which (a) keeps DECODE's 8-read-as-0 slips
(the reading agents corrected them only in their prose readings), and (b) drops every DECODE line that starts with a
paragraph tag (`<CLEARTEXT FR B:3.> 676 . 996 ...`): 7 lines of R1064 and 12 of R1065 were missing from the counts.

**New measure, `measure_sense.py`.** A group counts as read only if it has a value (key_M, H/M rows of read/*_new.tsv,
or `key_X.tsv`; '?' rows do not count) and the 9-group window round it scores as French under
`lang` model `fr-modern` (no spaces, per-char log-prob > -3.0) with at most one valueless group in the window. Proper
names spelt in syllables (Maham/Mahom, Baltimore, Macdonald) cannot pass an LM, so the ranges in `sense_names.tsv`
count when every group has a value. Image re-transcriptions in `transcr/R*.txt` replace the DECODE parse.
Calibration: the same test applied to the eight Lyonet letters, along their aligned (known-sense) group sequences,
passes 0.876 of groups, so the measure under-counts real sense by roughly an eighth; the figures below are the raw
measured ones. The Lyonet letters count as read (contemporary decipherment); R1071 counts as unread.

**Image re-transcription** (all from the DECODE images in img/, rotated -90, read strip by strip at full resolution):
- R1072: re-transcribed here (`transcr/R1072.txt`, 555 groups); the copyist's two looped forms of 8 were read as 0 by
  DECODE nearly everywhere (849, 898, 984, 878, 1018, 1088, 868, 885, 828 ...). Text now reads as a whole
  (comptoit, gratification de cent louis, d'Écosse et d'Irlande, Baltimore, remplit ses engagements, assez tôt).
- R1074: re-transcribed here (`transcr/R1074.txt`, 537 groups; DECODE's 564 included split/merged junk [1] [0] [21]).
- R1067: re-transcribed by an image sub-agent (`transcr/R1067.txt`, 1,481 groups; ~133 positions differ from DECODE:
  ~20 run-together groups, ~6 dropped, 3 added, one struck group kept by DECODE, the rest mostly the 8 trap; three
  copyist hands; paragraph numbers No 2-13 spread over the pages).
- R1064: converted with `doc2tr.py` (keeps the tagged lines) and then checked line by line on the images by a
  sub-agent (`transcr/R1064.txt`, 1,243 groups; ~48 8/0 fixes, one whole line DECODE dropped on p. 5, 2 splits,
  ~10 other digits; a second hand on pp. 3-4 writes 8 as a w-shaped double loop and 3 as a reversed c).
- R2067: the 19 Sept hand transcription reformatted (`transcr/R2067.txt`); R1065 converted with doc2tr.py for the
  denominator only.

**Pooled open codes** (`pool.py` lists every occurrence across all letters; only values that every occurrence forces
went into `key_X.tsv`, with evidence): 1096 ir, 823 gra, 630 lui, 990 dit, 336 facil, 520 faire (H); 1102 Écosse,
597 et, 459 to, 363 conven, 240 tôt, 686 pli, 458 en, 212 plus, 840 cli, 514 ld, 303 la Gouvernante (name code),
485 vous (M). Left open because more than one word fits: 970 (projets/desseins/plans, 6 occurrences), 869
(opérations/plans), 109/651 (two days: "avant [109] ou [651]"), 731/708, 1191 (le/du [1191] Macdonald), 1020, 1082,
890, 431, 373, 724, 993, 426, 427.

**Result, sense measure (threshold -3.0), before -> after:**

| Letter | groups | 5 Oct before | 5 Oct after | what moved it |
|---|---|---|---|---|
| R1072 | 555 | 0.661 | 0.888 | image re-transcription; 8 pooled values |
| R1067 | 1,481 (was 1,471) | 0.661 | 0.791 | image re-transcription; lui, dit, facil, faire, la Gouvernante |
| R1074 | 537 (was 564) | 0.702 | 0.747 | re-transcription; faire, Écosse, ld; names |
| R1064 | 1,243 (was 1,108) | 0.766 | 0.808 | 135 groups DECODE/parse.py had lost; image check |
| R2067 | 457 | 0.761 (not in cipher_U; counted from transcr) | 0.792 | lui, dit |
| R1054 / R1070 / R1073 / R1076 / R1068 | 372/400/312/403/60 | 0.925/0.885/0.885/0.819/0.667 | 0.949/0.905/0.885/0.819/0.750 | pooled values |
| undeciphered letters | 5,820 | 0.749 (of 5,245) | 0.824 | |
| all groups (Lyonet letters read, R1071 unread) | 10,067 | 0.778 (of 9,363) | 0.823 | |
| without R1071 | 9,306 | 0.847 | 0.890 | |

At threshold -3.4 the totals are 0.848 overall, 0.917 without R1071; at -2.6, 0.773 / 0.837.

**Why 95% is out of reach here.** R1071 is 761 of 10,067 groups (7.6%) in another code with no key material, so the
target cannot pass 0.924 even if every other group read. Within the readable letters the remaining failures are
(i) open codes where several words fit (listed above), (ii) key values that make nonsense in place (homophone
clashes the 651-group vote did not settle, e.g. 1080 pêche in the date of R1074, 307 forc/pen), and (iii) the
measure's own under-count of about an eighth.

## Remaining gaps

- open code groups where more than one word fits (970, 869, 109/651, 731/708, 1191, 1020, 1082, 890, 431, 373, 724, 993, 426, 427 and single groups listed as [n] in read/) - blocker: open-codes; pooled over all letters 5 Oct 2026 (pool.py), no occurrence forces one value; the decipherments NA 1.01.50 inv. 221/223 would settle them (not digitised)
- key values that read as nonsense in place (homophone clashes in key_M, e.g. 307, 1080), most in R1074 (0.75) and R1067 (0.79) - blocker: open-codes; would need the Lyonet key sheet or NA inv. 223 decipherments

Not a gap of unread text but a possible improvement (moved out of the gap list 14 Oct 2026): R1054, R1068, R1070,
R1073 and R1076 are measured on the DECODE parse (view.fix splits), not re-transcribed from the images; they already
measure 0.75-0.95, and their unread groups are the open codes above.

## Escalation

- [x] siblings: all R1052-R1076 and R2067 opened; eight Lyonet decipherments found among the images
- [x] clear-pages: the "clear" pages are Lyonet's decipherments, transcribed into plain/
- [n/a] known-keys: the key of this code was rebuilt from Lyonet's decipherments; the search for R1071's code (code C) is recorded in ../affry1757c/
- [x] print: De Leeuw 2000, Bussemaker 1906, Coquelle 1904 checked
- [x] key-rebuild: key_M.json voted from the alignments, inferred values in read/R*_new.tsv; key_X.tsv (5 Oct) pooled values
- [x] retry: 5 Oct 2026, R1072/R1074/R1067/R1064 re-transcribed from the images, open groups pooled across all letters, all letters re-measured with measure_sense.py (0.778 -> 0.823 of all groups)

## Contribution by WAINUT (21 Oct 2026)

WAINUT (a Dutch AI company, https://github.com/WAINUTAI) adds one source for the ten letters of this folder that have
no Lyonet sheet among the DECODE images: the Fagel registers in the Nationaal Archief, which hold their contemporary
decipherments. This section says where they are, how far this folder's key agrees with them, and which open groups,
key values and readings they settle or contradict. Nothing above is changed: key, transcriptions, readings and
profile are as they were. Where the registers disagree with a value, the evidence is given and the decision is left
to you. The files are in `wainut/`.

**How the work was done.** Google Gemini (gemini-4-argon) transcribed the register pages line by line from the NA's
full-resolution IIIF images (`wainut/register_clear.txt`). The alignment and the analysis were done with AI
language-model agents. The transcription of inv. 5186 scans 13R, 14L, 42R, 148R, 149L and 181L and of inv. 5187
scans 14R, 15L and 15R was checked line by line against the scans, and every register word quoted in this section is
on one of those pages. The other register pages are unchecked model transcriptions; only the automatic alignment uses
them.

**1. The deciphered letters are digitised in clear.** "Prior work" and "Remaining gaps" above say that the contemporary
decipherments survive in NA 1.01.50 inv. 221/223, which are not digitised. The registers of Fagel's papers, NA
1.10.29 (Archief Fagel) inv. 5186 (1757, 399 scans) and inv. 5187 (1758, 225 scans), are digitised. They are clerks'
copies, in clear, of d'Affry's letters in date order, each with a margin heading "Dat: ..." and "A: à R:" (or
"A: à B:"), most with the letter's number. All ten letters are there:

| Record | Letter | Register (NA 1.10.29) | Viewer, first scan |
|---|---|---|---|
| R1072 | No 123, 6 Jan 1757 | inv. 5186 scans 13R-14L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0013 |
| R1076 | No 124, 7 Jan 1757 | inv. 5186 scans 16R-17L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0016 |
| R1073 | No 133, 25 Jan 1757 | inv. 5186 scan 42R | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0042 |
| R1064 | No 136, 1 Feb 1757 | inv. 5186 scans 62R-63R | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0062 |
| R1067 | No 161, 1 Apr 1757 | inv. 5186 scans 148R-150L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0148 |
| R1068 | No 172, 26 Apr 1757 | inv. 5186 scan 181L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0181 |
| R1054 | 19 Jul 1757, to B. | inv. 5186 scans 248R-249L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0248 |
| R1070 | No 210, 22 Jul 1757, to B. | inv. 5186 scans 255R-256L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0255 |
| R2067 | 17 Jan 1758, to B. (No 283 above) | inv. 5187 scans 14R-15L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5187/file/NL-HaNA_1.10.29_5187_0014 |
| R1074 | its enclosure, "Extrait de la Lettre de Mr. Astier", margin "Du 11. Janvier 1758" | inv. 5187 scans 15L-15R | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5187/file/NL-HaNA_1.10.29_5187_0015 |

A scan number is the NA file number (`NL-HaNA_1.10.29_<inv>_<scan>`); L and R are the left and right page of the
opening. The registers also have entries for the letters whose Lyonet sheets are in `plain/` (for example No 171,
R1069); we did not align those.

The content of all ten letters was therefore known in clear in 1757-58, as it was for the eight Lyonet letters.

**2. Agreement of the key with the registers.** `wainut/align_register.py` aligns each ciphertext (`transcr/R*.txt`
where it exists, otherwise `cipher_U.txt` with view.py's split of run-together groups) with the register text of the
same letter, using this folder's key as `measure_sense.py` loads it (714 groups). A keyed group counts as matching
when its value stands at that point of the register text. The control is the same alignment with the key's values
shuffled among its groups (10 seeds); the denominator is all keyed groups in both cases.

| Record | groups | keyed groups | matching the register | share | shuffled keys: mean (max) |
|---|---|---|---|---|---|
| R1072 | 555 | 530 | 438 | 0.826 | 0.140 (0.170) |
| R1076 | 403 | 386 | 214 | 0.554 | 0.126 (0.153) |
| R1073 | 312 | 305 | 247 | 0.810 | 0.129 (0.154) |
| R1064 | 1,243 | 1,201 | 996 | 0.829 | 0.153 (0.180) |
| R1067 | 1,481 | 1,399 | 1,119 | 0.800 | 0.152 (0.172) |
| R1068 | 60 | 55 | 45 | 0.818 | 0.096 (0.145) |
| R1054 | 372 | 364 | 319 | 0.876 | 0.144 (0.206) |
| R1070 | 400 | 386 | 229 | 0.593 | 0.134 (0.148) |
| R2067 | 457 | 434 | 334 | 0.770 | 0.133 (0.171) |
| R1074 | 537 | 494 | 392 | 0.794 | 0.148 (0.170) |
| all ten | 5,820 | 5,554 | 4,333 | 0.780 | |

R1076 and R1070 are low because their first 157 and 139 groups get no register text. Those cipher pages begin in
mid-letter with a passage that the register has later in the same entry, and the alignment only runs forward. Among
the keyed groups that are aligned, 214/232 (0.922) of R1076 and 229/251 (0.912) of R1070 match; these two figures
describe only the aligned part of those letters (about 60%), not the whole letter. Many of the other
mismatches are the clerk's spelling and abbreviation (Roy for roi, "Sa Maj:", "Consr."), which are not key errors.

**3. Open groups that the registers settle** (`wainut/settled.tsv`; the script prints every occurrence). Of the 16
groups listed above as open (5 Oct 2026), 14 have at least two occurrences where the register has the same word.
Ten of them have no conflicting occurrence and are graded H in `settled.tsv`; 970, 1191, 890 and 431 are graded M,
because one occurrence conflicts or some aligned pieces sit at a segment edge (for 1191 only the two R1074 pieces
are clean):

- 970 projets: R1072 three times, "sur les Projets de l'Angleterre", "des Projets des deux Proprietaires", "tous les
  Projets proposés aux Ministres" (13R).
- 109 lundi and 651 mardi: R1067 "qu'il comptoit Lundi ou Mardi au plus tard" (148R) and "avant Lundi ou Mardi"
  (149L).
- 731 là dessus: R1067 "qu'il étoit là dessus impossible" (148R), and R1076.
- 708 impos: R1067 "impossible" (148R); R1072 "si c'est un Imposteur" (14L).
- 1191 sieur, written Sr: R1074 "le Sr Macdonald", "du Sr Macdonald" (5187 15R).
- 724 mes: R1067 "dans les termes", "les Yeux en larmes" (148R); with 1191, "Mrs. Pels" in R2067 (5187 14R) and
  "Messieurs" in R1067.
- 1082 ers: R1072 "des quartiers" (13R); R2067 "chez des Banquiers" (5187 14R).
- 373 voy: R1072 "Vous voyez" (14L); R1054 "Voyage".
- 993 doit: R1067 three times, one of them "ne me répondoit pas" (148R).
- 426 pouvoir: R1067 "pouvoir me procurer" (148R), "son Credit et son pouvoir" (149L).
- 427 mauvaise: R1067 twice.
- 890 détail: R1072 "un detail des quartiers" (13R), and R1064.
- 431 étrang: R1072 "les Cours étrangères" (13R), and R1064.

Two of these also have one occurrence that does not fit: 970 in R1074, where the register has "faire entrer en
France" (5187 15L), and 431 once in R1067. 1020 après has one clean occurrence (R1072 "Aprés bien des debats", 13R);
its R1067 occurrence stands where the register has "Aprés cette lecture" (148R), but the alignment splits the word.
869 stays open: it stands at "de tous les Plans de Campagne" in R1072 (13R), but in R1074 where the register has
"s'il y a moyen" (5187 15R).

Also: 1022 is very probably as (R2067 "Mr. Astier", "le Juif Boas", 5187 14R; R1074 "Mr. Astier", 15L), but the
aligned pieces are noisy ("ras", once "e"), so it is graded M. 307 has both values, forc
five times and pen twice ("recompenseroit", 13R; "une Pension", 14L). 1080 is not settled: R1074 opens "Extrait de la
lettre de M. [1022]tier du [1080] [110] ...", and the register's margin has "Du 11. Janvier 1758", but the alignment
gives the group no text.

**4. Key values the registers contradict.** `wainut/key_conflicts.tsv` lists the 64 keyed groups that disagree with
the register at least twice and more often than they agree. Many are spelling or abbreviation (premiers/premier,
roi/Roy, pensionnaire/Pensionaire, s.a.r. written out as "Son Altesse Royale"). Where the register has another word
at every occurrence:

- 675, key deux: vingt. R1073 "vers le vingt du Mois" (42R); R1074 "un Emprunt de Vingt Millions" (5187 15L); in
  R1067 it stands at the date "du 28" (148R).
- 1106, key succès: froid. R1073 "avec le même froid" (42R); R1067 "J'ai trouvé Mr le Pensionaire fort froid" (148R).
- 762, key égard: occasion. R1073 "à cette occasion voir le Consr. Pensionaire" (42R); also in R1064.
- 1151, key faire: parce que. R1073 "parce qu'il m'a repondu" (42R); R1067 "à Bruxelles parceque si la Navigation"
  (149L, where the aligned piece is partial); also in R1064.
- 556 ssi: contr- (contre three times, contraire twice); 116 pas: traité (3); 923 roit: ceux (3); 960 f: vu (3);
  1039 lies: et (7). These come from the alignment; we did not check them on the scans.

`wainut/open_groups.tsv` gives the register's word for 151 groups that have no value, for example 664 vendredi (R1068
"Il a passé Vendredi au Soir", 181L, and R1064), 94 la Haye (R2067 "étoit à la Haye", 5187 14R), 776 infraction
(R1073, 42R), 409 Allemagne, 803 consent-. A value seen once rests on the alignment alone and needs a look before it
is adopted.

**5. Readings that the registers correct.** In `read/R1073.md` (No 133; register 5186 42R):

| read/R1073.md | register |
|---|---|
| "je leur [413]ois", "Je lui ai [413]" | "je leur declarois", "Je lui ai declaré" (413 is déclar-) |
| "comme une [776] à la neutralité" | "comme une infraction à la Neutralité" |
| "à cet {égard} voir le {Pensionnaire}" | "à cette occasion voir le Consr. Pensionaire" |
| "les verroit avec {peine} leur s'engag{er}" | "les verroit avec douleur s'engager"; the key itself gives do-u-leur (599 527 399) |
| "avec le même {succès}" | "avec le même froid" |
| "Je suis [662 persuadé?]" | "je suis Seur" |
| "cette {aug}[1021]mentation" | "cette Operation" |
| "vous ra(?) vous [774] où {elle} est de {res}ter [507]ment [les] premiers" | "confirmera la Resolution ou Elle est de rester exactement Neutre" |
| "ver-bi-le[675] du [5?] {mois} prochain, que l'que be-he-n" | "vers le vingt du Mois prochain. Il semble que l'Abbé Senski" (the name is not clear on the scan) |
| "ne fournit pas des nouvelles" | "ne fournit plus de nouvelles" |
| "Il faut droit voir si cela ne va pas lon[g]" | "Il faudroit voir si celà ne va pas mieux" |

In `read/R1068.md` (No 172; register 5186 181L) the register reads: "Il a passé Vendredi au Soir un Courrier de Vienne
à Londres. Vous savez mieux que moi ce dont il est chargé. Mr. de Colloredo doit faire passer à Mr. Starrenberg ce
qu'on lui aura repondu." So 664 is Vendredi (the reading has "[664 hier?]"), 806 is mieux as the reading proposed,
and the recipient is Starrenberg (Starhemberg), not d'Arenberg. With the key the cipher gives "m d a re m be r g"; the
register implies 982 = st (key d) and 245 = n (key m), each from this one occurrence.

In `read/R2067.md` and `read/R1074.md` (registers 5187 14R and 15L-15R): "M. [1022]tier" is "Mr. Astier"; "J'ai eu
hier encore [223] i of [520] [1022]" is "J'ai eu encore hier le Juif Boas"; "[724] Sr [pe l s]" is "Mrs. Pels"; "étoit
à [94]" is "étoit à la Haye"; "le [1191 {Sr}?] Mac{do}na{ld?}" is "le Sr Macdonald".

**Caveats.** The registers are clerks' copies: they abbreviate and sometimes word things differently from the cipher,
so a mismatch is not always a key error. The alignment is automatic, and a piece at a segment edge can be a syllable
too long or too short. The ciphertexts are this folder's (`transcr/`, otherwise `cipher_U.txt`); we did not re-check
them against the KHA images. The register pages not listed under "How the work was done" are unchecked model
transcriptions.

**Files** (`wainut/`): `register_clear.txt` (register text of the ten letters, 20 pages); `align_register.py`
(Python 3 standard library and numpy; reads `../key_M.json`, `../overrides.json`, `../key_X.tsv`,
`../read/*_new.tsv`, `../transcr/` and `../cipher_U.txt`; run it from `wainut/` with `python align_register.py`,
about 30 s; it prints every number above and writes the files below); `align/R*.tsv` (each group, its key value, the
register piece and the status); `pool.tsv` (every group over all ten letters); `key_conflicts.tsv`;
`open_groups.tsv`; `settled.tsv` (written by hand from the script's output). No images: the scans are on the NA viewer
at the links above.
