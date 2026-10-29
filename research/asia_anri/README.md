# Arsip Nasional Republik Indonesia (ANRI) sweep, 28 Oct 2026

Part of the October 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`). Target: cipher and code
material, 1600-1950, held in Jakarta: VOC Hoge Regering, Algemene Secretarie, Binnenlands Bestuur, the Japanese
occupation and the 1945-49 revolution. Cross-checked with `research/nationaal_archief/` (the Hague side of the
VOC and of the 1942-50 Algemene Secretarie) and `known.py`.

**Result: 7 candidates** in `candidates.json` (2 held in Jakarta, 5 Hague items found through the cross-check
and marked "cross-lead, Nationaal Archief"), plus key leads below. Nothing here is scanned. ANRI's archive
holdings that matter are described only in PDF finding aids, and the VOC material shows no cipher at all.

## Method and endpoints

1. **Sejarah Nusantara** (`sejarah-nusantara.anri.go.id`, Corts Foundation/ANRI). Behind Cloudflare. Plain
   `curl` gets 403; `requests` with a browser User-Agent works (`fetch.py`).
   - Full-text search: `GET /search/?q=<term>&models=all&page=N`. It covers Realia, Marginalia to the Daily
     Journals, Diplomatic Letters, Placards, Appendices, Corpus Diplomaticum and the Harta Karun articles, *not*
     the full Daily Journals or the Hoge Regering volumes themselves. `harvest.py` ran 41 terms (cijfer, cijffer,
     cyffer, zyffer, sijffer, ciffer, gecijfert, cijfferschrift, chiffre, gechiffreerd, ontcijffert, geheimschrift,
     sleutel, cipher, cypher, nomenclator, code, sandi, rahasia, geheime, secreet/secrete ...) → `hits.jsonl`.
     Every cipher-word hit is a false positive (cijffer getallen on boats, sleutels of cash chests, geheime seinen =
     secret flag signals, Pastor Sleutel). "secreet/secrete" (534/313) are ordinary secret resolutions in clear.
   - The same page has an "Archive files" box (inventory-title search, max 10 per query, with page-browser link;
     scans need a free login). `harvest_files.py` → `files_hits.jsonl`: no cipher term matches any VOC or K66b
     inventory title.
   - The Hoge Regering inventory PDFs (`/media/userdefined/pdf/tanap_anri_hogeregering.pdf`, `BRILLVOCInventaris.pdf`)
     were grepped: no cijfer/chiffre/sleutel/code item; "geheimschrijver" is the secretary's title (inv. 2644-2653,
     correspondence with geheimschrijver J. Morees 1801-05), not secret writing.
2. **SIKN** (`sikn.anri.go.id`, Nuxt app). The search page calls an open JSON API found in its bundle:
   `https://svc-search-sikn.anri.go.id/archives?page=N&limit=100&qword=<term>[&repositories=<uuid>]`
   (also `/actors`, `/repositories`). `harvest_sikn.py` ran 46 terms (`sikn_hits.jsonl`, git-ignored). The search
   is fuzzy, and SIKN holds mostly regional archives (East Java province, Sumatera Barat, Wajo, Bima) and post-1950
   photographs. ANRI's own repository (`3bcfbe8a-34bc-4f7c-a997-01b961e085b9`) has 40,345 records, all dumped
   (`dump_anri_sikn.py` → `anri_sikn_all.jsonl`, git-ignored): only one is dated before 1951. So SIKN is not where
   ANRI's colonial and revolution archives are described.
3. **ANRI finding aids** (`anri.go.id/download/<slug>`, PDFs, found through `anri.go.id/search?keyword=`).
   `find_aids.py` collected 285 links (`finding_aids.json`); `get_aids.py` downloaded 130 textual inventories (132 texts with the two VOC PDFs)
   and guides (Algemene Secretarie series MGS/TGS/TZG/Besluiten/1942-50, Binnenlands Bestuur, residency lists
   1605-1923, Kementerian Pertahanan/Penerangan/Dalam Negeri 1945-49, Sekretariat Negara 1945-50, Delegasi
   Indonesia 1947-51, Kabinet Presiden RIS, Kepolisian 1947-49, Kejaksaan Agung Tentara 1945-49, the revolution
   guide GA-23, the defence guide GA-21 ...) into `pdf/` (git-ignored) and extracted their text; `grep_aids.py`
   → `aid_hits.txt` (cipher terms in context). This is where the Jakarta finds came from.
4. **Cross-check with the Hague.** The NA inventory 2.10.14 (Algemene Secretarie 1942-1950) marks every item kept in
   Jakarta ("wordt bewaard in het Arsip Nasional te Jakarta"). `na_21014_jakarta.py` pulled all 1,756 of them
   (`na_21014_jakarta.jsonl`); `na_jakarta.py` searched 2.10.14, 2.10.17, 2.10.62, 2.13.132 and others for code
   terms (`na_jakarta_hits.jsonl`) through the NA API (`zvt.nationaalarchief.nl/api/search/eads/<archive>?q=`).
   All the Hague items checked are `PHYSICAL` (not scanned). None of these archives is in the repo yet (known.py:
   no hits for 2.10.14, 2.10.17, 2.10.62, 2.13.132, Epidnation, Soerjotjondro).

## Best leads

| # | Shelfmark | Date | What | Note |
|---|---|---|---|---|
| 1 | ANRI Algemene Secretarie 1942-1950 inv. 1406 (= NA 2.10.14 inv. 1406, held in Jakarta) | Jun-Dec 1948 | Code telegrams of the Republican Soerjotjondro in Batavia to the telegraphic address "Epidnation", Singapore, held back by the telegraph office for NEFIS clearance | Finding aid: "the texts are not decoded and wholly unintelligible". **Caution:** "Epidnation" is probably the League of Nations (later WHO) Eastern Epidemiological Bureau in Singapore, so these may be epidemic reports in the published international epidemiological code. If so they are easy and minor |
| 2 | NA 2.10.17 inv. 735 (Procureur-Generaal) | 1947-48 | Intercepted Republican telegrams partly in code, with papers on breaking them | Dutch decipherment work; a key source for TNI/Republic codes |
| 3 | NA 2.10.62 inv. 6271 | 30 Jul 1948 | HK TNI mobilisation order with a coded message | Not stated as decoded |
| 4 | ANRI Algemene Secretarie inv. 24 | 1942-45 | Secret telegrams to Van Mook, the BSO and the navy in Australia, "often cryptic" | Probably cover names in clear |
| 5 | NA 2.10.62 inv. 2914, 4720, 5584 | 1946-48 | Republican codings intercepted at Makassar; Bandjermasin intelligence partly in code; East Java coded telegram | Local codes; sibling code sheets exist (key leads) |

## Key leads (bare keys and code material, no ciphertext)

- ANRI Algemene Secretarie 1942-50 inv. 54: "Stukken betreffende de telegrammen- en codedienst", 1945-1950 (held in
  Jakarta). NA 2.10.14 inv. 2308: the Regerings Codedienst (codes in use, security of code traffic).
- NA 2.10.62 (NEFIS captured documents): inv. 4678 "Code voor Boeginees en Makassaars en code voor Indonesische
  taal" (1947); inv. 4693 code found at Sampit, Borneo (24 Apr 1947); inv. 5470 "opgave cijfercode Markas Besar
  Tentara Staf Oemoem, Bagian Radio Code" (28 Sept 1947); inv. 5155 code of Angkatan Moeda PTT (20 Jul 1947);
  inv. 5438 code of the Satris signal service (1946, document missing).
- NA 2.13.132: inv. 2837 instructions for the field "geheimschrift" and key groups; inv. 2912 code words, lists,
  signals and secret writing.
- Dutch decodes of Republic traffic (cribs/keys for any open Republic code telegram): NA 2.13.132 inv. 938 (CMI
  Afd. VIII reports on "zeer geheime codetelegrammen" Kementerian Pertahanan Djokja ↔ Commandement Sumatra,
  12 May 1947 - 3 Feb 1948); NA 2.10.14 inv. 3904-3952 ("Zeer Speciale Rapporten", decoded intercepts 1947-49).
- The Republic's own codes: Dr Roebiono Kertopati's Dinas Code (from 4 Apr 1946), "Buku Kode C". Its records are
  in the Museum Sandi, Yogyakarta (BSSN), not ANRI (UGM thesis on Dinas Code ciphers, per web search).

## Dropped

- NA 2.10.62 inv. 5236: A.K. Gani's letter in code, Djokja 6 Jun 1947, decipherment in NEFIS doc. 3853. Read.
- CMI/NEFIS "Zeer Speciale Rapporten" and Afd. VIII reports: decoded texts, no ciphertext.
- ANRI Kabinet Perdana Menteri 1950-59 "kawat sandi" files (Irian Barat talks, Manila/Rangoon): 1951-54, past the
  1950 limit, and filed as decoded copies. Kamar Sandi Angkatan Darat / Jawatan Sandi administration files
  (1950-59) are administrative.
- SIKN "surat rahasia"/"geheim" hits (E.H. Eneth to Alting 1790, Wajo 1939-50): secret, not ciphered.
- Daily Journal / Realia "geheime seinen" (1761, 1803-10): secret flag signals, not writing.

## Not reached / blockers

- No cipher term appears in any VOC Hoge Regering inventory description, and the Sejarah Nusantara full text
  does not cover the Daily Journals or the letter-books themselves. The NA sweep found the same for the Hague
  VOC volumes (its row 16). A real search of the Batavia letter-books would need HTR text (GLOBALISE covers the
  Hague Overgekomen brieven, not the Jakarta Hoge Regering series).
- Scans: ANRI's scanned VOC volumes open only after a free Sejarah Nusantara login (not used). The 1942-50
  Algemene Secretarie, Binnenlands Bestuur and Republic archives have no online images at all; items need a
  reading-room visit or a reproduction request to ANRI.
- `jikn.go.id` does not resolve; `www.anri.go.id` returned Cloudflare 523 once; `sikn.anri.go.id` 403s plain curl.
- Japanese-occupation archives (1942-45): no ANRI finding aid with code/cipher entries turned up; the
  Japanese-era records ANRI holds are thin and mostly in the NIOD/NA Hague series.
- Malay-language diplomatic letters (Surat Emas, 1790-1820) are in clear by nature; no cipher found.

## Files

`fetch.py` (session with browser UA), `harvest.py`, `harvest_files.py`, `harvest_sikn.py`, `dump_anri_sikn.py`,
`find_aids.py`, `get_aids.py`, `grep_aids.py`, `na_jakarta.py`, `na_21014_jakarta.py`, `make_candidates.py`;
outputs `hits.jsonl`, `files_hits.jsonl`, `finding_aids.json`, `aid_hits.txt`, `na_jakarta_hits.jsonl`,
`na_21014_jakarta.jsonl`, `candidates.json`. `pdf/`, `js/`, `sikn_hits.jsonl` and `anri_sikn_all.jsonl` are
git-ignored (local `.gitignore`).
