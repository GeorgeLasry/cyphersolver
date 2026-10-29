# The site's videos

Two narrated pixel-art videos, cut from the same scenes:

- the **front page's**, 36 seconds (the cipher, a short ledger, the whole contribute walkthrough): [`docs/hero.mp4`](../../docs/hero.mp4), poster [`docs/hero_poster.png`](../../docs/hero_poster.png);
- the **contribute page's**, under a minute, adding how the work is done, the headline counts and the paper:
  [`docs/hero_full.mp4`](../../docs/hero_full.mp4), poster [`docs/hero_full_poster.png`](../../docs/hero_full_poster.png).

Both open on a real cipher passage: the write-up's own photograph of it, then its figures deciphered group by group
against the key, then the English. The passage changes every week (`featured.json`). The narration is burned in as
captions, because the pages play the videos muted until someone asks for sound. Everything is made here: no stock
footage, music or recordings of people.

| File | What it is |
|---|---|
| `hero_video.py` | Draws every frame from code at 320×180, scales it 4× to 1280×720 and encodes it. `CUTS` holds each cut's scenes, narration times, chapters, page links and bars. The counts, the timeline dots and the entries the ledger names are read from `docs/index.html`; the passage from `docs/reveal/`. A render also writes the cut's chapters, links and a new `?v=` into its page. |
| `featured.json` | The passages the videos decipher, one an ISO week: token ranges in `docs/reveal/<slug>.json`, the write-up's snip of the same lines and its credit, the English, who wrote it and how it was read. |
| `assets.py` | The hand-made 5×7 pixel font and the sprites. |
| `vo.json` | The narration: each line's text, the spelling the voice model is given and the take used. When each cut speaks it is in `CUTS`. |
| `voice.py` | Renders the narration with Chatterbox (Resemble AI, MIT) in the voice of `narrator.wav`. |
| `narrator.wav` | The narrator's reference clip: a voice designed, not recorded, with OmniVoice (k2-fsa, weights CC BY-NC) from "female, middle-aged, low pitch, british accent". |
| `vo/` | The chosen take of each line, as FLAC. |
| `audio.py` | The original chiptune score and sound effects, built bar by bar from each cut's `bars`, mixed with the narration (the music ducks under the voice). |
| `loop.py` | A write-up page's short silent loop (pilot: Toledo 1565). |
| `docs/herovid.js` | The player on both pages: muted autoplay, sound, chapters, the link under the chapters for the stretch playing, and the buttons over the close. |

## Rebuilding

Pillow, numpy, scipy and ffmpeg are enough to rebuild from the committed takes. The soundtrack and the video must
decipher the same passage, so pass the same `--featured` to both when you choose one (by default both take this
ISO week's):

```bash
python tools/hero_video/audio.py hero_audio.wav
python tools/hero_video/hero_video.py --audio hero_audio.wav
python tools/hero_video/audio.py full_audio.wav --cut full
python tools/hero_video/hero_video.py --cut full --audio full_audio.wav
```

The counts are floored and shown with a "+" (520+ entries), so the videos stay true as the ledger grows.
`--sheet sheet.png` writes a contact sheet (one frame every 2 s) and `--still 6.5 frame.png` writes one frame, for
checking a change without encoding; `--featured SLUG` shows another passage; `--no-page` leaves the page alone.

A new featured passage needs: a reveal file with the passage read in full (no `?` groups), an image on its write-up
that shows those very lines (not another page of the same letter), and the English from the write-up. Check it with
`--featured SLUG --sheet`: short passages are drawn at twice the size, long ones in up to three rows.

## Keeping them current

Every render of the front-page cut writes `shown.json`: what the video puts on screen from the site (the rounded
counts, the timeline's span, the entries the ledger scene names, the catalogue's top cipher, the featured passage).
Every Monday, [`.github/workflows/hero-video.yml`](../../.github/workflows/hero-video.yml) runs `update.py`, which
compares that with the site. The featured passage changes each week, so in practice it re-renders both cuts weekly,
updates both pages, and opens a pull request for review; an older weekly update still open is closed as
superseded. Renders are deterministic for a given week and ledger. Run it by hand with
`python tools/hero_video/update.py` (report only) or `--render`, or start the workflow from the Actions tab.

Opening the pull request needs "Allow GitHub Actions to create and approve pull requests" (Settings → Actions →
General). Without it the job still pushes the branch and opens an issue linking to it.

The narration can't be redone in the workflow. Each line that speaks a number has a `holds` range in `vo.json`
(e.g. "over five hundred entries" holds from 500 to 1,000 entries). When the site's count leaves that range, the
workflow opens one issue, "Hero video: a narration line needs re-recording".

Changing the narration means rendering new takes, which needs a venv with `chatterbox-tts` and preferably a GPU:
edit `vo.json`, run `voice.py OUTDIR --only <id>`, and check each take with Whisper. Then copy the take you choose
into `vo/` as `<id>_<take>.flac`, set its `take`, and its time in each cut's `vo` list. If a line gets longer, move
the scene changes in `CUTS` (they sit on the score's bar lines: 96 bpm, 2.5 s a bar) and the cut's `bars` with them.
