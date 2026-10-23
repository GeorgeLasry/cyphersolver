# Re-reading log, Raince fr. 2984 residue of 13 May and 20 Nov 1526 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b32)

## Starting point

Reading audit (22 Oct): outcome.texts entry "residue1526" decoded, not read, judged on `trans/reading_edited.txt`
(the 17 Sept running French, '…' or '(?)' in nearly every line). The audit did not score `trans/reading_v3.txt`,
the 5 Oct re-reading of all 106 lines glyph by glyph off the numbered-token images (sense measure 0.870).
No reading file in the brief's form.

## What was done

1. **DECODE.** No record of fr. 2984 on DECODE (cached list searched for 2984 / Raince / Rainse: none; the notes of
   17 Sept say the same). Nothing to open.
2. **The volume.** The Gallica IIIF manifest of fr. 2984 (btv1b90598430, fetched 23 Oct) is still the black-and-white
   microfilm ("Numérisation effectuée à partir d'un document de substitution", 85 views, online 2011). Its item list
   (39 letters) names no decipherment or clear copy of the 13 May (no. 7) or 20 Nov (no. 24) letters; the clear
   doubles in the volume are of 9/11/12 June (nos. 1, 5). Pastor IX app. 38 (26 Nov, no. 25) is a parallel, not a copy
   (17 Sept notes). No DECODE record, no print and no contemporary decipherment: the letters are read on the image or
   not at all.
3. **Reading file.** `trans/residue1526_reading.md` built from `trans/reading_v3.txt` by
   research/reading_audit/b32_raince_build.py: words with unresolved glyphs as `[...]`, `word(?)` as `[?word]`,
   words broken at a line end joined where the join is a word (32 joins, listed by the script; 9 breaks checked by
   hand and kept, e.g. "souspirant | rant", "dessusdict | a"; "mes m | ement" joined as "mesmement"). No word added.
   The glyph readings themselves are the 5 Oct ones (not re-read this session).
4. **Score** (b17_score.py, LANG_=fr, reading body, with [X], [X2], [Y] counted as holes): **0.513 (59/115)** plain;
   explicit holes only (HOLES=1) **0.713 (82/115)**. The plain failures are of two kinds: holes (unresolved glyphs,
   p. 29 ll. 1-2, 8, 18; p. 30 ll. 15-17, 23-24, 28, 33-34; p. 31 ll. 4, 17; p. 105 ll. 5, 9, 12-14) and 1526 spellings
   the word list does not know (dessusdictz, imperiaulx, destruict, nuyt, escripuise, eusent, sceurement, uouldroyent).
5. **Look-alike alternates.** Not measurable from the files: the 5 Oct pass resolved the microfilm's confusable sets
   (e/r, t/l/d, s/u/a) glyph by glyph and left the unresolved ones as `?`, but it did not record which letters were
   chosen against the more likely shape. No contemporary or printed text confirms them.

## Result

Unchanged: decoded, not read. On the plain figure 0.513 the reading falls in the band kept unread for other French
letters (0.47-0.56: matignon1586 f. 124r, fiesque1567); on explicit holes it would pass (0.713). The sentences of
p. 29 ll. 11-25, p. 31 and p. 105 ll. 1-8 hold; p. 30 and p. 105 ll. 9-21 have a hole in most sentences. The partial
reading is kept as `trans/residue1526_reading.md`.

## Open

- The unresolved glyphs (about one word in eleven) - blocker: illegible (the only images are the B/W microfilm;
  colour photographs of pp. 29-31 and 105 would decide them).
- [X], [X2], [Y] - blocker: no-key-material (not in Tomokiyo's key; [X2] perhaps i, see NOTES session 3b).
- The look-alike share - not-attempted (would need a per-token record of the 5 Oct choices).
