# Re-reading log, R9417 and R9323 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b20)

## Starting point

Reading audit (22 Oct): both "decoded, not read". R9417: `sysB/decoded.txt` read as Latin on P2 ll. 1-11 (glossed),
then systematic slips ("nisi isto mnno concoedim fist", P1 "feancie", "ceistiani"). R9323: a '?' or bracket in nearly
every line of `sysB/R9323_decoded.txt`.

## 1. Existing text?

- Every file on DECODE R9417 (2 images) and R9323 (1 image) fetched with the shared cookie (b20_fetch.py, scratchpad
  only; BayHStA images, not public domain). No DOC_* or other attachments; DECODE says "Partially decrypted" for both
  only because of the interlinear glosses.
- The only contemporary text is the faint interlinear gloss: R9417 P2 ll. 1-14 and P1 ll. 5-7 ("postremo", "me et mea",
  "Cracouie sedecima die iunii Lask", "scripsit manu propria"); R9323 ll. 1-3 and 11. No edition (21-22 Sept web
  searches; Acta Tomiciana not searched page by page). Neighbouring records R9404-R9407, R9418-R9422 were checked on
  21 Sept (other letters or systems).

## 2. Read on the image

**R9417.** The P2 image (rotated 180) has **29** cipher lines; `R9417_p2.tsv` held 21 and the decode stopped at "non"
(l. 21). Lines 15-21 had been coded with the two circle shapes and the two cross shapes the other way round from the
glossed lines: on ll. 12-14 the gloss fixes ⊙ (dotted circle) = a, ○ = m, plain x = r, starred ⋇ = e ("turcarum cesar
magnos", "labore", "annales", "paratur"), the same e/r exchange as R9403. With those values every word of ll. 15-29
and P1 reads at once; the decoder's "m for a, e for r" slips were transcription-code slips, not the writer's. Also: ‡
(barred tall cross) = b ("indicibili", "exibit"), ≐ = f, the 6-shaped sign = k (doubtful: "Cubergk", "Minkuics"), and
an owl-shaped word sign on l. 27 (unidentified). Each of ll. 15-29 and P1 ll. 1-7 read on 1.5-3x native crops;
sign codes in `R9417_signs_b20.tsv`, corrections in `R9417_corrections.tsv`. The value changes hold across every
occurrence in the letter (the glossed lines included); no key value was changed for R9322 or R9403.

New content (ll. 22-29, P1): Minkuics could not come earlier "ita enim erant obsessa itinera"; the King of Poland's
daughter: the match "ita frigide incipit", and someone [owl] is pressing through Sigismund Herberstein that she be
given to Frederick the Count Palatine; the dukes should send with others to Charles the Emperor to hold back his
brother from attacking King John. Dated "Cracouie sedecima die iunii", signed "Lask", "scripsit manu propria".

**R9323.** Re-read word by word on 1.5x crops of the rotated image. Corrections (`R9323_corrections.tsv`): l. 3
starts with the big looped X word sign (Ferdinand), so "concordiam inter [D] et [BIGX]"; the angular Ƶ is q (quia,
qui, itaque); the I-sign is b (Bauarie, Boemia, libentissimus, principibus); ‡ is n (nostro, as found on 15 Oct);
"oaun?ia" = omnia, "con?sumr?n?t tr?eer?" = consument terre, "porte" = forte, "eduo?st?" = equos. Two words of l. 10
before "ducere noluit" stay unread (faint).

## 3. Alignment

Every word of both readings is carried by its signs as read on the image (R9417 ll. 1-14 also by the gloss); supplied
letters are bracketed (duce[m] in R9323, where the sign is the dotted circle; Łask[i] only in the English). Doubtful
words are [?]-marked: R9417 [?ua], [?excusare], [?re], Min[?k]uics, [?iudeum], [?uos], [?anestris],
[?Wirtembergensis] (decode "nuretuaobergensis"), [?niteretur], [?faciet], Cuberg[?k], su[?a], [?sies], [?Ce]sarem;
R9323 [?timent], [?contemnendi], [?comuni]. The writer's own slips are kept ("paratur est", "omninos", "mititur",
"mitet").

## 4. Score (b17_score.py, la)

| letter | before | full word list | explicit holes (HOLES=1) |
|---|---|---|---|
| R9417 | decoded, not read | 0.250 (7/28) | 0.893 (25/28) |
| R9323 | decoded, not read | 0.111 (1/9) | 0.889 (8/9) |

The full-list figure is low because the checker's Latin list (37,769 forms) lacks common words (carissime, peribit,
arripere, nominabit, inducias, spolium) and the -cia spellings (negocium, potencia, amiciciam) as well as names
(Bude, Polonie, Boemia); the readings are not respelled to pass it. On the explicit-hole share both pass about 0.60
and the sentences hold. Both set read, grade B.

## Open

- R9417: the owl word sign (l. 27), [?anestris], [?sies], the 6-shaped sign (k?), "queiter" (l. 16) - blocker:
  no-key-material (one occurrence each; the gloss stops at l. 14).
- R9323: two words before "ducere noluit" (l. 10) - blocker: illegible (faint); [?comuni] - no-key-material.
