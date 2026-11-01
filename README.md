# Shalome & Tanmay — Save the Date

Interactive save-the-date for the wedding of Shalome & Tanmay: **March 5, 2027, Goa.** A formal invitation will follow.

**Live site:** https://tanmayhc7.github.io/ts_saveTheDate/

## How it works
1. Swipe right (or tap, or press Enter) to begin.
2. A short opening animation plays.
3. When it ends, a cloud fades in over the last frame. Scratch it to reveal the date.
4. The page glides to the invitation card, and soft music fades in (there's a mute button).

Works with touch, mouse and keyboard, and respects reduced-motion settings.

## Files
- `index.html` — the whole page (HTML, CSS and JavaScript, no build step)
- `assets/opening-video.mp4`, `assets/opening-video.webm` — opening animation
- `assets/scene.jpg`, `assets/intro.jpg`, `assets/card.jpg` — the painted artwork
- `assets/og-card.jpg`, `assets/icon-180.png` — link-preview image and home-screen icon
- `assets/background-music.mp3` — background music
- `assets/fonts/` — Cormorant, self-hosted
- `DESIGN.md` — colors, type, motion and the rules to keep when changing the design
- `PRODUCT.md` — what the page is for and who it's for

## Changing things
- **Music:** replace `assets/background-music.mp3` with another MP3 under about 5 MB, keeping the same file name.
- **Date or wording:** edit `index.html`, and update the link-preview tags at the top so shared links match.
- Do not move or rename files unless you also update the paths in `index.html`.

## Hosting
GitHub Pages, from the `Main` branch (**Settings → Pages → Deploy from a branch**). Keep `assets/` beside `index.html`.

## License
All rights reserved. See `LICENSE`.
