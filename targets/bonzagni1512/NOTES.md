# Giovanni Battista Bonzagni (Eger) to Ippolito I d'Este, 1512–1514 (ASMo, Ambasciatori b. 4/12; DECODE R1123–R1125) — NOTES

Status: in progress. Re-read 22 Oct 2026 (b14): R1124 and R1125 read from the contemporary decipherments (texts/); R1123 read in part.

**22 Oct 2026, re-read (REREAD_BRIEF, batch b14).** DECODE re-fetched: images only, no attachments. R1125: the
slip (image 5) transcribed and aligned group by group with the p. 3 cipher block (texts/R1125_align.tsv); read
(0.857). R1124: the gloss over the eight cipher lines transcribed and aligned (texts/R1124_align.tsv), and the clear
text of pp. 1-2 transcribed around it; read (0.625; the misses are inventory words outside the lexicon). R1123: the
clear opening, the first cipher block (a thousand gold ducats gathered; the King of Hungary's order that the troops ride
out by the August feast of Our Lady; 300 florins through Alberto Pratonerio's father) and the start of the lower block
read; the rest of the lower block (an inventory) and p. 2's cipher are not, so it stays decoded, not read. The cipher
holds Latin-looking code words among its signs: potest = Re d'Ungaria, valent = denaro/argenti, indigeo, parte. Log:
texts/R1123-R1125_reread_log.md. Class not read -> read in part; method read from existing decipherment; fraction
read c. 0.46 (estimated from word-group counts).

**22 Oct 2026, reading audit** (George Lasry's test): no text of R1123, R1124 or R1125 is in the repository; the decipherments are on the DECODE images only (main checkout `img/`). All three are *decoded, not read* in profile.json; class already solved -> not read and method -> not solved until the decipherments are transcribed. The verdict below (read at the time) stands as history, not as a reading held here.

Earlier status (before the 22 Oct 2026 reading audit): no write-up

**Verdict: read at the time. Nothing is left to decipher.** Catalogue entry 155 is resolved and removed. Checked
in one session on 2026-09-21.

## Sources

- DECODE R1123–R1125 (record pages in `decode/`). Images fetched with the shared cookie into the git-ignored `img/`
  of the main checkout. The DECODE status is "Partially decrypted"; there are no DOC_ files.
- Vestigia (vestigia.hu, public, no login): a search for "Bonzagni" returns 46 items, covering Bonzagni's whole
  file in ASMo Ambasciatori, Ungheria b. 4 (1512–1521). The list is in `vestigia/search_bonzagni.json`. Records for
  nos. 4, 5, 6, 10, 12a, 13, 14, 17 and 18 are in `vestigia/v*.json`.

| DECODE | ASMo b. 4 no. | Vestigia | date | pp. | cipher |
|---|---|---|---|---|---|
| R1123 | 4 | 1796 | Eger, 2 Aug 1512 | 4 | p. 1: c. 14 lines, a contemporary interlinear decipherment over every word; p. 2: two short groups, also glossed |
| R1124 | 6 | 1798 | Eger, 4 Aug 1512 | 2 | p. 1: 8 lines (Beatrice's jewels: cups, bowls, salts), interlinear decipherment throughout |
| R1125 | 12 (Vestigia "12a") | 1804 | Eger, 28 Dec 1514 | 5 | p. 3: 13 lines, no interlinear; image 5 is a separate decipherment slip (later hand, archive tag "1804-6c ... rejtjel megfejtés", i.e. "cipher decipherment") |

## The cipher

A simple substitution of invented, letter-like signs (Greek- and Latin-looking forms) for the letters of Italian,
with word division kept, plus a few word signs (a doubled cross for *et*). It is the same alphabet in all three letters.

## Check on R1125

The only passage without a gloss on its own leaf is the p. 3 block of R1125. The slip (image 5) begins "Mando per
Ladislao lator presto sei cavalli del pelo et valore si contiene in la inclusa lista; poi te mando uno bacino de
marche nove et oncie sei, pesetti tre, et una bronzina de marche tre oncie sei et mezo. De denaro non posso mandare
... perchè non ho ancora posso uno fiorino ...". Aligned word by word with the cipher's first four lines, the lengths
agree, and the letters repeat consistently: *sei* = f τ 3, *si* = f 3, *la* = m ω, *lator* = m ω f n f, *poi* =
α n 3, *bacino* = G ω λ 3 p n, *nove* = p n ι τ, *et* = the doubled cross. So the slip is the decipherment of that
block. The clear p. 4 continues the same business (the horses "non ho mandati al presente").

What the ciphers hide is private and household business, not state secrets: the estate of a dead man's goods and
jewels, horses and silver sent to Ippolito, and money. The political news (Bakócz, the Tatar khan, Poland, the Diet)
is in clear.

## Why no write-up

The letters were read at the time. Nothing here adds a reading, and the only new result is that the R1125 slip
belongs to its cipher block. A key table was not built. Per CLAUDE.md this is recorded as `Status: no write-up`.

## Remaining gaps

- R1123: the lower cipher block of p. 1 (about eleven glossed lines, an inventory of silver and sums) and the glossed cipher of p. 2 - blocker: illegible; the brown gloss ink is faint at the resolution of the DECODE and Vestigia photographs
- R1123: key rebuild to decode the signs under the faint glosses - blocker: not-attempted; about 170 aligned words in R1124/R1125 (texts/*_align.tsv) to rebuild it from; the next step
- R1125: the code word "parte" (cipher l. 7) and the number .31. (l. 10) - blocker: no-key-material; the slip leaves them out
- R1124: the torn right edge of p. 1 (clear text ll. 12-19) and the end of cipher l. 5 - blocker: illegible; paper lost

## Escalation

- [x] siblings: Bonzagni's file in ASMo Ambasciatori Ungheria b. 4 listed from Vestigia (46 items)
- [x] clear-pages: interlinear decipherments on R1123/R1124 and the R1125 slip found; not transcribed
- [n/a] known-keys: not needed, the decipherments exist
- [x] print: Kristóf 2018 (cited by Vestigia) not found online; web search 22 Oct 2026 found only her 2025 Eger article
- [ ] key-rebuild: needed for R1123's faint lower block; not attempted (22 Oct 2026)
- [x] retry: 22 Oct 2026, R1124 and R1125 transcribed and aligned; R1123 in part
