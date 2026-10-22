# f150: decoder output with key_contrib.json

Saved output of `KEY=key_contrib.json python dec.py f150_cipher.txt` (run 22 Oct 2026; the same decoder and key that
`measure.py --key key_contrib.json` scores, 21 Oct 2026). Raw machine decode: the first block is the joined,
word-segmented text, then one numbered line per manuscript line. Unkeyed tokens (`BOX`, `?`, unknown codes)
take whatever letter the language model prefers and are not read; `+`/`*` mark code groups. The prose
reading of the leaf, where one exists, is in the `f*_reading.md` file.

```
l n pour + qui le le uuis est faire si ce n est que l un et l aultre es coste nt trou uolontiers leur auens qui ne soul droient le m+nes point de compai en v ostre et le m autres point de superieur m+r ie uous en aisoul+ escrire lui n toire au aray affin que s ils en car le car de la me il se pour a fair i uous soye uni informe de la +er ete de faict qui est dieumercy ua se a see doucement encores qu ilyeust grande a re rance du contre ire i en auois point uue se d auoir encores dens seruin en ceste ar mi nostre en u en ie estime auoir au con ement a mien en es paiges me peut te sire il la le uous confe seront une our et l un et l aultre +r

1 l n pour + qui le le uuis est faire si ce n est que l un
2 et l aultre es coste nt trou uolontiers leur a
3 uens qui ne soul droient le m+nes point de compai
4 en v ostre et le m autres point de superieur m+r ie uous en
5 aisoul+ escrire lui n toire au aray affin que s ils en
6 car le car de la me il se pour a fair i uous soye uni i
7 n forme de la +er ete de faict qui est dieumercy
8 ua se a see doucement encores qu ilyeust grande
9 a re rance du contre ire i en auois point uue sedau
10 oir encores dens seruin en ceste ar mi nostre en ueni
11 e estime auoir au con ement a mien en espa ig
12 es me peut te sire il la le uous confe seront une
13 our et l un et l aultre +r
```
