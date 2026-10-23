# The Rosamonde telegrams, 1915–1916 (Sun Yat-sen and Soong Ching-ling)

Contributed result. Found, deciphered and edited by **Brice Dudout** with Claude (Opus 5.5), published at
<https://bdudout.github.io/wenmi/en/rosamonde.html> (CC BY 4.0; repository <https://github.com/bdudout/wenmi>).
He reported it by email on 15 Oct 2026 and sent the 6 and 7 March 1915 additions (20 → 22 telegrams) on
16 Oct 2026. On 15 Oct he agreed to cross-posting with attribution and to inclusion in the paper metadata. He says he
mainly uses Opus 5.5.

Outcome: key recovered from ciphertext-only (by the contributor); extent partial (three telegrams have unread words).
The project re-deciphered three telegrams from the scans; see "Check made here".

## The documents

From 1913 to 1917 the Communications Bureau of the Japanese Ministry of Communications copied the telegrams sent and
received by Sun Yat-sen's circle in Tokyo for the Foreign Ministry. The copies are in the Diplomatic Archives of the
MOFA of Japan, 1.6.1.4-2-1-2, 特定人ノ発受郵便物取調, digitised by JACAR:

- vol. 1, JACAR **B03050087600** (8 Jan – 11 Mar 1915): eleven telegrams, 17 Feb – 11 Mar 1915;
- vol. 1, JACAR **B03050087700** (Mar 1915 – Feb 1916): four telegrams, 12 Mar – 7 Jul 1915;
- vol. 3, JACAR **B03050089000** (29 Apr – 22 May 1916): seven telegrams, 1 – 13 May 1916.

Among the Chinese-code telegrams they form a separate family: ten-letter words of mixed letters with recurring groups
(hea, lyu, ound). The 1915 ones leave Tokyo in the name of 頭山滿 (Tōyama Mitsuru) for "Laisaosang, 445 Chaoufoong
Road" or "Rosamonde, 628 E. Yuhang Road", Shanghai; in 1916 they run between Shanghai and "Rosamonde Tokio". The
copies carry no translation. Related series, different systems: `targets/sunintercepts/` (the 1916–17 condenser
telegrams; docs/sunintercepts.html).

## The system and the key

English telegraphic text, no spaces, cut into ten-letter words, enciphered letter for letter by a **reciprocal
substitution** (the same table enciphers and deciphers):

    a-u  b-g  c-s  e-o  f-j  h-y  i-r  k-z  l-t  m-w  n-v  q-x    d and p unchanged

So *you* = hea, *love* = teno. One key from February 1915 to May 1916. Names, numbers, reply addresses and a few words
stay in clear (happy, Inuzuka, iron, trunk, know, own, Rosamonde, Porthos). The last word stops at ten letters, which
cuts *husba[nd]* on 4 and 12 May 1916. The 6 March 1915 form twice writes qq where pp is expected (rendered [pp]);
the contributor records this without changing the table.

How the key was found (contributor's page, "How we established it"): letter IC 0.062 (a language, not a code); f and q
absent; hea ×10. Simulated annealing over all 26-letter substitutions, then over reciprocal ones, scored by an English
quadgram model; control: English enciphered with a random key recovered at 100%. Out-of-sample check: the key taken
from the 1915 telegrams alone scores the 1916 forms (transcribed blind before the key was known) at z = 7.5 against
2,000 random reciprocal tables, Brice's blind re-transcription of 1915 at z = 10.9; a telegram in another system stays
at z = 0.6. No crib or outside plaintext is named. Hence `key recovered from ciphertext-only`.

Transcription: the forms (JACAR 200-dpi scans) were transcribed by Claude and independently by Brice, blind; 89% of
letters identical in the initial 20 texts. The two March additions were reviewed on a prefilled transcription (his R23).

## The telegrams

Readings are Brice Dudout's, quoted from his page. Square brackets: letters the form gives differently or leaves out
(he checked them on the images on 15 Oct 2026; mostly n/v, i/r, y/h, g/p, a/u, e/c cursive confusions); "…" not
deciphered.

| Date | From → to | Reading |
|---|---|---|
| 17 Feb 1915 | Tokyo → Laisaosang (Sun → Ching-ling) | Your letter [o]f the eight received. My life is [s]afe agai[n], I [ha]ve to thank you. Did you get my l[a]st cable? |
| 20 Feb 1915 | Tokyo → Rosamonde, 628 E. Yuhang Road, signed Hata | Must an[s]wer cable to Chu's yesterday. HATA |
| 21 Feb 1915 | Tokyo → Laisaosang | I am so happy, tha[n]k[s] to you. (*happy* in clear) |
| 23 Feb 1915 | Tokyo → Laisaosang | Yes, I'll save you or die myself if fail. But you must b[e] strong too. |
| 25 Feb 1915 | Tokyo → Laisaosang | With de[vou]t love I ask ye to throw of[f] Yung at once. If not I will surely die. I could throw of[f] … and sacrificed 100000 yu[a]n for you. Why are you [t]roubl[e] over a house a[n]d automobile? Now the [q]ues is: are you go[i]ng to cut h[i]m? |
| 26 Feb 1915 | Tokyo → Laisaosang | Whenever ye see Yung you inflict tor[t]ure [u]pon me, and the [p]ain will surely react on you more i[n]tens[e], for our souls are mingled i[n]to one. You can't esca[p]e. |
| 3 Mar 1915 | Tokyo → Laisaosang | Thirst[y] for hearing from you. An[s]wer. |
| 6 Mar 1915 | Tokyo → Laisaosang | I a[pp]rehend you going to desert me. Is it true? Tell definitely once for all to me. I shall a[pp]reciate you more for the honesty. |
| 7 Mar 1915 | Tokyo → Laisaosang | Why not give me comforts? |
| 9 Mar 1915 | Tokyo → Laisaosang (30 words) | [J]oy and ho[p]e return to me with your cable yes[ter]day. Many tha[n]k[s]. I just goin[g] … I a[m] well and sound usual. E[x]ecu[t]e your agreement at once, I b[i]d you [e]agerly. Your father su[r]prised me by a cal[l] t[h]is morni[ng]. (middle passage not deciphered) |
| 11 Mar 1915 | Tokyo → Laisaosang | What make ye cabled me so urgent yesterday? Re[p]ly by ci[p]her. Must write it at home, never do it in office, for [t]hey see. You don't use code book, so they can get our secrets by guessing. Write me often, [p]lease do. |
| 12 Mar 1915 | Tokyo → Laisaosang | Shall I tell father that you coming by Korea? Answ[er]. |
| 15 Mar 1915 | Tokyo → "Miss Nit", steamer Korea (wireless) | Who coming with you? Do father know when to meet ye? Are you land Kobe or Yoko? Re[p]ly [q]uick so that I may know what to do for your landing. Love. |
| 10 Jun 1915 | Tokyo → Laisaosang | Are you forgot me? Why not write and se[n]d the [p]hoto? |
| 7 Jul 1915 | Shanghai → Rosamonde, Tokio (Ching-ling → Sun) | Lovesick … in torture. Be merciful. Come or free me forever. |
| 1 May 1916 | Nagasaki → Rosamonde, Tokio (Sun → Ching-ling) | [In]te[n]s[e] love a[n]d ma[n]y k[is]ses to you. |
| 4 May 1916 | Shanghai → Rosamonde | Safel[y] la[n]d Fre[n]ch concess[i]on yesterday, no[w] very busy now. Love from devoted husba[nd]. |
| 8 May 1916 | Tokyo → "Junzaburo", Shanghai, form signed 中山 (Ching-ling → Sun, probable) | [I]s [i]t true y[o]u are going to Canton soon? |
| 10 May 1916 | Shanghai → Rosamonde | [I] not go to Canton. You can come here an[y] t[i]me, b[u]t do[n]'[t] take iro[n] trunk, leave [i]t to Mr Inuzuka's care. Do you understand? |
| 11 May 1916 | Shanghai → Rosamonde | D[a]rl[ing], have you [r]eceive cable a[sk] [y]ou to come he[r]e a[n]d do you know that iron trunk mus[t] be g[i]ve[n] to M[r] Inuzuka to take care. Love a[n]d k[is]ses to m[y] own w[i]f[e]. |
| 12 May 1916 | Shanghai → "Nakayama, 109 Harajuku, Tokio" | Cha[ng] K[i] [r]etur[n] Tok[i]o [i]s not true. D[i]d y[o]u [re]ceive two former ca[bl]es ask you to come back a[n]d g[i]ve the iro[n] tru[n]k [to] M[r] Inuzuka's [c]are? Have y[ou] done so? Fo[r] [I] [a]m very [anxi]ous about the t[r]unk, fo[r] [i]t [i]s ve[ry] d[an]ge[r]ou[s] fo[r] [y]ou to take [i]t yourself. Do [y]o[u] [q]uite cl[e]a[r] w[h]at [I] mea[n]? A[ns]wer at once. Husb[and]. (address Murai 317 Joffra) |
| 13 May 1916 | Tokyo → "Junzaburo", Shanghai, form signed 中山 (Ching-ling → Sun, probable) | [Pl]ease tell [T]ai h[i]s w[i]fe com[in]g also. Rosamonde. Porthos. |

Unless marked, 1915 Tokyo telegrams are Sun → Ching-ling and 1916 Shanghai/Nagasaki telegrams are Sun → Ching-ling.

## Attribution (contributor's argument)

No form names sender or recipient. "Rosamonde/Rosamond" is Soong Ching-ling's English name; in 1916 "Rosamonde Tokio"
is a telegraphic address of Sun's household. The fit: Ching-ling was in Shanghai from 28 Oct 1914 to 17 Mar 1915, and
the Tokyo → Shanghai run stops on 12 Mar, with the 15 Mar wireless to the steamer Korea that brought her back; she left
again on 3 May and the run resumes 10 Jun. Zhu Zhuowen ("Chu") wrote to Sun on 2 and 4 Feb 1915 that he had set up an
office for Miss Soong beside his own room (Zhu Jiulin 2016), which fits "cable to Chu's". On 9 Mar three clear
telegrams from Shanghai ask about Sun's health, one to Rosamonde signed "teno" (= love enciphered); Tokyo answers in
cipher "I am well and sound usual", and the next day Sun asks Shanghai in a condensed Chinese code what rumours are
going round about his safety. "Yung" is a suitor named in Charlie Soong's letter to Sun of 3 Aug 1915 (Yang Tianshi
2001). The May 1916 iron trunk and Porthos messages agree with Chinese-code telegrams in the same volume.
Soong Ching-ling married Sun on 25 Oct 1915, joined him in Shanghai 19 May 1916.

## What remains uncertain (contributor)

- About 45 of 750 letters corrected (6%) in the eleven complete telegrams of the initial 1915 sample.
- Eight words in the middle of 9 Mar 1915; one word on 25 Feb ("throw of[f] …") and the end of "de[vou]t"; one group
  on 7 Jul 1915.
- 1916 names: "Chang Ki" (Zhang Ji?), "Tai" (Dai Jitao?).
- "Laisaosang" and Yung's Chinese name are unidentified. Sender/recipient rest on cross-checks.
- Not found in the literature he checked (Bourdeau sunintercepts; Yang Tianshi 2001; Zhu Jiulin 2016; Chang & Halliday
  1986); other works not checked.

## Check made here (20 Oct 2026, Claude Opus 5.5)

Transcribed the cipher words of the three forms whose scans are in the contributor's repository
(`assets/img/rosamonde/`): 20 Feb 1915 (B03050087600 image 45), 26 Feb 1915 (image 52), 7 Jul 1915 (B03050087700
image 50). `ciphertext_checked.txt` (20 words, 200 letters, measured), `decipher.py` applies the key unchanged:

    wacluvcmoi sugtolesya chocloiduh        -> mustanswer cabletochu syesterday
    myovonoiho coohavbhea rvjtrsller ...    -> wheneverye seeyungyou inflicttoi tureabonme andthexain willsurely
                                               reactonyou moreintens foroursoul aremingled ietooneyou cantescabe
    tenocrszqu rvcleilaio gowoisrjat ...    -> lovesickxa instorture bemerciful comeorfree meforeverp

Agrees with his edition letter for letter, his bracketed corrections included (toi/tor[t], a for [u], x for [p],
e for [n], b for [p] in esca[p]e), and the unread "xa ins" of 7 July. Two small points: the scan gives *abon* (g, not p)
in "[u]pon", a second slip his brackets leave out, or a p read where this transcription sees g; and the cipher gives
"for our soul are mingled", where his edition prints "souls". `validation.tsv` + `docs/_validate.py`: pass
(z 7.9 vs random keys, 7.4 vs shuffled refit, 200 letters). The other 19 telegrams were not checked: their forms are not
in his repository and his cipher transcriptions are not published.

## Verification 3, 23 Oct 2026: the 1916 telegrams demoted

The v3 sweep flagged `outcome.texts[2]` (JACAR B03050089000, seven telegrams of May 1916). Its reading is the 1916
rows of Brice Dudout's table (`texts/readings_dudout.md`); scored alone they give **0.31 on explicit holes**, 0.25
plain, hole rate 0.48. 109 of their 627 letters (17%) are in brackets: letters the forms give differently (cursive and
transmission confusions n/v, i/r, y/h, g/p, a/u, e/c) supplied from sense. That is far over the 3% look-alike limit,
and nothing outside confirms them (the copies carry no translation; no cipher transcription of the 1916 forms is in
this repository). The entry is now **decoded, not read**. What would lift it: the 1916 forms transcribed from the
JACAR images and the confusions tested letter by letter against the key, as was done for 20 and 26 Feb and 7 Jul 1915.

## Remaining gaps
- 9 Mar 1915, eight cipher words in the middle of the 30-word telegram - blocker: illegible (transmission garble, per the contributor's check of the form; the form was not among frames 0163-0220 of B03050087600 inspected here 20 Oct 2026); not code groups but cipher words the known key does not turn into English (copying errors on the form, per the contributor); form not seen here, workable from JACAR B03050087600
- 25 Feb 1915, the word after "throw of[f]" and the end of "de[vou]t" - blocker: illegible (transmission garble). Checked here 20 Oct 2026 on B03050087600 p. 47 (frame 0209): the form is clear; the word is ejotrubuvd = of|eliag|and, five letters corrupt between "of" and "and"; "de[vou]t" is dogocl, n and a written g and c
- 7 Jul 1915, one group between "Lovesick" and "in torture" - blocker: illegible (transmission garble); key gives lovesickxa instorture, checked on image 50 here; the copy is corrupt at this point
- May 1916 telegrams (B03050089000), decoded, not read (v3 check 23 Oct 2026: 17% of letters emended look-alikes, 0.31 explicit holes) - blocker: illegible (copying and transmission confusions on the Japanese copies, as on the 1915 forms checked here; no translation on the copies to confirm the emended letters)

## Escalation
- [x] siblings: the contributor went through the 1915 volumes B03050087600/087700 and the May 1916 volume B03050089000; the 9 Mar clear telegrams and the Chinese-code telegrams of 10 Mar 1915 and 11-12 May 1916 were used as cross-checks
- [n/a] clear-pages: the copies carry no translation or decipherment; nothing to compare
- [n/a] known-keys: a single reciprocal key covers every telegram; there is no other key for this family to try
- [x] print: contributor checked Yang Tianshi 2001, Zhu Jiulin 2016, Chang & Halliday 1986 and the project's sunintercepts page; none prints these telegrams
- [n/a] key-rebuild: the key is complete (all 26 letters assigned); the open words fail on copying, not on the key
- [x] retry: 7 Jul retried on image 50; on 20 Oct 2026 B03050087600 was fetched and the 25 Feb form read (garbled word, see above); the 9 Mar form was not found in its frames 0163-0220

## Files

- `ciphertext_checked.txt`: the three telegrams transcribed here; `decipher.py`: the key; `validation.tsv`: letter pairs
  for `docs/_validate.py`.
- Page: `docs/rosamonde1915.html`; figure `docs/rosamonde1915_lead.jpg` (crop of B03050087600 image 52 from the
  contributor's repository); reveal `docs/reveal/rosamonde1915.json`.
