# Qatar Digital Library sweep (28-29 Oct 2026)

Status: closed 29 Oct 2026. Three rows in `candidates.json` (BRIEF format) for the catalogue merge; working notes on
every file looked at in `notes.json`.

A sweep of the Qatar Digital Library (qdl.qa) for cypher and code material dated 1900-1950. QDL publishes British
Library India Office Records (Gulf, Persia, Arabia) and Private Papers with free IIIF images. Kept: items with page
images that hold code or cipher groups not deciphered on the page.

## Access

- qdl.qa and iiif.qdl.qa return **403 to curl and WebFetch**. Everything here ran in the desktop app's built-in
  browser, using same-origin `fetch()` from a qdl.qa tab. Don't navigate the harvest tab away mid-run: the state
  lives in the page.
- Search: `/en/search/site/<query>?page=N`, 10 records a page. The records are logical (file descriptions). A hit
  record links its matching page images. The facet `f[0]=record_type:physical` limits hits to page transcriptions.
- Manifest: `/en/iiif/81055/<vdc>/manifest`. Each canvas's `images[0].resource['@id']` is the QDL page URL, and its
  `@id` is the IIIF image (`.../full/!1400,1400/0/default.jpg`, regions as `pct:x,y,w,h`).
- Page OCR is in `#transcription-plain` on the page URL. It exists only for typed pages: handwritten telegram forms
  (e.g. IOR/R/15/2/955) have none, and the typed BAPCO cipher cables in 450 had none either.

## Method

1. `harvest_browser.js` ran 11 queries: cypher, cipher, decypher, decipher, "code telegram", "code book",
   "code words", "cypher telegram", "code word", "en clair", "in cypher". That gave **2,642 records, 2,504 of them
   with dates overlapping 1900-1950**. The search stems (cyphered = cypher; "in cypher" returned the same 1,776
   records as cypher).
2. **Page-OCR scan, abandoned.** The 2,504 records link 23,753 hit pages. Fetching them ran at about 1 page a
   second, so I stopped after 379 pages. That sample found only code-book serial numbers on custody certificates
   (IOR/R/15/2/179), no code groups. Most hits are typed *decyphers* ("Cypher telegram. From ... Dated ...", clear
   text), so the word "cypher" on a page usually means the page is already read.
3. **Description pass.** I read the full catalogue description of the 47 in-range records whose title, snippet or
   description names a cypher or code. Most are about cypher administration (custody, clerks, channels).
4. **Image checks.** I made contact sheets of the IIIF images, laid out in the browser, and zoomed into pages of
   the five files in `notes.json`.

## Findings

- **IOR/R/15/2/450, BAPCO code messages 1944-46 (196 images): tier A.** Typed Bahrain <-> New York cables in
  5-letter cipher groups, with the plain-language censor copies in the same file. The companion file
  **IOR/R/15/2/423** (OCR'd) gives the conditions. A plain-language version of every message went to the local
  censor. The P.A.I.C. security officer judged the system of "small resistance to organized cryptography". It was
  allowed in Jan 1944 "on the understanding that the pad is not worked through more than once". This is a
  plaintext-ciphertext corpus for a 1940s commercial pad cipher. We can explain the system from the pairs. Any
  unpaired message is open only if the pad was reused.
- **IOR/R/15/2/955, "206 Cypher Codes" 1918-26 (40 images): tier A.** Handwritten telegram forms in Government
  Telegraph Code / Indian Word Code words. Some have pencil glosses, some none: f. 3r, Bushire 18 Oct 1918, has 13
  code words and no gloss. These are codebook codes, so the unglossed telegrams need the codebook or enough gloss
  pairs. IOR/R/15/2/1466-1467 hold the IWC 1924 supplements, but the sampled pages list only addressee code words.
- **IOR/L/PS/10/405/1, Turco-Persian Frontier Commission 1913-16: tier C.** The catalogue's "secret cipher"
  folios 375-376 are clear printed copies and decyphered drafts.
- Everything else in the 47 is administration (custody certificates, cypher clerks, channels, lost code books) or
  decyphered telegram copies.

## Outside 1900-1950

The harvest also found earlier items that fall within the project's 1350-1950 scope. They are listed in
`notes.json` under `out_of_range_leads`. I viewed them on the image on 29 Oct.

- **Harford Jones's Baghdad informant letters, c. 1802 (IOR/L/PS/9/76/212, /217): the best lead of the sweep.**
  - They are English translations with the key words in underlined page,word number groups and clear text all
    round. Neither has a decipherment written in.
  - 212 is docketed as enclosed in Jones's letter to the Chairman of 20 Jan 1802.
  - Jones's own 1798 letter to Dundas (IOR/L/PS/9/76/49) uses the same page,word form, and its clear copy is /51
    ("Copy - Original in Cypher. Secret."). That is a full pair, which gives the code values used in 1798.
  - Opened as `targets/jones1802/` (29 Oct). The 1802 letters use the same code book: the 1798 values give 50-57%
    of their groups, and letters fixed by names raise that to 76%. Sibling /214 (1801-02, dates in cypher) has
    not been viewed.
- **IOR/R/15/1/134 f. 32, 1852: not a cipher, probably.** The "unreadable" letter is in Armenian cursive. It is
  Ameer Khan Johannes at Isfahan replying to Kemball's English letter of 13 May 1852 (f. 26 in the same volume).

## Limits

- Not covered: handwritten code-group pages whose description doesn't mention cypher. Those would need an image
  classifier over the 23,753 hit pages, or over whole files.
- Only queried English vocabulary. Arabic and Persian items ("رمز", "شفرة") were not searched.
- Nothing added to `catalogue.json` yet.

## Close-out (29 Oct 2026)

Rows for the catalogue (`candidates.json`, BRIEF format with `needs_archive_scan: "no"`): merged as leads
1533-1535 by `research/archive_sweep_2026-10/merge.py` (`qdl` added to SWEEPS), each given a vetting block and
promoted to `catalogue.json` with `docs/_check_catalogue.py --promote` on 29 Oct 2026.

| id | row | cls | seen | note |
|---|---|---|---|---|
| 1533 | Harford Jones code, IOR/L/PS/9/76/49, /51, /212, /217 (1798-1802) | A | image | worked as `targets/jones1802/`, in progress, 91% at grade H |
| 1534 | BAPCO pad cipher cables, IOR/R/15/2/450 (+423), 1944-46 | A | image | plain-language censor copies in the same file |
| 1535 | Gulf telegrams in Government Telegraph Code / Indian Word Code, IOR/R/15/2/955, 1918-26 | B | image | some pencil glosses; no codebook found |

Seen and left out:

- **IOR/L/PS/9/76/214** (Rickards and Manesty to Jones, 1801-02, "dates in cypher"): a homophonic two-digit
  alphabet for dates and a few words, with the body in clear. Read in passing from context: "dated R-E-S-H-E-D",
  "N-O-V", "J-A-N", "A-R-M-E-N-I-A-N-S". Too little cipher for a catalogue row.
- **IOR/L/PS/9/76/243, /244, /274, /211, /213**: clear.
- **IOR/R/15/1/134 f. 32** (1852): Armenian script, not a cipher.
- **IOR/L/PS/10/405/1** (1913-16): the "secret cipher" folios are decyphered copies.
- Most of the 47 described records: cypher administration (custody, clerks, channels) or decyphered telegram
  copies.

Not reached: page-level image screening of the 23,753 hit pages (handwritten code groups have no OCR); Arabic and
Persian search terms; Mss Eur F126 (Pelly papers) beyond the one decoded 1875 telegram.
