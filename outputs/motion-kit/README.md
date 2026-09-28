# Motion kit

Builds the Storylines videos (`outputs/motion-*`). Each folder's `content.py` holds the on-screen text and narration as source-checked claims, the animation code, the score, and the timing plan.

Four steps, in order:

```
python3 outputs/motion-kit/timing.py  outputs/motion-press-ban   # speak the narration offline, fit the timeline to 30s
python3 outputs/motion-kit/motion.py  outputs/motion-press-ban   # check every claim; write animation, page, manifest, narration script
python3 outputs/motion-kit/render.py  outputs/motion-press-ban   # render frames to video_silent.mp4 and poster.jpg
python3 outputs/motion-kit/audio.py   outputs/motion-press-ban   # score, narration, captions; mux video.mp4
```

- `timing.py`: speaks each narration line with the local Kokoro voice, measures it, and works out how long each segment of the animation should hold so every line and every screen of text has room. Writes `timing.json`.
- `motion.py`: fails if any quote or figure (on screen or spoken) can't be found in its article. Writes `animation.html`, `index.html`, `manifest.md`/`.html` and `narration.md`.
- `render.py`: drives headless Chromium frame by frame. `--stills 2,8,15` writes review frames instead.
- `audio.py`: synthesises the score in code, places the narration, ducks the music under it, normalises to -16 LUFS, writes `narration.vtt` captions and adds them to the MP4 as a subtitle track. `--png` draws a spectrogram with the cues marked.

The animations are authored on a short design timeline; `timing.json`'s warp stretches the holds, not the movement, so entrances keep their speed.

Fetched articles (`sources/`), the Storylines data and the narration clips stay out of the public repo, so a rebuild needs local copies.
