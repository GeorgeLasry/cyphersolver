# Re-reading log, R4841-R4843 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b16)

## Starting point

Reading audit (22 Oct): all three drafts "decoded, not read". The repository held only a summary of each draft and the
name-code table (texts/key.md); no draft had been transcribed, although the images showed clear English prose.

## What was done

1. **Is there a text already?** The DECODE records were fetched again with the project cookie
   (research/reading_audit/b16_wotton_fetch.py, pages saved in the session scratchpad only): each holds its four page
   images (TH_IMG_R484x_I281xx_P1-P4) and nothing else: no transcription, decryption, key or attachment, as on 21 Sept.
   No contemporary copy: the drafts are themselves the text (Wotton's own hand, endorsed "Copie / To Mr Secretarye").
   Printed calendar: CSP Scotland viii (1914) calendars these despatches (no. 106 for 1 Sep, per walsingham1585 NOTES).
   It could not be reached for alignment: the HathiTrust ssd view (miun.abe1726.0008.001) answers with a Cloudflare
   check (not bypassed), archive.org `calendarofstatep0008vari` refuses the text download (401, lending-only), and the
   other archive.org Boyd volumes (calendarstatepa02boydgoog etc.) are earlier volumes. A calendar is in any case a
   summary, not the text.
2. **Transcription.** The twelve full-resolution images (main checkout targets/wotton1585/decode/R484x_p1-p4.jpg,
   about 4800x6837) were read in horizontal bands and zooms at native resolution (b16_wotton_crop.py,
   b16_wotton_zoom.py; crops in the scratchpad only). texts/R484x_transcription.txt are diplomatic: line numbers by
   page, ~~struck~~ words, ^{interlined} words, [?doubtful], [..] illegible; Wotton's working notes at the head of
   f. 167r (R4841 p1.01-p1.08) and the endorsements included. R4841 p3 and R4843 p3 are short continuations (the
   postscript; the "Ticket"); p4 of each is the endorsement only.
3. **Reading.** Each draft read in its last state (struck words dropped, insertions taken in), spelling modernised,
   numbers written out, the name code glossed in place as {n = gloss} (texts/R484x_reading.md), and rendered in modern
   English with the same holes (R484x_en.md).
4. **Alignment** (b16_wotton_align.py: struck words removed from the transcription, loose spelling key, longest
   matching blocks, then a second pass for interlineations that sit out of line order):
   R4841 594 reading words/codes, 564 carried in order, 17 as interlineations, 13 not matched;
   R4842 749: 683 + 43, 23 not matched; R4843 663: 607 + 35, 21 not matched.
   Every unmatched word was checked by hand: all are modernised spellings of a word in the transcription (towarde,
   continew, hable, thees, ceaze, spetial, onse, trew, knowlege, me self, pswaded, ingement, bounde, themselfes,
   pretense, Cutberd, Steward, maine-tame, autoritie, viol:, an other ...) or the expansion of Arb: (Arbroath). Words
   no transcription word carries were bracketed: [the], [and], [should], [the King], [he find] (dropped), [enemies]
   (struck in the draft), [Men that], [I], [is], [They], [her], [to], [Endorsed:].
5. **Score** (python docs/_check_reading.py --file, header lines cut): R4841 0.981 (51/52 sentences), R4842 0.892
   (58/65), R4843 0.914 (53/58). Before: no text (0).

## Code numbers

- 3: glossed **the Queen of England** (was "France, probable"). R4841: Arran "wilbe hable ... to ruine them and
  diverte 10 from 3. or if that finding the K. constantly affection towarde 3 ... he wil not fail to convey him into Fr."
  France is the destination, so 3 is what the King is attached to. R4843: "if the viol: course be resolved on, it can no
  way stand with 3 honor that I should be at that time in this contrey" (Wotton asking for his recall). Sense only, but
  all four occurrences fit and France fits none of the R4843 one; **flagged for review** in texts/key.md.
- 9: "the 9 frendshippe" (R4842, the King "very desirous" of it): England, probable, sense only.
- 20: Maxwell confirmed by context: "a deer frende of Max[well]" struck and replaced by 20 (R4842 f. 174r), 20's
  quarrel with the Laird of Johnstone (R4843); CSP no. 106 has "Morton" (Maxwell's earldom).
- 32 is a refuge of **the King**, not Arran (R4843: "if 10 would ... seeke to convey himself into 32, he wil by force
  stay him"); key.md corrected. 36: "money out of 36" (R4843). 27: Hamilton favourer from whom Gray's plot is kept
  (R4843 ticket). 11: "the 11 course" (R4842). All four unidentified.
- "10. hou:" = the King's house; "the Mr" = the Master of Gray (R4841 postscript, R4842 "by the Mr meanes").

## Failures and open points

- CSP Scotland viii unreachable (above). Its glosses of 27, 32, 36 and 11, if any, are the next thing to check.
- R4842 p2.05-p2.09 (how to "embark" the Scots in Elizabeth's course) is rewritten three times in the draft; its last
  state is only partly legible ([..] in the reading). R4843 p2.10-p2.17 (the commissioners' meeting) likewise; the
  margin note "till suche a day ... being informed by the Secretary that his commissioners cannot be ready so soone" is
  read.
- Doubtful: "premoveable" / "stick" (R4841 p1.28), "Jamington" (R4842 f. 174r, the Laird whose brother wrote to the
  Prior of Blantyre), "drawing" read as [?drowning], "fase" read as [?late] breach, "it is wil" (R4843 p3.11).
- The initials "the L. B: the L. H: S. J. H. and S." (R4843 p1.09, Johnstone's allies) and "the Erle Mo:" are left
  as written.
