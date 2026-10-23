# A member of Henrietta Maria's household (Paris) to Charles I, January 1646 — Lasry's "SP106-8" key — TNA SP 106/10 ff. 235–236 (DECODE R924) — NOTES

Status: in progress. Read 23 Oct 2026 (b35) from Lasry's key; writer Henry Jermyn (Sams); 85 code tokens open.

**24 Oct 2026, Lasry permission** (Claude Opus 5.5): George Lasry gave permission on 24 Oct 2026 to use his DECODE decryptions with attribution. His plaintext (D3090) is now in the repository as `lasry/R924_decryption.txt` (verbatim, attribution header), and the reading and English carry the credit line. read_share re-measured: see profile; state *read in part* (85 code tokens (58 distinct) his key lacks are the holes; four sense-valued codes count as holes). Credit: George Lasry (decryption on DECODE, used with his permission, 24 Oct 2026).

**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): Lasry's plaintext of R924 is on the DECODE record only; the git-ignored copy is in no checkout, so nothing of the letter could be read. R924 is *decoded, not read* in profile.json; class already solved is kept (his decipherment exists), fraction_read 0.9195 -> 0 (the old figure was key coverage).

Split on 14 Oct 2026 from `hm1645` under the one-key rule (George Lasry, 14 Oct 2026). The old entry (catalogue 59)
joined six letters of SP 106/10 in four of Lasry's reconstructed keys. This letter is the only one of the six in his
**"SP106-8"** key. The others are different ciphers, each with its own entry and page: [`targets/hm1645/`](../hm1645/NOTES.md)
(R785, R790, R923, key TNA SP 106), [`targets/sp106r787/`](../sp106r787/NOTES.md) (R787, SP106-2),
[`targets/sp106r929/`](../sp106r929/NOTES.md) (R929, SP106-5).

**Outcome: read from existing decipherment.** Lasry's key and interlinear plaintext are on the DECODE record
(23 Oct 2020). Nothing about the text is added here. Sessions 2026-09-19 and 2026-10-14.


**23 Oct 2026, re-read b35** (`R924_reread_log.md`): Lasry's files fetched with the shared cookie (now in `decode/`,
git-ignored) and the letter decoded afresh from Pettersson's rows (`research/reading_audit/b35_r924dec.py`; signs
`R924_signs.txt`, decode `R924_decode.txt`). Unvalued low figures are nulls between words; "Ian. 26" and "5 or 6
thousand" are numerals in clear; four codes valued by sense at every occurrence (168 *hope*, not *hold*; 116 *can*;
334 *what*; 227 *new*). **Read, grade B**: `R924_reading.md` (0.545 plain, 0.649 explicit holes, English of 1646),
`R924_en.md`. Found: **Eric Sams deciphered this letter and the Queen's (R925) in 1976** for Ian Roy (*Archivaria* 21,
1985-86, pp. 89-90; his solution unprinted); the writer is **Henry Jermyn**, dated Paris 26 January 1646, the day of
his letter to Nicholas referring him to "the kinge his letters" on the Portugal embassy.

## The record

- DECODE R924 "TNA_SP106/10_UND_(0235-0236)", two images (`decode/IMG_R924_I4915_P1.png`, `_I4916_P2.png`,
  git-ignored). The cipher runs sideways on the leaves, numbers separated by colons.
- Files on the record (in `decode/`, git-ignored, DECODE's and Lasry's work): `DOC_R924_D1817` Pettersson's
  transcription (2019); `D3089` Lasry's key "TNA SP106-8" (dated 1646-01); `D3091` his interlinear cipher/plaintext of
  ff. 235–236 and 238–240; `D3090` his plaintext with dating notes.
- 2012 cipher groups, 214 distinct (`python docs/_check_profile.py --measure targets/sp106r924/decode/R924_ciphertext.txt`).
- Lasry's plaintext opens "PARIS JAN <DATE E> <207> IT PLEAS YOUR MAJESTY YOU HAVE SO MUCH <797> <320> HANDS ...":
  a writer at Paris to the King against Sir H. Compton's journey and the treaty for Prince Charles's marriage with
  Portugal, on Montreuil's mission, the frost that stopped the river traffic, levies in hand to send over "a body of
  5 or 6 thousand men". "The Queen sends ..." and "the Queen desires your Majesty ..." show the writer is not the
  Queen. Signed "I AM YOUR MAJESTY S <219> OBEDIENT <SERVANT> <385>".
- Lasry's dating note: "First letter dated January ... Montreuil - French emissary ... Also mentions frost like
  0245-0246 so either both collections are from Jan 1645, or from 1646 (more likely)". His note on the sibling
  R925 puts Henry Compton's embassy to Portugal in 1646–48.
- DECODE's start date is 26 June 1646; the letter says "Paris Jan". Queued as a correction (`decode_updates/queue.json`).
- Same key, in Lasry's file: R925 (ff. 238–240), a letter of the Queen (his "Second Letter from Queen": the marriage,
  Compton). Not a document of this entry.

## The key

Lasry's "TNA SP106-8": one- and two-digit homophones (A 15|23|25|5, E 11|2|22|26, ...) and a numbered word list from
100 up, roughly alphabetical (100 all, 101 are, 102 as, 103 at, 108 and, 109 be, 141 for, 173 I, 174 in, 176 ing ...).
His file says "There are no nulls".

## Check done here (14 Oct 2026)

```
python targets/sp106r924/apply_key.py targets/sp106r924/decode/DOC_R924_D3089_3089.txt 0235-0236 targets/sp106r924/decode/DOC_R924_D3091_3091.txt
```

2012 groups; 1850 (91.9%) get a value from the key. On 11 lines Lasry's plaintext line has a different number of
words from the cipher line and the columns shift; on the others (1604 keyed groups) every value equals his
plaintext. 162 groups have no value: 58 distinct three-digit numbers (85 tokens: 324 ×4, 428 ×4, 321 ×3, 532 ×3,
208 ×3 ...) and 11 low figures (77 tokens: 21 ×24, 30 ×15, 42 ×12, 50 ×9, 16 ×7 ...), which Lasry renders "_".
The reveal on the page is the first 120 groups of this run.

## Remaining gaps
- R924 as a whole: decoded, not read (verify sweep 23 Oct 2026); the four code values set by sense (168 hope, 116 can, 334 what, 227 new) and 85 open code tokens - blocker: no-key-material; Lasry's key lacks the open codes and gives hold/brought where the sense needs hope/can; Sams's 1976 solution is not printed (needs the Bodleian).

- three-digit word-list numbers with no value (58 distinct, 85 tokens: 324, 428, 321, 532, 208, 797 ...) - blocker: no-key-material; four valued by sense here (R924_reread_log.md); Sams's 1976 solution is unprinted
- Eric Sams's decipherment (1976) - blocker: needs-physical-access; filed in the Bodleian per his letter to R. A. Sayce (9 Oct 1976)

## Escalation

- [x] siblings: R925 (ff. 238-240) is in the same key per Lasry's file; the other SP 106/10 letters are in other keys
- [x] clear-pages: none; the record holds no clear copy
- [x] known-keys: Lasry's SP106-8 key is the key; applied here (agrees with his plaintext)
- [x] print: Lasry's DECODE files; Eric Sams's 1976 solution exists (Archivaria 21) but is unprinted
- [n/a] key-rebuild: the entry is read from Lasry's existing decipherment; filling his word list (with R925) is new work for a later session
- [x] retry: 23 Oct 2026, decoded afresh with his key, nulls and four sense values; read (b35)

## Assumptions for George's review

- The key groups follow the CATALOG NAME headers of George Lasry's DECODE files (23 Oct 2020): "TNA SP 106" for
  ff. 207-215, 218, 220-221, 230-234 (hm1645); SP106-2 for 216-217 and 219 (sp106r787); SP106-8 for 235-240
  (sp106r924); SP106-5 for 245-247 (sp106r929). His credit on each entry covers only the letters in that key.
- Only sp106r929 counts as "read with known key" (his key applied before his plaintext was compared, 19 Sept 2026);
  the other three entries are "read from existing decipherment", the key applied only as a check.
- Figures his key leaves without a value are treated as open, not as nulls, although his key files say "There are
  no nulls".

## 23 Oct 2026 — verify sweep (reading audit v2): back to decoded, not read
- The b35 reading (`R924_reading.md`) scored 0.649 (50/77) on explicit holes with four code values adopted by sense:
  168 *hope* (7x; Lasry *hold*), 116 *can* (5x; Lasry *brought*), 334 *what* (2x), 227 *new* (2x; Lasry's plaintext
  has NEW). With those 16 words counted as holes the body scores **0.597 (46/77)**, 0.494 plain
  (`research/reading_audit/v2_score.py`); leaving 227 out (Lasry carries it) changes nothing. Under the bar, with code
  holes in most sentences; Lasry's own plaintext does not read at those places either.
- Result: `decoded, not read`, reading kept as a partial reading; fraction_read 1.0 -> 0; class `already solved`
  unchanged (Lasry's decipherment is on DECODE). Sams's 1976 decipherment (Bodleian / Ian Roy papers) would settle the
  four values and many of the 58 open codes.
