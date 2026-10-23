# Castelcicala 1816-23: re-read log for the 23 documents decoded, not read (22 Oct 2026, Claude Opus 5.5, batch mix1)

Brief: research/reading_audit/REREAD_BRIEF.md. The documents: R9553-R9567, R9569, R9570, R9579, R9582-R9585, R9587
(the two glossed 1823 letters R9571 and R9589 already read).

## 1. Is there a text already?

- Contemporary decipherments in busta 2337, all already transcribed in `transcripts/` and used for key.tsv: R9566 p. 3
  ll. 1-9 (despatch 3874: Decazes, Onís, the Floridas and Cuba), R9569 p. 1 ll. 8-16, R9571 and R9589 (whole).
  No other record of the 23 has a gloss (every transcript header checked: "P:" gloss lines occur only in R9566 p. 3,
  R9569, R9571, R9589). The neighbouring records of the box (R9550-R9552, R9568, R9572-R9581, R9590-R9591) are
  1850s-60s material in other codes (NOTES, first pass).
- Print: no edition of Castelcicala's 1816-23 despatches (web search 21 Sept 2026; Treccani DBI; Tomokiyo).
- The code book ("Cifra della Segreteria di Stato", headed so on R9553): not on DECODE (R9532-R9541 are 1859-60
  consular keys), not in print; ASNa Esteri only.

## 2. Read on the key

Coverage of each document by key.tsv (groups with a value or a five-figure null / all groups) and the longest run of
consecutive known groups (measured 22 Oct 2026 with corpus.py and key.tsv):

| doc | groups | known | share | longest known run |
|---|---|---|---|---|
| R9553 | 254 | 102 | 0.40 | 5 |
| R9554 | 841 | 409 | 0.49 | 14 |
| R9555 | 164 | 70 | 0.43 | 5 |
| R9556 | 124 | 52 | 0.42 | 5 |
| R9557 | 78 | 30 | 0.38 | 5 |
| R9558 | 296 | 61 | 0.21 | 5 |
| R9559 | 207 | 88 | 0.43 | 9 |
| R9560 | 329 | 61 | 0.19 | 3 |
| R9561 | 1310 | 524 | 0.40 | 12 |
| R9562 | 262 | 95 | 0.36 | 5 |
| R9563 | 620 | 314 | 0.51 | 9 |
| R9564 | 864 | 430 | 0.50 | 10 |
| R9565 | 725 | 382 | 0.53 | 12 |
| R9566 | 993 | 556 | 0.56 | 42 (the glossed lines) |
| R9567 | 662 | 384 | 0.58 | 12 |
| R9569 | 258 | 176 | 0.68 | 22 (the glossed lines) |
| R9570 | 80 | 45 | 0.56 | 5 |
| R9579 | 647 | 315 | 0.49 | 8 |
| R9582 | 74 | 34 | 0.46 | 5 |
| R9583 | 50 | 30 | 0.60 | 11 |
| R9584 | 19 | 12 | 0.63 | 4 |
| R9585 | 109 | 48 | 0.44 | 5 |
| R9587 | 218 | 59 | 0.27 | 3 |

Outside the glossed lines no document has a run of more than 14 known groups; a group is a syllable or a short word,
so that is at most a clause, with an unknown group on either side.

Retry by hand (the escalation step NOTES had open: hand-read against the crib themes): R9566 p. 3 ll. 10-14, the
unglossed continuation of the Decazes/Floridas passage, the best-covered unglossed stretch in the corpus. Decode:
"desidera della Francia [1998] e la [1702] i [1772] [2145] la Spagna [2068] [2095] [1964] sione? ces di [1613] [1734]
sarsi? si one [1462] [795] alla Francia [1481] [1723] te [22] e [1394] [1416] si . [45]". The theme (Spain, France,
the cession) is clear, but 17 of 37 groups have no value and the order "2085 2142" (sione? ces) contradicts the
glossed "2142 2085" (ces-sione), so the inferred value 2085 = sione is itself in doubt. No new value could be fixed:
each candidate (cessione, Spagna/Francia relations, Floride) leaves three or more neighbouring groups open, and the
code's alphabetical runs are too short to bracket them (runs of 2-5 values, NOTES "The code").

R9569 (4 Sept 1823): the gloss of p. 1 ll. 8-16 gives one sentence, now recognisable through the decipherer's syllable
splits: "... [l']elezione al Sovrano Pontificato del Cardinale [2261] ci ca ro do l [2283] ...; ed io ho motivo di
credere di no, e che [potessero ...] la suddetta elezione la Francia gli darebbe l'esclusiva" (France would give him
the exclusion, i.e. veto him). Lines 1-7 and p. 2 (out of focus) have no gloss and decode at the usual half
coverage. One sentence of about ten: not a reading.

R9566 (1 Dec 1816): the glossed ten lines of p. 3 read (Decazes, high in the King's favour, met the Spanish minister
Onís on his way through and spoke of the cession of the Floridas and of the rumoured cession of Cuba to England); the
other five pages (with the fragment in another hand, pp. 1, 5, 6) are at 50% coverage. One sentence of a long
despatch: not a reading.

## 3. Where it stops

All 23 stay decoded, not read. Blocker: no-key-material. The code is a two-part code of about 2,450 groups; 162
values come from four contemporary decipherments and further values can be inferred only where a crib theme is known,
which outside the glossed passages it is not. The 1816-19 code book or Circello's decipherments (ASNa, Esteri) would
move it (needs-physical-access); the images themselves are legible.
