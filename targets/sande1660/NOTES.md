# Marquês de Sande's papers, ANTT Luís de Miranda Pereira liv. 1: cipher A (Dutch Republic, c. 1657) and cipher B (Rome, 1664)

Status: contributed by WAINUT (27 Oct 2026). Cipher A: key recovered from the ciphertext alone; the transcribed
passages are read in part, but most of the cipher lines are not yet transcribed. Cipher B: located, not solved.
The site page and the ledger rows are left to the maintainer.

Catalogue 390. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents.
The transcription was made from the DigitArq scans by a vision-capable language model. A second agent re-read the
key passages on the scans, transcribed a page the first reader had not seen and decrypted it with its own code.

## 1. The volume

- **Source.** ANTT, Luís de Miranda Pereira, liv. 1 (PT/TT/LMP/0001), DigitArq
  [7d037cd7783448dfb5fa761cf9301aa5](https://digitarq.arquivos.pt/documentDetails/7d037cd7783448dfb5fa761cf9301aa5),
  592 scans (m0001-m0592). The scans are not in git; scan numbers below are DigitArq's file numbers.
- A factitious codex of Francisco de Melo e Torres, later marquês de Sande: the 1661 marriage treaty, Charles II's
  letters, Council of State papers, Lübeck/Hamburg letters and French marriage articles (m0450-0520), mostly in clear
  (Portuguese, French, English, Latin).
- All 592 scans were viewed as thumbnail sheets. Cipher stands in three places:

| Scans | What | State |
|---|---|---|
| m0265-m0273 | **Cipher A.** Numerical cipher letters in Portuguese to "Vossa Excelência". | Key recovered; about 45 lines transcribed and read in part |
| m0059-m0063 (probably also m0055-56, m0065, m0069-75, m0098, m0113, m0116-117) | **Cipher B.** Portuguese letters with numerical passages; m0063 is dated "Roma em 21 de Janeiro de 1664". Glosses of the time over some groups. | Located and described; not solved |
| m0170 (scanned upside down) | Numbers with some clear words; the tokens (9xx, 325, 330, 405 ...) match cipher B. | Located only |

m0580 ("a Lisbonne le 29 de Septembre 1660") is French clear text in a phonetic spelling ("Reglaman", "ceppandan"),
not a cipher.

## 2. Cipher A: the pages

The first survey took m0265-m0273 as one nine-page letter. A closer look at the page layout (read once, not checked by
a second reader) shows at least three units:

- **m0265-m0267**: a letter that opens "Com grande desgosto fico ao presente" with no heading and ends half-way down
  m0267 with a dash (raw decode "… hemqueocorre —").
- **m0268**: blank, except one line along the top edge, near the binding: in clear "[…]x° 30: Nov° 165[?]" (the start
  is lost in the gutter; the last digit is probably 7), then in cipher **"Vossa [62] Excelência não firme [61] suas
  cartas"** ("Your Excellency should not sign your letters"). This may explain why none of the cipher letters is
  signed. Which unit the line belongs to is not settled.
- **m0269**: one page. It ends with "… [?] para Duarte da Silva" in cipher and "Ds gde" (Deus guarde) in clear.
  Duarte da Silva may be the Portuguese merchant-banker of that name; not checked. m0270 is a blank verso.
- **m0271-m0273**: a letter ending "Deus [62] guarde a Vossa Excelência [62]", with no signature and no date.
  m0274 is a blank verso.

## 3. Cipher A: the system and the key

A simple substitution with a few homophones. Numbers 1-41 stand for letters; the writer leaves gaps between words.
Numbers of 60 and up are code groups. The full table is in `key.txt`:

| a | b | c | d | e | f | g | h | i | j | l | m | n | o | p | q | r | s | t | u/v | x |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3, 24 | 9 | 15 | 6 | 1, 27 | 12 | 8 | 14 | 5 | 10 | 21, 36 | 7 | 18 | 2 | 11 | 16 | 20, 30 | 13, 41 | 19 | 4 | 22 |

- Glyph note: the "e" sign 27 is written as a 2 followed by a reversed hook; the hook alone is 7 (m).
- 16 alone is "que" (q). The writer spells c and z as s ("fransa", "rela sao", "faser").
- Code groups seen in the transcribed lines: 61 (4 times), 62 (6), 63 (2), 64 (2), 65, 79, 102, 128, 132 (4), 341.
  None has a value.
- **How it was found.** From the ciphertext alone. Word gaps are kept, so frequent short words (16.4.27, 6.27,
  11.2.20) could be taken as que, de, por, and the values built out from there. No gloss, clear copy or key sheet was
  used. The round-1 values "17", "28" and "29" were misreadings (section 4), so the table has no unassigned
  letter signs in the transcribed lines.
- **The test that matters.** The second reader transcribed m0269 lines 3-12, which the first reader had never seen,
  and decrypted them with an independent implementation of the key. They come out as fluent Portuguese with no
  tuning ("… nagem confidente noso o qal teue grande discurso comigo e concluimos …").

## 4. Transcription and corrections

`transcription.txt` holds the transcribed lines: m0265 lines 1-18, m0266 lines 2-5, the m0268 line, m0269 from the end
of line 2 to line 12 plus its last line, and the last 12 lines of m0273. That is about 45 of roughly 290 cipher lines,
1,332 tokens. **It is not a full transcription.**

Corrections to the first reading, all made on the scan (the second reader's, unless marked):

1. m0265.07: the first group is **19.4, not 13.4**: "Monsiur de **Tu**", that is Jacques-Auguste **de Thou**, French
   ambassador at The Hague in 1657-62. 13 has a two-bowl "3"; 19 ends in a reversed hook.
2. m0265.08: "29" is **2.9** (o, b) with the dot left out: "obrigado". So 29 is not a cipher sign.
3. m0265.07: "28" is **20** with a looped 0: "embaixador".
4. m0265.09: "17" is most likely **12**: "afecto". m0265.03: "6.5.3.3" is most likely **6.5.8.3**: "diga".
5. m0265.09: "19.3.27" is **19.3.21**, "tal" (preparation check; the same sign as 21 in 1.21.36 on that line).
6. m0265.10: "13.3.2" before 2.4.5 is **18.3.2**, "não" (preparation check; the same 18 as in 18.3.13 on that line).
   With 5 and 6 the sentence reads "porque tal afecto no mo[d]o com que ele fala nas cousas do nosso reino não o vi".

Doubtful, not changed: "crocadas" (m0265.03) may be "trocadas" (19 for 15); "pesaados" (m0265.13) may be 18.14 for
13.24, giving "empenhados"; the blotted 62 in m0269.05 "e[62]stão".

## 5. The reading

Line by line in `decryption.txt` (output of `python decrypt.py`), as sentences in `reading.md`, in English in
`translation.md`. The opening (m0265):

> Com grande desgosto fico ao presente, porque chegou da Haia, e nela [62] vi [341] cousas são [?trocadas], que […]
> sei o que diga. Com a chegada dos [128], que tem feito relação […], estão todos tão acesos contra Portugal que não é
> crível. [63] [65] A Monsieur de Thou, embaixador de França, vi todos os dias desta semana, e lhe estou muito
> obrigado …

> I am at present in great displeasure, because word came from The Hague … With the arrival of the [128], who have
> made a report […], they are all so inflamed against Portugal that it is not to be believed. [63] [65] Monsieur de
> Thou, ambassador of France, I have seen every day this week, and I am much obliged to him …

m0269 (the page the first reader never saw):

> [Hum perso]nagem confidente nosso, o qual teve grande discurso comigo, e concluímos que [?estão] os [79] arrepesos
> [?do] em que se meterão. Mas por reputação é necessário que mostrem o contrário, e é infalível que se continuará
> com todo o rigor se não houver temperamento. O [132] de França faz grandes deveres para achar expediente …

> A personage, our confidant, had a long talk with me, and we concluded that the [79] [?are] repentant [?of] what
> they have got into. But for reputation's sake they must show the contrary, and it is certain that it will be
> carried on with all rigour if there is no accommodation. The [132] of France makes great efforts to find an
> expedient …

The close (m0273):

> … E torno a dizer que nada pode moderar esta fúria que ouvir alguma pessoa por parte de Sua M[ajestade] a tratar
> de composição. Deus a [62] e guarde a Vossa Excelência [62].

> … And I say again that nothing can moderate this fury except hearing some person on His Majesty's behalf come to
> treat of a settlement. God [62] keep Your Excellency [62].

"pode moderar" joins m0273.e08 "podemo" and e09 "derar" across the line end; the first reading had "podemos de[r]ar".
"Sua M[ajestade]" is "sua mo" in the cipher (also "a suamo" in e01); it could also be read "seu amo" (his master).

**What it says.** A Portuguese agent in the Dutch Republic writes to a minister ("Vossa Excelência"). The Dutch are
inflamed against Portugal. The French ambassador at The Hague, de Thou, is friendly, and France is working for a
mediation: Comminges, the French envoy in Lisbon, has pressed for it, and the said [132] (de Thou) writes to Bordeaux,
the French ambassador in London. A confidant says the Dutch regret what they have got into but must keep up the war
for reputation. The writer asks for advice and says that only an envoy from the King, sent to treat of a settlement,
can calm this fury.

**Date and people (inference, not proven).** De Thou at The Hague (1657-62), Comminges in Lisbon and Bordeaux in
London, with the Dutch "inflamed against Portugal", fit the Dutch-Portuguese war of 1657-61. The m0268 line dated
30 Nov 165[7] agrees. The writer is not identified. The catalogue entry names Diogo Lopes de Ulhoa at The Hague
writing to Rui Teles de Meneses in Paris; that lead, and Francisco de Melo (whose papers these are) as the addressee,
are both untested. The letter just before (m0264, clear, "Anterdã 22 nov", signed "Criado de V. Ex.ª") comes from the
same milieu; no link is shown.

**Measured.** In the transcribed lines 1,306 of 1,332 tokens get a value (23 code-group tokens and 3 blotted signs
open). `reading.md` has a hole rate of 0.128 on `research/reading_audit/v2_score.py` (read_share 0.872).
`docs/_check_reading.py` gives a low clean share (0.385), because the open code groups, the names (Thou, Comminges,
Bordeaux) and words outside the period Portuguese word list (acesos, empenhados, arrepesos …) count as holes in short
sentences.

## 6. Code groups

- **132 = embaixador** is proposed, not proven: "o [132] de França faz grandes deveres" (m0269.10); "Monsiur de
  Cominges [132] [64] de França" (m0265.16); "o dito [132] escreveu este correio muito largo a Monsiur de Bordeus"
  (m0266.04, de Thou writing to Bordeaux). On m0266.05 a blotted group after "Bordeus" (13[blot], perhaps 132) is
  followed by "de fr…", which would fit; it is not transcribed.
- **62** stands after a clause end in m0266.04, but also inside "vosa 62 exelesia" (m0268), mid-phrase in m0265.02
  and in the close "Deus a 62 e guarde". It may be a null or separator rather than a full stop. Not settled.
- **61** and **64** behave like short words or punctuation ("não firme [61] suas cartas").
- 63, 65, 79, 102, 128 and 341 are open.

## 7. Controls

`python decrypt.py --controls` counts the decrypted words found in a fixed list of about 50 common Portuguese words
(set before decoding), on the corrected transcription (300 words), 2,000 trials each:

| Text | Real key | Letter values permuted, mean / max | Groups shuffled, real key, mean / max |
|---|---|---|---|
| transcription.txt (300 words) | **115** | 5.0 / 27 | 18.0 / 29 |

The second reader's run on its own m0269 transcription alone (52 words) gave 17 for the real key, against 1.3 / 7 and
2.7 / 7.

## 8. Cipher B (Rome, 1664)

- Numerical: two-digit multiples of 5 (10, 25, 30 … 95), small numbers (12, 13, 14, 18, 24, 37), three-digit groups
  (120, 200, 204, 325, 330, 400, 405, 570) and 9xx groups (900-912) closing each cipher passage (end marks or nulls).
- Glosses of the time on m0063 over some groups, for example "do Cardeal" over 70.14.40.12.95, "da Casa" over
  70.14.10.12.10.204.907, "ninguem" by 45.30.45.18.25.80.45.13.912, "nosso" over 405.
- The groups do not line up one-to-one with letters (nine groups for "ninguem"), so the system is probably syllabic or
  homophonic with nulls. Not attacked. This part was not re-checked by the second reader.

## 9. Prior work

- No gloss, clear copy or key sheet for cipher A was found in the codex.
- The catalogue entry was scored from the archive description only ("no decipherment noted").
- Repository history (400 commits on main, 27 Oct 2026): nothing on 390, LMP/0001 or Sande's LMP papers. The nearest
  target is `targets/miranda1660/` (catalogue 389): the conde de Miranda's Hague-London letters to Francisco de Melo of
  1659-61 and the two keys in MMCG 3L, not digitised. If cipher A turned out to share a key with 3L, that would bear on
  catalogue 389.
- One web search (27 Oct 2026) on "Luís de Miranda Pereira", Sande and cifra found no edition or decipherment.
- Not checked: E. Prestage, *As relações diplomáticas de Portugal com a França, Inglaterra e Holanda de 1640 a 1668*
  (Coimbra 1928), and the published Sande correspondence. **No earlier solution was found, but the search was not
  exhaustive.**

## Remaining gaps

- Cipher A, the untranscribed lines (about 245 of 290: most of m0265-m0267, m0269 lines 1-2 and 13 onwards, m0271,
  m0272 and m0273 above the last 12 lines) - blocker: not-attempted. The scans are online and legible.
- Cipher A, code groups 61, 62, 63, 64, 65, 79, 102, 128, 132, 341 - blocker: open-codes. No key sheet; the rest of
  the text should repeat some of them.
- Cipher A, writer, addressee and exact date - blocker: not-attempted. Ulhoa / Teles de Meneses and Francisco de Melo
  are untested; the m0268 date line needs a second reading.
- Cipher B (Rome 1664) - blocker: not-attempted. The m0063 glosses are the way in.

## Escalation

- [ ] siblings: the rest of cipher A (m0265-m0273) is the first sibling; catalogue 385 (Teles de Faro to Francisco
  de Melo, 1658-59, MMCG 1E) and 389 / MMCG 3L (Miranda's keys) are not digitised
- [x] clear-pages: the clear letters around m0264 were looked at; none is shown to be a clear copy
- [ ] known-keys: not tested against the repository's Portuguese keys (joao1642) or the 3L keys (not imaged); cipher A
  did not need them
- [ ] print: Prestage (1928) and the Sande correspondence not checked
- [x] key-rebuild: the letter table is complete for the transcribed lines; the code groups are open
- [ ] retry: transcribe the remaining lines, then return to the code groups

## Files

- `transcription.txt`: the transcribed lines, with who read what and the corrections
- `decrypt.py`: decryption and controls (standard library); `python decrypt.py`, `python decrypt.py --controls`
- `decryption.txt`: output of `python decrypt.py`
- `reading.md`: the passages as Portuguese sentences, holes marked
- `translation.md`: English translation, same holes
- `key.txt`: the letter table and the code groups seen
