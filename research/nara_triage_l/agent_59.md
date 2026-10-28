# RG 59 negative-phrase triage (neg_59.txt, 334 items)

Agent pass, 27 Oct 2026. Input `research/nara_triage_l/neg_59.txt`. Full OCR fetched with `reels.py fetch` (cache in
`research/nara_reels/cache/`).

## Confirmed candidates

### 1. Coahuila state code telegrams, Múzquiz–Saltillo, June–July 1906 (Kickapoo affair)

- naId 19505183 (M862 roll 342, Numerical File 3703-3713), file 3706/36-45; frames M862_Roll342-0505 to -0513
  (8 telegrams, numbered 35-45 as enclosures), covering letter frames -0501/-0503, Department reply -0514/-0517.
- Correspondents: Jefe Político L. A. Guajardo (Múzquiz) and the 1st Judge of Letters F. Valdés Llano → Governor
  Lic. Miguel Cárdenas (Saltillo); Cárdenas → Guajardo; R. C. Conine (Múzquiz) → Guajardo (Monterrey); Guajardo
  (Sabinas) → Ignacio E. Rivas.
- Ciphertext: English (and some Spanish) translations made for the US Senate subcommittee, with the code passages
  left as two-digit numbers (e.g. "Conviene 70 48 35 40 34 30 98 99 70 90 73 49 75 42 90 40 98 74 43 33 para ...").
  Roughly 400-450 two-digit groups across the 8 telegrams; repeated words ("10 35 30 18", "10 35 70 18") and the
  mixed clear/code layout suggest a letter-level substitution (two-digit numbers for letters), Spanish plaintext.
- Why unread: Senator H. M. Teller (Senate Indian Affairs subcommittee on the Mexican Kickapoo land frauds) got the
  copies from the Múzquiz telegraph office and sent them 8 Nov 1907 for decipherment; Root replied 14 Nov 1907 that
  the Mexican Embassy "does not know the code and is unable to decipher it", suggesting the state governors' code,
  and returned copies. No decipherment in the file (rest of roll checked).
- Prior art to check: Senate hearings "Affairs of the Mexican Kickapoo Indians" (S. Doc. 215, 60th Cong., 1908)
  may print these telegrams, possibly with a reading if Teller obtained one. Not checked yet.
- Dedupe: known.py "Kickapoo", "Muzquiz", "Guajardo": no hits; naId not in catalogue.json.
- Link: https://catalog.archives.gov/id/19505183
- Prior art: web search 27 Oct 2026 ("Affairs of the Mexican Kickapoo Indians" + Guajardo/Cárdenas/Múzquiz cipher)
  found nothing. The Senate hearings (S. Doc. 215, 60th Cong. 1st sess., 1908) should still be checked for the
  telegrams and any reading Teller obtained later.
- Scores (suggested): year 1906, region Americas, period 1901-1950, language Spanish, cls C (no key, but long and
  probably a simple two-digit letter substitution with English/Spanish context), importance 2, solvability 4,
  difficulty 2. The code passages appear only in this typed translation copy; the Spanish originals went back to
  Teller.

## Leads not confirmed (ciphertext not on the fetched frames, or only a purport entry)

- Soviet radio cipher intercepts, Constantinople 1921: purport list naId 87657409 (M973-204-0916, -0965, -0970)
  shows Adm. Bristol (US High Commissioner, Turkey) sending "cipher tels. sent from and to Moscow" (861.00/8575,
  Apr 1921), "Russian cipher radio messages exchanged between Moscow and Berlin" (861.00/9071, Oct 1921), cipher
  messages from Soviet wireless (861.00/9130, /9132, Oct-Nov 1921), Moscow-Christiania messages (861.00/9133).
  The enclosures would be in 861.00 (M316), which is not among the digitised RG 59 items in the bulk scan. Worth
  a request to NARA or a check of M316 rolls if they appear online. No reading known.
- German Legation La Paz code messages, 1942: purport naId 88161456 (M973-594-1189): FBI (Hoover) returned copies,
  "unable to decipher same". Underlying file in 862.20224 / 800.20210; not fetched (fetch failed with 502).
- Peru #741, 1942: purport naId 88159920 (M973-593-0200): code messages typed on W. R. Grace machines "could not
  be decoded, as cipher tables are not available". Purport only.
- Joseph Henry Grimes, Manila 1898-99: naId 153563607 (M179-1074-0163): War Dept. reports his seized papers "were
  in cipher, the key to which could not be discovered". The papers are not in this file (probably RG 94/395 or
  the Philippine Insurgent Records).
- C. P. Van Ness, Madrid, 1831-32: Livingston (M77-142-0024, naId 149332001) says his despatches are "written in a
  cypher to which we have no key in the Department"; Van Ness replies (M31-031-0184, naId 188612517) that he used
  the newest cipher in the legation archives and that the two despatches held "a paragraph or two in cypher" each;
  he sent duplicates. The OCR of M31 vols 30-31 (naIds 188612109, 188612517) shows no numeric runs, so the cipher
  passages could not be located from OCR (possibly read interlinearly, or OCR missed the figures). Small; the
  JQA Madrid code (targets/jqa/code_table.tsv) is the obvious key to try if the frames are found.

## Rejected (counts)

- 334 items in neg_59.txt. Confirmed 1; unconfirmed leads 5 (above).
- ~150 US code-room traffic: Department or legation telegrams in the US codes that a post could not read (wrong
  code book, garbled, no key at post); the Department held the key. Includes Ralston 1902 (189185310, read by the
  Department), San Salvador 1907 "Merry" cables (19665732, 21 groups, Department decode notes on the frame),
  Panama 1892, Denmark 1867, Russia 1871 (two words), Austria 1898 and similar.
- ~70 purport/card-index entries summarising code administration (strip ciphers, code destruction, cipher tables).
- ~40 "could not decipher" handwriting, signatures, addresses, ballots, inscriptions (not cipher).
- ~30 secret-ink / invisible-ink mentions: regulations, FBI purports on WWII Axis secret-writing letters (all
  developed and read, or only summarised), Trotsky trial reports, etc.
- ~15 cipher inventors offering systems to the Department (1822-1908); no target ciphertext.
- Thomas Pinckney 21 July 1795 (M570 95119261; M179 calendar 152951716): read, deciphered on the copy sent to
  Congress 26 Feb 1796 (ASP Foreign Relations 1:534-35, per Washington Papers editors).
- Newspaper puzzle "cryptograms" and similar noise.

Fetches used: 19505183, 153563607, 149332001, 189185310, 188613022, 188612109, 188612517 (+ cached 19665732,
87657409); two catalogue searches. 88161456, 152951716, 87921209 not fetched (502 error, not retried further).
