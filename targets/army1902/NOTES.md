# Japanese Army numeric kana cipher, 1902–04 (JACAR, NIDS holdings)

Contributed by Harumi-Matsuba (GitHub issue #58, 20 Oct 2026; repository
https://github.com/Harumi-Matsuba/kagigo1901-public, code MIT, documents and data CC BY 4.0). Checked here 21 Oct 2026.
Page: `docs/army1902.html`. Outside the LLM paper's scope (Japanese, not a European classical cipher); contributed.

## The cipher

Domestic telegrams of the Imperial Japanese Army in which two digits stand for one kana. A coordinate table:

| first digit | second digit (consonant column, reverse gojūon) |
|---|---|
| vowel row a 0, i 1, u 2, e 3, o 4; +5 for a voiced kana | a 9, ka 8, sa 7, ta 6, na 5, ha 4, ma 3, ya 2, ra 1, wa 0; voiced ga 9, za 8, da 7, ba 6 |

ン = 10; a final 80 is taken as an end mark (conjecture). カ = 08, シ = 17, ガ = 59, ブ = 76. The same table appears from
March 1902 (Osaka) to January 1904 (Kokura, Moji). Whether it is the Army's 鑰号 (Yakugō, 1900–04) used without its key,
or the numeric part of 特号 (Tokugō), is not settled (contributor's METHOD §6); not claimed here either.

## The telegrams (one table, four telegrams)

| JACAR | frame | date, route | pairs | reading | against |
|---|---|---|---|---|---|
| C09122911500 | 0110 (translation 0108) | 27 Mar 1902, Osaka: Chief of Staff Ōyama → Lt-Gen. Terauchi | 35 + 80 | ホンシヨクキキヨウマデホンブノジムハキクワンヨロシクトリハカラハレタシ (本職帰京迄本部ノ事務ハ貴官宜シク取計ハレタシ) | 35/35 |
| C09123116600 | 0026 (reply draft 0025) | 25 Jan 1904, Kokura → Maj.-Gen. Iguchi, General Staff | 13 | ヨヨウノカンコクチズダイヨ + clear サレタシ ヲハラ (要用ノ韓国地図貸与サレタシ) | no translation; reply draft sends maps of Korea |
| C09122909900 | 0079 (translation 0078) | 28 Mar 1902, Osaka: Ōyama → Maj.-Gen. Fukushima | 12 | カシグンエンシウケンガク (カイグン…, naval exercise observation) | 11/12: イ written 17 (シ), table 19 |
| C03020059400 | 0119 | Jan 1904, Div. commander Inoue → War Minister | 12 | シンテイアクゼウシレイブ (辛碇泊場司令部) | 10/12: 09 (ア) for ハ 04, 88 (ゼ) for ジ 68 |

Not included: C09122806100 (18 Feb 1901, Hiroshima, Manabe → Tamura), 15 pairs in four runs that the 1902 table does
not read (the same ニ is 91 and 69). A different method, so by the one-key rule it is not part of this target; the
contributor's OPEN.md lists what was tried. Unread.

## How the table was found (contributor)

From C09122909900's 12 pairs and the furigana of its outgoing draft C09122909800 (カイグン, エンシウ): ン = 10 three
times, the first digit mod 5 follows the vowel, ≥ 5 only for voiced kana, ア 9 カ 8 サ 7, so reverse gojūon columns.
Then C09122911500 (found afterwards) agreed on all 35 pairs; only the ba column (6) was fixed from its ブ = 76.
So the 35/35 is not wholly independent of the table: the table's shape was completed with it in view, though
only one column value came from it. **C09123116600 is the real test**: 13 pairs, found by searching the catalogue
for digit runs, no translation, and it reads as a request that fits the reply draft in the same file. Two spellings in
it are irregular (ヨヨウ for ヨウヨウ 要用, ダイヨ for タイヨ 貸与); the contributor takes them as the sender's.

Method category: key recovered based on adjacent plaintext (the outgoing draft's furigana and the filed
translations beside the cipher). Provenance contributed. AI-only work (Claude Opus 5.5 transcription and table;
Codex and Claude Sonnet blind second transcriptions, lowest agreements 97.2%, 100%, 84.6%, 87.5%); no human check.

## Checks made here (21 Oct 2026)

- `decode.py` written from the stated table only. All four telegrams decode as the contributor says (`decode_out.txt`):
  35/35, 11/12, 10/12, and ヨヨウノカンコクチズダイヨ.
- Permutation control (`python decode.py control`, seed 1902, row and column digits shuffled, 1,000 tables):
  C09122911500 max 16 against 35; C09122909900 max 6 against 11; C03020059400 max 6 against 10; none reaches the
  real score (`control_out.txt`). Matches the contributor's figures (max 16 for 0110).
- JACAR images fetched (C09122911500, C09123116600, C09122909900 PDFs). Every digit of frame 0110 and frame 0026 read
  here against the transcription, column by column (columns right to left, top to bottom): all agree. One glyph,
  column 3 row 10 of frame 0110, looks like 九 but is read 五 (45 = ノ in ホンブノ), as the contributor has it.
- **Discrepancy in the contributor's repository**: `data/transcription.txt` and `data/telegrams.tsv` give
  C09122911500 with 34 pairs (column 2 = 一八四二…, reading ホンシヨクキヨウ…, "34/34"), while README and READING.md
  give 35 pairs (一八一八四二…, キキヨウ = 帰京, 35/35). The image shows 一八一八 at the head of column 2, and 35 pairs + 80
  = 72 digits matches the form's count of 72 characters. READING.md is right; the two data files are stale (the
  JACAR catalogue's own transcription drops the 18, per READING.md). `ct_C09122911500.txt` here has 35 pairs.
- C09122909900 and C03020059400 were not re-read here.

## Remaining gaps
- C09122909900 pair 2 (17 for イ) - blocker: needs-physical-access; the image shows 七, writer's or transmission error; binarised JBIG2 scan cannot settle the head of column 2 either
- C03020059400 pairs 5 and 7 (09 for ハ, 88 for ジ) - blocker: needs-physical-access; one digit off each, the 九/四 doubt needs the original

## Escalation
- [x] siblings: the contributor viewed about 420 items (1,088 frames) of the 1901-02 telegram files and 235 items of the 1904 Daijiki; C09123116600 found by a catalogue search for digit runs
- [x] clear-pages: the filed translations (fr. 0108, 0078, the Daijiki text) and the outgoing draft C09122909800 used as cribs
- [x] known-keys: Cryptiana's 1874 and 1894 Army coordinate ciphers (iroha order) do not fit; the 1902 table does not read C09122806100
- [x] print: contributor's prior-work check (PRIOR_CHECK.md, 20 Oct 2026) found no earlier reading
- [x] key-rebuild: table complete for the observed values; unobserved cells inferred from the rule
- [x] retry: the discordant digits judged blind by Codex and Sonnet (4 runs); none overturned the first reading

## Files

- `ct_<JACAR>.txt`: the digit pairs per telegram (from READING.md; 0110 and 0026 checked on the images)
- `decode.py`, `decode_out.txt`, `control_out.txt`
- Images are not committed (JACAR PDFs fetched into the scratchpad); crops for the site: `docs/army1902_f0110.jpg`, `docs/army1902_f0026.jpg`
