# Re-reading log, rupert (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b10)

## Starting point

Reading audit (22 Oct): five entries "decoded, not read", all of them undeciphered numeric ciphertexts with the note
"not deciphered": Maurice to Rupert 7 July 1645 (Warburton iii. 133), Add MS 72438 f. 9 (R8623) and f. 10 (R8624),
Add MS 18982 ff. 51-52 Trevor (R8433), Add MS 72438 f. 104 (R8725). The instruction for this batch: try them only if
a known key fits, looking at the sibling targets for Rupert's and Charles I's 1645 ciphers. The 9 Oct sessions had
already screened all 73 keys of Add MS 72438, keys 118, 123, 125, the Digby-Walsingham key, the Parliament keys and
Tomokiyo's royalist keys (NOTES.md): no fit.

## Step 1: is there a text already?

* No decipherment on any of the five sheets (all DECODE images seen 9 Oct; f. 104 again today at full resolution).
* Print, 22 Oct: Clarendon, *State Papers* ii (1773, archive.org `10622705bsb`, OCR grepped for "send for you",
  "threatning", "contentment", letters opening "Charles"), Bruce, *Charles I in 1646* (Camden Society 1856,
  `charlesiin1646le00chariala`, grepped for the Prince, "send for", "referring"), and two web searches for the f. 104
  phrases: nothing. Petrie, *Letters, Speeches and Proclamations of King Charles I* (1935) is on archive.org but
  lending-only (401), so not searched.

## Step 2: the known keys of the sibling targets

The sibling targets for the King's and the Queen's 1645-46 ciphers carry George Lasry's reconstructed keys on DECODE:
"TNA SP 106" (hm1645, R785, D3059), "TNA SP106-2" (sp106r787, R787, D3071), "TNA SP106-3" (goring1645, R932, D3079),
"TNA SP106-5" (sp106r929 and rupert1645, R929, D3085) and "TNA SP106-8" (sp106r924, R924, D3089). The four not already
in a checkout were fetched with the shared DECODE cookie into the scratchpad (and the SP106-8 key into the git-ignored
`decode/`). Each was applied to all five ciphertexts (scratchpad `apply_b10.py`):

| key | Maurice | f. 9 | f. 10 | Trevor | f. 104 |
|---|---|---|---|---|---|
| TNA SP 106 (letters 1-76, words 124-555) | 26/93 groups get a value, gibberish | 80/152, gibberish | 266/720, gibberish | 44/62, gibberish | 102/256, gibberish |
| SP106-2 (letters only) | 17/93, gibberish | 82/152, gibberish | 186/720, gibberish | 48/62, gibberish | 80/256, gibberish |
| SP106-3 (Goring 1645) | 16/93, gibberish | 57/152, gibberish | 149/720, gibberish | 29/62, gibberish | 55/256, gibberish |
| SP106-5 (King-Queen, read rupert1645) | 21/93, gibberish | 100/152, gibberish | 242/720, gibberish | 53/62, gibberish | 84/256, gibberish |
| **SP106-8** (Queen's household, Jan 1646) | 49/93, gibberish | 75/152, gibberish | 279/720, gibberish ("be qo at ...") | 38/62, gibberish | **201/256, English** |

**f. 104 is in Lasry's SP106-8.** Applied unchanged it gives "... CHARLES IT IS A GREAT CON[859]T MEN T TO ME THAT YOU
HAVE SO ... BY THE QUEEN S LETTRE S AND ARE SO ... FOR REFERRING YOU TO THE QUEEN ... I SEND FOR YOU ... I WILL SEND
FOR YOU ... THE QUEEN WILL NOT STA[79] BE HIN DE ...", and the endorsement "The direction endorst 347 313 364" reads
**THE KING TO THE PRINCE OF WALES**. So f. 104 is a clerk's fair copy of a letter of Charles I to the Prince of Wales.
The other four documents do not read with any of the five keys; SP106-5 has letter+digit word codes, which none of
them uses, and its letter table gives nonsense on their letter runs. They stay as they were (no-key-material, and
too-short for Trevor's 54 letter groups).

## Step 2b: f. 104 on the image

The transcription was checked line by line on IMG_R8725_I40320_P1 (6288 x 8451 px; crops in the scratchpad). It is
a clean clerk's copy with colons between groups; no label changed (`f104_corrections.tsv` therefore not written).
Line 11's 313 is written over another figure but reads 313.

## Step 3: filling the key from contexts

Lasry's SP106-8 lists only the values his one letter (R924) used. The values f. 104 needs are in
`f104_key_additions.tsv`, each with its basis, and come from two sources:

* **Lasry's own interlinear of R924 (D3091)**, where the same groups stand in readable sentences: 3, 7, 12, 30, 50
  are word spaces ('_'); 116 reads "can" in every R924 context ("that treaty can not possibly", "you can do for
  them"), not BROUGHT as in his key file; 127 = do, 207 = may ("207 it pleas your Majesty"), 208 = made ("if you
  have 208 any conclusion"), 320 = upon ("so much [797] 320 hands"), 334 = what, 450 = command ("in the 450 of that"),
  513 = express ("by the 513-ions you use").
* **f. 104's own words** and the alphabetical order of the nomenclator sections (100-344 and 399-776 run roughly
  A-Z): 43 = n (name), 90 = d (iudge), 62 = g (light), 73/51 = b/h (both), 79 = y (stay), 81 = c (a sence),
  859 = ten (contentment), 315 = then, 192 = let, 341 = whether, 412 = assur-, 429 = believe (Lasry: ASSUME?),
  136 = ever, 211 = make, 548 = God, 331 = who, 784 = true (conjectures marked so).

Tried and dropped: 3-a-7-s-e-n-81-e as "absence" (7 = b) before 3 and 7 were found to be word spaces in R924;
"so far" for 334-so-136 (334 = what in R924 gives "whatsoever").

## Word-by-word alignment

Every word of `f104_reading.md` was set against its groups in `f104_decode.py`'s output. Plain = every figure carries
it under Lasry's key; `[?word]` = a figure in it is one of the additions above (even the well-supported ones, such
as do, may, upon), or the word is partly carried (perswasion: the r is not written; blessing: 132 and an m are not
explained); `[word]` = supplied ("soone [as] I"); `[nnn]` = code not identified. Fixed in the pass: "as soone as" ->
"[161] soone [as]"; "absence" -> "a sence"; "God's blessing" -> "[?God]s [?blessing]".

## Result

| doc | before | after | state | rests on |
|---|---|---|---|---|
| f. 104 (R8725), Charles I to the Prince of Wales | not deciphered | **0.267** (4/15 clean sentences, body only, `reread_b10_score.py`) | decoded, not read | Lasry's SP106-8 key, unchanged + 35 values from R924's interlinear and f. 104's contexts; 3 of 5 sentences hold as sense, but most carry one or two open codes |
| Maurice 1645 | not deciphered | — | decoded, not read | no known key fits (five Lasry keys added to the screen) |
| f. 9 (R8623) | not deciphered | — | decoded, not read | same |
| f. 10 (R8624) | not deciphered | — | decoded, not read | same |
| Trevor 1645 (R8433) | not deciphered | — | decoded, not read | same; 54 letter groups too few to rebuild |

With every `[?]` value accepted as plain the f. 104 body would score 0.667; that figure is not the score, because
those values rest on one or two contexts. What keeps f. 104 below the bar is the nomenclator: 21 groups (227, 312, 131, 124, 466, 543, 534, 668, 38, 330,
308, 307, 188, 643, 502, 161, 769, 96, 132, 56, and 192 in its first use) are either absent from R924, Lasry's only
letter in SP106-8, or stand there unidentified too (227, 124, 466, 307, 502; 330 only as his "WAY?"), so they have
no key material. Sentence with translation (it is English): "let the Queen be iudge whether I really send for you or not;
assuring you that I will send for you [161] soone [as] I may do it with both our [769]ties" — the King's warning
that any summons not really his should be referred to the Queen.

## What would read more

* Another letter in SP106-8 (Lasry's key came from R924 alone): the other SP 106/10 letters of January 1646 that he
  assigned to other keys could be re-screened for SP106-8 code groups 466, 543, 534, 643, 502, 769.
* Petrie 1935 (lending-only) and the Clarendon MSS calendar for a printed text of the King's letter to the Prince.
