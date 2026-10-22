# Open points

[日本語](OPEN.md)

## Signs with no value (13 kinds, 15 places, among the 1,103 signs of the two pages)
Signs that get no value in `src/decode.py`. Line numbers are those of `data/transcription_f120_all.txt` (c1NN = f. 120r line NN, c2NN = f. 120v line NN). "Second" is the reading of the Claude Sonnet transcription (`second/`).

| Sign | Times | Where | Context, candidates |
|---|---|---|---|
| oo (∞-shape, two loops) | 3 | c109, c208 (2) | c109: pour les [∞]voyer (one would want en). c208: the last two signs. A different shape from the three-loop sign after mil (ooo), which is read as escus by inference |
| thb, 7, Sbar | 1 each | c101 | opening « [thb] a [7] u [Sbar] je vous asseure ». Perhaps an address (Monsieur or the like). The second reader read thb as tt (les) |
| 30 | 1 | c105 | ne se raportent [30] aux advis. A negative word fits; point would read (31 is pas in Tomokiyo's table). One place only; 30 also has no value in Burford's f. 385 |
| Esign (E-shape) | 1 | c115 | que [E] est tout resolu (a code sign for a person or a title?) |
| Om (flat Ω-shape) | 1 | c117 | partir si [?] qu'il saura (tost?) |
| qx (q with x) | 1 | c202 | l[?]urs estrangers (e for leurs). The image check found a separate q+ before it, so the earlier inference (qx = le) was dropped. Codex and Claude Sonnet disagreed between qx and r |
| invTl (⊏-shape) | 1 | c123 | je croy que [?] ne s'y trouvera pas (on, nul or the like?). The second reader read it as ⊣ (plus). Burford notes that on f. 385r of the same volume an inverted T (⊥) fits « vostre majesté » in all four places (his method/other-letters.md). « je croy que vostre majesté ne s'y trouvera pas » reads, but on the image the ⊏-shape is a horizontal stroke with a « [ » on its right, unlike the sheet's ⊥ |
| 15 | 1 | c128 | profit de n[?] [15] … tombé |
| .u. (u between dots) | 1 | c129 | un[e] [?] du secretaire La Marsilière (a letter or the like?) |
| 4d (4 with a dot) | 1 | c130 | des affaires de [?]spe… |
| Dsign (large D with a dot) | 1 | c208 | at the end |

## Unread stretches and divided readings
- r c03–c04: « qu'il souffre ne soit a desseing » (revised following the three-reader vote). The division « des seing » is inferred.
- r c05: « que l'on de[?]a donne[?s] ».
- r c09: « qu'un[?e] n de ment pour les [∞]voyer ».
- r c15–c16: « que quelque [?…]ment et conjuration que vous s[?] puis i es faire de s[en] aler ».
- r c22: « est le s[?ieu]r [?M]ontablaye ». The signs are w q+ g f delta th r 2c : 6 a 4 pi q+ 4 dbar r. For « le sieur » the last r (e) should be # or ls (r).
- r c24: « si je irai[s], [?s'ay en dray] ».
- r c25–c26: the stretch L r 6 a 4 pdots 9 delta # in « qui sui[?vent] [?…] ».
- r c28: « de n [15] est m est tombé » (w 2 w a // 8s pi delta). Something like « estant tombé »?
- r c29–c31: « qui nous le [?m]ort particulierement des affaires de [4d]spe … ade ment ».
- v c03–c05: « l'on ne sauroit [?rotir] rendre l[?λ]a … tort … faict [L] user ; [f] redu u ».
- Interlinear additions (« 8δ » in r c07 and c10, « ar » in r c11 and c13, « Hr » in r c12, « +q+ » in r c19) are not used in decoding. In r c19, mar + al reads as an abbreviation of mareschal. The « Hr » (le) of r c12 may make no + le an abbreviation of nouvelle.

## Look-alike signs
- r (e) and x (u): in r c01 ennuyé, r c20 se retirant and r c04 desseing, signs that look like x were read as r. Confusions the other way probably remain.
- 8 (t) and 8s (m): mil, mareschal, sepmaines, ennemis were read with 8s. The difference in form is small.
- S (c), ls (r), hs (r): asseure in r c01 and je croy in r c22 were read with ls.
- f (i|s), f2 (n), long f: conjuration in r c15–c16 was read with f2.
- curl (backslash with o) and curlo (stroke whose foot curls right): in the first transcription the backslash-shape was named bslash and the curling shape curl. The calibration showed the backslash-shape to be Burford's curl (pour), and the names were changed. The curling shape (o) is taken to be a sign not on Burford's sheet, but it was not compared with the sheet again.
- lambda (λ): q in Tomokiyo's table; x in Burford's key and in the calibration. In this letter it can be read both q (qu'une, r c09) and x (d[i]x iours, r c22).
- Pairs on which the Sonnet transcription used for checking differs most: ls and S (24 places), r and xbar (18), 8s and 8 (8). The first transcription chose by context in all of them.
- Differences from the independent second transcription (Codex, fifth run; edit distance of values 69 recto, 22 verso) have not been looked at (looking and correcting would make this comparison no longer independent). The 77 differences with Codex's third run before it were checked on the image and 9 places corrected (check/DECISIONS.md).
- Pairs where both models in the image check (Codex and Claude Sonnet) said the shape is that of another name on the sheet, but that name's value does not fit the context, so nothing was changed (check/DECISIONS.md):
  - curlo taken as the sheet's curl (4 places). Burford's key has curl = pour. In f. 120, reading the backslash-with-o shape (curl) as pour and the curling shape (curlo) as o fits (auons, corps, offres, souffre). Which of the two shapes the sheet's curl examples are has not been checked.
  - 2 (m) taken as the shape of 2u (de in Burford's key) (5 places): mil, estime, les mains, temps, etc. all read with m.
  - 6b (f) taken as B (s in Burford's key, from one or two places) (v c01): fondement reads with f.
  - 9 (d) taken as d (g in Burford's key) (v c07): grands reads with d.

## Not checked
- Sender and date. Unchecked inferences:
  - Date: about October 1586 (inferred). Three grounds. In the volume f. 120 lies between ff. 103–104 (Mayenne, September 1586) and ff. 149–150 (Mayenne, October 1586) (Tomokiyo's list and Burford's other-letters.md). The letter says the Cardinal of Guise wrote "on the 2nd" and cites the treasurer Bilart's despatch "of the 21st of last month", so it was written after the 2nd of a month, with Bilart's despatch in the month before. The content (the army breaking up, before winter, six more weeks) is the situation of f. 385 in the same cipher (start of winter 1586 in Burford's reading) and of ff. 149–150 (contemporary decipherment: « ceste armée d'ailleurs si desbauchée »).
  - Sender: someone on Mayenne's side, possibly Pierre Forget (the correspondent who uses this cipher in other letters) (inferred). Grounds: the cipher is Mayenne and Forget's Cipher-2; the writer calls Mayenne « ce prince » in the third person and addresses the recipient as « vous » (a king would be « Vostre Majesté »); the contemporary decipherment of f. 97r (Forget's letter) has « de se retirer, tant il est ennuyé », close to f. 120's « ce prince est plus ennuyé et fasché que jamais ». The recipient may be Villeroy or the like. None of this is checked.
  - How to check: compare paper, hand and folds with ff. 119 and 121; the dates of Biron's letters from f. 112 and of f. 192 (an intercepted letter to a secretary of the King of Navarre's chamber); printed collections (letters to Villeroy etc.). Two web searches (20 October 2026) found nothing.
- Persons: who Bilart, [M]ontablaye and La Marsilière are. La Marsilière appears in another document in the ledger as an envoy of the King of Navarre (« le Sr de Vesin de la Marsilliere »), and the catalogue describes f. 192 of the same volume as an intercepted letter to a secretary of the King of Navarre's chamber ("Notes" in [PRIOR_CHECK.en.md](PRIOR_CHECK.en.md)). Neither was checked.
- The endorsement that Tomokiyo calls « illegible » is not on views 246–247 (perhaps on another leaf).
- Accuracy of the transcription: on seven lines of f. 104r, sign accuracy by the same way of reading as the published transcription (one Opus reader decoding with the key) is 90.5% (95.6% counting same-value names as matches); one shape-only pass gave 86.9% (89.1%) and 70.6% letter agreement. The accuracy on f. 120 itself was not measured. Agreement of values with the independent second transcription (Codex, fifth run) on f. 120: 92.2% recto, 89.9% verso ([METHOD.en.md](METHOD.en.md)).
- The confusions of # and 4t, and of 2o and "a 0", found in the calibration were not re-examined in the transcription of f. 120.
