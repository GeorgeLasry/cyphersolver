# Re-reading log, R9409 and R9427 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b20)

Kept here for both letters (R9427's log points to this file).

## Starting point

Reading audit (22 Oct): both "decoded, not read". Hand readings of 5 Oct 2026 (`r9409/reading.txt`, 87% of words given
a reading; `r9427/reading.txt`, 84%), after three image re-transcription passes and constrained fill rounds
(`sysA2/fill.py`), but holes and broken syntax in most sentences.

## 1. Existing text?

- Every file on DECODE R9409 (8 images) and R9427 (2 images) fetched with the shared cookie (b20_fetch.py; scratchpad
  only). No DOC_* texts or other attachments. DECODE "Partially decrypted" on R9427 refers to the interlinear gloss.
- R9427: the only contemporary text is the faint gloss over P1 ll. 1-5 and 7-10 (`r9427/gloss.txt`, transcribed 21
  Sept). Checked again on contrast-enhanced native crops: l. 1 gives "... sten her..." after "genedig" (adopted as
  [?isten] [?herren]); ll. 2-4 and 7-10 show only the scattered letters already in gloss.txt ("betreffendt", "in dem
  ercl..."); nothing more is legible.
- R9409: no gloss, no decipherment; the clear passages are already in the reading. No edition (web search 21 Sept,
  "KAA 4591"). The sibling letters in System A′ (R9408, R9410, R9413, R9407) are on the same footing (hand readings).

## 2. Partial readings in the brief's notation

`r9409/R9409_reading.md` and `r9427/R9427_reading.md`: the 5 Oct readings converted without changing a word
(research/reading_audit/b20_kaa_md.py: {?} -> [...], clear text in italics, code signs kept), plus the R9427
salutation from the gloss.

## 3. Score (b17_score.py, de; the word list cannot know Early New High German spelling)

| letter | full word list | explicit holes (HOLES=1) | 'da' after an article counted as a hole |
|---|---|---|---|
| R9409 | 0.323 (83/257) | 0.658 (169/257) | 0.634 |
| R9427 | 0.196 (10/51) | 0.451 (23/51) | |

## 4. Reader's judgement

- **R9427** is below the bar on both figures: P1.01-P1.21 (the Württemberg affair) is [...] in nearly every line;
  P1.22-P2.26 (the Bebek capture, the married provost, Stehan's letter) builds, with holes.
- **R9409** passes 0.60 on explicit holes, but the sentences do not hold where a reader needs them: P1 (salutation,
  the confederation, the exchange rates) and P3 (the voivode's practices, Késmárk) are broken syntax with [...] runs;
  and the reading writes "da" 53 times where no word forms ("ir da hab ein sunderlich freuntlich wolgefallen", "irer
  da freuntlichen gruess", "mit der da vertragen", "zwischen der da und seins frids"). That "da" is the value of the
  c+ sign (da/ch/f in this hand); standing alone after "ir/irer/der/die" it behaves like a title sign, probably
  "Mt." (Majestät, i.e. King John or the Roman king). **Not adopted**: the gender varies ("der da", "dem da"), there is
  no key sheet or gloss for it, and the reading gives no sign-level alignment to confirm that each "da" is the lone
  c+; flagged for review (sense only). With it the mining articles of P5-P7 read as running text; P1 and P3 would not.
- Neither letter is set read. A translation is not made (the brief asks for one only with a reading).

## 5. What was tried and failed

- Gloss over R9427 ll. 2-4, 7-10: illegible beyond gloss.txt.
- No new key value holds across every occurrence (the 3-5 Oct fill rounds had already exhausted the attested values).

## Open

- R9409: P1 and P3 runs, the lone c+ sign ("da", 53 places) - blocker: no-key-material (System A′ has no key sheet; the
  per-letter keys are re-learned from R9407 and do not settle these signs).
- R9427: P1.01-P1.21 holes - blocker: illegible (the only outside text, the gloss, is too faint); the remaining holes
  P2.01-P2.24 - blocker: no-key-material.
