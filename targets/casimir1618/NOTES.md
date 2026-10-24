# Ernst Casimir's cipher keys, KHA A23-311 (1590s-1627)

Status: in progress (keys inventoried; the one ciphertext, scan 027, not yet read)

## Source

Koninklijk Huisarchief, The Hague, A23-311, "Stukken met sleutels voor geheimschrift gebruikt in brieven met diverse
correspondenten", 1618-1627 and undated; 97 scans fetched through the Koninklijke Verzamelingen rendition API
(`scan_ids.json`; `img/` git-ignored). Cover: "Verschiede Cyffers door Graaf Ernst Casimir en Syne Hoogh. Officieren
en Ministers gebruickt, onder andere ook die van de Koning van Denemarken en den Prins van Orange". Found by the
Nationaal Archief sweep, KHA lead K2.

## What it holds

`inventory.md` (made by a subagent, 24 Oct 2026; several cursive readings marked "?"): about 26 distinct keys.
Despite the catalogue's 1618-1627, a large group is from the 1590s Frisian war (Eusum, Cnoop, Vernou, Cornput,
Verdugo). Dated keys 1618-27: Utrecht Dec 1618, Casembroot 1623, Justinus van Nassau 1624, Prince of Orange
(Frederik Hendrik) 1626, Obrist Limbach 1626, Graf Solms in Danish service 1627; a cover-name code (Maccabaeus = Ernst
Casimir, Numa = King of Denmark, Tullius = Althusius). Thirteen keys use numbers (ranges in `inventory.md`).

## The ciphertext (scan 027)

Willem Lodewijk of Nassau, stadholder of Friesland, Leeuwarden, 5 April 1594, to an unnamed officer: clear Dutch with
about a dozen cipher runs in Greek-like signs. It uses the word signs of the 028 key (circled sign = *staten*, barred
sign = *soldaat*), but the 028 alphabet applied straight does not give Dutch; the letter itself says the recipient
found "onse laetste cyffer seer duncker" and so they kept the old one. Next: a sign-level transcription and a
substitution solve against Dutch (`lang` nl model), or a search of the other alphabets in the folder (028, 003, 016,
029) for one that fits.

## Matches to open targets

No ciphertext on DECODE or in the catalogue names Ernst Casimir, Willem Lodewijk or Frederik Hendrik. Candidates to
test the numeric keys against: Riksarkivet R4284 (Camerarius 1628), R4306 (1632), R4333-R4337 (Rusdorff 1628).
Not yet done.
