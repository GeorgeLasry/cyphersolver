# Hanoverian Privy Council, Mecklenburg commission, 1731-1761 (NLA HA Hann. 9g; Unsolved Catalogue no. 598) — NOTES

Status: in progress. Every cipher passage opened so far (five files, 1731-1738) carries its contemporary
decipherment written between the lines. One passage transcribed and read (Nr. 964 f. 6); the rest still to transcribe.

**Verdict so far: deciphered at the time.** The Hanover chancery wrote the decipherment above each line of figures, in
the rescripts from London as well as in the reports from Vienna. The catalogue's question ("whether decipherments are
filed with them is not stated") is answered: they are on the same pages. Outcome method, once the passages are
transcribed: *read from existing decipherment*. Checked 26 Oct 2026.

## Sources

- Niedersächsisches Landesarchiv, Abt. Hannover, Hann. 9g (Mecklenburgische Exekution / Kommission), Nr. 97, 379, 563,
  964, 1065, 1130, 1225, 1492, 1494, 1647. Finding-aid entries via the DDB index (Archivportal-D is behind an Anubis
  bot wall; the public Solr index is not).
- Images, public domain mark, no login. METS: `https://www.arcinsys.niedersachsen.de/arcinsys/mets?detailid=<v-id>`.
  Images follow a fixed pattern:
  `https://www.arcinsys-digitalisate.niedersachsen.de/nla_ha/hann._9g/nr._<n>/m_ha_hann._9g_nr._<n>_aufn_<NNN>.jpg`
  (about 7600 × 6700 px, one opening per image; `thumbs/` holds 150 px versions). `scripts/fetch_nla.py n:count ...`
  downloads and downscales them. Images are not committed.

| Nr. | Arcinsys | images | dates | finding aid ("Enthält: u.a.") | seen |
|---|---|---|---|---|---|
| 97 | v2492433 | 12 | 1733 | chiffrierte Verlautbarung, Christian Ludwig ↔ Seckendorf secret talk | all 12 |
| 379 | v2492434 | 23 | 1731 | zwei chiffrierte Schreiben an Georg II., Karl Leopold's Submissionsschrift | 4-8 |
| 563 | v2493774 | 19 | 1738-39 | chiffrierter Bericht aus Wien (Khart's "Gnadengeschenk"); chiffriertes Reskript | 5-8 |
| 964 | v2493412 | 19 | 1734-35 | chiffrierte Berichte Erffas aus Wien, Reichskontingent | all 19 (thumbnails), f. 6 zoomed |
| 1065 | v2493405 | 392 | 1734-38 | chiffrierte Reskripte Georgs II., schwarzburgische Truppen | not opened |
| 1130 | v2492829 | 16 | 1735-36 | chiffrierter Bericht Erffas, Rostock commandant | 5-8 |
| 1225 | v2493363 | 64 | — | chiffrierte Korrespondenz mit von Haus in Wien | not opened |
| 1492 | v2492740 | 308 | 1733-35 | z. T. chiffrierte Reskripte; Schwerin | not opened |
| 1494 | v2492742 | 253 | 1736-39 | chiffrierte Berichte Erffas, schwarzburgische Truppen | not opened |
| 1647 | v2493788 | 105 | 1760-61 | chiffrierter Bericht Steinbergs aus Kopenhagen | not opened |

## Cipher passages seen (image numbers = `aufn_NNN`)

| file / image | folio | piece | cipher | decipherment |
|---|---|---|---|---|
| 97 / 003 | f. 2r | P.S. to the King, Vienna 14 Jan 1733 (pr. 21 Jan) | about 9 lines of figures | interlinear |
| 97 / 004 | ff. 2v-3r | same P.S., continued | about 14 lines | interlinear |
| 97 / 011 | f. 10r | rescript, St James 2/13 Mar 1733 | 7 lines | interlinear |
| 563 / 006 | f. 4r | report, Vienna 1738 | 5 lines | interlinear |
| 563 / 007 | f. 4v | same | 8 lines in two runs | interlinear |
| 964 / 007 | f. 6r | rescript, St James 6/17 Dec 1734 | 4 lines | interlinear; **transcribed** (`texts/964_f6.txt`) |
| 1130 / 007 | ff. 6v-7r | Erffa's report on the Rostock command, 1735 | about 14 lines in four runs | interlinear |

The outgoing drafts (e.g. 964 / 004, to Erffa, 5 Dec 1734; 1130 / 005, to Erffa, 1735) are clear Konzepte with the
passages to be enciphered underlined. They are a second plaintext source for the outgoing letters, whose enciphered
originals are in Vienna, not here.

## The cipher

Undivided runs of figures, written continuously across lines, inside letters otherwise in clear German. A code, not a
letter substitution: on f. 6 about 140 figures carry about 20 words / 120 letters ("was ihr wegen des Mecklenburgischen
Reichs Contingents und dass dessen Stellung von des Königs von Preussen Maj. nicht übernommen werden möge"), too few
for one 2-digit group per letter, so the groups stand for syllables or words (probably 3- or 4-figure groups of a
Hanoverian code). Group boundaries are not marked. No key table was built.

## Remaining gaps

- The other cipher passages are not transcribed. Blocker: none from outside; it is transcription work on public
  images. Five files (1065, 1225, 1492, 1494, 1647; 1,122 images) not yet opened.
- No group-by-group check of a decipherment against the figures; that needs the code (rebuildable from the
  interlinear pairs, which would also give the Hanoverian code of the 1730s).
- Nr. 1647 (Steinberg, Copenhagen 1760-61) is a different decade and probably a different code; not opened.

## Escalation

- 0a siblings / clear pages: done in the sense that matters: the decipherments are on the cipher pages themselves.
- Next: page through 1065, 1225, 1492, 1494, 1647 (thumbnails are too small; fetch at 2400 px), list the cipher
  pages, transcribe each run with its interlinear decipherment, then align runs to decipherments to rebuild the code.
- Prior art: not on DECODE (Archivportal-D sweep README); no printed edition of these Hann. 9g pieces found in the
  quick web check of 26 Oct 2026. The decipherment found is the contemporary one, not a modern one.
