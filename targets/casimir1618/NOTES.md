# Ernst Casimir's cipher keys, KHA A23-311 (1590s-1627)

Status: in progress (keys inventoried; the one ciphertext, scan 027, not yet read)

## Source

Koninklijk Huisarchief, The Hague, A23-311, "Stukken met sleutels voor geheimschrift gebruikt in brieven met diverse
correspondenten", 1618-1627 and undated; 97 scans fetched through the Koninklijke Verzamelingen rendition API
(`scan_ids.json`; `img/` git-ignored). Cover: "Verschiede Cyffers door Graaf Ernst Casimir en Syne Hoogh. Officieren
en Ministers gebruickt, onder andere ook die van de Koning van Denemarken en den Prins van Orange". Found by the
Nationaal Archief sweep, KHA lead K2.

## What it holds

`inventory.md` (made by a subagent, 24 Oct 2026; several cursive readings marked "?"): about 26 distinct keys.
Despite the catalogue's 1618-1627, a large group is from the 1590s Frisian war (Eusum, Cnoop, Vernou, Cornput,
Verdugo). Dated keys 1618-27: Utrecht Dec 1618, Casembroot 1623, Justinus van Nassau 1624, Prince of Orange
(Frederik Hendrik) 1626, Obrist Limbach 1626, Graf Solms in Danish service 1627; a cover-name code (Maccabaeus = Ernst
Casimir, Numa = King of Denmark, Tullius = Althusius). Thirteen keys use numbers (ranges in `inventory.md`).

## The ciphertext (scan 027)

Willem Lodewijk of Nassau, stadholder of Friesland, Leeuwarden, 5 April 1594, to an unnamed officer: clear Dutch with
about a dozen cipher runs in Greek-like signs. It uses the word signs of the 028 key (circled sign = *staten*, barred
sign = *soldaat*), but the 028 alphabet applied straight does not give Dutch; the letter itself says the recipient
found "onse laetste cyffer seer duncker" and so they kept the old one. Next: a sign-level transcription and a
substitution solve against Dutch (`lang` nl model), or a search of the other alphabets in the folder (028, 003, 016,
029) for one that fits.

## Matches to open targets

No ciphertext on DECODE or in the catalogue names Ernst Casimir, Willem Lodewijk or Frederik Hendrik. Candidates to
test the numeric keys against: Riksarkivet R4284 (Camerarius 1628), R4306 (1632), R4333-R4337 (Rusdorff 1628).
Not yet done.

## Solve attempts (25 Oct 2026)

- `cipher_027.txt` / `signs_027.md`: the cipher runs transcribed by a subagent with ASCII labels (9 runs, 262 signs,
  33 distinct; S01/S21, S18/S23, S10/S11 and S30, S31, S33 doubtful). Labels instead of the shapes themselves, because
  long runs of Greek-like characters trip the output filter.
- `solve027.py`: the 028 alphabet applied through the legend's look-alikes scores -6.0 per char (gibberish), so the
  letter is not in that alphabet as transcribed. Annealing a substitution with at most two signs per letter: with
  `nl-modern` -2.71, with the new period model `nl-1600` -2.28 (`solve_nl1600.log`); restarts land on different keys
  with near-equal scores and no run reads as Dutch. Not solved.
- Likely obstacles: 262 signs is short for 33 signs; some signs may be nomenclator words (the 028 key has word signs);
  the transcription has doubtful pairs. Next: re-check the doubtful signs at full size, merge look-alike pairs, try the
  other alphabets in the folder (003, 016, 029) once their sign rows are labelled, and anchor the anneal on likely
  words from the clear context (e.g. *staten*, *soldaten*, *Verdugo*, *Groningen*, place names of the 1594 campaign).

## Recheck and anchored solve (25 Oct 2026)

- `recheck_027.md`, `cipher_027_v2.txt`: doubtful signs re-checked at full size by a subagent. S30 deleted (stroke
  overlap), S31 -> S32, S33 -> S10, S24 -> S05; S01/S21, S18/S23, S10/S11 kept apart; one doubled pair at a crop edge
  removed; 259 signs, 29 distinct. Word-sign candidates: S28 (double circle) and S32 (barred circle; the 028 key's
  *staten* / *soldaat* shapes), taken out of the letter stream.
- `solve027b.py` (`solve_anchor.log`): 777 placements of likely words (staten, soldaten, Groningen, Verdugo, Coevorden,
  Steenwijck, vyant, leger, geschut ...), each fixed and the rest annealed against nl-1600. Best -3.13 per char, no
  readable stretch around any placement.
- Unanchored, on v2: nl-1600 -2.29, fr-1600-letters -2.31, de-modern -2.77: no language gives readable text.
- Reading: the runs are not a plain letter substitution as transcribed. Candidates: more word signs than the two
  identified (the 028 key has twelve month signs and two word signs), nulls, or a homophonic table with more than two
  signs per letter. A key from the folder that fits would settle it; the other alphabets (003, 016, 029) still need
  labelling and testing.

## Other alphabets in the folder (25 Oct 2026)

A subagent compared sheets 003, 016 and 029 with the letter's signs (`alpha_003.tsv`, `alpha_016.tsv`,
`alpha_029.tsv`; 1600-px images, not full size). None gives a letter-to-sign alphabet for these signs:
- 003: a shifted letter/digit alphabet (a = 5 ... k = a ... z = p) and numbered code signs 1-80; no match.
- 016: a number-writing table (1 to 100000) in crosses, bars and barred circles; barred circles loosely like S32.
- 029: the closest in style. A block of about 64 signs with a rule that a dot marks a word end, but no plain letters
  written above them; several shapes resemble the letter's S01, S05, S07, S08, S20, S21, S22, S26, S27. The rest is
  a PRVDENTIA keyword table and a pigpen alphabet.
Nothing could be decoded, so `test_alpha.py` was not run. Next: the 029 block at full size (look for a plain row or
the paired sheet that gives its values), and any other folder sheet with a dot-word-end rule.
