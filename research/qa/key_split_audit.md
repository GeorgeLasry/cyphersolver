# QA report: one entry per key

Date: 14 Oct 2026. Snapshot: `origin/main` at 542ae56f9.

## Why

George Lasry, email of 14 Oct 2026:

> In general, solutions should be presented by keys/ciphers. Combining two entries with different ciphers just
> because they have something else in common (same collection, or same recipient, or same sender) is highly
> confusing and error prone.

This report checks every target in the ledger for that problem. It changes no target. The fixes it proposes
are for review; each one agreed will go in as its own commit.

## Method

1. A script read all 384 `targets/*/profile.json` with their `NOTES.md`. It scored each target on these signals:
   more than one method in `outcome.parts`, phrases such as "different key", "second cipher" or "two codes",
   more than one key record cited, more than one issuing country, a date span over five years, and more than
   three documents.
2. Everything scoring 3 or more was reviewed by hand, together with every multi-document target George solved
   or has a prior solution for. That came to 90 targets. Four reviewers (Claude agents) read each target's
   NOTES, profile and site page and gave it one of four verdicts:
   - **MIXED**: one entry (folder, profile, page or README row) groups documents written in different keys.
   - **SPLIT-OK**: several keys, but each key's documents already have their own `outcome.parts` and page section.
     Leftovers are noted.
   - **SINGLE**: one key throughout.
   - **UNCLEAR**: the files do not say.
3. The 294 targets left out scored low: most hold one document. A target with one document can still mix keys
   inside it (a cipher plus a separate code), but that is not the problem George raised.

## Results

Of the 90 targets reviewed: **37 MIXED**, 6 SPLIT-OK, 4 UNCLEAR, 43 SINGLE.

### George's entries

These need attention first, because his credit can read as covering documents he did not solve:

- **riksarkivet1628**: R4282 is listed as "not read". George's separate entry `decode4282` has it deciphered
  from the ciphertext alone (merged today, PR #33). The paper data now counts it twice, with opposite outcomes.
  The same entry also files R4284 and R4306, two unrelated ciphers, under the Bremen key.
- **vasto1527**: three systems (Cipher 1 for no. 10, Cipher 2 for no. 6, Ranzo's code for no. 20) share one
  outcome, "read with known key". The pooled fraction is stale. The Ranzo part credits Rosson only.
- **louis1615**: two unrelated keys are grouped only because DECODE gives Louis XIII as author. They are the
  Sabran 1631 key (R2748, George's prior solution) and the Brulart 1615-18 key (R2785/R2786, Tomokiyo).
- **gramont1529**: four letters in four of George's keys share one method, with no parts. The Mâcon 1537 letter
  uses the Mascon key, which belongs with `rome1536`.
- **hm1645**: six letters in four of George's SP 106 keys are filed as "read with known key". Only SP106-5 was
  applied here; the others are "read from existing decipherment".
- **matignon1586**: the README row mixes Cipher-1 (28%) and Cipher-3 (96%). George's f. 43 credit is for a leaf
  that is not among the target's documents.
- **segur**: f. 333 was read with Tomokiyo's f. 321 key, a different key. It sits under the ff. 233/239/288v
  ciphertext-only outcome. Question for George: which folios does your 2024 solution cover?
- **superscript, dandini1580, esp318, rome1536, siena1421**: the Gilino key (R8572) and Ghinucci (R8613) are
  already split in the README, but the profile still has one system and one credit. In `dandini1580`, the R73
  decryption is logged as "key used", not as George's prior solution. In `esp318`, the no. 95 key is credited
  across nos. 92-95. In `rome1536`, R4248 is a second cipher. `siena1421` still lists nos. 6/24, which are read
  in `siena1431`.

### The worst of the rest

- **potocka1714**: Potocka's key reads 95.3%. The target shows "read in part, 75.5%" only because Mniszech's
  letter R7524, in another key, is unread.
- **r1871**: two despatches 122 years apart (1558, 1680) share "read from existing decipherment". The 1680
  decipherment was never found.
- **sp106box10**: at least four systems sit under one "read with known key". The known key's own letter, R657,
  is not read.
- **sieniawski1708, kaa4591, champagne1590, sessa1593, caprile1519**: summary, method and fraction describe one
  key and are pooled over the others.
- **michell1751, nevers1593, bl32305, throckmorton**: the README rows claim more than the per-key results
  support.

### Why it happens

- **No key field per document.** `profile.json` has no field saying which key a document uses. The schema
  knows keys only through one `system` block and the optional `outcome.parts`, so nothing catches a merge.
  Proposal: add `documents[].key`, a short key label, and have `_check_profile.py` require one
  `outcome.parts` item per distinct label, each with its own method and fraction.
- **Folders follow the source, not the key.** Targets were opened from a catalogue number, DECODE record group,
  volume or correspondent, and later documents of the same origin were added to them.
- **Pooled fractions.** A single `fraction_read` over several keys hides both the read and the unread parts.

### Proposed fix order

1. George's entries above (the riksarkivet1628/decode4282 double count first).
2. Targets where the merge changes a headline result (potocka1714, r1871, michell1751, vich1511, nevers1593).
3. The schema field and the checker rule, so new targets cannot merge keys.
4. The remaining MIXED targets. Most need `outcome.parts` per key; split the folder where the documents share
   only the archive.

Per-target findings follow, with each key, the documents it covers, where the record merges them and a
proposed fix. The raw reviewer output is in `key_split_findings.jsonl`.

## Summary table

| Target | Verdict | Lasry involvement | Keys |
|---|---|---|---|
| [dandini1580](../../targets/dandini1580/NOTES.md) | MIXED | prior solution of R73 (decryption D3191 + key D3190 on DECODE, 2020), recorded only as 'key or decipherment used' | 2 |
| [esp318](../../targets/esp318/NOTES.md) | MIXED | key or decipherment used (no. 95 alphabet, 2022) | 4 |
| [gramont1529](../../targets/gramont1529/NOTES.md) | MIXED | key or decipherment used (2023 GL.htm tables, all four keys); prior solution (decoded all four texts 2023, unpublished) | 4 |
| [hm1645](../../targets/hm1645/NOTES.md) | MIXED | key or decipherment used (four reconstructed keys + plaintexts on DECODE, 2020); effectively prior solution of all six | 4 |
| [louis1615](../../targets/louis1615/NOTES.md) | MIXED | prior solution of R2748 (Sabran 1631 cipher, 2022) | 2 |
| [matignon1586](../../targets/matignon1586/NOTES.md) | MIXED | prior solution credit for fr. 15572 f. 43 (2022), a leaf excluded from the target | 3 |
| [riksarkivet1628](../../targets/riksarkivet1628/NOTES.md) | MIXED | solution of R4282 (in the separate target decode4282, 14 Oct 2026); not reflected here | 6 |
| [rome1536](../../targets/rome1536/NOTES.md) | MIXED | key or decipherment used (2023 re-tabulation of Mascon's cipher, GL.htm) | 2 |
| [segur](../../targets/segur/NOTES.md) | MIXED | prior solution (unpublished 2024, scope not stated per folio) | 3 |
| [siena1421](../../targets/siena1421/NOTES.md) | MIXED | none in profile credits (Lasry solved nos. 6/24, now in siena1431) | 8 |
| [vasto1527](../../targets/vasto1527/NOTES.md) | MIXED | key or decipherment used (Cipher 2, no. 6); prior solution (Cipher 1, no. 10); solution (Ranzo code, 14 Oct 2026) | 3 |
| [affry1757](../../targets/affry1757/NOTES.md) | MIXED |  | 2 |
| [beatrice1482](../../targets/beatrice1482/NOTES.md) | MIXED |  | 3 |
| [benedict1399](../../targets/benedict1399/NOTES.md) | MIXED |  | 3 |
| [bl32305](../../targets/bl32305/NOTES.md) | MIXED |  | 4 |
| [caprile1519](../../targets/caprile1519/NOTES.md) | MIXED |  | 3 |
| [castelcicala1816](../../targets/castelcicala1816/NOTES.md) | MIXED |  | 2 |
| [champagne1590](../../targets/champagne1590/NOTES.md) | MIXED |  | 4 |
| [geertruidenberg](../../targets/geertruidenberg/NOTES.md) | MIXED |  | 2 |
| [ilten1697](../../targets/ilten1697/NOTES.md) | MIXED |  | 2 |
| [kaa4591](../../targets/kaa4591/NOTES.md) | MIXED |  | 9 |
| [maisse1592](../../targets/maisse1592/NOTES.md) | MIXED |  | 2 |
| [michell1751](../../targets/michell1751/NOTES.md) | MIXED |  | 2 |
| [nevers1593](../../targets/nevers1593/NOTES.md) | MIXED |  | 2 |
| [papai1706](../../targets/papai1706/NOTES.md) | MIXED |  | 2 |
| [potocka1714](../../targets/potocka1714/NOTES.md) | MIXED |  | 2 |
| [r1871](../../targets/r1871/NOTES.md) | MIXED |  | 2 |
| [rakoczi1704](../../targets/rakoczi1704/NOTES.md) | MIXED |  | 3 |
| [sessa1593](../../targets/sessa1593/NOTES.md) | MIXED |  | 2 |
| [sieniawski1708](../../targets/sieniawski1708/NOTES.md) | MIXED |  | 5 |
| [sp106box10](../../targets/sp106box10/NOTES.md) | MIXED | none (his SP 106 keys tested on R931, do not fit) | 4 |
| [thurloe](../../targets/thurloe/NOTES.md) | MIXED |  | 4 |
| [transylvania1645](../../targets/transylvania1645/NOTES.md) | MIXED |  | 3 |
| [vanreede1787](../../targets/vanreede1787/NOTES.md) | MIXED |  | 2 |
| [vich1511](../../targets/vich1511/NOTES.md) | MIXED |  | 2 |
| [windischgraetz1720](../../targets/windischgraetz1720/NOTES.md) | MIXED |  | 2 |
| [wod1568](../../targets/wod1568/NOTES.md) | MIXED |  | 3 |
| [dubellay](../../targets/dubellay/NOTES.md) | UNCLEAR | prior solution (re-solved the 1528 cipher in 2022, GL.htm) - credited on a profile whose documents are all 1529 | 2 |
| [charlesi](../../targets/charlesi/NOTES.md) | UNCLEAR |  | 2 |
| [sp95box136](../../targets/sp95box136/NOTES.md) | UNCLEAR |  | 2 |
| [throckmorton](../../targets/throckmorton/NOTES.md) | UNCLEAR |  | 3 |
| [superscript](../../targets/superscript/NOTES.md) | SPLIT-OK | solution (Gilino R8572 edition, ciphertext-only per his notes) | 2 |
| [ferdinand3](../../targets/ferdinand3/NOTES.md) | SPLIT-OK |  | 3 |
| [malsburg1637](../../targets/malsburg1637/NOTES.md) | SPLIT-OK |  | 2 |
| [rupert](../../targets/rupert/NOTES.md) | SPLIT-OK |  | 4 |
| [sanchez1522](../../targets/sanchez1522/NOTES.md) | SPLIT-OK |  | 2 |
| [soria1523](../../targets/soria1523/NOTES.md) | SPLIT-OK |  | 2 |
| [alessandrino1568](../../targets/alessandrino1568/NOTES.md) | SINGLE | key or decipherment used (2020 polyphonic key on R93-R102, R115) | 1 |
| [egmond](../../targets/egmond/NOTES.md) | SINGLE | prior solution (2023 key, GL.htm s.2); pointer | 1 |
| [labbe1582](../../targets/labbe1582/NOTES.md) | SINGLE | verification (independent ciphertext-only solution, Oct 2026) | 1 |
| [mellon136](../../targets/mellon136/NOTES.md) | SINGLE | prior solution credit: transcription of p. 24 (2022), used as a check | 1 |
| [nuncio1566](../../targets/nuncio1566/NOTES.md) | SINGLE | key or decipherment used (reconstructed key on DECODE R85-R90, 2020) | 1 |
| [nunzio1718](../../targets/nunzio1718/NOTES.md) | SINGLE | key or decipherment used (S364 key and segmented decipherment on DECODE R154-R177, 2020) | 1 |
| [nunzio1736](../../targets/nunzio1736/NOTES.md) | SINGLE | key or decipherment used / prior solver: key 'ASV - S423' and segmented decipherment of all 11 items (24 Oct 2020) | 1 |
| [pallotto1629](../../targets/pallotto1629/NOTES.md) | SINGLE | pointer (identified that 6960 uses the 6956 key) | 1 |
| [r1892](../../targets/r1892/NOTES.md) | SINGLE | prior solution (solved independently 2021, unpublished) | 1 |
| [rupert1645](../../targets/rupert1645/NOTES.md) | SINGLE | key or decipherment used (King-Queen key 'TNA SP106-5', DECODE R929, 2020, applied unchanged) | 1 |
| [siena1431](../../targets/siena1431/NOTES.md) | SINGLE | solution (key recovered ciphertext-only, readings of nos. 6 and 24) | 1 |
| [vatican5](../../targets/vatican5/NOTES.md) | SINGLE | transcription (MysteryTwister 2019) and pointer | 1 |
| [battier1686](../../targets/battier1686/NOTES.md) | SINGLE |  | 1 |
| [buda1489](../../targets/buda1489/NOTES.md) | SINGLE |  | 1 |
| [catinat1691](../../targets/catinat1691/NOTES.md) | SINGLE |  | 1 |
| [cobham1588](../../targets/cobham1588/NOTES.md) | SINGLE |  | 1 |
| [eichel1758](../../targets/eichel1758/NOTES.md) | SINGLE |  | 1 |
| [estrada1503](../../targets/estrada1503/NOTES.md) | SINGLE |  | 1 |
| [fagel1804](../../targets/fagel1804/NOTES.md) | SINGLE |  | 1 |
| [ferdinand1619](../../targets/ferdinand1619/NOTES.md) | SINGLE |  | 1 |
| [harley287](../../targets/harley287/NOTES.md) | SINGLE |  | 1 |
| [hesse1603](../../targets/hesse1603/NOTES.md) | SINGLE |  | 1 |
| [jantini1517](../../targets/jantini1517/NOTES.md) | SINGLE |  | 1 |
| [joyeuse](../../targets/joyeuse/NOTES.md) | SINGLE |  | 1 |
| [lanssac](../../targets/lanssac/NOTES.md) | SINGLE |  | 1 |
| [lebel1593](../../targets/lebel1593/NOTES.md) | SINGLE |  | 1 |
| [lee1526](../../targets/lee1526/NOTES.md) | SINGLE |  | 1 |
| [lopehurtado](../../targets/lopehurtado/NOTES.md) | SINGLE |  | 1 |
| [lorraine1592](../../targets/lorraine1592/NOTES.md) | SINGLE |  | 1 |
| [maria1435](../../targets/maria1435/NOTES.md) | SINGLE |  | 1 |
| [ormonde](../../targets/ormonde/NOTES.md) | SINGLE |  | 1 |
| [ottobon](../../targets/ottobon/NOTES.md) | SINGLE |  | 1 |
| [r4157](../../targets/r4157/NOTES.md) | SINGLE |  | 1 |
| [raince](../../targets/raince/NOTES.md) | SINGLE |  | 1 |
| [rennes1563](../../targets/rennes1563/NOTES.md) | SINGLE |  | 1 |
| [sanchez1523](../../targets/sanchez1523/NOTES.md) | SINGLE |  | 1 |
| [smith1562](../../targets/smith1562/NOTES.md) | SINGLE |  | 1 |
| [sperantio1534](../../targets/sperantio1534/NOTES.md) | SINGLE |  | 1 |
| [stowe166](../../targets/stowe166/NOTES.md) | SINGLE |  | 1 |
| [toulon1803](../../targets/toulon1803/NOTES.md) | SINGLE |  | 1 |
| [warsaw](../../targets/warsaw/NOTES.md) | SINGLE |  | 1 |
| [wesselenyi1664](../../targets/wesselenyi1664/NOTES.md) | SINGLE |  | 1 |
| [windischgraetz1721](../../targets/windischgraetz1721/NOTES.md) | SINGLE |  | 1 |

## Entries that combine documents in different keys (37)

### dandini1580  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** prior solution of R73 (decryption D3191 + key D3190 on DECODE, 2020), recorded only as 'key or decipherment used'

| Key / cipher | Documents | Outcome |
|---|---|---|
| Lasry's key D3190 (even-second-digit letter homophones + 3-digit^ nomenclator) | R73 (ASV Francia 283C ff. 89r-90r) | read from existing decipherment (Lasry 2020); 32 illegible groups, 5 nomenclator groups open |
| R72 letter key (same frame and nomenclator, different letter assignment), rebuilt here by DP parse + swap annealing, then aligned with the leaf's decipherment | R72 (f. 52, 16 May 1580) | text read at the time (contemporary decipherment below the figures); key recovered here (ciphertext-only anneal within Lasry's frame, confirmed on adjacent plaintext) |

**Where it is merged:** Grouped by sender/recipient and volume. NOTES ('## Two keys in one frame', NOTES.md:21) and the page (sections 02/03) separate the two keys clearly, but the profile has no outcome.parts: one outcome.method 'read from existing decipherment' for both, system.summary merges them into one frame description, fraction_read 'unknown'; Lasry's role on R73 is logged as 'key or decipherment used' rather than 'prior solution'.

**Risk:** Lasry's R73 solution is not recorded as his prior solution in the paper data; the R72 key reconstruction (our own work) and Lasry's R73 reading collapse into one 'existing decipherment' outcome; a reader of the README row may think Lasry's key reads R72 (it 'gives nonsense on R72', NOTES.md:24).

**Proposed fix:** Add outcome.parts: R73 'read from existing decipherment' (credit lasry, prior solution); R72 'read from existing decipherment' for the text plus contribution 'key recovered' for the letter key. Optionally split into dandini1580-r72 and dandini1580-r73.

**Evidence:** NOTES.md:15-17 'Decrypted by George Lasry'; NOTES.md:21-27 'It reads R73 but gives nonsense on R72 ... a different letter assignment'; profile credits lasry role 'key or decipherment used'; no outcome.parts; README.md:336

### esp318  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (no. 95 alphabet, 2022)

| Key / cipher | Documents | Outcome |
|---|---|---|
| EscrivÃ  no. 1 key | no. 5 (ff. 5-6v, 11 Jan 1497) | read from existing decipherment (Parisi 2020) |
| Cifra general de los RRCC (Galende DÃ­az 1994) | no. 92 (f. 116r-v, 17 Aug 1500) | read with known key, ~3/4 |
| Lasry 2022 alphabet (no. 95) | no. 95 (f. 122r-v, 8 Jan 1497) | read with known key in stretches, ~2/3 of f. 122r; f. 122v unread |
| suspected Gran cifra 1501-04 (not obtained) | nos. 93, 94 | not solved |

**Where it is merged:** Grouped by volume (BnF Espagnol 318 / catalogue item 9). Profile has one system block ('a different key per letter', system.notes 'Five letters under at least four keys'), one outcome.method 'read with known key', one fraction_read 0.4 (an estimate by letter averaging five keys), no outcome.parts; one README row (README.md:298) and one page. Page sections per letter (no5, no92, no95, no9394) do separate them, but the profile/README do not.

**Risk:** Paper data credits a single 'read with known key' outcome across letters where no. 5 is a prior print, no. 92 a Galende key, no. 95 Lasry's key and 93/94 unread; the 0.4 fraction mixes keys; Lasry's key credit at entry level may read as covering nos. 92-94; system.nomenclator entries 683 is the Cifra general count applied to all.

**Proposed fix:** Add outcome.parts per letter/key (no. 5 read from existing decipherment; no. 92 read with known key Cifra general; no. 95 read with known key Lasry 2022, partial; nos. 93-94 not solved); scope Lasry's credit to no. 95; or split into esp318-no92, esp318-no95 (Lasry), esp318-no93-94, with no. 5 as prior-solved note.

**Evidence:** profile system.summary 'a different key per letter'; system.notes 'Five letters under at least four keys'; outcome.notes fraction 'an estimate by letter'; NOTES.md:139-142, 176-178

### gramont1529  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (2023 GL.htm tables, all four keys); prior solution (decoded all four texts 2023, unpublished)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Avranches' cipher 1 (= Tomokiyo fr. 3005 f. 107) | langeac1529 = BnF fr. 3083 no. 8 ff. 20-21 (Langeac, Venice, 14 Jan 1529) | read with known key (Lasry); read in full bar two short groups |
| Gramont's cipher (1529) (= fr. 3040 f. 16, Clair. 330 f. 53) | gramont1529 = fr. 3091 no. 23 ff. 45r-47v (11 Oct 1529) | read with known key (Lasry); read in full |
| Gramont's cipher (1530) (= fr. 3019 f. 20) | gramont1530 = fr. 3071 no. 7 f. 17 (21 July 1530) | read with known key (Lasry); ~85% |
| Mascon's cipher (= fr. 3053; same key as target rome1536) | macon1537 = fr. 3071 no. 4 ff. 9-10 (11 Apr 1537) | read with known key (Lasry); ~90%; f. 9bis contemporary slip agrees |

**Where it is merged:** Four letters by three writers in four different keys grouped only as catalogue item 6 / recipient Montmorency. profile.json has one system (system.summary 'Four separate keys, each a homophonic substitution...' profile; system.types merged), one outcome.method 'read with known key' and outcome.parts = null, fraction_read 'unknown'. README row (README.md:267) is one row 'complete' for 'Gramont, MÃ¢con and Langeac'. The page does have one h2 per letter (langeac, tarbes, cardinal, macon), so the per-letter reading is visible, but nothing per key in the profile. The MÃ¢con 1537 letter is in Mascon's cipher, the same key as rome1536 (fr. 3053), yet sits in a different entry from its key-siblings.

**Risk:** Paper statistics treat four keys as one 'system' and one solve; key-level counts (number of Lasry keys applied) are undercounted by 3; the 'read'/complete status hides that Gramont 1530 is ~85% and MÃ¢con ~90%; Mascon's cipher is reported under two targets (gramont1529 and rome1536) with no cross-link at key level, so its statistics and corrections (rome1536 'split by sign shape', curly X = Q/U) may not be applied to the 1537 letter.

**Proposed fix:** Add outcome.parts with one part per key (Avranches 1, Gramont 1529, Gramont 1530, Mascon) each with records, method, extent and measured fraction; or split into four profiles. Preferably move fr. 3071 no. 4 (MÃ¢con 1537) to the Mascon's-cipher entry with rome1536 (or cross-reference it there as a part). README: one row per key or at least name the four keys in the row title.

**Evidence:** targets/gramont1529/NOTES.md:7 'each letter has its own key'; NOTES.md:15-18 key table; profile.json system.summary 'Four separate keys'; outcome.parts null; README.md:267 'Four letters, four keys (not three)'; NOTES.md:18 macon key = "Mascon's cipher" (= fr. 3053)

### hm1645  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (four reconstructed keys + plaintexts on DECODE, 2020); effectively prior solution of all six

| Key / cipher | Documents | Outcome |
|---|---|---|
| Lasry 'TNA SP 106' (Sept 1645, homophonic, words 124+) | R785 (ff. 213-215), R790 (ff. 230-232), R923 (ff. 233-234) | read from Lasry's existing decipherment; not checked here |
| Lasry 'SP106-2' (July-Aug 1645, homophonic with nomenclator) | R787 (ff. 216-217, French) | read from Lasry's existing decipherment; not checked here |
| Lasry 'SP106-8' (Jan 1646, numbered word list 100+) | R924 (ff. 235-236) | read from Lasry's existing decipherment; not checked here |
| Lasry 'SP106-5' (Jan 1646, letter+digit nomenclator; also the King-Queen key used for rupert1645) | R929 (f. 247) | key applied here independently to Pettersson's transcription; matches Lasry's plaintext |

**Where it is merged:** Six letters in four of Lasry's keys grouped by correspondence (household -> Charles I) and volume (SP 106/10 ff. 213-247). NOTES has a clear per-record key table and the page has a 'letters and the keys' section, but profile.json has one system (summary 'four key periods per Lasry'), parts = null, one outcome.method 'read with known key' and class 'already solved' for all six; documents[] carry no key. The only check done here (SP106-5 on R929) is reported as if for the target. Siblings R752, R788, R789, R925, R928 (catalogue 54, 55, 60) are declared 'resolved' (outcome.notes) without being documents.

**Risk:** Method 'read with known key' suggests the project applied keys to all six; it applied one key to one letter and took Lasry's plaintexts for five (method should be 'read from existing decipherment' for those). Per-key Lasry credit is lost for the paper; catalogue 54/55/60 closed with no record in the profile.

**Proposed fix:** Add outcome.parts per Lasry key (TNA SP 106: R785, R790, R923; SP106-2: R787; SP106-8: R924; SP106-5: R929) with method 'read from existing decipherment' for the five unchecked and 'read with known key' for R929; list the sibling records or give them their own entries.

**Evidence:** targets/hm1645/NOTES.md:13-17 four keys 'one per key period'; NOTES.md table rows R785 ... 'TNA SP 106', R787 'SP106-2', R924 'SP106-8', R929 'SP106-5'; NOTES 'Check done here: Applied Lasry's SP106-5 alphabet to ... f. 247 (R929)'; profile.json outcome.parts null, method 'read with known key'

### louis1615  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** prior solution of R2748 (Sabran 1631 cipher, 2022)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Louis XIII-Sabran cipher of 1631 (letters, digits, signs; Lasry's key on cryptiana GL.htm) | R2748, BnF Baluze 155 f. 79-80, 28 Mar 1631 | solved by Lasry 2022 (read from existing decipherment; key not re-applied here) |
| Brulart de Leon cipher of 1615-18 (figures with diacritics; Tomokiyo's reconstruction) | R2785 (fr. 18043 f. 83-84, 15 Sep 1615), R2786 (fr. 18044 f. 109-110, 25 Jul 1617) | read by Tomokiyo 2021, residue unread (probably nulls) |

**Where it is merged:** NOTES itself says 'The catalogue grouped three unrelated items because DECODE lists all three with Louis XIII as author' (NOTES.md:9), yet one profile holds both keys: system.summary 'Two different keys', system.types merged, one outcome.method 'read from existing decipherment', fraction_read 'unknown', no outcome.parts; title joins Sabran 1631 and Brulart 1615/1617. No page or README row (Status: no write-up), but the profile still feeds the paper data.

**Risk:** In the paper export one record credits Lasry and Tomokiyo jointly for a 3-document target; Lasry's 1631 solution is counted together with Tomokiyo's 1615-17 work, and the 1615-17 residue (unread passages) is hidden under the same outcome; system statistics (types, symbol kind) mix two unrelated ciphers.

**Proposed fix:** Split into two folders/profiles: sabran1631 (R2748, Lasry prior solution, sibling fr. 4134/4135) and brulart1615 (R2785, R2786, Tomokiyo). Or at minimum add outcome.parts per key with records and credit each solver only on his part.

**Evidence:** NOTES.md:9 'The catalogue grouped three unrelated items'; NOTES.md:11-15 table (R2748 Lasry 2022; R2785/R2786 Tomokiyo 2021); profile system.summary 'Two different keys: the Brulart de Leon cipher of 1615-18 ... and the 1631 Sabran cipher'; outcome.parts null; credits tomokiyo + lasry

### matignon1586  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** prior solution credit for fr. 15572 f. 43 (2022), a leaf excluded from the target

| Key / cipher | Documents | Outcome |
|---|---|---|
| Mayenne-Forget Cipher-1 (Tomokiyo partial tables, re-derived) | fr. 15572 ff. 110, 123-124, 143r/v, 150, 154, 173, 196, 201; fr. 15571 f. 177 (all 13 profile documents) | read with known key, read in part, 28% measured |
| Matignon Cipher-3 (Tomokiyo partial table) | fr. 15572 f. 276; fr. 15571 f. 179 (not in documents[]; f276/, f179/) | read with known key by alejandrozarco PR #25, 96.2% and 92.9%, not in the total |
| Mayenne-Forget Cipher-2 (f. 79r crib) | mentioned only (NOTES:25, :271) | not part of the reading |

**Where it is merged:** One README row (README.md:303) and one target cover Cipher-1 and Cipher-3: the row says 'Partial, in progress (28% measured)' for Cipher-1 then appends 'Matignon's Cipher-3 leaves added ... f. 276 deciphered (96.2%)'. profile.json has no outcome.parts; documents[] lists only Cipher-1 leaves while outcome.credits carries zarco's Cipher-3 solution and Lasry's f. 43 prior solution, so credits describe documents not in the record. Title says 'in Mayenne-Forget Cipher-1' but the folder/row hold Cipher-3 too.

**Risk:** Paper data: zarco's Cipher-3 96% reading and Lasry's f. 43 credit attach to a Cipher-1 profile whose fraction 0.28 and method describe a different key; per-key statistics (Cipher-3 near-complete vs Cipher-1 28%) are blurred; Lasry appears as prior solver of a target he did not solve.

**Proposed fix:** Split Cipher-3 (ff. 276, fr. 15571 f. 179, with the deciphered siblings ff. 189, 277-280, 282) into its own folder/profile/README row (e.g. matignon1586c3) credited to zarco + Tomokiyo; keep matignon1586 Cipher-1 only; move Lasry's f. 43 credit out (or to a note, role 'pointer'), or give f. 43 its own record if it is a separate key.

**Evidence:** profile title 'in Mayenne-Forget Cipher-1'; NOTES.md:5-6 'Cipher-3 leaves f. 276 ... measured separately ... not yet in the total'; NOTES.md:21-23; NOTES.md:327-328; README.md:303; profile outcome.parts null; credits zarco 'Cipher-3 leaves f. 276 deciphered' and lasry 'f. 43 ... (left out of this target)'

### riksarkivet1628  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** solution of R4282 (in the separate target decode4282, 14 Oct 2026); not reflected here

| Key / cipher | Documents | Outcome |
|---|---|---|
| Bremen band key (6-column grid homophones) | R4330, R4331 (Bremen -> Salvius 1631) | key from adjacent plaintext (glosses), read in full |
| ~40-sign letter cipher | R4282 (lada II:113) | here 'not read'/'open'; actually key recovered ciphertext-only by Lasry, read (targets/decode4282, README row 58) |
| homophonic numbers (108 values) | R4284 (1628, Camerarius) | not solved |
| numbers 5-203 | R4306 (1632?) | not solved |
| Rusdorff numeric code | R4333-R4337 | surveyed, not worked (not in documents[]) |
| E 708 two-digit letter code + 4-digit nomenclator | R4338-R4341 | read in part at the time, not worked (not in documents[]) |

**Where it is merged:** Catalogue 207 grouped by archive ('four unrelated groups', NOTES.md:8). system.summary describes only the Bremen key; one outcome.method 'key recovered based on adjacent plaintext' for all; no outcome.parts; fraction_read 0.30 pools Bremen with three unrelated ciphers; page h2 'The three ciphers not solved' and NOTES.md:69 still list R4282 as unsolved/not-attempted although Lasry's decode4282 reads it.

**Risk:** Contradiction on Lasry's own solve: R4282 is 'not read' here and 'key recovered from ciphertext-only' in decode4282, so it is double counted with opposite outcomes in the paper data; README row 198 reads as one result for 14 records.

**Proposed fix:** Retitle riksarkivet1628 to Bremen 1631 (R4330/31) only, or turn it into a research/ survey; remove R4282 from documents (point to decode4282); give R4284 and R4306 their own attempted/open entries (or parts with 'not solved'); update page section 04 and NOTES gaps.

**Evidence:** profile system.summary 'Bremen 1631: two-digit homophonic ...'; documents R4282 read='not read'; NOTES.md:8 'four unrelated groups'; NOTES.md:69 'R4282 ... blocker: not-attempted'; docs/riksarkivet1628.html:80; README.md:58 (decode4282, 'Contributed by George Lasry'); docs/_build_site.py:712

### rome1536  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (2023 re-tabulation of Mascon's cipher, GL.htm)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Mascon's cipher (Tomokiyo reconstruction, Lasry 2023 table) | R4233, R4234, R4235, R4238, R4239, R4240, R4247 (BnF fr. 3053 ff. 6, 16, 21, 32, 35, 40, 77) | read with known key, read in part (~95% after pass 5) |
| second, unrelated fr. 3053 cipher (Tomokiyo's second fr. 3053 table) | R4248 (fr. 3053 f. 85; decipherment f. 86) | read from existing decipherment (contemporary clear decipherment f. 86); key not tabulated |

**Where it is merged:** profile.json has one system ('Homophonic substitution on digit-like graphic signs...' i.e. Mascon's only; notes add 'The f. 85 record (R4248) uses a second, unrelated fr. 3053 cipher'), one outcome.method 'read with known key' and parts = null, so R4248 is credited as read with Mascon's key (Tomokiyo/Lasry) although it was read from the f. 86 contemporary decipherment. fraction_read 0.95 mixes both. README.md:291 says 'every cipher passage of the eight records deciphered, seven in part; the eighth resolved'. The page does have a separate h2 id='second'. The Mascon's-cipher letter of 11 Apr 1537 (fr. 3071 no. 4) is filed under gramont1529 instead.

**Risk:** R4248 counted as a document read with Lasry's/Tomokiyo's Mascon key and with the same method; its glyph count and the system's distinct_symbols=50 could absorb a different cipher; paper's method tallies wrong for one document.

**Proposed fix:** Add outcome.parts: (1) Mascon's cipher, R4233-R4247, read with known key, partial ~95%; (2) second fr. 3053 cipher, R4248, read from existing decipherment, complete. Or move R4248 to its own small target. Cross-reference / move gramont1529's macon1537 document here as a Mascon's-cipher part.

**Evidence:** targets/rome1536/NOTES.md:13-14 'its cipher is not MÃ¢con's at all but a second fr. 3053 cipher'; NOTES.md:160-161 'MÃ¢con's key gives nonsense'; profile.json system.notes; outcome.parts null; docs/rome1536.html h2#second

### segur  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** prior solution (unpublished 2024, scope not stated per folio)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Navarre 1585-86 key A (letters 1-53, syllabary 54-123), recovered here | ff. 233, 239, 288v (f. 366 'probably this key', open) | key recovered from ciphertext-only; read in substance |
| Tomokiyo's f. 321 key (same design, letters shifted +8, syllabary 63-142, adds h/j rows) | f. 333 (and f. 321 key letter) | read with known key (Tomokiyo), extended by 24=f,34=l,36=m; blind re-derivation only under design assumption |
| f. 143 (1583) third key | f. 143 (not in documents[]) | not read |

**Where it is merged:** profile documents[] includes f333 alongside f233/f239/f288v/f366 under one system (summary gives key A's numbers 1-53/54-123 only) and one outcome.method 'key recovered from ciphertext-only', class 'read', no outcome.parts. f. 333 was read with Tomokiyo's different key (NOTES.md:152, :169, :175 'the f. 321 key is the ff. 233 key shifted'). f366 is unread but counted in the 'read' entry. README row (README.md:89) correctly names only ff. 233/239/288v, but page (docs/segur.html h3 'The rest of the volume, f. 333 and f. 366') and profile fold f.333 in.

**Risk:** f. 333 is counted as a ciphertext-only recovery in the paper data when it was read with a published key; Lasry's 'prior solution' credit applies to the whole entry including f.333/f.366 although his 2024 solve presumably concerned the Tomokiyo-listed letters; f366 (unread) inflates the 'read' class.

**Proposed fix:** Add outcome.parts: (1) ff. 233/239/288v key A, ciphertext-only; (2) f. 333 Tomokiyo f.321 key, read with known key; (3) f. 366 not solved. Or move f. 333 (and f. 321) to its own entry 'Navarre f.321 key'. Ask Lasry which folios his 2024 solution covers and scope the credit.

**Evidence:** profile sys.sibling_key 'Tomokiyo's f. 321 key (same design, shifted by eight) used to read f. 333'; outcome.notes 'f. 333 read with the sibling key; f. 366 left open'; no outcome.parts; NOTES.md:150-152,169-175

### siena1421  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** none in profile credits (Lasry solved nos. 6/24, now in siena1431)

| Key / cipher | Documents | Outcome |
|---|---|---|
| no. 25 own key (rebuilt ciphertext-only) | no. 25 (R4813) | key recovered ciphertext-only, 96.2% read |
| no. 18 own key (Ziegler articles) | no. 18 (R4806) | key recovered ciphertext-only, ~87% |
| no. 14 own key | no. 14 (R4802) | key recovered ciphertext-only, ~60% read in part |
| Borghesi 1456 key | no. 4 (R4793) | key from adjacent plaintext (fragment + recipient glosses), 114/144 |
| R4755 Cristofano | nos. 6, 24 (R4795, R4812) | solved by Lasry, moved to siena1431, still listed here 'read in part' |
| nos. 20+23 system | R4808, R4811 | unread, no key |
| separate unidentified keys | nos. 7, 11 (Acciaiuoli 1478), 17 (1528), R4794, 9/15/19/21 | unread |
| contemporary decipherments | nos. 8, 10, 13/16, 22; no. 12 DECODE 'Decrypted' | read at the time / existing decipherment |

**Where it is merged:** A whole busta (1421-1547) grouped by collection. system.summary admits 'each letter uses its own ... key ... so the system is per document', yet the profile has NO outcome.parts, one outcome.method 'key recovered from ciphertext-only' and one fraction_read 0.22 pooled over ~13,400 tokens of many keys; README row (README.md:75) is one row for 'the cipher letters of the Concistoro'.

**Risk:** No. 4 (glosses = adjacent plaintext) and contemporary/DECODE readings are scored as ciphertext-only; the 0.22 fraction is meaningless across 10+ systems; nos. 6/24 double-counted with siena1431 (Lasry's solve); per-key results (no. 25 96% read) are hidden under 'read in part'.

**Proposed fix:** Split per key: siena-no25, siena-no18, siena-no14, siena-no4 (Borghesi 1456) as their own targets (as siena1431 already was), leave siena1421 as a survey in research/ or at least add outcome.parts per letter with its own method and fraction; drop no06/no24 documents.

**Evidence:** profile system.summary 'each letter uses its own Sienese or foreign key'; outcome.parts absent; fraction_read_source 'no. 25 477/496, no. 18 1,271/1,459, no. 14 ~757/1,291, no. 4 114/144, over ~13,400'; NOTES.md:3, NOTES.md:290-301

### vasto1527  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (Cipher 2, no. 6); prior solution (Cipher 1, no. 10); solution (Ranzo code, 14 Oct 2026)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Gasto-Charles V Cipher 1 (Lasry 2023) | BnF fr. 3022 no. 10 (ff. 26-28 + f. 39) | read from existing decipherment (Lasry/Tomokiyo), partial, not reworked or measured |
| Gasto-Charles V Cipher 2 (Lasry 2026 key, extended here) | fr. 3022 no. 6 (ff. 16v-17v); no. 19 (ff. 40-43) same key, not transcribed | read with known key, 98.0% measured |
| Ranzo/Garbino code (initial letter + number) | fr. 3022 no. 20; fr. 2988 ff. 9-10 (DECODE R1894, copy R4450) | read from existing decipherment: Rosson key (79.8% no. 20, 93.1% R1894 in connected stretches) and Lasry's independent 871-entry key; not by us |

**Where it is merged:** Three different systems grouped by volume (fr. 3022) / catalogue item 7. outcome.parts are per key (good), but: system.summary 'Nos. 6/10: Caesar-shifted substitution ...' treats Cipher 1 and Cipher 2 as one system; system.types merges homophonic+code; single outcome.method 'read with known key' covers all; fraction_read 0.5485 pools Cipher 2 tokens with Ranzo-code groups and is stale ('no. 20: 0 of 1,321 groups') while parts say 79.8%; NOTES verdict table still says no. 20 'not solved'; Ranzo part basis names only Rosson, Lasry's 14 Oct solution is a credit but not in parts; README row title implies one del Vasto solution.

**Risk:** Paper/scoreboard counts one 'read with known key' result for what is three outcomes (one ours-with-Lasry-key, two others' readings); the pooled 54.85% is neither key's figure; Lasry's Ranzo solution and Cipher 1 reading may be credited to the 'del Vasto' entry as a whole or lost; Cipher 1 described with Cipher 2's key structure.

**Proposed fix:** Split into vasto1527 (Cipher 2: no. 6 + no. 19), vasto1527-cipher1 (no. 10, read from Lasry/Tomokiyo, no write-up or short) and ranzo1528 (no. 20 + R1894/R4450, Rosson and Lasry solutions). At minimum: per-key system entries, fraction_read only over no. 6, update no. 20 status, add Lasry to the Ranzo part's basis.

**Evidence:** profile system.summary 'Nos. 6/10: Caesar-shifted substitution'; NOTES.md:10 'Gasto-Charles V Cipher 1'; NOTES.md:22 '## No. 6 / Cipher 2'; NOTES.md:12 no. 20 '**not solved.**'; profile fraction_read_source 'no. 20: 0 of 1,321 groups'; NOTES.md:189 'George Lasry's independent Ranzo contribution'; README.md:297

### affry1757

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| d'Affry nomenclator ~1,200 groups (codes A+B, shown to be one code, key_U.json) | R1052, R1053, R1062-R1065, R1072, R1073, R1075, R1076 (A); R1054, R1066-R1070, R1074, R2067 (B) | key from adjacent plaintext (Lyonet's decipherments), 0.89 read as sense |
| code C (different) | R1071 (to Choiseul, 7 Aug 1757) | not solved |

**Where it is merged:** Grouped by sender and file (KHA inv. 192). Profile documents still list 'codeA' and 'codeB' as separate documents although NOTES.md:31-33 says they are one code; R1071 code C is included under the same method 'key recovered based on adjacent plaintext' with no outcome.parts; fraction 0.82 includes R1071 (0.89 without). system.summary does say 'R1071 in another code'.

**Risk:** Low: R1071's different code is counted under the main code's method and drags the fraction; profile's codeA/codeB split suggests two keys where there is one.

**Proposed fix:** Merge codeA/codeB into one document group (or label them 'one code'), move R1071 into its own attempted/open entry or an outcome.part 'not solved', and report 0.89 for the main code.

**Evidence:** profile system.summary 'R1071 in another code'; NOTES.md:31-33 'the cosine split reflects homophone habits, not two codes ... R1071 (C) is different'; fraction_read_source 'R1071 (761, code C) unread. Without R1071: 0.890'

### beatrice1482

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| 1482 graphic alphabet (old cipher) | R1140 (31 May 1482), R1141 (8 Jun 1482) | read from existing decipherment (MDE III 1877 nos. 10, 12) |
| 1486 graphic alphabet(s); March 1486 letter says a new key is enclosed, so March and May 1486 may differ | R1142 (8 Mar 1486), R1143 (2 May 1486, decipherment slips) | read from existing decipherment (MDE III no. 54, 75; IV suppl. 45; Berzeviczy 1914) |
| none (plain Italian letter) | R1154 (29 May 1505) | not applicable |

**Where it is merged:** Grouped by sender (Beatrice) and archive. RESULT.md itself warns 'the 1482 and 1486 alphabets look different; the old/new-cipher statement makes pooling all four letters under one key especially unjustified', yet profile has one system (types ['undetermined'], summary 'graphic substitution systems'), parts = null and one method for five records including a non-cipher; README.md:356 one 'complete' row.

**Risk:** Low for credit (all from print), but the paper would count one 'system' where there are two or three plus a non-cipher; R1154 counted as an 'already solved' cipher.

**Proposed fix:** Add outcome.parts: 1482 key (R1140-R1141), 1486 key(s) (R1142-R1143), R1154 not a cipher; or split R1154 out as not-a-cipher and keep per-key parts.

**Evidence:** targets/beatrice1482/RESULT.md:87 'pooling all four letters under one key especially unjustified'; profile.json system.notes 'Cipher alphabets differ; March 1486 closing states a new key is enclosed. R1154 is not a cipher.'; outcome.parts null

### benedict1399

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Benedict XIII's one-sign-per-letter substitution (20 values + dotted-V name sign + null separators), rebuilt from the p. 475 facsimile | benedict-1399-1403 (Benedict -> Climent; plate = letter XXXV, doc. 1068) | read from existing decipherment (Puig 1920); key rebuilt here, 91.4% of the plate confirmed |
| unverified: Puig says 'La clave o claves'; the entourage letters may share the key or not | entourage-1399-1416 (Santa Cruz, Exea, Comuel -> Climent, Puig app. XXIX, LXIV, CXVI, CXXXV) | read from existing decipherment (Puig); no image, key not checked on them |
| unknown key ('de clave desconocida') | vico-1398-line (Fr. Pedro de Vico -> Guillem Carbonell, 4 Dec 1398) | not read; not printed, no image |

**Where it is merged:** Grouped by archive (Climent's papers, ACB). One outcome.method 'read from existing decipherment', fraction_read 0.914 measured on the p. 475 plate only, no outcome.parts, while documents[] includes the Vico line in an explicitly different, unknown key (NOTES.md:123) and letters from other senders over 1399-1416 whose key was never checked. Puig's own note says 'La clave o claves' (NOTES.md, p. 466 quote), i.e. possibly more than one key. README row (README.md:340) presents Benedict and 'his circle' as one deciphered set.

**Risk:** The Vico 1398 line (unread, different key) is counted inside a 'read' target; the 91.4% sign-level confirmation and the rebuilt key are implied to cover the entourage letters (to 1416) which were not tested and may use other keys.

**Proposed fix:** Add outcome.parts: (1) Benedict letters, plate-checked key, read from existing decipherment; (2) entourage letters, read from existing decipherment, key unverified; (3) Vico 1398 line, not solved, different key. Or drop the Vico line into a separate open record. Say in system.notes that the key is verified only on doc. 1068.

**Evidence:** NOTES.md:123 'Sigue una lÃ­nea cifrada, de clave desconocida'; NOTES.md Puig p. 466 'La clave o claves que me han servido'; profile outcome.method 'read from existing decipherment', frac 0.914 (plate); documents vico-1398-line read 'not read'; outcome.parts null

### bl32305

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Paris 1719 two-part 3-figure code (~900 groups) | R2964 (f. 6), R2965 (f. 7) | not solved; ~12 contemporary glosses (33/354 groups) |
| 'Carre' 1742-45 two-part 3-figure code (~800 groups) | R2968, R2970, R2972 | not solved, 0 read |
| German 'Marquis' letter, figures for names/words | R2963 (f. 5) | read at the time (interlinear); not in documents[] |
| 2-figure letter cipher of 1749 | R2974 (ff. 25-28) | read at the time; not in documents[] |

**Where it is merged:** Grouped by volume (Add MS 32305, 'unidentified cipher keys'). NOTES.md:9-10 'They are not one correspondence'. One profile with system.summary covering two codes jointly, one outcome.method 'not solved', outcome.parts null, and fraction_read 0.09 that counts only the 1719 glosses (outcome.notes) but stands for the whole two-code set. credits 'R2963 and R2974 deciphered at the time' refer to records not in documents[]. README row (README.md:401) and page title join 1719 and Carre, date range '7 Feb 1719 - 17 Nov 1749' runs to R2974.

**Risk:** The 9% 'read' is applied to the Carre code, of which nothing is read; credits for R2963/R2974 readings attach to a target whose documents are all unread; two codes' sizes (900 vs 800) and stats blended.

**Proposed fix:** Split into bl32305-1719 (R2964/R2965, glosses 9%) and bl32305-carre (R2968/R2970/R2972, 0%); or add outcome.parts per code with own fraction_read; record R2963/R2974 as separate read-at-the-time documents or drop them from credits.

**Evidence:** NOTES.md:9-10 'They are not one correspondence'; NOTES.md:14,25,31; profile outcome.notes 'fraction_read counts the contemporary glosses in R2964 (33 of 354 groups)'; outcome.parts null; README.md:401

### caprile1519

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| 1520-21 homophonic sign cipher (rebuilt from Somogyi 2025 cribs) | R1139, R1136 (8 Mar 1520), V1921, R1138 (Somogyi), V1920 | key recovered based on plaintext from external sources; V1921 97.0%, R1139 89.7%, R1136 66.9% |
| 1519 two-tier cipher | R1128 (target); R1129-R1135 read at the time/1882 | R1128 not read; R1129-R1135 read from existing decipherments |
| Cistarelli two-digit numeric cipher | R1137 (catalogue 158, different sender) | fragments only, ciphertext-only anneal; effectively not solved |

**Where it is merged:** Three systems and two senders (catalogue 157 + 158) grouped by archive box (ASMo Ungheria b. 4) and mission. Profile system.types ['homophonic'] and distinct_symbols 49 describe only the 1520-21 cipher; one outcome.method 'key recovered based on plaintext from external sources' and one fraction_read 0.3 (estimated) across all; no outcome.parts. Single README row (README.md:118) and page title 'Caprile and Cistarelli'. NOTES table classes R1128-R1135 as '1519 two-tier' and R1137 'two-digit numeric' (NOTES.md:25-34).

**Risk:** Paper data attributes the external-crib key recovery to R1128 and R1137, which use different ciphers and are unread; Cistarelli (catalogue 158) appears read in part under Caprile's key; system statistics (49 signs, homophonic) misdescribe the 1519 and numeric systems.

**Proposed fix:** Split into caprile1520 (1520-21 key: R1136, R1138, R1139, V1920, V1921), caprile1519 (two-tier: R1128 + R1129-R1135 as key material, open) and cistarelli1520 (R1137, open); at minimum add outcome.parts per system and per-system system blocks.

**Evidence:** profile system.summary '1520-21: homophonic ... 1519: a two-tier sign cipher; Cistarelli: two-digit figure cipher'; outcome.notes 'R1128's two-tier system and R1137's numeric key are not'; NOTES.md:14-15,25-34

### castelcicala1816

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Neapolitan two-part syllabic homophonic code (~2,450 groups), key rebuilt from glosses | R9553-R9567, R9569-R9571, R9579, R9582-R9585, R9587, R9589 (25 docs) | key from adjacent plaintext, read in part (45% valued; R9569/R9571/R9589 read at the time) |
| different code, values 100-1100, pencil syllabic glosses | R9586, R9588 | not attempted, not solved |

**Where it is merged:** Mostly one code (catalogues 166+167 merged correctly by code), but R9586/R9588 are a different code included by shared busta/sender; system.summary describes only the main code; no outcome.parts; fraction_read_source says it 'Includes the different-code R9586/R9588'. Minor case.

**Risk:** Small: the two other-code letters dilute the 43% figure and are implicitly labelled with the main code's key and method.

**Proposed fix:** Move R9586/R9588 to a separate attempted/open entry (or an outcome.part 'not solved'), and exclude them from fraction_read.

**Evidence:** NOTES.md:34 'R9586 and R9588 are in a different code'; NOTES.md:126; profile fraction_read_source 'Includes the different-code R9586/R9588'; README.md:190 'R9586/R9588 another code'

### champagne1590

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| nine-entry name code, key slip bound on f. 36r | n23 = fr. 3623 no. 23 (Bienvenut, 28 Feb 1590, R9453) | read with known key (contemporary slip), complete |
| two-digit alphabetical homophonic alphabet + code numbers | n24-25-60 = fr. 3623 nos. 24, 25, 60 (June 1590, R9454, R9455, R9459) | key recovered based on adjacent plaintext (interlinear glosses), partial 63/104 |
| Nevers key no. 57 (fr. 3995 ff. 102-103, La Verriere/Lauriere, Feb 1593) | n55 = fr. 3625 no. 55 (9 Jul 1593); fr. 3625 no. 10 (13 Jul 1593, blind test, not a profile document); f3985_58 = fr. 3985 f. 58 (12 Aug 1593) | read with known key (identified by setsunaatto, issue 13); no. 55 85/86, f. 58 94.8% |
| unknown (one group of ~6 signs) | n78 = fr. 3623 no. 78 (1591, R9460) | not solved (too short) |

**Where it is merged:** Four systems from different writers and years (1590 news-letters vs Lauriere's 1593 letters in three other volumes) in one target under catalogue item 30 / recipient Nevers. outcome.parts = null; one outcome.method 'key recovered based on adjacent plaintext' (true only for nos. 24/25/60); one fraction 0.863 ('All counted letters: 383 of 444') pooled across keys; system.summary describes only no. 23 and 24/25/60 (key 57 only in system.notes). Page h1 'Champagne news letters ... 1590-91' though half the reading is Lauriere 1593 with key 57. README (README.md:196) one 'partial' row. Page sections are per letter, so a reader can follow, but the record cannot.

**Risk:** setsunaatto's key-57 reading is filed under an 'adjacent plaintext' method; 86.3% merges a known-key reading (~95%) with a partly rebuilt key (61%); key 57's documents and statistics hidden; no. 10 used as a test but not listed.

**Proposed fix:** Add outcome.parts per key (name code no. 23; alphabetical 2-digit table nos. 24/25/60; key no. 57 nos. 55, 10, f. 58; no. 78 unread). Better: split Lauriere/La Verriere 1593 (key no. 57) into its own target and retitle; one README row per key.

**Evidence:** targets/champagne1590/profile.json system.summary 'No. 23: a small name code ...; nos. 24/25/60: a two-digit homophonic alphabet'; system.notes 'No. 55 ... is Nevers key no. 57'; NOTES.md:340-341 'key no. 57 ... give no sense ... they use a different, alphabetical two-digit system'; outcome.parts null; docs/champagne1590.html h1 '1590-91'

### geertruidenberg

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Torcy's two-part code of 800+ values with homophones (values to 823) | torcy, BL Add MS 61575 ff. 38-41 (R8755), 3 Apr 1710 | not solved |
| Villars' smaller code (values to 560) | villars, BL Add MS 61575 f. 44 (R8756), 1 Jun 1710 | not solved |

**Where it is merged:** Grouped by volume/recipient (Geertruidenberg conference, Add MS 61575). profile system.summary 'Two different numerical codes'; one outcome.method 'not solved', no outcome.parts; one page and one README row (README.md:377) 'no key fits either code'.

**Risk:** Low because both are unread and the README says 'a different code'. Risk: system statistics (types, symbol counts) and any future reading of one code would be credited to the pair; paper counts one target where there are two ciphertext-only problems of different size.

**Proposed fix:** Add outcome.parts per code (Torcy R8755 / Villars R8756, both not solved) and per-code length fields; split into two folders if either is ever read.

**Evidence:** profile system.summary 'Two different numerical codes. Torcy ... Villars: a smaller code'; outcome.parts null; README.md:377 'Villars: 173 groups ... a different code'

### ilten1697

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| code A: numeric syllabic nomenclator, groups to ~505, null 62 (1697) | A, Hattorf -> Ilten, 7 Nov 1697 (Ms XXIII 1245:4 ff. 212-213) | read from existing decipherment (interlinear), read |
| code B: numeric syllabic nomenclator, groups to 1010, null 91 (1705-06) | B (Heusch, Berlin, 10 Oct 1705), C (Hattorf, 31 Jan 1706), D (Elector Georg Ludwig, 25 May 1706) | read from existing decipherment (interlinear), read; 7 unglossed tokens open |

**Where it is merged:** Mild. Grouped by recipient (Ilten) and catalogue 346. profile system.summary names both codes, but one system.types list, one outcome.method, a pooled fraction_read 0.986, no outcome.parts. Page has one 'The codes' section (ilten1697.html:73) and reads per letter.

**Risk:** Low: both codes have the same outcome (interlinear decipherments). Paper statistics (code size, nulls, fraction) blend a ~505-group and a ~1010-group code from different correspondents.

**Proposed fix:** Add outcome.parts per code (A: letter A; B: letters B, C, D) with measured fractions; optionally per-code system notes.

**Evidence:** profile system.summary 'Two numeric syllabic nomenclators: code A ... and code B ...'; NOTES.md:62,65 'Code B is one code for all three later letters'; outcome.parts null

### kaa4591

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| System A' (R9407 Augurelio key carried over, gloss of R9427) | R9408, R9409, R9410 (f.244r and Latin ff.246-247), R9413, R9427 | key from adjacent plaintext (glosses), read in part 77-90% |
| System B (Laski) | R9322, R9323, R9417 | key from adjacent plaintext (glosses), read (R9323 3/13 lines) |
| key R9324 (letter substitution + nomenclator) | R9325 (Fulda 1576) | read with known key (key filed in the volume), read |
| key R9423 block 2_4 'H. Wilh.' | R9367 (1535) | read with known key + context, read in part |
| R9416 pp.1-2 system (glossed) | R9416 f.262 | read at the time / existing decipherment |
| R9416 pp.3-4 homophonic | R9416 f.263 | key recovered ciphertext-only, read in part (separate README row 102) |
| Latin-letter substitution | R9424 | not solved |
| dot grille | R9319 (1583) | not solved, blocked (cover letters not imaged) |
| none (key fragment) | R9291 | not applicable |

**Where it is merged:** Catalogue entry 161 grouped by volume (the Bavarian key volume). system.summary says 'Not one system: at least six' and types ['unknown']; outcome.parts has only 2 parts and part 1 lumps System A', System B and R9325 (a filed key R9324, i.e. read with known key, not key-from-adjacent-plaintext) under one method; R9367 (key R9423), R9416 f.262 (read at the time), R9424, R9319 have no parts; fraction_read 0.893 has no source and mixes systems; README row 200 is one row for 'fourteen ciphertexts' (R9416 f.263 already split to row 102).

**Risk:** R9325 and R9367 are counted as key recovered from adjacent plaintext when they were read with filed keys; the unread R9424/R9319 vanish inside an 89% figure; per-system difficulty statistics impossible.

**Proposed fix:** Split per system: kaa4591-systemA (R9408-R9413, R9427, with R9368/R9407 siblings), kaa4591-laski (System B: R9322/23/17), kaa4591-r9325 (key R9324), kaa4591-r9367 (key R9423), keep R9416 f.263 separate, list R9424/R9319 as attempted/open entries. At minimum one outcome.parts per system with its own method and measured fraction.

**Evidence:** profile system.summary 'Not one system: at least six'; outcome.parts[0] label 'the glossed systems (A', B) and R9325'; NOTES.md:13-15 'separate letters in at least six systems'; NOTES.md:22 R9325 key 'R9324 (f.124-127)'; NOTES.md:280-286 R9367 key R9423; README.md:200

### maisse1592

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Maisse's Cipher (1592), homophonic figure cipher (Tomokiyo henryiv_Maisse1.png) | BnF fr. 16093 ff. 370, 373 | f. 370 read with known key and checked letter for letter against the Brienne 13 clear copy; f. 373 read from the clear copy only |
| Maisse's Cipher (1592-1593), mixed letter-symbol + figure nomenclator, the Breves cipher (henryiv_Maisse2.png) | ff. 404/406, 410 (412 duplicate) | read from existing decipherment (Brienne 13 clear copies); not deciphered with the key |

**Where it is merged:** Grouped by recipient (Henri IV -> Maisse). system.summary and the page ('Four leaves, two ciphers') state the two systems, but there are no outcome.parts; one outcome.method 'read from existing decipherment' and fraction_read 1.0 for both, although only f. 370 (81 characters) was deciphered with a key (NOTES.md:8-11 flags this).

**Risk:** Low-medium: the two ciphers get one outcome; the 1.0 fraction implies the Breves cipher was verified on the leaves when it was not; the Breves cipher sits in a 'Maisse' entry where a search by key (Breves 1593-1602) would miss it.

**Proposed fix:** Add outcome.parts per cipher (ff. 370/373: read with known key for f. 370, existing decipherment for f. 373; ff. 406/410: read from existing decipherment), and set fraction per cipher; or split ff. 406/410 into a Breves-cipher entry.

**Evidence:** profile system.summary 'Two ciphers, not one'; NOTES.md:8-11 'the key was checked letter for letter on f. 370 only'; NOTES.md:157-176; docs/maisse1592.html:61; README.md:338

### michell1751

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Frederick II's cabinet code of 1751 to Michell (groups 2-6472) | R1957 (KHA inv. 198) | read from existing decipherment (PC 8 no. 5263 matched), complete; key recovered from external plaintext by WAINUT, partial 69.5% |
| Michell's envoy code (groups 2-5346, half-groups), key material R1050/R1051 | R1955 (ministerial rescript, same day) | read after matching with key from external sources (WAINUT), partial 26.4%, fragments |

**Where it is merged:** Two different Prussian codes grouped by date/route/volume (KHA inv. 198, 28 Dec 1751). outcome.parts does separate them (three parts, R1955 its own), and system.summary says 'Two different Prussian numerical codes'. But top-level outcome.method 'read from existing decipherment', class 'already solved' and the README row (README.md:357) status 'complete', 'Solved earlier by Printed in Politische Correspondenz' sit over R1955, which is not in print and is 26.4% read; outcome.notes still says 'R1955 is attempted, open'. Page title names only the R1957 letter; no h2 for R1955.

**Risk:** README/site badge says R1955 was already solved in print when it was not; scoreboards count it 'complete'.

**Proposed fix:** Either move R1955 to its own target (michell1751-rescript, partial, WAINUT credit) or set README row to 'partial' and name both codes; add a page section for R1955; reconcile outcome.notes ('attempted, open') with parts[2] (read in part).

**Evidence:** targets/michell1751/profile.json system.summary 'Two different Prussian numerical codes'; outcome.parts[2] 'R1955 in Michell's envoy code ... 26.4%'; outcome.notes 'R1955 is attempted, open'; README.md:357 'complete | Solved earlier by Printed in Politische Correspondenz'

### nevers1593

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Nevers cipher no. 46 (two-digit alphabet with homophones, barred/plain/dotted word lists; fr. 3995 f. 87) | f209 (fr. 3985 f. 209, 8 Sep 1593), f168 (fr. 3986 f. 168, 14 Oct 1593), to Pisany | read with known key: f209 read, f168 read in part |
| Court symbol cipher no. 60 (symbol alphabet ~5 homophones/letter + syllabary; ff. 108-111) | f88 (fr. 3985 f. 88, 21 Aug), f146v, f157v (to Revol); also ff. 176, 198 named but not in documents[] | f88 read in part (tunarob, issue #32); f146v, f157v not read |

**Where it is merged:** Grouped by sender and catalogue item 21. profile system.notes: 'Two keys in one catalogue item; system fields describe no. 46' (system.types, homophones, nomenclator are no. 46 only). One outcome.method 'read with known key', fraction_read 0.3 estimated 'by letters (2 of 7 read ...)', outcome.parts null. The page separates the keys (nevers1593.html:45 'two letters in the numerical key no. 46, five in the symbol cipher no. 60', section 05 'The letters to Revol and key no. 60'), but the README row (README.md:300) is titled 'Nevers -> Pisany' only and still says of the Revol letters 'none read yet', though f88 is now read in part.

**Risk:** No. 60 letters inherit no. 46's system description and the 'read with known key' method in the paper data; the 30% blends a near-complete no. 46 reading with a barely started no. 60; credits (tunarob key corrections to no. 60, Tomokiyo partial readings of no. 46 letters) are not tied to their key.

**Proposed fix:** Split into nevers1593 (no. 46, Pisany: f209, f168) and nevers1593revol (no. 60: ff. 88, 146v, 157v, 176, 198) with their own system blocks and credits; or at least add outcome.parts per key with measured fractions, and update the README row title and the f88 status.

**Evidence:** profile system.notes 'Two keys in one catalogue item; system fields describe no. 46'; outcome.notes 'fraction_read 0.3 is an estimate by letters'; outcome.parts null; docs/nevers1593.html:45,125; README.md:300 'none read yet'; credits tunarob 'partial reading of f. 88r'

### papai1706

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Papai envoy key DECODE R580/R581 (Hungarian syllabic nomenclator 10-322) | R740, R741, R757, R765, R784, R793-R796, R805, R823 (11 letters) | read with known key, 99.7% of groups |
| graphic-sign substitution (~25 signs), no key | R731 (6 Mar 1710, Belgrade) | not solved, not reliably transcribed |

**Where it is merged:** Grouped by sender (Papai). system.summary mentions R731's separate alphabet, but there are no outcome.parts; one outcome.method 'read with known key' and fraction 0.97 adds R731's ~330 signs as unread to the R580 groups. README row 293 merges catalogue 46, 47 and 50 (same key: fine).

**Risk:** Low: R731 is labelled 'read with known key' by method; the class 'read in part' for the R580 letters is caused only by a different-system letter.

**Proposed fix:** Split R731 into its own attempted/open entry or add outcome.parts (R580 letters: read with known key, complete; R731: not solved); compute the R580 fraction alone.

**Evidence:** profile system.summary 'R731 uses a separate graphic-sign alphabet'; fraction_read_source 'R731's ~330 signs added as unread'; NOTES.md:101-108; README.md:293

### potocka1714

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Potocka's partly ordered numerical alphabet with doubled homophones and person codes | R7525-R7530, R7534-R7536 (Barbara Potocka -> Jakub Dunin, 1714-16) | key recovered from ciphertext-only (from the R7526 Polish postscript), 844/886 = 95.3% sense (meets the read bar) |
| Mniszech's separate word-divided homophonic system (77 signs) | R7524 (Jozef Mniszech -> Dunin, 1714; 232 tokens) | not solved |

**Where it is merged:** Grouped by recipient (Dunin) and archive (Archiwum Sanguszkow). outcome.parts = null and outcome.credits = null; one outcome.method 'key recovered from ciphertext-only'; fraction_read 0.771 / 75.5% pools both; NOTES.md:3 'Mniszech R7524 not read, so the target is 75.5%' and outcome.notes 'the target stays read in part because one document (R7524) is unread'. system.summary covers both but counts describe Potocka only.

**Risk:** The Potocka key, which meets the 95% read bar, is reported 'read in part' at 75.5% because an unrelated key's letter is unread; the paper's result for Potocka's cipher is understated and Mniszech's failure is hidden inside a 'ciphertext-only' success.

**Proposed fix:** Split R7524 into its own target (mniszech1714, not solved) and mark potocka1714 read at 95.3%; or add outcome.parts (Potocka key: ciphertext-only, complete; Mniszech: not solved) and compute the class per part.

**Evidence:** targets/potocka1714/NOTES.md:8 'R7524, Jozef Mniszech to Dunin, uses a separate, still unread numerical system'; NOTES.md:3 'so the target is 75.5%'; profile.json outcome.notes 'the target stays read in part because one document (R7524) is unread'; outcome.parts null

### r1871

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Venetian nomenclator, base letter + superscript letter (Bonavoglia 'Cifra n. 3' family), 1558 | R1873, ASVe Busta 30 ff. 4-6, Mocenigo, Rome 25 Apr 1558 | read from existing decipherment (Bonavoglia, saved r1873_bonavoglia.txt) |
| Foscarini's 1680s 3-digit numerical nomenclator (Paris/Madrid) | R1871, ASVe Busta 30 f. 4, Foscarini, Paris 11 Sep 1680 | not read here; Bonavoglia lists it but his decipherment could not be retrieved; attempted ciphertext-only, failed |

**Where it is merged:** NOTES.md:8 'Catalogue 264 ... merges two records that belong to different despatches, 122 years apart', yet one folder/profile keeps both: one outcome.method 'read from existing decipherment' for both, fraction_read 'unknown', outcome.parts null, system.types ['nomenclator'] with a summary describing both ciphers. NOTES.md:5 'Verdict: both already read, by Paolo Bonavoglia' although R1871's decipherment was never seen (NOTES.md R1871 section 'His decipherment could not be retrieved'). Folder named after R1871, the unread one. No page/README row (Status: no write-up).

**Risk:** Paper data counts R1871 as 'read from existing decipherment' though no decipherment was obtained and the attempt here failed; the 1558 and 1680 ciphers' statistics are pooled; the contamination question (reading existed and was seen) is answered 'yes' for a document whose reading was not seen.

**Proposed fix:** Split into r1873 (Mocenigo 1558, read from existing decipherment, Bonavoglia) and r1871 (Foscarini 1680, not solved / decipherment exists but unretrieved, ciphertext-only attempt failed); or add outcome.parts per record with distinct methods. Change the NOTES verdict to 'R1873 read by Bonavoglia; R1871 listed by him, decipherment unseen'.

**Evidence:** NOTES.md:5 'both already read'; NOTES.md:8 'merges two records ... 122 years apart'; NOTES.md 'His decipherment could not be retrieved'; 'Attempt here (22 Sep 2026): not read'; profile outcome.method 'read from existing decipherment', outcome.notes 'R1871 attempted, not read'; outcome.parts null

### rakoczi1704

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Bonac-Groffey French nomenclator, DECODE R639 | R912, R922 (1707) | read after matching with external key (R639), ~97%; about a third read at the time interlinear |
| a different issue of the R639 table | R852 (Dantzig 22 Jan 1706) | read from its own clear copy (existing decipherment) |
| Rakoczi's Latin syllabic key (rebuilt from the interlinear by align483.py) | R483 (Lwow 27 June 1711) | key recovered from adjacent plaintext (interlinear decipherment) |

**Where it is merged:** Grouped by catalogue 44 / DECODE author 'Rakoczi'. system.summary describes only the one-part French nomenclator 10-560; one outcome.method 'read after matching with key from external sources' for all four; no outcome.parts (NOTES.md:100: 'A parts split ... is for the main session to decide'); README row 223 says 'Read' for the whole set. Page sections are per letter, good.

**Risk:** R483 (Latin, own key rebuilt from interlinear) and R852 (clear copy) are counted as external-key matches; R483's key is described as the French R639 table.

**Proposed fix:** Split R483 into its own target (Rakoczi 1711 Latin syllabary, key from adjacent plaintext); keep R852/R912/R922 together but add outcome.parts (R912/R922 external key R639; R852 existing decipherment / different issue).

**Evidence:** profile system.summary 'One-part numerical French nomenclator, values 10-560'; NOTES.md:7-8 'its syllabic key has been rebuilt from that decipherment'; NOTES.md:50 'R852 uses a different issue of the table'; NOTES.md:100; README.md:223

### sessa1593

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Spanish office cipher 1592-93 (office key BnF fr. 3995 f. 97, DECODE R4076-R4077; Tomokiyo phelippes2.png) | no45 = fr. 3983 no. 45 (Miranda->Feria, 25 Feb 1593); no79 = fr. 3983 no. 79 (Sessa->Ibarra, 11 Mar 1593); no47 = fr. 3984 no. 47 (Sessa->Philip II, 30 Jun 1593) | read with known key, partial ~92.5%; checked against no. 47 interlinear |
| Feria-Mansfeld cipher 1593 (Tomokiyo spanish3mansfeld.png; nomenclature missing) | no68 = fr. 3984 no. 68 (Ibarra, Paris, 10 Jul 1593) | read with known key (alphabet/syllables only), partial 37.5%; three-letter word codes open |

**Where it is merged:** Two different ciphers (two different correspondences: the office cipher of Sessa/Miranda, and Feria-Mansfeld's syllabic cipher used by Ibarra in Paris) in one target grouped as catalogue item 19 / year 1593. outcome.parts = null; one outcome.method 'read with known key'; one fraction_read 0.753 pooling 92.5% and 37.5%; system.types merged and system.summary describes the office cipher with no. 68 as an add-on clause; README row (README.md:284) leads with 'The Spanish office's own key survives' for all four. The page does have h2#keys and a per-letter h3 for no. 68.

**Risk:** The 75.3% figure is meaningless for either key; Arya's office-key credit ('read all four letters in part') covers a letter in another cipher; paper per-system stats (distinct_symbols 133, alphabetical key order) mix two systems.

**Proposed fix:** Add outcome.parts: (1) office cipher, nos. 45/79/47, read with known key, partial 92.5%; (2) Feria-Mansfeld cipher, no. 68, read with known key, partial 37.5%. Or split no. 68 into its own target (ibarra1593) and retitle; README one row per cipher.

**Evidence:** targets/sessa1593/NOTES.md:88 'no. 68 is in the other cipher'; NOTES.md:242 'a different cipher - the Feria-Mansfeld key'; NOTES.md:5 '92.5% of nos. 45/79/47, 37.5% of no. 68, 75.3% overall'; profile.json outcome.parts null, fraction_read 0.753

### sieniawski1708

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Schenck letters: 2-digit alphabetical-block letter table + 3-digit person codes | R7486-R7500 (AKM 21 plik 30/1; 'Sidon' in Vienna -> Baron Schenck, 1706) | key recovered from ciphertext-only, partial (93.5% of letter numbers, 63.6% of all tokens; 65/77 codes open) |
| key A (Wallachian chancellery key, Kaczka 2012 fn. 21) | R7468-R7474, R7477-R7480, R7483 (Brancoveanu/Cantacuzino -> Sieniawski 1709-14) | read from existing decipherment (Kaczka 2012 print), sample checked |
| key B (Turculet key, Kaczka fn. 22) | R7481-R7482 | read from existing decipherment (interlinear), 99.6-100% |
| alphabetical homophonic table rebuilt from the gloss | R7475 (adviser, 1707) | read from existing decipherment (interlinear), ~99.6% |
| Chomentowski 3-digit syllabary | R7476, R7484-R7485 (Chomentowski 1713-14) | read from existing decipherment (interlinear); R7476 ~94.4-94.9%, R7484 96.5%, R7485 100% |

**Where it is merged:** Five systems and two unrelated correspondences (a Vienna agent to Schenck 1706 vs Wallachian/Polish writers to Sieniawski 1707-14) in one folder, profile and page, joined only by the DECODE range R7468-R7500 / catalogue 333. README is split into two rows (README.md:103, 368) and outcome.parts has three parts, but part 3 ('unprinted Sieniawski letters') lumps key B, the R7475 table and the syllabary; documents[] are grouped by collection (one document 'nr 13 and nr 5' for 11 records). Top-level system.summary, distinct_symbols=143, outcome.method 'key recovered from ciphertext-only' and fraction_read 0.636 describe only the Schenck letters, yet sit over all 33 records.

**Risk:** The ciphertext-only break and 63.6% figure attach to the whole target including 18 letters read from print/interlinears; system statistics (143 symbols, alphabetical order) applied to four other systems; per-key outcomes for key B/syllabary not recoverable.

**Proposed fix:** Split into two targets: sieniawski1708 (Sieniawski letters) and a new schenck1706 (R7486-R7500). Inside the Sieniawski target give outcome.parts one entry per key (A, B, R7475 table, syllabary) and documents[] per record or per key.

**Evidence:** targets/sieniawski1708/profile.json system.summary 'the Sieniawski letters use four other systems (keys A and B, an alphabetical homophonic table, a 3-digit syllabary)'; outcome.notes 'R7468-R7500 are four collections'; NOTES.md:31 'Sieniawski group, several systems'; README.md:103 'Split entry, part 1 of 2'

### sp106box10

**Verdict:** MIXED  
**Lasry:** none (his SP 106 keys tested on R931, do not fit)

| Key / cipher | Documents | Outcome |
|---|---|---|
| System A: two-figure Italian nomenclator, codebreaker's key R725 | R657 (ff. 128-138) + worksheets | key transcribed; R657 'not read' (not worked against R725) |
| System B: three-figure syllabic code (grid R658) | R660, R664, worksheet R720; also R722 (Venetian secretary 1625) and the R703 'Venetian cifar' dossier with R656, R661, R663, R667, R684, R701, R702 | about 45 values rebuilt from interlinear glosses; R660/R664/R722 read in fragments; R722 code not deciphered |
| System C: letter-and-figure syllabary | R704, R721 (R722 first filed here, now moved to B) | not read |
| English royalist numerical code of Sept 1645 (~260 values) | R931 | not solved; page says it 'does not belong to the case' |

**Where it is merged:** One profile/page/README row for at least four systems grouped by box (SP 106/10). profile system.types merges nomenclator+homophonic+syllabic+code; one outcome.method 'read with known key' and fraction_read 0.1 with outcome.parts null, though the 'known key' R725 is system A and R657 (system A) is 'not read'; the fragments actually read are system B values rebuilt from glosses (key recovered from adjacent plaintext). credits only 'R725, grid R658 and interlinear solutions'. README row (README.md:295) presents 'the seven records are one case ... the cipher explained'. R931 (1645, different code, unrelated) is in documents[].

**Risk:** Method misclassification: system B fragments are scored as 'read with known key' using system A's key; the 10% fraction mixes three systems and an unrelated 1645 letter; DECODE/paper readers may think R725 reads the file. R931's 'not read' inflates the denominator of an unrelated case.

**Proposed fix:** Add outcome.parts per system (A: key R725 known, R657 not read; B: key recovered from adjacent plaintext (glosses), R660/R664/R722 fragments; C: not solved; R931: not solved); better, split into sp106box10a (R657+R725), sp106box10b (R660/R664/R720/R722 + R703 dossier + grid R658) and sp106box10c (R704/R721), and move R931 to its own target or to the 1645 royalist group.

**Evidence:** profile system.summary 'Three ciphers in one codebreaker's file: (A) ... (B) ... (C)'; docs/sp106box10.html:118 'The file holds three ciphers, not one'; html section 08b 'R931 does not belong to the case'; profile R657 read 'not read'; outcome.method 'read with known key', parts null; README.md:295

### thurloe

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| (a) figure substitution + small code (8 code groups) | a-beverning-1653, TSP i.435 | not solved |
| (b) figures mixed with letters | b-dugard-1656, TSP v.78-79 | not solved |
| (c) ten-digit cipher | c-brussels-1656, TSP v.267 | not solved |
| (d) homophonic figures with two codes (226, 243) | d-waddall-1656, TSP v.337 | not solved |

**Where it is merged:** Grouped by printed source (Thurloe State Papers, cryptiana item #9). profile system.summary 'Four unrelated short ciphers'; system.types ['undetermined'] 'for the set'; nomenclator.entries pools (a) and (d); one outcome.method 'not solved', no outcome.parts; README row (README.md:415) 'Four short pieces, all period keys fail'; no page.

**Risk:** Low today (all unread, stated as four systems). Paper counts one target for four separate ciphertext-only problems, and the control run (done on (a)'s layout) is reported for the whole set; system statistics are pooled/undetermined.

**Proposed fix:** Add outcome.parts per piece (a)-(d), each 'not solved' with its own length/system; or split into four profiles if the paper counts per cipher. Keep the README row but say 'four different ciphers'.

**Evidence:** profile system.summary 'Four unrelated short ciphers'; system.notes 'Four separate systems, so types is undetermined for the set ... nomenclator.entries counts the 10 code groups seen in (a) and (d)'; outcome.notes control 'on (a)'; README.md:415

### transylvania1645

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Hungarian substitution 'shared alphabet family' (c=p, p=c, g=u, q=t) | R4936 (1645), R4940 (1648), fragments R4937, R4942 | key recovered from ciphertext-only; R4940 23 letters read, others partial/unverified |
| 'Different substitution' (unsolved) | R4941 (1648) | not solved |
| unknown, not inspected | R4933 (1628/1658), R4934, R4935 (1628, KemÃ©ny_XIX), R4938, R4939 | not transcribed |

**Where it is merged:** Ten DECODE records grouped by a DECODE number range across two collections (KemÃ©ny_XIX_1628 vs Keresdi_Bethlen_14/15) and dates 1628-1658, title '1645'. NOTES.md:33 'R4941 | 1648 | Different substitution'. Profile system.types 'undetermined' with summary 'the other systems remain to be inspected', yet one outcome.method 'key recovered from ciphertext-only', class 'read in part', no outcome.parts. Status: in progress; no README row or page yet.

**Risk:** If written up as is, a single read-in-part entry would credit a ciphertext-only recovery to ten records of which only R4940 (23 letters) is read, and the 1628 KemÃ©ny letters (different writer, decade, likely key) would be counted under the 1645-48 Bethlen key.

**Proposed fix:** Before write-up, classify each record by system; split into keresdi1645 (records sharing the R4936/R4940 alphabet), a separate entry for R4941, and kemeny1628 (R4933-R4935); give each outcome.parts; until then set documents' outcome per record.

**Evidence:** profile system.summary 'R4936 shows alphabetic ciphertext; the other systems remain to be inspected'; outcome.notes 'R4940 cipher expressions read, others unverified or untranscribed'; NOTES.md:24-35

### vanreede1787

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| William V 1782 Grand Chiffre (DECODE R1024) | R1026 (29 Dec 1787), R1027 (4 Mar 1788) | read with known key, 452/472 groups |
| marked three-digit code (no key) | R1893 (24 Mar 1793, Staten-Generaal inv. 6695) | not solved |

**Where it is merged:** Grouped by sender (van Reede). system.summary names both codes, but there are no outcome.parts; one outcome.method 'read with known key' and fraction 0.383 (447/1167) pool the read Grand Chiffre letters with the unread R1893 code; title 'Dispatches of A. W. C. van Reede from Berlin, 1787-1793' implies one series.

**Risk:** R1893 inherits 'read with known key' in method counts; the 38% figure understates the Grand Chiffre result and overstates R1893; anyone attacking R1893 might assume R1024.

**Proposed fix:** Split R1893 into its own target (attempted, open), or add outcome.parts: R1026/R1027 'read with known key'; R1893 'not solved'; fraction per key.

**Evidence:** profile system.summary 'R1893 uses a distinct three-digit marked-number code'; no outcome.parts; fraction_read_source 'all of R1893 unread; 447/1167'; README.md:292

### vich1511

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Ferdinand-Vich nomenclator of 1511-12 (rebuilt from deciphered siblings N.46, N.52BIS) | N.45 (4 Apr 1511), N.57 (5 Jun 1512), N.60 (1 Sep 1512), AHN Estado 8715 | key recovered based on adjacent plaintext, read in part (3-8% of groups unread) |
| unknown 1515 system (different key; N.74 is a third system) | N.73 (26 Oct 1515, Pedrezuela; 3,177 tokens) | not solved |

**Where it is merged:** N.73 is grouped with the 1511-12 letters only by sender/recipient (Ferdinand -> Vich) and bundle (AHN Estado 8715). outcome.parts = null; one outcome.method 'key recovered based on adjacent plaintext' for all four; fraction_read 0.865 pools the read key with 3,177 unread N.73 tokens (outcome.notes even gives 0.74 for the same pool); system.types includes the 1511-12 system only, summary says '(N.73 is a different, unread system)'. Page h1 'Ferdinand the Catholic to Jeronimo de Vich, 1511-12' but includes h2#n73; README row (README.md:193) title lists N.73 under '1511-12'.

**Risk:** The 1511-12 key is held below the read bar purely by an unrelated 1515 cipher (NOTES.md:165 'N.73 ... alone caps the target at ~0.90'); N.73 is counted as attacked-with-adjacent-plaintext instead of 'not solved'; inconsistent fractions (0.865 vs 0.74).

**Proposed fix:** Move N.73 to its own target (vich1515, status attempted/open) or add outcome.parts: (1) 1511-12 nomenclator, N.45/N.57/N.60, adjacent plaintext, partial; (2) N.73, not solved. Measure fraction_read over N.45/N.57/N.60 only.

**Evidence:** targets/vich1511/NOTES.md:16 'different key, not read'; NOTES.md:165 'N.73 (3,177 tokens, other key) alone caps the target at ~0.90'; NOTES.md:191 'different system, no deciphered sibling'; profile.json outcome.parts null

### windischgraetz1720

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Chancellery two-part nomenclator R5017 (1-977) | No. 1, 3 Feb 1720 (R5019 autograph, R5020 copy) | read with known key, read |
| Emperor's private key R5018 (numbers 10-38 + graphic signs, codes 39-210) | Nos. 2, 3, 6 (R5021/R5022, R5023, R5024), 1720-22 | read with known key, read |

**Where it is merged:** Mild. The page separates the keys (windischgraetz1720.html:73 'The letters and the two keys', :97 No. 1, :137 'Nos. 2, 3 and 6 in the private key') and system.summary names both, but profile.json has no outcome.parts, a single fraction_read 0.995 and single system.types/homophone counts ('Homophone counts are for R5018'); grouping is by sender/recipient. README row (README.md:271) names both keys.

**Risk:** Low: both keys survive and both readings are by known key, so the method is right for both. Risk is only statistical: per-key fraction, key size and homophone counts are blended or describe R5018 only, so the paper cannot tell how R5017 (one letter) vs R5018 (three) performed.

**Proposed fix:** Add outcome.parts: one part 'No. 1, key R5017' (records R5019/R5020) and one 'Nos. 2, 3, 6, key R5018' (R5021-R5024), each with its own measured fraction; optionally separate system notes per key.

**Evidence:** profile system.summary 'Two keys: No. 1 in ... R5017 ..., Nos. 2, 3, 6 in the private key R5018'; system.notes 'Homophone counts are for R5018'; outcome.parts null; docs/windischgraetz1720.html:73,97,137

### wod1568

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Throckmorton Cipher 1 (Tomokiyo key image, 7 values corrected) | R2988 f. 32: Throckmorton to Elizabeth 10 July 1559 | read with known key, ~85-90% |
| word-sign margin code (222 groups), undetermined | R2988 f. 32 margin | not solved |
| Moray-Wood 1568 cipher family, undetermined | R2989 f. 33: John Wood to Cecil 6 Sept 1568 | not solved (Bain crib did not align) |

**Where it is merged:** Three systems from 1559 and 1568 grouped by leaves (BL Add MS 4136 ff. 32-33, catalogue 97). Profile system.types 'undetermined' and system.summary describe only the two unread systems, while outcome.method 'read with known key' and class 'read in part' come from the Throckmorton Cipher 1 letter, which is not a separate document in documents[] (only R2989 and R2988). No outcome.parts. fraction_read 0.3 'is over all three texts'. README row (README.md:280) and page title combine all three (page h2s do separate them).

**Risk:** The paper data pairs a 'read with known key' outcome with an 'undetermined' system; readers/statistics may take the Wood 1568 line or margin code as partly read. The read text (1559) is a different letter, date and sender than the catalogue's 'John Wood 1568' item.

**Proposed fix:** Split documents[] into three (1559 letter, margin code, Wood line) with outcome.parts (read with known key / not solved / not solved) and per-system descriptions; or split into wod1568 (Wood line + margin, unread) and throck1559 (read with Cipher 1). Retitle README/page so the catalogue item's own ciphers are shown as unread.

**Evidence:** profile system.summary 'R2989: same symbol families as the Moray-Wood 1568 cipher ... R2988 margin: a shorthand-like sign system'; outcome.basis 'The text reported as read is Throckmorton's own 10 July 1559 letter'; outcome.notes 'fraction is over all three texts'

## Unclear from the files (4)

### dubellay  (Lasry entry)

**Verdict:** UNCLEAR  
**Lasry:** prior solution (re-solved the 1528 cipher in 2022, GL.htm) - credited on a profile whose documents are all 1529

| Key / cipher | Documents | Outcome |
|---|---|---|
| Bayonne's cipher (1529), Tomokiyo table from Clair. 333, extended | 16jun1529 (fr. 3078 no. 3, R3688), 22jun1529 (fr. 3078 no. 4), 17oct1529 (R3691), 30jun1529 (fr. 3040 f. 68, R4229), 22oct1529 (fr. 3005 f. 165) | read from existing decipherment (Le Grand 1688, Scheurer 1969, interlinear); 16 June block 98.5% |
| du Bellay's 'first' cipher of 1528 (key recovered by Bourrilly & de Vaissiere 1905; re-solved by Lasry 2022 as 'Bayonne's Cipher (1528-1529)') | fr. 3077 no. 23 (28 Oct 1528, = Clair. 328 f. 291, DECODE R2287); 21 Oct 1528 stretch; named in README row and profile title but not in profile documents[] | read from existing decipherment (Bourrilly 1905 prints in clear); nothing done here |

**Where it is merged:** Profile title and README row (README.md:364) say '1528-29 ... fr. 3077 nos. 18, 23', and outcome.credits include Bourrilly ('28 Oct 1528 cipher') and Lasry ('re-solved the 1528 cipher in 2022'), but documents[] and system.summary cover only Bayonne's cipher of 1529. NOTES calls the 1528 cipher du Bellay's 'first' cipher (NOTES.md:43) yet Lasry's table title spans 1528-1529 (NOTES.md:46), so whether 1528 and 1529 are one key with revisions or two keys is not settled in the files. Page h1 says only 'London 1529'.

**Risk:** Lasry is credited as prior solver on a profile whose listed ciphertexts he did not (per the files) work on; the paper's prior-solution/contamination field for the 1529 letters is wrong if the 1528 key is different; README credits Bourrilly's 1528 key recovery to a 1529-cipher entry.

**Proposed fix:** Compare Bourrilly's 1528 key / Lasry's GL.htm table with Tomokiyo's 1529 table. If two keys: either add the 28 Oct 1528 letter as a document with its own outcome.parts entry (1528 key, read from existing decipherment, Bourrilly 1905; Lasry 2022 prior solution) or drop it and move the Bourrilly/Lasry credits off; retitle the README row to the 1529 cipher. If one key: say so in system.summary and list R2287 as a document.

**Evidence:** targets/dubellay/NOTES.md:41-46 'recovered the lost key of du Bellay's first cipher'; NOTES.md:55 'Bayonne's Cipher (1529)'; profile.json credits lasry 'prior solution ... re-solved the 1528 cipher'; README.md:364 'fr. 3077 nos. 18, 23 ... 1528-29'; docs/dubellay.html h1 'London 1529'

### charlesi

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| unknown numeric nomenclator A | 1648-05-22 (Charles I -> Edward Worsley, 112 groups, Albin 1795 p. 237) | not solved |
| unknown numeric nomenclator B (postscript says 'This Cypher which now I write in, is that which was sent you by the noble frend') | 1648-08-01 (Charles I -> Prince Charles, 88 groups; DECODE R8342, Harley 6988 f. 208) | not solved |

**Where it is merged:** Two letters to two different recipients grouped by sender/date (Isle of Wight 1648). The files exclude the published keys for both, but never state whether the two letters share one key; the 1 Aug postscript says it uses a cipher sent by the bearer, which suggests a key different from the Worsley one. system.summary describes only the 22 May letter ('uses 1-97 and 204-416 only'). One outcome 'not solved' for both, so no false credit.

**Risk:** Low (both unread). If the two are different keys, pooled statistics (band gaps, near-repeat test) and any future break would be misattributed; DECODE R8342 is in this target and possibly also in an untracked charles1648 folder in the local checkout.

**Proposed fix:** State in NOTES/profile whether the two letters share a key (compare number ranges/band structure); if different, give each its own system notes or outcome.parts, and retitle README row to name both recipients.

**Evidence:** targets/charlesi/NOTES.md:71-73 postscript 'This Cypher which now I write in ...'; NOTES.md:15 'both letters remain unread'; profile.json system.summary 'the 22 May cipher ...'; README.md:408

### sp95box136

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| unknown; candidates Swedish/French keys R7721, R7723, R7724/R7725 (Scheffer, Wynantz 1749-53) or Spanish R7801 (Grimaldi-Canis at Stockholm 1752) | SP95-136 (TNA SP 95/136, 1748-55, contents unseen) | not applicable (blocked on images) |
| unknown; candidate Spanish R7801 ('& Marq. del Puerto at the Hague') or R7793-R7795 | SP87-24-33 (del Puerto, 19 Mar 1748) | not applicable (blocked on images) |

**Where it is merged:** Two unrelated TNA items (Swedish supplementary volume and a Spanish ambassador's intercept in Cumberland's papers) grouped by the TNA label 'not deciphered'. Ciphertexts not seen, so whether they share a key is unknown; system.types ['undetermined'], one outcome 'not applicable', no outcome.parts. No page or README row (Status: blocked).

**Risk:** If images arrive, a reading in one key (e.g. R7801 for del Puerto) could be credited to the whole two-item target; Swedish and Spanish key statistics would be mixed.

**Proposed fix:** When images are obtained, split per key found (likely sp95box136 for the Swedish volume, sp87del-puerto1748 for SP 87/24/33), or add outcome.parts per item from the start.

**Evidence:** NOTES.md title and 'What the target is' (two TNA items); profile system.summary 'Not seen'; system.sibling lists Spanish R7801/R7793 and Swedish R7721/R7723/R7724; outcome.notes 'key none because no key is yet tied to these letters'

### throckmorton

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| Throckmorton's 'third cipher' (DECODE R9262, Add MS 4136 ff.180-185) | verified only on R9220 (27 tokens) and R9230 (15 tokens) | read from existing decipherment (Forbes 1740-41), two samples checked against the key |
| Throckmorton's first and second ciphers (DECODE R9260) | not assigned; any of the other 18 records (1560-63) may use them | not tested |
| other writers' keys (e.g. Thomas Smith on f.169) | R9255 (composite: Smith on f.169 + Throckmorton to the Queen) | not verified |

**Where it is merged:** Twenty records grouped by volume (BL Add MS 4136 = Forbes Papers V) and sender. NOTES itself says three Throckmorton ciphers survive (R9262 'third cipher', R9260 'contains the first and second', NOTES.md:52-53) and that R9255 is composite with other writers (NOTES.md:17, 104), but profile system.summary describes only the third cipher ('The sampled Throckmorton passages use the archived third cipher'), parts = null, one method 'read from existing decipherment' and class 'already solved' for all 20. README.md:354 status 'complete', 'Archived key and prior printed plaintext verified', while NOTES.md:3 says 'Status: in progress'.

**Risk:** README and profile imply all twenty records are in one verified key; which of the three Throckmorton ciphers each record uses is not established, and R9255's non-Throckmorton material is counted as solved by Forbes; DECODE corrections could assign R9262 as key to records in cipher 1 or 2.

**Proposed fix:** Assign each record to a key (first/second from R9260, third R9262, Smith key) by date and sign shapes; add outcome.parts per key with the records covered and 'verified' vs 'matched to print only'; split R9255's Smith part out; set README status to match NOTES (in progress).

**Evidence:** targets/throckmorton/NOTES.md:52-53 'R9262 is headed Sir Nicholas Throckmorton's third cipher. R9260 contains the first and second'; NOTES.md:17 'R9255 is composite'; profile.json system.summary 'The sampled ... passages use the archived third cipher'; README.md:354 'complete'

## Several keys, already presented per key (leftovers noted) (6)

### superscript  (Lasry entry)

**Verdict:** SPLIT-OK  
**Lasry:** solution (Gilino R8572 edition, ciphertext-only per his notes)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Ghinucci/Worcester syllabic superscript-digit cipher (sibling key of R8476/R8589/R8590) | R8613 (target); R8476, R8589, R8590 key material | key recovered based on plaintext from external sources, 97.9% |
| Milanese Sforza key DECODE R5258 (Gilino) | R8572 | read after matching with key from external sources, 96.1%; Lasry independent reconstruction contributed 14 Oct |

**Where it is merged:** Two unrelated ciphers grouped only because both are in Cotton Vespasian C IV/1527. Mitigated: outcome.parts per key, README split into two rows ('Split entry, part 1 of 2'/'2 of 2', README.md:124, :232), page h2 per record. Residual: one folder/profile/page ('Ghinucci to Wolsey and Gilino to Sforza, 1527 â€” Read'); system.types/summary describe only the Worcester cipher, Gilino only in system.notes; single outcome.method (Worcester's) and single fraction_read 0.965 averaging both; Lasry's credit (role 'solution') sits at entry level, not on the R8572 part; page h2 'Key' (unnumbered, after section 04) shows Lasry's Gilino key without a caption tying it to R8572 only.

**Risk:** Entry-level Lasry 'solution' credit and the badge read as if he solved Ghinucci R8613; paper statistics (one method, one fraction, system.types) treat Gilino as a Worcester-type syllabic cipher. Lasry's Gilino method (crib/pattern, no external key) is not recorded as a part, so his ciphertext-only result vs project's external-key match is conflated.

**Proposed fix:** Split into targets/superscript (Ghinucci R8613) and a new targets/gilino1527 (R8572) with its own profile/page; or at minimum put Lasry's credit on the R8572 part, add his method as a separate part/credit, give Gilino its own system block, and caption the page 'Key' section 'Gilino (R8572) key, George Lasry'.

**Evidence:** profile system.notes: 'Gilino R8572 is a different (Milanese) system'; outcome.parts two entries; credits lasry role 'solution' note 'Contributed Gilino R8572 edition'; NOTES.md:207-209; docs/superscript.html h2 list

### ferdinand3

**Verdict:** SPLIT-OK

| Key / cipher | Documents | Outcome |
|---|---|---|
| 1635 alphabet (from draft R954) | R1889 | key recovered based on adjacent plaintext, complete 97.2% |
| 1640: R1889 alphabet + AEIOU syllabary | R1890 | key recovered from ciphertext-only (syllabary), complete |
| 1634 different vowel-series repertoire | R1887 | key recovered based on adjacent plaintext (in-letter crib), partial 88.4% |

**Where it is merged:** Grouped by correspondents (the two Ferdinands) and shelfmark (AGR SEA 540). Mitigated: outcome.parts per letter, README split into three rows ('Split entry, part 1/2/3 of 3', README.md:104, :203, :204), page h2 per record. Residual: one profile-level outcome.method ('key recovered based on adjacent plaintext', which is wrong for R1890) and one fraction_read 0.959 averaging the complete and the partial letters; system.types merges both repertoires.

**Risk:** Low. Top-level method/fraction could be used by the paper analysis instead of parts, misclassifying R1890 and hiding R1887's partial status.

**Proposed fix:** Keep as is; ensure the analysis uses outcome.parts; optionally move R1887 (different key) to its own folder ferdinand1634.

**Evidence:** profile sys.sibling_key 'R1887 shares only the vowel-series principle'; system.summary '1634: a different repertoire'; outcome.parts x3

### malsburg1637

**Verdict:** SPLIT-OK

| Key / cipher | Documents | Outcome |
|---|---|---|
| Malsburg numerical homophonic table + nomenclator | HCPortal 496-509 (ff. 3-33), incl. the French letter signed 232 and news extracts, 'same key' | key recovered from ciphertext-only (Bourdeau), complete 95.9% |
| period-five alphabetic shift cipher (4,5,3,6,2 over 24 letters) | ten-line block at the foot of image 0012 (HCPortal 497) | key recovered from ciphertext-only (Beck with ChatGPT, PR #17), partial |

**Where it is merged:** Properly separated: outcome.parts one per system, outcome.notes 'Overall fraction and code totals are unknown because the distinct systems are not combined', page has h2#letter-block, README row names the separate block and its contributor. Residual: top-level fraction_read 0.959 is the numerical part only while class 'read in part' reflects the block; one physical document (497) carries both systems, which is stated.

**Risk:** low; top-level fraction could be read as covering the alphabetic block.

**Proposed fix:** none essential; label top-level fraction as numerical-system only.

**Evidence:** targets/malsburg1637/profile.json outcome.parts (two systems); outcome.notes 'the distinct systems are not combined'; docs/malsburg1637.html h2#letter-block

### rupert

**Verdict:** SPLIT-OK

| Key / cipher | Documents | Outcome |
|---|---|---|
| f. 106 lower alphabet (graphic-sign substitution, key R8727) | BL Add MS 72438 f. 107r (R8728) | read with known key, complete (95.3%) |
| Maurice's 'your cipher' (unknown numeric nomenclator) | Maurice to Rupert 7 Jul 1645 (Warburton iii.133) | not solved |
| f. 9 key (no group above 343) and a different f. 10 key (groups to 697) | R8623 (f. 9), R8624 (f. 10) | not solved |
| unknown numeric keys | R8725 (f. 104), R8433 (Trevor, Add MS 18982 ff. 51-52) | not solved |

**Where it is merged:** Mostly split: outcome.parts gives one part per group, the page has separate sections (rupert.html:91-104) and README has a separate row for f. 107 (README.md:245) and one for the unread letters (README.md:376). Residual merges: the top-level outcome.method 'read with known key' and fraction_read 0.0864 pool f. 107 with five unread ciphers; the part 'Cryptiana #6, Add MS 72438 f. 9 ... and f. 10' joins two documents whose keys differ (system.notes 'f. 9 and f. 10 use different keys'); the part for f. 104 + Trevor joins two unrelated letters; system.types merges nomenclator and the f. 107 monoalphabetic; f. 107 is grouped only because it sits in the same volume.

**Risk:** Paper statistics: the target counts as 'read with known key' though the read piece (f. 107) is an unrelated letter found in the same volume and the cryptiana targets are all unread; the 8.6% blends keys. Low risk of crediting a reading to the wrong document since parts and page are explicit.

**Proposed fix:** Move f. 107 (R8727/R8728) into its own folder/profile (e.g. addms72438f107) with method read with known key; leave rupert as 'not solved'; split the f. 9 / f. 10 part into two parts and f. 104 / Trevor into two parts.

**Evidence:** profile system.notes 'f. 9 and f. 10 use different keys (f. 9 has no group above 343, f. 10 runs to 697)'; outcome.parts labels; outcome.method 'read with known key', fraction_read 0.0864; docs/rupert.html:6 title 'still unread; f. 107 deciphered'; README.md:245 and :376

### sanchez1522

**Verdict:** SPLIT-OK

| Key / cipher | Documents | Outcome |
|---|---|---|
| Alonso Sanchez's 1522 Venice cipher (Tomokiyo reconstruction, extended) | R9653, R9635 (profile documents); other Sanchez records of R9593-R9657 open | read with known key, partial (0.6 of code groups on the two leaves) |
| Lope Hurtado de Mendoza's 1522 Rome cipher (third member of the family) | R9634, R9644-R9646, R9648-R9650, R9652, R9656 - now its own target lopehurtado (README.md:185) | handled in target lopehurtado |

**Where it is merged:** Profile documents and system cover only Sanchez's key and NOTES says the Hurtado letters 'deserve their own target' (they now have one). Residual: README.md:314 row title still reads 'Alonso Sanchez (Venice) -> Charles V, and Lope Hurtado de Mendoza, 1522 ... DECODE R9593-R9657, 29 records', so the nine Hurtado records appear under both rows; page keeps an h2#hurtado section. Juan Manuel's Rome cipher is a sibling, not included.

**Risk:** Double-counting the Hurtado records; a reader of the README row thinks Sanchez's key covers Hurtado's letters.

**Proposed fix:** Retitle the README row to Sanchez only and state the record range excluding R9634/R9644-R9656; link the page's hurtado section to the lopehurtado target.

**Evidence:** targets/sanchez1522/NOTES.md:303 'The Lope Hurtado de Mendoza letters are not in Sanchez's cipher'; NOTES.md:313 'third member of the same family'; README.md:314 title 'and Lope Hurtado de Mendoza'; README.md:185 separate Lope Hurtado row

### soria1523

**Verdict:** SPLIT-OK

| Key / cipher | Documents | Outcome |
|---|---|---|
| key A (June-July 1523) | R9488-R9490, R9492-R9493 (body) | key recovered from ciphertext-only, complete (June 99.5%, July body 98.0%) |
| key B (from late July 1523; also in R9844) | R9491, R9492-R9493 (post data), R9494-R9498 | key recovered based on plaintext from external sources (R9844 + court decipherment), partial (94.0%) |

**Where it is merged:** Properly split: outcome.parts per key, README has two rows 'Split entry, part 1 of 2' / 'part 2 of 2' (README.md:101, 123), page has h2#keys and per-letter sections. Residual: top-level outcome.method 'key recovered from ciphertext-only', fraction_read 0.966 and class 'read' are pooled over both keys, though key B alone is 94.0% (below the read bar) and came from external plaintext. One letter (R9492-R9493) uses key A body + key B post data, correctly stated.

**Risk:** Analysis reading only top-level outcome.method/fraction would credit key B with a ciphertext-only break and 'read'.

**Proposed fix:** Keep the split; ensure the paper analysis uses outcome.parts; note top-level fraction is pooled.

**Evidence:** targets/soria1523/profile.json outcome.parts (two keys); README.md:101 'Split entry, part 1 of 2'; README.md:123 'part 2 of 2'; parts[1].basis '94.0% over the key-B letters'

## One key throughout (43)

Checked and found to use a single key (or one key with minor revisions): alessandrino1568, egmond, labbe1582, mellon136, nuncio1566, nunzio1718, nunzio1736, pallotto1629, r1892, rupert1645, siena1431, vatican5, battier1686, buda1489, catinat1691, cobham1588, eichel1758, estrada1503, fagel1804, ferdinand1619, harley287, hesse1603, jantini1517, joyeuse, lanssac, lebel1593, lee1526, lopehurtado, lorraine1592, maria1435, ormonde, ottobon, r4157, raince, rennes1563, sanchez1523, smith1562, sperantio1534, stowe166, toulon1803, warsaw, wesselenyi1664, windischgraetz1721.

