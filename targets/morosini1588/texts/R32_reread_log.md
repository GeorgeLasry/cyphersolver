# Re-reading log, R32 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R32_decryption.txt` (character-model segmentation of DECODE D1696, KaJo,
Jan 2017, Meister no. 40): clean-sentence share 0.524, hole rate 0.145.

## 1. Is there a text already?

- DECODE "cleartext" image (D1037 = f. 180): the covering letter in clear, Blois 24 October 1588, ending "Il resto sarà
  nell'incluso foglio"; not a decipherment. 182r carries a clear docket "Del S. Card. Morosini, li 24 ottobre 1588"
  (transcribed by DECODE as a CLEARTEXT line). No interlinear glosses.
- Rome's decipherments (Segr. Stato Francia 27, per Hübner) not imaged: physical access.
- Tempesti II, book VII §§ XIX–XXIV: the Saluzzo affair and Poigny's mission (offer of the government to Nemours), from
  Morosini's letters; used to recognise Nemurs, Pugni, Saluzo; no words taken from it.

## 2. Decode

- `reread_b00_decode.py R32` (the batch decoder) first; then a scratch copy (scratchpad `dec2.py`: the same decoder with
  extra names — saluzo, sauoia, arles, balagni, ualeta, cambrai, angolem — and the 1/5 confusion added to its slip table).
  It turned "sanuto", "arnese", "uorriano", "ia lione" into Saluzo, Arles, "finiti li Stati … a Lione", "deue partire".
- A forced-alignment helper (scratchpad `fit.py`: aligns a candidate sentence against the transcribed figures of a line
  range, printing each slip) was used to test every repair; the tsv records the accepted ones.

## 3. What the breaks were

- 1/5 confusion in the transcription: Saluzo (10 for 50), Arles, "il Re" (17 1 10 1 153), anulato.
- m + 8 = -mente: specialm., publicam., chiaram., espresam., liberam., inuiolabilm. (as in R43).
- Spurious dots: 302/021 (Fano?), 259 (particolare), 533 (entrate), 221 (dal canto), 142 (hauere), a dotted 113 lost
  among stray 1s (parser read 134). Real codes found undotted: 131 (cardinale di Lenoncourt, 182r l. 2).
- "contra" written 6 4 9 2 twice (183r l. 22, 183v l. 13).
- Names: Nemur[s], Pugni/Pugne (Poigny), Lenoncourt, Renes (Parlement of Rennes), Cambrai, Parma, Balagni (Balagny,
  governor of Cambrai), Epernone, la Ualeta (La Valette), Metz, Bologna (Boulogne), Angolem, Cognac.

## 4. Image checks

The pages are heavily ink-corroded; crops of 181r ll. 1–5 and 8–9 (scale 1.3) show the figures as blurred strokes
through which single figures cannot be compared with the transcription. No correction rests on the image; all are
`figures` or `figures+context`. The transcriber's own '?' marks (181r l. 11, 181v l. 11, 182r ll. 11–12) coincide with
the unread stretches.

## Result

Before 0.524 → after 0.587 clean-sentence share on the "## Reading" body (hole rate 0.145 → 0.127; the checker counts
the clerk's spellings and the bracket marks). By hand: 28 unread stretches […] (most of them one or two words; three of
a line or more: 181r ll. 8–9 and 11, 182v l. 13), 20 partly carried words, 3 dotted groups not in the key ([962],
[162], [741]) in about 1,070 words. The narrative holds throughout: Saluzzo and Poigny's mission, the Rennes Parlement
against Lenoncourt's indult, the Cambrai canon and Balagny, Épernon and La Valette removed from Provence, the bull of
the *confidenze* and the Council of Trent. Grade B (many single-figure corrections from context, several holes).

## Still open, and why

- 181r ll. 8–9 (after "Arles") and l. 11 (paper damage marked '?' by the transcriber); 181r l. 3 (a title "sig.
  ilustris." whose bearer is not carried); 181r ll. 4–5 before "di quanto".
- 181v l. 4 [962] and the words before "darlo"; 181v l. 10 (the nuncio's see, read "Fano" from 30 21 01 9, unchecked);
  181v ll. 11, 15 (damage).
- 182r l. 2 (opening figures before "il sig."), ll. 11–12 ("non solo … nela bola …", '?'-marked figures), l. 14.
- 182v l. 3 ("li fa … contradire"), l. 13 (two addressees, [162]), l. 17 [741].
- 183r ll. 8 and 11 (damage marks), l. 15 [?parlare], l. 17 ("è [uero …]sima").
- 183v l. 2 (the man for Boulogne), l. 11 ("per … anime", damage marks), ll. 15–16 (the King's answer on the bull).
No outside blocker other than the corrosion is known; a second pass on a better image (or Francia 27) is what would
settle them.

## Word-by-word alignment (`reread_b00_align.py`, REREAD_BRIEF step 3)

- First run TOTAL R32: 1040 words, 3 supplied, 22 partly. Bracketed: d[i] Angolem, ricapit[at]o, godu[t]i, ragio[n]e, parti[c]olare. Left as aligner artefacts: "se" (181r l. 10, its s is inside the misparsed dotted 113/134) and "dal" (183r l. 9, its d is inside the spurious dotted 221).
