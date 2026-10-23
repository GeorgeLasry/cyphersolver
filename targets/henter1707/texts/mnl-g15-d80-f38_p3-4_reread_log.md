# Re-reading log, R496 paragraphs 3-4 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b28)

## Starting point

Reading audit (22 Oct): the second `outcome.texts` entry (paragraphs 3-4: the delayed audience, the captive, the
closing) "decoded, not read": the normalized text in NOTES had these paragraphs as words between `[…]` holes ("the hand
overlaps the cipher signs; needs a Hungarian palaeographer"). `docs/_check_reading.py` on the whole decryption file:
0.188 clean (3/16).

## 1. Is there a text already? Yes — the interlinear on the leaf

- DECODE R496, R533, R534 re-fetched with the cookie (`research/reading_audit/b28_fetch.py`, DOC_ only): no DOC_
  attachment and no comment on any of them; R496 has its two images only (letter and address).
- The text is the contemporary interlinear decipherment written over each cipher line. It is legible at 2-3x on the
  DECODE image (`b28_strips.py`, `b28_crop.py`, crops in the scratchpad); the earlier "illegible" came from reading the
  page at its native size.
- Print: not in Láng's dissertation beyond the identification (C.Hen.01); no edition known.
- The key: no separate key needed — the alphabet is fixed by the interlinear of paragraphs 1-2 and of the closing
  formula (and agrees with the values noted from R533/R534). No Hentér key among the G15 key records harvested for
  bay1706 was needed or checked further.

## 2-3. Interlinear, figures, alignment

Every row of paragraphs 3-4 (and the end of paragraph 2, so the first sentence is whole) was read twice: the
interlinear as written, and the cipher under it sign by sign (`mnl-g15-d80-f38_p3-4_cipher.tsv`, 9 rows, 51 words).
Each word of the reading is carried by its figures; the interlinear agrees except at four places, where the figures
decide:

| interlinear | figures | |
|---|---|---|
| "de a Magyar" (20 Sept normalization) | **de a jancsar-sag** (ʒ π 8 3 χ π ↓) | the Janissaries |
| "twrbabo" (unread) | **turbatio** (w 0 ↓ ∞ π w n 20) | disturbance |
| "naltatnak" | **compo-nalodnak** (8 π б 20 4 8 π 5) | are settled |
| "zenenkedem" | **remenkedem** (↓ '' 9 '' 8 5 '' 4 '' 9) | I hope |

and "Felsegednek" in row 9 is **Felsegedet** in cipher (… 4 '' w). Latin "habeant patientiam, vocabuntur ad
praesentandas literas" is in cipher too. No supplied word; 4 words bracketed `[?]`.

Look-alike letters: **6** (p = б0 in "pedig", e = 1 in "pedig", the π-like i of "tiszteket", the Λ-like u of "uram",
the n-shaped a of "habeant", the doubled t-a of "valtoztatni").

## 4. Score and judgement

`b17_score.py` LANG_=hu on the reading body: **0.000 (0/6)** on the checker's modern Hungarian word list (no accents in
the cipher, 1700s spelling: kozot, akaruan, uiabban, szolgaia count as unknown); explicit holes only (HOLES=1):
**0.833 (5/6)**. Before: 0.188 for the whole decryption file, paragraphs 3-4 all holes. Reader's judgement: the six
sentences hold (the audience delayed by a Janissary disturbance, the wait while the officials are changed, the audience
solicited twice, "habeant patientiam", the hope for the captive's release, the closing). Set **read, grade A**
(contemporary decipherment checked against the figures word by word).

## Open

Nothing workable: the four `[?]` words are carried by look-alike signs (blocker: illegible at this resolution would
overstate it; they read in context and are kept marked). The unnamed captive ("szegeny rab uram") is not identified
here (not a reading gap).
