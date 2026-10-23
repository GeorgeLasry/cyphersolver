# Re-reading log, fr. 3984 no. 68 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b28)

## Starting point

Reading audit (22 Oct): "decoded, not read". `texts/no68_decryption.md`: 0.000 clean sentences (0/3,
`docs/_check_reading.py`); a stream of syllables with the three-letter word codes unread.

## 1. Is there a text already? Not of no. 68 — but the key's sibling has one

- Not a DECODE target (Gallica only); DECODE searched by name (Ibarra, Feria, Mansfeld, fr. 3984/3995) in the harvested
  list: nothing.
- **Neighbouring folios opened** (Gallica IIIF thumbnails of canvases 232-303 and full images of 242-245, 262, 265,
  268, 269, 272; scratchpad `reread/ibarra/`):
  - **f. 130 (canvas 242)**: Count Charles of Mansfeld to the Duke of Feria, "de Formentieres 7 de julio de 1593",
    wholly in the Feria-Mansfeld cipher (the other letter Tomokiyo cites for this key; NOTES' "Next" item, which
    Gallica's Cloudflare had blocked on 14 Oct). Transcribed: `f130_mansfeld_ct.txt`.
  - **f. 131r (lower half) - f. 131v (canvases 243-244)**: **contemporary decipherments**, in a French clerk's hand,
    of (1) that Mansfeld letter ("Lre du Comte Charles au duc de Feria") and (2) Feria's letter from Paris, 10 July
    1593, whose cipher is **f. 143 (canvas 265)**. Transcribed: `f131_decipherment.txt`. The clerk left the
    three-letter codes he could not read as dots with the group written above ({pra}, {ner}, {cur}, {den}, {he},
    {que}, {flu}, {la}, {dar}, {ris}, {tus}, {cor}, {gal}): **the interceptor did not have the nomenclature
    either**.
  - f. 146-149 (canvases 269-274): French letters and a "Estat des gens de guerre" of 13 July; no decipherment of
    no. 68 anywhere in canvases 232-303.
- Print: Tomokiyo's table (key only). No edition of Ibarra's 1593 letters searched beyond NOTES (earlier sessions).

## 2. The crib: f. 130 against f. 131

`research/reading_audit/b28_ibarra_dec.py` decodes f. 130 with keyM + 57 = li; aligned by eye with the decipherment
(`f130_mansfeld_ct.txt` decode vs `f131_decipherment.txt`, every line). The letter alphabet and syllabary hold
throughout ("Visto por la de V.E. de 3 de este ... que la Infanteria no llega a 3000 hombres ni la cavalleria a
400 ... el enemigo me ha de venir a buscar ... para el salbamento de V.E."). Values fixed by the decipherment:

| group | value | occurrences (f. 130) | evidence |
|---|---|---|---|
| 64 | ha | 3 (+9 in no. 68) | "se 64 de ocupar" = se ha de; "para 64[ser]"; Tomokiyo's h-row runs 64-60 (hu = 60) |
| 63 | he | 3 | "63 vis to" = (he) visto; "lo 63 63 cho" = lo he hecho |
| 62, 31 | hi, jo | 1 | "el gobernador 62 31 de 81 lle ro y" = hijo de Villeroy (j-row ja 34 ... jo 31) |
| 19 | fa | 3 | "+19v den ys" = Frandenys (Saint-Denis), "19+ tan do" = faltando, "+19v ses" = franses (f-row fe 18, fi 17, fu 15) |
| 81 | vi | 2 (+1) | "81 lle ro y" = Villeroy; "be a u 81" = Beauvais (homophone of 82) |
| xen | Infanteria | 1 (+3) | "que la xen no llega a 3000" |
| pun | hombre | 1 (+1) | "pun° ni la cavalleria" = hombres |
| mon | gente | 4 (+3) | clerk: Armada, orden, gente, gente; **gente fits all four** ("tan la gente sin", "hasta que me llegue la gente que me an prometido", "esta poca gente", "numero de gente") — sense-backed, flagged for review |
| tel | exercito | 2 (+1) | clerk: exercito, campo; exercito fits both — flagged for review |
| fon | Flandes | 1 (+1) | "despacho a fon por la posta" |
| dir | Magestad | 1 | "al servicio de su dir" (clerk "M.de") |
| Vas | señor(es) | 2 | "esos Vas" (clerk "segnores"; Tomokiyo vas = segnor) |
| con | fuerças | 1 | clerk "fuercas" |

Kept out of `keyM.tsv` (written to `codes_b28.json`); no keyM value changed. Unresolved there too: gal, 7, 9, mo, c.

## 3. no. 68 decoded again and read on the image

`ct68.txt` decoded with the new values (`b28_ibarra_dec.py ct68.txt codes_b28.json`); its marks (dropped on 5 Oct)
re-read on line crops of the Gallica full image where a word needed them (finals -s/-n/-r and the doubling arc:
"cavalleria", "continua", "ningun", "todas estas", "espero en Dios", "presente"). `ʃ` in ct68 is two signs: the
p-shaped e and the f of code groups (ʃon = fon = Flandes, as on f. 130). New stretches that build: "que aya recivido
su gente", "A mi no me parece que puede con esta gente", "Se ha de poner todo lo que se puede y por ningun caso",
"hasta el ultimo aliento", "No estamos desesperados", "espero en Dios que ha de acudir a lo que esta[...]",
"Supuesto el numero de ese exercito en Flandes, pareceria que venia a ...", "a lo menos no parece sino".

Partial reading `no68_reading_b28.md` (English `no68_en_b28.md`); each word is in the decode or the clear text; the
code groups without value are shown as `<pra>` holes. Look-alike letters: 4 (ʃ read f in fon/Flandes; + over 98 read
as tr in [?tregua]; ∇ read o in [?Alonso] — not adopted, left [?]; ú read u).

## 4. Score and judgement

`b17_score.py` LANG_=es on the reading body: **0.258 (8/31)**; explicit holes (HOLES=1): **0.355 (11/31)**. Before:
0.000. Reader's judgement: about a third of the sentences build; the rest break on the code groups (pra ×6, xur ×3,
gar, dur, var, tor, vis ×2 each, and some 25 singletons). Stays **decoded, not read**.

## Open

- The three-letter code groups (about 45 tokens, ~30 types): **no-key-material** — not in Tomokiyo's table, not fixed
  by the f. 130/131 crib (other groups), and the 1593 French decipherer left the same groups blank; a nomenclature
  for this key is not known.
- Syllable runs between codes that do not divide into words (ll. 7-12): no-key-material (they sit between unread
  codes; the syllables are confirmed on the image).
