# Filippo Maria Visconti to Francesco Sforza, Cusago 23 Jan 1447, in the Duke's second key (BnF italien 1584 f. 15)

Status: read (deciphered with DECODE key R5324; checked against the clear text f. 16 on the same mount).

## The document

BnF italien 1584 (Archivio Sforzesco, 1447) f. 15: a parchment slip wholly in cipher, 15 lines, Duke Filippo Maria
Visconti to his son-in-law Count Francesco Sforza, dated in cipher "Cusaghi die vigesimo tertio ianuarii" (Mazzatinti,
*Inventario*, 1883/1887: "Lettera del Duca al medesimo (Cusago 23 gennaio). In cifre: membran."). Gallica ark
`btv1b100373864`, canvas 17 (upper piece); IIIF image API `openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b100373864/f17/`.
Below it on the same mount is f. 16, the same letter in clear ("Filia 1447. 13 Januarii. Cusaghi" in a later pencil;
dated in the text "Cusaghi die vigesimo tertio Januarii"), not listed separately by Mazzatinti.

Split out of `targets/visconti1446/` on 29 Oct 2026 (one key, one entry): the Duke's twenty other slips of Nov 1446 -
Mar 1447 are all in his other key, R5323, and are written up there.

## Key

`key.md`. ASMi Carteggio Sforzesco cart. 1597 no. 24 = DECODE **R5324**, an 18th-c. copy headed "Filippo Maria Duca di
Milano", catalogued on DECODE as a key with no names and a 1450-1555 date range. Found 28 Oct 2026 while fetching the
15th-c. keys of cart. 1597 (R5301-R5340) for the visconti1446 slips: nos. 23 and 24 carry the Duke's name. R5323 fits
those slips; f. 15 opened with signs R5323 does not have, and R5324 fitted it from the first word ("Per vostre
lettere date ...").

## Reading

`texts/f15.md` (per line: signs, values, plaintext; comparison table), `texts/f15_reading.md`, `texts/f15_en.md`,
`texts/f15_tokens.tsv`, `texts/f15_signs.txt`, `texts/f15_clear.md` (f. 16 transcribed).

722 cipher tokens (87 distinct; `docs/_check_profile.py --measure texts/f15_signs.txt`): 686 read, 22 nulls, 14 unread
= 95.0% of all tokens, 98.0% of the 700 non-null tokens. Against f. 16, over the 629 tokens that carry text up to the
date: 604 agree = 96.0%; the 23 disagreements are wording and spelling (cipher "recordi" where f. 16 has "pareri",
"mandaremo"/"mandamo", "Pedro da"/"Piero de", "conseglii"/"consigli"). So f. 16 is a parallel clear minute, not a copy
made from the cipher.

The Duke thanks Sforza for his letters of the 11th and his advice, which shows he is worthy of his forebears, and
following it will send another ambassador to the Pope and the King of Aragon, besides Pietro da Pusterla and Antonio da
Trezzo, to act for "the Count" and take orders from him and from Sforza. The slip ends, after the date, with the Duke's
full title in cipher: "Filippus Maria Anglus, Dux Mediolani etcetera, Papie Anglerieque comes ac Ianue dominus".

## Prior solution

f. 16, the clear text, has sat on the same mount since the letters were filed: the letter was never unread. What is new
here is the key's identification (R5324 is unlabelled on DECODE) and its check against a clear text. The clear text was
in view during the transcription (worker A calibrated the slip's sign shapes on it).

## Remaining gaps

- five signs between the date and the title, and seven after the title - blocker: too-short; isolated groups with no
  context (the closing groups of the R5323 slips are padding, `targets/visconti1446/texts/closing_groups.md`)
- two signs in the text (l. 8 first sign, l. 9 last sign) - blocker: illegible; at the slip's edge

## Escalation

- [x] siblings: the twenty R5323 slips of the same correspondence (targets/visconti1446); none is in this key
- [x] clear-pages: f. 16 on the same mount is the clear text, transcribed and compared
- [x] known-keys: R5323 and R5324 tried; R5324 fits
- [x] print: Mazzatinti 1883/1887 lists the slip only; no edition found (web search 29 Oct 2026)
- [n/a] key-rebuild: the key is on DECODE; three code words not on the copy were read against f. 16
- [n/a] retry: the open signs are padding-position groups and two edge signs

## Log

- 28 Oct 2026 (Opus 5.5, with subagent worker A): canvas mapped; R5324 identified; f. 15 transcribed and deciphered,
  compared with f. 16.
- 29 Oct 2026: split into its own folder from targets/visconti1446.
