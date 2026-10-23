# Re-reading log, R2276, the lines decoded, not read (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b32)

## Starting point

Reading audit (22 Oct): outcome.texts entry 1 (p. 1 ll. 16-26, 38-40; p. 2 ll. 1-3, 13-21, 36-40) "decoded, not read";
entry 0 (the rest of the letter) read in part, grade B. Clean-sentence share of the unread lines before, taken from
`reading.txt` with every `?` as a hole (research/reading_audit/b17_score.py, LANG_=fr): **0.069 (2/29)**, explicit
holes only (HOLES=1) **0.172 (5/29)**, hole rate 0.25-0.32 over 352 words.

## What was done

1. **The DECODE record.** R2276 fetched again with the project cookie (b28_fetch.py): three page images, no attachment,
   no transcription, no comment block; the record says "Non-decrypted" and points to Tomokiyo's guise.htm. Neighbours
   R2275 (a Saxon cipher book, Dresden) and R2277 (fr. 20974 pp. 25-28, a different cipher read by Lasry/Biermann with
   the key on p. 93) are not this letter.
2. **Another scholar's text?** Tomokiyo's guise.htm and nevers.htm fetched 23 Oct: still only "In 2021, Norbert
   Biermann found that this can be read with the Nevers-Piles cipher" (private communication); no text of a reading.
3. **The key source.** The BnF catalogue record of fr. 3612 (archivesetmanuscrits cc50062c, fetched 23 Oct) lists the
   ciphered letters of Jehan de Piles to Nevers with their decipherments (ff. 11, 15, 43, 56, 60, 86, 98, 101: 1586),
   which is where Tomokiyo's Nevers-Piles table comes from. The record has no Gallica link (no digitised item): the
   volume that would give the missing sign values is still not online.
4. **The volume.** fr. 20974 is the Guise 1556 keys volume; pp. 1-3 are this letter and p. 4 its verso with a pasted
   1556 key. No decipherment of the letter is bound in it (Tomokiyo's item list, our 5 Oct pass over the Gallica
   scan). The descriptions of the 331 digitised Gallica volumes with cipher items (research/gallica_sweep/
   sru_chiffre_desc.json) grepped for Piles, Orbais and Reims: Piles letters of 1592-1595 and Brulart from Reims 1590,
   nothing of June 1589 and no deciphered copy of this letter.
5. **The image.** p. 1 ll. 21-26 cropped again from the DECODE PNG (3016 x 4656): the right half of the leaf is lost
   on these lines (the text stops at the tear), and the surviving signs are the ones already in t1.txt; the unread
   words inside the surviving text are blocked by signs with no attested value (U, W, q, k, overlined Z), as recorded
   on 5 Oct. No new value can be proved from this letter alone.

## Result

Unchanged: decoded, not read (0.069 plain, 0.172 explicit holes). No transcription or key change.

## Open

- The torn lines (right edge of p. 1, left margin of p. 2) - blocker: illegible (paper lost, no other copy).
- Unread words with unattested signs - blocker: no-key-material (the Nevers-Piles decipherments in BnF fr. 3612 are
  not digitised; a reading would need the volume, or Biermann's unpublished table).
