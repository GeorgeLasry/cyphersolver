# Academia Sinica (Taiwan) sweep, 28 Oct 2026

Goal: find unread ciphertexts (1600-1950) in the Academia Sinica archives: the Institute of Modern History (IMH,
近代史研究所檔案館) diplomatic files (Zongli Yamen 01-, Waiwubu 02-, Beiyang Waijiaobu 03-) and the Institute of History
and Philology (IHP, 史語所) Grand Secretariat archives (內閣大庫檔案).
Result: **9 candidates** in `candidates.json`, all from the IMH Waijiaobu files, all scored from catalogue titles only
(none viewed). The sweep was cut short by two blockers (below), so this is a partial harvest.

## Blockers

1. **The IMH archive search does not resolve from this machine.** `archdtsu.mh.sinica.edu.tw` (the old 檔案查詢系統)
   no longer exists in DNS (NXDOMAIN). Its successor `archivesonline.mh.sinica.edu.tw` resolves on Google/Cloudflare DNS
   (140.109.154.118) but not through the local resolver, so curl, WebFetch and the built-in browser all fail. Pinning
   the IP was refused by the permission system and was not pursued. `www.mh.sinica.edu.tw` and
   `archives.sinica.edu.tw` load fine. Fix: run the IMH part from a machine whose DNS resolves the host, or ask the user.
   Note that IMH image viewing needs a registered reader account in any case.
2. **The union catalogue blocked our IP.** The IMH item metadata (館藏號, 件名, 產生者, date, 頁數, 原檔/抄檔) is mirrored in
   the TELDAP union catalogue `catalog.digitalarchives.tw` (ASCDC). `Search.jsp?QS=<Big5-encoded term>&ShowPage=n` is
   server-rendered and scriptable (`harvest.py`), but after about 240 page requests at 0.7 s intervals the ASCDC
   firewall returned HTTP 401 "您的IP已被封鎖" for every request. The block was not circumvented; unblocking is by their
   問題回報 form. **Only two terms were harvested: 密碼 (1,148 hits, complete) and 密電 (225 of 581).** The other 25 terms
   in `harvest.py` (電碼, 密本, 譯電, 暗號, 暗碼, 密函, 隱語, 密信, 碼本, 電報密碼, 密電本, 不能譯, 未譯, 密碼電報, 密電碼,
   電本, 無從翻譯, 難譯, 密碼本, 密語, 暗語, 截獲, 偵譯, 破譯, 譯文) returned 0 because of the block, not because nothing exists.
   Rerun with a longer delay (several seconds) once unblocked.

## Method

- `harvest.py` -> `hits.jsonl` (1,373 lines; one per term x hit). 283 unique hits are Academia Sinica records
  (`imh_hits.txt`: term, date, producer, title, 館藏號, pages, original/copy, union-catalogue item path). The rest are
  National Central Library local documents and modern cryptography theses.
- IHP Grand Secretariat database (`newarchive.ihp.sinica.edu.tw/mcttpc/mctwebtp`, free version) was searched in the
  built-in browser by posting its simple-search form with `fetch` (session in hidden `SECU`): 密碼 0, 暗碼 0, 密信 0,
  密函 0, 蠟丸 0, 字母 0, 密字 0, 暗語 0, 密電 0, 電報 0, 暗號 6, 密書 4, 隱語 2, 密寄 2, 番字 7, 密本 68. All are clear
  administrative or legal records: 暗號 = secret-society hand signs, 密書 = secret letters in rebellion cases, 密本 =
  "secret memorial" (密本房 of the Board of War), 番字 = foreign script. **No ciphertext in the Grand Secretariat
  archives**; the collection ends in 1911 and holds no telegrams (電 matches 141 records, none telegrams).
- Dedup: `research/archive_sweep_2026-10/known.py` on Academia Sinica, sinica, Zongli, Chinese legation, Wellington Koo,
  Xinjiang, 密電, 03-32-073: no hits in the repo or DECODE.
- One web search for published work on Beiyang Waijiaobu code books found nothing specific (Columbia RBML blog on
  Chinese telegraphic codebooks covers the Nationalist period; Fudan's Wellington Koo e-archive lists 1921 Waijiaobu
  cipher telegrams copied from IMH hand copies).

## What the IMH hits are

Almost all of the 密碼/密電 hits are correspondence *about* cipher use, not ciphertext: rules on foreign merchants'
and consuls' code telegrams (Yingkou 1917, Chahar 1921, Urga martial law 1920, Yunnan/Chongqing Japanese consuls
1916-17), the WWI bans on enemy code telegrams (German at Wusong and Jinan 1914), Soviet protests over limits on
consular cipher traffic (Chita, Khabarovsk 1922-23), and the issue of code books to legations. Chinese telegrams
quoted in the files are in plain Standard Telegraph Code or already decoded, and are out of scope.

## Best leads (candidates.json)

1. **Xinjiang, Aug 1920: Russian cipher telegrams seized by the governor, sent via the Ministry of Finance "please
   decipher"** (4 pp.). The only title that says outright that the cipher reached Beijing unread. 3/2/4.
2. **Xinjiang, Dec 1919-Jan 1920: Russian officers' and the Kashgar consul's cipher telegrams detained** (6 records,
   ~15 pp.; 03-32-108-04-015 forwards the telegram copies). 3/1/4.
3. **Sep-Oct 1920: Russian legation/consular and Far Eastern Republic (Yurin) cipher telegrams held by Chinese
   telegraph offices** (03-32-432/433/436, 03-02-032-04). 3/1/4.
4. **"魯案密電（洋文）" 03-33-162-04-001**, 47 pp. copy: Shandong-question cipher telegrams in a Western language. 3/2/3.
5. **1920 Harbin/Jilin intercepts of Japanese army and diplomatic telegrams** (03-32-073 group, ~100 pp., incl.
   Uchida -> Obata). Probably Chinese translations; kept in case a record carries the code groups. 3/1/4.

Also: Brussels legation 密電 registers 03-13-043 (276 pp.), the 03-44-034 密電 volumes filed beside the 新十碼 code
books (class A if in code), Harbin Soviet representative 1921, Li Jiaao Moscow 1924.

## Key leads (code books and cipher rules, no ciphertext)

These can read Chinese legation traffic held elsewhere (Fudan Koo archive, Academia Historica, Second Historical
Archives Nanjing, intercepts in TNA HW 12 / JACAR):

- **新十碼密碼電本**, five volumes, Waijiaobu 03-44-035-01-001 (53 pp.), -02 (29), -03 (69), -04 (59), -05 (107), copies.
  The ten-digit code book of the Beiyang foreign ministry.
- 03-12-018-02-001 (May 1913): 新編密碼電本「甲密」 sent to the Washington legation (8 pp.); -003: 「由密」 code exchanged as
  乙密; -005 (Jun 1913): 美密電本 compiled for the US legation (8 pp.).
- Wellington Koo's legation code: 顧密電本 with a supplement 聯字條例補編 (Apr 1917, 20 pp., Waijiaobu 03, item
  `00/09/50/81`); request to re-edit the worn book (Jun 1917, `00/09/50/74`); 另編洋文代字密電碼 (Dec 1917, 03-12-018-02-017).
- 英文電報代字密碼用法 (English code-word cipher instructions sent from Washington to consulates, Nov 1917:
  03-12-018-02-007/-012/-013; Vancouver and Panama acknowledgements; Canada asks for the method).
- 會密電碼 for the Sino-Soviet conference (Apr 1925, 03-32-500-03-002), receipts from Chita, Harbin, Nikolsk.
- 1926-27 特密, 新外密, 仁密, 安密 code books (03-46-011-01, 03-46-012-01).
- Qing: Tang Shaoyi's code book for Korea (1897, 01-25-049-01); 廣州將軍 咨送電報密碼 (1898, 01-09-014-02-004);
  telegraph code for the Lüshun dock (1898, 01-18-071-03); Yang Zhaoyun in Belgium receives the 宇字密碼電本 (1902,
  02-12-027); 理藩部 辰午密碼電本 (1908, 02-02-004-04-014); 盛京將軍 洪字密本 (1902). These are receipts and requests;
  whether the code books themselves are in the files is not known.

Union-catalogue item paths for all of these are in `imh_hits.txt` (prefix `https://catalog.digitalarchives.tw/item/`).

## Not reached

- The IMH archive system itself (blocker 1): item images, finding-aid descriptions below title level, and the
  Zongli Yamen/Waiwubu files beyond what the union catalogue mirrors.
- 25 of 27 search terms in the union catalogue (blocker 2), and 356 of the 581 密電 hits.
- Academia Historica (國史館, ahonline.drnh.gov.tw) is the obvious holder of Nationalist-era (1928-49) cipher
  telegrams (蔣中正總統文物 特交檔案, 外交部 files) and of the code books of that period; not searched here.
- Second Historical Archives (Nanjing) holds the bulk of Beiyang Waijiaobu records; outside this sweep.
