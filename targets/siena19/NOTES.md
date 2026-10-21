# Siena, Concistoro 2308 fasc. 2, no. 19 (DECODE R4807): Sienese envoys waiting on the "S. Capitano", 9 March (1440s)

Status: attempted, open. Key unknown; 118 cipher tokens, too short without a key; no filed key fits.

Part of the Concistoro 2308 collection index: [`research/siena2308/`](../../research/siena2308/README.md). Split out
of the former `targets/siena1421` entry on 18 Oct 2026 under the one-key rule: George Lasry's report puts no. 19 under
heading D, "Fifteenth-century Sienese ciphers, one key each", so it shares no key with nos. 4, 14, 21 and 25.

## The document

- ASSi, Concistoro 2308, fasc. 2 "Lettere in cifra", pencil no. 19; DECODE R4807 (`Concistoro_2308_61`, 1 p.,
  catalogued "1500-1599", no status).
- A short report in Italian to the "Magnifici domini domini mei singularissimi" by Sienese envoys ("scrivemo", "siamo
  stati", "partiamo") who have pressed the "S. Cap(itan)o" several times for leave to depart; he keeps them waiting for
  an answer; "domattina partiamo col nome di Dio". Written on 9 March (the day after "octo al presente di marzo"),
  year not stated; no place; the letter ends in cipher, so no signature.
- Four lines of cipher (L07-L10) with clear phrases between the runs: "e in effecto afferma", "per ogni modo e
  l'altro", "che venne", "per ogni modo / se altro non nascera". The cipher is written in a formal upright hand, sign by
  sign, distinct from the cursive clear text.
- Dating: George Lasry gives "1440s"; this project had no year (24 Sept 2026). The basis of his date is not stated in
  the report.

George Lasry's report: "Sienese envoys, 9 March, 1440s, 112 symbols — unsolved as of 17 October 2026 (names only)"
(`lasry_report.md`). "Names only" is not explained in the report.

## Files

- `transcripts/no19.txt`: transcription by agent J, 24 Sept 2026, with sign legend and notes (moved here from
  `targets/siena1421/transcripts/` on 18 Oct 2026).
- `transcripts/no19.tok`: the cipher tokens only, extracted from it on 18 Oct 2026: 118 tokens / 37 sign types
  (measured; George Lasry counts 112 symbols).

## What was tried

- 24 Sept 2026: the alphabets of the fifteenth-century keys of fasc. 1 compared by eye with the sign set (digits,
  inverted triangle, B-like signs, letter-like signs): no match.
- 24 Sept 2026: homophonic annealing (homsolve2/homsolve3) on the short pieces: no convergence; 118 tokens over 37
  signs is below what ciphertext-only search needs.
- 18 Oct 2026: compared with the key of no. 8 (`targets/siena8/`, c. 1440-41, rebuilt from its decipherment), the
  other 1440s key in the fascicle: a different sign set (no. 19 has digits and the triangle, no. 8 neither).

## Remaining gaps

- the four cipher lines (118 tokens) - blocker: too-short; about 37 signs over 118 tokens, homophonic-looking, no filed key fits and there is no gloss or decipherment. Also unsolved by George Lasry (report of 17 Oct 2026). His recoveries of nos. 17 and 11 and R4794 (160-393 signs) show that "too-short" was too pessimistic for the pieces of this fascicle in general (`research/siena2308/README.md`, 20 Oct 2026); it stands here because he failed on this piece too.

## Escalation

- [x] siblings: every record of the busta opened (keys R4746-R4789, letters R4790-R4814, R1858); no other letter of these envoys found.
- [x] clear-pages: the clear phrases between the runs are context, not a decipherment; none on the record.
- [x] known-keys: the fasc. 1 keys compared by eye; the no. 8 key (1440s) compared sign by sign: different.
- [x] print: Meister 1902, Cecchini 1952 inventory: no decipherment.
- [x] key-rebuild: homophonic annealing: too short to converge.
- [n/a] retry: no key was extended, so there is nothing to rerun.

## Questions for George Lasry

- What dates no. 19 to the 1440s, and what does "names only" mean: names identified in the cipher, or a cipher of
  names only?
