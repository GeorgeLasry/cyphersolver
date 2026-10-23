# Re-reading log, Méry de Vic 1589, Dupuy 61 f. 43r (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b30)

## Starting point

Reading audit (22 Oct): "decoded, not read", excerpt only: two excerpts from George Lasry's report, each with holes; his
full decipherment is not in the repository; his report says "Partly deciphered". Clean-sentence share before: no text
of the cipher (0.00).

## What was done

1. **Existing text?** No DECODE record. Lasry's full transcription and decryption are not in the repository (his report
   carries only the key table, `../lasry_p004_1.png`, and two excerpts). No contemporary decipherment: Gallica
   btv1b103164206 views 85-100 opened (f. 40r-f. 43v and neighbours, IIIF through openapi.bnf.fr, no 403); the letter
   is ff. 40r-43r (views 89-96), wholly clear except **one cipher block, 16 lines on f. 43r** (view 95); no interlinear
   gloss, no decipherment on the neighbouring folios. Not known in print (web search not productive; not searched in
   the Lettres missives).
2. **The key.** Lasry's table (81 signs) is the only key. Not found under another name on DECODE (no record for Dupuy
   61 ff. 40-43) or in the BnF inventory.
3. **Decode on the image.** The 16 cipher lines cut into thirds at 1.5x native (research/reading_audit/b30_lines.py and
   inline crops; images in the scratchpad) and read sign by sign against Lasry's table, `f43r_cipher_decode.tsv`. The
   decode reproduces both of Lasry's excerpts ("qui avoit tenu le feu roy en esperance de le servir, s'est declare come
   plusieurs du … m'ont asseure"; "assembler a huict lieues de ceste ville. Leur troupe … au plus de douze cents … et
   deux cents chevaux et doivent meiner deux ou trois pieces") and adds: "Il … amas d'hommes et se delibere de … un gros
   …", "qui a tousiours parle en … servit[e]ur de roy se change", "… sont plus a creindre que … persones",
   "plusieurs qui soient ennemis de la [?ligue] changent, qui prenent [?le] pretexte de la religion", "Ie [?les]
   contiens ce que ie puis", "… servira beaucoup", "ailleurs. Et que les susdictz s'assemblent".
   The 13 Oct spot-check's "disagreement" (clear "de roy se change come on ma asseure" against Lasry's "s'est déclaré
   comme plusieurs du ? m'ont asseuré") is two different passages: both are in the cipher, l. B and l. I.
4. **Key changes.** None adopted. Sense-only values flagged for review, each seen once: ꝗ = g in "[?ligue]" (Lasry's
   table has this 9-shape under s/t); Ӿ = le(s) in "prenent [?le] pretexte" and "Ie [?les] contiens" (Lasry: Ӿ = re,
   which holds in "les recognoissent"). The 9/g-shaped signs are read among e (dotted), s and t, as Lasry's table lists
   9-shapes in all three columns.
5. **Look-alike alternates: 7 letters** of the reading rest on one: u read u in "plusieurs" (Lasry: u-shape = a);
   π read as ϖ (n) in "deuoie[n]t"; small x read as κ (i) in "trois" and "tousiours"; f read as ſ (s) and t read
   as t in "s'assemblent"; l read as t in "pretexte".
6. **Alignment, word by word**: every unbracketed cipher word is carried by its signs (tsv, column decode); supplied
   letters bracketed ("servit[e]ur"); unread groups […] or the sign itself in brackets.
7. **Score** (b17_score.py, LANG_=fr): whole reading body (clear text of f. 43r + cipher) **0.667 (20/30)**, explicit
   holes 0.767; **the cipher passage alone 0.308 (4/13), explicit holes 0.462 (6/13)**. Reader's judgement: the cipher
   sentences do not hold: 8 of 13 have a hole, three (ll. D, H, N-O) are unreadable stretches.

## Result

Stays **decoded, not read**: the cipher passage is below the bar (0.31; holes-only 0.46). Partial reading kept.

## Open (blockers)

- Unread groups (`bʒttgto`, `y)`, `Ɛobttg`, `ꝏ`, `&γγω`, `xa5ttℒo`, `8`, `/t/`, `⚲`, `&`, `y-V:· ꝏ`, `Xo£ 59x7tq7 Wϖω
  favo5πꞒ`) and the unidentified signs [P], [A], [ʃ], [7]: blocker **no-key-material** (Lasry's table lists 20
  unidentified types; no other copy of the key or the plaintext is known). Lasry's own decryption file may close some
  of them: ask him.
