# Count of Sabugosa to Queen Amélie, four code telegrams of 1903, 1904 and 1910 (ANTT PT/TT/CAM/M14, catalogue 410)

Status: contributed by WAINUT (27 Oct 2026). Three of the four telegrams are read from decodes made at the time and
filed in the same unit (one of them with the decoder's own gaps). Pairing the decodes with the groups gives 52
values of a one-part (alphabetical) Portuguese code. The 1903 telegram has no decode and is not read. The site page
and the ledger rows are left to the maintainer.

Catalogue 410. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents;
the transcriptions were made with a vision-capable language model and checked against the DigitArq images. The two
printed telegrams (m0014, m0016) were re-read independently. The decodes on the clear cards were found later, while
checking the contact sheets; they, the handwritten 1910 telegrams and the pairing have had one reading only.

## 1. The unit

- **Source.** Arquivo Nacional Torre do Tombo, *Documentos de D. Carlos, D. Amélia e D. Manuel II*, maço 14,
  PT/TT/CAM/M14, [DigitArq record](https://digitarq.arquivos.pt/documentDetails/a71061e2ccac4d0db94101fcb8dfa192),
  17 images, downloadable through DigitArq's JSON backend.
- **What is in it.** Four code telegrams (m0010, m0012-13, m0014, m0016; m0017 is a telegram envelope) and clear
  cards and sheets (m0001-m0009). Most of the clear cards are pencil decodes of the telegrams.
- The sender is the Count of Sabugosa (António Maria de Melo), the Queen's chief steward (mordomo-mor) [from
  general knowledge, not checked]. He signs SABUGOSO (1903), SABUGOZA (1904) and Sabugosa (1910).

## 2. The telegrams and their decodes

| telegram | route and date | groups | decode of the time | state |
|---|---|---|---|---|
| m0014 | Lisbon -> Paris, 13 May 1903 (stamp probable), "AMPLIATION", signed SABUGOSO | 43 | none found | not read |
| m0016 | Lisbon (Alcântara) -> Naples, 24 Apr 1904 | 10, among clear words | m0009, dated 24-4-04 | read |
| m0010 | London (Buckingham Palace) -> Lisbon (Necessidades), 21 May 1910 | 16 | m0008, dated 21-5-10 | read |
| m0012-13 | London -> Lisbon (Necessidades), received 24 May 1910 | 37 | m0005 + m0004, with question marks | read in part |

Headers, stamps and word counts are in the transcription files. For the three handwritten and Naples forms, the
word count on the form equals groups + clear words + address words, which checks the number of groups.

**Corrections to the first pass:** m0014 runs Lisbon -> Paris, not Paris -> Lisbon (form's rule: origin before the
serial number), is of May 1903, not 1910, and has 43 groups, not 51. m0016 runs Lisbon -> Naples, not Naples ->
Lisbon; its year (1904) comes from the decode. The first pass split the groups into a "1903-04 code" and a "1910
Sabugosa code"; that fails. Sabugosa used one code in 1903, 1904 and 1910, and King Carlos used a different one
(`targets/carlos1903`) in the same weeks of 1903.

**How each decode was matched.** m0009 begins with the clear words of m0016 ("Agradeço com vivo reconhecimento
telegramma de V. M. que") and gives ten words for its ten groups. m0008 has the date and signature of m0010 and 15
words for its 16 groups. m0005 + m0004 are signed Sabugosa; their question marks fall where the receiver circled
groups in m0012-13, and their first word, Rainha, is the group 5411 that m0008 also reads Rainha.

## 3. The readings

**m0016, 24 Apr 1904** (`m0016_*`):

> Agradeço com vivo reconhecimento telegramma de Vossa Magestade, que veio socegar meu coração. Ser e serei sempre
> o mesmo. Estimo muito boas noticias e demonstrações. Escrevo. Beijo mão Vossa Magestade. Sabugoza.

"I thank Your Majesty with lively gratitude for the telegram, which has set my heart at rest. I am and always will
be the same. I am very glad of the good news and the demonstrations. I am writing. I kiss Your Majesty's hand."
Only "veio ... mesmo" is coded; the code has the infinitive "ser" where the sense wants "sou".

**m0010, 21 May 1910** (`m0010_*`):

> Hoje ElRei tenciona falar Rainha para Soveral tratar com ella assumpto. Espero amanhã dar informação. Sabugosa.

"Today the King intends to speak to the Queen so that Soveral may take up the matter with her. I hope to give news
tomorrow." Edward VII had been buried the day before; the King is George V. Soveral is the Marquis of Soveral,
Portuguese minister in London [our identification].

**m0012-13, 24 May 1910** (`m0012_*`), with the decoder's gaps kept:

> Rainha Alexandra recebeu-me hontem á noite, dizendo-me palavras muito agradaveis [?]. S. M. ElRei terminou dizendo
> [?va] [?] [?conde] [?socegado]. Tratar é de o casar. Não tive occasião ver Princeza. Soveral diz ir tratar
> [?subsequente] negociação. Sabugosa.

"Queen Alexandra received me last night and said very kind words to me [?]. His Majesty the King ended by saying
[...]. The point is to get him married. I had no opportunity to see the Princess. Soveral says [he] will go to handle
the [?further] negotiation." "Him" is presumably King Manuel II; the Princess is not named.

These are the 1910 attempts to arrange a British marriage for Manuel II, in the days after Edward VII's funeral.
`related_clear.md` transcribes two more cards of the same week: a decode of 22 May (m0001, probably continued on
m0002: Queen Alexandra invites "the Princess" and her family to dinner; "I hope this is significant and that the
Princess will please His Majesty the King"), whose coded telegram is not in M14, and the Queen's clear reply of
21 May (m0007). Whether these cards are quoted in the literature on Manuel II was not checked.

## 4. The code (`code_values.tsv`, `python code.py`, output in `code_output.txt`)

52 groups get a value from the three decodes, with no conflict between them. Graded as in the README: C from a
decode one group to one word, M where the decoder marked a doubt or the value stands out of alphabetical place, I
for our split of a decoded phrase over groups.

- **One-part, alphabetical.** Five-digit groups (11501-23400) carry words from a to h (agradaveis 12190 ... hontem
  23024); four-digit groups (0139-9019) carry words from i to v (informação 0139, ir 0320 ... veio 8975). Within each
  series the numbers follow the alphabet. Grade C values: 3 of 406 pairs out of order in the 4-digit series, 0 of
  136 in the 5-digit series; 2000 random shuffles of the same words over the same numbers give at least 117 and 32.
  The 3 pairs are tive/terminou (7753/7785) and ver/veio (8747-8748/8975).
- **Names are spelled in pieces.** Soveral is three groups, 7034 / 8747 / 12296 = So / ver / al: in m0004 the decoder
  first wrote a word in So- and struck it, then wrote "ver al". The same three groups stand for "Soveral" in m0010.
- **One code 1903-1910.** The 1904 and 1910 values fall into one alphabetical order, and the 1903 telegram m0014
  shares 19482 (diz), 18063 (de, twice) and 19656 (e, three times).
- **What the order says about the decodes.** socegado 7114 sits next to socegar 7115 (1904), which supports the
  doubtful "socegado". The decoder's "va" (0539) stands among i-m words, so it is probably wrong. 13657, which m0008
  renders "assumpto" (the matter), stands just after casar 13616; by its place it is a word in cas- (casamento,
  marriage?) and "assumpto" may be the decoder's paraphrase. Not adopted.

**m0014 (13 May 1903).** 6 of 43 groups take a value (diz, de x2, e x3); `code.py` lists the alphabetical
neighbours of the other 37. Not enough to read.

## 5. Prior work

- The decodes are in the archive, so the readings are not new. No printed decipherment of the telegrams was found
  (one web search). Not checked: biographies of Manuel II and studies of the 1910 marriage project, which may quote
  these cards.

## Corrections to catalogue entry 410

- Date "1910": the unit holds telegrams of 13 May 1903, 24 Apr 1904, and 21 and 24 May 1910.
- Place "unknown": London (1910), Lisbon -> Paris (1903), Lisbon -> Naples (1904).
- Status: decodes of the time for three of the four telegrams are in the unit (m0008, m0005 + m0004, m0009).

## Remaining gaps

- m0014, 43 groups (Lisbon -> Paris, 13 May 1903) - blocker: no-key-material. No decode; 6 groups have a value,
  the rest only alphabetical bounds; the codebook was not found.
- m0012-13: 1738 and 3667 (left blank by the decoder) and the doubtful 0539 va, 17004 conde, 7114 socegado -
  blocker: open-codes. Single occurrences; the alphabetical bounds (1738 between ir and me, 3667 just after para)
  do not fix a word.
- 13657, the decoder's "assumpto" - blocker: open-codes. Its place suggests a word in cas-; one occurrence.

## Escalation

- [x] siblings: all four telegrams and the clear cards of M14 examined; three decodes found and paired
- [x] clear-pages: m0016's clear words frame its code; the related cards are in related_clear.md
- [x] known-keys: King Carlos's 1903 code (targets/carlos1903) and Manuel II's 1910 code (targets/manuel1910) are different codes
- [x] print: one web search; no edition found
- [x] key-rebuild: 52 values rebuilt and the alphabetical order tested against shuffles; applied to m0014
- [ ] retry: the printed codebook (a Portuguese one-part code of about 24,000 entries?) or more decoded telegrams of Sabugosa would read m0014

## Files

- `m0010_*`, `m0012_*`, `m0016_*`: transcription, decode of the time (`_contemporary.txt`), group-by-group
  decryption, reading (Portuguese) and translation (`_en.md`)
- `m0014_transcription.txt`, `m0014_decryption.txt` (6 values)
- `code_values.tsv`: the 52 values with grade and source; `code.py`, `code_output.txt`
- `related_clear.md`: the decode of 22 May 1910 without its telegram, and the Queen's reply of 21 May
