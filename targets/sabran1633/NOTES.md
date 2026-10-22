# Melchior de Sabran to Claude Bouthillier, Genoa 1633 — BnF fr. 4134 (Sabran's letter-book) — NOTES

Status: in progress (21 Oct 2026). A contributed partial reading (issue #56, Harumi-Matsuba), checked here on two
leaves; the stretches that form no words, five name codes and fr. 4135 are still workable with the same key, and
George Lasry is to be asked whether he holds readings of these letters.

**Outcome: read with known key, read in part (contributed).** George Lasry's 2022 key "BNF Francais 4134" (published
by S. Tomokiyo on Cryptiana GL.htm, "Melchior de Sabran (1631)") applied by Harumi-Matsuba to the cipher passages of
nine leaves of fr. 4134: 891 signs, 879 with a value (98.7%). Measured here: 74.3% of the decoded letters fall in
French words of three or more letters (chance with shuffled keys: 27.0%); the language-model score beats all 1000
shuffled keys on every leaf; the calibration 551/599 = 92.0% on Baluze 155 f. 79 reproduces from their files.
The passages report the discovery in September 1633 of a plot to hand over Savona: the munitionnaire and two others
arrested and brought to Genoa, "ceux qui sont pris" speaking of "donner la place".

Sibling target: [`targets/sabran1631/`](../sabran1631/NOTES.md) (Louis XIII to Sabran, Baluze 155 f. 79, 1631, same
key, deciphered by Lasry; page `sabran1631.html`). Kept apart because that entry is Lasry's existing decipherment
and this one a contributed reading of different letters.

## Documents

- BnF Français 4134, "Recueil de copies … Troisième livre des negotiations du Sr de Sabran à Gennes", 1633: the
  letter-book of Melchior de Sabran, French resident at Genoa (1630–1637), copies of his despatches to Claude
  Bouthillier, secretary of state. Gallica ark:/12148/btv1b9060193z. Cipher passages on nine leaves:
  f. 46v (view 100), f. 50v (108), f. 54r (115), f. 57r (121), f. 57v (122), f. 66r (139), f. 66v (140), f. 69v
  (146), f. 73v (154). f. 66r and f. 66v are headed "23 septembre".
- Not covered: f. 51 (listed by Tomokiyo, not opened by the contributor); BnF fr. 4135 (1635), ff. 132–251, said
  to use the same key, in another copyist's hand. No DECODE records for fr. 4134 or fr. 4135 (checked in
  `research/catalogue_harvest/decode/list.json` and `decode_updates/records_current.json`, 21 Oct 2026).
- Catalogue 310 ("letters readable with keys in hand": Sabran to Bouthillier, fr. 4134 ff. 46–73 and fr. 4135).

## The key

Lasry's reconstruction (25 May 2022) of the 1631 Louis XIII–Sabran cipher: homophonic letters (up to five signs for
e), a doubling sign, word signs (de, en, et, la, que, qui, vous, ment, tion, ont, si, prince/duc …) and a title
sign (27). `contributed/data/key.tsv` rewrites it with shape names (66 distinct signs used here). Codes not in the
key: 3i, 35, 12, 20, 33 (probably names).

## The contribution (issue #56, 20 Oct 2026)

Harumi-Matsuba (GitHub account created 19 Oct 2026), repository
https://github.com/Harumi-Matsuba/sabran1631-public (CC BY 4.0 / MIT), copied into `contributed/`
(`contributed/ATTRIBUTION.md`). All AI work: first transcription by Claude Opus 5.5, seven rounds of disagreement
judging by OpenAI Codex and Claude Sonnet (a sign changed only where both agreed; 16 of 60 corrections reverted on a
two-way re-judging), an independent Codex transcription (three runs, 92.4–92.7% sign agreement), a shuffled-key
control (0/1000 on every leaf) and a calibration on Baluze 155 f. 79 (blind Opus transcription through the same
rounds: 92.0% of Lasry's letters). **No person checked the transcription.** They call it a partial reading
themselves. Their "full reading" criteria (inter-model agreement plus control) are not this project's read bar.

## Checks made here (21 Oct 2026)

- `measure.py` → `measure.txt` (fr-1600-letters LM without spaces, 1000 shuffled letter keys; word coverage from
  the fr-henri4 corpus, words of 3+ letters seen 5+ times, DP maximum cover):

  | leaf | signs | valued | LM real | shuffled max | coherent | shuffled median |
  |---|---|---|---|---|---|---|
  | f. 46v | 87 | 86 | -2.57 | -4.10 | 0.73 | 0.27 |
  | f. 50v | 269 | 265 | -3.37 | -4.34 | 0.64 | 0.27 |
  | f. 54r | 38 | 37 | -3.25 | -3.61 | 0.63 | 0.35 |
  | f. 57r | 127 | 127 | -2.83 | -4.25 | 0.81 | 0.28 |
  | f. 57v | 64 | 64 | -2.73 | -3.91 | 0.77 | 0.25 |
  | f. 66r | 149 | 144 | -2.23 | -4.34 | 0.79 | 0.25 |
  | f. 66v | 59 | 58 | -2.17 | -4.02 | 0.81 | 0.26 |
  | f. 69v | 71 | 71 | -2.67 | -4.09 | 0.86 | 0.30 |
  | f. 73v | 27 | 27 | -1.95 | -3.30 | 0.93 | 0.22 |
  | total | 891 | 879 | | | 0.743 | 0.270 |

  The word cover is generous (short words fit anywhere; shuffled keys reach 27%), so 74% is an upper bound on the
  share that reads as sense. Their READING.en.md gives a word division for about half the runs; the rest, most of
  f. 50v and parts of ff. 54r and 57r, form no words.
- Calibration recomputed from their files with their stated method (difflib against `calib/lasry_plain.tsv`):
  final 551/599 = 92.0%, first transcription 540/599 = 90.2%. Both reproduce.
- Sign counts: `_check_profile.py --measure … --drop-first` gives 892 tokens; the extra one is the `|` separator on
  c115_35. 66 distinct signs.
- Image spot-check (`spotcheck.md`): f. 66v 59/59 signs agree; f. 66r 113/116 checked signs agree. Two errors on
  f. 66r: `8 nt` counted twice across c139_23/23b, and the AI-agreed correction z→lh on c139_23c is wrong on the
  image (the sign is z: *secre[t]*), as their own OPEN.en.md suspected.

## Remaining gaps

- f. 50v, most of lines 17–23, 25, 26, 29, 30, 32 (about 200 signs) form no words - blocker: open-codes; the key is in hand and the signs are legible, so this is a re-transcription by a person against the key, not an outside block
- f. 57r lines 21, 24, 27, 36, 38 and f. 54r line 9 form no words - blocker: open-codes; same: workable re-transcription
- name codes 3i, 35, 12, 20, 33 (not in Lasry's key) - blocker: open-codes; few occurrences, context (Savona, citadelle?) does not fix them
- corrections the AI judges agreed on that read worse (f. 46v c100_32 x→pl, f. 66r c139_23c z→lh, f. 57r c121_24) - blocker: open-codes; c139_23c checked here and wrong on the image; the others need the same check
- BnF fr. 4135 (1635), ff. 132, 215v, 217, 224v, 226v, 227v, 231v, 239v, 243, 251 - blocker: open-codes; same key per Lasry, but the copyist's forms do not match the fr. 4134 sign sheet; a two-run Codex trial gave only scattered words (le Milanois, de la ligue); workable with a sign atlas for that hand
- f. 51 (listed by Tomokiyo) - blocker: open-codes; not opened by the contributor or here; workable with the same key
- the originals as received by Bouthillier (Archives diplomatiques, Correspondance politique, Gênes) and any contemporary decipherment there - blocker: needs-physical-access; not digitised

## Escalation

- [x] siblings: Baluze 155 f. 79 (sabran1631, Lasry's decipherment) used for calibration; fr. 4135 tried by the contributor (scattered words); f. 51 still to open
- [x] clear-pages: the contributor found no contemporary decipherment on the leaves examined; none seen on f. 66r-v here
- [x] known-keys: Lasry's 1631 key is the key named for these letters (Tomokiyo louisxiii.htm); NoAutopilot's transcription of the same key compared by the contributor
- [x] print: Tomokiyo louisxiii.htm and GL.htm list the passages as undeciphered; no edition found by the contributor; George Lasry may hold unpublished readings (Tomokiyo says he found the key applies to them) - to be asked
- [n/a] key-rebuild: the key is Lasry's complete table; the open stretches look like transcription errors, not missing key values (the shuffled-key control and the 98.7% valued share say the table fits)
- [x] retry: f. 66r-v re-checked on the image here (two errors found on f. 66r); the rest awaits a person's check

## Files

- `contributed/` — the contributor's data, documents and code (see ATTRIBUTION.md).
- `measure.py`, `measure.txt` — the re-measure above. `spotcheck.md` — the image check.
- Page crops: `docs/sabran1633_lead.jpg`, `docs/sabran1633_f66r.jpg`, `docs/sabran1633_f66v.jpg` (BnF fr. 4134
  f. 66r-v, via the BnF IIIF service).
