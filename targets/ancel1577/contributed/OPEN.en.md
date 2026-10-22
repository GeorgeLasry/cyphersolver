# Open points

## 1. Symbols not in Tomokiyo's table, or whose value is inferred
| symbol (token) | value used | evidence | status |
|---|---|---|---|
| m-shaped double sign (`m`) | uu / uv | p.33 "trouué" = margin "trouvé" | confirmed by contemporary decipherment (1 instance) |
| ʒ-like curl (`z`) | r | p.33 "decret" | 1 clear instance; elsewhere 3 (m) and ʒ (r) are not separable by shape (see section 2) |
| lone plain small c (`c`) | null | p.33 l.6, p.539 l.4, p.526 | inferred: never needed by the reading |
| flat L-like sign (`L`) | g | seigneur, Borgia, gendarmerie, magesté (p.561); also p.526 | inferred from 6+ words; not in Tomokiyo's table as drawn |
| q with crossbar (`ffx`) | ff | affaire, affection, officier (p.562), difficile (p.563), affoiblir (p.563) | Tomokiyo has "ff?"; confirmed by context |
| box-like q (`qq`) | nn | personnage, bonne, ordonné, connoistre | Tomokiyo's nn; confirmed by context |
| 4 with an extra bar (`gn` / `{gn?}`) | gn? | one instance on p.525 l.1 (first pass); the adjudicated transcription reads qq (nn) there: "connoistre" | resolved as qq in the adjudicated transcription; no independent gn instance |
| stem with an upper-right loop and lower-left bowl | r (context) | p.563 l.1, l.6, l.10; p.565 l.15 ("recevoir", "resolution", "attirer") | written "?"; value inferred from context only |
| three-bar stem with a top-right hook | e (context) | p.563 l.5 ("asseurement") | written "?"; one instance |
| cross in a cup | ? | p.562 l.3 and l.18 ("son fre?e") — looks like r in context, transcribed as VM? | unresolved |
| cross standing on a box (`dq`) | mm | p.562 l.8, p.563 l.7 "comme"; p.285 | Tomokiyo's mm. Two signs written "gn" in the second adjudication renamed dq (marked "?") |

## 2. Shape pairs that the two transcribers and the image adjudication could not separate
- 3 (m) vs ʒ (r): image-based changes to z gave non-words on p.525 (serblable, directerent, tellerent); kept 3 and marked "?" where the adjudicator could not decide.
- p (f) vs φ (m): image-based changes to φ gave non-words on p.525 (mait, maire, mrere, maut, merme); kept p and marked "?".
- qa (q) vs al (a): image-based changes to al gave non-words on p.526 (auon, auenuiron); kept qa and marked "?".
- oc (o) vs t4 (t) vs 4 (a): the recurring cross sign; Codex names it t4 or fl; the image adjudicators could not always decide; the reading o makes the words (vous, son, Monseigneur...). Marked "?" where undecided.
- 9 (d) vs q (l): tail length is a continuum; Codex reads q far more often. Marked "9?" where the tail is long.
- ∂ (i) vs δ (n): the main error of the first pass (p.525: about 35 corrected from the image).

These are listed per position in `xcheck/adjudication_img_<page>.tsv` (decision = ambiguous) and appear as uppercase letters in the key output.

## 3. Code words (plain-letter groups inside the cipher)
| group | proposed meaning | evidence | status |
|---|---|---|---|
| pur bellum | l'Electeur palatin | p.33 margin | confirmed (contemporary decipherment) |
| ucb+ (with smua, sec?) | l'Electeur de Saxe | p.33 margin | confirmed for the whole group; how it splits is open |
| saturnus | l'Empereur (Rudolf II) | on the calibration pages p.258 and p.285 the margin (five-reader majority) has "l'empereur" / "emper…" at the place of saturnus; p.440 margin "…ur" at the same place; p.525 "ledit seigneur [saturnus] son frere" | matches the contemporary decipherment on p.258 (one instance with exact anchors); p.285 and p.440 point the same way with weak anchors |
| Juno | le Roy d'Espagne (the King of Spain) | p.440: beside the cipher "… [que] {Juno} avoit voulu …" three independent readings of the margin (two Claude Sonnet 5.5 readers, Codex) agree on "le Roy d'Espaig[ne] … avoit … voulu" (`calib/codeword_juno_p440.txt`); fits p.561 "ou du dit [Juno] ou du dit seigneur Archiduc" | confirmed by contemporary decipherment (1 instance) |
| my | qu'il (my z = qu'ilz) | p.321: beside the cipher "il semble [my]z ayent en ceci intelligence" the margin is read "quelz? ay·u·?" by Codex and "quelz ay·en·" by Claude Sonnet 5.5 (`calib/readers/cwm_*.txt`); context: p.526 "sur ce [my] escrivit … [my] envoya", p.501 "celle [my] faut trouver", p.449 "tout haut [my]z veulent vivre" etc. | confirmed by contemporary decipherment (1 instance); many context instances |
| totum | l'Empire? | p.443 "les deputez de [totum] assemblez a Francfort", "des autres Estatz de [totum]"; p.258 margin "l'Empire et que" at "[mait totum] et que" | probable (margin reading uncertain) |
| mare, grinter (eviter) | persons or titles | p.443 "service du [mare]", "en la faveur du [mare]", "ledit [grinter] a fait des levées" | open |
| my3, my3θ, mine | my3 = qu'il (or que); my3θ = qu'ilz (θ = z); mine my3θ = du pis qu'ilz | p.258 margin: "que/qu'il" at "contributions [my3] demande", "du pis qu'ilz" at "seroient [mine my3θ] porroient" | my3θ confirmed (1 instance); mine alone open |
| nelluy benitow (p.258) | probably l'Electeur palatin et duc Casimir | p.258 margin "Loys Elect. Palatin et duc Casimir" beside these groups | probable (calibration page) |
| manua, manue | a person (Spanish side?) | p.561 "[manue] a dit", p.565 "le susdit [manua]" | open |
| Mitte (p.258) | "dauantage les autres"? | p.258 margin at the same place (anchors match, word boundaries uncertain) | open |
| principalem (p.258) | et principallement celuy | p.258 margin | confirmed (an abbreviation) |
| roe | pour (a variant of ros?) | p.258 margin: "pour" at "souvent [roe] la defense" | 1 instance |
| nez/mez, bel, mim | ? | deciphered letters p.439–501 (low-confidence alignments by Claude Sonnet 5.5; not included) | open |
| fec, sec, sanc, sane, pome, estre, toe, vib, roc, ar, puis, x | nulls (the reading never needs them) | absent from the margin decipherments where checked (p.33, p.258; sane pome on p.258) | probable |

## 4. Passages not read
- p.570 (one line, 22 symbols): the control is weak (4/1,000; 8/1,000 with table symbols only), but the last margin line of p.569 gives the contemporary decipherment "… quil ny reussiroit(?) peu ou point de proffit", which matches the key output (so it was not undeciphered). The verb in the margin is read "reussiroit" by Claude Sonnet 5.5 and Claude Opus 5.5 and "en sera" by Codex; not settled.
- p.539 l.2–3: "[my3θ] sont n'avoient charge" and "nonobstant que est · [saturnus] [sanc]" — syntax unclear around the code words.
- p.561 l.1–4 and l.18–19, p.562 l.25–26, p.565 l.9 and l.15–16: partly unreadable or code words.
- p.526 l.9–10, l.13–14: syntax unclear.
- Line ends cut by the binding shadow on p.562.

## 5. Not checked
- No human has checked the transcription or the images (see README).
- Dates: p.539 (2 Nov 1577), p.561 (14 Dec 1577), p.565 (21 Dec 1577), p.525–526 (22 Oct 1577, from the heading on p.523) are read from the page headings; sender attribution (Ancel) follows Tomokiyo's list and is not checked against the signatures.
