# XL Chess

> Verified game note.

![XL Chess screenshot](https://raw.githubusercontent.com/Momonimome/xl-chess/main/docs/screenshot.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 5.2/10 ([manually reviewed image](https://github.com/Momonimome/xl-chess/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/Momonimome/xl-chess](https://github.com/Momonimome/xl-chess)
- **Evidence:** [direct model evidence](https://github.com/Momonimome/xl-chess/commit/fe6970da6cd37bcb43c46edc4767e105efd7ee9f)
- **Live demo:** [open demo](https://momonimome.github.io/xl-chess/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Momonimome/xl-chess/blob/main/docs/screenshot.png) — 📸 5.2/10 · manual visual review · Use this frame for the game-level score. Plain chess board with settings panel; clean and readable, minimal.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Chess game and engine in plain JavaScript: alpha-beta search in a Web Worker, verified against python-chess and perft. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Momonimome/xl-chess/blob/main/src/engine/position.js](https://github.com/Momonimome/xl-chess/blob/main/src/engine/position.js)
- [https://github.com/Momonimome/xl-chess/commit/fe6970da6cd37bcb43c46edc4767e105efd7ee9f](https://github.com/Momonimome/xl-chess/commit/fe6970da6cd37bcb43c46edc4767e105efd7ee9f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/Momonimome/xl-chess

[Back to the awesome list](../../README.md)
