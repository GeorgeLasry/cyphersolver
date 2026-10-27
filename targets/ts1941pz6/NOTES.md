# German Army Truppenschlüssel, net pz6, 4 July 1941 (catalogue 643): broken by others in September 2026

Status: no write-up. An earlier solution exists. CryptoCellar's 1941 Message List (status 20 Oct 2026) marks all
eight messages of 4 July 1941 as broken, by Norbert Paefgen on 21 Sept 2026 and by Ben Davies (AI) on 25 Sept 2026.
The plaintexts and keys are not published there, so this folder holds no reading. It records the pointer, the
ciphertext checked against the facsimiles, and our own attack, which did not break the messages. Contributed by
WAINUT (https://github.com/WAINUTAI), 27 Oct 2026. The work was done with AI language-model agents.

## The messages

Source: Olaf Ostwald and Frode Weierud, CryptoCellar, "German Army Truppenschlüssel Messages: Messages That We Have
Failed to Break" (<https://cryptocellar.org/bgac/g-army-ts-messages.html>, last updated 27 Jul 2026). The forms
come from the German Army message collection of Operation Barbarossa (Heeresgruppe Nord, 1941).

| Nr. | first group | received | von/an | cells | note |
|---|---|---|---|---|---|
| 88 | TKYKJ | 0300 | pz6 | 38 (40 declared) | N.F. to Ib; facsimile |
| 90 | KVLIG | 0850 | pz6 | 98 | N.F. to Ib |
| 91 | SGOXX | 1010 | pz6 | 88 | N.F. to Ib |
| 92 | UBYVQ | 1010 | pz6 | 126 | N.F. to Ib |
| 94 | HFEYY | 2110 | pz6 | 148 | "übermittelt jid2"; facsimile |
| 95 | LICUD | 2017 | blank | 74 | "übermittelt"; facsimile |
| 96 | DSZPZ | 2024 | blank | 62 | "qzr zvo1, msd1 de msd2" |
| 97 | DEZPS | 2028 | pz6 | 60 | N.F. to Ib |

694 cells in all, of which 683 are legible letters (the catalogue's 547 for the six pz6 messages, plus 74 and 62).
The ciphertext is in `messages.txt`. The facsimiles are on CryptoCellar:
[Nr. 88](https://cryptocellar.org/bgac/spruch/04071941-088-in.pdf),
[Nr. 94](https://cryptocellar.org/bgac/spruch/04071941-094-in.pdf),
[Nr. 95](https://cryptocellar.org/bgac/spruch/04071941-095-in.pdf).

**Check against the facsimiles.** We read the three forms ourselves. The groups of Nr. 88, 94 and 95 match the
transcription in order.

- Nr. 88 has 38 cells against the declared 40. Three of the 38 hold only a dot, not a letter. So the count of 38 is right.
- In Nr. 94, group 23 is blank on the form. That gives the five dashes.
- Nr. 90, 91, 92, 96 and 97 have no facsimile, so for them only the transcription was used.
- The Nr. 95 link on the TS page is broken. It points to `spruch/spruch/04071941-095-in.pdf`; the file is at
  `spruch/04071941-095-in.pdf`.

## The system

Truppenschlüssel (TS) is a single-stage two-square cipher (a simplified Doppelkasten). The rule we used is the one in
Ostwald and Weierud, "Modern Cryptanalysis of the Truppenschlüssel", *Cryptologia* (author copy
<https://cryptocellar.org/pubs/mcts.pdf>):

- The plaintext is split into consecutive pairs, with no seriation.
- p1 is looked up in the left square and p2 in the right square.
- If the rows differ: c1 = R[row p1][col p2] and c2 = L[row p2][col p1].
- If the row is the same, each letter takes its right neighbour.

**Rule control** (`ts_check.py`, output in `ts_check_output.txt`):

- The paper's Fig. 2 example key gives PE→LW, RT→AF, AF→IY and LW→HX. That is 4 of 4, as in the paper.
- We also tried the two 17 Sep 1941 plaintext-ciphertext pairs with the squares of Fig. 6. They agree on 24 of 28
  letters and on 117 of 126 letters.
- Each differing pair is a one-letter garble in the ciphertext. One of them is the "sq" garble (BF/FF) that the
  paper itself notes.

**The repeats fit the system.** All 9 repeats of 6 or more letters start at the same parity, as a fixed
substitution of consecutive pairs requires. Examples:

- HGZVUULV in Nr. 90 and 92.
- VZHGZVUU in Nr. 91 and 92.
- YRTUHBYF twice in Nr. 94.
- YRZOZHVL in Nr. 96 and 97.

Nr. 90 and 91 end in nearly the same 13 letters: RODVL MQULH VKZ against RODVL MQVLH FKZ. Nr. 96 and 97 are almost
the same text.

## Earlier solution

CryptoCellar, "1941 Message List" (<https://cryptocellar.org/bgac/1941-msg-list.html>, "Status on: 20 October
2026"):

> 04.07.1941 88 TKYKJ, 90 KVLIG, 91 SGOXX, 92 UBYVQ, 94 HFEYY, 95 LICUD, 96 DSZPZ, 97 DEZPS: Broken (Nr. 88 to
> Nr. 97 broken by Norbert Paefgen on 21.09.2026 and Ben Davies (AI) on 25.09.2026)

The list marks AI-assisted breaks with "(AI)". The "unbroken" TS page is older (27 Jul 2026) and still lists the
messages; the catalogue entry was taken from that page. Neither page publishes the plaintexts or the keys. So we
cannot compare a reading, and we record the result as a pointer to the earlier solution. We found the status lines
during our work. Both pages were fetched again on 27 Oct 2026, and the copies were identical.

## Our own attempt (not solved)

This was a test of our tools on a set that we now know is solvable. It was not a claim.

| run | data | result | best score per 4-gram |
|---|---|---|---|
| control: net ib9, 30 Jun 1941, Nr. 62-70 (about 400 letters, broken by George Lasry in 2022) | 16 restarts × 30M | broken in 1 of 16 restarts (a second solver: 2 of 16); German such as "duenaburg x duenaburg", "brand geloesqt x munitionsausgabe kann weitergehen" | -4.71 (second solver -4.72) |
| control: 14 Jul 1941 (194 letters, the paper's shortest break) | several runs | not broken | - |
| pz6, all 8 messages | 24 × 30M (second solver: 12 × 30M) | no German | -6.09 (second solver -6.15) |
| pz6: the 6 messages marked pz6; pairs swapped; a language model with X word separators | 8-24 × 15-30M each | no German | -6.01 to -6.16 |
| crib HARTIIENSTEIN on the 13-letter end repeat of Nr. 90/91 | crib bonus | the crib fits a key (23 of 26 letters), but the rest stays gibberish | - |
| net nfw, 3 Jul 1941, Nr. 84-86 (250 letters) | 8 × 15M | no German (a short text scores higher by overfitting) | -5.40 |

How the scores compare (control with its known key):

| key | score per 4-gram |
|---|---|
| the right key | -4.72 |
| the right key with 2, 4 or 8 random swaps (mean) | -5.8, -6.5, -7.3 |
| 2,000 random keys | best -7.5 |

A score of -6 is no better than a key with three or four wrong letters. It is not a partial break.

What we ran:

- The solver is simulated annealing over both squares, with letter, row and column swaps.
- The language model is a German 4-gram table in TS spelling (CH→Q, J→II, SZ, umlauts as AE/OE/UE). It was built
  from literary texts.
- A second, independently written solver was used as a check, with the same language model.
- The solvers need numpy and numba and a 4-gram table of several MB, so they are not included. The rule and the
  checks are in `ts_check.py`.

**Why it probably failed.** Our search is weaker than Ostwald and Weierud's hill climber. It broke the 400-letter
control in only 1 or 2 of 16 restarts. Our language model is literary German, not military text, and the pz6
messages look formulaic: numbers, abbreviations and names. Paefgen and Davies broke them. What is needed is a
stronger search or a military language model, not a new idea.

## Catalogue 643 as a whole

Row 643 covers all 30 TS messages of 1941 that were then listed as unbroken, not only pz6. On the 1941 list of
20 Oct 2026 these 30 stand as follows:

- **24 are marked broken**, all in September 2026, by Norbert Paefgen, Ben Davies (AI), Jack Willis (AI) and
  Jairus Khan (AI). One of the 24, DOLHA Nr. 252, is marked "Partial break with garbles". So 23 are full breaks.
  - pz6 Nr. 88-97 (this folder) were broken by Paefgen (21.09) and Davies (25.09).
  - nfw Nr. 84 and 86 were broken by Paefgen (17.09) and by Davies and Willis (25.09). Nr. 85 was broken by Khan
    (26.09).
  - f8y Nr. 109, 110 and 121, and 4fc Nr. 129 and 130, were broken by Paefgen (17.09) and Davies (25.09).
  - 8be Nr. 263 was broken by Khan and Nr. 264 by Davies.
  - XWFEC Nr. 193 and DOLHA Nr. 252 (partial) were broken by Paefgen, Davies and Willis. VHRNE Nr. 284 was broken
    by Davies, LSSLG Nr. 268 and YSGSS Nr. 56 by Willis, and CFQIB Nr. 281 by Willis and Khan.
- **6 are still unbroken:**
  - EHNPZ Nr. 123 (8 Jul, net 4fc, 87 letters)
  - AFUVO Nr. 26 (13 Jul, 14 letters)
  - ZUBZE Nr. 8 (10 Aug, 62 letters)
  - MZXNX Nr. 21 (17 Aug, 88 letters)
  - AAXYN Nr. 31 (5 Sep, 72 letters)
  - AOXST Nr. 91 (23 Sep, 152 letters)

  Five of them are single short messages with no other TS message of the same net and day. EHNPZ Nr. 123 is
  different: Nr. 129 and 130 of 8 July are on the same net (4fc) and are marked broken. Why Nr. 123 is still open
  (another key, or garbles) was not checked.
- **Not in row 643:** a seventh unbroken TS message, BCUCC Nr. 20 NF (5 Sep 1941, 64 letters). It comes from the
  2026 Bundesarchiv finds.

## Files

- `messages.txt`: the ciphertext of the eight messages, with their headers.
- `ts_check.py`: the TS rule, the rule control, the lengths and the repeats. It uses the standard library only.
  `ts_check_output.txt` is its output.
