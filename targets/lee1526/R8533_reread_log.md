# Re-reading log, R8533 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b29)

## Starting point

Reading audit (22 Oct): "decoded, not read". `r8533_reading.txt` was a sign-level worksheet (cipher words only, 414 of
457 read) with no running text; f. 109r and f. 110r had not been re-read at full resolution (pass 2), and the clear
text between the cipher runs was only roughly transcribed in pass 1. Clean-sentence share before: no running text
(0.00).

## What was done

1. **Every file on the DECODE record**: R8533 fetched with the project cookie (`research/reading_audit/b28_fetch.py`):
   four images (P1 f. 109r, P2 f. 110r, P3 address leaf, P4 f. 109v, each about 6600 x 9300) and one attachment,
   `DOC_8533_2024-Oct-10-20-23-55_82215.png`, which is S. Tomokiyo's Lee-Worcester key table (the key already in use),
   not a decipherment. No other text of the letter on the record.
2. **Existing text?** Tuke's interlinear decipherment of the f. 110r runs (on the leaf); L&P IV 3055 calendars the
   letter only as a duplicate of 3028 (8 April), whose decipherment by Tuke is at TNA (not online). L&P 3028 was used to
   check sense only.
3. **Read on the image**: the three written pages cut into half-width bands of three lines at 0.42 scale
   (`research/reading_audit/b29_strips.py`; f. 109r 12 bands, f. 109v 13, f. 110r 12) and every line read, clear and
   cipher; doubtful places zoomed at 0.8 (`b28_crop.py`). The clear text was transcribed for the first time as running
   text; the cipher runs were checked sign by sign against the pass-2 worksheet and corrected where the image differs
   (`R8533_corrections.tsv`, 12 rows).
4. **Key**: no value changed. Two code signs read by context and flagged: the cross on f. 109r l. 17 read as *the King
   [of England]* (Tuke's gloss of the same cross on f. 110r l. 22), not *the French King*; the lone stroke ı as *to* and
   *that* (as in the worksheet).
5. **Reading** (`R8533_reading.md`): running text, clear and cipher together, spelling as written. Word-by-word
   alignment: each cipher word was compared with its sign run on the strips, each clear word with the image; words
   neither carries are bracketed (`[..]self`, `[but]`, `[I]`); unread sign clusters (name codes, underlined clusters,
   blots) are `[..]`. **Look-alike alternates: 2 letters** (the o of *Perote*, f. 109v l. 1, read ⊥ where the stroke is
   closer to +; the p of *Perot*, f. 109r l. 13, † or +) **and 1 code sign** (the King's cross, f. 109r l. 17).
6. **Score** (`research/reading_audit/b17_score.py`, LANG_=en, reading body): **0.158 (15/95)** with the modern word list
   (1527 spelling: *bycause, myghte, doughter, sholde, englonde* ...), **0.895 (85/95)** counting explicit holes only
   (HOLES=1). Holes: 1192 words, 0.056 explicit-hole rate.
7. **Reader's judgement**: the sentences hold and translate (`R8533_en.md`): Almain's warning not to trust Francis I,
   Perrenot's letter (the King of England's offer of his daughter and Boulogne; Wolsey's request for French envoys; the
   triumph for the Duke of Richmond, to be King of Ireland), the French match with Eleanor pursued, wives for Richmond,
   an exchange of privy-chamber men, no secret treaty, the Swiss, the news from Italy (Moncada, Vaudémont, the Viceroy at
   Ceprano, Trivulzio's men, Russell's leg), and the closing advice on don Inachus (Mendoza). The unread places are
   name codes and short clusters inside sentences that still build. Read, grade B.

## Open

- Name and code signs outside Tomokiyo's table (ꟸ, A, ʍ, m, R ʌʌ, x ℯ² x²², the f. 109v l. 15 cluster, the
  underlined clusters on f. 109r and f. 110r l. 18): blocker **no-key-material** (Tuke's decipherment of the 8 April
  original, which would gloss them, is at TNA and not online; the f. 110r interlinear skips the one cluster there).
- Clear words not settled (f. 109v l. 7 *don [?Inarches]*, *[?nowe]*; f. 110r ll. 8, 11-13, 16, 23 and 26, a few words
  each): blocker **illegible** at the DECODE resolution in Lee's hand.
- Blots and struck signs (f. 109r ll. 12, 23, 24; f. 109v ll. 3, 9, 13): blocker **illegible**.
