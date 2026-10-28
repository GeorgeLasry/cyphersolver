# NARA triage slice J: coverage per record group

Generated 27 Oct 2026 from the slim subsets (`out/<rg>_slim.jsonl`, made by `slim.py` from `out/<rg>_all.jsonl`); conclusions
from `review_j.py` reads (see README). Counts are the slim counts (all non-frame hits; frames = top frame per 60 items); the
phrase count in the review files after boilerplate filtering is given in brackets.

| record group | desc | phrase | word | frame | letters | caps | read / sampled, conclusion |
|---|---|---|---|---|---|---|---|
| rg_64 | 17 | 2039 (1305) | 75592 | 60 (31788 items in slim_items.tsv) | 1013 | 102806 | NARA's own records incl. digitised State Dept decimal-file microfilm (M274/M314 Mexico, M336 Germany, M316 Russia, M329 China, M353 Turkey ...), War Dept annual reports, Army morning reports, Russian consulate records (M1486). All 126 non-"in cipher" phrase hits read; 1,179 "in cipher/cypher" grouped by publication and sampled: own-government telegram boilerplate, garbles repeated, Signal Service weather ciphers, Fleet Problem exercise traffic. M1486 roll 83 target 2 (naId 571170362) = Russian MFA cipher circulars to the New York consulate 1891-1910 with keys 381/389/400/402/448 and naval keys 383/394 -> ROW. M336 roll 64 (naId 574876562) = the German Lima traffic of 1917, already catalogue 658 (file found scanned; update, not a row). Lokke "Official Ciphers - Livingston 1801-1804" (26025477) not digitised, key lead. APC code books / captured German crypto = accession dossiers, not digitised. Numeric frames = tables |
| rg_24 | 28 | 41 | 659 | 60 | 3 | 9003 | Bureau of Naval Personnel: deck logs ("key lost/missing" in 1957-78 logs, numeric positions), personnel files with Cypher surnames, WWII civilian-internee/casualty code book in POW records. No row |
| rg_29 | 184 | 22 | 1073 | 60 | 13 | 1362 | Census: Soundex index cards marked "Undeciphered" (illegible names), 1950 enumeration-district descriptions, territory punch-card code keys. No row |
