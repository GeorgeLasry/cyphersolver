# Re-reading log, R48 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R48_decryption.txt` (character-model segmentation of DECODE's
transcription D1713, KaJo, Jan 2016, under Meister no. 40) scored 0.64: the general sense of both sheets was visible,
with long garbles ("beati tisico mesi", "si gatis guisa", "iormania ciatori").

## 1. Is there a text already?

- DECODE images: 8 cipher pages (399r–402v) and 5 "cleartext" images (despatches in clear, not a decipherment). The
  transcriber noted that the images may hold two ciphers, the second from 401r: they do (399r–400v and 401r–402v, each
  beginning and ending in mid-sentence).
- Tempesti, *Vita di Sisto V* (1754) II, book IX (scratch OCR ll. 4907–4943) paraphrases the audience of 401r–401v
  closely (Morosini goes to the King's chamber unannounced while the King is dressing; "ricordarsi del grave delitto
  commesso nella persona del Cardinal di Guisa"; the King's answer, "non si suol perdonare né anco a' figliuoli",
  Mayenne approaching, "tenerle tutte unite", the Cardinal of Bourbon as would-be king). It confirmed the sense of
  several re-parsed passages ("a i propri figliuoli", "tenirle tute unite per potere resistere", "s'auicinaua a queste
  parti"); no word was taken from it.

## 2. Word decode and hand re-parsing (R48_corrections.tsv, 69 rows)

- Codes with displaced or wrong figures: 296 for 196 (Sauoia), 113 for 131 (cardinale), 131 followed by a redundant
  "di"; spurious dotted 171 at the start.
- per (64) inside words: prosperità, prosperam.; 64 written for 44 (specialm.).
- Abbreviations with 8: esatisimam., continouam., suplic[he]uolm., presentialm., prosperam., specialm.
- 4 for 14 (h) again (fin hora), 24 for 14 (hauere).
- Vocabulary gaps where the figures were right: sofficienza, mestitia, piisimo, cesarà, immortali, protrahendo, gran
  priore, bagni a Luca, entrarui, gabineto, asignatione, eceso, figliuoli, s'auicinaua, certificata, tratenise, Umans
  (Le Mans), altercationi, "come io per nome di N. S.".
- No image crops were taken for this record (image use kept for the other five); the open stretches below were not
  re-checked on the images.

## 3. Alignment

`python reread_b00_align.py R48`: `TOTAL R48: 1525 words, 0 supplied, 6 partly` after moving the 401v page marker to
where the page turns inside "contenta|re" and re-ordering "[…] come era". The six remaining flags (sofficienza,
basterà, scintila, immortali, mouere, da' predicatori) are one-figure slips listed in the tsv.

## Result

Before: 0.64. After: 0.73 clean-sentence share on the "## Reading" body (hole rate 0.091). By hand: 11 unread stretches
([…]), 7 partly carried words, 1,525 words; both sheets build sentences throughout except at the page-turn gaps.
Grade B: sentences hold; more holes than R46, several figure-context corrections, no image checks.

## Still open, and why

- The beginnings and ends of both sheets (399r l. 2, 400v l. 9, 401r l. 2, 402v l. 15): fragments of words carried over
  from pages not in the record, plus figures that do not parse.
- 399v/400r: "onde si crede che" is followed by "…rauo di fare con il Re questo oficio": text missing at the page turn
  (perhaps a line skipped by the encipherer).
- 400r l. 5 ("1 5 3"), 400v ll. 4 and 7, 401v ll. 20–21 (what the Pope would advise the King to do), 402v ll. 10 and 12:
  short stretches with no parse under the slips tried. Not checked on the images (no outside blocker known; left for an
  image pass).

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`; the pages are clean, the ink faint on 401v), cancellation strokes looked for (none), the figures
parsed (`r2p_parseall.py`). Nothing could be filled.
Left, with blockers:
- 399r l. 2 "[…] hauendo io": "171^. 9 4 2 7 5 2 0 1 2 0 8" (best parse "iobicnran"). Blocker: no-key-material.
- 399r l. 4-5 "uoglio riuerire [?obedire] et seruire": "9 4 2 3 5 2 0 1 7 1 | 0 1 5 3" (best parse "obemine"). Blocker: no-key-material.
- 400r l. 1 "[…] rauo di": "(none)". Blocker: nothing written there; no-key-material.
- 400r l. 5 "la quale […] non ho": "(none)". Blocker: nothing written there; no-key-material.
- 400v l. 4 "che lui […] le haueua": "7 1". Blocker: too-short.
- 400v l. 7 "lo facese […] non ricusaria": "(none)". Blocker: nothing written there; no-key-material.
- 400v l. 8-9 "duca hauesero ca[u]sa di lamentarsi": "2 2 1 3 7 | 4 5 2 1 2" (best parse "aauisa"). Blocker: no-key-material.
- 400v l. 9 "di lui […]": "8 2 2 1 5 2 4 7 0 0 171^. 5 4 9 7 111^. 0 0 7 0" (best parse "acsirisoi[il"). Blocker: no-key-material.
- 401r l. 2 "[…] hauendo questa": "1 0 7 7 5 2 4 7 5 0 1 0 0 5 8" (best parse "niicsienre"). Blocker: no-key-material.
- 401r l. 14 "andare là [a] parlare senza": "2". Blocker: too-short.
- 401v l. 2-3 "uenise qualche [?ordine] da N": "1 9 3 | 0 0 2 6 1 7 0 1 5" (best parse "rofmtine"). Blocker: no-key-material.
- 401v l. 8 "il sig [?cardinale] di Borbone": "113^.". Blocker: no-key-material.
- 401v l. 20 "di fare […] per impedire": "0 1 7 3 6 3 7 0 9 1 5 1 3 5 4 5 1 5 3" (best parse "nutupotese"). Blocker: no-key-material.
- 401v l. 21 "non ci [?sia] [?in] Francia": "4 1 7 1 7 1 1 7 1" (best parse "siii"). Blocker: no-key-material.
- 401v l. 22 "altro Re […] come era": "8 5 6 5 0 3 7 1 1 7 1" (best parse "tluri"). Blocker: no-key-material.
- 402r l. 21 "di Trento [?et] che loro": "1 6". Blocker: no-key-material.
- 402v l. 10 "ela si […] in buona": "7 1 8". Blocker: too-short.
- 402v l. 12 "di fare [?lo] anco aprouare": "0 2". Blocker: no-key-material.
- 402v l. 14-15 "l autorità […]": "8 2 | 4 7 5 4 0 0 1 112^. 2 6 9 6 7 4 4 0 1 1 7 1 0 5 5 6 9 0 1 0" (best parse "stegn[l'imperatore]atotispnileetnn"). Blocker: no-key-material.
Result: 0 holes filled; 18 left, each with its blocker.
