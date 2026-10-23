# Re-reading log, Bremen 1631 (R4330, R4331) (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b33)

## Starting point

Reading audit (22 Oct): "decoded, not read". `bremen_decoded.txt` gave every figure group a value but left them as
unsegmented strings with slips (`<ouolfk>`, `<itslatdgefodert>`, `<gener{5}ltots>`) inside a clear German transcribed
with `?` from the phone photographs, with name numbers bare. No reading body; `_check_reading.py` on
`bremen_decoded.txt`: 0.477.

## 1. Is there a text already? Only the interlinear glosses

- DECODE R4330 and R4331 fetched logged in on 23 Oct 2026 (`research/reading_audit/b33_fetch.py`): four images each
  (P1-P4), no attachment, no transcription, no comment, no plaintext field. Record note: "Letter from Johan Fredrik av
  Holstein, arcbishop to Tott, Åke Henriksson" (the address leaf, R4330 P3, names Johan Salvius; already corrected in
  NOTES). R4330: P1 archive cover sheet, P2 first page, P3 address leaf, P4 second page with date and signature.
  R4331: P2 first page, P1 its continuation, P3 closing lines (date 2 Dec 1631, signature), P4 a postscript leaf.
- The only decipherment of the time is the interlinear glosses, already used to rebuild the key. They were re-read
  on the crops: several readings in `bremen_transcription.txt` change (`Gr:` not `Dr:`, `Gronsfeldische`,
  `Reynacher` not `Regimenter`, `veste zuversicht`, `Unserige sehen`, `nicht mutiger`, `Tillische`, `Zell` over 27,
  `dem accord mit begriffen` not `kein accomodo`, `vergönnet`, `herab`?, `Dümeny`, `Obr` not `aber`).
- Print: one web search (Johann Friedrich, Salvius, 1631, Reinach, Gronsfeld, Neuenburg): no edition of these letters.

## 2. Read on the photographs

Crops of every line at about 2x (`research/reading_audit/b33_br_crop.py`, scratchpad `reread/crops/`). The phone
photographs are the limit: 2448 x 3264, the hand a fast Kanzlei cursive; 0/6, 3/7, 5/7, 2/7 and 4/9 are not always
distinguishable.

**Clear text.** Re-read throughout; many `?` resolved and several misreadings corrected (R4330 *Wir zweiffeln nicht*
not *Wir haben nicht*; *so 4. eilend zugeschicket werden möchte*; *Wan Wir dan berichtet werden*; *ob solte 3. von 11.*
(the "F." and "U." of the transcription are the numbers 3. and 11., glossed *Landgraff [Hessen]* and *Kön:*);
*nunmehr unverlengt*; *wie itzo uns bericht bekombt*; *Demnach ist*; R4331 *Wir setzen in keinen zweiffel*;
*seidem nun auch die [?schantze] Burg*; *so thut doch [Reynach]*; *mit dem ersten*; *so viel man nur zum
fodderlichsten in eil mechtig sein kan*; *Und thun demnach*; *versprochener massen*; postscript *haben Wir gnädigst*,
*Daran geschicht Uns zu [?gnedigem] gefallen*). Words still uncertain are marked `[?word]`.

**Figures.** 23 label corrections (`bremen1631_corrections.tsv`), each read on the crops; eight rest on a look-alike
digit pair where the photograph is ambiguous and the gloss decides (see the tsv, column look-alike). The cipher words
with their corrected groups are `bremen1631_aligned.txt`, which serves as the corrected transcription of the figures.

**Key.** Unchanged. No value was altered; every correction is a reading of the figure, not a key change.

**Name numbers** (written with a point): 4 = wir/uns (glossed *Uns*, *Wir* several times), 5 H. Christian, 7 H. Georg,
17 Tillische, 27 Zell, 32 Minden (*Bistthum Mind.*, and *Mind* over 32 in R4330), 59 Salvius / Ihr, 83 guter: all from
glosses. Read with doubt from glosses: 3 Landgraff (Hessen), 11 Kön:, 75 conjunctio(n) (rendered *[?conjungiren]*),
81 Unglück, 42 Stad(e). Unidentified: 18, 19 (gloss *stark: Colonien:* not understood), 31, 82 (twice glossed
something like *Hauss*, does not fit), 86.

**Clerk's slips.** Ten cipher words are one or two letters off their word (*widersant*, *scheunigen*, *sarck*,
*seunigst*, *succus*, *anzhal*, *assistece*, *assistenie*, *verhaden* with its *n* struck, *latd* for *Stadt*); the
gloss over each gives the word, and the reading follows the gloss (`|g` in the aligned file).

## 3. Reading and word check

`research/reading_audit/b33_br_build.py targets/riksarkivet1628`: 132 cipher words, 118 equal to their decode, 10 gloss
words over a slip, 4 holes, 41 name numbers; 0 cipher words whose reading differs from the figures without a mark. The
clear words come from the photographs; supplied words: none (holes are marked `[...]`).

| | clean-sentence share |
|---|---|
| before | no reading body; `_check_reading.py` on `bremen_decoded.txt` 0.477 |
| b17 plain (`LANG_=de`) | **0.600** (42/70), hole rate 0.113 |
| b17 `HOLES=1` | **0.843** (59/70), hole rate 0.065 |
| `_check_reading.py --file` (header and notes included) | 0.52 |

The plain figure falls on period spelling the German list does not know (*erwehlter, vernemmen, palt, müglich,
gnedig, troupen, Dumeine, fodderlichsten, dörfften*). Reader's judgement: the sentences of R4331 and its postscript
hold except the opening of the postscript; in R4330 the first paragraph (*ob solte [3] von [11] ... westpfelische
[...]. Und [?daro] nicht ...*) and the sentence *dadurch [3] [18] [82] gehen* do not build. Look-alike letters: 8 of
about 900 cipher letters (0.9%).

Verdict: read (grade B): above the explicit-hole bar, sentences hold through most of both letters.

## Open

- R4330 *westpfelische [...]* (23 34 81 22 73 80 21, *tortert*) and the clear words around *[?daro] nicht [?ab] [?oben]*:
  blocker **illegible** (phone photographs; a better image could settle the digits).
- Name numbers 18, 19, 31, 82, 86 and 42 in R4330: blocker **no-key-material** (no gloss of the time names them; no
  nomenclator sheet on DECODE).
- Uncertain clear words (`[?…]`, about 30): blocker **illegible** at the resolution of the photographs.
