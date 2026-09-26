"""Render a motion folder's animation.html to video.mp4 (1920x1080, H.264) and poster.jpg.

Usage: python3 outputs/motion-kit/render.py outputs/<motion-folder> [--fps 60] [--stills 1.0,4.2,...]

Drives headless Chromium frame by frame (each frame is a pure function of
time, so nothing depends on how fast the machine is) and pipes the frames to
ffmpeg. --stills writes PNG frames at the given times to stills/ for review
instead of rendering the video.
"""
import argparse
import pathlib
import subprocess

from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("folder")
ap.add_argument("--fps", type=int, default=60)
ap.add_argument("--stills")
ap.add_argument("--poster", type=float, default=None)
ap.add_argument("--poster-only", action="store_true")
args = ap.parse_args()

folder = pathlib.Path(args.folder).resolve()
url = (folder / "animation.html").as_uri() + "?render"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
    page.goto(url)
    page.wait_for_function("READY === true")
    duration = page.evaluate("DURATION")

    def shot(t, **kw):
        page.evaluate(f"renderAt({t})")
        return page.screenshot(clip={"x": 0, "y": 0, "width": 1920, "height": 1080}, **kw)

    if args.stills:
        out = folder / "stills"
        out.mkdir(exist_ok=True)
        for t in [float(x) for x in args.stills.split(",")]:
            (out / f"t{t:05.2f}.png").write_bytes(shot(t))
        print("stills written to", out)
    elif args.poster_only:
        pt = args.poster if args.poster is not None else page.evaluate("typeof POSTER_T !== 'undefined' ? POSTER_T : 1.5")
        (folder / "poster.jpg").write_bytes(shot(pt, type="jpeg", quality=88))
        print("wrote poster.jpg")
    else:
        n = round(duration * args.fps)
        ff = subprocess.Popen(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(args.fps), "-c:v", "mjpeg",
             "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
             "-movflags", "+faststart", "-r", str(args.fps), str(folder / "video.mp4")],
            stdin=subprocess.PIPE)
        for i in range(n):
            ff.stdin.write(shot(i / args.fps, type="jpeg", quality=95))
            if i % args.fps == 0:
                print(f"  {i / args.fps:4.1f}s", flush=True)
        ff.stdin.close()
        ff.wait()
        pt = args.poster if args.poster is not None else page.evaluate("typeof POSTER_T !== 'undefined' ? POSTER_T : 1.5")
        (folder / "poster.jpg").write_bytes(shot(pt, type="jpeg", quality=88))
        print("wrote", folder / "video.mp4", "and poster.jpg")
    browser.close()
