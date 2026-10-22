# Japanese Army numeric kana cipher, 1902-04: decryptions of the four telegrams

The table section below is copied verbatim from NOTES.md ("The telegrams"); the block after it is decode_out.txt, the saved output of decode.py.

### The telegrams (one table, four telegrams)

| JACAR | frame | date, route | pairs | reading | against |
|---|---|---|---|---|---|
| C09122911500 | 0110 (translation 0108) | 27 Mar 1902, Osaka: Chief of Staff Ōyama → Lt-Gen. Terauchi | 35 + 80 | ホンシヨクキキヨウマデホンブノジムハキクワンヨロシクトリハカラハレタシ (本職帰京迄本部ノ事務ハ貴官宜シク取計ハレタシ) | 35/35 |
| C09123116600 | 0026 (reply draft 0025) | 25 Jan 1904, Kokura → Maj.-Gen. Iguchi, General Staff | 13 | ヨヨウノカンコクチズダイヨ + clear サレタシ ヲハラ (要用ノ韓国地図貸与サレタシ) | no translation; reply draft sends maps of Korea |
| C09122909900 | 0079 (translation 0078) | 28 Mar 1902, Osaka: Ōyama → Maj.-Gen. Fukushima | 12 | カシグンエンシウケンガク (カイグン…, naval exercise observation) | 11/12: イ written 17 (シ), table 19 |
| C03020059400 | 0119 | Jan 1904, Div. commander Inoue → War Minister | 12 | シンテイアクゼウシレイブ (辛碇泊場司令部) | 10/12: 09 (ア) for ハ 04, 88 (ゼ) for ジ 68 |

Not included: C09122806100 (18 Feb 1901, Hiroshima, Manabe → Tamura), 15 pairs in four runs that the 1902 table does
not read (the same ニ is 91 and 69). A different method, so by the one-key rule it is not part of this target; the
contributor's OPEN.md lists what was tried. Unread.

## decode.py output (decode_out.txt)

```
C03020059400: 12 pairs  シンテイアクゼウシレイブ  | agrees 10/12 4:09=ア/ハ 6:88=ゼ/ジ
C09122909900: 12 pairs  カシグンエンシウケンガク  | agrees 11/12 1:17=シ/イ
C09122911500: 36 pairs  ホンシヨクキキヨウマデホンブノジムハキクワンヨロシクトリハカラハレタシ|  | agrees 35/35 
C09123116600: 13 pairs  ヨヨウノカンコクチズダイヨ
```
