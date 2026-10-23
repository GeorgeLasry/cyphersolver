# Re-reading log, R483 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b33)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R483_clerk.txt` merged the clerk's interlinear with the clear passages
line by line, the clear passages put at line ends out of reading order, with "?" doubts or alternatives on most
lines. Clean-sentence share before (`R483_clerk.txt`, whole file put under a `## Reading` heading, b17 `LANG_=la`):
**0.311 (33/106)** plain; `_check_reading.py --file R483_clerk.txt` 0.415. (The `HOLES=1` figure for the old file,
0.981, is not comparable: its doubts are written `word?`, which the scorer does not count as holes.)

## 1. Is there a text already?

- **DECODE record R483** (fetched logged in, `rec.htm` / `rec.txt` in the scratchpad `reread/R483/`): six images,
  one document (`DOC_R483_D2172_2172.txt`, EK's transcription of 2 April 2020: the groups, with the interlinear and
  clear text transcribed in `<PLAINTEXT>` / `<CLEARTEXT>` tags, heavily starred `*` and `?`), no comments, no
  attachments, no note of a printed edition. Status "Partially decrypted"; date given as 7 June (the leaf has 27).
- **The contemporary decipherment is the clerk's interlinear** over every ciphered stretch, already transcribed in
  `tr/`. Nothing else on the record.
- **Print.** Searched (web) for the letter's phrases (*Puncta Submissionis*, *Pacis Carolianae*, *Leopoli* 1711) and
  read the OCR of Thaly's *Archivum Rákóczianum* I/3, *II. Rákóczi Ferencz leveleskönyvei* 1710-1712 (MEK 18829,
  `18829_3.pdf`, 764 pp., downloaded to the scratchpad `reread/R483/print/`): grep for Mangol-, Spigel/Spiegel,
  Jablonsk-, Dukl-, Carolian-, Submission-, and every June-July 1711 dateline. **R483 is not printed there** (the
  register for June 1711 has Viszocka letters of 3-19 June and none of 27 June to an envoy). Related: no. 44 (spring
  1711), Rákóczi to **Klement**, about the fiscal wines Hegyi was to deliver to the King of Prussia's man and which
  were partly lost by Hegyi's defection: the same affair as p. 6 of R483 (*Hegyio*, *cellario regio*), which makes
  Mihály Klement, Rákóczi's chamberlain-envoy to Berlin and Holland, the likely addressee. Not checked: the
  Bercsényi volumes (AR I/6) and Thaly's other editions; the Festetics original was not looked for elsewhere.

## 2. Reading order and the clear passages, on the images

- `research/reading_audit/b33_rk_merge.py` walks each `C:` line and puts the next `|` segment of the `P:` line at each
  cipher run, the clear passages where they stand. On pp. 1-3 the `P:` lines are split per run; on pp. 4-6 they are
  not, so the split was made by hand from the key decode.
- `research/reading_audit/b33_rk_dec.py` decodes every run group by group with `R483_key_rebuilt.json` (values seen
  once marked `*`).
- `research/reading_audit/b33_rk_crop.py` cut each page into nine overlapping full-width strips (2120 x 370 px, native
  resolution) and zooms (1.2-2x) where needed; every written line of the six pages was read on these strips (p. 1 top
  on a separate crop, p. 6 below the postscript is blank), against the merge and the decode.
- What this changed (all in `R483_corrections.tsv`, 72 rows): many clerk doubts settled by the figures (*in* for
  *ni*, *ab inimicitiis* for *ab Armistitiis*, *inimicitias suas* for *amicitiis fidis*, *tranquillos reddat animos*,
  *sine mora*, *vix suppeditari potest*, *retinere nolle, sed cura Judaei cujusdam*, *domino Jablonski* for
  *Fablanski*, *custodiae hominis ipsius*, *cellario regio*); words built across a cipher and a clear piece
  (*Ta-Bella-rius*, *Copia-liter*, *an-nihil-arentur*, *ad-jura-ndi*, *con-ditiones*, *saep-ius*, *ad-inveniri*,
  *vi-duae*, *do-lente-r*, *de-gente-s*); clear words re-read (*Prout* for *Gerons*, *Et ipse-met*, *expresso*,
  *profecto sat dolenter*, *Spreta*, *firmiter*, *hactenus*, *superexistere*). One clerk omission restored from the
  figures (*juramento suo*, p. 2 l. 4). The clerk's two struck *Hungariae / Hungaria* (p. 3) are kept, because the
  cipher has them; his other struck words have nothing under them and are left out.
- No cipher group label was changed (the tsv lists readings of the interlinear and of the clear text), so no
  corrected `tr/` file was written.

## 3. What failed or stays open

- **P. 1 clear opening** (*Supponimus redditas jam … Vobis fuisse Responsorias Literas nostras ad … Vestras
  transmissas, et quid contineant, et annexis earundem abunde … -nistris*): a fast cursive the 2304-px image does not
  settle at 2x; five words open (marked). Not tried: a higher-resolution scan (MNL OL), which is the only way on.
- Doubtful words where the clerk and the decode do not agree and neither makes sense with confidence: *[?concludendam]*
  (decode co-n-c-ie-de-n-da-m), *[?remediationis]*, *de novo [?latis]*, *[?possidere]* (figures po-s-si-de-re; sense
  wants *providere*), *Sperabamus enim eo [?hacce] […] [?eos] [?teneri]*, *[…] millium* (p. 3 foot), *[…] Consilii
  nostri* (p. 6, group 478), *[?commisso]*, *domino Jablonski […]* (110 340 390). These are key-value gaps (groups seen
  once or not at all), not illegible figures.
- Tried and dropped: reading p. 1 l. 5 clear *nistris* as a word of its own (it is the end of a word broken over the
  line, still unread); *in effectu* (clerk, p. 4 l. 3), replaced by *profecto* from the same groups as p. 3 l. 4.

## 4. Scores

`R483_reading.md` body (b17, `LANG_=la`):

| | clean-sentence share |
|---|---|
| before (`R483_clerk.txt`) | 0.311 (33/106) plain; `_check_reading` 0.415 |
| after, plain | 0.141 (14/99), hole rate 0.312 |
| after, `HOLES=1` (explicit holes only) | **0.889 (88/99)**, hole rate 0.050 |
| `_check_reading.py --file` (whole file) | 0.237 |

The plain figure fails on the Latin word list, not on the reading: it rejects *sincere*, *ob*, *re*, *acceptare*,
*alliatis*, *dieta*, *libertatum*, *restitutionem*, *praescribunt*, and every chancery word (*quietantiis*,
*copialiter*, *assecurationes*); the old file scored higher only because its "sentences" were single manuscript lines.
The explicit-hole figure is the bar used, as the brief allows when the word list cannot know the language of the
text; 11 of 99 sentences carry more than one hole in ten words (p. 1 opening, p. 3 *Tirnavii* and *Sperabamus*
sentences, p. 4 *conservarent […]*, p. 5 *Jablonski […]*).

**Word alignment.** Every reading word was checked against the clerk's interlinear, the group-by-group decode or the
clear text on the image (the tsv lists every place where the reading departs from the clerk); no word is supplied, so
there are no `[word]` brackets. **Look-alike letters: 0**: the reading rests on the clerk's hand and on the clear
text; the key was used to choose between the clerk's alternatives or to correct him where his words do not fit the
groups, never to pick between look-alike figure shapes.

**Reader's judgement.** The sentences hold and translate (`R483_en.md`): the Szatmár treaty copy and the Palatine's
proclamation of Charles; why Rákóczi will not recognise a king proclaimed outside a free diet; the appeal through the
Tsar and the Polish Senate council; the conditions offered; the estates' letter to the widowed Empress-regent and the
Allies' insincerity; Pálffy's taking of Munkács; Transylvania; instructions to the envoy (if too ill to go on to
Holland, pass the matter on; send the views to Spiegel via Saxony; trust only news from Rákóczi); Ráday and the Polish
Grand Chancellor Jabłonowski; the wines left with a Jew; Hegyi's defection; the postscript on Mangold's instruments.

## Result

Read from the existing decipherment (the clerk's interlinear), with the clear passages read on the images and the
clerk's doubts settled by the rebuilt key; grade B (p. 1 opening and about a dozen doubtful words open).
