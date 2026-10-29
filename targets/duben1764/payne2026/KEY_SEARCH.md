# Continued search for the May1764 key

Updated28October2026. The May letter's key is **not yet found**. This file records new sources actually inspected, distinguishing sample comparisons from exhaustive rejection.

## Uppsala F474: full portfolio now publicly accessible

The previous DECODE metadata lead can now be followed without an account through [Alvin record164482](https://www.alvin-portal.org/alvin/view.jsf?pid=alvin-record%3A164482), **Grön portfölj med chiffre-klaver**. Catalogue date:1767–1770 plus several undated items. The entire38-page scan was downloaded from the record's actual PDF link and visually surveyed. Relevant tables were rendered at3600pixels wide and enlarged for sample readings.

Public PDF: `https://www.alvin-portal.org/alvin/attachment/document/alvin-record:164482/ATTACHMENT-0039.pdf`.

The catalogue's contents and actual PDF page sequence differ: covers and reverses count as pages, and several sheets contain more than one key component. Use the following scan-page map rather than assuming DECODE item numbers equal PDF page numbers.

| PDF pages | Material inspected | Result / limits |
|---|---|---|
|1–2,38|Portfolio exterior/interior|No cipher values|
|3–4|Clavis Positiva; reverse|Alphabetic syllabary, with letters including Germanic forms; language of any target use unproved|
|5–7|Short additional alias list; reverses|Starts at136; fairy-tale/person aliases, not the full May key|
|8–10|Chiffres François cover and reverses|Folder, not a key by itself|
|11–12|Clavis Resolutiva; reverse|Numerical counterpart of p3, checked on selected entries|
|13–15|Names and places list; reverse|Includes Princess Albertine, king, queen, Sinclair, Düben, Gyldenstolpe; no date inferred solely from these names|
|16–17|Large key starting100:A|At some labels syllable and word values coexist; partial sample only|
|18–19|Alphabetical French table; following cover names Mr de Lary|Association follows scan sequence/catalogue; complete-table transcription not done|
|20–21|Three numbered tables; reverse headed A Déchiffrer1770|Many values1–480 in each table; a table-selection rule must be established before application|
|22–25|1767 enciphering/deciphering tables and labelled reverses|Heading Entre S.E. et Moy; neither initial is expanded into a named correspondent here|
|26–27|A Chiffrer1770 table and reverse|Possible counterpart of20; exact equivalence not yet independently checked|
|28–37|Envelope and perforated card/metal grilles|Different physical mechanism; no evidence connecting them to the numeric May letter|

The [2016 Uppsala library article](https://400-blogg.ub.uu.se/2016/07/11/postvaska/) independently identifies the portfolio as F474 and shows photographs. Its small sample photograph is the alphabetical table visible in the full portfolio, not a new standalone key. The full catalogue scan is much more useful than that photograph.

### Bounded comparisons

`f474_key_samples.tsv` records27 primary-source sample entries across four table families; doubtful readings carry M grades. `screen_f474_samples.py` reproduces `f474_fingerprints.json`. Examples:

| Family |218|578|583|
|---|---|---|---|
|Clavis, pp3/11|ng|ob|xa|
|100:A family, pp16–17|conversation|luthérien|not transcribed|
|French alphabetical table, p18|amitié|Parme|not transcribed|
|1767 pair, p24|uncertain abbreviation|q|si|

These samples have produced **no accepted May-letter reading**. They are not complete key transcriptions and do not exclude transformations, polyphony, null conventions or changed versions. Do not report these sources as cryptanalytically ruled out. The27 sample entries are not added to a recovered May key.

## Riksarkivet: more directly dated sources

The public records and JSON-LD were inspected for these holdings:

| Holding | Date in catalogue | Relevance | Online availability observed |
|---|---|---|---|
|[Chifferklaver202/8](https://sok.riksarkivet.se/arkiv/SfXY9HOEpqQefZv3xfb3Q3)|1750s–1770s|Positive/resolutive cipher keys|Physical-instantiation metadata; no scan link found|
|[Chifferklaver202/9](https://sok.riksarkivet.se/arkiv/8DzDWd4HCYBHXlPHDbU1E2)|1750s–1770s|Positive/resolutive cipher keys|Physical-instantiation metadata; no scan link found|
|[Chifferklaver202/10](https://sok.riksarkivet.se/arkiv/CWJMnfyLXw7TgYfPC7DAB5)|1760–1770s|Positive/resolutive cipher keys|Physical-instantiation metadata; no scan link found|
|[Diplomatica Muscovitica,71](https://sok.riksarkivet.se/arkiv/tKVBbqrjL4ke78ui7pI720)|1763–1766|Envoy Carl Wilhelm von Düben's letters/archive; contemporary official copies might identify a key or supply a clear copy|No scan link found; no key explicitly named in this record|
|[Gyldenstolpe collection, Sjöholmsarkivet](https://sok.riksarkivet.se/arkiv/6rwr4tudIaUl0BlcR403m2)|Undated collection|Recipient's papers; catalogue redirects royal letters to Kungliga biblioteket and exercises to Ericsbergsarkivet|No scan link found; contents require a more detailed finding aid|

For structured source metadata use `https://data.riksarkivet.se/archive/<record-id>.jsonld`. The API searches for Düben(160hits) and Gyldenstolpe(174hits) were read across both result pages; the above are selected relevant holdings, not a claim that every individual letter is catalogued by name.

These are **archive leads**, not located keys. The broad date ranges alone do not establish that any key in202/8–10 belongs to the private royal channel.

## Related1768 letter: clear draft, not numeric ciphertext

[Alvin490037](https://www.alvin-portal.org/alvin/view.jsf?pid=alvin-record%3A490037), F414, is headed15November1768, no1, Chiffrée. The catalogue describes an original of a dispatch sent in cipher to Sinclair and delivered to C.W.vonDüben. All six scan pages were visually inspected: the extant draft is clear French, with corrections, and supplies no numeric cipher run for comparison. The parent component490036 has1758 in one date field; the detailed record and manuscript heading say1768. Do not silently use the parent typo as evidence of an earlier cipher.

PDF link from the record: `https://www.alvin-portal.org/alvin/attachment/document/alvin-record:490037/ATTACHMENT-0007.pdf`.

## Language and dating cautions

- The French clear passages do not by themselves prove the language beneath the May cipher. Göran Behre's article *Postspionaget under1700-talet* describes earlier Swedish diplomatic correspondence using French clear letters and Swedish cipher letters. That is historical context, **not evidence that this particular letter is Swedish**. The journal issue identifies the article as Scandia29:2(1963); the library blog's2008 reference appears to follow the online publication date. No target-specific key or plaintext was found in the searchable article text.
- The large K259 key cover161 names C.W.vonDüben and A.H.vBorcke. Several historical Borckes have similar names; no identity or key date is established here from a generic biography. Its first sample substitutions remain unvalidated.
- Key219's verified1771 use is positive evidence about that later letter. It does not date all the loose keys in K259 or F474.

## Most useful next checks

1. Obtain detailed inventories/images of Chifferklaver202/8–10 and the contemporary Düben file71, looking specifically for the private Düben–Gyldenstolpe/queen channel and key change notices.
2. Check the recipient's surviving papers and the KB royal letters for copies, enclosures, or key instructions.
3. Continue the primary-source alignment work on K259 images124–126, allowing documented spelling variation and checking disputed numeric groups first.
4. Complete additional F474 transcriptions only where a specific sample, date, instruction or correspondent gives stronger evidence of relevance; avoid equating a broad numerical range with a key match.

No archive inquiry, email or account creation was sent. Large scans remain outside the contribution folder; stable source URLs are recorded here.
