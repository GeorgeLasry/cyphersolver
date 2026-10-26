# Brief: pair cipher passages with decipherments in a KHA item

Scan ids in order: the item's key in C:\Users\dbour\cypher\research\nationaal_archief\k89_ids.json (scan number =
position). 400-px thumbnails: th/<id>.jpg in this folder. Full size when needed:
  curl -sL -A "Mozilla/5.0 Chrome/120" -o <scratch>/<id>.jpg "https://cms.koninklijkeverzamelingen.nl/api/images/rendition/<id>/original/"
(crop with python PIL, view with the Read tool). Earlier thumbnail flags for the item: flags_a32.tsv / flags_a35.tsv.

Go through every scan (make your own contact sheets of about 12 thumbnails; open full size only to read dates,
headings and whether a decipherment is written in). Cipher can be numbers, letters or drawn signs. NEVER write
symbol shapes or non-ASCII signs; describe them in words.

Append to the output file, tab-separated, one line per cipher letter or passage: date as written, cipher page ids,
decipherment page ids or none, decipherment kind (interlined / separate clear copy / partial / none), approximate
size (lines or groups), system in words, note. Lines starting `# other` for keys, tables or clear copies without a
cipher page. ASCII only. Final reply per item: counts, how many deciphered, and the list with no decipherment
(date, ids, size, system).
