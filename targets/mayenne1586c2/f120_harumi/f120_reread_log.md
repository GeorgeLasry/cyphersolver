# Re-reading log, fr. 15573 f. 120r-v (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b21)

## Starting point

Reading audit (22 Oct): decoded, not read. Harumi-Matsuba's punctuated reading (`READING.en.md`) has holes in most
sentences of r c01-c05, c15-c19, c28-c31 and v c03-c05. Checker on the reading body: 0.50 (16/32).

## 1. Is there a text already?

No. Not a DECODE record. Gallica btv1b90618780 views 244-249 looked at: f. 119r-v is a clear memorandum ("Ce que le
S.r des R... a dict a la Royne ...", on Navarre, Biron and Champigny), not a decipherment of f. 120; f. 120v has the 8
cipher lines; f. 121r is blank and f. 121v (view 249) carries the address "Pour Monseigneur de Villeroy" with a docket
ending "1586": the cover of this letter (the second leaf of its sheet), so the recipient is very probably Villeroy, as
Harumi-Matsuba guessed. No interlinear decipherment: the few superscripts on f. 120r (r c07, c10 '8δ', c11 and
c13 'ar', c12 'Hr', c19 '+q+') are written in cipher signs (insertions by the writer), not glosses. Tomokiyo lists the
letter as undeciphered; no print known.

## 2. On the image

f. 120r fetched at full resolution (openapi.bnf.fr IIIF, view 246, 4959 x 6438) and cut into line strips
(scratchpad). Checked: r c01 (the opening signs thb + 7 I Sbar, as transcribed; still no value), r c11 (the 'ar'
superscript is two cipher signs), r c30 (B : hs alpha = 'sort', as transcribed), r c31: the sign the transcription
calls curlo before 'inances' has the same shape as the delta (e) later in the line, so 'finances' rests on a
look-alike alternate, written [?finances]. The other holed lines were not re-read sign by sign.

## 3. Word check and the reading

`research/reading_audit/b21_may_check.py` aligns the reading's letters with the decode letters: 302 of 326 plain words
fully carried; the others differ only by the choice between the two values of a two-valued sign, or by letters the
reading had added, which are now bracketed. The reading had normalised the cipher's spelling (ennuyé, souffre, effects,
sommes, pouvoir ...): restored to the figures' spelling (brief, step 4). Result `f120_reading.md`.

| | checker (fr word list) | explicit holes only (b17_score.py HOLES=1) |
|---|---|---|
| contributed READING.en.md body | 0.50 (16/32) | 0.625 (20/32) |
| f120_reading.md (b21) | 0.50 (17/34) | 0.647 (22/34) |

The checker does not know the cipher's single-consonant spellings (somes, efects, afaires, enemis, trouera). On the
explicit holes the reading passes 0.60, but by a reader's judgement the sentences do not hold in r c15-c19 (what
"[?E]" is resolved to, "s[?] puis [?…] faire"), r c24-c31 (the deputies, "n[?] [?15] [?…] tombé", "[?]spe[?…]ment")
and v c03-c05: the content of the letter is in those stretches. **Kept decoded, not read.** Letters on a look-alike
alternate: 1 (the f of [?finances]).

## Open, and why

- Code signs with no value in the key (thb, 7, Sbar, 30, Esign, Om, 15, .u., 4d, oo, Dsign, invTl; 15 places): no
  value in Tomokiyo's table nor in the six letters deciphered at the time (no-key-material).
- The holed lines r c15-c19, c24-c31, v c03-c05 have not been re-read sign by sign on the image (not-attempted): the
  next step, with Burford's sign sheet.
