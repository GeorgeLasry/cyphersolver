# Count of Cifuentes (Rome) to Charles V, 3 Sept 1534 (AGS Estado leg. 862 ff. 53–54; DECODE R9963) — NOTES

Status: no write-up. Read at the time; the f. 54r decipherment transcribed and the letter read from it on 23 Oct 2026 (re-read b25).

**23 Oct 2026, re-read (b25)**: all six DECODE images opened. The decipherment is record image 6 (file _005; image 5 is its faint verso). Transcribed line by line (`texts/f54_decipherment.txt`); reading = clear text + decipherment (`texts/R9963_reading.md`, English `texts/R9963_en.md`, log `texts/R9963_reread_log.md`). Checked against the letter at three anchors (clear islands, the clear numeral xviij closing a f. 53r cipher line, the repeated run "q L 20 4 m b" = embaxador); no sign-by-sign decode. Body 0.756 clean sentences (31/41), explicit holes 1.00. R9963 read; class already solved, method read from existing decipherment.

**22 Oct 2026, reading audit** (George Lasry's test): no text of R9963 is in the repository beyond the fragments quoted below; it is *decoded, not read* in profile.json, class already solved -> not read and method -> not solved until f. 54 is transcribed. The verdict below stands as history.

Earlier status (before the 22 Oct 2026 reading audit): no write-up

**Verdict: read at the time. The decipherment is bound with the letter as f. 54.** Catalogue entry 205 is resolved and
removed. Checked in one session on 2026-09-21.

## Sources

- DECODE R9963 ("Non-decrypted", 6 images, no DOC_ files). Record page in `decode/rec9963.htm`. The images were
  fetched with the shared cookie into the main checkout's `targets/cifuentes1534/decode/`. They are git-ignored.
- Not listed in Tomokiyo's AGS Estado page (`targets/vasto1527/prior/spanish2C_now.htm`).

## The document

| image | folio | content |
|---|---|---|
| 1 | 54v | address "A la S.C.C. Mt. del emperador y rey mi señor"; docket "Roma. A Su Mt. El conde de Cifuentes, iij de setiembre 1534" |
| 2 | 53r | "Sacra Ces. Cattho. Md." Opens in clear about the Pope's illness (Clement VII, who died 25 Sept 1534): "La mejoria de Su Sd. no ha ido adelante ... la calentura continua". Then a struck-out cipher line, glossed in the margin "tienen los fisicos poca esperança de su vida". Then c. 12 cipher lines, a clear island "y en este proposito me dixo que havia un mes que le", and 2 more cipher lines |
| 3 | 53v | c. 11 cipher lines; "Tambien" + 11 cipher lines |
| 4 | 54r? (the right half of the sheet) | 2 cipher lines, then clear: "Despues de escripto lo de arriba rescebi la carta de V. Md. de los 13 del passado ...". Dated "Rome iij Septembris MDxxxiiij", signed by Cifuentes |
| 6 (file _005) | 54r | **decipherment** in a secretary's hand: "Son tan negociadores estos Italianos que stando Su Sant. como esta ... me embio a dezir el duque de Ferrara por su embaxador ... y en este proposito me dixo que havia un mes que le dixo el embaxador de Francia que aqui reside ..." / "Tambien me dixo el dicho embaxador que le havia dicho el embaxador de Francia que el lantzgrave y duque de Saxonia venian a ... con el Rey de Francia para tractar medio de concierto ... el conde de Nassao ... Flandres ... España ..." |
| 5 (file _006) | 54v | blank verso (show-through of the decipherment) |

The decipherment keeps the letter's clear islands ("y en este proposito me dixo que havia un mes que le", "Tambien")
at the same places. The same cipher run ("q L 20 4 m b ...") stands where the decipherment reads "dixo el embax[ador]"
in both passages. So f. 54 is the decipherment of the cipher on ff. 53r–54r. It was read at the time.

## The cipher

A syllabic cipher of Charles V's Rome correspondence in the 1530s. Base signs (letter-like forms, T, ◊, ⊥, ✕, # and
others) carry small superscript digits 1–10 for the vowel or syllable. It is the type Luo (2021) reconstructs for
1530–39. No key table was built.

## Content

Clement VII's last illness: the doctors hold little hope for his life. Ercole II of Ferrara uses Cifuentes to press
for his investiture before the Pope dies. The French ambassador in Rome offers to settle Ferrara with Charles. There
are reports that the Landgrave of Hesse and the Duke of Saxony are treating with Francis I, and news about Nassau
going to Flanders.

## Why no write-up

The letter was read at the time, and its decipherment is on the next leaf. The only new result is identifying image 5
as that decipherment. Per CLAUDE.md this is `Status: no write-up`. For the DECODE status, see decode_updates/queue.json.

## Remaining gaps

- R9963: the contemporary decipherment on f. 54 - closed 23 Oct 2026 (transcribed, letter read)
- R9963 f. 54r l. 25: "el dicho [...]", short abbreviation - blocker: illegible
- R9963: cipher not decoded sign by sign - blocker: not-attempted (decipherment covers every cipher line)

## Escalation

- [n/a] siblings: one letter
- [x] clear-pages: decipherment bound as f. 54 found; not transcribed
- [n/a] known-keys: not needed
- [x] print: not in Tomokiyo's AGS Estado page
- [n/a] key-rebuild: not needed
- [x] retry: f. 54r transcribed and the letter read, 23 Oct 2026 (b25)
