# QRG – QR Game Engine

> Verified game note.

![QRG – QR Game Engine screenshot](https://raw.githubusercontent.com/TylusKinas/QRG/main/docs/img/breakout.gif)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 4.4/10 ([manually reviewed image](https://github.com/TylusKinas/QRG/blob/main/docs/img/breakout.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/TylusKinas/QRG](https://github.com/TylusKinas/QRG)
- **Evidence:** [direct model evidence](https://github.com/TylusKinas/QRG/commit/d671d3a6c556b9698dfc92ba96653606840294df)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/TylusKinas/QRG/blob/main/docs/img/breakout.gif) — 📸 4.4/10 · manual visual review · Use this frame for the game-level score. Tiny Breakout board with coloured brick rows and paddle; minimal.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

QRG – a whole game in one QR code. Scan it with any phone camera and play instantly in the browser: no app, no server. Retro 256×240 console, JavaScript engine, custom compressor, visual & code editors, sandboxed games, per-game save memory, offline PWA.… Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/TylusKinas/QRG/blob/main/src/editor/visual-compile.js](https://github.com/TylusKinas/QRG/blob/main/src/editor/visual-compile.js)
- [https://github.com/TylusKinas/QRG/commit/d671d3a6c556b9698dfc92ba96653606840294df](https://github.com/TylusKinas/QRG/commit/d671d3a6c556b9698dfc92ba96653606840294df)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/TylusKinas/QRG

[Back to the awesome list](../../README.md)
