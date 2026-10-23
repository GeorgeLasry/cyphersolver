# No. 66 re-read log (batch b23, 23 Oct 2026, Claude Opus 5.5)

Brief: `research/reading_audit/REREAD_BRIEF.md`. Result: **read** (`no66_reading.md`, `no66_en.md`).

## 1. Is there a text already?

- No DECODE record ids in `profile.json` or `arya/` (nothing to fetch with `b23_fetch.py`).
- Tomokiyo, `arya/src/francis.htm` §18 and Lasry's GL.htm (`targets/gramont1529/GL.htm`, "Gaspar Sormano's Cipher")
  list nos. 63-66 with the key image only; no decipherment of no. 63 or 66.
- The twin no. 65 (`n65_reading.md`) is the only contemporary text of the same letter. It was used as a check; every
  word of the reading is carried by no. 66's own signs except the bracketed ones.

## 2. Images

- IIIF `info.json` for f125: 8653 × 5877, maxWidth 8653 — the same master as `raw/full125.jpg` (8653 × 5877) used
  before. A 1600 × 400 crop fetched at `max` differs from the raw crop by 2 grey levels on average (re-encoding) and
  has the same sharpness. PNG is not served; WebP is the same image. **The IIIF full-resolution image does not beat
  the old capture; it is the old capture.** The old blocker "illegible, microfilm" is nevertheless wrong for this
  leaf: at 1.0-1.8× the 50-60 px signs are readable by eye, line by line.
- Helpers (all in `research/reading_audit/`): `b23_sormano_lines.py` (two-line strips, two halves),
  `b23_sormano_l3.py` (one line in thirds), `b23_sormano_slab.py` (zoom on a region), `b23_sormano_rows.py` (line
  centres from the ink profile), `b23_sormano_strips.py` (first attempt, band detection merged lines: abandoned).
  Crops saved under the scratchpad `reread\sormano\` only.

## 3. What was wrong before

`n66_transcription.md` f. 121r gives letter strings that make no words (e.g. "con dio i l io il di ir o d {dover}"),
and stops at f. 121v L20; f. 121v L21-43 and the eleven cipher lines of f. 122r were never transcribed. Re-read sign
by sign, every f. 121r run gives Italian (see `no66_corrections.tsv`): the first run is *con [Duca] per che
conclusion si facese secondo il desiderio di vostra maiesta*, not a garble.

## 4. Key values, with evidence (hold across the document)

| sign | value | evidence | status |
|---|---|---|---|
| crossbarred long-s | null | about 20 places, each a word only when dropped: *in (f)nome*, *vost(f)ra*, *s(f)ua*, *pos(f)serita*, *tal(f)*, *mi t(f)rovai*, *n(f)on*, *e(f)t*, *l'imp(f)resa*, *maies(f)ta*, *intra(f)r*, *trat(f)ar*, *satisfacese*… | adopted for no. 66; agrees with f. 123r (three nulls). KEY.md's "= e" (from f. 113r) should be rechecked; not changed here |
| Б (b-shaped, looped ascender) | rr | *ridu[rr]e*, *Fe[rr]ara*, *l'e[rr]ore*; no. 65 has the same sign in *ridu{B}e* and *le {B}ore* | adopted (3 + 2 contexts) |
| Ʒ with loop (large) | z | *speran[z]a*, *excelen[z]a*, *contente[z]a*; f. 115r *excelen[z]a*, *remonstran[z]e* | adopted |
| δı (second f form) | f | *afectionato*, *se gli feriva* ×2 | adopted; *[o]feriva* supplied |
| ⊬7 (V with long stroke + e) | Papa (code) | *col ⊬7 et la quasi ferma speranza*, *tratar tra ⊬7 et lei*, *sospeto si del ⊬7*, *componere le cose soe con ⊬7*; no. 65 transcription *col p{apa}(?)* | **flagged, sense only**: written [Papa] |
| curled saltire | ?Imperatore (code) | one context: *sospeto si del [Papa] come de ✗ … suoi nimici* | **flagged, sense only**: written [?Imperatore] |

## 5. Look-alike letters (a sign read as the value of a similar sign)

13 letters: bold ✗ read as t (x) in *stabilimento*, *alcunamente*, *dubitai* (3); Y/ɣ forks read with the other value in
*gloria*, *sul*, *sue*, *deba voler*, *dificile*, *dificulta*, *sian* (7); H read as o in *quanto* (1); 8-like sign read
as l in *stabilir le* (1); stroked Q read as r in *liberar* (1).

## 6. Alignment

Each reading word was checked against its sign string (`no66_corrections.tsv` gives the signs for every f. 121r run;
f. 121v and f. 122r were read the same way, strip by strip). Bracketed: [Duca] ×4 (◎), [Papa] ×4, [?Imperatore],
[o] of *oferiva* ×2, [?posterita] (figures *posserita*), [?quanto] (H/o), *la[ssar]* (clear-hand abbreviation).
Where no. 66 differs from no. 65 the figures were followed: *prefato* (no. 65 *deto*), *parente* (no. 65 *figliolo*),
*soa*/*soe*, *poco cedeva in alcun suo profito* (no. 65 *concedeva(?)*), *circa la cosa del regno* followed by two
nulls (the old transcription put ◎ there).

## 7. Score

`b17_score.py`, LANG_=it, reading body: before (n66_reading.md body, 《…》 as holes) 0.316 (18/57), HOLES=1 0.877;
after **0.753 (70/93)**, HOLES=1 **0.989 (92/93)**. The sentences hold; grade B (codes identified from context, one
look-alike-heavy family).

## 8. Failures

- Band detection by ink profile (`b23_sormano_strips.py`) merged lines (show-through, slope): replaced by fixed
  overlapping strips.
- Line centres from `b23_sormano_rows.py` are off by up to 70 px on the right half (the lines slope); zooms were
  re-cut by hand several times.
