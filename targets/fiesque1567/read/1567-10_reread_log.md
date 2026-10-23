# Re-reading log, 1567-10 (views 6 right - 8 right), 22 Oct 2026, Claude Opus 5.5, batch b02

## Starting point
Profile: "decoded, not read" (mechanical decodes decoded_v007l..v008r, unspaced; 0 of 11 sentences clean by
docs/_check_reading.py on decoded_v007l.txt).

## Existing text?
- No contemporary decipherment on views 6-8 (looked at view 6 at 1200 px and the contact sheets of views 7, 8: no
  margin or interlinear writing beside the cipher). Not in La Ferrière (contributor's prior check). None found.

## Image checks
- View 6 (full, 1200 px; header crop 2200 px): **the letter begins on view 6 right**, dated in the docket hand
  "11 octob. 1567, Vienne" (the contributor had "Oct 1567?"). Four lines of clear text ("Madame, ma derniere lettre a
  esté du [xxv?] du moys passé ... sur ses pieds") and then about 22 lines of cipher that are **not in the contributed
  transcription** (no v006r file). The contributed v007l starts in mid-sentence. Not transcribed here (about 800 signs;
  workable from the image, not attempted in this pass).

## How the reading was built
Line by line from the decode, using a sign-by-sign listing (research/reading_audit/reread_b02_signs.py) at breaks.
Confusions read through (all already flagged by the contributor or visible in the decode):
- `fu` (barred f / ꝑ, key u) stands for **l** in several words: "fu a desunyon" = la desunion (v007r c24), "fu //"
  = la, "fu // vd c 11 H# // b o fu" = l'ambassadeu[r] (v007r c18); elsewhere u. Probably two signs merged under one
  label; not corrected in the transcription.
- `fx` (t-shape, key c) is o in many words (n fx m 3n H# 1 v vbar -| o = cognoistre, v008l c01; "ection" in affection).
- `H#` = ss in "ambassadeur" (v007r c18, v008l c04, c07), = o elsewhere.
- `=20` (pour) appears inside words where it cannot be "pour": "remer[20]cicict" (remercioit), "sama[20]estc" (Sa
  Majesté), "ma[20]dict" (m'a dict). Probably a different sign read as 20; the words read without it.
- "ibre" twice = estre (v008l c03 "bien ibre" = bien estre; c20 "ibre esueu" = estre esleu?).
- `c` (key b) = r in "ciens" (riens, v008l c25).

## Holes left
v007l c01 (start, needs view 6 right); "[?faict]", "[?loue fort]" (c04 uoueyort), "[?conseiller]"; v007r c15 "soitctcri";
v007r c22 "deme"; v008l c19 "des filles de m[...]" (dem: possibly a code for the Emperor, not in the key); v008l c21
"uaneganasncrrte"; c22 "gechaocictua"; c24 "mnese?tcnte".

## Result
_check_reading.py on the reading: clean share 0.72 (42/58; hole rate 0.089) against 0.00 for the decode. Sentences
hold on views 7-8; the letter's first cipher page (view 6 right) is unread because it is untranscribed.
