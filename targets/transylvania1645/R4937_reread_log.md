# Re-reading log, R4937 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b15)

## Starting point
Decoded, not read: a 25-line extract and a quadgram solver output under a different key.

## What was done
1. **Is there a text already?** One image, no attachments on the DECODE record; no edition found (see the R4936 log).
2. **Transcription** of the whole page, 34 lines, 869 cipher letters (`R4937-transcription.txt`), from 2-2.2x crops;
   clear words in braces; line 23 begins with a struck-out run, not transcribed.
3. **Decode** with the family key unchanged: it reads at sight ("czasar dipplomaia serent semmit nem sem akar
   efectualni..."). The solver key of 23 Sept (m=r, h=z ...) was wrong for this hand.
4. **Alignment** (`R4937_align.tsv`): 847 letters, 839 on the figure's own value, 3 class-resolved, 4 inside
   `[?words]`, 1 supplied (`herce[g]`). Cipher l (=k) and r (=h) are confused twice (`hamis`, `ha szinte`).
5. **Score**: `_check_reading.py` 0.05 (see the R4936 log for why the checker cannot score this Hungarian); explicit holes
   only (`b17_score.py` with `HOLES=1`) 0.90 (18 of 20 sentences). Set read, grade B.

## Open
l. 3 `idrwhdxxgkgwi` after `megsegni` (decodes to `oharossuluan`, no word); l. 13 end (`aznekicautep` before the clear
`-lekedgink`); `[?sinluan]`, `[?satisfactiohoz]` (one figure b for o), `[?sabadsagunk]`, `[?benmek]`, `[?is]`.
Sender not named on the page.
