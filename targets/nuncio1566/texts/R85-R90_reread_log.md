# Re-reading log, R85-R90 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b09)

## Starting point

Reading audit (22 Oct): all six records "decoded, not read": the beam search under Lasry's polyphonic key
(`decrypt_raw.txt`, word-split copies in `texts/R8x_decryption.txt`) gave Italian fragments between garbled strings in
nearly every line ("colospo", "rimpesti e beuersi", "allcgcatolica"). _check_reading.py on the old decryption files:
R85 0.29, R86 0.27, R87 0.27, R88 0.21, R89 0.24, R90 0.40 clean.

## 1. Is there a text already?

- **DECODE images.** All page and "cleartext" images of R85-R90 fetched with the project's DECODE cookie
  (`research/reading_audit/b09_fetch.py`, 39 files) into the session scratchpad only (ASV images, not in the repository):
  R85 163r, 163v, 164r, 164v, 167r, 167v; R86 237r, 237v; R87 244r, 245r, 246r, 247r, 247v, 248r, 248v, 251r, 251v; R88
  299r, 299v, 300r, 300v, 302r; R89 313r, 313v, 315r; R90 323v, 325r, 325v, 326r. Contact sheets first, then strips at
  native resolution.
  - **R87: f. 251r is the contemporary decipherment** (DECODE labels it "cleartext"; 251v.jpg is a second photograph of
    the same leaf). The top five lines are eaten away; it stops at "resistere" (cipher f. 250r row 13). Transcribed:
    `R87_decifrato_f251r.txt`.
  - **R90**: its second sentence is in clear on f. 302r, the end of the copy of the 4 Nov 1567 letter that carries R88
    ("Sarebbe forse bene che S. M. Cat.ca facesse sapere alla Regina di Francia ..."). Transcribed:
    `R90_clear_f302r.txt`. R90 also continues R89 word for word ("da persona molto bene | instrutta ..."), and R88 and
    R89 are two cipher copies of one text: the three records read against each other.
  - R85 (covering letter ff. 163r-167r, "Di Roma a 8 di Gen.o 1567. Sarà con questa un poco di cifra"), R86 (ff. 237r-v,
    letter of 25 July held "fino a 2 d'Agosto", "un poco di cifra qui inclusa"), R88 (ff. 299r-302r, 4 Nov 1567, "Con
    questa sarà una Cifra"), R89 (ff. 313r-v, a copy of the same 4 Nov letter, and 315r, a different letter of 29 Dec
    1567), R90 (ff. 325r-326r, a third copy of the 4 Nov letter, "Con questa sarà una Cifra"; address 323v): clear
    letters only, no decipherment, no interlinear glosses. The words in the left margin of f. 165r are the line ends of
    f. 164v, not glosses.
- **Print.** Serrano, *Correspondencia diplomática entre España y la Santa Sede durante el pontificado de S. Pío V*
  (1914) may print these letters: not reachable (HathiTrust 403, not on archive.org; as in alessandrino1568's log). Not
  needed for a reading now; recorded as unchecked.

## 2. Key, from the R87 decipherment and the copies

`reread_b09_align.py` (copied from alessandrino1568's `reread_aless_align.py`) aligns a reading with one page's figures
by dynamic programming and marks every disagreement; `research/reading_audit/b09_align.py` runs it on each "### f."
section of a reading. `reread_b09_decode.py` is alessandrino1568's extended beam decoder (9 = con, 00. = et, X0Y codes,
3060 -mente, 4020 come, 5090 qui, doubled letters once), run with `--rows` on every page as the first draft.

| finding | evidence |
|---|---|
| 8010 = [la] Regina [di Francia] (the Queen Mother), not "Re di Francia" | R87 dec. "la Reg.na di Francia" twice; R88/R89 "ingannata" (fem.), R90 = f. 302r "alla Regina di Francia" |
| 4010 = S.M. (the King: Philip II in R87, Charles IX in R85/R88/R89), not "Sua Santità" | R87 dec. "dal Re [Catt.co]" for 7 4 0 4 0 1 0; R88/R89 "se S.M. facesse mettere in prigione il Conestabile ... li faria tagliare il capo"; R85 "Regina di Francia et S.M. hanno desiderio" |
| 1020 = essere | R87 dec. "di essere invitata"; R89 "non può essere altramente" |
| 1040 = lettera (as in alessandrino1568 R95) | R89 "capitulo di lettera venuta", "detta lettera viene scritta" |
| 8030 = religione | R87 "ristaurare la religione" (dec.); R85 twice |
| 8070 = ugonotta | R88 6 0 8 0 7 0 where R89 spells 1 3 5 6 1 4, u-g-o-n-t-a |
| 8080 = heretici (written 8 0 8) | R87 "dependente da heretici o debole" (dec.) |
| 8090 = havere | R87 "di havere ottenuto", "possa più havere" (dec. "havere"); R89 "di non havere voluto credere" |
| 3040 = Fiandra | R87 dec. "in Fiandra" |
| 3 0^. 9 = qua | R87 "quanto più presto" (dec. "quanto più") |
| "colospo" = colloquio | 8 5 4 5 + 5 0 9 (qui) + 5; R87 dec. "colloquio" |
| 2 0 9 = "chi" as a syllable | R85 "richiesti" (7 2 2 0 9 6 5 1 2), as Chiesa/chinea in alessandrino1568 |

Where the R87 decipherer and the figures differ, the figures are followed ("dal qual si crede" for his "ma quel si crede",
"ma perché" for "il perché", "esso pretenso arcivescovo" for "detto pretensore Arc.vo", "o dependente" for "et
dependente"); 4 of 1,000-odd figures disagree, one-letter clerk's slips (privatione, resistere with 2 for t).

## 3. Readings on the figures

Each page read row by row against the figures, with the image checked at every break (strips at native resolution of
IMG_R85_I643, R86_I650, R87_I653-655, R88_I665-666, R89_I672-673, R90_I677). Twelve transcription labels corrected
(`R85-R90_corrections.tsv`; corrected files `R85_transcription_corrected.txt`, `R86_...`, `R87_...`), e.g. R86 row 1 "2 0
2 0 ... 4 0 2 0 9" is 1 0 1 0 (N.S.) ... 4 0 1 0 9 0 (a V.S.), which turned the opening "il disegno di [con] per dira"
into "Il disegno di N.S., per dirlo a V.S. sola"; R85 row 2 had four figures too many before "abboccarsi con Re".
Ticked underlines in R85 (under "dirli", "è ben vero che", "admettere anzi procurare", "ascoltar") were first taken for
deletions; the words they cover are needed by the sense, so they are a reader's marks, and the words are kept.
Failures and doubts kept in the readings: R85 [3050] after "sarà per", [3020] in "che [3020] non si diffidi" where
"quando" does not fit, "come […] da più bande" (a blotted figure), "di fare […] altra cosa" (a ticked run of 6s and 0s),
"[?di] Re"; R86 "[?quel] fatto", "[?havere]" (8090 where the sense wants "dare"), "[2020] infetti", "[?via]", one stray
figure before "loro"; R87 "[?poi]" at the end; R88 one unread group 7 3 8 (301v row 11).

## Result

| record | before (audit) | after: clean-sentence share of the reading body | rests on |
|---|---|---|---|
| R85 | 0.29, decoded, not read | 1.00 (17 sentences), 4 holes, 2 codes | figures, 8 labels corrected on the image |
| R86 | 0.27, decoded, not read | 1.00 (15), 1 code, 4 partly carried words | figures, 3 labels corrected |
| R87 | 0.27, decoded, not read | 1.00 (38), 1 partly carried word | decipherment f. 251r + figures |
| R88 | 0.21, decoded, not read | 0.93 (28), 1 hole | figures + R89 copy where the paper is damaged |
| R89 | 0.24, decoded, not read | 0.92 (26), none | figures + R88 copy |
| R90 | 0.40, decoded, not read | 1.00 (4), none | figures + clear text f. 302r |

(`python research/reading_audit/b09_score.py R85 ... R90`: _check_reading.py on the "## Reading" body only. The
sentence counts are inflated by "N.S." and "S.M."; every sentence has at most one hole in ten words.)
Word-by-word alignment (`b09_align.py`): R85 169/190, R86 155/164, R87 437/448, R88 326/361, R89 336/349, R90 45/48
words carried; every word not carried is bracketed, a damaged figure read from the other copy (R88), a one-letter slip
listed in the notes, or a dotted zero the transcription lost.

## Still open, and why

- R85: codes 3050 and 3020 (this use), one blotted group, one ticked run before "altra cosa": no key material for the
  codes (not in Lasry's table, no other occurrence), the rest illegible on the image.
- R86: code 2020 (only occurrence), 8090 in an unexpected sense, one stray figure: no key material.
- R87: the closing "9 5 2" ("[?poi]"): too short to settle.
- R88: 7 3 8 (301v row 11): illegible / no counterpart in R89.
- Serrano 1914 not checked (access).
