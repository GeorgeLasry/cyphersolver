# Re-reading log, ff. 87 and 89 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b33)

## Starting point

Reading audit (22 Oct): entry 0 (the recovered key applied to Tomokiyo's partial transcription,
`ff87-89_decryption.md`) *decoded, not read*: cipher letters run together and the clear text only in part. Entry 1
(Avenel's text) read, but only as an abridged excerpt with ellipses. Clean-sentence share before
(`_check_reading.py --file ff87-89_decryption.md`): 0.286. The Avenel excerpt: 0.775 (b17, fr).

## What was done

1. **Record and images.** DECODE R9461 (f. 87, one image) and R9462 (f. 89r-v, two images) fetched with the project
   cookie (`research/reading_audit/b33_fetch.py`; images only in the session scratchpad): colour scans of the
   originals, no attachment, no transcription, no comment on either record.
2. **Existing text?** Yes: Avenel, *Lettres de Richelieu* III (1858), nos. CXCIX (pp. 368-369) and CCV (pp. 381-383),
   found in Sept and used then only as an excerpt. Page images fetched from Google Books (id OIQItRIybmIC,
   `research/reading_audit/b26_gbooks_fetch.py`, PA367-PA386) and both letters transcribed in full, with Avenel's
   figures exactly as printed and his footnote decipherments (`ff87-89_avenel_figures.txt`).
3. **Figures checked.** Every printed run decoded with the recovered key (`research/reading_audit/b33_rl_decode.py`):
   all 39 runs give Avenel's footnote word for word, except two slips: f. 87 *menee r u bois* (Avenel prints `16`
   where *au* is wanted) and f. 89 *ambassada* (last figure 29 = a).
4. **Key change.** Figure 39 = *et*, not *a*: its two occurrences are *frontiere 39 menee* and *58 39 autres*, glossed
   by Avenel "frontière et menée" and "Chevreuse et". The 22 Oct key had 39 = a from Tomokiyo's transcription read as
   *amenée*. Adopted (holds at both occurrences); `final.py`, `key.md`, `SOLUTION.md` and the regenerated
   `ff87-89_decryption.md` carry it.
5. **Manuscript spot checks** (crops of the DECODE scans): f. 87r l. 5 reads `... 30 16 27 39 24 27 22 ~30 26 11 37 36 25
   40 26 21 22 ...` — no `16`: the clerk wrote *menee u bois* (the *a* of *au* left out); Avenel's `16` is a misprint.
   f. 89v: *et luy direz* [two struck words] *la proposition que j'ay faite a* (interlined) `51 30 18 52` [struck word]
   *de luy en ceste occasion* = *au roy et à la reyne mère*; Avenel printed only `51`. The second *Brassac* carries
   the doubling overline on the manuscript; the last word ends `29 20 29` (*ambassada*) on the manuscript as in print.
6. **Reading** (`ff87-89_reading.md`): Avenel's clear text, the ciphered words written as the figures spell them
   (*Vincienes*, *dis mil*, *pretres*, *letre*, *aus*), nomenclator figures named from Avenel's footnotes in `{...}`;
   one hole, [?au] (only the *u* is in the figures). English in `ff87-89_en.md`.

## Measures (reading body only, `research/reading_audit/b17_score.py`, LANG_=fr)

- plain: 0.826 (57/69 sentences clean, hole rate 0.048); the unclean sentences hold proper names (Vautier,
  Marcheuile, Andreni, Beauclerc, Ebeuf, Vantelet, Brassac), *letre*, and the numerals 1500/2000.
- HOLES=1: 0.971 (67/69). `_check_reading.py --file`: 0.713 (header and notes included).
- Look-alike alternates: none (printed figures; the three manuscript checks agree with print apart from the slips
  noted).
- Reader's judgement: every sentence holds and translates.

## Still open

Nothing in the cipher. Avenel's clear text was not collated word for word against the manuscript (his accents and
punctuation are kept); the three manuscript checks found him faithful except the two figure slips noted.

## Notes on the reading

- *la* {l'Angleterre} (f. 89): the figures write *la* before 84; Avenel's footnote reads it as "la reine d'Angleterre"
  (Henrietta Maria), to whom *elle*, *sa maitresse* and the bishop and priests *pres d'elle* also refer.
- *il (elle)*: Avenel's own gloss; the original writes *il* for the Queen Mother, who is coded as 52.
- The reading's header was shortened after a first draft so that `_check_reading.py richelieu` (whole file) gives
  0.734; the body figure is unchanged (0.826).
