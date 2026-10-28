# Letter to the Portuguese ambassador in Rome, 24 April 1658 (Unsolved Catalogue no. 386)

Status: no write-up. Blocked on access: not digitised (ANTT, Condes da Ponte cx. 8 doc. MT-151; scans to order from the Torre do Tombo).

Blocked on images: the item is not digitised and has to be ordered from the Torre do Tombo. Nothing below
rests on a sight of the letter.

## The document

- ANTT, Arquivo dos Condes da Ponte, Caixa 8 (Mello e Torres), Doc. MT-151; reference code PT/TT/CPN/000210
  (old id ANTT9314640). DigitArq: https://digitarq.arquivos.pt/documentDetails/589eba945b114ea3a0b0ff7e71e14542
- Catalogue title (type ATTRIBUTED, so the archivist's, not the document's): "Carta ao embaixador do Rei de
  Portugal em Roma". Description, in full: "Parcialmente em cifra." Date 1658-04-24. Language: Italian.
  Writer and place not given.
- The record was harvested in the October 2026 Torre do Tombo sweep (`research/torre_do_tombo/details.jsonl`,
  `crawl_PT_TT_CPN.jsonl`). It was scored from the description alone.

## Access (checked 26 Oct 2026)

- `GET /api/docs/details/589eba945b114ea3a0b0ff7e71e14542`: `hasImages: false`, no dimensions, no
  physical description.
- `GET /api/rdigital/589eba945b114ea3a0b0ff7e71e14542`: `{"results":[],"total":0}`, so no scans.
- Not on DECODE. Of the 2,713 records in the Condes da Ponte crawl only 68 have images, and none of the
  related ones: the Orsini / Vieira da Silva cipher letters (CPN mç. 17 n.º 1, PT/TT/CPN/0017/00001, 1657-),
  the Rome letters of Gaspar Dias de Mesquita 1658-60 (mç. 20 n.º 1 and 2) and no other Caixa 8 item of
  1657-59.

## Context (from the catalogue and the literature, not from the letter)

- Portugal had no ambassador recognised by the Holy See in 1658. Francisco de Sousa Coutinho's mission to
  Rome ran 1655-1658 (Revista *Saeculum*, UFPB, 2026 article on Sousa Coutinho). He is the likeliest
  recipient on the date alone. That is unconfirmed.
- The letter sits in the papers of Francisco de Melo e Torres (later Conde da Ponte and Marquês de Sande), so
  it may be a copy or an intercept passed to him, not the original as received in Rome.
- Gaspar Dias de Mesquita wrote from Rome in 1658-60 (CPN mç. 20). He is a possible writer or a source of
  matching letters, but nothing here says he wrote this one.

## Prior art

None found. `known.py` (repo, DECODE, Cryptoole) gave no hit during the sweep. Web searches on 26 Oct 2026
(shelfmark, Condes da Ponte + Mello e Torres + cifra 1658, Portuguese envoy in Rome 1658 + cipher) found no
edition or decipherment. Still unchecked: *Teatro do Mundo: embaixadas e diplomacia em Roma durante a
Restauração portuguesa (1640-1671)* (2025), which may cite or calendar the Rome correspondence. Cryptiana has
no Portuguese 1650s page to grep.

## Remaining gaps

- The whole letter: needs-physical-access. Nothing can be transcribed, measured or attacked until the scans
  are ordered from ANTT. The system is undetermined.

## Escalation

- Siblings: the Orsini and Vieira da Silva cipher letters (mç. 17 n.º 1) and the Mesquita Rome letters
  (mç. 20) are the best chance of a shared key, a clear copy or a decipherment. None is digitised. Order them
  with MT-151.
- Clear pages: the letter is only "partly" in cipher, so its clear Italian may give a crib. That can be tried
  once it is imaged.
- Known keys: none for Portuguese Rome correspondence of the 1650s turned up on DECODE or Cryptoole.
- Print: check *Teatro do Mundo* (2025) and the Sousa Coutinho literature for a calendar of this letter.
- Next step: order reproductions of PT/TT/CPN/000210, PT/TT/CPN/0017/00001 and PT/TT/CPN/0020/00001-2 from
  the Torre do Tombo (DigitArq reproduction request). Then transcribe, count signs, try siblings, and only then
  a ciphertext-only attack with an Italian model from `lang/`, with a control at the same length.
