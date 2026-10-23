# R7484 and R7485 reread log (23 Oct 2026, batch r2k)

## Why

The pass-3 reading of R7484 and the pass-2 reading of R7485 (9 Oct 2026) were headed "modernised Polish" ("ponieważ",
"jeszcze", "mówią", "Jedykuły", "rezolucyą") and marked doubtful words "(?)", which the explicit-hole score does not
count. The reading rules forbid modern spelling in a reading. R7476 was restored the same day (r2b,
`R7476_reread_log.md`); this pass does the same for the other two letters.

## Method

R7484.txt and R7485.txt give, line by line, the numbers (C) and the interlinear gloss (G) but no key line, so the
r2b stream script (which reads R7476.txt's K lines) was not reused; each line was re-spelt by hand from its C/G lines,
the syllabary (`syllabary.tsv`) and the slips settled in `R7484_pass2.txt` / `R7485_pass2.txt` (passes 2-3), and the
result aligned word by word with the token stream.

Rules applied:

1. Clear words exactly as transcribed ("Pisałem do WMM Pana w ostatnim", "Mając bowiem", "być mogło", "chciał",
   "dziano z kąd", "dla czego", "gdyż", "WMM Panu iednak", "JMC"; R7485 "Juz tedy z łaski Bozey", "perswadował, y
   namawiał", "że", "Hospodar JMC wierny"; R7485's clear body as transcribed in R7485.txt).
2. Each code by its value. The glosser sometimes normalised the writer's o for a nasal vowel; the figure's value is
   kept, as R7476 writes "bawio", "chco", "z tod", "kazdo": 179 o glossed "ą" -> "mowio", "widzoc"; 52 do glossed
   "dą" -> "bedoc", "[po]ydo"; 275 to glossed "tą" -> "dotod"; 332 zo glossed "zę" -> "poczoł"; 30 co glossed "ą" ->
   "chcoc". 330 = "ze" (glossed "że"; R7476 also "ze"). 174 no glossed "n" -> "stanowszy"; 141 li glossed "ły" ->
   "Iedikuli". Exception kept from the gloss: R7485 36 "cą" in "chcą" (36 is ce 2x, cą 1x: no settled value).
3. Encipherer's slips are emended in brackets: R7484 "na na[s]" (204 for 244), "po[te]ntie" (178 for te),
   "[po]ydo" (297 for 197), "Apr[i]lis" (a-p-r-li-s), "namowi[o]ny" (101 glossed o), "August[a]", "Cesarz[a]" (word
   codes with no ending), "F[e]rmana" (gloss "Frmana"); R7485 "Han[o]wi" (191 for 181), "wo[ła]ia" (120 for 139),
   "pi[e]r[w]sza" (figures pi-r-s-za). Surplus figures left out: R7484 326 z doubled in "Szwedzkiego"; R7485 59 e
   after "ale".
4. The pass-3 "(?)" words became [?word]: "[?umowia]" (100 glossed iu/ia), "[?Iezdził]" (clear word read
   "Sędzio"/"Iezdzi[ł]"), "modlit[?wa]" (gloss over 244 unread), "[?dowiedzie]" (clear closing). The 9 Oct guesses
   "[zwokowani(?)]" and "stambulscy" -> "Stambułsci [...]" (34 297 119 294 173 "c wo ko wa ni" unread). Code 112 is
   "[112]". R7485 "[bo]" is a clear word in the glosser's ink, so bracketed; "[Han]" (supplied subject in pass 2) is
   dropped from the reading (it stands only in the gloss over 284 u) and given in the English.
5. Latin as written: "non uanus", "meto potentie Germanice" (the figures give meto, not metu), "Stanisława".

Lines checked one by one against R7484.txt and R7485.txt; R7484 has 18 of 513 cipher tokens unread (as on 9 Oct),
R7485 none of 96. Look-alike alternates: the emended letters (slips above) are 9 letters in R7484 (~1,050 letters)
and 5 in R7485 (~220 cipher letters), under 1% and about 2%; R7485's cipher passage is also confirmed by the
contemporary clear decipherment at the head of the page.

No images were opened in this pass: the DECODE crops of 9 Oct are not on disk in either checkout; the restoration
works from the transcription, whose G lines were already checked on 2-3.5x crops in passes 2-3.

## Score

`python research/reading_audit/v2_score.py <file> pl` (reading body after `## Reading`):

| | plain | explicit holes | hole rate |
|---|---|---|---|
| R7484, 9 Oct modern spelling (whole file, "(?)" not counted) | 0.056 | 0.750 (27/36) | 0.096 |
| R7484, 23 Oct writer's spelling, doubtful and supplied marked | 0.087 | 0.739 (17/23) | 0.094 |
| R7485, 9 Oct modern spelling (whole file) | 0.111 | 0.889 (16/18) | 0.079 |
| R7485, 23 Oct writer's spelling | 0.125 | 0.750 (6/8) | 0.099 |

Plain is meaningless (modern Polish word list against 1713 spelling). Both stay above the 0.60 explicit-hole bar and
their sentences hold: **R7484 and R7485 keep read**. English: `R7484_en.md`, `R7485_en.md` (modern spelling only
there).

## Still open

- R7484 p.111 L3-4 "umowi-iu/ia t r ze y s za" (7 tokens), p.111 L10 "ta" + "s fi d no" (5), p.113 L6 "c wo ko wa ni"
  (5): values certain (gloss and code agree, checked at 2-3.5x on 9 Oct), no Polish, Latin or Ottoman word found for
  them; no sibling, print or other gloss gives them. Blocker recorded as no-key-material (no outside text for these
  words).
- R7484 code 112 (1 token): gloss a flourish at 3.5x, its R7476 occurrence also illegibly glossed: illegible.
- R7485 clear body (pale ink, pp. 115-117): very faint with show-through on the DECODE images; read only in part on
  9 Oct: illegible on the available images.
