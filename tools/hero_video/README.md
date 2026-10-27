# Front-page hero video

The one-minute narrated pixel-art video at the top of the front page: [`docs/hero.mp4`](../../docs/hero.mp4), with
its poster frame [`docs/hero_poster.png`](../../docs/hero_poster.png). Everything in it is made here: no stock
footage, music or recordings of people.

| File | What it is |
|---|---|
| `hero_video.py` | Draws every frame from code at 320×180, scales it 4× to 1280×720 and encodes it. `SCENES` holds the timing. The counts and the timeline dots are read from `docs/index.html`. |
| `assets.py` | The hand-made 5×7 pixel font, the stand-in cipher signs and the sprites. |
| `vo.json` | The narration: each line's text, the spelling the voice model is given, the take used and when it starts. |
| `voice.py` | Renders the narration with Chatterbox (Resemble AI, MIT) in the voice of `narrator.wav`. |
| `narrator.wav` | The narrator's reference clip: a voice designed, not recorded, with OmniVoice (k2-fsa, weights CC BY-NC) from "female, middle-aged, low pitch, british accent". |
| `vo/` | The chosen take of each line, as FLAC. |
| `audio.py` | The original chiptune score and sound effects, mixed with the narration (the music ducks under the voice). |

## Rebuilding

Pillow, numpy, scipy and ffmpeg are enough to rebuild from the committed takes:

```bash
python tools/hero_video/audio.py hero_audio.wav
python tools/hero_video/hero_video.py --audio hero_audio.wav
```

The counts are floored and shown with a "+" (520+ entries), so the video stays true as the ledger grows.
`--sheet sheet.png` writes a contact sheet (one frame every 2 s) and `--still 21.5 frame.png` writes one frame, for
checking a change without encoding.

## Keeping it current

Every render writes `shown.json`: what the video puts on screen from the site (the rounded counts, the timeline's
span, the catalogue's top cipher). Every Monday, [`.github/workflows/hero-video.yml`](../../.github/workflows/hero-video.yml)
runs `update.py`, which compares that with the site. If anything has moved, it re-renders the video, bumps the
`?v=` on its source in `docs/index.html`, and opens a pull request for review; an older weekly update still open is
closed as superseded. Renders are deterministic, so an unchanged ledger gives an identical file. Run it by hand with
`python tools/hero_video/update.py` (report only) or `--render`, or start the workflow from the Actions tab.

Opening the pull request needs "Allow GitHub Actions to create and approve pull requests" (Settings → Actions →
General). Without it the job still pushes the branch and opens an issue linking to it.

The narration can't be redone in the workflow. Each line that speaks a number has a `holds` range in `vo.json`
(e.g. "over five hundred entries" holds from 500 to 1,000 entries). When the site's count leaves that range, the
workflow opens one issue, "Hero video: a narration line needs re-recording".

Changing the narration means rendering new takes, which needs a venv with `chatterbox-tts` and preferably a GPU:
edit `vo.json`, run `voice.py OUTDIR --only <id>`, and check each take with Whisper. Then copy the take you choose
into `vo/` as `<id>_<take>.flac` and set its `take` and `at`. If a line gets longer, move the scene changes in
`SCENES` (they sit on the score's bar lines: 96 bpm, 2.5 s a bar).
