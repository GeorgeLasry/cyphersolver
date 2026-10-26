# Bienvenut to "Vostre Altesse" (the duc de Nevers?), Paris, 28 February 1590 (BnF fr. 3623 no. 23; DECODE R9453)

Status: read (26 Oct 2026): ff. 35r-v transcribed in full and read with the key slip, read_share 0.985 (see the dated section below). The site page still shows the 22 Oct excerpt until the write-up is rerun.

**22 Oct 2026, reading audit** (George Lasry's test): texts/n23_decryption.md is a sample of about 90 words joined by "..."; it reads, but most of the letter is not in the repository. Claim read -> read in part (about 15%, estimated) until ff. 35r-v are transcribed; every code is already resolved by the key slip.

Earlier status (before the 22 Oct 2026 reading audit): read. A clear copy in which only nine persons and provinces are coded by small numbers; the key is bound with
it on f. 36r, and every number in the letter is on it.

Split on 14 Oct 2026 from `champagne1590` under the one-key rule (George Lasry, 14 Oct 2026). Until then this letter
was filed with the June 1590 news-letters nos. 24, 25 and 60 of the same volume, which use a two-digit alphabet:
[`targets/champagne1590/`](../champagne1590/NOTES.md) (a different cipher, with its own page). The two keys conflict:
here 35 = Mayenne, 37 = M. de Nemours, 53 = Saint-Sorlin; there 35 = a, 37 = c, 53 = i. Laurière's 1593 letters in
Nevers key no. 57, also once filed there, are [`targets/lauriere1593/`](../lauriere1593/NOTES.md). The work below was
done in the champagne1590 session of 21 Sept 2026 and is carried over from its NOTES.

Work date: 2026-09-21. Catalogue item 30 (the item that grouped the Champagne letters).

Images: Gallica `btv1b525245007` canvases 79–81 (f. 35r–v and f. 36r); copies in the main checkout's
`targets/champagne1590/img/` (`full_5007_79.jpg` – `_81.jpg`, git-ignored; shared source folder, not moved).
DECODE R9453 (catalogued there as "N/A (key record)").

## The letter: Bienvenut, Paris, "du dernier febvrier 1590" (f. 35r–v, key f. 36r)

A copy addressed to "Vostre Altesse" (the duc de Nevers? the style suggests a sovereign prince; the letter speaks
of "Mr de Nemours ... en son gouvernement"). All text is in clear except code numbers for persons; the copy marks
"Et après en chiffre" before the last paragraph, so the cipher had been resolved by the copyist except for names.
The key slip on f. 36r reads:

    1 Le Roy d'Espaigne · 10 Le Pape · 15 Les villes de l'Union, ou Provence & Daulphiné ·
    17 Le Duc de Parme, ou Picardie · 36 Madame de Nemours · 35 Monsr du Maine ·
    37 Monsieur de Nemours · 26 Le Roy · 53 Monsr de St Sorlin

Every number in the letter is in the key. Sample: "[Mme de Nemours] me pourmena hyer par la gallerie du logis de la
Reyne ... elle me monstra plus[ieu]rs avis qu'elle avoit eu de [St Sorlin] ... qu'il y a une tres estroicte
intelligence entre [le Pape] & [le Roy d'Espagne] ... le courrier que Mr le Legat despescha a Rome ... pour entretenir
la guerre jusques a ce que [le Pape] puysse envoyer 8 ou 10000 hommes de guerre avec lesquelz il baste l'ame a
[Mayenne] & les porte sans qu'il a d'accabler [le Roy]". Grade H (key in the document).

## 26 Oct 2026: full transcription of ff. 35r-v and measured reading (Claude Opus 5.5)

Gap closed: "n23, ff. 35r-v beyond the sample: not transcribed".

* **Transcription.** `texts/n23_transcription.md`: both pages, diplomatic, one manuscript line per line (35r.01-33,
  35v.01-35), read in 2x crops of the full-resolution Gallica images (canvases 79-80; main checkout
  `targets/champagne1590/img/full_5007_79.jpg`, `_80.jpg`). Abbreviations expanded in [ ], struck words kept as ~~ ~~,
  doubtful words listed at the end of the file with folio and line. 1,259 tokens (`_check_profile.py --measure`).
  The 26 code numbers stand exactly where `codes.txt` lists them (15 recto, 11 verso): no correction to codes.txt.
* **Reading.** `texts/n23_decryption.md` (replaces the sample) and `texts/n23_en.md` (English, replaces the excerpt
  translation). Every code resolves from the key slip. The two dual entries, every occurrence:
  - 15 at 35r.28 "les Ambass. de 15": both values kept ([Provence et Daulphiné, ou les villes de l'Union]); at 35v.09
    "sinon qu'elle y remedie en 15": Provence & Dauphiné (a place where the Altesse can act).
  - 17 at 35r.30 "que 1. veuille empieter [?] / 17. soubz pretexte ... de protection": Picardie; 35v.19 "menées qu'ilz
    font en 17": Picardie; 35v.33 "harquebuziers ... des meilleurs de 17": not settled (the best of Picardy, or of the
    duc de Parme's army), both kept.
* **Measured.** read_share 0.985 (962 words, 1 unread word, 13 doubtful; `research/reading_audit/v10_relabel.share`);
  `docs/_check_reading.py` 0.80 clean sentences (73/91). Above the 95% read bar: read in part -> read.
* **What stays open** (scattered, none blocks the sense): the struck-and-replaced word before "lieu" (35r.26); doubtful
  "émotions" (35r.04), "ferait" (35r.11), "Roccas", "Vier" (35r.22, a place and a captor not identified),
  "affect[ionné]s" (35r.24), "empieter" (35r.29), "baste l'ame" (35v.05, possibly "l'asne"), "me" (35v.12),
  the heading "Ce qui s'ensuyt mys en chiffre" (35v.20), "stylé", "cogneu", "occurrans" (35v.22-23).
* **The content, beyond the sample.** Madame de Nemours wants her son in Philip II's service (Moreo did not answer) or
  back in his government; news of Grenoble besieged, Gex castle demolished, Bonne besieged; the Legate hampered by the
  French hatred of Spain; Pope, Spain and Mayenne agreed that Spanish aid will go through the Pope, repaid secretly at
  bankers' interest. Panigarola explains Moreo's and Mendoza's affront to Bienvenut; they keep the Altesse's ministers
  out. In cipher (the copy marks it twice): Bienvenut means to leave Paris in March with Nemours's troops, M. de Riddes
  staying to report; he offers 1,000-1,200 arquebusiers.
* **Recipient (hypothesis, not proven).** The full text points to Charles-Emmanuel I of Savoy rather than Nevers:
  Bienvenut signs as the Altesse's "subject"; Gex and the siege of Bonne (Savoyard places attacked by Geneva and Bern in
  1589-90) "nous travaille"; the Altesse is to "remedy in Provence & Dauphiné" (Savoy's 1590 intervention); Mendoza and
  Moreo keep "the Altesse's ministers" out of the League council. Nevers was with Henri IV in 1590. The copy in the
  Nevers papers would then be an intercept or a copy passed on. Web search (26 Oct 2026) for Bienvenut as a Savoyard
  agent found nothing. DECODE R9453 should carry the transcription and the recipient question.

## Open

* The dual entries 15 (villes de l'Union, or Provence & Dauphiné) and 17 (duc de Parme, or Picardie) are taken from
  context. The recipient ("Vostre Altesse") is probably Nevers, not proven.

## Files

* `texts/n23_transcription.md` (26 Oct 2026): the full diplomatic transcription; `texts/n23_decryption.md` the reading,
  `texts/n23_en.md` the English.
* `codes.txt` (14 Oct 2026): the 26 code numbers of ff. 35r–v in text order, read from the full-resolution images
  (15 on the recto, 11 on the verso; plain numbers such as "8 ou 10000 hommes" left out). All 26 are on the slip.
* `key.txt`: the key slip, f. 36r.

## Prior work

DECODE R9453 lists the record as a key; the copy and its key were not connected to a reading there. No printed text
found (Tomokiyo nevers.htm and GL.htm, Mémoires de Nevers index checked 21 Sept 2026).

## Remaining gaps

- ~~n23, ff. 35r-v beyond the sample: not transcribed~~ - closed 26 Oct 2026: transcribed in full (texts/n23_transcription.md) and read, read_share 0.985. Left: 13 doubtful words and one struck word (35r.26), and the dual key values at 35r.28 (15) and 35v.33 (17), listed in the 26 Oct section

## Escalation

- [x] siblings: champagne1590 and lauriere1593 split off (other keys)
- [x] clear-pages: the letter is itself a clear copy; key slip f. 36r
- [x] known-keys: the key slip resolves all 26 codes
- [x] print: none found
- [n/a] key-rebuild: key complete
- [x] retry: full transcription of ff. 35r-v done 26 Oct 2026; doubtful words re-read at 2x, still doubtful
