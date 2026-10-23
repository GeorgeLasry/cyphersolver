# Re-reading log, R1026 and R1027 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b24)

## Starting point

Reading audit (22 Oct): both "decoded, not read". `reading_R1026.txt` / `reading_R1027.txt` came from `resolve_j.py`
(21 Sept), which tried every digit for each DECODE `J+` sign and let a French 6-gram model choose; the result had
garbled runs in most sentences ("comme ils mauvais oyent A differer d' la") and nine "open codes". `_check_reading.py`:
0.00 counted as a reading.

## 1. Is there a text already? No

- DECODE R1026, R1027 fetched again with the project cookie (`research/reading_audit/b24_fetch.py`, scratchpad): page
  images (5275-5277) and the transcription only; no attachment, no comment, no plaintext.
- The printed Van de Spiegel material in the main checkout (`brievenennegoti0[1-3]spiegoog.txt`, Brieven en
  negotiatien; `mrlaurenspieter0[0-3]middgoog.txt`, Vreede) grepped for Van Reede and "outre mer": nothing of these
  letters. Colenbrander's Gedenkstukken not searched (the letters now read on the figures).
- Neighbouring records: R1028 (undated Van Reede despatch with its plaintext) is the control already used; R1029,
  R1030 are other letters, not copies of these.

## 2. Read on the image

**The `J+` sign.** Zoomed strips of the three pages (`b24_strips.py`) show one glyph, a 1 with a hooked foot, beside
the plain 1 and two shapes of 3 (round, and flat-backed like a B). Read as 1 at every occurrence (77 in R1026, 24 in
R1027) it gives a key word that fits each time ("257J JJ8J" = 2571 1181 "au Roi", "375J" = 3751 "dix", "JJ27" = 1127
"question"); J=3 gives "au reste il n'est". The 21 Sept per-group choice (0, 1, 2, 3 or 4) was the garble.

**The key.** The DECODE transcription of R1024 lacks 1-50, 331-370, 1201-1250, 2751-2800, 3131-3160, 3621-3660. On the
key images (P6, P11, P12, P19, P21, P25) each is a block headed "Nonvaleurs depuis … jusqu'à …": nulls. That disposes
of the "open codes" 1250, 331 (x3), 2800 (x2), 3160, 3660 (x2), 3153, 2751 (x2), 50, 1201: they open and close the
letters as padding. Number-column slips fixed by page order (`b24_vr_key.py`): 3637 "cependant" is 2637 (the
recurring "open code"), 3635 = 2635, 1615 = 2615, 2520 = 2530, 3530 = 3539, 3577 = 3677, 3230 = 3730. Word slips read
on the key images and adopted because they hold at every occurrence:

| value | evidence |
|---|---|
| 54 = est (DECODE "es") | key P12 "53. es / 54. est"; R1026 "la reponse est arrivée", "envoyer separement est supprimé" |
| 2142 = paroit, 2143 = paroitre (DECODE: 2142 paroitre, 2143 missing) | key P15 "2141 paroissoit, 2142 paroit, 2143 paroitre, 2144 parole"; R1026 "elle me paroit bonne" |
| 4910 = que (DECODE "quo") | key P33 "4909 Q. 4910 que"; R1027 "croit encore que l'Imperatrice" |

**Labels** corrected on the letter images (`R1026_corrections.tsv`, `R1027_corrections.tsv`, corrected group files
`*_transcription_corrected.tsv`): R1026 `J?00` = 100 (me), `21423068` = 2142 3068 (two groups run together),
`4 4 3 8` = 4438 corrected by the writer to 4433 above it (je ne), `51?` = 513 (ce qui; flat-backed 3), `308?9` = 3089
(ce); R1027 `3?089` = 3089, `1?1021` = 1021 (ou), `0969` = 1969 (Imperatrice). Every other R1027 group re-read on
the strips; DECODE's digits stand.

**Bar marks.** The transcriber recorded bars above (`^_`) and below (`__`) groups. Read from the letters (no
instruction sheet on the record), they are inflection signs: a bar above cuts final letters from the key word (prier
→ prié, demander → demandé, soin + R → soir, motif + ver → motiver, Sieur + N → sien, persister + oyent → persistoyent,
entendre → entend, article + ul + er → articuler, temperer + or + air + E → temporaire, seulement → seule, laissai + nt
→ laissant, zèle → zel in Cobentzel, gouter / réunir / ses → vigoureuse); over the first digit it cuts the front (749
"le Comtte de Finkenstein" after "du"); a bar below adds the ending (Ministres, sentiments, heures, possessions,
Puissances, nouvelles, Messieurs, capots, a faite, connue, Turcs, propositions); an accent stroke over a group gives é
(entre' es = entrées, de ci de' = decidé). The number of strokes does not always match the letters cut (seulement
with three or four). Failure: `soient` + two bars (R1026 group 97) gives "soie", read `[?soit]`; `fournir` with bars
above and below (group 133) read `[?fournit]`.

Decodes group by group: `R1026_decode_b24.txt`, `R1027_decode_b24.txt` (`b24_vr_build.py`).

## 3. Readings and word check

`R1026_reading.md`, `R1027_reading.md` (English `R1026_en.md`, `R1027_en.md`). R1026's clear passages (the audience,
the ceremonial, the dinner invitation, the close) read from the image; DECODE's cleartext lines are garbled.
Names spelt in key syllables joined: se gu R = Segur, co be nt zel = Cobentzel, ke L ler = Keller, in de ci se =
indecise.

Word check (`b24_vr_align.py`): every word of the cipher parts is in the stream of decoded key words or is a
bar-marked form listed above; no supplied word. Look-alike count: R1026 403 of 1,388 decoded letters come from groups
with the hooked 1 (one identification, holding at all 77 places), 24 from the five corrected labels; R1027 118 of 601
and 15.

## Result

| record | before (audit) | after: clean-sentence share of the body (`b17_score.py`, LANG_=fr) | explicit holes only (HOLES=1) | rests on |
|---|---|---|---|---|
| R1026 | 0.00, decoded, not read | 0.735 (25/34) | 0.971 | figures under R1024, J+ = 1, nulls, 4 key slips, 5 labels, bar marks |
| R1027 | 0.00, decoded, not read | 0.867 (13/15) | 0.933 | the same, 3 labels |

Both set read, grade B (the bar-mark convention is inferred from the letters). Open: R1026 [?soit], [?fournit],
[?énonçoit], R1027 [?decidement] (slips in the figures; no key material for the marks), and three faint words of
R1026's clear passage (illegible on the 1240-px image).

Content corrected by the reading: R1026's "Prince d'Anhalt Schlaumbourg", "Amsterdam", "Novembre", "la Duchesse" and
"Guerres" were artefacts of the 21 Sept digit choices; the letter is about Hertzberg's own report, article seven struck
out to please England, the treaty made temporary for twenty years, and Van Reede's audience. R1027's "Russian
ministers" are Ségur and Cobenzl; the envoy without an answer is Keller.
