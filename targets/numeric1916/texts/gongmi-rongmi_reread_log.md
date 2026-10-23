# Re-reading log, 共密 (gongmi) and 容密 (rongmi) (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b21)

## Starting point

Reading audit (22 Oct): both decoded, not read. `texts/gongmi_decryption.md` and `rongmi_decryption.md` were verbatim
decoder output with clusters of wrong characters (N32, N33, N35; N19b, N21, V4D) and no translation in the folder.

## 1. Is there a text already?

- Not a DECODE target: the forms are JACAR B03050089200-89500, B03050089900, B03050090000.
- **Brice Dudout's Wenmi pages** (bdudout.github.io/wenmi/en/gongmi.html, rongmi.html, fetched 23 Oct 2026 into the
  session scratchpad) carry, per telegram, a raw decoding, a *proposed reading* ({x} = a probable reading replacing an
  anomalous character, 〔x〕 = kept, unresolved), an English translation and a digit table group by group. His
  convention matches ours closely; the reading follows it, checked group by group.
- His repository's `messages.json` (the source of our `groups.tsv`) was fetched as well: the **page digit tables are
  newer for gongmi**. Twenty groups were re-read by him on the scans since (N30, N32, N33, N35), nearly all 一/二/三
  confusions (1847 -> 2847 請, 2104 -> 1104 黃, 8229 -> 8339 同, 2729 -> 3739 興 ...): `gongmi_corrections.tsv`. Rongmi
  digits are unchanged.
- No other edition: Hsueh Chun-tu's 黃興等電稿 has nothing between 8 and 20 June (Dudout).

## 2. Alignment with the figures

`research/reading_audit/b21_wenmi_page.py` (page -> json of digits, readings, translations), `b21_wenmi.py` (decode with
our `decode.py`; align each proposed reading unit by unit with the decode; test every {x} for a one-digit variant of its
group), `b21_wenmi_md.py` (reading/English files, score). Output `gongmi_align.tsv`, `rongmi_align.tsv`.

| | characters | figure's own value | one-digit alternate | supplied [x] | [?x] | […] |
|---|---|---|---|---|---|---|
| gongmi | 555 | 510 | 21 | 3 | 21 | 0 |
| rongmi | 1,307 units / 1,306 groups | 1,197 (one table variant 偽/僞) | 41 | 15 | 47 | 6 |

The one-digit alternates are characters that rest on reading one digit of the copy otherwise (N17 速 訴 重 重 北, N18 目
興, N23 鑒 借 親, N32 強, N33 政 詢, N35 表 ×3 袁 法 國 ×2 速; rongmi V4B 18 ...). In N35, 表 and 袁 are written with 8 for 3 at
all four places (Dudout's note); the scan shows the 8 plainly (below), so these are the clerk's slips, not our misreading.

## 3. On the image

JACAR B03050089500 fetched as PDF (the `/content/item/aj12/C200138752900/raw/...pdf` path from the viewer page) and
p. 2 (N35 sheet 1) read at 6x: prefix 〇三六四 一三七八, then groups 1-8 exactly as on Dudout's page; group 8 is
八〇〇七 (8007 噸), so 表 (3007) is an alternate digit. The hand's 二 and 三 are slanted strokes that are often hard to
count (the 三 of the prefix 1378 shows two strokes), which is the source of most of the re-readings. The other sheets
were not re-read here.

## 4. Changes to his reading

- **N24 group 22**: 2530 滠 -> 2520 灰 (tens 三 read as 二): '灰日唐宅開會', on the 10th a meeting at Tang's house, after
  '佳日黎電' (the 9th) in the same passage. Adopted, counted among the alternates; sense-checked only, for review.
- **V4E group 23**: 8063 圉 -> 8053 垣 (one digit, 六/五, not a look-alike pair); V4D says 曉垣 went to Beijing. Kept as
  [?垣], a conjecture.
- Tried and not adopted: the telegram endings N32 會逵境, N33 會城, V4E 覃, N24 攴, N25 收 (signature/date codes: no
  variant gives a day code that fits); N36 樨 (variant 望 reads '東械望速運' but on sense alone); N17 漠行 (no variant gives
  實行); N24 硏 (three places, no variant fits all).

## Result

| doc | before | after (explicit holes, one character = one word) | rests on |
|---|---|---|---|
| gongmi | decoded, not read (Chinese: not scored by `_check_reading.py`) | 41/45 sentences clean, 0.91; 21 holes in 555 | Dudout's proposed reading, every character checked against the figures |
| rongmi | decoded, not read (not scored) | 82/90 clean, 0.91; 53 holes in 1,307 | the same |

Both read, grade B. Open: the [?x] characters (digits to re-read on the police copies, or names and date codes) and
N36 (11 holes in 58 characters), V4B (16 in 265); blocker illegible.

Example: N35 '段有襲袁故智之勢' — "Duan seems to be taking up Yuan's old tricks" (袁 on the alternate 3087 for the written
8087).
