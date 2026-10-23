# R4625 re-read log (batch b06, 22 Oct 2026, Claude Opus 5.5)

## Is there a text already?

No. The DECODE record has no transcription or key; the seven images carry no interlinear or margin decipherment (pp. 2,
3, 5 checked on crops); Mírka 2012 read only R3811. read/SUMMARY_R4625.md (Sept 2026) is our own summary, used only as a
guide. The letter is undated and begins mid-sentence (p. 2); p. 7 is a covering letter.

## Image checks and transcription (read/R4625_corrections.tsv, 39 rows; tr/IMG_R4625_*.txt edited in place)

- The crossed long-s flourish transcribed `p` (key: null) is the #f-cross sign = ta after 27 on every page
  (Halberstatt, starck, Standt/Standen, zustandt, Stab, dreitausendt, tausent): relabelled `#f-cross` (22 places).
  Elsewhere the same flourish reads vi (proviant, privilegia, viel iahr) or nothing; left as `p`.
- `6 #z-tail` had been read `62 #z-tail` (tausendt, essen sie davon on the P5 image; tausent essen, geniesen, muesen by
  the same shape): 6 places.
- `6` for φ (z) in zu, herzog (3); "ob" and "besser", "Weilen", "khönden wir mit" are clear words (4); `61 6 w` is
  `6 16 w` = sein on the image.

## Key observations (proposals; key.json not changed)

- `9`: besides te, 7 places need vo: volck (P2 ×3), ein vormaur (P3), von weitem, von Halberstat (P6), vor dem
  nidersachsischen Crais (P7). The R3813 fork saw the same in "9 l c k" = Volck. At DECODE resolution the sign looks like
  the ordinary 9; a second, 9-like sign (or a homophone) for vo is likely. Printed [?].
- `m` after 29 = a: quando, quartier, a quarteriis (P3, P5); key null. Printed [?].
- `p` = vi where it is not after 27 (above). Printed [?].
- `α` = ve in "wir verlohren" (P6), not sa.

## Reading

read/R4625_reading.md (German/Latin), read/R4625_en.md. b06_align.py: 0 words not carried. b06_score.py (body only):
before, the deciphered runs alone were unspaced (audit: decoded, not read); after, clean share 0.42 (44 of 105
sentences), hole rate 0.18. Most failing sentences hold one or two real holes plus words the 1640s word list does not
know (Crais 30 times, Halberstat, Hazfeld, Latin phrases such as "consultius", "excludamur").

## Stays open

- Runs that do not decode into words although the figures are legible ("mehrers etgentedi serto", "an dilei ortten",
  "tecian", "eodem bi coCaesarem satequte bannieriam", "hungerlas listerten ... bunmiren", "diener tennich"): blocker
  is labour (a further image pass) and the key questions above, not the image.
- Latin on p. 5 with run-together groups.
- The eight clear lines at the head of p. 7 were never transcribed (clear text, not cipher).

Result: stays **decoded, not read** (0.42 < 0.60), with this partial reading.

## Second pass (22 Oct 2026, after the key update: 38 = d, Δ = nu, #dot = su, #s-long = ti, m = a, 9v = vo)

- Words now carried were unbracketed (quando, quartier, quartieriis, suprema, Artigleria, coniunction, resolution,
  conniventia et clementia, verfassung, stift, titubantes); the aligner flag (Halberstatttschen) fixed.
- 9 relabelled 9v (vo) in 9 places: darvon, volck ×3, voluimus, vormaur, von weitem, von Halberstat, vor dem.
- Image checks on pp. 2, 3, 5, 6, 7 (40 further rows in R4625_corrections.tsv, 79 in all): "lassen sterben" (6 z-tail and
  93), "nach consumiren" (86, not 80), "diener bin ich gewiss" (92), "der fructus" (100), "der groste" (line-head 9),
  "nimmer Bischof" (92), "an disen ortten" (6 31), "Halberstatt ist" (97), "si talibus conseliis voluimus uti"
  (crossed long-s = ta), "neutralitas" (one crossed long-s), "etliche", "gar zu ruinirt", "-sischen" (73).
- Clear text re-read on the image: p. 2 "sondern" (not vorkommen), "so sein dan"; p. 3 "Crais berathschlagung", "so
  sein"; p. 6 "muss ich es dahin gestelt sein lassen, und leben daheim", "solte sein", "wir verlangten khein frieden,
  sondern ain und den andern Standt", "khainer der weg hat", "und nit wir selbst", "wolle, sonst", and the date "Hamburg
  den 10. Febr. Ao 1639" (the memorandum is dated); p. 7 the eight clear lines of the covering letter (two words
  illegible) and "E. H. melden" (not wolden).
- Score (body only, b06_body_score.py): 0.42 → 0.522 (60 of 115 sentences), hole rate 0.151; aligner 0 flags.

Why it stays under 0.60: of the 55 failing sentences most fail on words the 1640s word list does not know rather
than on holes: Crais (12 sentences), Halberstat (6), Latin inside German sentences ("et", "ut", "si" count as holes
there), period spellings (khönden, vermuhet, genungsamb, unmoglich, werren). Real holes left: about 30 [...] and 25
[?word], mostly runs that do not decode although the figures are legible (listed in the reading's Notes), the crossed
long-s = vi (Salvius, proviant, privilegia, viel: not in the key), and the Latin of p. 5.

Result: stays **decoded, not read** (0.52 < 0.60).

## Third pass (22 Oct 2026, key pv = vi added)

- p → pv (crossed long-s read vi, key pv): privilegia, proviant, vil iahr, Salvius (P5) (4 rows).
- Image checks: "die kaiserliche armada" (84, not 87), "nos possumus" (the raised #dot = su before the struck group),
  "Halberstatt ist alle tag" (crossed long-s = ta), "der tacite von Kai. Maiest. empfangen" (crossed long-s = ta, 9v
  before the z-tail), "dess so einer zu hauss ... und sein zaun huete" (the sign d; no gap between the lines).
- Clear text on the image: "manco mal per noi" (Italian; not "manes"), "war dem ehe feindt, wer freundt seye", "Was den
  19. eiusdem khombt dises Augenblickh, ist khurz", "Der gast ist schon hinüber".
- Figures printed as written where the [?] was only a spelling question: esignierten (99 = e for de-), bloqurter,
  sarcker, lez estu, religui sunt armati.
- 92 rows in R4625_corrections.tsv in all.
- Score (body only): 0.522 → 0.603 (70 of 116 sentences), hole rate 0.141; aligner 0 flags.

Result: meets the bar narrowly (0.603); the sentences cohere through the memorandum and the covering letter. Open: about
20 [...] (runs listed in Notes, the Latin of p. 5) and 15 [?]; blocker is labour on legible figures, not the image.
