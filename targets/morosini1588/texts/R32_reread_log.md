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

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`), cancellation strokes looked for, the figures parsed (`r2p_parseall.py`). On all six pages of R32
the ink has spread and the verso's lines show through exactly over the recto's, so most of each line looks
cross-hatched (the clean line-ends, where the verso is shorter, show that it is show-through and not cancellation);
the figures cannot be checked on these images beyond DECODE's transcription.
Filled (DECODE's figures carry every letter):
- 181r l. 2 "dia [a] dare": "62 17 2" = dia (the a before dare is not written).
- 182r l. 14 "che io le facese dare": "8 5 6 | 7 1 9 1 | 5 0 5" = che, io, le.
- 182r l. 15 "prouedere in quello": "1 7 1 1 0" = in. ("[?Non]": 61 8 = non, but the sense wants a verb; kept partly.)
- 183r l. 19 "né si potea": "70 91 51 35 2" = potea (the period form; was "[?poteua]").
- 183v l. 16 "dise che era uenuta molto a tempo": "5 00 21 | 3 3 35 01 37 15 2 | 20 91 27 9" (u written twice; 27 = lt).
Left, with blockers:
- 181r l. 2 "dare horamai [?a] questo negotio": "2 7 2". Blocker: illegible (spread ink and show-through).
- 181r l. 3 "et così […] mi ha": "8 4 8 4 1 7 4 0 1 7 1 5 0 3 7 4 9 1 7 4 8" (best parse "igilustris"). Blocker: illegible (spread ink and show-through).
- 181r l. 4 "non pensi [?il sig.] duca di": "4 0". Blocker: illegible (spread ink and show-through).
- 181r l. 5 "di Sauoia […] di quanto": "7 1 0 9 1 5 3 1 0 1 5 1 9" (best parse "inoentro"). Blocker: illegible (spread ink and show-through).
- 181r l. 6 "di Saluzo [?che] tenga anco": "0". Blocker: illegible (spread ink and show-through).
- 181r l. 6 "anco altri […] secrete nela": "0 1 3 7 1 5 1 1 7 5 2 1 1" (best parse "nutriear"). Blocker: illegible (spread ink and show-through).
- 181r l. 8-9 "Arles per […] a quella": "1 9 1 1 2 4 1 2 1 0 3 5 2 6 1 7 1 5 1 7 1 | 1 4 3 7 9 7 0 2 1 7 0 1 2" (best parse "orbraneditirsuoimina"). Blocker: illegible (spread ink and show-through).
- 181r l. 10 "M tà [s] e ne": "(none)". Blocker: nothing written there; no-key-material.
- 181r l. 11 "a Lione […] importuna […]": "5 8 5 3 5 0 1 2 6 9 9 2 1 2 2 0 3 1 2" (best parse "eenatooamura"). Blocker: illegible (spread ink and show-through).
- 181r l. 12 "[…] importuna […] da tuto": "5 1 2 1 2 9 2" (best parse "taoa"). Blocker: illegible (spread ink and show-through).
- 181r l. 12 "mondo di [?risentirsi] contra quello": "1 1 7 4 5 2 5 0 2 5 1 1 7 0 0 4 5 7" (best parse "risalatirsi"). Blocker: illegible (spread ink and show-through).
- 181r l. 13 "contra quello [?à aiutato] et il": "2 1 2 2 7 3 1 5 2 2 1 2" (best parse "alturca"). Blocker: illegible (spread ink and show-through).
- 181v l. 4 "gli oferiscono [962] […] darlo": "962^. 1 2 1" (best parse "otaa"). Blocker: illegible (spread ink and show-through).
- 181v l. 5 "mons di Nemur[s] che è": "8 1 0 3 5 2 0 3 7 0 0 2 5" (best parse "femurae"). Blocker: illegible (spread ink and show-through).
- 181v l. 6 "et descendente […] [?dela quale] non": "7 2 8 6 2 9 5 0 5 9 5 0 5 1 5 3" (best parse "iaaqualquale"). Blocker: illegible (spread ink and show-through).
- 181v l. 7 "di scontentarsi […] mons di": "1 7 1 1 0 8 9 7 2 6 3 1 3 5 9" (best parse "iniatureo"). Blocker: illegible (spread ink and show-through).
- 181v l. 10 "a mons [?di Fano] nuntio di": "2 6 7 8 3 021^. 0 1 9" (best parse "dinano"). Blocker: illegible (spread ink and show-through).
- 181v l. 11-12 "uoglia aiutare […] [?Ho lasato] di": "5 0 3 7 2 3 3 1 2 3 6 11^. 9 2 1 8 1 4 9 5 0 2 1 | 4 5 2 1 7 1 9" (best parse "luauntautrconasolascio"). Blocker: illegible (spread ink and show-through).
- 181v l. 13 "ad altro parti[c]olare che a": "3 0 2 1 0 0 1 5 1 7 259^. 1 5 0 2 1 0 0 5" (best parse "farticolare"). Blocker: illegible (spread ink and show-through).
- 181v l. 15 "sua cortesia […]": "8 1 7 111^. 2 2 9 1 1 9 1 2 2 5 4 2 0 2" (best parse "i[il"). Blocker: illegible (spread ink and show-through).
- 182r l. 2 "[…] il sig": "9 7 5 5 7 7 8" (best parse "oeteii"). Blocker: illegible (spread ink and show-through).
- 182r l. 6 "le dirò solame[nte] che io": "4 9 1 5 0 2 1 2 0 5" (best parse "solame"). Blocker: illegible (spread ink and show-through).
- 182r l. 9 "et nondimeno […] ho [?hauuto]": "1 0 1 1 2 4 4 9 1 0 1 2" (best parse "nxbsona"). Blocker: illegible (spread ink and show-through).
- 182r l. 9 "[…] ho [?hauuto] che a": "1 4 2 1 3 7 5 9" (best parse "haugr"). Blocker: illegible (spread ink and show-through).
- 182r l. 11-12 "non solo […] nela bola": "7 7 0 8 7 1 1 7 3 3 5 0 0 1 7 | 3 0 1 7 2 1 2" (best parse "ipxiuerifia"). Blocker: illegible (spread ink and show-through).
- 182r l. 12 "nela bola […] prohibire al": "2 6 1 1 1 2 0 2 2 0 1 2 1 9 1 7 1 0" (best parse "dxzmanzoin"). Blocker: illegible (spread ink and show-through).
- 182r l. 14 "facese dare [?il] memoriale [?Non]": "1 7 3 0" (best parse "if"). Blocker: illegible (spread ink and show-through).
- 182r l. 15 "[?il] memoriale [?Non] uederia di": "6 1 8". Blocker: illegible (spread ink and show-through).
- 182v l. 3 "li fa […] contradire al": "5 0 1 2" (best parse "lz"). Blocker: illegible (spread ink and show-through).
- 182v l. 6 "male È ricapit[at]o qui un": "0 0 1 2 5 2 1 7 0 1 7 1 5 9" (best parse "nncapito"). Blocker: illegible (spread ink and show-through).
- 182v l. 12 "beni temporali [?Io] ne ho": "8 7 0 9 1" (best parse "po"). Blocker: illegible (spread ink and show-through).
- 182v l. 13 "con il […] et con": "1 1 5 9 8" (best parse "xgr"). Blocker: illegible (spread ink and show-through).
- 182v l. 13 "et con [162] mostrandoli che": "1 162^.". Blocker: illegible (spread ink and show-through).
- 182v l. 15 "che i […] christianis[simi] et": "3 0 5 1 5 3 2 5 1 4 0 0 1 7 4 7 1 7 2 1 0 1 1 7 4" (best parse "feechristianis"). Blocker: illegible (spread ink and show-through).
- 182v l. 17 "entrate dele [741] Mi hano": "741^.". Blocker: illegible (spread ink and show-through).
- 182v l. 21 "che non [?io] sapeuo come": "1 7 1". Blocker: illegible (spread ink and show-through).
- 182v l. 23 "eclesiastici siano godu[t]i": "4 0 9 1 2 6 3 7" (best parse "godu"). Blocker: illegible (spread ink and show-through).
- 183r l. 8 "haueria ubidito […] che le": "8 7 7 9 1 2 6 1 7 4 5 1 7 1" (best parse "iodisi"). Blocker: illegible (spread ink and show-through).
- 183r l. 11 "et pietà […] rimedio che": "6 7 0 9 1 4 6 9 7 2 2 2 5 1 9 1 8" (best parse "tpostoiaaco"). Blocker: illegible (spread ink and show-through).
- 183r l. 14 "di solecitare [?l'espeditione] et di": "5 0 1 7 1 4 4 3 5 3 3 1 7 1 5 1 7 9 1 0 1 5" (best parse "enissepritione"). Blocker: illegible (spread ink and show-through).
- 183r l. 15 "auiso a [161] Hogi ho": "161^.". Blocker: illegible (spread ink and show-through).
- 183r l. 15-16 "ritornato a [?parlare] con S": "7 0 2 1 0 0 5 6 | 2 1 5 3 1 5 3" (best parse "paredee"). Blocker: illegible (spread ink and show-through).
- 183v l. 2 "mons di […] per lasare": "6 1 5 2 1 4 0 1 7 2 1 0 1 8" (best parse "ttagian"). Blocker: illegible (spread ink and show-through).
- 183v l. 3 "il gouerno d[i] Angolem di": "6 2". Blocker: illegible (spread ink and show-through).
- 183v l. 3-4 "Angolem di [?Santonge] et di": "8 1 1 2 1 0 1 1 5 | 9 1 0 1 4 0 3 5 8" (best parse "znxeonhne"). Blocker: illegible (spread ink and show-through).
- 183v l. 11 "et per […] anime di": "1 7 1 7 2 3 7 0 5 9 5 6 1 4 2 8 2 6 9 5 0 5 2 2 1 1 5 6 3 5" (best parse "iiauloethatoleaatte"). Blocker: illegible (spread ink and show-through).
- 183v l. 13 "nisuno con ragio[n]e ne poteua": "1 2 1 9 0 1 7 9 1" (best parse "raonio"). Blocker: illegible (spread ink and show-through).
- 183v l. 16 "di hauere […] et dise": "0 2 2 5 2 1 0 0 1 7 4 8" (best parse "nacaris"). Blocker: illegible (spread ink and show-through).
- 183v l. 23 "ancora ritrouarsi […]": "(none)". Blocker: nothing written there; no-key-material.
Result: 5 holes filled; 49 left, each with its blocker.
