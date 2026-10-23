# Guillaume Ancel, Vienna, to "Monseigneur", October–December 1577 — BnF Cinq Cents de Colbert 398 pp. 525–565

Status: in progress (21 Oct 2026). A contributed reading (Harumi-Matsuba, issue #53), made and cross-checked by AI
only. Our dictionary measure puts 95.4% of the cipher tokens inside French words, but nobody has checked the
transcription by eye against the manuscript beyond the three lines sampled here, 29 of 125 lines carry the
contributor's own "conjecture or unclear syntax" mark, and most code words are unexplained. The read bar is not met
on the evidence in hand; the work owed is a human check of the transcription and the doubtful lines.

**Outcome: read with known key, read in part, contributed.** Key: Satoshi Tomokiyo's reconstructed table "Vulcob
and Ancel's Cipher (1575-1584)" (Cryptiana, `code/frencheastern.htm`, 15 Mar 2026), which he says "will allow
reading undeciphered letters" of this volume, with additions by the contributor checked on pages that carry a
contemporary decipherment. Reading, transcription and checks: Harumi-Matsuba, GitHub issue
[#53](https://github.com/dbourdeau/cyphersolver/issues/53) (20 Oct 2026), repository
https://github.com/Harumi-Matsuba/vulcob1575-public (CC BY 4.0 data, MIT code), done with Claude Opus 5.5 /
Sonnet 5.5 (transcription, decoding, word division) and OpenAI Codex (independent transcriptions). This project
fetched the files, re-measured them with its own language models and spot-checked three lines on the Gallica images.

## The documents

BnF, Cinq Cents de Colbert 398, "Recueil de lettres originales sur les affaires d'Allemagne", Gallica
ark:/12148/btv1b525218133 (1,022 views). Letters of the French residents at the Imperial court, Jean de Vulcob
(1575–76) and Guillaume Ancel (1576–78, 1584). Most cipher passages carry a contemporary decipherment in the left
margin; these do not:

| page | Gallica view | letter | cipher tokens (measure.py) |
|---|---|---|---|
| p. 524 end – 526 | f558–f560 | 22 Oct 1577 (heading on p. 523) | 930 + 538 |
| p. 539 | f573 | 2 Nov 1577 | 197 |
| pp. 561–563 | f595–f597 | 14 Dec 1577 | 739 + 856 + 562 |
| p. 565 | f599 | 21 Dec 1577 | 563 |

p. 570 (one line, 26 tokens, f604) turned out to be deciphered in the last margin line of p. 569 ("… quil ny
reussiroit(?) peu ou point de proffit"); the key output agrees. The addressee is not identified: the letters open
"Monseigneur" (p. 523, f557, seen here), not "Sire", so not the King himself; the volume holds letters to Charles IX,
Henri III and Catherine de Médicis and their ministers. The court is at Vienna (p. 523: Matthias left at night by
coach for a castle on the Danube on the road to Linz). Sender attribution to Ancel follows Tomokiyo's list and was not
checked on the signatures by the contributor or here.

## The key

Tomokiyo's table drawn as symbols: two to four homophones per letter (4, 7, α = a; ω, π = e; ∂, μ = i; δ, ♭ = n;
cross, ɮ, ∞ = o; β = r; △, T = t ...), double-letter signs (ss, tt, pp, rr, mm, nn, cc, ff, uu), and a small
nomenclature written as letter groups or signs (ucl = est, ros = pour, plus = que, guod = guerre, VM = Vostre
Majesté). Words and names are hidden in plain-letter "code words" (saturnus, Juno, my, my3 …) mixed with plain-letter
nulls. Contributor's additions (OPEN.en.md §1): m-shaped double sign = uu (one margin instance), the flat L-like sign
= g, the crossed q = ff, box-q = nn, a lone c = null; all from context or from the p. 33 margin.

Code words checked against contemporary margins (contributor, OPEN §3): saturnus = l'Empereur (p. 258), Juno = le Roy
d'Espagne (p. 440), my = qu'il, my3θ = qu'ilz (p. 258, p. 321), pur bellum = l'Electeur palatin, ucb+ … = l'Electeur
de Saxe (p. 33), principalem = et principallement celuy. Open: manua/manue (a person), mare, grinter, totum (l'Empire?),
nez/mez, bel, mim, Mitte; probable nulls fec, sec, sanc, sane, pome, estre, toe, vib, roc, ar, puis, x.

## What the contributor did (contributed/METHOD.en.md)

1. First transcription in symbol names from enlarged tiles (Claude Sonnet 5.5; p. 539 Claude Opus 5.5).
2. Codex cross-check transcription from line images (no key, no values); disagreements adjudicated on crops by Claude
   Sonnet 5.5 in two rounds; 15 image-based changes that made non-words were put back by context and marked "?".
3. Independent Codex transcriptions after the transcription was fixed (three runs): value agreement 95.2–96.1% over
   the seven pages, lowest page 88.8% (p. 565).
4. Shuffled-key control (1,000 shuffles, wordfreq French trigram model): 0/1,000 on every read page.
5. Calibration on two pages with a margin decipherment (p. 258, p. 285, Vulcob 1576), processed blind: 85.9% letter
   agreement against a five-reader majority reading of the margin (81.8% against a single adjudicated reading).
6. Key output and word division per line (contributed/READING.en.md, marks ◎ reads as is / ○ one or two symbols
   corrected by context / △ larger conjecture).
7. Prior-work check by a separate Claude reader (contributed/PRIOR_CHECK.en.md): nothing found; Fontvieille 2024
   works from the interlinear decipherments of Vulcob's 1570s letters and does not reach these passages (conference
   report); Labouchère 1923 summarises only the clear paragraph of the 22 Oct letter.

The contributor says plainly that no human has checked the transcription.

## What this project checked (21 Oct 2026)

- Files copied into `contributed/` (key, final transcriptions, key output, reading, open points, method, prior
  check, calibration decode and margin files, their `vk.py` and `calib.py`); `contributed/ATTRIBUTION.md`.
- `measure.py` → `measure.txt` (their key read from `vk.py` with `ast`, their code not run except `calib.py`, read
  first, on their calibration files):
  - tokens on the seven pages 4,385 (4,275 symbols with a key value, 18 unreadable, 92 plain-letter groups, of which
    41 are checked code words). Share given a value: 0.984 (symbols + checked codes).
  - fr-1530-despatches (order 5, no spaces), per character: real key −1.81 to −2.29 per page; median of 20 shuffled
    keys −6.26 to −6.62. The text is French; the shuffled keys are noise.
  - Coherent share: the key output segmented into a 16th-century vocabulary (fr-1520s-diplomatic + Henri IV letters,
    20,298 words): 95.4% of tokens fall inside words (pages 91.9–96.8%), against 50.0% for shuffled keys. The measure
    is lenient (a mis-transcribed sign inside a common word can still be covered), so it is an upper bound on sense.
  - Calibration recomputed with their `calib.py` on their files: p. 258 339/398 (85.2%), p. 285 133/158 (84.2%),
    both 472/556 = 84.9% (they report 469/546 = 85.9%).
  - Their own marks: of 125 reading lines, 27 ◎, 69 ○, 29 △.
- Spot-check on the BnF IIIF images (openapi.bnf.fr, 2400 px; images not kept): p. 525 lines 9–10 (f559) and p. 565
  line 5 (f599), compared sign by sign with `contributed/transcription/`: 126 signs, sequence and count agree on all
  three lines; on p. 525 l. 9 two ∂/δ (i/n) choices could not be told apart at this resolution and are settled by
  context ("apeine", "encetellement"), as the contributor notes for that pair. The three lines decode to
  "…encetellement que apeine pouuoit il faire un pas / hors de sa chambre sans le congé d'iceluy seigneur…" and
  "…elle solliciter principalement le marquiz de Varemb[on]…". Also looked at p. 523 (f557), the clear opening of
  the 22 Oct letter: "Monseigneur, Comme la negotiation du Sr de Malstet envoyé depuis un mois en ça de la part des
  Estatz du pays bas vers l'Empereur …", as the contributor gives it.
- Cross-link: George Lasry's 1573 Charles IX → Vulcob letter (BnF fr. 3318, `targets/vulcob1573/`) was compared by
  him with a key in this volume (14 shared letter forms); whether it is the same cipher was not established here.
  Tomokiyo says Vulcob's letter of 2 Aug 1572 (BnF fr. 18989) uses this cipher.

## Prior work

- Tomokiyo, frencheastern.htm (15 Mar 2026): key and list of letters; no readings. He lists p. 525, 539, 561, 565, 569
  among Ancel's letters (561/565/569 in brackets).
- D. Fontvieille, "Du bon usage du chiffre par les ambassadeurs … Jean de Vulcob … (1570–1576)", Heidelberg colloquium,
  11 Apr 2024 (proceedings announced in Zeitschrift für Historische Forschung, not seen): Vulcob's correspondence from
  the interlinear decipherments; per the H-Soz-Kult report, not Ancel 1577.
- G. Labouchère, "Guillaume Ancel, envoyé résident en Allemagne", Revue d'histoire diplomatique 37 (1923): clear text
  only.
- Not checked by anyone: DECODE document lists (the catalogue has no Colbert 398 record), Lasry's unpublished reports,
  Google Books/HathiTrust full text.

## Content (contributor's summary, checked against the key output only)

22 Oct: Archduke Matthias's flight to the Low Countries; Ancel thinks the Emperor [saturnus] will deny any part in
it: the young prince could hardly step out of his room without his brother's leave or leave the castle shut at night.
2 Nov: the Emperor does all he can to persuade the Spaniards it happened without his knowledge. 14 Dec: Varambon,
sent by Don John, has waited three weeks for leave to levy troops; Borgia says the Emperor must back his brother in
earnest, as the Catholic King will defend his right; the Estates will hardly grant extraordinary aid. 21 Dec:
Varambon back from Archduke Charles's court with nothing; the Emperor waits for the King of Spain's [Juno] answer.

## 23 Oct 2026: verification 3 (explicit-hole score)

The v3 sweep scored the four letters on `contributed/READING.en.md` (the table with the key output and the reading side
by side, 0.178) or on the raw key output (p539, 0.2): a false alarm. The reading column is now in running text per
letter in `texts/<doc>_reading.md` (`research/reading_audit/v3a_ancel_write.py`: hyphenated line ends joined, the
probable nulls of OPEN.en.md section 3 dropped, saturnus/Juno/my/my3/my3θ written as resolved codes since margin
decipherments confirm them, other code words left as holes, the contributor's parenthesised letters bracketed as
holes). Explicit-hole scores: p525-526 0.857, p539 0.75, p561-563 0.75, p565 0.75 (plain 0.79, 0.75, 0.68, 0.58).
All four keep read; the profile entries now point `reading` at these files. Still unchecked by a human against the
images (OPEN.en.md section 5), as before.

## Remaining gaps
- Transcription of all seven pages not checked by a person (AI transcription and AI adjudication only; 3 of 125 lines spot-checked here) - blocker: open-codes; workable: an eye check of the transcription against the 2400 px images, starting with the 29 lines marked △
- Code words manua/manue, mare, grinter, totum, nez/mez, bel, mim, vost, mesme, and probable nulls (fec, sec, sanc, sane, pome, estre, toe, vib, roc, ar, puis, x) - blocker: open-codes; meanings need further instances in the margin-deciphered letters of the volume (pp. 33-501)
- Look-alike pairs decided by context (3/ʒ = m/r, p/φ = f/m, qa/al = q/a, cross/4 = o/a, 9/q = d/l, ∂/δ = i/n), shown as capitals in the key output - blocker: open-codes; needs the eye check above
- p. 539 l. 2-3, p. 561 l. 1-4 and 18-19, p. 562 l. 25-26, p. 565 l. 9 and 15-16, p. 526 l. 9-10 and 13-14 (syntax unclear around code words or unreadable signs) - blocker: open-codes
- Line ends lost in the binding shadow on p. 562 - blocker: needs-physical-access; the Gallica scan stops at the gutter

## Escalation
- [x] siblings: every Vulcob/Ancel page in Tomokiyo's list viewed by the contributor; p. 570 found deciphered in the p. 569 margin; margin-deciphered pages used for calibration and code words
- [x] clear-pages: the contemporary margin decipherments of pp. 33, 258, 285, 321, 440 used; none exists for the seven read pages
- [x] known-keys: Tomokiyo's Vulcob-Ancel key is the key; Lasry's fr. 3318 comparison noted
- [x] print: Labouchère 1923, Fontvieille 2024 (report), Cryptiana, cyphersolver, GitHub searched by the contributor; nothing prints the cipher passages
- [x] key-rebuild: contributor added uu, g, ff, nn, null c and seven code-word meanings from the margins
- [n/a] retry: no new key material since the contributor's last pass (20 Oct 2026); the remaining step is a human eye check, not a decoding retry

## Files
- `contributed/`: the contributor's files as fetched 21 Oct 2026 (see `contributed/ATTRIBUTION.md`).
- `measure.py`, `measure.txt`: this project's re-measure.
- Page: `docs/ancel1577.html`; crops `docs/ancel1577_*.jpg` (BnF via Gallica/IIIF).
