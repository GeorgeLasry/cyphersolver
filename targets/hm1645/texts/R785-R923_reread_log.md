# Re-reading log, R785, R790, R923 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b14)

## Starting point

Reading audit (22 Oct): all three "decoded, not read": George Lasry's plaintext (DECODE, 23 Oct 2020) had been taken
as the reading, but no copy was left in any checkout, so nothing could be read here.

## What was done

1. **Every file on the records opened.** research/reading_audit/b14_fetch.py (project cookie, still valid) fetched the
   three record pages and every linked file into the session scratchpad (not the repository: Lasry's and DECODE's
   work): per record Sofia Pettersson's transcription (DOC_R785_D1809, R790_D1815, R923_D1816), Lasry's key
   (D3059 = D3067 = D3068, one file), his interlinear cipher/plaintext (D3060 = D3065 = D3069) and his plaintext with
   dating notes (D3061 = D3066 = D3070), and the page images (R785 3, R790 2, R923 2; 2300 px wide, cipher written
   across the opening). No other decipherment, margin gloss or clear copy is on the records.
2. **Decode.** research/reading_audit/b14_hm.py decodes every cipher line of the interlinear file with Lasry's key and
   prints it beside his plaintext line (including the 17 lines whose columns do not line up, which apply_key.py skipped).
3. **Key corrections** that hold in every occurrence: 292 = "by" (Lasry "because": "here by the Queen", "by the next",
   "by degrees", "by unbusying the hands", "by his just acknowledgments", "byfore" = 292 341 e; 12 occurrences);
   435 = "next" (Lasry "of"; "by the next ocation", "until next week"; 438 remains "of").
4. **Nomenclator values proposed.** The three-figure groups from 279 up are an alphabetical codebook (279 and, 283
   able, 292-296 b-, 311-312 c-, 316-321 d-, 333 end, 341-343 f-, 355-357 g-, 362-371 h-, 380-386 i-, 396-401 l-,
   407-427 m-, 428-429 n-, 438-442 o-, 445-462 p-, 492-493 r-, 503-504 s-, 508-526 t-, 530-533 u-, 536-551 w-,
   553-555 y-), and the 1xx-2xx groups are names. A group's band plus its contexts across all six letters in the key
   (the three here and Lasry's French sections ff. 207-212, 218-221) fixes many of the 58 he left open:
   texts/hm1645_codes.tsv. Values that hold in two or more contexts are printed {word} in the readings (295
   business, 330 dispatch, 340 foot, 405 master, 446 particular, 502 she, 518 those, 548 who/who-ly/who-le, 392+498
   lord+ship ...); values from one context are [?word] (326 doth, 457 post, 459 public, 474 remainder, 497 succour,
   528 there, 539 what ...). 28 groups and the two-figure 85 and 60 stay open (40 tokens in the three readings).
5. **Images checked** where decode and sense disagreed: R785 l. 1 "pertectly" (the writer wrote 10, T); R923 l. 5
   "from the King this post" (the figure is 127, a 7 written over a 6: the Queen, as Lasry suspected); R923 l. 4 554
   "your" (4 over 5, the writer's correction); R923 l. 11 "some for-r-a-in 497" (341 is clear: "forrain [succour]",
   not Lasry's "Lorrain support"). Other one-figure slips (mget, dewanded, hong, chntinue, wnll ...) are normalised
   and listed in texts/hm1645_corrections.tsv, not checked on the images.
6. **Readings** (texts/R785_reading.md, R790_reading.md, R923_reading.md) written sentence by sentence from the decode,
   Lasry's plaintext alongside, in the figures' own spelling (slips as written). A first draft in modern spelling was
   replaced on the coordinator's instruction; that text is now the *_en.md files (modern spelling, holes kept).
7. **Alignment.** research/reading_audit/b14_align.py compares each reading letter by letter with the key decode
   (supplied [words] dropped): R785 0.978 of the reading's letters carried, R790 0.980, R923 0.959; every remaining
   difference was looked at and is a modernised spelling, u/v, a listed slip, or a word now bracketed ("King['s]",
   "{design}[ed]", "no[ne]", "[k]indness"); R923's difference at the end is Lasry's key list appended to the file.

## Result

_check_reading.py on the reading bodies (b14_score.py): R785 0.645 (40/62), R790 0.542 (13/24), R923 0.52 (13/25), in
the figures' spelling; the same texts in modern spelling scored 0.841, 0.792, 0.84. The difference is the modern word
list (lettre, answear, termes, takeing ...), not the sense. Letter-by-letter alignment with the decode: 0.992, 0.995,
0.984 carried. All three read as continuous English and are kept read.

What the letters say, beyond Lasry's notes: R785 is signed "A Cowley" (Abraham Cowley, then in the Queen's household
at St Germain) and is addressed to a peer ("your Lordship"); its third image (f. 215) is a second, unsigned letter in
the same key that begins mid-sentence. R923's "forrain succour" replaces Lasry's "Lorrain support", and its place 85,
twice "the releef of 85", is a town whose relief risked a battle in late September 1645 (perhaps Chester).

## Open

- 28 three-figure codes (120, 148, 208, 212, 228, 234, 237, 257, 300, 334, 344, 348, 350, 353, 424, 469, 486, 488, 489,
  500, 507, 522, 525, 529, 535, 541, 543, 545) and the two-figure 85 and 60: no-key-material (names or words seen
  once or twice with no context that fixes them; 541 has four contexts that do not agree on one word).
- The one- and two-figure groups with no value (77, 78, 16, 49, 59, 39, 79, 30 ...) fall between words throughout;
  read as separators. Not settled whether the writer meant them as nulls.
- R923 breaks off after "give him" (the record has no further leaf).

## Failures

- The first fetch timed out on a file; rerun with retries.
- Several one-figure slips were not checked on the images (2300-px images of a double page, figures about 15 px
  high); listed as such.
