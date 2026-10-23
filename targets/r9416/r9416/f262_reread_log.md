# Re-reading log, R9416 f. 262 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b32)

## Starting point

Reading audit (22 Oct): outcome.texts entry 1 (f. 262) "decoded, not read": the contemporary interlinear gloss
(`gloss.txt`) reads on page B but page A had "..." and [?] in most lines and A09-A11 carry no gloss; the cipher signs
of f. 262 had never been transcribed. Clean-sentence share before: gloss only, page A not assembled (no reading).
The audit's own fix: key the signs from page B's gloss and read page A from its signs.

## What was done

1. **The DECODE record.** R9416 fetched logged in (b28_fetch.py): four images (P1 = f. 262 page B, P2 = page A, P3-P4
   f. 263), no attachment or comment. No printed edition (kaa4591 notes).
2. **Image.** P1 and P2 turned 180 deg, deskewed (0.75 and 1.5 deg), cut into one image per cipher line at full
   resolution (3468 px wide; scratchpad only, the images are not public domain), with the faint gloss above each line
   visible in the same crop.
3. **Key** (`f262_key.md`). Page B lines B01-B07 aligned sign by sign with the gloss ("thun etzlich practick durch
   hern angefangen", "weiter in gang zu bringen auch mein aus-", "stendig pension von siben iaren zu erfodern bit",
   "demnach eur furstlich gnad mir in abschlag", "meiner besoldung funfzig gulden gen straubing", "zum oberrichter",
   "gnad solichs fur gut ansicht verordnen dan ich"): a simple substitution with homophones for a, e, u, b and code
   signs, words separated. Every value adopted recurs on page A with the same value (evidence words in the key file).
   Two shape families carry more than one value and are read by the sense of each word (look-alikes): the
   circle-with-stroke / looped-6 family (w, b, p) and the 4-shape (u, o).
   New values not in the gloss: # = ss/ß (dermassen, diß), ƛ = n(n) (dan, twice), x = i (ainfeltigs, weil).
   Codes left unidentified: large X (2x), ⊼ (2x), a G-shaped sign (1x).
4. **Page A read from its signs**, all 25 lines, including the three lines with no gloss (A09-A11: "minkwicz und ander
   geferden halb durch slesi und [?belen] auch nit komen die weil aber [X] treflich ansachen gelegen und [⊼] entlich
   vor hat zu") and the faint ones. The signs correct the gloss transcription in several places: A03 "unter" (not
   "untiden"), A13 "mit ainem" (not "nit allain"), A18 "welt dan [⊼]" (not "wolt ia"), A19 "fuer die turcken bis in"
   (not "euer die kaysken bei in"), A22 "schonen" (not "wonen"), A16 "den bartlen von [?eschelkamb] het dohin
   gefertigt", A20 "in schein sein botschaft".
   The sign-by-sign decoding was written straight to letters while reading each crop; no separate sign-label file was
   kept for f. 262 (a gap: the decode cannot be re-run mechanically; the key file and the crops make it repeatable).
5. **Page B** follows the gloss; B01-B07 checked against the signs (agree, with "funfzig", "strabing" and "dan" from
   the figures); B08-B15 not re-checked sign by sign (not-attempted).
6. **Word-by-word check.** Each word of page A was read from its signs; words where a sign is doubtful or the value
   rests on sense only are bracketed ([?vertraue], [?zuzrehen], [?gewornet], [?boit], [?belen], [?eschelkamb],
   [?gestalten], [?wag]). No word is supplied.
7. **Look-alike alternates.** Letters resting on a member of a multi-valued shape family chosen by sense: the
   w/b/p family about 14 times and the u/o 4-shape about 5 times on page A, some 19 letters of roughly 1,000 (about
   2%).
8. **Score** (b17_score.py, LANG_=de, reading body, with the code signs [X], [⊼] counted as holes): **0.444 (12/27)**
   plain (early New High German spelling: genediger, komt, geschrai, geferden ...); explicit holes only (HOLES=1)
   **0.852 (23/27)**. Reader's judgement: the letter reads as a whole: the writer could not get through Austria and
   Styria (troops everywhere, a messenger struck down), nor through Silesia and Poland because of Minckwitz and other
   dangers; Italian and Spanish foot are to move through Styria and down the Danube into Hungary; the duke should have
   sent Bartlen von Eschlkam; four thousand Turks are said to be out under cover of an embassy; the writer means to
   travel on, pursue certain dealings, claim seven years' pension, and asks for the Oberrichter post at Straubing.

## Result

Read (grade B). The context (Minckwitz's feud, Turks in Hungary, Spanish and Italian troops for Hungary) fits the
1530s and the f. 263 report of c. 1533-34.

## Open

- Codes X, ⊼ and the G-sign - blocker: no-key-material (each 1-2 times, no gloss over them).
- Page B lines B08-B15 sign by sign - blocker: not-attempted (the gloss reads; not needed for the reading).
- A sign-label transcription of f. 262 - blocker: not-attempted.
