# Re-reading log, R4938 and R4939 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch r2h)

## Starting point

Both records not attempted: images in hand (main checkout `transylvania1645/`, 1,704 x 2,272 px, the DECODE files;
`image-manifest.json`), never transcribed. DECODE: R4938 4 images, R4939 3 images, no documents, no comments, no
associated records (metadata files of 23 Sept). Print: Lukinich 1907/1908, Szilágyi 1885 (Linz) and *Erdély és az
északkeleti háború* I (MEK 06508, local text from b15) grepped; the latter prints the reports of Bethlen and
Klobusiczky from the 1648 Polish election diet (11, 13, 15, 21 Oct 1648) but not this letter or a decipherment of it.

## R4939 (1648)

1. **What it is.** Two pages of cipher in Latin minuscules, a clear salutation line, a clear dating and signature
   ("... Albae [?9] ... 1648", "Geor. Rakoczy" and a second signature) and on image P3 the clear address: "Magnificis
   Francisco Betthlen de Keresd ... ac Andreae Klobusiczki ... ad moderna comitia Reipub. Poloniae legatis". A pencil
   gloss over the first cipher line ("kivantuk volna ..."): a later reader's start, used only as a check.
2. **Transcription** (`R4939-transcription.txt`, 46 lines, 1,500 letters): read from 2x crops of P1/P2.
3. **Family key** (`shared-key-hypothesis.json`) tried: gives no Hungarian (different alphabet; the hand is not the
   family hand). Ruled out.
4. **Ciphertext-only break.** `research/reading_audit/r2h_r4939_anneal.py` (injective substitution, word divisions,
   hu-modern 5-gram, 10 restarts) gave running Hungarian on the first page at restart 1: "kivantuk volna ...
   oervendetezeb hirt irhattunc volna kegyelmeteknnk az mi kegyelmez urunznac ...". Key `R4939_key.md`. The pencil gloss
   agrees ("kivantuk volna").
5. **Label corrections.** The remaining breaks were the hand's look-alikes misread in the first pass: q/g (n/e), r/t/long
   s/x. On 3x crops (lines 2, 16, 18, 20) the g's closed loop, the t's cross and the x's long stroke are visible; 51
   labels corrected where the word needs them (`R4939_corrections.tsv`).
6. **Reading** (`R4939_reading.md`, English `R4939_en.md`), aligned word by word with the decode of the corrected
   labels: 16 letters of 1,449 (1.1%) still rest on the other member of a look-alike pair by sense (a/e 8: "nagysaga" x3,
   "ugy" x2, "megh", "igyekez", "feiedelemseget"; r/t 2 "esseben"; c/e 2 "foglalna", "alap"; x/t + g/q 2 "istentul";
   g/q 1 "oltalmazzon"; 1 more) - under the 3% limit. Words not carried are bracketed: lines 03-09 keep several unread
   groups.
7. **Score** (`v2_score.py`, hu): explicit holes **0.75 (18/24)**, plain 0.0 (the modern word list does not know the
   period spelling: oe, cz, -unc). Reader's judgement: from line 10 to the end the sentences hold - the father (György I
   Rákóczi) is dying; he did not want the Polish crown for himself; the sons will not risk the country by seeking the
   principality for Zsigmond now; the envoys are bound to promote Zsigmond's candidacy, money to be spent on it; letters
   will follow at the father's death. Read, grade B.

## R4938 (1647)

1. **What it is.** A clear Hungarian letter dated "24 Ap. Ao 1647", signed G. Rákóczy, with three short cipher spans on
   image P2 (45 letters) in the family hand, glossed in pencil by a later reader.
2. **Transcription** (`R4938-transcription.txt`) and decode with the family key unchanged: "az lakocvsig mon", "az nekunk
   ailunkker uolna", "mineuvnkne fologion": the family's h/k look-alike gives r for k in "Rakoc-", "forogion"; "az
   Rakoczi Sigmon", "az nekunk [...] volna", "mi [?nevunkre] forogion" (`R4938_reading.md`). One word ("ailunkker") unread.
3. Not counted as a reading: three phrase fragments, no sentence of their own (the clear letter around them is not
   transcribed here); 45 letters, the unread word occurs once - blocker too-short.

## R4936's g/q look-alikes

Nothing here settles them. R4938 is in the family hand but its spans contain no t (q) and its g's are all u/v; R4939 is
a different hand whose g and q do separate on scans of the same 1,704-px width, which shows the limit is the R4936 hand,
not the photography alone. The R4936 blocker stays: a sharper image of Keresdi_Bethlen_14 or a printed text.
