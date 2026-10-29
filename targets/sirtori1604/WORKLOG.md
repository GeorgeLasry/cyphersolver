# WORKLOG, sirtori1604 (catalogue 358)

- 2026-10-28 access: BDH record bdh0000174344 and bnedigital.bne.es answer 403 to scripts and show a Cloudflare "verify you are human" page in the browser; not passed. Took Pelling's 2012 copies of ff. 85, 86r, 86v (~950x1480 px) and Gomez's key image from ciphermysteries.com.
- 2026-10-28 literature: Cryptiana valle.htm (episode, folios, f. 90 dated 7 Oct 1604); Cipher Mysteries post and comments (Gomez stream, Caballero's Latin, his own caveats). No decipherment anywhere.
- 2026-10-28 transcription: copied Gomez's 747-sign stream and Caballero's word-divided f. 85 into transcription/.
- 2026-10-28 statistics: Gomez stream IC 1.84 (x26); '3' follows F/B 76 of 85 times.
- 2026-10-28 statistics: f. 85 body has 94 words (own count on the image = Caballero's), 206 signs, 2.19 signs/word. Corpora: letters/word es 4.27, it 4.69, la 5.68; consonants/word es 2.22, it 2.40, la 3.03. Letter-for-letter substitution excluded; consonant signs + vowel marks (Spanish) fits.
- 2026-10-28 solver: first many-to-one anneal collapsed to 'iiii' (Roman numerals in the corpus); fixed by dropping numeral tokens and swap-only moves on a frequency-matched key.
- 2026-10-28 solver: swap-only moves could not reach keys with more homophones than the frequency start (Italian control 0%); added reassignment moves, a cap of 2x each letter's share, stricter numeral filter, and restart 0 from the unshuffled frequency key. Controls at 747 symbols / 29 signs: es 99%, la 99%, it 100%.
- 2026-10-28 hypothesis: consonant skeleton. Mean fits Spanish (2.22 consonants/word) but the distribution does not (f. 85: 98% of groups 1-3 signs; Spanish consonant counts 17% at >=4). Ruled out. Skeleton-substitution controls only reach 7-18%: that solver test is underpowered and says nothing.
- 2026-10-28 hypothesis: groups = syllables spelled letter by letter. Lengths fit (13/59/26/3% vs Spanish syllables 8/56/29/6%), but vowel_set_test.py finds no set of 4-6 signs occurring once per group (64%; shuffled controls 60-63%; real Spanish syllables 89%). Ruled out.
- 2026-10-28 access: second try at bnedigital.bne.es card 0000174344: still the Cloudflare check. ff. 83-84, 88-90 not seen.
- 2026-10-28 statistics: position_test.py: signs have preferred places in the groups (skew 0.41; shuffled median 0.24, 99th pct 0.33). Initial-leaning I E S V; final-leaning O Q G (Caballero's labels). Groups are structured units.
- 2026-10-28 solver: full battery (results/stream_runs.json). Full-letter substitution, raw stream: controls es 99%, it 100%, la 99%; real -2.78/-2.70/-2.65 vs controls -1.81/-1.78/-2.15. Ruled out. Merged F3/B3: la control 99%, real -2.61 vs -2.16; es 48%, it 0% (search trap). Skeleton models: controls 3-24%, underpowered.
