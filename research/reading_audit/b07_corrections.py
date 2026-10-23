"""b07 (lopehurtado1523): write the per-document corrections tables (<doc>_corrections.tsv) of the 22 Oct 2026 re-read.

    python research/reading_audit/b07_corrections.py
Each row: line, the tokens as transcribed before, as re-read on the full-resolution DECODE image, the reading they
give, and the evidence. Look-alike signs in this hand: the ß-like barred sign (a) was often transcribed ʇʇ (r);
`y ʇʇ` / `ʇʇʇ ʇʇ` is one sign ɣ̶ (g); the barred m (m̶) is f or c; ʒ is p (or h after m̶).
"""
import pathlib

T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'lopehurtado1523'

ROWS = {
    'R9869': [
        ('R1 l2', 'yuc ʇʇ ω 7 9 m', 'yuc ∠? ω 7 9 m', 'enviado', 'the sign after yuc is a crossed double stroke like ʇʇ; reads v here and in R8 l21 (envio); probable'),
        ('R1 l3', 'yob c', 'yob c', 'ducado(s)? (1522 key, probable)', 'not used in the reading: the words around it do not read'),
        ('R4 l7', 'zaf f ⊤ c ß 4', 'yaf f ⊤ c ß 4', 'escusan', 'image: yaf (es), not zaf; the clear word before is written su'),
        ('R7 l17', 'yub yal zar xab', 'yub yal zar rab', 'el exercito de V. Mt.', 'image: rab, not xab'),
        ('R7 l18', 'ʒul', 'zul', 'con', 'zul = con (key, confirmed): "con aparejo para sostener la guerra"'),
        ('R7 l18', 'y˙ 9 ʇʇ', 'y˙ 9 ʇʇ', '[?poder]', 'y˙ unvalued; slot "para [poder] en Francia" only'),
        ('R7 l20', 'ʃeg', 'ʃeg', '[?tengo]', 'ʃeg = tengo also in R9866 R14 "como tengo escrito"; probable'),
        ('R8 l21', 'yuc ʇʇ ω m', 'yuc ∠? ω m', 'envio', 'as R1 l2'),
        ('R8 l22', 'tul y m̶ 8 ε 8 ɣ̶ ω 9 m', 'tul ym 8 ε 8 ɣ̶ ω 9 m', 'quando fue elegido', 'image: y m without a bar = code ym (fue, key confirmed)'),
        ('R11 l5-6', 'quales / era (clear)', 'qual-/quiera', 'qualquiera', 'clear word divided at the line end'),
    ],
    'R9868': [
        ('R1 l6', 'zar ɣʇʇ ʇʇ ʇʇ b ω m ω f 7 ʇʇ ω 8', 'zar ɣ̶ ʇʇ ß b ω m̶ ω f 7 ʇʇ ω 8', '[?gratificarle]', 'image: ɣ̶ (g) and a ß-like a; the barred m = f; one i/l slip'),
        ('R7 l17', 'zad', 'zad (zed?)', '[?arçobispo]', 'clear ll. 1-3: the archbishop of Capua has left; zad/zed look-alike'),
        ('R8 l18', 'zil ʋ ω ʇʇ 9 m', 'zil m̶ ω ʇʇ 9 m', '[?confiado]', 'barred m = f; ʇʇ in the a slot'),
        ('R10 l3', 'zil m ω ß 9 m σ', 'zil m̶ ω ß 9 m σ', 'desconfiados', '"muy desconfiados"'),
        ('R11 l6', 'ʋ 8 4 m c ω 9 m c ω b ʇʇ 8 c', 'same', 'menos y dos y tres', '"al menos a dos y tres que son mas cerca de su Bt"'),
        ('R12 l9', 'f m ε m 4 ʇʇ', 'f m ε m 4 ß', 'Colona', 'last sign ß-like = a; the clear before reads "[e]staria mejor en"'),
        ('R13 l11', 'f ɣ ε 8 ɣʇʇ ω y4', 'f y ε 8 ɣ̶ ω y', 'colegio', 'y = o, ɣ̶ = g'),
        ('R13 l11', 'm ʇʇ 8 9 8 f 8 ε 8', 'm ʇʇʇ 8 9 8 f 8 ε 8', 'obedecele', 'three bars = b; m = o'),
        ('R13 l12', 'zu ∂ ʇʇ 4 c ∂ 8 ʇʇ m', 'zu ∂̶ ʇʇ m c ∂̶ 8 ʇʇ m', 'al Prospero', 'the 4 is m (o) on the image; ∂̶ = p'),
        ('R13 l12', 'ʃed ∂ ß 9 ʇʇ 8 tul 8 ʇʇ 7 ʇʇ ω ʇʇ', 'ʃed ∂̶ ß 9 ʇʇ 8 tul 8 ʇʇ 7 ~ʇʇ ω ʇʇ~', 'su padre quando era […]', 'the last three signs struck through by the writer'),
        ('R16 l16-17', 'toc zar f ʇʇ b ʇʇ z ω 7', 'toc zar f ʇʇ b ß z ω 7', '[…] de [?Catania]', 'the sign after b is ß-like (a); the first ʇʇ also read a'),
        ('R16 l18', '⊃ ʇʇ ʇʇ 8 f 8', '⊃ ß ʇʇ 8 f 8', 'parece', 'first sign ß-like (a)'),
        ('R16 l18', '⊃ m 9 ʇʇ ⊃ ton φ ß ʇʇ', 'same', '[?podria] quexar', 'ton φ ß ʇʇ = que-x-a-r, φ in the x slot; same group R17 l22'),
        ('R17 l19', 'zil c 8 ʇʇ φ ß ω 8', 'same', '[?conservarle]', 'one sign short'),
        ('R17 l21', 'y4 ⊤ ω b ß ʇʇ', 'same', '[?evitar]', 'y4 unvalued'),
        ('R17 l22', 'ʃu ∂ ⊤ σ 9 7 z', 'ʃu ⊃ ⊤ 8 9 7 z', 'se puedan', 'σ read 8 (e), ∂ read ⊃ (p)'),
    ],
    'R9866': [
        ('R1 l5', '∂̶ ⊃ 8 9 ω b m', 'f ρρ 8 9 ω b m', 'credito', 'image: first sign f (c), second ρρ-like (r)'),
        ('R1 l5-6', 'ʇʇ 4 | ε 7 4 ß 9 m', 'ß 4 | ε 7 4 ß 9 m', '[?an] [?allanado]', 'first sign ß-like (a); 4 in an l slot'),
        ('R3 l9', 'to ∂ 8 9 ω m tog ʒ y m̶ m c', 'same', 'no […] por pocos', 'ʒ = p, m̶ = c'),
        ('R3 l10', 'ti xer c 9 ω ʇʇ c', 'ti xer c 9 ω ß c', 'ni […] dias', 'ß-like (a)'),
        ('R3 l11', 'zil xer ʒ ß ε ʋ m zar b ω 8 φ ß', 'same', 'con […] palmo de [?tierra]', 'ʒ = p'),
        ('R4 l12', 'φ ω .j. m c', '⁝φ ω .j. m c', '[?Suiços]', 'a dotted φ opens the word'),
        ('R4 l12', '⊃ m 8 ʒ φ b ʇʇ m̶ ω m 4', 'same', '[?reputacion]', 'ʒ = p, ʇʇ in the a slot, m̶ = c; the first two signs stand for r'),
        ('R4 l13', '7 z m̶ m ʇʇʇ ʇʇ 7 9 m', 'same', 'an cobrado', 'm̶ = c'),
        ('R4 l13', '4 φ ω c ω 8 ʇʇ 8 z', 'ɋ φ ω c ω 8 ʇʇ 8 z', '[?quisieren]', 'first sign a barred 4 (q?)'),
        ('R5 l16', '⁝φ ʇʇ ʒ ʇʇ m φ 8 m̶ ʒ 7', '⁝φ ß ʒ ʇʇ m φ 8 m̶ ʒ 7', 'y aprovecha', 'first sign ß-like (a); m̶ʒ = ch'),
        ('R5 l17', 'zar zub', 'zar zub', 'de alla', 'zub = alla (1522 key, probable); "la costa de alla"'),
        ('R7 l23', 'm̶ m ε ω y ʇʇ 7 9 m c', 'm̶ m ε ω ɣ̶ 7 9 m c', 'coligados', 'y ʇʇ is one sign ɣ̶ (g)'),
        ('R7 l24', '8 z 8 ʋ ω y ʇʇ m c', '8 z 8 ʋ ω ɣ̶ m c', 'enemigos', 'as above'),
        ('R7 l24', '⊃ ⊃ 8 m̶ ω c b ω ʇʇ', 'same', 'resistir', 'the first pair stands for r'),
        ('R9 l7', 'ʃed xun ∂ ʇʇ y φ 8 7', 'same', 'su Magestad provea', '∂ = p'),
        ('R9 l8', 'ʃu ʇʇ zar φ 8 z 9 8 ʇʇ', 'ʃu ß zar φ 8 z 9 8 ʇʇ', 'se ha de vender', 'ß-like (a)'),
        ('R10 l10', '⁝φ ʃu ʒ 7 ɣ̶ ʇʇ φ 8', 'same', 'y se pague', 'ʒ = p'),
        ('R11 l11', 'm φ ω 8 c 8 xod m̶ ʒ y', 'same', 'oviese fecho', 'm̶ʒ = ch'),
        ('R11 l11', 'tu xil ε 7 ε b 7 T̄ ʇʇ z', 'same', 'no le [?faltaran]', 'the first ε in an f slot'),
        ('R13 l13-14', '⁝φ φ c m̶ 7 9 m ⁝φ ʇʇ T̄ c m̶ ß ʇʇ ω 7 z', 'same', 'y [?buscado] y [?buscarian]', 'φ and ʇʇ in the b slot'),
        ('R14 l17', 'zm ʃeg', 'zm ʃeg', '[?como] [?tengo]', 'zm = como (R9867 l21), ʃeg = tengo (R9869 R7); probable'),
        ('R14 l18', 'ʇʇ ʃed xun', 'ß ʃed xun', 'a su Magestad', 'ß-like (a)'),
    ],
    'R9867': [
        ('l01', 'zar ʃ ʇʇ', 'zar ♀? ß', '[?dexa]', 'a barred long sign read as x; probable only'),
        ('l07', 'sub ʃu xil c ʇʇ', 'sub ʃu xil c ß', 'si se les ha', 'ß-like (a)'),
        ('l09', 'ton co 8 ʇʇʇ ʇʇ φ 8', 'ton co 8 ɣ̶ φ 8', 'que [?lle]gue', 'ʇʇʇ ʇʇ is ɣ̶ (g); co unvalued'),
        ('l17', 'zu 7 ʇʇ ʇʇʇ ß ρρ', 'zu 7 ʇʇ ɣ̶ ß ρρ', 'alargar', 'ɣ̶ (g)'),
        ('l18-19', 'ʒφ ω 9 7 σ m ʇʇ', 'same', '[?cuidado]', 'ʒφ = cu?; one sign over'),
        ('l21', 'zm', 'zm', '[?como]', '"hare lo que suelo, como V. Mt. me lo a mandado"; also R9866 R14'),
        ('l23', 'zub', 'zub', '[?alla]', '1522 key, probable: "de lo que alla se me deve"'),
        ('l24', 'ʃφ ʇʇ φ 8 4 f 7', 'same', '[?verguença]', 'R9866 clear "tanto daño y verguença"'),
    ],
    'R9683': [
        ('a1-a2', 'zar ∂ 3 8 y 9 & eo α f m', 'same', 'de [?Theodorico]', '1522 sign values (& = o, key_1522_r9634.tsv); eo = r here; one word only'),
        ('a5', '∂ 8 sid', '9 e sid', 'de Sad', 'first sign 9-like (d)'),
        ('a5', 'zil c H ʇʇ φ ~ß~ ω &', 'same', 'con su [?servicio]', 'H = e (1522 confirmed), & = o; ß struck'),
        ('b1', 'ʃʇ ʇʇ ⊤ ï 7 σ', 'same', '[?cruzada]', 'ʃʇ = c?, ï = z?; one word only'),
    ],
    'R9667': [
        ('A', 'zar ɋ ɛ ʃ ʈ ʒ', 'zar ɣ Σ ʃ ϵ 8', 'declare', 're-read on the image: "el papa no se declare"'),
        ('A', 'tudd ɋ 8 x 7 7', 'tud∂ ɣ & ∂ 7', 'otra cosa', 'tud ~ tod (otro); & = o (1522)'),
        ('B', 'L 8 8 4 d 7 L tto', 'ɭb 8 4 ∂ 7 ∠ Ho', '[?pensava]', '1522 values ɭb = p, ∠ = v, Ho = a'),
        ('C', 'ton 8ʃ7 zar ɛ tin xon ʃu', 'ton 8 ʒ 7 zarε ton xon ʃu', 'que era del que mas se', 'ʒ = r (1522); zarε = del'),
        ('D', 'xiLd', 'xil ∂', 'les', 'xil = le + ∂ (s)'),
    ],
}

for doc, rows in ROWS.items():
    with open(T / f'{doc}_corrections.tsv', 'w', encoding='utf-8', newline='\n') as f:
        f.write('line\ttranscribed\tre-read on the image\treading\tevidence\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
print('written', len(ROWS))
