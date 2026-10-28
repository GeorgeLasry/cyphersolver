# Polish Museum of America (Chicago) sweep, Oct 2026

Sweep of the Polish Museum of America (Muzeum Polskie w Ameryce; also the archive of the Polish Roman Catholic
Union, which founded it in 1935) and related Chicago Polish/Central-European holdings, run 28 Oct 2026 under
`research/archive_sweep_2026-10/BRIEF.md`. Full search log: `coverage.md`.

**Result: 0 candidates** (`candidates.json` is an empty list). Zero is the honest count. It is not a
claim that the PMA holds no cipher; it means nothing described online says so.

## Method

1. **PMA archive guide** (Archiwa Państwowe / PMA 2019, 382 pp., the English version of the 2016 *Informator*):
   `https://archiwa.gov.pl/wp-content/uploads/2022/03/PMA_EBOOK.pdf`. curl and WebFetch got an Incapsula stub;
   the built-in browser loaded it, and the text (750k chars, 211 collection entries, 703/1-703/303) was extracted
   in the page with pdf.js and grepped. Cipher terms (cipher, cypher, encipher, encrypt, decipher, decod-,
   cryptogra-, secret writing, szyfr, coded, code book, chiffr-, tajn-) gave **0 hits**. Wider terms (code, key,
   telegra-, cable, secret, confidential, intelligence, conspira-, underground, courier, clandestin-, cyfr-,
   depesz-) gave 90 hits, all noise.
2. **PMA online catalogue** (PastPerfect, `polishmuseum.pastperfectonline.com`; curl gets 403, the browser works):
   45 keyword searches 3.2 s apart, in Polish, English and French cipher vocabulary. Every cipher term returned 0;
   the code, secret, klucz, tajne and telegram hits are book titles and photos. The archive records that do
   exist (e.g. 2016.03.0032, Haller's order of the day sent to Paderewski 1918) carry Polish scope notes, so a
   cipher item described there would have matched "szyfr*".
3. **Web searches** on the PMA, PRCUA, Kościuszko and Pułaski letters, 1863, Haller's Army, Paderewski and Polish
   National Department telegrams, the Ukrainian National Museum, and Polish guides to polonica in the USA (see
   `coverage.md` for each query and what it gave).
4. **Dedupe:** `known.py` for "Polish Museum", "Muzeum Polskie", PRCUA, "Polish Roman Catholic", "Ukrainian
   National Museum", Kosciuszko, Haller: no PMA item is in the repo, and DECODE holds no Chicago records.

## What the PMA holds that is closest to the brief (for a future on-site check)

The pre-1900 political and royal letters are few and catalogued only by sender, date and subject. None is flagged
as cipher, but these are the only places where an unflagged cipher passage could sit:
- **Royal Collection 703/215** (91 units, 1555-1868): Sigismund II Augustus 1555/1566, Sigismund III 1597,
  Ossoliński 1646, John Casimir 1668/1672, Sobieski 1683/1691, Marie Casimire 1697/1710/1715, Radziejowski
  1690/1698, Augustus II 1701/1704, Leszczyński 1708-1753, Augustus III 1734/1752, Stanisław August 1788/1791,
  Napoleon 1813, Czartoryski, Potocki and Małachowski family letters.
- **Tadeusz Kościuszko Collection 703/213** (122 units, 1775-1818), printed by the PMA in 1977 (*Autograph letters
  of Thaddeus Kosciuszko in the American Revolution*); no cipher noted.
- **Gen. Kazimierz Pułaski Collection 703/294** (8 units, 1772-1779).
- **Embassy of the Republic of Poland in Tokyo 703/11** (1939-41): letters to Ambassador Romer and press bulletins,
  not telegrams.
- **Polish National Department 703/8** (627 units, 1916-26): the Haller's Army recruitment forms and the
  department's correspondence; no code telegrams described.

## Key leads

None (no bare keys or code books found). Stanisław Ząbek papers 703/205 hold a WWI French radiotelegraph
operating manual, which is equipment instructions, not a cipher key.

## Not reached / blocked

ArchiveGrid (Cloudflare check), HathiTrust (403 to scripts), szukajwarchiwach (Imperva check, per the earlier
Polish sweep), and the Ukrainian National Museum archives (no online finding aid; in-person access only by the
director's permission). The PMA's item-level "working file" inventories are not online.
