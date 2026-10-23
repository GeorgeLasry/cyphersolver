# View 6 right (f. 2r), first cipher page of the 11 Oct 1567 letter: round-2 log, 23 Oct 2026, Claude Opus 5.5

Before: not in the contributed transcription; the letter's reading started mid-sentence at view 7 left. Gap blocker
"not-attempted".

## Existing text?
- No decipherment beside the cipher (view 6 at 1600 px; views 5, 9, 21, 24 at 800 px: view 5 is the volume's title
  leaf, view 9 a docket, nothing interlined or in the margins). Not in La Ferrière (contributor's prior check).

## Image
- openapi.bnf.fr IIIF, ark:/12148/btv1b90573568/f6 (7593 x 5591). Lines found by ink profile in x 4700-7600; 23 cipher
  lines (y 1540-4666), each cut at native resolution in two halves (x 4700-6200, 6100-7600) and viewed upscaled
  1.3-2.5x (research/reading_audit/r2_fiesque_zoom.py). Images in the scratchpad only.
- Four clear lines first: "Madame, ma derniere lettre a esté du [xxvi?] du moys passé, et depuis n'ay peu parler a
  l'Empereur que mercredy dernier, car il ne bouge de sa chambre et ne se peult soustenir sur ses pieds."

## Transcription and decode
- read/r2/transcription_v006r.txt: 816 signs, labels as in contributed/data/key.tsv; name!x marks a sign read as x rather
  than its key value. Decode with research/reading_audit/r2_fiesque_dec.py (Dz=con): 940 letters, 31 on look-alike
  alternates (3.3%), 12 signs unexplained.
- How this hand writes (checked against the contributed transcription of view 7 left, same hand, where "le mal si
  avant que de sa part il ne" was aligned sign by sign): the crossed-descender p is the contributor's "fu" and reads l
  (and u); the barred double cross reads u/v (fu) or o (++) by word; the h-shape is 3n (n); the d with a loop is vbar (t)
  or D (d); "ic" is the code 10 (et); "zo" is the code 20 (pour); the u-shape reads e (Tomokiyo's a!, linked to u in his
  table); # reads ss in "meissent", "necessaire", "obeyssant" and ff in "affin".
- **Dz (ꝺʒ) = con.** The contributor's unvalued sign reads "con" in four words on this page: [con]gé (c01),
  [con]mandements (c14), [con]dition (c20), and a struck [con] (c21). The same value reads "[con]clusion" and
  "[con]ditions" in 10 Sep 1569 (v150l c19-c20), "[con]tanter" (v150l c15), "[con]servation" (v150r c07), "[con]me"
  (6 Mar 1568 f. 39r c21) and "[con]soler" (17 Jul 1568 f. 79v c07): a syllable code, not in Tomokiyo's table. Once
  (c13 "encores que [Dz] son royaulme") it does not fit and stays a hole.
- The small "1" sign reads r in several words of this page (crestienté x3, entendroict, seroict); counted as alternates.

## Reading (read/1567-10_reading.md, [v006r] paragraph; English in read/1567-10_en.md)
"Je luy dicts que, quant je prins congé de vous pour m'en venir par deça, vous me [?commandastes] d'entendre s'il
estoict vray ce que luy vous avoict dict: que, se plaignant Sa Majesté des desordres qui sont a la crestienté a cause de
la relligion, ... il me dict qu'il estoict vray que, y voiant tant de desordres, il ne pouvoict moins faire que de se
plaindre [?amerement] de la condition du temps, et qu'il n'attribuoict ce [?malleur] qu'a la desunyon des princes
crestiens, qui sont plus enclins a leur particullier qu'au bien publict," and view 7 left goes on "et aveugles a leur
interest, ont [?faict] cognoistre le mal si avant ..." (v007l c01 re-read on the image: "ic // ‡ a ꝑ̃ m ꝑ a v // ꝑ u ꝑ ⊣
8 h ʊ a ⊣ o v ꝭs" = et aveugles a leur interest; this closes the v007l c01 hole).

## Holes left on this page
- c05-c06 "que […] bien qu'il estoict necessaire" (two words, "ꝑ⊣a ıꝑ#ʒ+1tʊ": not resolved on the image).
- [?commandastes] (an s not written), [?ne s'espargneroict] and [?espargnerez] (several look-alikes each), [?mettriez]
  (one unexplained sign), [?feroy] (one extra sign), [?amerement] (written "amremant"), [?malleur] (y-shape for u), [Dz]
  in c13.

## Scores
- _check_reading.py on the v006r paragraph alone: 0.33 (6/18 chunks); holes only (b17 HOLES rule): 0.94; with this
  target's own period spellings added to the word list (r2_fiesque_holes.py --extra): 0.61. The failures are spellings
  the word list does not know (estoict, crestiens, unyon, soict, meissent, prandre), not holes.
- Whole letter (read/1567-10_reading.md, body only): 0.61 plain, 0.92 holes only, 0.70 with target spellings
  (0.67 plain before, on the shorter text).
- Look-alike alternates on this page: 3.3% of letters (31/940), at the brief's 3% limit; no contemporary text confirms
  them. The letter stays read, grade B, on the strength of views 7-8 and the sense of view 6; the view 6 page itself is
  a single unchecked AI transcription.
