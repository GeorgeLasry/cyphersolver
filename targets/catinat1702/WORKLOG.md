2026-10-28 access: page images 1-3 and Bazeries-More-Letters.pdf downloaded from scienceblogs.de; thread text saved (klaus.txt).
2026-10-28 literature: read 46 comments; no decipherment anywhere; Tomokiyo's Item 4/8B/10B/d'Usson rejected there.
2026-10-28 transcription: ciphertext.txt = Lichtenberger + Norbert's 17 corrections, 591 tokens; page 1 lines 1-3 match the image; page 3 is clear closing formula.
2026-10-28 statistics: 186 distinct, 64 singletons, IC 0.0086, 252 tokens <=99 in 141 runs.
2026-10-28 hypothesis: ordered alphabetical blocks for 1-99 (ordered_low.py): real -2.35/token vs nulls -2.42..-2.60; gibberish decode. Inconclusive.
2026-10-28 control: synthetic ordered scheme, real run lengths: letter accuracy 35-40%, gap to null 0.09/-0.02. Solver too weak at this length; nothing claimed.
2026-10-28 transcription check: all 47 lines of pp. 1-2 compared with the images; changes 1.22.7 10->13, 1.18.14 57->54; doubtful groups listed in ciphertext.txt header. p. 2 ends "140.39. Je suis avec plus de verite" (clear), running on to p. 3.
2026-10-28 key matching: Tomokiyo's 8B (4 Apr 1702) layout: never uses 1-21 (ours 11% there) and 24% above 400 (ours 6%): different code. Item 4 key not published as a table.
2026-10-28 key matching: Pignerol petit chiffre 1690 key (targets/feuquieres, 167 groups) covers 247/591 tokens; decode scores -3.70/char (4-gram) vs -2.98..-4.06 for relabelled nulls (grid_test-style). Does not fit.
2026-10-28 hypothesis: grid layout (column = initial letter, Item 4/8B): residues mod k=5..30 of the 339 high tokens, permutation null: no k significant (best z 0.88 at k=13).
2026-10-28 control: grid_control.py builds a true grid code (k=10,13,18) at 591 tokens; grid_test.py does not detect it either (z<=0.9). Test underpowered; real result uninformative.
2026-10-28 crib consistency: the 5 contexts of 41 269 give [291 10], [10 66], [17 66], [17 10]; with 10=17 a doubled unit after "41 269" fits Norbert's "l'armee"; with the ordered-letters guess 10/17 sit in the c-e region, so "ee". Not testable further without a key: unconfirmed.
2026-10-28 estimate (sibling_need.py): a deciphered sibling in the same code of ~200 tokens would give values for ~70% of this letter's tokens, ~400 tokens for ~85%, ~1000 for ~97% (optimistic: assumes the same group distribution).
2026-10-28 literature (subagent): Aargau catalogue blocked by a JS check; AH 167/50 neighbour; Vault II/III read for Sept 1702: no 15 Sept letter; 1819 Memoires t. III unreachable; no Catinat 1702 key found (research_found.md).
2026-10-28 identification: Vault II: camp under Strasbourg from 14 Sept, HQ Eckbolsheim -> "Ingleshem" = probably Lingolsheim, not Ingenheim (left 30 Aug). Checked in the archive.org OCR.
