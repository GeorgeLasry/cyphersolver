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

# r2j (23 Oct 2026, Claude Opus 5.5): second pass at the breaks

1. **A clear copy or decipherment nearby?** Gallica btv1b90618780 views 724-757 contact-sheeted (500 px) and views 738,
   739 read at 1400 px: ff. 368-378 are clear letters of 1585-86 (ff. 377r and 378r are petitions to the King from
   town councils, not copies of this despatch; f. 373 is the Cipher-3 letter with its own decipherment, already used by
   Burford), ff. 382-384 blank leaves and an address, ff. 385-386 a different cipher (numerals and crosses, another
   system) addressed "Pour Monseigneur de Villeroy" on f. 386v; views 758-760 do not exist. No clear copy, minute or
   decipherment of ff. 379-381 in the neighbouring folios. (The brief named "the Cipher-1 key"; the despatch is in
   Cipher-3, Tomokiyo and Burford; Cipher-1 is the Mayenne-Forget key of `targets/matignon1586/`.)
2. **Full-size images** (views 740-745 at about 4976 x 6656, IIIF `full/max`) cut into four-line bands at 2000 px and
   read at the breaks. f. 379v l. 3: no sign between # and k (Burford's "p" is bleed-through, as his agent saw but
   the voting did not adopt): the line reads *la dite riuiere* (`ff379-381_corrections.tsv`). f. 379r l. 8 s. 2 is the
   crossed 3 (Burford's own note), the same shape as z3 = m in l. 11: *et* is not carried, kept [?et]. f. 379r l. 16:
   the p+ of *sembla?le* has the shape of the p+ = a of *a Caumont* in the same line, so the b there is a second value of
   the sign, not a separate class on the image. f. 380r l. 8 (*se + S S i t*): the image has the two o-signs, *seroit*
   not carried.
3. **Second values that recur** (`research/reading_audit/r2j_lattice.py`: a word lattice over Burford's signs with the
   Henri IV letters' period vocabulary, proposing single-sign substitutions; tallied per sign class and then checked
   word by word): C = h (3 places), p+ = b (6), b = y (8), g = o (2), Lr = n (1 here, 2 in Burford's EM on f. 277r).
   Rejected: d = s (14 lattice hits, all spurious word breaks), z3 = et (2, but z3 = m in *come* l. 11), 9t = e as a
   value (only *les* needs it; used as a look-alike), g = o in *responce* (the word wants an n that no sign gives:
   *respo[n]ce*). Look-alike alternates used: 9t/xi (*les*), +/F (*riuiere*, *deslibere*), xi/eps (*coure*), eps/xi
   (*agreable*), S/Sq (*quelque*). Letters resting on a second value or a look-alike: 28 of about 2,300 (1.2%).
4. **Word-by-word carry check** (`research/reading_audit/r2j_matignon_carry.py`, a monotone alignment of every
   unbracketed reading word with the signs): b30 had unbracketed words the signs do not give, now corrected:
   *commissions* (signs: *comissions*), *ataquer* (signs: *ataque* + *uer*, now *ataque[…]*), *pourra* (*poura*),
   *qu'il poura* (*qui poura*), *mile escus* (*mil escus*), *ie supplie* (signs *ie sunlie*: now [?supplie]), *quelque*
   (S where q is wanted: now carried by S/Sq), *ie li escrivi* (signs *ue li*: now [?ie]), *faire sa recepte* (signs *sa
   sa recepte*), *responce* (*respo[n]ce*), *Verdu[n]* (yv = n gives *Verdun*), *profit[er]* (the next line begins
   *er*: *profiter*), *Nauarrains* (*Navarains*). Newly read: *les places*, *la riuiere*, *Sainte Baselle*
   (Sainte-Bazeille), *ie luy en envoye*, *le semblable a Caumont et au Mas de Verdun*, *la dite riuiere*, *pouroyt
   estre si long*, *si vostre maieste* (d = vostre), *agreable, il seroit besoing*, *Bergera[c], Saincte Foy*,
   *Cleruant* (twice), *luy oster*, *aduerty*, *de luy*, *l'on luy en compte*, *qu'il n'en a rien faict*, *meschancete*,
   *mil escus*, *le semblable* (f. 381r), *de Gourgues*, *a deslibere*, *d'Andos, seneschal de Foys*, *coure le bruict*,
   *l'euesque*.
5. **Score** (`research/reading_audit/v2_score.py`, fr): before (b30) plain 0.279 (17/61), explicit holes 0.344
   (21/61); after plain 0.426 (26/61), explicit holes **0.590 (36/61)**, hole rate 0.133, 762 words. Plain is low
   because the modern word list does not hold the period spellings (soullaigement, conptablie, pouroyt, deslibere,
   impugny, seyse, chevall).
6. **Reader's judgement.** f. 379r, f. 380v-381v and most of f. 380r build sentences that translate; the middle of
   f. 379v (the march of the army, ll. 17-21) and f. 380r ll. 1-2, 18-22 still have runs of holes. At the bar's edge.

## Result (r2j)

**Read** (grade B, at the edge of the bar: 0.59 explicit-hole share, hole rate 0.13, look-alike and second-value letters
1.2%). What stays open, by blocker: the code signs (circle on a cross, small 8, looped epsilon, zigzag-tailed 3, m with
a z-tail, barred double o): **no-key-material**; blotted or bled-through spans (f. 380r ll. 2, 6-9, 18; f. 381r ll. 5,
8, 12, 19): **illegible**; the remaining [?word]s and […] runs where the signs are clear but give no word under the key
(Bourdeaulx, nouuelle, come, faict, reuenu, semble, propos, pourroit, seroit, Brulart, fortifications, recherche,
consuls, supplie, consequence, Castelnau, Bearnais): **no-key-material** (no deciphered Cipher-3 letter attests the
values they need; Monaco J 41, Matignon's minutes, not screened: needs-physical-access).
