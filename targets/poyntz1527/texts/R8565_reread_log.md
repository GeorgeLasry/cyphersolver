# Re-reading log, R8565 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b31)

## Starting point

Reading audit (22 Oct): "decoded, not read". Nothing of the decipherment was in the repository, only three L&P
paraphrases in NOTES.md; the full images had never been seen (only 200-px thumbnails).

## 1. Is there a text already? Yes, on the page

- **DECODE record R8565**, fetched logged in on 23 Oct 2026 (`research/reading_audit/b31_fetch.py`): 8 images
  `IMG_R8565_I39496_P1..P8` (about 6650 x 9300 px) and one document, `DOC_8565_..._96769.png`, S. Tomokiyo's
  Lee-Worcester key table (alphabet, 10 word signs, 10 more word signs, 5 name signs). No transcription, no comment
  block. Every image opened (scratchpad `reread/R8565/`):
  - P1 (f. 174r, old 166): opens "the xv of Julie viij of clock in the morning, Mons. de Pratt and Mons. de Burlans
    from the Emperor ..." - the separated second part of L&P IV 3271 (confirms the 21 Sept identification; the check left
    open in NOTES is closed). One cipher word, l. 11, glossed *intimacion*.
  - P2 (f. 174v): cipher at the foot, two faint lines, decipherment in five darker lines over and between them.
  - P3 (f. 175r): cipher ll. 1-2 (no gloss; covered by P2's decipherment) and ll. 6-9 (interlined ll. 6-7, left margin
    for ll. 8-9).
  - P4, P5 (ff. 175v, 176r): clear throughout.
  - P6 (f. 176v): cipher band ll. 21-28, decipherment interlined.
  - P7 (f. 177r): cipher band ll. 13-17, decipherment interlined; signatures Hier. eps. Wigorn., Edouarde Lee, Fraunceys
    Poyntz.
  - P8 (f. 177v): address *To my lord legates grace*, endorsement *the [?] of July 1527*.
- **Print**: L&P IV ii no. 3271 (1872), OCR from archive.org `11001939bsb` (BSB scan; BHO returned a Cloudflare
  challenge). The calendar paraphrases the deciphered passages; used as a check only.

## 2. The decipherment against the signs

Crops at full resolution (`research/reading_audit/b31_crop.py`). For each band, the signs under the decipherment were
read with Tomokiyo's key and compared word by word: every checked word agrees (list in `R8565_reading.md`, Notes).
One disagreement of form: P3 l. 1 `4 ʒ - 6 6 v c` is *stikken*, the decipherer wrote *stikkyd*; the reading keeps the
decipherer's word. P7 `- 4` *is* where the decipherment's word is not clear: `[?is]`.

## 3. Key

No key change. Tomokiyo's table held for every sign checked. Sign `5` = *not* (P3 l. 9 *do not*, P6 *shal not*; not in
Tomokiyo's table; holds at both occurrences, flagged for review). `1` = *that*, `‡` = the King (of England), `H`/`A` = your
grace, `Φ` = *wol(de)*, `∴` = *shal*, as in the table.

## 4. Reading and scores

`R8565_reading.md`: the five cipher passages in the decipherer's spelling, with the f. 174r word in the Notes.

| | clean-sentence share |
|---|---|
| before | no reading body |
| b17 plain (`LANG_=en`) | 0.227 (5/22) |
| b17 `HOLES=1` (explicit holes only) | **0.909 (20/22)**, hole rate 0.034 |

The plain figure falls on 1527 spelling (wolde, highnes, thinges, frenchemen, therfor). Reader's judgement: the
sentences hold, and agree with L&P's paraphrase point by point. Word alignment: every unbracketed word is in the
decipherment as transcribed here; the one supplied word is `[and]` (passage 2). **Look-alike letters: 0** (the reading
follows the decipherer's hand).

## Open

- *[?bere]* (P2 l. 26) and the four words between *therfore* and *the doughter* (P6), written over each other in the
  decipherment: blocker **illegible** at DECODE's resolution (the signs under them are faint).
