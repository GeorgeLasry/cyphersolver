# Tamil Nadu graffiti marks (tngraffiti.in)

Source: the Graffiti Marks of Tamil Nadu web corpus (K. Rajan, R. Sivanantham, G. Sundar; Tamil Nadu State Department of
Archaeology and the Indus Research Centre, RMRL): https://tngraffiti.in/ , data API
https://api.tamilknowledgecampus.in/graffiti/ (endpoints indus, base-sign, concordance?signQuery=N, filter, sites,
options, fields-symbols). Pointed to by K. Rajan (email to D. Bourdeau, 26 Oct 2026); the book (Rajan & Sivanantham,
*Indus Signs and Graffiti Marks of Tamil Nadu: A Morphological Study*) is on tamilvu.org / tamildigitallibrary.in.
42 base signs, 544 variants, 1,521 composites from 9,486 graffiti.

- `raw/` (git-ignored; no licence stated): the API responses as fetched 26 Oct 2026 and the site's script bundle.
- `graffiti_indus_map.tsv`: each graffiti sign's Indus parallel as the corpus gives it (Mahadevan 1977 number,
  verified against the cited seals), mapped to ICIT. This is their identification, not ours.
- Concordance records: sequences of 2-6 signs on one sherd (fields s1..s6, internal sign ids; base-sign.json maps the
  42 base signs to internal ids), with occurrence counts.
