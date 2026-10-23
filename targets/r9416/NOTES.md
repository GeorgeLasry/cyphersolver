# A Bavarian servant to his duke, and a report on the Pressburg talks, c. 1533–34 (BayHStA KAA 4591 ff.262–263, DECODE R9416)

Status: in progress — f.263 now has a partial reading of the whole leaf (23 Oct 2026, r2h), kept decoded, not read beyond recto lines 11-16 (look-alike letters 3.9% unconfirmed); no write-up update yet.
**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): the f. 262 gloss reads on page B but not on page A ("..." and [?] in most lines), so f. 262 is *decoded, not read*. The f. 263 entry counts only recto lines 11-16 (excerpt note); fraction_read 0.06 unchanged.


**23 Oct 2026, re-read (REREAD_BRIEF, batch b32; `r9416/f262_reread_log.md`):** f. 262 is **read** (grade B). The
key was rebuilt letter for letter from the contemporary decipherment of page B (`r9416/f262_key.md`: simple
substitution with homophones and three code signs) and page A was read from its signs on the full-resolution
image, all 25 lines, including the unglossed A09-A11 ("Minkwicz und ander geferden halb durch Slesi ... auch nit
komen"); page B follows the decipherment. The signs correct the gloss transcription at A03, A13, A16, A18, A19,
A22 ("Bartlen von Eschelkamb", "die turcken bis in vier tausent stark", "feind schonen"). Score 0.852 on explicit
holes, 0.444 plain. Reading `r9416/f262_reading.md`, English `r9416/f262_en.md`. fraction_read 0.06 -> 0.352.

Split on 15 Oct 2026 from `targets/kaa4591/` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue entry 161
grouped fourteen ciphertexts of the Munich key volume KAA 4591 in at least six systems; R9416 is a record of two leaves
in two sign sets of their own. The other letters are different ciphers, each with its own page: System A′
([`targets/kaa4591/`](../kaa4591/NOTES.md)), Łaski's cipher ([`targets/kaa4591b/`](../kaa4591b/NOTES.md)), the Fulda note
([`targets/fulda1576/`](../fulda1576/NOTES.md)), R9367 ([`targets/r9367/`](../r9367/NOTES.md)), R9424
([`targets/r9424/`](../r9424/NOTES.md)) and R9319 ([`targets/r9319/`](../r9319/NOTES.md)). Work 21 and 30 Sept 2026 (Claude
Opus 5) as part of kaa4591; `r9416/` moved here unchanged; the solver `anneal.py` stays in `targets/kaa4591/` (also used
on R9424 and R9367). The `de-1500s` language model in `lang/` was built for this leaf.

The record keeps two parts in one entry (`outcome.parts`), because the two leaves are filed as one DECODE record and
the f.263 report reads as the enclosure of the f.262 letter; each part has its own method and README row:
1. **f.263 (pp.3–4)**, the report on the Pressburg talks: key recovered from ciphertext-only, partial (primary part).
2. **f.262 (pp.1–2)**, a servant's letter to his duke: read from the existing (contemporary interlinear) decipherment.

Images: DECODE, login; not public domain, kept untracked; the page shows none.

Outcome: **key recovered from ciphertext-only (f.263), read in part**; f.262 read at the time, its gloss transcribed in part.

## R9416 pp.1–2 (f.262) — read at the time

A Bavarian servant to his duke, "eritags nach Jacobi" (Tuesday after 25 July): troops in Austria and Styria, the
Italian and Spanish foot ("walischen und spanischen knechten") to move through Styria and by the Danube into Hungary;
he asks for seven years' pension and the Oberrichter post at Straubing. The leaf is glossed over every
line by a hand of the time; the gloss is faint and is transcribed in part (`r9416/gloss.txt`, photos rotated 180°;
"..." illegible, [?] uncertain). The cipher signs of f.262 were not transcribed: the gloss is the reading.

## R9416 pp.3–4 (f.263) — broken from ciphertext only

3,150 signs, 661 words, word-separated, ~23 frequent signs; 'io' always together (treated as one sign). The
constrained annealer (`targets/kaa4591/anneal.py`, homophone caps) with the new `de-1500s` model (Deutsches Textarchiv prints
1472–1609, added to `lang/` for this target) gave running German on the first run: "…uon beden kunigen zu entlicher
handlung gen Pressburg gesetzt… der tag zu Pressburg erfolgt ist… mit grossem pomp… dem turkischen kaiser… tribut…
zu geben…". The faint interlinear gloss on the first lines of f.263 ("nunmen bag uon beden kunigen zu entlicher /
handlung gen bresburg gesetzt") agrees with the solver's text word for word, which confirms the break independently.

Working decrypt (solver key, before the look-alike split; `r9416/decrypt_f263.txt`; corrected transcription
`r9416/p34_v2.txt`): the report of a Bavarian agent on the Pressburg negotiations between "beden kunigen" (Ferdinand
and John Zápolya) and their commissaries; a Turkish embassy; "der Emrich beeche" (Imre Czibak) offering the Sultan
tribute and "tausent tucaten"; "den hern Griti abgefertigt" (Alvise Gritti, killed Sept 1534) — so c.1533–34. The
cipher (sign codes f/z/j, H/K split in v2) is a homophonic simple substitution; codes "der d", "der g", "der h" are
persons (probably Ferdinand, Gritti's party, the Hungarian king). State: read in part — running German with local
errors; a clean reading needs the v2 transcription re-keyed and the 'y' sign split.

**30 Sept 2026 — recto lines 11-16 read clean** (to fill the gaps in the quotation for Lasry's list;
`r9416/reading_p3_11-16.txt`, word by word with grades). The v2 transcription was re-keyed by hand and every word
checked on the image; lines 11-12 agree with the faint contemporary gloss, which runs further down the page than
"its first lines" (g11: "das aus den tag zu bresburg erfolgt ist dahin auch"; g12: "des Ferd tail ... mit grossem
bumbb kummen sint auch"). The split the notes asked for, on these lines: v2 `z` is two shapes, the one-bar zig-zag
(e) and a two-bar dagger (s: "daraus", "Bresburg", "ist", "grossem", "sich", "das", "Fasnacht"); `b` covers d and l.
Normalised: "... daraus der Tag zu Pressburg erfolgt ist, dahin auch des [Ferd.] Tail mit grossem Pomp kummen
sint, auch volmechtigen Gwalt anzaigt, und sich zu beden Tailn entliche Vertrage versehen. Es hat sich aber
zutragen, das am Ertag in der Fasnacht von dem turkischen Kaiser ain treffliche Botschaft ankummen ..." [Ferd.] is
the code sign g read from the gloss (faint; "Fed" possible). Three signs after "Tail" (circle with dot, I, closing
curve) are passed over by the gloss and are not rendered. Lines 17-19 read in outline "... welcher dem [T] ain
Brief vom Kaiser bracht hat, welcher in Latein transferirt ist, desselben Copei ich E. F. G. hiemit schick";
"mit vy fngioDDio" on line 17 (perhaps "mit ir Scheffe[n]") is not settled. The rest of f. 263 is not re-keyed.

Measured: `signstream.py` → `r9416/signs_f263.txt`, 3,313 transcription codes on f.263 (v2, look-alike splits and
doubtful signs included; the 3,150 above is the count before the v2 split). `mk_validation.py` aligns the hand-keyed
lines 11-16 sign by sign (225 signs, 199 read; 6.0% of f.263 read clean, a lower bound) and writes `validation.tsv`.

**23 Oct 2026, r2h (REREAD_BRIEF; `r9416/f263_reread_log.md`): f. 263 re-keyed in full, kept decoded, not read.**
- The f. 262 key was tried on f. 263 and does not apply: on the full-resolution images the two leaves use different
  sign sets (f. 262 figure-eight g, ♀/9 e, triangle d; f. 263 open square n, daggers, `io`, triangle f).
- f. 263 has its own contemporary interlinear decipherment, faint, over recto lines 1-12 and the last verso lines (not
  only the first two lines): `r9416/f263_gloss.txt`. It writes "fg" over the hourglass X (= E. F. G.), "Khö" over the
  barred T (the King, by the context Zápolya), "Ferd" over g.
- Every line (recto 39, verso 43) read on its crop from the v2 labels decoded with the extended hand key
  (`r9416/f263_key.md`, `research/reading_audit/r2h_dec263.py`): `r9416/f263_reading.md`, English `r9416/f263_en.md`.
  New: K serves k and b, so the old "Kreekurg/Krakau" is **Bresburg** (r22, r24, v36); the embassy came "mit vij scheffe";
  "Emrich Besche" offers tribute "und darzu das ganz widisch lannt, welches doch nit sein ist" and is to have [?hundert]
  tausent tucaten; on the verso the King dispatches Gritti, the writer (always called to the King's negotiations) has
  both dukes included through an article in [Ω]'s instruction, the commissioners are recalled from Pressburg; the last
  line is **"datm ofen den 12 marcij"** (Buda, 12 March, the month in clear).
- Score (body): explicit holes **0.775 (55/71)**, plain 0.465. Look-alike letters: 117 of 2,738 (4.2%) rest on the
  second value of a multi-valued sign chosen by the word (z e/s, b d/l, p b/w, K k/b), 108 (3.9%) outside the glossed
  lines (`research/reading_audit/r2h_lookalike263.py`); spot checks do not separate the e and s daggers consistently and b
  is one shape for d and l. Above the 3% limit with nothing to confirm them, so the leaf beyond recto 11-16 stays
  *decoded, not read*; fraction_read 0.352 -> 0.353 (measured counts).

Closed 23 Oct 2026: f.263 person codes "der d", "der g", "der h" from the gloss (X = E. F. G., T = Khö. the King, g = Ferd.); +L and Ω stay open (below).

## Remaining gaps

- f.263 beyond recto lines 11-16: letters on the multi-valued signs (b d/l, z e/s, p b/w, K k/b) chosen by sense, 3.9% of the reading's letters - blocker: no-key-material; 23 Oct 2026 (r2h) the whole leaf was re-keyed line by line on the full-resolution image (`r9416/f263_reading.md`, 0.775 explicit-hole share), but the contemporary gloss covers only recto 1-12 and the last verso lines and there is no print to confirm the rest.
- f.263 codes +L (6x, beside Ferd.) and Ω (7x), the dotted-circle cluster (r12, r21, r34), and the groups r08-r09, v27-v28, v38-v40 - blocker: no-key-material; no gloss over them, values tried with the extended key 23 Oct 2026.
- f.262 code signs X (3x), ⊼ (2x) and a G-sign (2x), the first group of A04, the end of A03 and one sign in B01 - blocker: no-key-material; no gloss over them (the gloss skips the B09 G and the B12 X); the rest of f. 262 is read from its signs, sign-label transcription `r9416/f262_signs.txt` (23 Oct 2026). Page B B08-B15 checked sign by sign 23 Oct 2026 (closed).

## Escalation

- [x] siblings: the volume's other ciphertexts and keys (R9423 register, System A′, System B, R9324) checked; none is the f.263 or f.262 sign set
- [x] clear-pages: the gloss on f.262 transcribed, and (23 Oct 2026) used to key the signs: f. 262 page A read from its signs; the faint gloss over f.263's first lines agrees with the solver's text
- [x] known-keys: the volume's keys do not fit either leaf
- [x] print: web search for KAA 4591 / the Pressburg talks report found no edition
- [x] key-rebuild: constrained annealing with de-1500s (first run); v2 look-alike split; lines 11-16 re-keyed by hand
- [x] retry: 23 Oct 2026 (r2h) the rest of f.263 re-keyed line by line on the full-resolution image with the extended key and the newly transcribed gloss (`r9416/f263_reading.md`); the f. 262 key tried and ruled out (different sign set)

## Assumptions for George's review

- f.262 and f.263 are kept as two parts of one entry (one DECODE record, the report as the letter's enclosure), not
  as two entries; they are different sign sets.

## 23 Oct 2026 — verify sweep (reading audit v2): f. 262 sign labels saved, kept read
- The b32 reading of f. 262 had no sign-label transcription, so its decode could not be re-run. Both pages (40 cipher
  lines) are now transcribed sign by sign from IMG_R9416_I44531_P1/P2 (re-fetched with the project cookie, turned 180
  deg, read in full-resolution strips): `r9416/f262_signs.txt`, 1,498 signs, labels listed in its header. Re-decoded with
  `f262_key.md` by `research/reading_audit/v2_r9416_f262_dec.py`.
- Word-by-word alignment with `f262_reading.md` changed 17 words to what the signs give: A02 zuziehen (was [?zuzrehen]),
  vertraue; A03 unter (was "under"); A04 gewornet; A07 bot (messenger; was [?boit]); A08 "das ich es sein solt" (was
  "es lern solt": the rumour was that it was he); A10 polen (was [?belen]); A12 italische; A16 eschelkamb; A18 wolt (was
  welt); A21 gestolen (was [?gestalten]); A23 verner (the unread word before "gnediger her") and [?gefallen] (an 8 where a
  should stand); A24 mag (was [?wag]); B05 guldin; B11 [?dinst]; B14 unterteniglich. Added from the signs where the gloss
  is silent: B09 "an [G] von eurn" (a code sign: the recommendation is addressed to someone) and B12 "noch [X] die zeit her"
  ("weder wirtenberg noch [X] die zeit her": Württemberg). English updated to match.
- Score of the reading body: 0.852 -> **0.963 (26/27)** on explicit holes, 0.444 -> 0.481 plain (`v2_score.py`,
  `b17_score.py` HOLES=1 0.963). Look-alike letters: the P family (w/b/p) and the R/6 pair (r/m) chosen by the word,
  about 2-3% of letters. Kept read, grade B.
