# R3814 re-read log (batch b06, 22 Oct 2026, Claude Opus 5.5)

## Is there a text already?

No. No DECODE transcription or key; no interlinear or margin decipherment on pp. 1-2 (crops checked); Mírka 2012 read
only R3811. Undated; DECODE and the docket give 1639 (Feb.).

## Image checks and transcription

- pp. 1-2 checked on crops. One correction (read/R3814_corrections.tsv): on p. 2 the numbered point "5." (with a raised
  mark, like "4." at the head of the page) had been transcribed as the sign 5 (sch) plus "{lo}".
- Clear text on p. 1 compared with the image; the transcription agents' reading kept (minor doubts: "verhaist ihm fr.
  wollte", "abzugestalt sehen").

## Key observations (proposals; key.json not changed)

- The crossed flourish `p` (null) reads ta (Gusta[v], tracta-, zu [ta]ufen) and vi (Sal[vi]i, Sal[vi]us, Sal[vi]o) in
  this letter; `Salui` (P2) confirms Salvius. Likely two crossed signs merged under `p`; printed [?].
- `m` after 29 = a (quae), as in R4625.

## Reading

read/R3814_reading.md, read/R3814_en.md. b06_align.py: 0 words not carried. b06_score.py (body only): clean share 0.35
(22 of 63 sentences), hole rate 0.22. The letter is about half Latin, and its Latin runs are where the decode breaks
(run-together groups, the crossed sign).

## Stays open

- Unread runs (P2 "rirettransac", "terthelhabenaberteir", "quanosnisnlipsis"; P3 "demecichnichtswurdtnitlgeschadet",
  "tertefreltungbenstettn"; P5 "lece", "deprereppalma") and pp. 3-5 not checked on the images: blocker is labour (an
  image pass on pp. 3-5) and the `p` split in the key.
- p. 4 clear postscript (about 20 lines) never transcribed (clear text).

Result: stays **decoded, not read** (0.35 < 0.60), with this partial reading.

## Second pass (22 Oct 2026, after the key update: 38 = d, Δ = nu, #dot = su, #s-long = ti, m = a, 9v = vo)

- All five pages checked on crops (pp. 3-5 for the first time). 27 further rows in R3814_corrections.tsv (28 in all):
  - crossed long-s = #f-cross (ta): tam, petat, promittat, tractatibus, tractare, prerepta, universalitate, distincta,
    zu taufen, eim tag (10);
  - 9 → 9v (vo): vorthel, von Schwarzenberg, von mir, gelt von Franckreich, Vorarbeit (5; two of them had been read
    93 + z-tail);
  - figures: "satisfactionis" (23 39), "iure pignoris" (10, not c), "forma in verbis" (92), "zu lassen" (φ and 6 z-tail),
    "zu consultiren" (φ), "derselbe post" and "Wehselbrief" (6 33 40, run together; by sense);
  - clear text: "sein meistentheils in" (p. 1), "Im übrigen erscheint das" (not "im Königreich"), "erhebt noch ein"
    (p. 5); the "..." on p. 4 is the writer's monogram.
- New readings: "nulla sit spes nec diei denominade", "hoc casu", "suo tempore", "Brisacum erit Suecorum", "ad manus
  Caesaris", "NB zu consultiren, was Dennemarck fur interesse bei Riga hat", "quod nihil tam absurdi petat ... de aula
  Caesarea sibi non promittat", "iure pignoris ... cum denominatione summae", "Ragozi ... gelt von Franckreich", "glorirt
  de prerepta palma", "Wann mir dise herren nur folgen wolten", "uber Nurenberg mit derselbe post", "Wehselbrief".
- Postscript, p. 4: about twenty lines in Kurz's own fast abbreviated hand; read only in part at DECODE resolution
  (blocker: illegible at this resolution); the legible words are in tr/ as an editorial note and in the reading's Notes,
  not in the body.
- Score (body only, b06_body_score.py): 0.35 → 0.49 (31 of 63 sentences), hole rate 0.167; aligner 0 flags.

Why it stays under 0.60: half the letter is Latin and names (Mithofi, Salvius ×5 as [?] because the crossed long-s =
vi is not in the key, Pommeren, Balbey, Ragozi), which the word list does not know; real holes left are the runs listed
in the reading's Notes. A key value for the crossed long-s = vi (as was done for 9v) would close the Salvius words.

Result: stays **decoded, not read** (0.49 < 0.60).

## Third pass (22 Oct 2026, key pv = vi added)

- p → pv (crossed long-s read vi, key pv): Salvii, Salvium, salvis, Salvius ×2, Mithovius, nit vil, Salvio (8 rows).
- Further: "erben zu bringen" (φ), "Gusta-" (crossed long-s = ta; still printed [?Gustav]: the figures give Gusta-und),
  clear text "werde dergestalt sich von Dennemarck keine leges praescribiren lassen" (not "abzugestalt sehen"),
  "zimblich"; "betrift" printed for betri-f-?-t.
- 40 rows in R3814_corrections.tsv in all.
- Score (body only): 0.492 → 0.524 (33 of 63 sentences), hole rate 0.151; aligner 0 flags.

Result: stays **decoded, not read** (0.52 < 0.60). The failing sentences now fail mostly on Latin and names the word
list does not know (Mithofi, Pommeren, Balbey, Ragozi, ezaminetur, generalissimis, NB); about 15 [...] remain in runs
whose figures are legible but do not make words (listed in the reading's Notes).

## Fourth pass (23 Oct 2026, r2c, Claude Opus 5.5)

- DECODE R3814 re-fetched: five images plus Mírka's key reconstruction (xlsx, DOC_3814_…xlsx, and the same handwritten
  table as R3813, DOC_3814_…pdf). A key, not a decipherment; no text of R3814 exists elsewhere (see R3813 log, section 8,
  for neighbours and print).
- Key: k = to, m = va adopted for all letters (KEY.md); neither occurs in R3814's open runs except "quod" below.
- Image checks (r2c_line.py crops): P2 r. l.4 "aber [te]ir" — the 9 is the bold 9 (#sect, w) → "aber wir"; P2 r. l.7 "29 9 38"
  — the 9 is the q-form → 9v, quod (29 + vo + d); P3 r. l.18 "9 28 14 83 28" → 9v: "vor oder hinter Pomeren" (Vor- and
  Hinterpommern). Three rows added to R3814_corrections.tsv.
- Tried without result: P3 r. l.21 "auf terte freltung ben stettin" with 9 = vo/te/w gives no word; P5 l. l.22 "zeit
  wetlohren"; P1 "denomina-d-4-e" (4 is a plain 4 on the image; x gives nothing); P2 "rirettransac", "quano snisn lipsis".
  These stay [...]: the figures are legible and give no word under any value of the key or of Mírka's table.
- Score (body only, v2_score.py): plain 0.508 (32/63), explicit holes 0.952 → 0.968 (61/63), hole rate 0.041; b06_align.py
  0 flags. Half the letter is Latin, so the plain share understates it; on explicit holes and on reading (the satisfactio
  coronae points, Salvius fooling Mithoff, the secret correspondence via Nuremberg and Wolfenbüttel) the sentences hold.
  **Read.** The p. 4 postscript in Kurz's cursive stays outside the body (illegible at DECODE resolution).
