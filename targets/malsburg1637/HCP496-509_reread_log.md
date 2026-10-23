# Re-reading log, HCPortal 496, 502, 503, 507 (+508), 509 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b08)

## Starting point

Reading audit (22 Oct 2026): five of the ten Malsburg records "decoded, not read" (HCPortal 496 = f. 3, 502 = f. 14,
503 = ff. 15-17, 507 = ff. 28-29 with its duplicate 508 = ff. 30-31, 509 = ff. 32-33). Their decryption was the
machine-segmented line of `reading_segmented.txt` (word division by dictionary, codes as `<nnn>`, bracketed letters
where a group gave no word). Clean-sentence share of those blocks (`docs/_check_reading.score_text`, de): 496 0.333,
502 0.143, 503 0.389, 507 0.271, 509 0.182.

## What was done

1. **Existing text?** None. No decipherment on any leaf or address side (ff. 4, 13, 17 checked in September), no
   clear copy, no edition or calendar (NOTES, Escalation: print). The neighbouring records of HStAM 4 h 1411 are the
   other Malsburg letters already in this target. The only second witness is the writer's own "Duplicat" of the 28 March
   letter (ff. 30-31), enciphered separately with its own line breaks.
2. **Images.** HCPortal records 496, 502, 503, 507, 508, 509 and their 12 original scans fetched from api.hcportal.eu
   (a full browser User-Agent and `Origin: https://crypto.hcportal.eu` are needed; a short User-Agent gets "Access
   Forbidden"); saved only in the session scratchpad. Crops with `research/reading_audit/b08_crop.py`.
3. **Decodes.** Every cipher line decoded with `key.txt` unchanged, the group printed under each letter
   (`research/reading_audit/b08_dec.py`), and each break looked at on the scan. No key change: the breaks are code groups,
   signs, slips of the encipherer and groups cut at the torn edge of f. 14, not wrong table values.
4. **Readings.** `HCP496/502/503/507/509_reading.md`, built sentence by sentence; English `_en.md` with the same holes.
   - f. 28-29 read against ff. 30-31: where the copies differ the reading follows the copy whose figures give a word
     (`HCP507_corrections.tsv`): "uberlant" (f. 28 "uberlani"), "Schieffe" (f. 28 "SCHogTTe"), "wider Bestellung" (the
     "128" of f. 28 l. 41 is a w-group, not the code for Cöln), "Forstenau aber", "Hohendorf", "den Rest", "zu Rantzo".
   - f. 32: the French letter of "232" (3 Apr 1637) transcribed in full from the scan (the September transcription had
     only the words next to the cipher); one label corrected (extraordin<Q>re: the sign is the ai-sign, not mm;
     `HCP509_corrections.tsv`, `f032_corrected.txt`).
   - Signs with no single value were left open rather than forced: the crossed H gives ll (will, alle, voller, wollen)
     and tt (hette, hetten); the lone 7 stands for st (be7imten = bestimten, both copies of f. 28), ö (hochn7tig) and b
     (a7gehe); the cross + precedes "au" three times (auf + tman, + au casselisch, + Aufkündigung) without a value
     fitting all three; 4# fits "um" once and nothing elsewhere.
   - Readings of the encipherer's slips are marked `[?word]` (gewesen from "geaesen", Bruder from "budder", ziehen from
     "wihen", gleichwohl from "mleich vohl", berichtet from "berichtmmet", Ambassadeur over a blot).
5. **Spelling.** The bodies of the readings normalised in part (`b08_norm.py`, a whole-word map of the writer's forms:
   alhir → alhier, Feit/Feint → Feind, schleinig → schleunig, hette → hätte, Widerkunft → Wiederkunft ...); 496 by hand
   (hirnechst, alhir, nunmer, duppelt, Fridens-, Konig, Virtel). The diplomatic decode stays in `reading_segmented.txt`.
   The normalisation moves the scores by 0.00-0.04; none of the decisions below depends on it.
6. **Word-by-word check** (`b08_align.py`: every unbracketed cipher word looked up in the decode stream, u/v and i/j
   merged, the normalisation map reversed). It caught "Verlusts" (figures: "uerlust vor"), "Tractes" (figures: "des
   traicte"), "itzigen" (figures: "itzigem"), and unmarked slips (kürtzlich, geworben, gehindert, angedeutet, December,
   aufmachen, London, Printz), all corrected or bracketed. The words left on its list are carried by a sign valued in the
   key (a<H#>e = alle, Audiens with the au-sign), by the duplicate copy, or are the noted readings (unsre from "unssre",
   bestehet over a cut group, casselische from "cassellisch").
7. **Score** (`research/reading_audit/b05_score.py`, body only, de; for 509 the French paragraph scored as French).

## Result per document (clean-sentence share of the reading body)

| document | before | after | state |
|---|---|---|---|
| HCPortal 496 (f. 3) | 0.333 | 0.667 (6/9) | **read** (B) |
| HCPortal 502 (f. 14) | 0.143 | 0.167 (3/18) | decoded, not read |
| HCPortal 503 (ff. 15-16) | 0.389 | 0.375 (9/24) | decoded, not read |
| HCPortal 507 (ff. 28-29) | 0.271 | 0.437 (31/71) | decoded, not read |
| HCPortal 508 (ff. 30-31, duplicate) | — | as 507 | decoded, not read |
| HCPortal 509 (ff. 32-33) | 0.182 | 0.545 (24/44; French 23/30, German 1/14) | decoded, not read |

fraction_read 0.436 → 0.480 (496's 455 tokens added: 4,923 of 10,246).

## What stays open and why

* **502, 503, 507**: the German builds sentences around the codes, and a reader can follow every letter (f. 14 the
  provisioning of Hermanstein and the march by Mülheim and Siegburg; ff. 15-16 Beauregard's audience, Hoff's reports, the
  recruiting patents; ff. 28-29 the four objections to the sea journey, the guns without carriages, the questions for the
  States, the conjunction at Cloppenburg or Vechta). What keeps the share down is the code layer: about 40 open
  three-digit codes and a dozen signs, two to six in most sentences (blocker: open-codes, no key material; the Hesse-Kassel
  key sheets were tried in September), plus, in 507, many place names outside the period word list, and in 502 the torn
  right edge of the sheet. 503 scores lower than its raw decode because partly carried words are now marked as such.
* **509**: the French letter reads (0.77 as French); the German news extracts in the second hand were not re-transcribed
  (blocker: not-attempted). Their cipher runs are short and dense with paired-letter signs (OO, AA, XX, GG, CC, KK, LL)
  and codes (115, 123, 126, 129, 133, 148, 155, 156, 248), so even a full transcription of the clear words would leave
  most of their sentences holed.
* **508**: the duplicate; used as the control copy for 507, not read separately.

## One sentence per document

* 496: "Es ist noch Zeit, das man sich beim König von Ungern angebe wegen der Friedenstractaten und salvum conductum vor
  <H#> Gesanten nach {Cöln} sollicitire." — It is still time for one to present oneself to the King of Hungary about the
  peace negotiations and to solicit a safe-conduct for <H#> envoys to {Cologne}.
* 502: "Jan de Wert ist in persona zu Cölln …; wirt ihnen ohne Zweiffel nachgehen." — Jan de Werth is at Cologne in
  person …; he will no doubt follow them.
* 503: "Er redet aber nirgend von Friedmachen." — But he speaks nowhere of making peace.
* 507: "Zudem so müssten die [168] umb einen freien Pass ersucht werden, dann kein Garnison ohne expressen Befehl ein
  solch Anzal Schiffe würde passiren lassen." — Moreover, the [168] would have to be asked for a free passage, for no
  garrison would let such a number of ships pass without express orders.
* 509: "j'ay addressé toutes mes lettres a Mons Sengel a Londres" — I have addressed all my letters to Monsieur Sengel
  in London.
