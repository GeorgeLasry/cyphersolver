# Re-reading log, HCPortal 497, 504, 505, 506 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF / VERIFY3_BRIEF, batch r2b)

## Starting point

The 22 Oct audit kept these four letters "read", but their only text was the machine segmentation in
`reading_segmented.txt` (dictionary word division, bracketed letters, `<nnn>` codes). The v3 verification of 23 Oct
scored those blocks 0.0 (f. 12-13), 0.5 (f. 18), 0.5 (ff. 23-24) and 0.286 (f. 25) on the explicit-hole measure and
demoted them to "decoded, not read" (blocker: not-attempted). The same day batch b08's sibling readings
(HCP496/502/503/507/509) were found to carry a spelling normalisation (`b08_norm.py`: alhir -> alhier, hette -> hätte,
Feint -> Feind ...), which the reading rules forbid.

## 1. Spelling restored in the sibling readings

`research/reading_audit/r2b_mals_denorm.py` walks each reading body in order against the decode stream of its
transcription files (letters only, u/v and i/j/y merged, umlauts folded, the transcribed clear words included; ff. 30-31
as the alternative stream for 507) and puts back, for every word that is a value of the b08 map or of the 496 hand list,
the writer's form its figures give at that point (the candidate found next in the stream and followed soonest by the
next word). Restored: 496 10 words (hirnechst, alhir, nunmer, Virtel 2x, weill, duppelt, Fridenstractaten, one, biel),
502 10 (newe, bestimte, Hoffstat, füret, deme, mitt, iren, one, Wen, dan), 503 11 (hatt, andeiten, Stilstants, Tragons,
irer 2x, dan 2x, deme, leizten, Deitschlant), 507 87 (Feit/Feint, schleinig, damm, Schieffe, musten, uberlant, unt,
nitt, hette ...), 509 0 (its normalisation had touched no word). The headers now say so. Scores (`v2_score.py`, de):
explicit-hole share unchanged (496 0.667, 502 0.118, 503 0.458, 507 0.662, 509 0.659); the plain share falls where the
modern word list no longer recognises the writer's forms (496 0.667 -> 0.333; 507 0.437 -> 0.380). 496 stays read on
the German explicit-hole bar.

## 2. Re-read of 497, 504, 505, 506

1. **Existing text?** None: no decipherment on any leaf or address side (f. 13 is an address side with show-through
   only), no clear copy, no edition (NOTES, Escalation: print, known-keys). The only second witness in the volume is
   the duplicate of 28 March (ff. 30-31), which belongs to 507.
2. **Images.** HCPortal records 497, 504, 505, 506 and their six original scans (hstam_4_h_1411_0012, 0013, 0018,
   0023, 0024, 0025) fetched 23 Oct 2026 from api.hcportal.eu (full browser User-Agent and the crypto.hcportal.eu
   Origin) into the session scratchpad `reread\r2b\img` only; crops with `reread\r2b\crop.py`.
3. **Decodes.** Every cipher line decoded with `key.txt` unchanged, the group under each letter
   (`research/reading_audit/b08_dec.py`, P=1). Readings built sentence by sentence from the decode; the breaks looked
   at on the scan where a group could change the word (f. 12 block 1 and block 3 last lines; f. 18 lines 10, 14 and
   block 2; f. 23 lines 12, 16-20; f. 25 lines 14-15).
4. **Findings on the scans.**
   - f. 25 l. 15: the transcription's "4#0?" is a 40 struck through by the writer, and its "12?" is 42 (m): "ist nunmer
     um vierten mal dem [122] zu kommen" (`HCP506_corrections.tsv`).
   - f. 18 l. 11: "das die Reiterei noch wol sobalt keinen Dinst" (the segmentation had "Reiter ein noch"); l. 14 the
     groups before [122] are 77 84 30 (s e r), no word; block 2 the "78" of "ulerige" is a clear 78, not a b-group.
   - f. 12 block 3: "tractinen" has a clear 63 (n) where r is needed; "mi<H> der" is the crossed H, read tt.
   - f. 23 l. 17: "1 t Reichst" (1 thousand Reichsthaler) and "seimer beit sich" are as transcribed; l. 19-20
     "wolte eelbige" and "wir bberufzie weise" are as transcribed (no word).
   - f. 24: "weil es mit de[m] Reiderlant": the struck 57 is the m of "dem"; the Reiderland is named on f. 28 too.
5. **Readings** `HCP497/504/505/506_reading.md`, English `_en.md` with the same holes. The plain H sign stands for ll
   and (Mittel, mitnemen, hatt, Mitt der) tt, as b08 found in the siblings; the crossed Z and the lone 7 for st
   (Estat, Stillstant, gestalt); `t.` before "Reichst." is "tausend" as written. Encipherer's slips are bracketed
   letters or `[?word]`; codes stay `[nnn]` unless `codes.txt` values them (128, 130, 188, 253, 273).
6. **Word-by-word check** (`b08_align.py`): every unbracketed word looked up in the decode stream. It caught
   "Stattalter" (figures: Statthalter), "Augusto" (figures: Augustto) and "bewussten" (figures: bewustem), all
   corrected. The words it still lists are carried by a sign with that value (mitnemen, Mittel, hatt, wiewol: H = tt/ll;
   Stillstant: crossed Z; Soldaten: crossed 39; diselben: the e written above the line; mal: the corrected 42).
7. **Look-alike letters**: none of the readings rests on the other member of a look-alike pair; the H read as tt is
   the sign's second value in this key, not a look-alike.

## Result per document (`research/reading_audit/v2_score.py`, de, reading body)

| document | before (segmentation) | after: explicit holes | plain | state |
|---|---|---|---|---|
| HCPortal 497 (f. 12) | 0.0 | 0.632 (12/19) | 0.421 | **read** (B) |
| HCPortal 504 (f. 18) | 0.5 | 0.562 (9/16) | 0.438 | decoded, not read |
| HCPortal 505 (ff. 23-24) | 0.5 | 0.545 (24/44) | 0.364 | decoded, not read |
| HCPortal 506 (f. 25) | 0.286 | 0.625 (10/16) | 0.438 | **read** (B) |

## What stays open and why

* **504, 505**: the sentences build German, but the code layer stands in most of them: 504 [212], [122], [120],
  [123], [148], [260] and the signs <L>, <16#>, <9#>, <H>, <V>; 505 thirteen codes ([120], [122], [140], [137], [163],
  [177], [189], [191], [200], [202], [217], [231], [269]) and the signs <f>, <S>, <F>, <0>, <8>, <V>. Blocker:
  no-key-material (about 40 open codes in the volume, mostly single occurrences; the Marburg key sheets were tried in
  September). A few letter strings give no word after the image check (504 "ser", "ulerige wrlich", "1 wl rlist";
  505 "seimer beit", "bberufzie", "alswaeEIEI"): encipherer's slips with no second copy to correct them.
* **497**: block 1 has two open clauses ("sein we …", "und tam7"); the rest reads.
* **506**: the clause "<H#> Schreiben an <V> vom <L> 1 Ianua" keeps three signs open.

## One sentence per document

* 497: "Es ist von guter Hant avisiret, dass man zu Regenspurg geschlossen, <H#> Gesanten nach {Cöln} keinen salvum
  conductum zu erteilen." - It is reported from a good hand that it was decided at Regensburg to give <H#> envoys to
  {Cologne} no safe-conduct.
* 504: "So verstercken sich auch die {Compagnien} zu Fus noch schlecht, wie auch die newen Werbers." - The foot
  companies are also filling up badly, as are the new recruiters.
* 505: "Stecken also [?in der] Bruhe, wissen nit, womit wir ihn zwingen wollen, und befinden nun in [d]er That, das wir
  mit einem Frantzosen gehan[d]elt haben." - So we are [?in the] soup, do not know how to compel him, and find now in
  fact that we have dealt with a Frenchman.
* 506: "[120] hatt sich nunmer resolviret, die Furleite zu contentiren." - [120] has now resolved to satisfy the
  carters.
