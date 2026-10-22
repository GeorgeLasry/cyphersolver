# Huang Xing's three-kana telegrams, May 1916 (JACAR B03050731500, B03050089100, B03050731100)

Folder moved here from `targets/sunyatsen/` (HUANG_NOTES.md, huang.py) on 21 Oct 2026: the three-kana code is a
different system from the Swatow condensers, so it gets its own target (one key, one entry). Page: `docs/huangxing.html`.

## Status (21 Oct 2026)

Three telegrams in one code, all decoded with **S. Tomokiyo's three-kana formula** (Cryptiana,
chinesecrypto_e2.htm, added 23 Sept 2026): the standard Chinese telegraph code c written as three kana,

```
k1 = S1[c // 200]              S1 = the 46 kana column by column: a ka sa ta na ha ma ya ra wa / i ki shi chi ... wi / u ... / e ... we / o ... ro
k2 = S2[(c - 1) % 10]          S2 = a i u e o ka ki ku ke ko
k3 = S3[((c - 1) // 10) % 20]  S3 = ho he fu hi ha no ne nu ni na to te tsu chi ta so se su shi sa
```

| document | groups | how | result |
|---|---|---|---|
| Huang Xing → Lin Hu, Li Genyuan and others, 25 May 1916 (B03050731500 fr. 0246) | 46 | this project's transcription of 15 Sept 2026, Tomokiyo's one correction (O HI → CHI) | 46/46 |
| Military Affairs Council → Huang Xing, 20 May 1916 (B03050089100 fr. 0076–0078, groups 0–107) | 108 | Harumi-Matsuba (issue #48) | 60 as written, 43 spelling-corrected, 5 filled from the print; 102/107 against the 1916 print |
| Lin Hu, Li Genyuan and four others → Huang Xing, 20 May 1916 (same frames, groups 108–228) | 121 | Harumi-Matsuba (issue #48) | 73 as written, 43 spelling-corrected, 4 inferred, end mark |

Method: read with known key (Tomokiyo's formula). Provenance mixed: the reply from this project's own transcription,
the 20 May telegrams contributed. AI-only work throughout; no human has checked any transcription letter by letter.

### The reply, decoded from the cipher (`python threekana.py reply`)

> 隱印崧詔鬯行諸兄鑒：正寄函間，適接哿電，敬悉一切。護國軍能速入湘贑，甚好。行嚴何日東渡？望速啓行，先電示。興。徑

Run on this project's own transcription (huang.py, made 15 Sept 2026 before the formula was known), with the single
correction KONUOHIKE → KONUCHIKE. The "superfluous kana at position 106" of section 5 below was this misread CHI.
The cipher **corrects this project's reading of the cursive decode**: 詔 鬯 (not 誥/蕘 邕), 正寄函 (not 正發書), and no
章 before 行嚴 (the small 章 beside 行 on frame 0247 is a clerk's gloss, not enciphered). The addressees are courtesy
names: 隱 = Lin Hu (隱青), 印 = Li Genyuan (印泉), 崧 = Cheng Zikai (崧生), 詔 = Wen Qun (詔雲), 鬯 = Yang Yongtai
(暢卿/鬯卿), 行 = Zhang Shizhao (行嚴) (identification by Harumi-Matsuba from the 1916 staff lists in 軍務院考實; four of
them as in the footnote of 近代史資料 no. 50, which gives other names for the fourth and fifth). 近代史資料 no. 50
prints the reply without the 速 of 能速入湘.

### The 20 May telegrams (contributed, `sankana/`)

From Harumi-Matsuba's repository sankana-public (CC BY 4.0 for data; issue #48, 20 Oct 2026), copied here:
`sankana/romaji_raw.txt` (literal transcription, 126 words), `romaji_copy2.txt` (second copy), `corrections.csv`
(40 word and 9 group corrections with reasons and certainty), `groups.csv` (the final 229 groups), `worksheet.csv`
(the 1916 analysts' pencil notes against the reading).

Telegram 1 (groups 0–107), Military Affairs Council to Huang Xing, already printed in 1916 (護國軍紀事 no. 5,
軍政府歡迎黃克強電; the print was found by saberwatchmanga, 10 Oct 2026). A check, not a new reading:
> 黃克強先生鑒：奉删電，知公抵日，歡躍逾恆。堯等碌碌庸才，勉起討賊，正慮綆短，適逢公歸。願承不遺，俯賜提挈。公首倡共和，富有方略，各國情勢，考查復殷，將來內政外交，諸賴指導。大局所繫，惟公圖之。唐繼堯、岑春煊、梁啓超、劉顯世、陸榮廷、龍濟光、呂公望、蔡鍔、李烈鈞、陳炳焜。哿

Telegram 2 (groups 108–228), six at Zhaoqing to Huang Xing. No print; about 83 characters were pencilled on the 1916
worksheets. New as a continuous text:
> 公抵日，喜甚。潤輔當告公近形，以定進行方略。軍務院僅擁虛名，委員、代表等會皆未組織。協和軍旬內可齊，卽由韶入贑。非俟幹卿協和兵入湘贑，吾人恐難發言。馮段調停。此間暫置代理參謀事，源專任之。虎任第四師長，收集舊部約萬，亦卽出贑。楷調粤中湘軍卽出湘。釗擬來東，面達近情。虎、源、楷、羣、泰、釗。哿

**The correction rate is high.** 86 of the 229 groups (43 in each telegram) read only after a spelling correction
of the romaji, and 4 groups of telegram 2 are inferred (贑 164, 出 211, 楷 223, 泰 225). In telegram 1 the
corrections were made with the print in view, so their agreement with it is no test; the clean test is the 59
uncorrected groups of the printed passage, 54 of which match (the other 5 are wording differences). In telegram 2
there is no outside control beyond five spellings that appear as corrected in the second copy. The two copies agree in
114 of 126 words, so the misspellings were already in the transmission. Grade them M (corrected) and I (inferred).

### Checks made here (21 Oct 2026)

- `threekana.py` written from the formula alone, with this repository's code table (`../sunyatsen/tw.csv`), not the
  contributor's converter or Unihan extract.
- Reply: decoded from this project's own 15 Sept transcription, independent of Tomokiyo's and the contributor's
  romaji; 46/46 groups give exactly the contributor's text (`reply_out.txt`).
- Stream: all 219 coded groups of `sankana/groups.csv` decode to the contributor's character (219/219;
  `python threekana.py stream`, `stream_out.txt`). This checks the formula and table, not the 86 corrections or the
  transcription, which were not redone.
- Telegram 1 against the print (saberwatchmanga's transcription of 護國軍紀事 no. 5): 101 identical characters of
  107, plus 刪/删 (variant forms): 102/107, as claimed. Differences: 我 only in the print, 慮/憂, 提挈公/教言, 查/察.
- Their raw romaji run through this decoder unchanged: the stream loses alignment early (a misread kana shifts
  every later group), which is why the corrections matter; 634 of the 687 final kana are in the raw stream in order.
- B03050731100 fetched: images 24–26 (frames 0030–0031) are consul Ōta's telegram no. 42 from Zhaoqing, 21 May 1916,
  forwarding the stream at Cen Chunxuan's request ("（以下支那側暗號）"), romaji beginning *sokahokaet arakotsuka
  atauichire* as in B03050089100.

### Earlier repository

saberwatchmanga/sun-circle-cipher-1916 (published 10 Oct 2026; "an unfinished source audit") implemented the formula,
found the 1916 print of telegram 1 and compared it with the stream (107 characters), and left telegram 2 unresolved. It
is credited for the identification of the print; it did not publish a reading of telegram 2.

## Remaining gaps
- telegram 1, groups 48, 49, 50, 52, 58 - blocker: illegible; garbled in transmission (out-of-rule or transposed kana), filled from the 1916 print
- telegram 2, groups 164, 211, 223, 225 - blocker: illegible; garbled groups (6381 has no character, others one kana off), inferred from context and the reply, grade I

## Escalation
- [x] siblings: B03050731100 second copy compared (contributor); the reply B03050731500 decoded
- [x] clear-pages: frames 0079-0081 worksheets compared (sankana/worksheet.csv); frame 0247 decode corrected by the cipher
- [x] known-keys: Tomokiyo's formula; the Swatow condenser family does not apply
- [x] print: 護國軍紀事 no. 5 (telegram 1), 近代史資料 no. 50 (reply); no print of telegram 2 found (contributor, saberwatchmanga)
- [n/a] key-rebuild: the key is a fixed published formula, nothing to rebuild
- [x] retry: the four inferred groups tried against one-kana and one-digit neighbours by the contributor (corrections.csv)

---

# Earlier work (15 Sept 2026): Huang Xing to Lin Hu and Li Genyuan, 25 May 1916 (JACAR B03050731500)

Superseded by the status above: the "private codebook", the free-vowel reading and the superfluous kana were wrong;
the cursive transcription below is corrected by the cipher (詔 鬯, 正寄函, no 章).

Catalogue status on cryptiana: **"Solved but Specific Scheme Unknown"**. Tomokiyo found a memo that the
Japanese Foreign Ministry had filed a decode with the telegram, but reported he could not read the
handwritten Chinese and could not identify the encryption scheme. This note supplies both.

## 1. The file

JACAR **B03050731500** = Gaimushō record 1.6.1.75-1_015, reel 1-0955, frames 0244–0302 (59 images).
Fetched as a PDF from `…/content/item/aj12/C200138859200/raw/B03050731500.b10148.1-0955.00000244.pdf`
(the viewer is a single-page app; the `raw` path is in the page's `data-src`/JSON).

Covering note (frame 0244–0245), 電送第一九八〇号, cipher, **25 May 1916, 4.35 p.m.**, Foreign Minister
**Ishii** → Consul **Ōta at Zhaoqing (肇慶)**, no. 22:

> 黄興ヨリ林虎李根源宛電報依頼アリタルニ付同人ニ伝達アリタシ　内容ハ先日来電ノ挨拶ナリ（以下支那側暗号）

"Huang Xing has asked that a telegram be sent to Lin Hu and Li Genyuan; please pass it to them. The content
is an acknowledgement of the telegram received the other day. (Chinese-side cipher follows.)"

| frame | content |
|---|---|
| 0246 | the telegram itself, on an **Imperial Government Telegraphs** forwarded-message form |
| 0247 | **電稿** — the decoded Chinese text, cursive, five columns |
| 0248 | the clerk's **annotated reading** in Japanese word order, on 外務省 ruled paper |

## 2. The plaintext

From frames 0247 and 0248 together. The clerk's own glosses are in brackets.

> 隱印崧蕘邕行諸兄鑒　〔林虎・李根源等ノ字ナラン＝probably the courtesy names of Lin Hu, Li Genyuan and others〕
> 正發書翰之際，適接哿〔二十日〕電，敬悉一切。
> 護國軍能速入湘贛〔＝湖南江西〕甚好。
> 章行嚴〔Zhang Shizhao〕何日東渡〔日本ニ来ルヤ〕？速令出發，並望預電。
> 興　徑〔二十五日〕

"To brothers Yin, Yin, Song, Yao and Yongxing: just as I was sending a letter, your telegram of the 20th
arrived, and I have respectfully noted it all. It would be excellent if the National Protection Army could
move quickly into Hunan and Jiangxi. What day does Zhang Xingyan cross to Japan? Have him start at once,
and please wire me in advance. — Xing, the 25th."

Both date characters are 韻目代日 rhyme-codes: **哿 = 20**, **徑 = 25**, and 徑 matches the dispatch date
on the covering note exactly. Several characters of the cursive are still uncertain; the column lengths are
2 + 12 + 11 + 12 + 11, i.e. **46 characters** of message after the 電稿 heading. (Tomokiyo's note gives the
same column lengths but sums them as 68; they add to 48.)

## 3. The scheme

139 kana, no voicing marks, packed into ten-letter telegraph words. 46 characters into 138 kana is
**three kana per character**, with one kana left over at the end.

The gojūon syllabary is a 10 × 5 grid: ten consonant rows (—, k, s, t, n, h, m, y, r, w) by five vowels.
Group the kana in threes and ask which part carries the information (`huang.py`):

| reading | collisions in 46 groups | expected by chance | permutation p |
|---|---|---|---|
| consonant row | **7** | 1.03 | **0.006** |
| vowel | 8 | 8.28 | 0.70 |
| literal kana | 1 | — | — |

**Each kana carries one decimal digit in its consonant row; the vowel is a free homophone.** Every digit can
be written five ways, which is what makes the cipher look like pronounceable Japanese and why the surface
text almost never repeats. The repeated triples show the mechanism directly — the same character written
two different ways:

```
S K N   at 4, 35    SE-KA-NA  /  SHI-KO-NU
R - H   at 9, 13    RE-U-HO   /  RE-O-HI
T - H   at 2, 22    TA-U-HO   /  TE-U-HI
S K H   at 12, 18   SA-KU-FU  /  SHI-KI-HE
```

Three digits per character means a **private codebook of at most 1000 entries** — not the four-digit
standard Chinese telegraph code, and not Yamada's 20 × 5 condenser used in the Swatow telegram
(`NOTES.md`), which packs two digits into each kana-like syllable. This is a different and simpler design.

## 4. What is left

* the permutation mapping the ten consonant rows to the ten digits (10! but heavily constrained once any
  codebook is assumed, and constrained already by the repeat pattern);
* the codebook itself. With 46 characters of known plaintext aligned to 46 code triples, 46 entries of it
  are directly recoverable — the blocker is an exact character-by-character transcription of the cursive
  on frame 0247, where several glyphs remain uncertain.

Reproduce: `python huang.py` (no data files needed; ciphertext is in the script).

## 5. Corrections from the frames themselves (2026-09-15, second session)

The JACAR PDF was re-fetched (`jacar/f0244.pdf`, 59 pages; the raw path is
`/content/item/aj12/C200138859200/raw/B03050731500.b10148.1-0955.00000244.pdf` under www.jacar.archives.go.jp) and
frame 0247 was read at 500 dpi (`jacar/f0247_top.png`, `f0247_bot.png`). Four columns of 12, 11, 12 and 11
characters after the 電稿 heading, 46 in all, which is the number of kana triples:

> 隱印崧誥邕行諸兄鑒正發書 · 間適接哿電敬悉一切護國 · 軍能速入湘贛甚好[章]行嚴何日 · 東渡望速啓行先電示興徑

Section 2 above followed the clerk's Japanese paraphrase on frame 0248 (書翰ヲ發セルノ際, 速ニ出發セシメ且ツ豫メ電報アランコトヲ望ム)
and so had 50 characters; the cursive on 0247 has 46. 章 is a small interlinear addition beside 行 and is not
enciphered. The second character of column 2 (間 here) and 誥 in column 1 remain uncertain.

**One transmission error, located.** The plaintext repeats 行 (6, 32, 41), 速 (26, 39) and 電 (17, 43). Under the
grouping of section 3 only 行 6 = 32 matched. If one kana is dropped at position 106 (the O of OHIKE, the first kana of
character 36), every triple from 36 on shifts by one and all three repeats become **identical kana**: 行 = KE-KI-NI
three times, 速 = HE-U-HA twice, 電 = RE-U-SA twice, and the spare SU at the end completes character 46 (徑 = RA-KI-SU).
So the telegram as filed carries one superfluous kana, and the code is deterministic: the same character is always
written with the same three kana.

**This overturns the free-vowel reading of section 3.** The seven consonant-row collisions counted there are not
the same character written with different vowels; after the shift they are pairs of *different* characters (印/護
T-H, 誥/日 SKN, 鑒/間 R-H, 書/敬 SKH, 國/嚴 NKT, 甚/何 -KT, 諸/示 S-S) that share a row triple and differ only in
vowels. The vowels therefore carry information. What stands: 3 kana per character, a private code, the row of
the kana correlated with but not equal to the code value (the excess of row collisions over chance, p = 0.006, is
what the correlation looks like from outside).

**Row-to-digit test, negative.** If the rows were the digits of a 3-digit codebook compiled in dictionary order,
some permutation of the ten rows would make the 42 distinct characters' code numbers monotone in standard
telegraph-code (radical) order. Over all 3,628,800 permutations the best Spearman rho is 0.524; for the same test on
twelve shuffles of the plaintext the null gives mean 0.468 and max 0.614. No signal.

**Status.** Solved as far as one telegram allows: the scheme (three kana per character, deterministic, private
codebook of at most 50³ but presumably 10³ entries), the transmission error, and 42 codebook entries (character to
kana triple, listed by `huang.py` alignment). The kana-to-digit table and the rest of the book need a second
telegram in the same code. `python -c "import huang"`; the alignment table is in the session transcript and
reproducible from `huang.CT` with kana 106 dropped.
