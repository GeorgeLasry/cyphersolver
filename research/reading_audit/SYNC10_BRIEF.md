# Site sync for the per-document read bar (24 Oct 2026)

A document is now *read* only when 95% of its words read as sense (`read_share` in its profile entry, measured by
`v10_relabel.py`); one that builds coherent sentences under 95% is *read in part*. `v10_relabel.tsv` lists every
measured document (folder, entry index, doc, file, words, read_share, state); 155 moved from read to read in part
and 35 targets moved from class read to read in part (`v10_class_moved.txt`).

For each target in your list, make its page `docs/<slug>.html` say exactly what the profile now says:
* where the page says a document (letter, folio, despatch) is read / deciphered in full and its entry is now
  "read in part", say it builds coherent sentences but reads at N% (its read_share), under the 95% bar, and keep the
  quote (it is the reading, holes marked);
* where the page's headline, title suffix or status line says the target is read and its class is now read in part,
  change it (title "— Read in part");
* do not touch the generated blocks (`texts:start`, outcome line, seal: the rebuild regenerates them) or any profile;
* keep image credits and the cipher snip; `python docs/_check_terms.py <slug>` must not get worse.
Do not edit README, ledgers, index or the manifest. Write long edits with the Edit tool. Stage nothing, commit
nothing, no helper agents. Reply as a table: folder / what changed / anything the page cannot say yet.
