# Key notes -- joao1642 (ANTT MSLIV 1017), from letters 9 and 13 and the control on m0019

Evidence worked from: letter 9 (m0020) checked against its clear copy on m0021; letter 13 (m0024-25) checked
against the 'Carta inclusa' clear copy on m0025-26; letter 8 (m0019) with its 'Papel junto a dita carta'.

## The draft key holds

Every substitution in `key.py` is confirmed by the clear copies; no letter value had to be changed:

    a->o  b->g  c->e  d->f  e->c  f->E  g->d  h->b  i->a  l->p  m->z  n->i  o->u  p->g  q->s  r->r/v  s->n
    t->x  u->x/z  z->l

Words that carry the confirmation (cipher = plain, where seen):
- `pagetfofc` = liberdade (l.9 run 1; copy 'liberd.e')
- `aEℓinc` = Infante (l.9, passim; copy 'Inf.e')  -- see the sign note below
- `fxotnc` = Duarte; `atzoz` = irmam (copy 'irmão')
- `cieuintot` = encontrar; `gorrorcz` = passassem; `zoifotoz` = mandaram (copy 'mandarem')
- `crgoibucr` = Espanhoes (copy 'Hespanhois'); `gtalauicatur` = prizioneiros (copy 'prision.ros')
- `oxalu` = avizo; `eolu` = cazo; `rcdtcfu` = segredo; `crrciaop` = essencial; `eornepo` = Castela
- `xorroppo` = vassalla (l.13; copy 'vassalo'); `tadou` = Rigao; `puxtcieu` = Lourenco
- `Eutnolpolor` = fortalezas; `Euzcinoxo` = fomentava; `fareutfeor` = discordias (copy 'dissensoens')
- `ofzanatoz` = admitiram; `gtonaeor` = praticas; `ecrroeoz` = cessacam; `otzor` = armas
- `eotfcop` = cardeal; `rxeecrru` = sucesso; `zcpbut` = melhor; `euxlor` = couzas; `eotdu` = cargo
- `gcicatot` = penetrar; `oiazu` = animo; `zaiarntur` = ministros; `ofxctnatfcr` = advertirdes
- `gurraxcp` = possivel; `crnutxopu` = estorvalo; `opeoieor` = alcances; `cicinfcpfcr` = entenderdes
- `patdofo` = largada; `Etoiecrcr` = Franceses; `euzctcau` = comercio

## Additions and corrections

1. **`ft` = ElRei Christianissimo / ElRei de Franca.** Confirmed twice. Letter 9 run 1 `eotnor fc ft` is 'cartas de
   ElRei Christ.mo' in the clear copy (m0021); in run 2 the same `ft` answers to the copy's 'ElRei de Fr.a'. In
   letter 13 run A `sxc ft euiecfao` = 'q ElRei Christ.mo concedia'. So `ft` is one code group with both styles of
   the French king, not two.
2. **Crossed-circle symbol (+) = ElRei de Castela.** Already in `SYMBOLS`; the clear copy of letter 13 fixes it as
   'ElRei de Cast.a' in `fareutfeor euz (+)` = 'dissensoens com ElRei de Cast.a' and in `sxc (+) euinaixc` =
   'q ElRei de Cast.a continue'. In letter 9 run 2 the plain word 'Castela' is spelled out in cipher (`eornepo`)
   instead, so the symbol and the spelled form are alternatives, not a fixed usage.
3. **The Infante group `aEℓinc`.** 'Infante' is written a + looped E + a second tall looped letter + i + n + c.
   The second tall loop is the plain-f sign repeated for the -fante, i.e. the group is just a-f-a-n-t-e with the
   first vowel elided in writing; it always answers to 'Inf.e' in the copies. Transcribe it as one unit; it is not
   a separate code group.
4. **Clear abbreviations carried inside cipher.** The scribe sometimes enciphers an abbreviation rather than the
   full word: `cs` = 'e q(ue)' (l.13 l.27), `zx` = 'm.tas' (l.13 l.25, copy 'm.tas vezes'). The same hand also drops
   out of cipher mid-sentence for a familiar phrase (l.13 m0024 l.29 'pelo q vos encomendo, e encarrego' is in the clear).
5. **Homophones.** Only the two the draft key already has are in evidence: s = r or v (`xorroppo`, `rctoz`) and
   u/v = x or z. No new homophone appeared in either letter.
6. **No new code words.** Apart from `ft` and the (+) symbol, every proper name in these two letters is spelled out
   in the cipher alphabet: Duarte, Milam, Alemanha, Castela, Rigao, Sam Lourenco, Longavilha, Principe Thomas,
   the Cardeal (Richelieu), the Duque de O[..]a.

## Scribal traps confirmed (not key changes)

- **c / e** are nearly identical; most apparent nonsense resolves by swapping them (`guenu` for `guinu` = ponto,
  `ogctnuer` for `ogctnur` = apertos, `gtoncifcrner` for `gtcncifcrncr` = pretendestes).
- **t / z** and **r / x** are confused by the same hand (`ox` for `or` = as, `xur` / `xut`).
- **o / u** at word ends (`ou` for `au` = ao, `euins` for `euinu` = conta).
- Letters are occasionally transposed in copying: `auzctecu` for `euzctcau` = comercio, `octno` for `ectno` = certa.
- Word divisions are not reliable: `orcx` = 'o rcx' (a seu), `bcu` = 'bc u' (he o), `ogcrruo` = 'o gcrruo' (a pessoa),
  and conversely `gtu extot` = procurar is split.

## Control on m0019 (letter 8, 25 Oct 1642, with its 'Papel junto a dita carta')

Checked as a second witness; it contradicts nothing and adds no value:
- `u aEEoinc o rzppoz` (m0019, c. l.14) = 'o Infante a Millam' -- the same Infante group and the same spelling of
  Milam as in letter 9, with s written as r here and as z there (`o zoppoz`), i.e. the r/v homophone and the
  m/z letter both behave as in the key.
- `pagetfofc fu aEEoinc` = 'liberdade do Infante'; `gato nxfu` = 'para tudo'; `etcfanur` = 'creditos';
  `gbiafur` / `ancinovvcz` are the same hand's c/e and r/v slips over 'pondo' / 'intentarem' [?].
- The 'Papel junto' below is a clear paper on the same business (Lopo Ramires, broker in Amsterdam, brother of
  Duarte Nunes da Costa), not a word-for-word decipherment, so it checks vocabulary and names rather than letters.

## Contradictions / open points

- `gut urfe` (letter 9 run 2) reads 'por os de' against the copy's 'q os da'; the first group may be `s` + a flourish
  rather than `g`. Left doubtful.
- The duke's name in letter 9 run 3 (`u[..]o`, copy reads like 'Oria') is blotted on the scan; neither witness settles it.
- Letter 13's m0025 half-page is too faint for a letter-exact transcription of lines 3-5 and 12-16; the plaintext
  there is known from the clear copy on m0026, so nothing is lost for the reading, but the cipher text is not recorded.
