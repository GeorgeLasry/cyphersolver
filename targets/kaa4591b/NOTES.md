# Hieronymus Łaski's cipher (System B), BayHStA Kurbayern Äußeres Archiv 4591: four letters to the Bavarian court, 1529–1531

Status: in progress (23 Oct 2026: all four letters read as sentences; FLW and one owl word sign open; class kept read in part, see Remaining gaps)

Split on 15 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). This folder used to hold catalogue entry 162
("… to unknown recipient, 3 ciphertexts": DECODE R9403, R9414, R9415), three letters in three different ciphers. It
now holds the one key it shares with part of catalogue entry 161 (`targets/kaa4591/`): Łaski's graphic cipher, called
System B in the volume notes. The letters in this key are gathered here:

- R9322 (ff. 121–122), R9323 (f. 123), R9417 (f. 264), moved from `targets/kaa4591/` (catalogue 161), with the gloss
  key and its working files (`sysB/`);
- R9403 (ff. 226–228), already here (catalogue 162).

The other two letters of catalogue 162 are different ciphers, each with its own page: R9414 (Wardein, 14 Mar 1537,
homophonic system G) is [`targets/wardein1537/`](../wardein1537/NOTES.md); R9415 (18 Apr 1533, homophonic system L) shares
its key with the Sperantio file and moved to [`targets/sperantio1534/`](../sperantio1534/NOTES.md). The rest of
catalogue 161 is listed in [`targets/kaa4591/`](../kaa4591/NOTES.md) (System A′ and the other single letters).

Images: DECODE, login only (cookie in `targets/bordeaux/decode/cookie.txt`). DECODE's rights line reads "Publishing it is
only possible with the permission of the Archive"; no permission has been asked for, so the JPEGs stay untracked
(`targets/kaa4591/img/` in the main checkout) and the site page carries no image figures.

Outcome: **key recovered based on adjacent plaintext, read in part.** R9322 (96.4%), R9417 (99.1%) and R9403 (99.5%)
pass the read bar; R9323 (76.1%) does not, because of faint signs; together 1,184 of 1,243 words (95.3%,
`measure_sysb.py` + `r9403/decoded.txt`). Key state: recovered (21 letter signs; FLW word sign open).

**23 Oct 2026, re-read (REREAD_BRIEF, batch b20; Claude Opus 5.5).** R9417 and R9323 are now read (log
`sysB/R9417-R9323_reread_log.md`). Every file on the DECODE records fetched with the shared cookie: no attachments; the
only contemporary text is the faint gloss. **R9417**: the P2 image has 29 cipher lines, the transcription held 21; the
"m for a, e for r" slips were coding slips (on ll. 15-21 the two circles and the two crosses had been coded the other
way round from the glossed lines, where dotted circle = a, plain circle = m, plain x = r, starred x = e, the R9403
exchange). Lines 15-29 and P1 read at the image (`sysB/R9417_signs_b20.tsv`, `R9417_corrections.tsv`): Minkuics to
meet the dukes' envoys at Coburg in Saxony on 4 July, the roads were beset; the King of Poland's daughter: the match
"ita frigide incipit" while someone (an owl word sign) presses through Sigismund Herberstein for Frederick the Count
Palatine; the dukes should send with others to Charles V to hold back his brother from attacking King John; "Cracouie
sedecima die iunii. Lask. Scripsit manu propria". **R9323**: re-read word by word (`R9323_corrections.tsv`): l. 3
begins with the Ferdinand word sign ("concordiam inter [D] et [BIGX]"), Ƶ = q, the I-sign = b, the dagger = n; "si non
erit concordia quia peribit Boemia, quam Turce sicuti et Austriam consument"; two faint words of l. 10 unread.
Readings `sysB/R9417_reading.md`, `sysB/R9323_reading.md`, English `_en.md`. b17_score.py (la): R9417 0.250 on the
full word list, 0.893 on explicit holes; R9323 0.111 / 0.889 (the checker's Latin list lacks carissime, peribit,
arripere, the -cia spellings and the names). Words in letters that read: 1,307 of 1,307 (fraction 1.0).

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read**: R9322 and R9403
(continuous Latin, rare slips). **Decoded, not read**: R9417 (p2 ll. 12-21 and p1 carry systematic letter slips, m for
a, e for r, t for b, in most words) and R9323 (a doubtful sign in nearly every line). The 95.3% above counts words
with slips as read and is withdrawn as a reading figure; 69.3% of the words are in letters that read (861 of 1,243).

## The four letters

| Record | Folio | Date | Who | Read |
|---|---|---|---|---|
| R9322 | 121–122 | Buda, 24 Nov 1529 | f.121 Hieronymus Łaski to a Bavarian duke (with a copy of his letter to Count Palatine Frederick, imperial captain); f.122 King John of Hungary to Duke Ludwig of Bavaria | 429/445 words (96.4%) |
| R9417 | 264 | Kraków, 16 June [1530] | Łaski to the dukes' secretary "Waisenfelder" | 217/219 (99.1%) |
| R9323 | 123 | [1529–30] | Latin note to the Bavarian secretary (Łaski circle) | 124/163 (76.1%) |
| R9403 | 226–228 | Łask, 17 Sept 1531 (docket "anno 32") | Łaski to a councillor of the Bavarian dukes (probably Leonhard von Eck: inference) | 414/416 (99.5%) |

## The key (System B)

Monoalphabetic graphic substitution with a few word signs; key rebuilt from the interlinear glosses (153 aligned
word pairs; `sysB/key_from_glosses.tsv`): 3 i, X e, ⊕ s, U2 u/v, ⊙ a, N n, O m, M o, ⋇ r, HH t, W c/t, D d, ≡ p,
9 l, B b, Z g, Q q, ≐ f, † f, H h, XH x. Word signs from context: DAG = King John (Zápolya) ("non alio loco vult
habere [DAG] quam loco fratris sui", said of the Sultan), BIGX = Ferdinand ("concordia inter [DAG] et [BIGX]";
"ad oppugnandum dominia [BIGX]"), FLW = probably King John's title. Decoded text in `sysB/decoded.txt`; sign inventory
`sysB/signs.md`. In R9323 the dagger T reads n (dando, contra, comendet, sint, sunt).

In R9403 e and r are swapped (e = ⋇ starred x, r = X plain x) and some sign shapes differ. The raw decode of R9417 p.1
shows the same exchange ("feancie", "ceistiani" for francie, christiani), so the swap is a variant of the one key.

## R9322 and R9417 — Łaski and King John, 1529–30: read

- R9322 f.121: Łaski to a Bavarian duke, Buda 24 Nov 1529 (with a copy "ad illustrissimum dominum Fredericum imperii
  capitaneum"): King John followed the dukes' counsel; the Sultan, forced home by plague in his army, left John the
  kingdom of Hungary without tribute, fifty guns and a thousand hundredweight of powder, and will return next summer
  against Ferdinand's lands unless there is a concord; Łaski commends himself as the duke's servant.
- R9322 f.122: "Joannes Dei gratia rex Ungarie" to Duke Ludwig of Bavaria, Buda 1529: sends Lazarus the Jew as envoy.
- R9417 f.264: Łaski, Kraków 16 June [1530], to the dukes' secretary: letters of 12 June received; the siege army
  before Buda; concord best made through imperial princes; Nicolaus Min… sent to the King of France; the Sultan
  willing to receive in friendship whom King John names; asks for envoys to meet at Coburg in Saxony by (date) July.

## R9323 — note to the Bavarian secretary: read in part

`sysB/R9323_decoded.txt`: King John loves the Duke of Bavaria; Łaski wants concord between King John and Ferdinand,
for without it the Turk will consume Bohemia and Austria; he made a pact with the Turk that unless the estates of the
Empire provoke hostility by aiding Ferdinand …; the princes should not stir the Turks against themselves. Lines 4 and
8–10 are faint.

## R9403 — Łaski, 17 Sept 1531: read

Reading: `r9403/decoded.txt` (line by line, then normalised). Ruffus brought the dukes' letters on the 15th; Łaski
thanks them. Asked what the Turk intends: this winter the Sultan told Ferdinand's envoys there is no friendship,
peace or truce unless Hungary is given up to King John; he will come looking for Ferdinand. Preparations: ships,
guns, grain carried to the Danube, a levy of soldiers. The Speyer diet will be short; Łaski is ill but will ride
post to it; the dukes and their friends should stop any decision against the king until he comes. The king trusts
no princes in the Empire more. On the marriage he cannot yet write: in ten days he will settle it with the King of
Poland; in Poland as in France the dowering of kings' daughters is fixed by law. Postscript: put the king's letters
before the imperial estates.

Caveat: `r9403/transcription.tsv` is reading-aligned. The sign codes were written from the reading with the key
(`r9403/build.py`); homophone variants (W/HH for t, EQs/T for f) were not kept, so the sign count (2,452) is a
reconstruction. Doubtful words: ergo, ruffus, sequentes, contra, postas, constituar, nam, ub[i], dotandis, meus
(97.1% if these ten count as unread). Latin LM check: `lm.best_language` → la (−1.78) against fr (−2.64).

## Measures (15 Oct 2026)

`measure_sysb.py` counts the words of the System B decodes: a word with '?' or an unsettled sign ([F]/FLW, [I], [Y],
[XC], struck) is unread; DAG and BIGX count as read. These are machine decodes with the gloss key, not hand readings,
so a recognisable word with a letter slip counts as read (generous). R9322 429/445, R9417 217/219, R9323 124/163;
with R9403 (414/416) 1,184/1,243 = 95.3%. Statistical validation (`mk_validation.py`, pairs from the contemporary
glosses only, `la` model): pass (862 read tokens, reading −2.091 against random keys −6.002 and shuffled refits −3.757).

## Remaining gaps
- R9417 decoded, not read - closed 23 Oct 2026: read at the image (8 untranscribed lines added, circle/cross codes corrected from the glosses)
- R9323 decoded, not read - closed 23 Oct 2026: re-read word by word at the image, read
- R9323 l. 10, two words before "ducere noluit" - blocker: illegible; faint signs
- R9417 the owl word sign (P2 l. 27), "queiter" (l. 16), [?anestris], [?sies], the 6-shaped sign read k - blocker: no-key-material; one occurrence each, the gloss stops at l. 14
- FLW word sign (R9322, R9323) - blocker: no-key-material; probably King John's title, three occurrences, no gloss or key sheet
- R9403 P3 l.11 "[?]orator", P3 l.12 "[?]meus", small insertion on P1 l.4 - blocker: illegible; cramped signs on the image
- R9322 16 words with doubtful signs - blocker: illegible; '?' signs in the transcription

## Escalation

- [x] siblings: R9404-R9407 and R9418-R9422 viewed (other letters or other systems); R9423 key register checked in kaa4591; no other System B letter was found among the records viewed
- [x] clear-pages: glosses used on R9322, R9323, R9417 and R9403; they are the source of the key
- [x] known-keys: System A′ (R9427 gloss key) and R9369 (Augurelio's 1531 cipher) do not fit; the gloss key fits all four with the e/r exchange on R9403
- [x] print: web searches 21 and 22 Sept 2026 (Łaski 1529-31, Zápolya letters to the Bavarian dukes, KAA 4591) found no edition; Acta Tomiciana t. 8 (1530-32) is the Polish chancery's record and was not searched page by page
- [x] key-rebuild: key rebuilt from 153 glossed word pairs; DAG and BIGX fixed by context
- [n/a] retry: the open words are faint or cramped signs, not key gaps; a retry needs better images
- [x] retry (23 Oct 2026, b20): R9417 lines 15-29 and P1 and all of R9323 re-read at the image; both letters read

## Assumptions for George's review

- R9403 is counted in the same key as R9322/R9417 although its e and r signs are exchanged and some shapes differ. The
  same exchange shows in the raw decode of R9417 p.1, so it is taken as a variant of one key, not a second cipher.
- The R9322/R9417/R9323 percentages come from machine decodes, not hand readings (see Measures).

## Files

- `sysB/`: `R93xx_p*.tsv` (cipher words aligned with gloss words), `key_from_glosses.tsv`, `decoded.txt`,
  `R9323_decoded.txt`, `signs.md`; `R9322_signs.txt` etc. written by `signstream.py`.
- `r9403/`: build.py, transcription.tsv, decoded.txt, signs.txt.
- `measure_sysb.py` (word counts), `mk_validation.py` → `validation.tsv` (gloss pairs).

## History

- 21 Sept 2026: System B key rebuilt from the glosses on R9322/R9417 and R9322, R9323, R9417 decoded, as part of
  `targets/kaa4591/` (catalogue 161).
- 21–22 Sept 2026: R9403 read with that key, e/r swapped, as part of catalogue 162 here, with R9414 and R9415.
- 15 Oct 2026: split by key (see the top of this file).
