# João IV → marquês de Nisa, 1642-44 (Unsolved Catalogue no. 380)

Outcome: key recovered based on adjacent plaintext, read in part (27 Oct 2026). Both cipher alphabets of the
letter-book rebuilt from clear text in the same volume; 398 of 438 transcribed cipher words read (90.9%); letter 153,
the only piece without a contemporary decipherment, read but for five words.

## Document

ANTT, Manuscritos da Livraria n.º 1017 (PT/TT/MSLIV/1017), "Notícias do senhor rei D. João o IV. Cartas aos
governadores do reino. Tomo II": a letter-book of 284 letters of João IV to his ambassador in Paris, Vasco Luís da
Gama, marquês de Nisa (conde da Vidigueira), 1642-45. 289 scans on DigitArq
(https://digitarq.arquivos.pt/documentDetails/1bfdb5d27fe049d7af1599290b3ebb03), 1060 px wide, the only size
served. `scans/index.json` maps scan names to file ids (image =
`https://digitarq.arquivos.pt/rdigital/dissemination?fileId=<id>`); the images are git-ignored. Folio = scan − 4.
Each letter carries an ink number by its heading = the DigitArq item number.

| letter | date | scans | cipher | clear text |
|---|---|---|---|---|
| 00009 | 28 Dec 1642 | m0020 | A, 3 runs, 158 words | clear copy of the whole letter on m0021 |
| 00013 | 31 Dec 1642 | m0024-m0025 | A, 4 runs, 207 legible words | 'Carta inclusa', m0025-m0026 |
| 00044 | 9 Oct 1643 | m0064-m0066 | A, short runs, 9 words transcribed | none |
| 00049 | 9 Oct 1643 | m0068 (instructions for Luís Pereira de Castro follow, m0068-m0073) | A, 29 words | none |
| 00056 | 20 Nov 1643 | m0085 | A, 3 words + ⊕ | none |
| 00153 | 21 Sept 1644 (page heading: 21 Nov) | m0157 | B, 31 words, 148 letters | none for this letter |

DigitArq's flags are incomplete. Also in cipher: letter 8 (25 Oct 1642, m0019, with a clear 'Papel junto'), m0089
(20 Dec 1643), m0114 (22 Jan 1644, Carta 82, the Angola armada), and in alphabet B m0179 (Carta 187, 14 Jan 1645)
and m0190 (Carta 212, 7 Feb 1645). m0276, a leaf before the index, lists the deciphered passages of Cartas 54, 59,
60, 82, 187 and 212 in clear. Pages headed "Carta Decifrada" (m0074, m0224, m0246, m0254-55, m0258) are clear texts
of letters received in cipher.

## System A (1642-44)

Letter-for-letter substitution with two homophones (s = r/v, u/v = x/z), written as pseudo-words in Latin letters,
word divisions kept, plus ⊕ for Castile / the King of Castile and the code word `ft` for ElRei Christianíssimo / the
King of France. Plain→cipher: a o, b g, c e, d f, e c, f E (looped capital), g d, h b, i a, l p, m z, n i, o u,
p g, q s, r t, s r/v, t n, u x, v x/z, z l (`key.py`). Proper names are spelled out (Duarte, Milão, Rigão, São
Lourenço, Longavilha). Scribal traps: c/e, t/z, r/x and o/u look alike; the copyist sometimes enciphers a clear
abbreviation (cs = e q[ue], zx = m.tas) or drops into clear mid-sentence (`key_notes.md`). The 1643 letters use the
key unchanged (`key_notes_1643.md`).

Key rebuilt from adjacent plaintext: letter 8's cipher against its 'Papel junto' (ecinarcinu = sentimento, fxotnc =
Duarte, atrou = irmão, etcfanur = créditos), then letter 13 against its 'Carta inclusa' (paecico = licença, uxntur =
outros, iozeur = navios, Eurcinox = fomentava, fareutfeor = discórdias). Every value is confirmed by the clear copies
of letters 9 and 13. Statistical check (`docs/_validate.py`, 1,164 letters of letters 9 and 13, pt-modern): pass.

## System B (1644-45)

A second alphabet whose signs look like Greek letters (ε, η, ρ, χ, β, ν). Labelled by the Latin letter each sign
resembles (`l153_cipher.txt`), cipher→plain: E o, b m, e n, f i, i p, m r, n s, p a, u d, x e, z f, q c, a l, c h,
v u, o t, t z, r u (`KEY_B` in `key.py`); homophones for i (f/s/t) and p, values for d and g uncertain. The 1642 key
and its shifts do not read it; three anneals on pt-modern gave nothing (`solve153*.py`): 148 letters is too short.

Key rebuilt from adjacent plaintext: the volume sweep (`sysB_siblings.txt`) found the same alphabet on m0179 and
m0190, whose clear texts are on m0276 ("Do Pr.e sobre todos meu m.to amado, e prez.do f.o"; "sobre o casam.to do Pr.e
... e das Inf.as porq este neg.o não q.o q saiba mais q vós, e Luís Pr.a"). Aligned: imfeqtix = principe, bxv = meu,
nEqmx = sobre, oEuEn = todos, zfacE = filho, ixmxfmq = Pereira.

## Readings

- Letter 9 (`transcription_l09.txt`, 149/158 words): the release of the Infante D. Duarte, "meu muito amado e
  prezado irmão"; letters of the French king to Prince Thomas and the Duke of Longueville to intercept the troops
  taking the Infante to Milan; Spanish prisoners of rank to be obtained from France to exchange for him; any attempt
  by force or escape "mui arriscado para a vida do Infante", whose guards had orders to kill him; secrecy "o ponto
  mais essencial deste negócio". One name blotted (Duque de O[..]a).
- Letter 13 (`transcription_l13.txt`, 199/207 legible words): the French king's licence to Rigão and others to send
  ships to São Lourenço (Madagascar), trade and build forts; the reported death of Richelieu, held to be the man who
  most fomented the wars with Castile and on whose account offers of a cessation of arms had been refused; the fear
  that Castile will now succeed; Nisa to penetrate the secrets of Castile and the French king's mind.
- Letters 44, 49, 56 (`transcription_l44/49/56.txt`, 24/42 words): Münster, the Infante's news from Genoa, the
  instructions of France and Castile for the general peace, the instructions sent to the ministers at Münster.
- Letter 153 (`l153_reading.txt`, 26/31 words): "visto se não entende tão no[s] dos casamentos do Príncipe meu sobre
  todos muito amado e prezado filho e das Infantas, sobre que vos mandei escrever: porque estes não comunicareis nem
  confiareis ao Marquês nem a outra alguma[?] pessoa, mais que [..] mandado [..]." Nisa, leaving the embassy to the
  marquês de Cascais, is to keep the marriage negotiations for Prince Teodósio and the Infantas from him.

## Remaining gaps
- cipher words of letters 44, 49 and 56, and m0025 ll. 3-5 and 12-16 of letter 13 - blocker: illegible; rubbed or faint at 1060 px, the only resolution DigitArq serves; better images from ANTT would close them (letter 13's text is known from its clear copy)
- letter 153, 'pn Evcv Eno nE' before 'mandado' and 'purzmofm' after it - blocker: too-short; five words in alphabet B with no parallel text, and the values they need (d, g, r and the homophones) rest on one or two occurrences

## Escalation
- [x] siblings: the whole volume swept (289 scans); alphabet-B siblings m0179 and m0190 found and used; letter 8's cipher and clear paper used for alphabet A
- [x] clear-pages: 'Papel junto' (letter 8), clear copy (letter 9), 'Carta inclusa' (letter 13) and the list of deciphered passages (m0276) are the decipherments; 'Carta Decifrada' pages checked, they are received letters
- [x] known-keys: alphabet A and every shift of it tried on letter 153; does not fit
- [x] print: web search for Laranjo Coelho's 1940-42 edition finds only library records (Biblioteca Municipal de Redondo, vol. 1; Arquivo Histórico Militar); not digitised, so whether it prints the cipher passages needs a library copy
- [x] key-rebuild: alphabet B rebuilt from m0276 against m0179/m0190, then extended from letter 153's own context (marquês, pessoa, alguma)
- [x] retry: every open word of letter 153 decoded again with the extended KEY_B; the five left give no word; the 1643 words re-examined at 2x crops, still not legible

## Prior work

- Contemporary: the letter-book carries its own decipherments (clear copies of letters 8, 9 and 13; m0276 for
  Cartas 54, 59, 60, 82, 187, 212). Nothing for letters 44, 49, 56 or 153.
- Printed: *Cartas de El-Rei D. João IV ao Conde da Vidigueira (Marquês de Niza)*, ed. P. M. Laranjo Coelho,
  Academia Portuguesa da História, 1940-42, from Torre do Tombo manuscripts. Not seen; it may print the clear copies.
- Brice Dudout (email, 27 Oct 2026): had rebuilt the key from the volume's own 'papel junto', noted that three of
  the six letters have a clear copy beside them, and that 00153 is the only apparently unpublished piece, in a
  different system. His key was not seen; alphabet A was rebuilt here independently from the same clear copies the
  same day. Alphabet B and the reading of 00153 are new here.

## Files

`key.py` (both alphabets), `key_notes.md`, `key_notes_1643.md`, `transcription_l09/l13/l44/l49/l56.txt`,
`cipher_l09.txt`, `cipher_l13.txt` (word lists for measurement), `l153_cipher.txt`, `l153_reading.txt`,
`sysB_siblings.txt` (volume sweep), `solve153.py`, `solve153b.py`, `solve153c.py` (failed anneals),
`make_validation.py` → `validation.tsv`, `profile.json`.
