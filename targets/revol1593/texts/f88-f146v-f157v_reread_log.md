# Re-reading log, revol1593 ff. 88r-v, 146v, 157v (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b15)

## Starting point
Reading audit (22 Oct): all three decoded, not read. Token decoder output under key no. 60 with a few anchors
(f. 88r "de absolution", "le Roy", "qu'il"; f. 146v Tomokiyo's "l'absolution", "a la verite", "interest").

## 1. Is there a text already?
- These are not DECODE records: the copies are BnF fr. 3985/3986 on Gallica (microfilm canvases), and Tomokiyo's
  cryptiana page (henryiv2.htm) lists the letters and quotes the three f. 146v words only.
- No interlinear decipherment on ff. 88, 146v, 157v (checked again on canvas 287 of fr. 3986 at full resolution,
  4949 x 6957, openapi.bnf.fr IIIF v3: no glosses over the cipher).
- Print: Memoires de Nevers part 2 (Gallica bpt6k64451005), the four pages where Gallica's earlier ContentSearch hit
  "Reuol" (pp. 324, 425, 453, 513 = views 373, 474, 502, 562) were fetched through openapi IIIF and read: a Henri IV
  letter of 1597, Nevers's memorials to Clement VIII, and his discourse on the League. None prints a Nevers-Revol
  letter of August-October 1593. Gallica's ContentSearch is now behind a Cloudflare block (HTTP 403 page), so the
  volume could not be searched further; archive.org has no copy. The Instruction of 31 Aug is the only cipher text of
  the set in print (already used as a crib).
- Result: no text of these three passages exists outside the cipher.

## 2. Reading on the image (f. 146v, the best-preserved page)
- Canvas 287 fetched at full resolution; the cipher block (three full lines and the line-ends around them, about
  200 signs) cut in four column strips at native resolution.
- Line 2 re-read: `+ g ? λ 14 ꝑ 4 20 xx ‡ π ⊥ | n p ı∂ .:. ı. y xx m 8 s 9 ıı o q n ‡‡ + p Δ T y ✱ θ7 ro ur Q+ p V η`.
  With key no. 60: "nostre ... de l'absolution et que ... Je ... fait me ... Mr de Mercure ...". The anchors hold;
  between them each copyist form maps to two or three table entries (ꝑ = so or p; 4 = l or x; xx = t or doubled x;
  the "‡‡" compounds are not on the sheet), and no assignment gives a French clause.
- Line 3: "... nous [?au]rions et a la verite si ..." around `|- ⱶⱶ 3 π ⊥ r n ∂ λ y 3 q`; the run before it
  (`ꝑ ro ⊥ = ꝑ æ g+ ∞ y V u+ ꝑ ıı ⊥ h L++ g ꝑ f++ ...`) does not read under any of the alternatives tried.
- Not a reading: fewer than one sentence in five would carry words between the anchors.

## 3. ff. 88r-v and 157v
- f. 88r-v: only the contributor's transcription (issue #32) and the bitonal microfilm canvases 176-177; his
  variants at about one sign in six; the decode with every variant combination (shuffle_control.py) gives the
  three words already known and nothing between them.
- f. 157v: faded; clear cursive and cipher run together (NOTES, 17 Sept); the cipher extent is not yet segmented.

## Outcome
All three stay **decoded, not read**. What is missing is a sign-by-sign table of the copyist's forms (the glyph atlas
`atlas60.md`, to be finished from the interlined Instruction, fr. 3985 c. 264-268, where the same copyist's signs
stand under the office's decipherment): with it each ambiguous form gets one value and the pages can be re-transcribed.
That is work not yet done (not-attempted), not an outside blocker, for ff. 88 and 146v; f. 157v is also faded.

## Failures
- Gallica ContentSearch (Cloudflare block) and the full OCR of Memoires de Nevers part 2 could not be reached this
  session; four pages read by image only.
