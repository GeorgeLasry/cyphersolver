# Re-reading log, fr. 15573 ff. 379r-381v (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b30)

## Starting point

Reading audit (22 Oct): "decoded, not read": Brett Burford's v0.5 key decode, word-divided by code but unpunctuated,
with a garbled word in nearly every sentence and no translation (his English is a gist). The fix asked for: repair the
sentences on the images (views 740-745), punctuate, translate.

## What was done

1. **Existing text?** No contemporary decipherment: Tomokiyo lists the despatch as "Undeciphered"; no DECODE record;
   Burford's prior-art search (GitHub, cryptiana, Cryptoole, web) found none. The Cipher-3 key is not known in any
   archive inventory under another name: Tomokiyo's table and the values from the deciphered siblings (ff. 277-280,
   fr. 15570 ff. 271-273) are what exists; Monaco J 41 (Matignon's minutes) not screened (needs-physical-access; no
   online inventory found).
2. **Images.** Gallica btv1b90618780 views 740-745 fetched at full size (about 4976 x 6656) through openapi.bnf.fr
   IIIF (no 403); f. 379r ll. 1-3 cut into strips and compared with Burford's sign names: his names hold for l. 2
   (b a k 30 xi [hooked y] [9t] p+ L u T q …); no label changed.
3. **Reading built** (`ff379-381_reading.md`): the literal decode divided into words and punctuated, line by line
   (`ff379-381_alignment.tsv` is the base); Burford's image notes in `burford/unresolved-v0.5.md` used for each
   unresolved stretch (Bourdeaulx, nettoyer, Clervant, Poigny, Gourgues, Castelnau, quinse a seyse mile escus, courre le
   bruict, Duras). Every word that departs from the literal letters is bracketed [?word]; supplied letters [x]; stretches
   with no sense […]. New readings here: "veu la saison qui est proche de l'iuer" (f. 379r l. 3-4), "president
   [?Brulart]" (f. 380r l. 17: literal "arulart"; the 1586 Lenoncourt-Poigny-Brulart negotiation with Navarre),
   "pour lettre de vostre armee", "le receveur ... Nicullier, qui est a Agen", "baillant trois cents escus a vostre
   seur" (f. 380v l. 22-23: literal "tro|iscets escus"), "Ie croy que c'est a chercher moyens".
4. **Departures** (the bracketed [?word]s, by page): f. 379r: les, riuiere, et, Bourdeaulx, nouuelle, marchandises, come,
   Bazeille, faict, luy, la, co[p]ie, et (×2), reuenu (15); f. 379v: semble, qu'il, propos, nettoyer, dite riuiere, de,
   pourroit (×2), vostre, il, besoing, Bergerac, Foy (13); f. 380r: sieur, Clervant, luy, oster, seroit, Brulart, I',
   pour, cela (9); f. 380v: fortifications, vostre, recherche, et, consuls, reduictz, faire, luy, meschancete (9);
   f. 381r: semblable, Gourgues, delibere, sieur, Castelnau, Bearnais, bruict (7); f. 381v: Baio… (1). Letters resting on
   a look-alike alternate or a sense-only value inside these words: about 60 (one or two per word); none adopted as a
   key change (each occurs once or twice, none holds across the despatch).
5. **Score** (b17_score.py, LANG_=fr): reading body **0.299 (20/67)**, explicit holes **0.433 (29/67)**. Before:
   Burford's normalised text scores 0.55 (44/80) and 1.00 holes-only, but only because his code word-breaks cut garble
   into real short words ("me pou a der", "in cy mode", "a a selle par les cv m"); it has no punctuation and no holes
   marked, so the figure is not comparable. Reader's judgement: f. 379r and the second half of f. 381r-381v build
   sentences (the Garonne tolls; the King of Navarre's plans and forces; Duras in Spain); f. 379v, f. 380r and most of
   f. 380v do not hold: most sentences have two or more holes.

## Result

Stays **decoded, not read** (0.30; holes-only 0.43). Partial reading and English kept.

## Open (blockers)

- About 25 damaged spans (blots, gutter, bleed-through; Burford's "damaged" items): **illegible**.
- Nine code signs (circle on a cross, looped epsilon with a stroke, the zigzag-tailed 3, m with a z-tail, the small 8,
  the barred double o where it is not *le roy de Navarre*): **no-key-material** (in none of the deciphered Cipher-3
  letters).
- About 75 doubtful words where the signs are clear but give no word under the key: **not-attempted** this session as
  a full sign-by-sign human re-read of the six pages (only f. 379r ll. 1-3 were compared with the image). That re-read,
  with the deciphered siblings ff. 189-190, 282 and fr. 15573 f. 373 searched for the doubtful sign classes, is the next
  step.
