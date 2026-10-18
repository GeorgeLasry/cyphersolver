# Siena, Concistoro 2308 fasc. 2, no. 21 (DECODE R4809): an informal letter "Karissimo come padre" (15th century)

Status: attempted, open. Key unknown; 107 cipher tokens, too short without a key; no filed key fits.

Part of the Concistoro 2308 collection index: [`research/siena2308/`](../../research/siena2308/README.md). Split out
of the former `targets/siena1421` entry on 18 Oct 2026 under the one-key rule: George Lasry's report puts no. 21 under
heading D, "Fifteenth-century Sienese ciphers, one key each", so it shares no key with nos. 4, 14, 19 and 25.

## The document

- ASSi, Concistoro 2308, fasc. 2 "Lettere in cifra", pencil no. 21; DECODE R4809 (`Concistoro_2308_63`, 1 p.,
  catalogued "1500-1599", no status).
- A short informal letter opening "Kar(issi)mo come padre" (no salutation to the Signori), in fast faded cursive.
  L01-L02 are mostly clear ("... la nostra lettera per ... scripsi che per ... vi convenne etc."); a name in L01 is
  written with cipher signs; L03-L04 are mostly cipher with clear words between. Date line "A di .. agosti(?) ..."
  (no year, no place). Signature: a cipher group followed by clear "vostro".
- The signs: crosses and bars (+, double-barred cross, three uprights crossed by a bar), squares (plain, divided,
  filled with three uprights), Λ, a hooked stroke, f, and letter- and digit-like signs.
- Dating: George Lasry's heading D says fifteenth century; the project had none.

George Lasry's report: "No. 21 = R4809 — 109 symbols — unsolved as of 17 October 2026" (`lasry_report.md`).

## Files

- `transcripts/no21.txt`: transcription by agent J, 24 Sept 2026, with sign legend and notes (moved here from
  `targets/siena1421/transcripts/` on 18 Oct 2026).
- `transcripts/no21.tok`: the cipher tokens only, extracted from it on 18 Oct 2026: 107 tokens / 35 sign types
  (measured; George Lasry counts 109 symbols).

## What was tried

- 24 Sept 2026: the alphabets of the keys of fasc. 1 compared by eye with the sign set: no match. The cross-and-box
  signs recall no filed key.
- 24 Sept 2026: homophonic annealing (homsolve2/homsolve3) on the short pieces: no convergence at 107 tokens.
- 18 Oct 2026: compared with the key of no. 8 (`targets/siena8/`, c. 1440-41): a different sign set.

## Remaining gaps

- the cipher in L01, L03-L04 and the signature (107 tokens) - blocker: too-short; about 35 signs over 107 tokens, no filed key fits and there is no gloss or decipherment.

## Escalation

- [x] siblings: every record of the busta opened (keys R4746-R4789, letters R4790-R4814, R1858); no other letter of this writer found.
- [x] clear-pages: the clear lines are context only; no decipherment on the record.
- [x] known-keys: the fasc. 1 keys compared by eye; the no. 8 key compared: different.
- [x] print: Meister 1902, Cecchini 1952 inventory: no decipherment.
- [x] key-rebuild: homophonic annealing: too short to converge.
- [n/a] retry: no key was extended, so there is nothing to rerun.
