# Cardinal Alessandrino to the nuncio in Spain, 1568–69 — read in part

Status: in progress (23 Oct 2026, verification 4: seven letters demoted to decoded, not read; four read: R94, R95, R100 from their contemporary decipherments, R101 on the figures).

**22 Oct 2026, reading audit** (George Lasry's test): R93, R96, R97, R98, R99, R102 and R115 build Italian sentences with scattered slips; **R94, R95, R100 and R101 are decoded, not read**: the beam search's digit choices corrupt words in most of their sentences (R94 "liberagemptume", R95 "desersaleaniosina", R100 ends in ??????, R101 "unmannifestsobismain"). Claim read -> read in part; 7,036 of 10,555 items (66.7%) in letters that read.

**22 Oct 2026, re-read (REREAD_BRIEF, batch aless; texts/R94-R101_reread_log.md)**: the DECODE "cleartext" images
of these records hold the **contemporary decipherments** of three of the four: R94 on f. 45r (covering letter Rome 7
Nov 1567, f. 44r, "Con questa un poco di cifra" — so R94 is of 1567), R95 on f. 58r, R100 under the cipher on f.
280r. Transcribed (texts/R94_decifrato_f45r.txt, R95_decifrato_f58r.txt, R100_decifrato_f280r.txt) and aligned with
the figures (`reread_aless_align.py`); the disagreements showed what Lasry's key lacked: **9 also = "con"**, **dotted 0
= z**, **0^.0 = et**, doubled letters enciphered once, X0Y0 codes written X0Y, 3 0 9 = qua, and code values 1040
lettere (not "Regina di Francia"), 3020 quando, 3060 -mente, 4020 come, 4040 Milano, 4080 et, 5070/6050
Imbasciatore, 6060 Inquisitione, 8090 havere (not "sauere"), 2 0 9 = "chi" (chinea, Chiesa). R101 (no decipherment)
re-decoded with the extended key (`reread_aless_decode.py`) and read word by word: the chinea accepted with the
fisc's protest, devolution under the investitures of Julius II and III, the schism in Naples, notaries and executors
imprisoned. Readings + English: texts/R94|R95|R100|R101_reading.md, _en.md; clean-sentence share 1.00, 0.94, 1.00,
0.84 (before 0.75, 0.89, 0.78, 0.81 on the garbled decodes). State decoded, not read -> read; class back to read.

Catalogue items 253 (class B) and 254. ASV (AAV), Segreteria di Stato, Spagna 6/I, items 1–10 ("Lettere orig. e
cifre del cardinale Alessandrino dal 16 gennaio 1568 …"), DECODE R93–R102; and Spagna 6/II item 13 (1569), DECODE R115.
Sender: Michele Bonelli, Cardinal Alessandrino, nephew and secretary of Pius V. Recipient: the nuncio at Madrid,
Giovan Battista Castagna. The letters are undated on DECODE; folio order puts 6/I in 1568.

**Result (21 Sept 2026): read.** All eleven ciphertexts read end to end with George Lasry's reconstructed key.

## Key

Lasry's reconstruction (DOC_R9x_D32xx.txt, 24 Oct 2020), attached to every record; DECODE lists the records as
"partially decrypted" because the key is there, but no plaintext was posted.

- Polyphonic: each digit stands for two letters — 1 u|t, 2 i|m, 3 f|g, 4 a|l, 5 o|s, 6 e|n, 7 d|r, 8 b|c, 9 p|z.
  0 is a null. No h, q.
- Nomenclator: four digits X0Y0 (1010 Nostro Signore, 1090 V. S., 2090 che, 3010 Re, 4030 S. M.tà, 5020 per,
  6090 quel, 7090 quello, 8010 Re di Francia …) and dotted pairs (0^.0 comma, 30^.9 qua). Full list in decrypt.py.

Because each digit has two readings and the zeros make X0Y0 codes ambiguous with letter+null pairs, the text is
chosen by a beam search scored by the shared Italian model (`lang/`, it-cinquecento, no spaces):
`python decrypt.py > decrypt_raw.txt`. Output is unspaced; `[WORD]` = nomenclator, `[NN.]` = dotted group not in
Lasry's list. Each page ends in a run of padding (strings like `fcpfbrpf`), which is the cipher clerk's filler.

## The letters (gist from decrypt_raw.txt)

- R93 (6/I/1, f. 6r): friends of the crown of France have asked here that the Pope promote a marriage of one of the
  French King's daughters to His Catholic Majesty; the Pope would not move without knowing the King's mind; the
  nuncio is to sound it in the way he thinks best, assuring him no word will be said before his intention is known.
- R94 (6/I/2, f. 42r): jurisdiction. The Pope does not mean to revoke the King's privileges but to remove abuses grown
  through his ministers; the ministers try to strip the Holy See of its authority; the King should hear this freely.
- R95 (6/I/3, f. 55r): reply on the ministers' claims, the crusade alms ("elemosina … indulgentia"), the Pope's
  offer of a pension; the King must not be thought alienated from the Holy See.
- R96 (6/I/4, f. 81r): awaiting the nuncio's answer on the marriage; union of the three principal princes of
  Christendom; a heretic prosecuted by the Holy Office; the Hermits of St Jerome (Jeronimites).
- R97 (6/I/5, ff. 88r–89v, 4 pp.): Bolognese exiles (fuorusciti) sheltered in the King's lands, the Cavaliere
  Gualengo; the King as the Holy See's feudatory for Naples must hand back exiles under the investiture; the Turk in
  Adrianople, a French ambassador there, the German Protestants promising the Sultan help; danger to Christendom.
- R98 (6/I/6, f. 136r): the King's orders to his ministers about the clergy are delayed by waiting for commissions.
- R99 (6/I/7, f. 169r–v): the Order of St John and its Grand Master; Don John of Austria; the Milan senate against
  the archbishop (Borromeo) over the Corpus Domini procession; the Pope will use spiritual arms.
- R100 (6/I/8): the King's ministers' proceedings; a brief to be executed.
- R101 (6/I/9, f. 291r–v): Naples census (the hackney and the feudal dues of St Peter's day), the investiture, the
  schism threatened by the ministers; the King's realms will be troubled if he does not remedy it.
- R102 (6/I/10, f. 306r): a prelate "deputato in regno" failing in his office; the Pope might have made him cardinal.
- R115 (6/II/13, f. 641r, 1569): pensions on a see, the King's nomination, a commission; the Council.

## Grades and what is open

- Reading is continuous Italian throughout; individual letters are model choices (M), words H where the context
  forces them. Lasry's tentative glosses kept: 1040 Regina di Francia?, 3040 Fiandra?, 8090 sauere?, 2020 con?.
- Unlisted dotted groups met: [01.] [02.] [03.] [04.] [08.] [09.] [1.] [40.] [43.] [44.] [51.] [60.] [70.] [80.] [90.]
  — mostly punctuation-like (04. and 60. recur where a comma or "et" fits); not resolved.
- Not done: comparison with the contemporary decifrati and with Serrano, *Correspondencia diplomática entre España y
  la Santa Sede durante el pontificado de S. Pío V* (1914), which prints Alessandrino–Castagna letters of 1566–68 and
  may give some of these in clear. HathiTrust full-text search returned 403 from here.
- Transcriptions are DECODE's (TimB 2016, RebAn, Midas) and were not re-checked against the images.

## Verification 4, 23 Oct 2026

The v4 sweep could not score R93, R96, R97, R98, R99, R102 and R115: their entries pointed at the unspaced beam
decodes (`texts/<rec>_decryption.txt`). Each was re-decoded with the key as extended from the R94/R95/R100
decipherments (`reread_aless_decode.py`, which the 22 Oct re-read had used only on the four) and word-divided as
`texts/<rec>_reading.md`, every beam choice not checked on the figures bracketed. v2_score, explicit holes:

| record | explicit holes | hole rate | words |
|---|---|---|---|
| R102 | 0.556 | 0.115 | 122 |
| R97 | 0.486 | 0.137 | 422 |
| R99 | 0.45 | 0.161 | 242 |
| R96 | 0.429 | 0.176 | 153 |
| R93 | 0.375 | 0.156 | 90 |
| R98 | 0.333 | 0.258 | 128 |
| R115 | 0.167 | 0.301 | 136 |

The audit's "build Italian sentences with scattered slips" does not hold once the text is divided into words: the
polyphonic digits leave many words as model choices. All seven **demoted to decoded, not read** (partial readings
kept). Class read -> read in part; fraction_read 1.0 -> 0.333 (3,519 of 10,555 items in R94, R95, R100, R101). The
way forward is the one that worked for R94-R101: open these records' DECODE cleartext images for contemporary
decipherments, then re-read on the figures with `reread_aless_align.py`.

## Remaining gaps

- R94 (2 short gaps): "9 0 4 0 2 0" before S.M. and the verb 6 2 4 7 6 after "comincia" - blocker: open-codes; the contemporary decipherer left the first unread and guessed the second; no other text of the letter (Serrano 1914 not reachable)
- R95 (4 holes): dotted groups [08.] (the Crusade?) and [3.] (a person), "co[…]", "[?fece]" - blocker: open-codes; the decipherment is illegible at these words
- R101 (5 holes): two places in row 1 under a burn and a hole in the paper, one illegible group in row 14, "[?Sora]", codes 9090, 6020, 8020 - blocker: illegible
- R93, R96, R97, R98, R99, R102, R115: decoded, not read (23 Oct 2026) - blocker: not-attempted; their DECODE cleartext images not yet opened for decipherments, no figure-by-figure re-reading yet
- Serrano, Correspondencia diplomatica ... Pio V (1914): not checked - blocker: needs-physical-access (HathiTrust 403 from here, not on archive.org)

## Escalation

- [x] siblings: all eleven Spagna 6/I and 6/II ciphers decoded with the same key; the R94/R95/R100 decipherments extended it and the extension read R101
- [ ] clear-pages: cleartext images of R93, R96-R99, R102, R115 not yet opened. Done: 22 Oct 2026, all 45 DECODE cleartext images of R94, R95, R100, R101 looked at; decipherments found for R94 (f. 45r), R95 (f. 58r), R100 (f. 280r), none for R101; R94's covering letter dates it 7 Nov 1567
- [x] known-keys: Lasry's reconstructed key (DECODE, 2020)
- [x] print: 22 Oct 2026, Serrano 1914 searched again: not on archive.org, HathiTrust full text 403, Google Books API quota exhausted; Serrano's Liga de Lepanto (1918-19) begins in 1570 - not reached
- [x] key-rebuild: 22 Oct 2026, key extended from the decipherments (9 = con, dotted 0 = z, 0^.0 = et, codes 1040, 3020, 3060, 4020, 4040, 4080, 5070, 6050, 6060, 8090); [01.], [03.], [08.], [3.], [4.]8 (= perché), 9090, 6020, 8020 partly or not resolved
- [x] retry: 22 Oct 2026, R94, R95, R100, R101 re-read (texts/R94-R101_reread_log.md); all four build sentences; 23 Oct 2026 the other seven re-decoded with the extended key and word-divided: below the bar
