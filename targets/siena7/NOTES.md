# Siena, Concistoro 2308 fasc. 2, no. 7 (DECODE R4796): an orator at Milan to the Officials of the Balìa, 1450s

Status: attempted, open. Key unknown; no filed key fits; nine values from the letter's own interlinear gloss.

Part of the Concistoro 2308 collection index: [`research/siena2308/`](../../research/siena2308/README.md). Split out
of the former `targets/siena1421` entry on 18 Oct 2026 under the one-key rule (George Lasry's report of 17 Oct 2026,
"one key, one entry"): no. 7 shares no key with any other piece of the fascicle.

## The document

- ASSi, Concistoro 2308, fasc. 2 "Lettere in cifra", pencil no. 7; DECODE R4796 (`Concistoro_2308_50`, 2 pp.,
  catalogued "1500-1599", no status).
- A long Italian despatch (c. 45 lines on p. 1) to the "Magnifici et excelsi domini Officiales Balie" of Siena, from
  an orator ("Servitor vester Orator Ant...", signature not legible with confidence). Line 4 names "messer Lionardo
  Benvoglienti" in the third person; the Duke of Milan is named; the postscript on p. 2 names the "conte Iacomo"
  (Jacopo Piccinino?), Genoa and Bologna. So the Sienese embassy at Milan, 1450s (Benvoglienti was ambassador there in
  1454; key R4750 of fasc. 1 is "a messer Leonardo e messer Antonio, ambasciatori a Milano, 1454"). Date line torn.
- The cipher is a block of 11 lines near the foot of p. 1 (L02-L12), with clear words between the runs. Faint
  interlinear letter glosses over parts of L04 and L08: a reader's partial decipherment.

George Lasry's report lists it under heading H, "Pieces with an interlinear or separate plaintext": "c. 330 symbols, a
few words with interlinear plaintext — unsolved as of 17 October 2026" (`lasry_report.md`).

## Files

- `transcripts/no07.txt`: transcription by agent J, 24 Sept 2026, with the sign legend and notes.
- `transcripts/no07.tok`: the cipher tokens only, 363 tokens / 45 sign types (measured; George Lasry counts c. 330
  symbols, the difference is in how look-alike and joined signs are split).
- `transcripts/no07_reading.txt`: agent G's sign-by-sign test of key R4750 against the gloss.

Moved here from `targets/siena1421/transcripts/` on 18 Oct 2026.

## What was tried (24 Sept 2026)

- Key R4750 (Milan ambassadors 1454) tested sign by sign on the image: does not fit. The L08 gloss contradicts it
  (R4750 gives 7 = o, 6 = i, + = s, 2 = f, c = u where the gloss has l, n, o, e, o); at least 73 of the 363 tokens
  (20%) are sign types R4750 lacks; its only e-sign would be 2.5% of the text. An earlier "milano" was a solver
  artefact from free signs and was withdrawn.
- Keys R4753, R4754, R4756, R4757, R4762 (transcribed in `research/siena2308/keys/`) fail the same gloss.
- The other filed keys of fasc. 1 compared by eye: no match.
- Homophonic annealing (`research/siena2308/homsolve2.py`) on 363 tokens / 45 signs: no convergence.
- 18 Oct 2026: the same solver with the nine gloss values fixed (12 restarts x 40,000 iterations, it-cinquecento order 3-4): no convergence; the restarts disagree and none reads (best -2.04 per token).
- The gloss gives a partial key: 7 = l, q = a, 6 = n, + = o, B3 = t, 2 = e, x = r, 8o = i, c = o (o has at least two
  signs, + and c): a homophonic cipher.
- 18 Oct 2026: compared with the key of no. 8 (`targets/siena8/`, c. 1440-41, rebuilt from its decipherment): a
  different key (no. 8 has 7 = d, + = c, 2 = a).

## Remaining gaps

- the whole cipher block (363 tokens) - blocker: too-short; homophonic with at least 45 signs, no filed key fits, and the gloss gives only nine values; ciphertext-only search does not converge at this length. Also unsolved by George Lasry (report of 17 Oct 2026). His recoveries of nos. 17 and 11 and R4794 (160-393 signs) show that "too-short" was too pessimistic for the pieces of this fascicle in general (`research/siena2308/README.md`, 20 Oct 2026); it stands here because he failed on this piece too.

## Escalation

- [x] siblings: every record of the busta opened (keys R4746-R4789, letters R4790-R4814, R1858); the Milan embassy key R4750 is the obvious sibling and fails.
- [x] clear-pages: the interlinear glosses on L04 and L08 used; no decipherment elsewhere in the fascicle; the p. 2 postscript is clear and not a decipherment.
- [x] known-keys: R4750, R4753, R4754, R4756, R4757, R4762 tested sign by sign; the other fasc. 1 keys by eye; the no. 8 key (c. 1440-41) compared.
- [x] print: Meister 1902, Cecchini 1952 inventory, Senatore 2009 (Benvoglienti's Milan letters); no printed decipherment found.
- [x] key-rebuild: homophonic annealing (homsolve2.py, it-cinquecento) without (24 Sept) and with (18 Oct, 12 restarts) the nine gloss values fixed: no convergence, restarts disagree, best -2.04 per token and no Italian.
- [n/a] retry: no key was extended, so there is nothing to rerun.

## Questions for George Lasry

- His count is c. 330 symbols, ours 363 tokens: is his CTTS transcription of no. 7 available, to rerun the anneal on it
  with the gloss values fixed?
