# Siena no. 9 — Castiglione this winter, with the King of Aragon's assent (DECODE R4798)

Status: read in part; key recovered from the adjacent plaintext (the decipherment written below the cipher in a second hand) by George Lasry with CTTS and Claude. The two cipher passages read; the final cipher group (Francesco?) and two code words open. Contributed result, filed here 18 Oct 2026.

Archivio di Stato di Siena, Concistoro 2308, fasc. 2 ("Lettere in cifra"), no. 9; DECODE
[R4798](https://de-crypt.org/decrypt-web/RecordsView/4798) (Concistoro_2308_52), catalogued "1500-1599", status N/A.
A slip with a key of its own (report section H, "Pieces with an interlinear or separate plaintext"; heading H groups
pieces by kind of plaintext, not by key: nos. 9, 13/16, 10, 7 and 8 are different ciphers).

## Source

George Lasry, "The cipher documents of Concistoro 2308, fasc. 2" (17 Oct 2026), consolidated report sent by email to
Daniel Bourdeau, pp. 33-34, section H. His section is quoted whole in [`lasry_report.md`](lasry_report.md); his key
figure is `docs/siena9_key.png`. His reading, translation and dating are not re-edited here.

## What the report gives

- **Status (Lasry):** "Solved (the two cipher passages). 15–17 October 2026, by George Lasry with CTTS and Claude:
  transcription by Claude, held in CTTS; key recovered by Claude from the interlinear plaintext written on the slip in
  a second hand ('uno altro anno', 'Chastiglone questa vernata'), which fixes the two passages sign for sign."
- **Ciphertext:** 53 cipher symbols in 3 lines (manuscript lines 5, 6 and the right end of 8), inside Italian clear text.
- **Key:** 33 distinct signs (31 letter signs, two separators); homophonic, five signs for a, three each for e and o,
  two each for r, t, u; one sign probably a null; two clear code words, Stella = the King of Aragon and nichil = ?
  (la pratica?).
- **Reading:** "[la pratica?] [di?] Chastiglone questa vernata con lo sentimento di [re d'Aragona] e nutrire questa
  guerra uno altro anno Francesco? i?" (cipher: Chastiglone questa vernata; uno altro anno; Francesco? i?).
- **Dating (Lasry):** 1440s-1450s?, Castiglione (della Pescaia?) held by Alfonso V from 1447; the winter of 1447-48
  fits best; unverified.

## Measure

George Lasry's reading, letters in the cipher passages: *Chastiglone questa vernata* (24) and *uno altro anno* (12)
are read without a query, 36 letters confirmed by the contemporary decipherment; *[di?]* (one sign) and the final
group *Francesco? i?* (George's key: f?, a?, co? signs and three letter signs, plus i?) are doubtful. Our count:
36 of 44 letter values read without a query (81.8%), with the code words nichil and Stella left out (clear words).
This is a count on his reading text, not on the 53 symbols (nulls and separators not in the plaintext).

## Project's earlier attempt (siena1421 survey, 24 Sept 2026)

Agent J transcribed the slip (`transcripts/no09.txt`, 46 cipher tokens / 28 sign names, moved here from
`targets/siena1421/transcripts/` on 18 Oct 2026) and closed it as too short for ciphertext-only. Agent J took lines 7-8
for ordinary clear text in a second hand ("la . pri ... L glone questa uernata ... d(e)l re (d')Ragona", "e mutui q(ue)sta
guerra uno asse(dio) o anno") and noted that they "might instead be a partial decipherment"; George Lasry's reading shows
they are the decipherment of lines 5-6. Nothing of the project's attempt is claimed in the reading.

## Disagreements with the repository

- **Date.** The siena1421 notes had "c. 1495-1516?" (Correggio, Carpi, Rimini, re di Ragona); the report has
  1440s-1450s?, unverified. Both are conjectures from the persons named; the report's Castiglione/Alfonso V reading
  is followed here, unverified.
- **The second hand's lines.** Repository: clear text. Report: the decipherment. The report is followed.
- **Counts.** Repository 46 cipher tokens (28 names); report 53 symbols (33 signs). The report is followed.
- DECODE: "1500-1599", no sender, no status.

## Remaining gaps

- the final cipher group at the right of line 8 ("Francesco? i?", about 7 signs) - blocker: too-short; outside the second hand's decipherment, single-occurrence signs (f?, a?, co?)
- the sign read [di?] before Chastiglone and the clear code word nichil (la pratica?) - blocker: too-short; single occurrences; the decipherment line reads "la . pri" over them
- the date, the writer and the addressee ('V. S.'); Guido and 'da Rimino' in the clear lines - blocker: no-key-material; nothing on the slip names or dates them

## Escalation

- [x] siblings: every piece of fasc. 2 opened (siena1421 survey); no other piece in this key.
- [x] clear-pages: the second hand's lines 7-8 are the decipherment (George Lasry); used for the key.
- [x] known-keys: the fasc. 1 key sheets compared by eye on 24 Sept (siena1421); none fits. Stella = the King of Aragon recalls R4751 (Senenses = Stella), a different assignment.
- [x] print: Meister 1902, the 1952 inventory; Ryder's Alfonso the Magnanimous (1990) cited for the context.
- [n/a] key-rebuild: the key is fixed by the contemporary decipherment wherever it covers the cipher; the uncovered signs occur once.
- [n/a] retry: no key extension was made here, so nothing to rerun.
