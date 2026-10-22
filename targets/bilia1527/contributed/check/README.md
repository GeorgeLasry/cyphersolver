# 画像による確かめ / Image checks

- round1/：1回目の書き起こしと Codex の読みが食い違った51か所（disagreements_v1.tsv）を、行画像で OpenAI Codex（codex.txt）と Claude Sonnet（sonnet.txt）に別々に判定させたもの。questions.txt の候補 A・B の順番はばらばら（key_AB.tsv）。verdict.tsv が結果（直す／直さない／未決）。 / 51 disagreements judged separately by Codex and Sonnet on line images.
- round2/：round1 で割れた22か所を、原寸から切った3分割の拡大画像でもう一度判定させたもの。 / The 22 split places judged again on enlarged thirds.
- 直したのは、2つの判定がそろって Codex の読みを選んだ所だけ。 / A place was corrected only when both judges chose the Codex reading.
- 位置（pos）は、その回の書き起こしの行内の順番。 / Positions are within-line positions in the transcription of that round.
