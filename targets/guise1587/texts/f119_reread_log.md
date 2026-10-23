# Re-reading log, f. 119 (DECODE R4162) (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b27)

## Starting point

Reading audit (22 Oct): "decoded, not read". `f119_reading.txt` is a line-by-line reading without word division
across lines or punctuation, with [?] runs, nomenclator words given as their table value even where the sense
refuses it (LES ... LES ... QUE), and broken grammar in ll. 00-03, 11-13, 17-18, 25, 27, 30, 33-38. Scored as it
stands (joined, `[?]` as holes): 0.302 clean (13/43).

## 1. Is there a text already?

* DECODE R4162 fetched with the project cookie (`research/reading_audit/b25_fetch.py`, scratchpad): six images, the
  Gallica views 132 (the cipher page with the address leaf) and 133 (f. 120r: a clear letter of another writer,
  Montauban, May 158[1], not a copy), and four strips of the cipher; no DOC_ attachment, no comment. R4165 (f. 142)
  likewise: images only.
* Lasry's published material (cryptiana GL.htm): the key table and an f. 27 decipherment only. No print. The peer
  folder `targets/mercoeur1587/` (ff. 27, 30, 78, 151) holds no text of f. 119. The key is Lasry's; the BnF holds no
  other.

## 2-3. Re-read against the labels and candidate values

Each line's sign labels (`f119_glyphs.txt`) were printed with the candidate letters of every unpinned sign (the
`bl2.py` tables) and the reading rebuilt word by word, across line ends, with punctuation; line images `img/yNN.png`
(main checkout) checked at ll. 00-03, 22, 37, 38, 40. Gains, each carried by its signs:

* l. 03 "p C o x certainement" = ρ Є Δ X = C R O Y: "[je] croy certainement" (was "LES [?][?]o[?] certainement").
* l. 07 "[fbi] [ffm] l s" = LES + QUE + l s: "lesquels" (as before); "les leve pour nous".
* l. 13 "C C andr t e" = Flandre (C = l/r/f/s), after "la" ([f6]) at the end of l. 12: "[?Flandre]".
* l. 17 "[ffb] T s pourront" = QUI + l + s: "ce qu'ils pourront"; "dir j x" = "diray" (j = a, x = y).
* l. 18 "craig %" = "craigs"; "plus les traistres que les ennemis".
* l. 21 "espargne r i n" = "espargne ri[e]n"; "fault tous que n general" = "qu'en general".
* l. 25 "m ) m n % 6 doibt" ends "ne se doibt" (m n % 6 = n e s e): "il ne se peult [?ni] ne se doibt".
* l. 27 "nos a-U x s" = "nos a[m]ys"; "m n % eschauffe" = "ne s'eschauffe".
* l. 33-34 "d w ercoer" = "d[e] Mercoer" (w = M).
* l. 35 "comme l toutes" = "comme a toutes" (l = a).
* l. 36-37 "tel Y s / ubiects" = "tels subiects".

**The group `fbn`** is LES in Lasry's table and `key.md`, but reads as JE at ll. 00 (receu), 03 (croy), 04 (tiens),
17 (vous diray), 18 (craigs), 21 (n'y espargne), 36 (vous ay desia mandé), 37 (ne feras), 40 (vous baise): nine of
ten places, while LES is carried by `fbi` (ll. 07, 18, 24, 35). At l. 22 the same shape stands before "moyens"
("nous en cherchions [fbn] moyens"), where JE does not fit. So it does **not** hold at every occurrence: not
adopted, each such word shown `[?je]`, flagged for review (the shapes of l. 22 and l. 40 look the same on y22/y40).

No sign label changed (no corrections file). No key value changed. Look-alike readings that the new words rest on:
5 letters (l. 03 X as Y, l. 13 the two C-shapes as F and L, l. 17 x as Y, l. 33 w as M).

## 4. Score and judgement

`texts/f119_reading.md`, `b17_score.py`, LANG_=fr: **0.558 (24/43)**; explicit holes 0.698 (30/43). Before: 0.302.
Reader's judgement: the middle reads (the levies, Pfyffer, the heretics' army, "je craigs trop plus les traistres
que les ennemis", diligence, "c'est un grand malheur ... ferme fondement"), but the opening (ll. 00-03), the sentences
of ll. 29-33 and the closing request (ll. 36-39) do not build. Below the bar: kept **decoded, not read**, with this
partial reading.

## Open, and why

* The unread runs of ll. 00-03, 05, 12, 25, 29-30, 33-34, 37-38: signs read in three or more earlier passes and here;
  the remaining choices are between homophones the context does not fix, and between nomenclator readings (`ffm`
  QUE/POUR, `ffmm`) that do not fit as tabulated. No further key material (Lasry's table is the only key; no
  decipherment of this letter exists). Blocker: no-key-material.
* `fbn` = JE: a sense-only value, for George Lasry's review.
* Name codes [21] [43] [71] [9b] [N] [&]: Lasry's "Unknown" row; no key material.

One sentence: "[?Je] vous diray que [?je] craigs trop plus les traistres que les ennemis" (I will tell you that I
fear the traitors much more than the enemies).
