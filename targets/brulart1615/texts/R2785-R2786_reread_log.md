# Re-reading log, R2785 and R2786 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b17)

## Starting point

Reading audit (22 Oct): both letters "decoded, not read": nothing of either text was in the repository; Tomokiyo's key
image (DOC_2785/DOC_2786, one file) and his DECODE notes only. One page image of each had been fetched earlier.

## 1. Is there a text already?

- **DECODE records** fetched with the project cookie (`research/reading_audit/b17_fetch.py`) into the session
  scratchpad: R2785 4 page images (I17343_P = f. 83r, I17344_P1 = f. 83v, P2 = f. 84v address, P3 = f. 84r) and the key
  png; R2786 4 page images (P1 = address leaf, P2 = f. 109r, P4 = f. 109v, P3 = f. 110r) and the same key png. No
  transcription, plaintext or other attachment on either record; the record text gives Tomokiyo's note only ("Some
  passages are not deciphered ... They may be partially or totally nulls").
- **Contemporary decipherment**: both letters carry an interlinear decipherment over their cipher runs, in a second
  hand. R2785: over every run but the three spaced-sign lines at the foot of f. 83v / head of f. 84r. R2786: over most
  runs of ff. 109r-110r; rows 6 and 9-11 of the f. 109v block have none or only scattered words.
- **Print / cryptiana**: louisxiii.htm gives the key, not the letters (already checked 21 Sept). No edition of these
  letters known; not searched further.

## 2. Transcription and alignment

The clear text and the interlinear decipherment were transcribed from the page images (strips at native resolution,
`research/reading_audit/b17_crop.py`). Each cipher run was aligned with its decipherment and checked against
Tomokiyo's key (`texts/R2785_align.tsv`, `R2786_align.tsv`, written by `research/reading_audit/b17_brulart_align.py`).
The key's numbers carry the run in every case checked: 20 de, 20̄ se, 5̄ pre, 7̄ que, 8̄ qui, 18 con, 30̄ tion, 35 en,
36 ent, 74 me, 75 ment, 81 mon, 84 ne, 91 ou, 93 ont, 97 pour, 10 bien, 21 dict, 22 droict, 22̄ son, 41̄ uent, 3 avoir,
54 guerre, 60 homme, 71 jusques, 72 il; ö duc de Savoye, q̈ duc de Mantoue; letters B/ƃ = a, x = d, ε = f, q = r, w = p,
ʃʃ/T = t, π = x, tt/tto = s.

Findings:
- θ is a null (R2786 f. 109v row 10-11 "ff ʃʃ θ" = "et"; it stands between words elsewhere); φ is Tomokiyo's delete sign.
  No key change: θ is not in his table, and the null reading holds in every place it occurs here.
- R2786 f. 109v row 8: the decipherer wrote "incommoditez", the figures give i-n-con-v-e-n-i-ent-s; the reading follows
  the figures ("inconvenients").
- R2786 f. 109v row 11 had no decipherment: decoded with the key as "en mesme temps" (35 74 s 74 29̄ m p s).
- R2785 f. 83r: the decipherer's "de" sits over a figure read 10 (bien); 20 (de) expected; the decipherment followed.
- The date of R2785 is 16 Sept 1615 ("le xvi jour de Septembre"), not 15 Sept.

## 3. Failures and open pieces

- R2785: the three spaced-sign lines (f. 83v rows 17-18, f. 84r row 2; about 60 signs) have no decipherment and give no
  French under the key, with or without θ and φ; Tomokiyo took such passages for nulls. Left [...]: no-key-material.
- R2785 f. 83v: three runs where the decipherer's cramped words could not be read with confidence ("m'est possible",
  "[?lors] de [?propos]", "l'Equidray", and the gloss after "ont este"); the figures under them were not decoded sign by
  sign (the letter signs of those runs are partly ambiguous in Tomokiyo's table: the circled ʜ is l or y). The clear name
  "[?Manjeaux]" not identified.
- R2786 f. 109v rows 9-11 and 110r row 1: only the words the decipherer glossed or the numbers carry (l'intention,
  aulcunement, me, bien differend, en son endroict); the rest gives no French under the key (θ, φ, ꝁ, ξ). The
  figures 16 (car), 21 (dict) on row 8 do not fit; left as numbers.

## Result

| record | before (audit) | after: clean-sentence share of the reading body | rests on |
|---|---|---|---|
| R2785 | no text, decoded, not read | 0.854 (35/41) | clear text + contemporary interlinear decipherment, checked with Tomokiyo's key |
| R2786 | no text, decoded, not read | 0.863 (44/51) | the same; two runs decoded with the key where no gloss exists |

Both set `read` (grade B: the decipherer's hand is small and some glosses are read with doubt).
