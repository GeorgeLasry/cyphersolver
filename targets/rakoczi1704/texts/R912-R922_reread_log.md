# Re-reading log, R912 and R922 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b22)

## Starting point

Reading audit (22 Oct): both decoded, not read. `R912_image_read.txt` and `R922_image_read.txt` are the corrected R639
table run over the 21 Sept image transcriptions (`tr/`), printed group by group: syllables, table words used for their
sound ('Cond', 'Comme', 'sou', 'donc', 'present', 'cher') and stray capitals, with no word division. `_check_reading.py`
on them: R922 0.143 (4/28), R912 0.25 (22/88).

## 1. Is there a text already?

All files on DECODE R912, R922 and the key R639 fetched with the project cookie (`b17_fetch.py`, scratchpad): one
transcription each, the page images (3 + 2) and the key image. No other attachment, no comment block (only the MNL
copyright notice). Contemporary text: the interlinear on R912 p. 1 (all but three lines), R912 p. 2 ll. 1-4 and p. 3
ll. 1-2, R922 ll. 1-2, as recorded in NOTES (30 Sept). The R922 image shows a clear letter under the cipher sheet (p. 350
of the fascicle, rotated: '... Altesse ... de Suede ... Seig.r'), not imaged on its own and not on DECODE; whether it is
a clear copy of R912 or R922 cannot be told from the edge visible (blocker: needs-physical-access or an MNL image of
pp. 348-350). No printed edition found in the notes; not searched further here.

## 2. Reading

- R912 p. 1: the interlinear read on the image in eight half-width strips at native resolution
  (`texts/R912_interlinear_p1.txt`), checked group by group against `tr/R912_p1.txt` decoded with R639
  (`research/reading_audit/b22_rk_lines.py`). Seven figure corrections seen on the image (texts/R912-R922_corrections.tsv:
  416 -> 426, 473 -> 493 les Polonois, 147 -> 197 twice, 501 -> 301, 534 -> 504, 51 -> 81, 515 -> 315).
- R912 pp. 2-3 and R922: word division and normalisation by hand from the groups, with the table words read for their
  sound (161 con, 160 com, 395 son, 188 dont, 343 pre, 170 che, 129 av, 127 ar, 252 inte, 400 ti). Doubtful places
  checked on the image for R922 ll. 3, 17-18: the figures are as transcribed (244, 208), so 'marquer' and 'estre' rest
  on look-alike alternates.
- No key change adopted: the sound uses of the table words are the table's own syllables, not new values; 9 and 574 (R922)
  and 89, 93, 607, 609 (R912) stay unread.

## 3. Look-alike letters

R922: 18 letters of about 1,300 (marque 244 -> 294, affaire 128 -> 123, estre 208 -> 207). R912: 13 letters (luy 264 ->
267, lettre 264 -> 265, ay 533 -> 133, di 276 -> 176), not re-read on the image; the seven image corrections above are
not counted as look-alikes.

## Result

| doc | before (image read) | after (`b17_score.py`, body) | explicit holes only | judgement |
|---|---|---|---|---|
| R922 | 0.143 (4/28) | 0.839 (26/31) | 0.968 | read, grade B: every sentence builds; holes at 9, 873, 'Ma D T hi', 574 |
| R912 | 0.25 (22/88) | 0.783 (54/69) | 0.899 | read, grade B: p. 1 and the end of p. 3 build fully; p. 2 ll. 3-7, 14-22, 26-31 and p. 3 ll. 2-3 keep runs of holes |

Open (R912): the p. 2 runs where the groups as transcribed give no French (not re-read on the image; blocker
not-attempted for a second pass), the closing figures of p. 3 (a date and name in figures), 'Slupce'.

Example (R912): 'Aussy publie-t-on comme une chose presque certaine qu'il n'entrera en Moschovie que la campagne qui
vient.' — So it is given out as an almost certain thing that he will not enter Muscovy until the coming campaign.
