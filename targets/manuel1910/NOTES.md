# King Manuel II to Queen Amélie, three code telegrams from Bussaco, August 1910 (ANTT PT/TT/CAM/M13, catalogue 408)

Status: contributed by WAINUT (27 Oct 2026). The three telegrams are transcribed and dated; they are not read. No
decode was found in the unit and the code is not Sabugosa's. The site page and the ledger rows are left to the
maintainer.

Catalogue 408. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents;
the transcriptions were made with a vision-capable language model from the DigitArq images. One telegram (m0021) was
also read by a second agent for its first sheet only; the rest has had one reading.

## 1. The unit

- **Source.** Arquivo Nacional Torre do Tombo, *Documentos de D. Carlos, D. Amélia e D. Manuel II*, maço 13,
  PT/TT/CAM/M13, [DigitArq record](https://digitarq.arquivos.pt/documentDetails/fc51cb8d1cf34151a475a3a78f13c2a4),
  22 images, downloadable through DigitArq's JSON backend.
- **What is coded.** Only the three telegrams. The letters and cards (m0001-m0014) are in clear. m0001-m0002 hold a
  pencil text in telegram style signed Manuel ("Confidencialíssimo. Realisou-se hoje jantar no Paço offerecido Rainha
  Viuva ...", with question marks and "Paris terça-feira onze horas manhã"), which may be the decode of a London
  telegram of May 1910; its coded form is not in M13, and it does not match these three. That telegram, like the one
  behind Sabugosa's decode of 22 May 1910 (`targets/sabugosa1910`, related_clear.md), may be in another CAM unit; if
  either turns up, its decode is a crib for the code.

## 2. The telegrams

| images | route and date | items | clear words |
|---|---|---|---|
| m0019 | Bussaco -> Pena (Sintra), 2 Aug 1910, no. 62 | 3 groups | "Resposta A 22/2" [reading uncertain] |
| m0021 + m0022 | Bussaco -> Pena, 2 Aug 1910, no. 55, "urgente" | 54 (49 groups, five "06") | "Querida mãe Tudo bem Tempo lindo veio Sabugosa hoje" ... "Beijo mão Manoel" |
| m0015 + m0017 | Bussaco -> Pena (Cintra), 8 Aug 1910 | 36 (31 groups, "05", four "06") | "Querida Mãe. Recebi sua carta Tudo bem tempo lindo" ... "Beijo mão Manuel" |

The clear words, in English: "Dear Mother, all well, lovely weather, Sabugosa came today ... I kiss your hand,
Manuel" and "Dear Mother, I received your letter, all well, lovely weather ... I kiss your hand, Manuel". The stamps
are those of the Real Paço da Pena telegraph office (2 AGO 10, 8 AGO 10). On both long telegrams the word count on
the form (72 and 54) equals code items + clear words + address words, which checks the number of items.

Transcriptions: `m0015_transcription.txt`, `m0019_transcription.txt`, `m0021_transcription.txt`. Doubtful digits are
marked with a trailing ?. At Pena the receiver struck each group of m0021-22 through its third digit and dashed the
groups of m0015; what the marks mean is not known.

**Corrections to the first pass.** The first pass listed 15 groups of m0021, starting at 37708. The sheet has two
more groups before it (4965?, read as four digits, and 89864?), the group read 37644 is 39644 (as in m0015 and
m0022), and the telegram goes on for 37 items on m0022 (marked sheet 2). The receiver corrected 47183 to 97183 by
writing 9 above the 4; 97183 is also in m0015.

## 3. What the groups show (`python groups.py`, output in `groups_output.txt`)

- m0021-22 and m0015 share 37708, 39644, 93608 and 97183, and open with a parallel run after the same clear words
  "Tudo bem tempo lindo": `37708 ... 97183 39644 06/05`. Random telegrams of 36 and 54 groups over 00000-99999 share
  two groups in about 1 of 10,000 trials, so this is one code and probably one stock phrase.
- m0019 consists of the three groups of m0022 that are underlined in brown (57710 29134 70790). It is probably a
  service repetition of doubtful groups [our inference].
- Short items 05 and 06 stand between groups, as "03" does in King Carlos's 1903 telegrams.
- Sabugosa's alphabetical code (`targets/sabugosa1910`, 52 values) does not fit: no group matches, as written or with
  the struck third digit dropped, and 7 of 79 groups would then fall beyond its last known value (veio 9019).

## 4. Prior work

- No decode in M13 and no printed decipherment found (one web search by the first pass). The days fit the King's
  stay at Bussaco in August 1910 [not checked against the literature].

## Corrections to catalogue entry 408

- Date "1908-1910": the three code telegrams are of 2 and 8 Aug 1910.
- Place "unknown": Bussaco -> Pena (Sintra).
- "3 telegrams": confirmed (m0015+m0017, m0019, m0021+m0022).

## Remaining gaps

- All 93 items of the three telegrams - blocker: no-key-material. No decode in M13 and no codebook found. The shared
  opening run would serve as a crib only if one decoded telegram in this code turns up.

## Escalation

- [x] siblings: the three telegrams compared; shared groups and the parallel opening listed
- [x] clear-pages: the clear openings and closings transcribed; M13's letters hold no decode of these telegrams
- [x] known-keys: Sabugosa's 1903-1910 code tested and ruled out; King Carlos's 1903 code has no values to test
- [x] print: one web search; nothing found
- [x] key-rebuild: not possible without a single decoded telegram
- [n/a] retry: no group has a value, so there is nothing to retry with. Other CAM units (Manuel II's papers) may hold
  decodes of his telegrams to his mother

## Files

- `m0015_transcription.txt`, `m0019_transcription.txt`, `m0021_transcription.txt`
- `groups.py`, `groups_output.txt`: counts, repeats, shared groups, chance control (standard library)
