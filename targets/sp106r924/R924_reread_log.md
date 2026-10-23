# Re-reading log, R924 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b35)

## Starting point

Reading audit (22 Oct): "decoded, not read" because no text of the letter was in any checkout (Lasry's DECODE files
git-ignored). Before = 0.00 (no reading file).

## 1. Is there a text already?

- DECODE R924 record fetched with the project cookie (`research/reading_audit/b35_fetch.py`): 2 images (ff. 235-236)
  and 4 files (Pettersson's transcription D1817; Lasry's key D3089, plaintext D3090, interlinear D3091). The files are
  now in `decode/` (git-ignored, DECODE's and Lasry's work). Both images opened: cipher only, no interlinear, no
  decipherment, no clear copy.
- Neighbouring records R922 (Hungarian, not this volume), R923 (ff. 233-234, other key), R925 (ff. 238-240, the
  Queen's French letter in the same key), R926 (no files): opened; R925's three images and R788's are cipher only.
  f. 237 is on no DECODE record (TNA, not online).
- **Eric Sams deciphered this letter in 1976**: "Cryptanalysis and Historical Research", *Archivaria* 21 (1985-86),
  pp. 87-97 at 89-90 (a number cipher in Abraham Cowley's hand used for two letters to Charles I, one from Baron
  Jermyn, in English, the other from Henrietta Maria, in French, January 1646, PRO); his letter to R. A. Sayce,
  9 Oct 1976 (ericsams.org): solved for Ian Roy. His solution is not printed (the ericsams.org page "Solutions to the
  cipher letters of Henrietta Maria and Prince Rupert", 1976, holds no text; he says his decryptments were filed in the
  Bodleian). So: the writer is **Henry Jermyn** (Sams), and a prior decipherment exists but is out of reach
  (needs-physical-access). Jermyn's letter to Nicholas of 26 Jan 1646 (SP 106/10 no. 15, Adolph, *Collected Letters
  of Jermyn*, 2023) refers Nicholas "to the kinge his letters" on "the embassage and marriage of Portugall": this
  letter, same day.

## 2-3. Decode, key, alignment

- Decoded afresh from Pettersson's rows with Lasry's key (`b35_r924dec.py`; signs `R924_signs.txt`, corrections
  `R924_corrections.tsv`, decode `R924_decode.txt`). Lasry's interlinear had 11 lines whose columns shift; the fresh
  decode has none.
- Corrections: the date "Ian. 26" (26 as a numeral, not E); "a body of 5 or 6 thousand men" (5, 6 numerals in clear).
- Unvalued figures below 100 (21, 30, 42, 50, 16 ...) stand between words everywhere: nulls / word dividers.
- **Code values adopted by sense (flagged)**, each holding at every occurrence:
  - 168 *hope* (Lasry *hold*), 7 occurrences: "I hope to evidence", "the hopes of that which", "they can hope for an
    ambassador", "they have no hopes of any", "the hope of the summe of money ... is the highest delusion", "good
    [118] to hope that we should", "which I hope will be of great use"; *hold* is spelled out in letters elsewhere in
    the letter ("I will hold your Majesty no later"), so 168 is not *hold*; its slot (167 has, 173 I) fits.
  - 116 *can* (Lasry *brought*), 5: "that treaty can not possibly", "the greatest step that can be [208]", "you can
    [127] for them", "they can hope", "that can [208] to the prejudice". Its slot (114 been, 118 bring) does not fit
    *can* alphabetically, nor does *brought* (after *bring*); the list is not strictly ordered. Sense only.
  - 334 *what*, 2: "we had seen what might have been relied on", "this and what [357] writes"; w-block (322-330).
  - 227 *new*, 2: "any new order", "if a news"; n-block (229 not). Lasry's plaintext already had NEW.
- Lasry's own guesses marked "?" in his key are bracketed `[?word]`: Holland (561), Scots (744), way (330), assume
  (429), we (328), well (337), humble (550). His *convince* (487) is not used: "Sr H. Compton is [487]d" and "for not
  [487] him" do not take it.
- 118 *bring* kept where it fits (3 of 4); at "we have good [118] to hope" it does not, so `[118]` there.
- Word-by-word alignment (`b35_align.py` reading vs decode): every difference is a code word standing for a syllable
  (THERE = ther, ARE = ar in *marriage*, LATE = lat), a doubled letter of the cipher, or a bracketed item; three
  modernised spellings found and restored to the figures (*nether*, *ether*, *breifly*); *coniuntion*, *disiont*,
  *concerrning* as written. Supplied words: none unbracketed.
- Look-alike letters: 0 (no letter of the reading rests on another sign's value).

## 4. Score

| | before | after |
|---|---|---|
| reading body, b17 plain (LANG_=en) | 0.00 | 0.545 (42/77) |
| reading body, b17 HOLES=1 | — | **0.649 (50/77)** |

English of 1646: the word list does not know the period spelling (*iourney*, *svre*, *treatyd*), so the explicit-hole
figure is the bar. Reader's judgement: the argument holds sentence by sentence (against Compton's journey to Portugal;
the Dutch match and the States; the frost; Montreuil; the levies of 5 or 6 thousand men; the Queen's request), with
code holes in most sentences but at most one or two per clause. Two passages stay thin: "that treaty can not possibly
... be at [?ani] […]" and "[382] will presently returne ... will subs[…] good [321] these men arrive".

## Result

Read, grade B: Lasry's key with four sense-valued codes, Pettersson's transcription, nulls as dividers.

## Open

- 85 code tokens with no value (58 distinct: 324, 428, 321, 532, 208, 797 ...) - blocker: no-key-material (Sams's
  1976 solution not printed; R925 shares few of them).
- Sams's own decipherment - blocker: needs-physical-access (Bodleian / Ian Roy papers).
